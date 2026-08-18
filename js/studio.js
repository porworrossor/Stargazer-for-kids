/**
 * Constellation Studio & Customizer - Core Application Logic
 */

class ConstellationStudio {
  constructor() {
    this.data = JSON.parse(JSON.stringify(CONSTELLATIONS_DATA));
    this.currentIndex = 0;
    this.selectedStarId = null;
    this.lineStartStarId = null;
    this.isDragging = false;
    this.draggedStarId = null;

    // View Options
    this.viewOptions = {
      showGrid: true,
      showLabels: true,
      showArt: true,
      showGlow: true,
      showLines: true
    };

    this.currentViewMode = 'studio'; // 'studio' or 'gallery'

    this.init();
  }

  init() {
    // Starfield Background
    if (typeof CosmicStarfield !== 'undefined') {
      new CosmicStarfield('starfield-canvas');
    }

    this.buildZodiacChips();
    this.bindEvents();
    this.loadConstellation(0);
  }

  buildZodiacChips() {
    const nav = document.getElementById('zodiac-nav-bar');
    nav.innerHTML = '';

    this.data.forEach((c, idx) => {
      const chip = document.createElement('button');
      chip.className = `zodiac-chip ${idx === 0 ? 'active' : ''}`;
      chip.dataset.index = idx;
      chip.innerHTML = `
        <span class="chip-symbol">${c.symbol}</span>
        <span class="chip-name">${c.thaiName}</span>
      `;
      chip.addEventListener('click', () => {
        document.querySelectorAll('.zodiac-chip').forEach(el => el.classList.remove('active'));
        chip.classList.add('active');
        if (this.currentViewMode === 'gallery') {
          this.switchViewMode('studio');
        }
        this.loadConstellation(idx);
      });
      nav.appendChild(chip);
    });
  }

  bindEvents() {
    // View Mode Toggle (Studio vs Gallery)
    document.getElementById('btn-mode-studio').addEventListener('click', () => this.switchViewMode('studio'));
    document.getElementById('btn-mode-gallery').addEventListener('click', () => this.switchViewMode('gallery'));

    // Canvas Tool Toggles
    const toggleButtons = [
      { id: 'toggle-grid', key: 'showGrid' },
      { id: 'toggle-labels', key: 'showLabels' },
      { id: 'toggle-art', key: 'showArt' },
      { id: 'toggle-glow', key: 'showGlow' },
      { id: 'toggle-lines', key: 'showLines' }
    ];

    toggleButtons.forEach(({ id, key }) => {
      const btn = document.getElementById(id);
      if (btn) {
        btn.addEventListener('click', () => {
          this.viewOptions[key] = !this.viewOptions[key];
          btn.classList.toggle('active', this.viewOptions[key]);
          this.renderStudioSVG();
          if (this.currentViewMode === 'gallery') this.renderGalleryGrid();
        });
      }
    });

    // Inspector Tabs
    document.querySelectorAll('.inspector-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.inspector-tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        const tabId = btn.dataset.tab;
        document.getElementById(`tab-${tabId}`).classList.add('active');
      });
    });

    // Add New Star Button
    document.getElementById('btn-add-star').addEventListener('click', () => this.addNewStar());

    // Connect Lines Button
    document.getElementById('btn-connect-line').addEventListener('click', () => this.connectSelectedStars());

    // Live SVG Code Editor Input
    const svgEditor = document.getElementById('svg-art-textarea');
    svgEditor.addEventListener('input', () => {
      const current = this.data[this.currentIndex];
      current.artOverlay = svgEditor.value;
      this.renderStudioSVG();
    });

    // Copy JS Code
    document.getElementById('btn-copy-code').addEventListener('click', () => this.copyCodeToClipboard());
    document.getElementById('btn-download-js').addEventListener('click', () => this.downloadJSFile());

    // SVG Drag & Drop and Mouse Movement
    this.setupSVGInteractions();
  }

  switchViewMode(mode) {
    this.currentViewMode = mode;
    const studioSection = document.getElementById('studio-main-workspace');
    const gallerySection = document.getElementById('gallery-main-view');

    if (mode === 'studio') {
      document.getElementById('btn-mode-studio').classList.add('active');
      document.getElementById('btn-mode-gallery').classList.remove('active');
      studioSection.style.display = 'grid';
      gallerySection.classList.remove('active');
      this.loadConstellation(this.currentIndex);
    } else {
      document.getElementById('btn-mode-gallery').classList.add('active');
      document.getElementById('btn-mode-studio').classList.remove('active');
      studioSection.style.display = 'none';
      gallerySection.classList.add('active');
      this.renderGalleryGrid();
    }
  }

  loadConstellation(index) {
    this.currentIndex = index;
    this.selectedStarId = null;
    this.lineStartStarId = null;

    const current = this.data[index];

    // Update Header
    document.getElementById('studio-constellation-title').textContent = `${current.symbol} ${current.thaiName} (${current.latinName})`;
    document.getElementById('studio-zodiac-name').textContent = current.zodiacName;

    // Render Canvas
    this.renderStudioSVG();

    // Populate Inspector Panels
    this.populateStarsInspector();
    this.populateLinesInspector();
    this.populateArtOverlayInspector();
    this.populateMetadataInspector();
  }

  renderStudioSVG() {
    const current = this.data[this.currentIndex];
    const svg = document.getElementById('studio-svg-stage');
    svg.setAttribute('viewBox', current.viewBox || '0 0 500 400');
    svg.innerHTML = '';

    // 1. Grid & Coordinates Layer
    if (this.viewOptions.showGrid) {
      const gridG = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      gridG.setAttribute('class', 'grid-layer');
      
      // Vertical lines every 50px
      for (let x = 50; x < 500; x += 50) {
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', x);
        line.setAttribute('y1', 0);
        line.setAttribute('x2', x);
        line.setAttribute('y2', 400);
        line.setAttribute('class', 'grid-line');
        gridG.appendChild(line);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', x + 3);
        text.setAttribute('y', 14);
        text.setAttribute('class', 'axis-text');
        text.textContent = x;
        gridG.appendChild(text);
      }

      // Horizontal lines every 50px
      for (let y = 50; y < 400; y += 50) {
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', 0);
        line.setAttribute('y1', y);
        line.setAttribute('x2', 500);
        line.setAttribute('y2', y);
        line.setAttribute('class', 'grid-line');
        gridG.appendChild(line);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', 4);
        text.setAttribute('y', y - 4);
        text.setAttribute('class', 'axis-text');
        text.textContent = y;
        gridG.appendChild(text);
      }

      svg.appendChild(gridG);
    }

    // 2. Art Overlay Layer
    if (this.viewOptions.showArt && current.artOverlay) {
      const artG = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      artG.setAttribute('id', 'studio-art-overlay');
      artG.innerHTML = current.artOverlay;
      svg.appendChild(artG);
    }

    // 3. Lines Layer
    if (this.viewOptions.showLines && current.lines) {
      const linesG = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      linesG.setAttribute('id', 'studio-lines-group');

      const starMap = new Map();
      current.stars.forEach(s => starMap.set(s.id, s));

      current.lines.forEach(([s1Id, s2Id]) => {
        const s1 = starMap.get(s1Id);
        const s2 = starMap.get(s2Id);
        if (s1 && s2) {
          const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          line.setAttribute('x1', s1.x);
          line.setAttribute('y1', s1.y);
          line.setAttribute('x2', s2.x);
          line.setAttribute('y2', s2.y);
          line.setAttribute('stroke', '#00F0FF');
          line.setAttribute('stroke-width', '2.5');
          line.setAttribute('stroke-linecap', 'round');
          line.setAttribute('opacity', '0.85');
          line.setAttribute('filter', 'drop-shadow(0 0 6px rgba(0, 240, 255, 0.6))');
          linesG.appendChild(line);
        }
      });

      svg.appendChild(linesG);
    }

    // 4. Stars Layer
    const starsG = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    starsG.setAttribute('id', 'studio-stars-group');

    current.stars.forEach(s => {
      // Glow Ring
      if (this.viewOptions.showGlow && s.bright) {
        const glow = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        glow.setAttribute('cx', s.x);
        glow.setAttribute('cy', s.y);
        glow.setAttribute('r', (s.r || 6) * 2.2);
        glow.setAttribute('fill', s.color || '#00F0FF');
        glow.setAttribute('opacity', '0.35');
        glow.setAttribute('filter', 'drop-shadow(0 0 8px ' + (s.color || '#00F0FF') + ')');
        starsG.appendChild(glow);
      }

      // Main Node Circle
      const starCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      starCircle.setAttribute('cx', s.x);
      starCircle.setAttribute('cy', s.y);
      starCircle.setAttribute('r', s.r || 7);
      starCircle.setAttribute('fill', s.color || '#FFFFFF');
      starCircle.setAttribute('class', `star-node ${s.id === this.selectedStarId ? 'selected' : ''}`);
      starCircle.dataset.starId = s.id;

      // Click to select
      starCircle.addEventListener('click', (e) => {
        e.stopPropagation();
        this.selectStar(s.id);
      });

      starsG.appendChild(starCircle);

      // Star Label
      if (this.viewOptions.showLabels) {
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', s.x + (s.r || 7) + 4);
        text.setAttribute('y', s.y + 4);
        text.setAttribute('class', 'star-label');
        text.textContent = s.bayer || s.name || `Star #${s.id}`;
        starsG.appendChild(text);
      }
    });

    svg.appendChild(starsG);
  }

  setupSVGInteractions() {
    const svg = document.getElementById('studio-svg-stage');
    const coordDisplay = document.getElementById('mouse-coords-readout');

    // Mouse Move tracker & drag handler
    svg.addEventListener('mousemove', (e) => {
      const rect = svg.getBoundingClientRect();
      const scaleX = 500 / rect.width;
      const scaleY = 400 / rect.height;
      const svgX = Math.round((e.clientX - rect.left) * scaleX);
      const svgY = Math.round((e.clientY - rect.top) * scaleY);

      if (coordDisplay) {
        coordDisplay.textContent = `X: ${Math.max(0, Math.min(500, svgX))}, Y: ${Math.max(0, Math.min(400, svgY))}`;
      }

      if (this.isDragging && this.draggedStarId !== null) {
        const current = this.data[this.currentIndex];
        const star = current.stars.find(s => s.id === this.draggedStarId);
        if (star) {
          star.x = Math.max(10, Math.min(490, svgX));
          star.y = Math.max(10, Math.min(390, svgY));
          this.renderStudioSVG();
          this.updateStarRowInput(star);
        }
      }
    });

    // Mouse Down on star node
    svg.addEventListener('mousedown', (e) => {
      const target = e.target.closest('.star-node');
      if (target) {
        this.isDragging = true;
        this.draggedStarId = parseInt(target.dataset.starId, 10);
        this.selectStar(this.draggedStarId);
      }
    });

    // Mouse Up
    window.addEventListener('mouseup', () => {
      if (this.isDragging) {
        this.isDragging = false;
        this.draggedStarId = null;
      }
    });
  }

  selectStar(starId) {
    this.selectedStarId = starId;
    this.renderStudioSVG();

    // Highlight row in inspector
    document.querySelectorAll('.star-edit-row').forEach(row => {
      row.classList.toggle('selected', parseInt(row.dataset.starId, 10) === starId);
    });

    // Auto-select dropdown in Lines Tab
    const select1 = document.getElementById('line-select-star1');
    const select2 = document.getElementById('line-select-star2');
    if (select1 && !select1.value) {
      select1.value = starId;
    } else if (select2 && select1.value != starId) {
      select2.value = starId;
    }
  }

  populateStarsInspector() {
    const list = document.getElementById('stars-data-list');
    list.innerHTML = '';
    const current = this.data[this.currentIndex];

    // Populate dropdowns for line adding
    const s1Select = document.getElementById('line-select-star1');
    const s2Select = document.getElementById('line-select-star2');
    s1Select.innerHTML = '<option value="">เลือกดาวดวงแรก...</option>';
    s2Select.innerHTML = '<option value="">เลือกดาวดวงที่สอง...</option>';

    current.stars.forEach(s => {
      // Add to select options
      const opt1 = document.createElement('option');
      opt1.value = s.id;
      opt1.textContent = `#${s.id} - ${s.bayer || s.name}`;
      s1Select.appendChild(opt1);

      const opt2 = document.createElement('option');
      opt2.value = s.id;
      opt2.textContent = `#${s.id} - ${s.bayer || s.name}`;
      s2Select.appendChild(opt2);

      // Star Row Card
      const row = document.createElement('div');
      row.className = `star-edit-row ${s.id === this.selectedStarId ? 'selected' : ''}`;
      row.dataset.starId = s.id;
      row.innerHTML = `
        <div class="star-row-header">
          <span class="star-badge">⭐ #${s.id} ${s.name} (${s.bayer || '-'})</span>
          <button class="tool-toggle-btn btn-delete-star" title="ลบดาวดวงนี้" style="color: var(--accent-coral); padding: 2px 8px;">ลบ 🗑️</button>
        </div>
        <div class="star-inputs-grid">
          <div class="input-field-group">
            <label>X (พิกัด)</label>
            <input type="number" class="studio-input in-star-x" value="${s.x}" min="0" max="500">
          </div>
          <div class="input-field-group">
            <label>Y (พิกัด)</label>
            <input type="number" class="studio-input in-star-y" value="${s.y}" min="0" max="400">
          </div>
          <div class="input-field-group">
            <label>R (ขนาด)</label>
            <input type="number" class="studio-input in-star-r" value="${s.r || 7}" step="0.5" min="2" max="25">
          </div>
          <div class="input-field-group">
            <label>สีดาว</label>
            <input type="color" class="studio-input in-star-color" value="${s.color || '#FFFFFF'}" style="padding: 2px; height: 28px;">
          </div>
          <div class="input-field-group">
            <label>ความสว่าง (Mag)</label>
            <input type="number" class="studio-input in-star-mag" value="${s.mag || 3.0}" step="0.1">
          </div>
        </div>
        <div class="star-inputs-grid" style="grid-template-columns: 1.5fr 1fr;">
          <div class="input-field-group">
            <label>ชื่อภาษาไทย</label>
            <input type="text" class="studio-input in-star-name" value="${s.name || ''}">
          </div>
          <div class="input-field-group">
            <label>รหัส Bayer</label>
            <input type="text" class="studio-input in-star-bayer" value="${s.bayer || ''}">
          </div>
        </div>
      `;

      // Live inputs change
      row.querySelector('.in-star-x').addEventListener('input', (e) => {
        s.x = parseFloat(e.target.value) || 0;
        this.renderStudioSVG();
      });
      row.querySelector('.in-star-y').addEventListener('input', (e) => {
        s.y = parseFloat(e.target.value) || 0;
        this.renderStudioSVG();
      });
      row.querySelector('.in-star-r').addEventListener('input', (e) => {
        s.r = parseFloat(e.target.value) || 6;
        this.renderStudioSVG();
      });
      row.querySelector('.in-star-color').addEventListener('input', (e) => {
        s.color = e.target.value;
        this.renderStudioSVG();
      });
      row.querySelector('.in-star-mag').addEventListener('input', (e) => {
        s.mag = parseFloat(e.target.value) || 3.0;
      });
      row.querySelector('.in-star-name').addEventListener('input', (e) => {
        s.name = e.target.value;
        row.querySelector('.star-badge').textContent = `⭐ #${s.id} ${s.name} (${s.bayer || '-'})`;
      });
      row.querySelector('.in-star-bayer').addEventListener('input', (e) => {
        s.bayer = e.target.value;
        row.querySelector('.star-badge').textContent = `⭐ #${s.id} ${s.name} (${s.bayer || '-'})`;
        this.renderStudioSVG();
      });

      // Delete star
      row.querySelector('.btn-delete-star').addEventListener('click', (e) => {
        e.stopPropagation();
        this.deleteStar(s.id);
      });

      // Click row to select star
      row.addEventListener('click', () => this.selectStar(s.id));

      list.appendChild(row);
    });
  }

  updateStarRowInput(star) {
    const row = document.querySelector(`.star-edit-row[data-star-id="${star.id}"]`);
    if (row) {
      row.querySelector('.in-star-x').value = star.x;
      row.querySelector('.in-star-y').value = star.y;
    }
  }

  addNewStar() {
    const current = this.data[this.currentIndex];
    const newId = current.stars.length > 0 ? Math.max(...current.stars.map(s => s.id)) + 1 : 1;
    const newStar = {
      id: newId,
      x: 250,
      y: 200,
      r: 7.0,
      name: `ดาวดวงที่ ${newId}`,
      bayer: `Star ${newId}`,
      mag: 3.5,
      spect: "V",
      bright: false,
      color: "#00F0FF"
    };

    current.stars.push(newStar);
    this.selectStar(newId);
    this.populateStarsInspector();
    this.renderStudioSVG();
  }

  deleteStar(starId) {
    const current = this.data[this.currentIndex];
    current.stars = current.stars.filter(s => s.id !== starId);
    // Also remove lines connected to this star
    current.lines = current.lines.filter(([s1, s2]) => s1 !== starId && s2 !== starId);
    
    this.selectedStarId = null;
    this.populateStarsInspector();
    this.populateLinesInspector();
    this.renderStudioSVG();
  }

  populateLinesInspector() {
    const container = document.getElementById('lines-chips-container');
    container.innerHTML = '';
    const current = this.data[this.currentIndex];

    current.lines.forEach(([s1, s2], idx) => {
      const chip = document.createElement('div');
      chip.className = 'line-chip';
      chip.innerHTML = `
        <span>[ #${s1} ➔ #${s2} ]</span>
        <button class="btn-del-line" title="ลบเส้นนี้">✕</button>
      `;

      chip.querySelector('.btn-del-line').addEventListener('click', () => {
        current.lines.splice(idx, 1);
        this.populateLinesInspector();
        this.renderStudioSVG();
      });

      container.appendChild(chip);
    });
  }

  connectSelectedStars() {
    const s1 = parseInt(document.getElementById('line-select-star1').value, 10);
    const s2 = parseInt(document.getElementById('line-select-star2').value, 10);

    if (isNaN(s1) || isNaN(s2) || s1 === s2) {
      alert("กรุณาเลือกดาว 2 ดวงที่ต่างกันเพื่อเชื่อมเส้นครับ");
      return;
    }

    const current = this.data[this.currentIndex];
    // Check if line already exists
    const exists = current.lines.some(([a, b]) => (a === s1 && b === s2) || (a === s2 && b === s1));
    if (exists) {
      alert("มีเส้นเชื่อมระหว่างดาวคู่นี้อยู่แล้วครับ");
      return;
    }

    current.lines.push([s1, s2]);
    this.populateLinesInspector();
    this.renderStudioSVG();
  }

  populateArtOverlayInspector() {
    const current = this.data[this.currentIndex];
    const textarea = document.getElementById('svg-art-textarea');
    textarea.value = current.artOverlay ? current.artOverlay.trim() : '';
  }

  populateMetadataInspector() {
    const current = this.data[this.currentIndex];
    document.getElementById('meta-thai-name').value = current.thaiName || '';
    document.getElementById('meta-zodiac-name').value = current.zodiacName || '';
    document.getElementById('meta-latin-name').value = current.latinName || '';
    document.getElementById('meta-symbol').value = current.symbol || '';
    document.getElementById('meta-correct-answer').value = current.correctAnswer || '';
    document.getElementById('meta-hint').value = current.hint || '';
    document.getElementById('meta-funfact').value = current.funFact || '';
    document.getElementById('meta-starguide').value = current.starGuide || '';

    // Attach live change listeners
    const fields = [
      { id: 'meta-thai-name', key: 'thaiName' },
      { id: 'meta-zodiac-name', key: 'zodiacName' },
      { id: 'meta-latin-name', key: 'latinName' },
      { id: 'meta-symbol', key: 'symbol' },
      { id: 'meta-correct-answer', key: 'correctAnswer' },
      { id: 'meta-hint', key: 'hint' },
      { id: 'meta-funfact', key: 'funFact' },
      { id: 'meta-starguide', key: 'starGuide' }
    ];

    fields.forEach(({ id, key }) => {
      const input = document.getElementById(id);
      input.oninput = (e) => {
        current[key] = e.target.value;
        if (key === 'thaiName' || key === 'symbol' || key === 'latinName') {
          document.getElementById('studio-constellation-title').textContent = `${current.symbol} ${current.thaiName} (${current.latinName})`;
          this.buildZodiacChips();
        }
      };
    });
  }

  renderGalleryGrid() {
    const grid = document.getElementById('gallery-grid-container');
    grid.innerHTML = '';

    this.data.forEach((c, idx) => {
      const card = document.createElement('div');
      card.className = 'gallery-card';
      card.innerHTML = `
        <div class="gallery-card-header">
          <div class="gallery-card-title">${c.symbol} ${c.thaiName}</div>
          <span style="font-size: 0.85rem; color: var(--accent-cyan);">${c.latinName}</span>
        </div>
        <div class="gallery-card-svg" id="gallery-svg-${idx}">
          <!-- Mini SVG injected here -->
        </div>
        <div class="gallery-card-footer">
          <span>⭐ ${c.stars.length} ดวง</span>
          <span>📐 ${c.lines.length} เส้น</span>
          <span style="color: var(--accent-gold);">คลิกเพื่อปรับแต่ง 🛠️</span>
        </div>
      `;

      card.addEventListener('click', () => {
        document.querySelectorAll('.zodiac-chip').forEach(el => el.classList.remove('active'));
        const chip = document.querySelector(`.zodiac-chip[data-index="${idx}"]`);
        if (chip) chip.classList.add('active');
        this.switchViewMode('studio');
        this.loadConstellation(idx);
      });

      grid.appendChild(card);

      // Render Mini SVG inside card
      setTimeout(() => {
        const container = document.getElementById(`gallery-svg-${idx}`);
        if (container) {
          const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
          svg.setAttribute('viewBox', c.viewBox || '0 0 500 400');
          svg.setAttribute('class', 'studio-svg');
          svg.innerHTML = '';

          // Art Overlay
          if (c.artOverlay) {
            const art = document.createElementNS('http://www.w3.org/2000/svg', 'g');
            art.innerHTML = c.artOverlay;
            svg.appendChild(art);
          }

          // Lines
          const starMap = new Map();
          c.stars.forEach(s => starMap.set(s.id, s));
          c.lines.forEach(([s1Id, s2Id]) => {
            const s1 = starMap.get(s1Id);
            const s2 = starMap.get(s2Id);
            if (s1 && s2) {
              const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
              line.setAttribute('x1', s1.x);
              line.setAttribute('y1', s1.y);
              line.setAttribute('x2', s2.x);
              line.setAttribute('y2', s2.y);
              line.setAttribute('stroke', '#00F0FF');
              line.setAttribute('stroke-width', '2.5');
              svg.appendChild(line);
            }
          });

          // Stars
          c.stars.forEach(s => {
            const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circle.setAttribute('cx', s.x);
            circle.setAttribute('cy', s.y);
            circle.setAttribute('r', s.r || 6);
            circle.setAttribute('fill', s.color || '#FFFFFF');
            svg.appendChild(circle);
          });

          container.appendChild(svg);
        }
      }, 0);
    });
  }

  generateFullJSCode() {
    const formattedData = JSON.stringify(this.data, null, 2);
    return `/**\n * ฐานข้อมูลกลุ่มดาว 12 จักราศี (12 Zodiac Constellations Dataset)\n * ส่งออกจาก Constellation Studio\n */\n\nconst CONSTELLATIONS_DATA = ${formattedData};\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = { CONSTELLATIONS_DATA };\n}\n`;
  }

  copyCodeToClipboard() {
    const code = this.generateFullJSCode();
    navigator.clipboard.writeText(code).then(() => {
      const btn = document.getElementById('btn-copy-code');
      const originalText = btn.innerHTML;
      btn.innerHTML = '✅ คัดลอกสำเร็จ!';
      setTimeout(() => btn.innerHTML = originalText, 2000);
    }).catch(err => {
      alert("ไม่สามารถคัดลอกได้อัตโนมัติ: " + err);
    });
  }

  downloadJSFile() {
    const code = this.generateFullJSCode();
    const blob = new Blob([code], { type: 'application/javascript;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'constellations.js';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }
}

// Instantiate Studio on Load
document.addEventListener('DOMContentLoaded', () => {
  window.studioApp = new ConstellationStudio();
});
