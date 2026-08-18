/**
 * Stargazer Kids Quiz - Main Game Application Logic
 */

class StargazerApp {
  constructor() {
    this.currentMode = 'practice'; // 'practice' or 'challenge'
    this.challengeTimePerQuestion = 10; // seconds per question in challenge mode
    this.timerInterval = null;
    this._lastTickSec = null;

    this.questions = [];
    this.currentIndex = 0;
    this.score = 0;
    this.streak = 0;
    this.maxStreak = 0;
    this.correctCount = 0;
    this.isAnswered = false;
    this.isOverlayVisible = false;
    this.isLinesVisible = true;
    this.isGlowVisible = true;

    // Lifeline tracking
    this.lifelines = {
      peekUsed: false,
      fiftyUsed: false,
      clueUsed: false
    };

    // DOM Elements
    this.screens = {
      start: document.getElementById('screen-start'),
      quiz: document.getElementById('screen-quiz'),
      result: document.getElementById('screen-result')
    };

    this.starfield = null;
    this.confetti = null;

    this.init();
  }

  init() {
    // Initialize Canvas Visuals
    this.starfield = new CosmicStarfield('starfield-canvas');
    this.confetti = new CosmicConfetti('confetti-canvas');

    this.bindEvents();
    this.buildCodex();
  }

  bindEvents() {
    // Audio button
    const btnSound = document.getElementById('btn-toggle-sound');
    const soundText = document.getElementById('sound-btn-text');
    btnSound.addEventListener('click', () => {
      const isMuted = audioManager.toggleMute();
      soundText.textContent = isMuted ? 'เสียง: ปิด' : 'เสียง: เปิด';
      btnSound.style.opacity = isMuted ? '0.6' : '1';
      if (!isMuted) audioManager.playPop();
    });

    // Home logo
    document.getElementById('btn-home-logo').addEventListener('click', () => {
      audioManager.playPop();
      this.stopTimer();
      this.showScreen('start');
    });

    // Start Practice Mode Button
    document.getElementById('btn-start-practice').addEventListener('click', () => {
      audioManager.playPop();
      this.startQuiz('practice');
    });

    // Start Challenge Mode Button -> Opens Timer Selection Modal
    const modalTimerSelect = document.getElementById('modal-timer-select');
    const sliderCustomTime = document.getElementById('slider-custom-time');
    const customTimeVal = document.getElementById('custom-time-val');
    const btnTimerValDisplay = document.getElementById('btn-timer-val-display');

    let selectedChallengeTime = 10;

    const updateSelectedTime = (time) => {
      selectedChallengeTime = parseInt(time, 10);
      if (sliderCustomTime) sliderCustomTime.value = selectedChallengeTime;
      if (customTimeVal) customTimeVal.textContent = selectedChallengeTime;
      if (btnTimerValDisplay) btnTimerValDisplay.textContent = selectedChallengeTime;

      document.querySelectorAll('.timer-chip-btn').forEach(chip => {
        chip.classList.toggle('active', parseInt(chip.dataset.time, 10) === selectedChallengeTime);
      });
    };

    document.getElementById('btn-start-challenge').addEventListener('click', () => {
      audioManager.playPop();
      updateSelectedTime(this.challengeTimePerQuestion || 10);
      if (modalTimerSelect) modalTimerSelect.classList.add('active');
    });

    // Timer Modal Controls
    document.querySelectorAll('.timer-chip-btn').forEach(chip => {
      chip.addEventListener('click', () => {
        audioManager.playPop();
        updateSelectedTime(chip.dataset.time);
      });
    });

    if (sliderCustomTime) {
      sliderCustomTime.addEventListener('input', (e) => {
        updateSelectedTime(e.target.value);
      });
    }

    const closeTimerModal = () => {
      audioManager.playPop();
      if (modalTimerSelect) modalTimerSelect.classList.remove('active');
    };

    const btnCloseTimer = document.getElementById('btn-close-timer-modal');
    if (btnCloseTimer) btnCloseTimer.addEventListener('click', closeTimerModal);

    const btnCancelTimer = document.getElementById('btn-cancel-timer-modal');
    if (btnCancelTimer) btnCancelTimer.addEventListener('click', closeTimerModal);

    // Confirm Start Challenge Button
    const btnConfirmChallenge = document.getElementById('btn-confirm-start-challenge');
    if (btnConfirmChallenge) {
      btnConfirmChallenge.addEventListener('click', () => {
        audioManager.playPop();
        if (modalTimerSelect) modalTimerSelect.classList.remove('active');
        this.startQuiz('challenge', selectedChallengeTime);
      });
    }

    document.getElementById('btn-main-play').addEventListener('click', () => {
      audioManager.playPop();
      this.startQuiz('practice');
    });

    // Constellation Overlay Toggle
    const btnOverlay = document.getElementById('btn-toggle-overlay');
    if (btnOverlay) {
      btnOverlay.addEventListener('click', () => {
        this.toggleOverlay();
      });
    }

    // Constellation Lines Toggle
    const btnLines = document.getElementById('btn-toggle-lines');
    if (btnLines) {
      btnLines.addEventListener('click', () => {
        this.toggleLines();
      });
    }

    // Star Brightness / Glow Toggle
    const btnGlow = document.getElementById('btn-toggle-glow');
    if (btnGlow) {
      btnGlow.addEventListener('click', () => {
        this.toggleGlow();
      });
    }

    // Lifeline Buttons
    document.getElementById('btn-hint-peek').addEventListener('click', () => this.useLifelinePeek());
    document.getElementById('btn-hint-5050').addEventListener('click', () => this.useLifeline5050());
    document.getElementById('btn-hint-clue').addEventListener('click', () => this.useLifelineClue());

    // Skip Question Button
    const btnSkip = document.getElementById('btn-skip-question');
    if (btnSkip) {
      btnSkip.addEventListener('click', () => this.skipQuestion());
    }

    // Next Question Button
    document.getElementById('btn-next-question').addEventListener('click', () => {
      audioManager.playPop();
      this.nextQuestion();
    });

    // Play Again & Home
    document.getElementById('btn-play-again').addEventListener('click', () => {
      audioManager.playPop();
      this.startQuiz(this.currentMode, this.challengeTimePerQuestion);
    });

    document.getElementById('btn-back-home').addEventListener('click', () => {
      audioManager.playPop();
      this.stopTimer();
      this.showScreen('start');
    });

    // Codex Modal
    const modalCodex = document.getElementById('modal-codex');
    document.getElementById('btn-open-codex').addEventListener('click', () => {
      audioManager.playPop();
      modalCodex.classList.add('active');
    });
    document.getElementById('btn-close-codex').addEventListener('click', () => {
      audioManager.playPop();
      modalCodex.classList.remove('active');
    });
    modalCodex.addEventListener('click', (e) => {
      if (e.target === modalCodex) modalCodex.classList.remove('active');
    });

    // Hint Modal Confirm & Close
    const modalHint = document.getElementById('modal-hint');
    document.getElementById('btn-close-hint').addEventListener('click', () => {
      audioManager.playPop();
      modalHint.classList.remove('active');
    });
    document.getElementById('btn-confirm-hint').addEventListener('click', () => {
      audioManager.playPop();
      modalHint.classList.remove('active');
    });
    modalHint.addEventListener('click', (e) => {
      if (e.target === modalHint) modalHint.classList.remove('active');
    });

    // Certificate Generator Modal
    const modalCert = document.getElementById('modal-certificate');
    document.getElementById('btn-show-cert').addEventListener('click', () => {
      audioManager.playPop();
      this.generateCertificate();
      modalCert.classList.add('active');
    });
    document.getElementById('btn-close-cert').addEventListener('click', () => {
      audioManager.playPop();
      modalCert.classList.remove('active');
    });
    modalCert.addEventListener('click', (e) => {
      if (e.target === modalCert) modalCert.classList.remove('active');
    });

    // Download & Print Certificate
    document.getElementById('btn-download-cert').addEventListener('click', () => this.downloadCertificate());
    document.getElementById('btn-print-cert').addEventListener('click', () => this.printCertificate());
  }

  showScreen(screenName) {
    this.stopTimer();
    Object.values(this.screens).forEach(s => s.classList.remove('active'));
    if (this.screens[screenName]) {
      this.screens[screenName].classList.add('active');
    }
  }

  startQuiz(mode = 'practice', timeLimit = 10) {
    this.stopTimer();
    this.currentMode = mode;
    this.challengeTimePerQuestion = timeLimit;
    this.score = 0;
    this.streak = 0;
    this.maxStreak = 0;
    this.correctCount = 0;
    this.currentIndex = 0;

    // Reset lifelines
    this.lifelines = {
      peekUsed: false,
      fiftyUsed: false,
      clueUsed: false
    };

    // Shuffle constellations for diverse playthroughs
    this.questions = [...CONSTELLATIONS_DATA].sort(() => Math.random() - 0.5);

    // Setup HUD for current mode
    const timerBadge = document.getElementById('quiz-timer-badge');
    const timerModeTag = document.getElementById('timer-mode-tag');
    if (timerBadge) {
      if (mode === 'challenge') {
        timerBadge.style.display = 'flex';
        if (timerModeTag) timerModeTag.textContent = `โหมดนักล่า (${timeLimit}s)`;
      } else {
        timerBadge.style.display = 'none';
      }
    }

    this.updateScoreHUD();
    this.showScreen('quiz');
    this.loadQuestion(0);
  }

  loadQuestion(index) {
    this.stopTimer();
    this.currentIndex = index;
    this.isAnswered = false;
    this.isOverlayVisible = false;

    const data = this.questions[index];
    if (!data) return;

    // Update Question Counter & Progress
    const counterEl = document.getElementById('quiz-question-counter');
    counterEl.textContent = `กลุ่มดาวที่ ${index + 1} / ${this.questions.length}`;

    const progressPercent = ((index) / this.questions.length) * 100;
    document.getElementById('quiz-progress-fill').style.width = `${progressPercent}%`;

    // Constellation Tag & Guide
    document.getElementById('constellation-symbol').textContent = data.symbol;
    document.getElementById('constellation-name').textContent = data.zodiacName;
    document.getElementById('star-guide-text').textContent = `💡 จุดสังเกต: ${data.starGuide}`;

    // Reset Overlay Button
    const btnOverlay = document.getElementById('btn-toggle-overlay');
    const btnOverlayText = document.getElementById('overlay-toggle-text');
    if (btnOverlay) {
      btnOverlay.classList.remove('active');
      if (btnOverlayText) btnOverlayText.textContent = 'ภาพร่างจริง';
    }

    // Reset Tool Buttons
    const btnLines = document.getElementById('btn-toggle-lines');
    const btnLinesText = document.getElementById('lines-toggle-text');
    if (btnLines) {
      btnLines.classList.toggle('active', this.isLinesVisible);
      if (btnLinesText) btnLinesText.textContent = this.isLinesVisible ? 'เส้นโยง: เปิด' : 'เส้นโยง: ปิด';
    }

    const btnGlow = document.getElementById('btn-toggle-glow');
    const btnGlowText = document.getElementById('glow-toggle-text');
    if (btnGlow) {
      btnGlow.classList.toggle('active', this.isGlowVisible);
      if (btnGlowText) btnGlowText.textContent = this.isGlowVisible ? 'แสงดาว: เปิด' : 'แสงดาว: ปิด';
    }

    // Reset & Enable Lifelines and Skip
    document.getElementById('btn-hint-peek').disabled = false;
    document.getElementById('btn-hint-5050').disabled = false;
    document.getElementById('btn-hint-clue').disabled = false;
    const btnSkip = document.getElementById('btn-skip-question');
    if (btnSkip) btnSkip.disabled = false;

    // Hide Feedback Card
    document.getElementById('feedback-card').style.display = 'none';

    // Render Constellation SVG
    this.renderConstellationSVG(data);

    // Render 4 Options (Shuffled)
    this.renderOptions(data);

    // Start countdown timer if in Challenge Mode
    if (this.currentMode === 'challenge') {
      this.startQuestionTimer();
    }
  }

  startQuestionTimer() {
    this.stopTimer();
    const timerBadge = document.getElementById('quiz-timer-badge');
    const timerSecondsEl = document.getElementById('quiz-timer-seconds');
    const progressCircle = document.getElementById('timer-progress-circle');

    if (timerBadge) {
      timerBadge.style.display = 'flex';
      timerBadge.classList.remove('low-time');
    }

    const totalTime = this.challengeTimePerQuestion || 10;
    if (timerSecondsEl) timerSecondsEl.textContent = totalTime;
    if (progressCircle) progressCircle.setAttribute('stroke-dashoffset', '0');

    const startTime = Date.now();
    this._lastTickSec = null;

    this.timerInterval = setInterval(() => {
      if (this.isAnswered) {
        this.stopTimer();
        return;
      }

      const elapsedMs = Date.now() - startTime;
      const remainingSec = Math.max(0, totalTime - (elapsedMs / 1000));
      const displaySec = Math.ceil(remainingSec);

      if (timerSecondsEl) timerSecondsEl.textContent = displaySec;

      // Circle Progress (0 is full, 100 is empty)
      const percentLeft = (remainingSec / totalTime) * 100;
      const dashOffset = 100 - percentLeft;
      if (progressCircle) progressCircle.setAttribute('stroke-dashoffset', dashOffset);

      // Low time warning when remaining <= 3s
      if (displaySec <= 3 && displaySec > 0) {
        if (timerBadge && !timerBadge.classList.contains('low-time')) {
          timerBadge.classList.add('low-time');
        }
        if (this._lastTickSec !== displaySec) {
          this._lastTickSec = displaySec;
          audioManager.playTick();
        }
      }

      // Timeout triggered
      if (remainingSec <= 0) {
        this.stopTimer();
        this.handleTimeout();
      }
    }, 50);
  }

  stopTimer() {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }
    this._lastTickSec = null;
    const timerBadge = document.getElementById('quiz-timer-badge');
    if (timerBadge) timerBadge.classList.remove('low-time');
  }

  handleTimeout() {
    if (this.isAnswered) return;
    this.isAnswered = true;
    audioManager.playTimeout();

    // Reset streak on timeout
    this.streak = 0;
    this.updateScoreHUD();

    // Disable all options and show correct answer
    const allButtons = document.querySelectorAll('.option-btn');
    allButtons.forEach(btn => {
      btn.disabled = true;
      if (btn.dataset.correct === 'true') {
        btn.classList.add('correct');
      }
    });

    // Reveal art overlay
    this.toggleOverlay(true);

    // Disable lifelines and skip button
    document.getElementById('btn-hint-peek').disabled = true;
    document.getElementById('btn-hint-5050').disabled = true;
    document.getElementById('btn-hint-clue').disabled = true;
    const btnSkip = document.getElementById('btn-skip-question');
    if (btnSkip) btnSkip.disabled = true;

    // Show Feedback Card indicating Timeout
    const data = this.questions[this.currentIndex];
    const feedbackCard = document.getElementById('feedback-card');
    const feedbackTitle = document.getElementById('feedback-title');
    const feedbackFunfact = document.getElementById('feedback-funfact');

    feedbackTitle.className = 'feedback-header wrong-head';
    feedbackTitle.innerHTML = `<span>⏰</span> หมดเวลาแล้ว! คำตอบที่ถูกต้องคือ: <strong>${data.correctAnswer}</strong>`;

    feedbackFunfact.innerHTML = `
      <strong>💡 เรื่องน่ารู้แห่งดวงดาว:</strong> ${data.funFact}
    `;

    feedbackCard.style.display = 'block';
  }

  renderConstellationSVG(data) {
    const svg = document.getElementById('constellation-svg');
    svg.setAttribute('viewBox', data.viewBox || '0 0 500 400');
    svg.innerHTML = '';

    // Defs for glowing effects
    const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    defs.innerHTML = `
      <radialGradient id="starGlowGrad" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="1" />
        <stop offset="40%" stop-color="#00F0FF" stop-opacity="0.8" />
        <stop offset="100%" stop-color="#00F0FF" stop-opacity="0" />
      </radialGradient>
      <linearGradient id="ramGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.3" />
        <stop offset="100%" stop-color="#9D4EDD" stop-opacity="0.3" />
      </linearGradient>
    `;
    svg.appendChild(defs);

    // Group for Art Overlay (hidden by default)
    const overlayGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    overlayGroup.id = 'svg-art-overlay';
    overlayGroup.innerHTML = data.artOverlay || '';
    overlayGroup.setAttribute('class', 'overlay-graphic hidden');
    svg.appendChild(overlayGroup);

    // Group for Connector Lines
    const linesGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    linesGroup.id = 'svg-lines-group';
    if (!this.isLinesVisible) {
      linesGroup.setAttribute('class', 'hidden');
    }

    const starMap = new Map();
    data.stars.forEach(s => starMap.set(s.id, s));

    data.lines.forEach(([startId, endId], idx) => {
      const s1 = starMap.get(startId);
      const s2 = starMap.get(endId);
      if (s1 && s2) {
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', s1.x);
        line.setAttribute('y1', s1.y);
        line.setAttribute('x2', s2.x);
        line.setAttribute('y2', s2.y);
        line.setAttribute('class', 'star-line');
        line.style.animationDelay = `${idx * 0.1}s`;
        linesGroup.appendChild(line);
      }
    });
    svg.appendChild(linesGroup);

    // Group for Star Nodes
    const starsGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    starsGroup.id = 'svg-stars-group';

    data.stars.forEach(s => {
      // Glow circle halo for bright stars (Twinkles gently around the star)
      if (s.bright) {
        const glow = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        glow.setAttribute('cx', s.x);
        glow.setAttribute('cy', s.y);
        glow.setAttribute('r', s.r * 2.4);
        glow.setAttribute('fill', s.color || '#00F0FF');
        glow.setAttribute('class', `star-glow-ring ${!this.isGlowVisible ? 'hidden' : ''}`);
        glow.setAttribute('filter', 'drop-shadow(0 0 8px ' + (s.color || '#00F0FF') + ')');
        starsGroup.appendChild(glow);
      }

      // Main star node
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('cx', s.x);
      circle.setAttribute('cy', s.y);
      circle.setAttribute('r', s.r || 6);
      circle.setAttribute('fill', s.color || '#FFFFFF');
      circle.setAttribute('class', 'star-node');
      circle.style.cursor = 'pointer';

      // Astronomical detailed tooltip string
      const starDetailStr = s.spect ?
        `✨ ${s.name} | อันดับความสว่าง: ${s.mag} | ชนิดสเปกตรัม: ${s.spect}` :
        `✨ ${s.name} | อันดับความสว่าง: ${s.mag}`;

      // Native SVG Tooltip
      const title = document.createElementNS('http://www.w3.org/2000/svg', 'title');
      title.textContent = starDetailStr;
      circle.appendChild(title);

      circle.addEventListener('mouseenter', () => {
        document.getElementById('star-guide-text').textContent = starDetailStr;
      });

      circle.addEventListener('mouseleave', () => {
        document.getElementById('star-guide-text').textContent = `💡 จุดสังเกต: ${data.starGuide}`;
      });

      circle.addEventListener('click', () => {
        audioManager.playPop();
        document.getElementById('star-guide-text').textContent = starDetailStr;
      });

      starsGroup.appendChild(circle);
    });

    svg.appendChild(starsGroup);
  }

  renderOptions(data) {
    const container = document.getElementById('options-container');
    container.innerHTML = '';

    // Shuffle options
    const shuffledOptions = [...data.options].sort(() => Math.random() - 0.5);

    shuffledOptions.forEach((opt) => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.dataset.correct = opt.correct;

      btn.innerHTML = `
        <div class="option-icon">${opt.icon}</div>
        <div class="option-text">${opt.text}</div>
      `;

      btn.addEventListener('click', () => this.handleOptionClick(btn, opt.correct, data));
      container.appendChild(btn);
    });
  }

  toggleOverlay(forceState = null) {
    const overlay = document.getElementById('svg-art-overlay');
    const btnOverlay = document.getElementById('btn-toggle-overlay');
    const btnOverlayText = document.getElementById('overlay-toggle-text');

    if (!overlay) return;

    if (forceState !== null) {
      this.isOverlayVisible = forceState;
    } else {
      this.isOverlayVisible = !this.isOverlayVisible;
    }

    if (this.isOverlayVisible) {
      overlay.classList.remove('hidden');
      if (btnOverlay) btnOverlay.classList.add('active');
      if (btnOverlayText) btnOverlayText.textContent = 'ซ่อนภาพร่าง';
      audioManager.playMagicOverlay();
    } else {
      overlay.classList.add('hidden');
      if (btnOverlay) btnOverlay.classList.remove('active');
      if (btnOverlayText) btnOverlayText.textContent = 'ภาพร่างจริง';
    }
  }

  toggleLines(forceState = null) {
    const linesGroup = document.getElementById('svg-lines-group');
    const btnLines = document.getElementById('btn-toggle-lines');
    const btnLinesText = document.getElementById('lines-toggle-text');

    if (forceState !== null) {
      this.isLinesVisible = forceState;
    } else {
      this.isLinesVisible = !this.isLinesVisible;
    }

    if (linesGroup) {
      if (this.isLinesVisible) {
        linesGroup.classList.remove('hidden');
      } else {
        linesGroup.classList.add('hidden');
      }
    }

    if (btnLines) {
      btnLines.classList.toggle('active', this.isLinesVisible);
      if (btnLinesText) {
        btnLinesText.textContent = this.isLinesVisible ? 'เส้นโยง: เปิด' : 'เส้นโยง: ปิด';
      }
    }
    audioManager.playPop();
  }

  toggleGlow(forceState = null) {
    const glowRings = document.querySelectorAll('.star-glow-ring');
    const btnGlow = document.getElementById('btn-toggle-glow');
    const btnGlowText = document.getElementById('glow-toggle-text');

    if (forceState !== null) {
      this.isGlowVisible = forceState;
    } else {
      this.isGlowVisible = !this.isGlowVisible;
    }

    glowRings.forEach(glow => {
      if (this.isGlowVisible) {
        glow.classList.remove('hidden');
      } else {
        glow.classList.add('hidden');
      }
    });

    if (btnGlow) {
      btnGlow.classList.toggle('active', this.isGlowVisible);
      if (btnGlowText) {
        btnGlowText.textContent = this.isGlowVisible ? 'แสงดาว: เปิด' : 'แสงดาว: ปิด';
      }
    }
    audioManager.playPop();
  }

  skipQuestion() {
    if (this.isAnswered) return;
    this.stopTimer();
    this.isAnswered = true;
    audioManager.playPop();

    // Reset streak on skip
    this.streak = 0;
    this.updateScoreHUD();

    // Disable all options and highlight the correct one
    const allButtons = document.querySelectorAll('.option-btn');
    allButtons.forEach(btn => {
      btn.disabled = true;
      if (btn.dataset.correct === 'true') {
        btn.classList.add('correct');
      }
    });

    // Reveal art overlay
    this.toggleOverlay(true);

    // Disable lifelines and skip button
    document.getElementById('btn-hint-peek').disabled = true;
    document.getElementById('btn-hint-5050').disabled = true;
    document.getElementById('btn-hint-clue').disabled = true;
    const btnSkip = document.getElementById('btn-skip-question');
    if (btnSkip) btnSkip.disabled = true;

    // Show Feedback Card
    const data = this.questions[this.currentIndex];
    const feedbackCard = document.getElementById('feedback-card');
    const feedbackTitle = document.getElementById('feedback-title');
    const feedbackFunfact = document.getElementById('feedback-funfact');

    feedbackTitle.className = 'feedback-header';
    feedbackTitle.style.color = '#FFA502';
    feedbackTitle.innerHTML = `<span>⏭️</span> ข้ามข้อนี้แล้ว! คำตอบที่ถูกต้องคือ <strong>${data.correctAnswer}</strong>`;

    feedbackFunfact.innerHTML = `
      <strong>💡 เรื่องน่ารู้แห่งดวงดาว:</strong> ${data.funFact}
    `;

    feedbackCard.style.display = 'block';
  }

  useLifelinePeek() {
    if (this.isAnswered) return;
    audioManager.playLifeline();
    document.getElementById('btn-hint-peek').disabled = true;

    // Show overlay for 3.5 seconds
    this.toggleOverlay(true);
    setTimeout(() => {
      if (!this.isAnswered) {
        this.toggleOverlay(false);
      }
    }, 3500);
  }

  useLifeline5050() {
    if (this.isAnswered) return;
    audioManager.playLifeline();
    document.getElementById('btn-hint-5050').disabled = true;

    const optionButtons = Array.from(document.querySelectorAll('.option-btn'));
    const wrongButtons = optionButtons.filter(btn => btn.dataset.correct !== 'true');

    // Shuffle and hide 2 wrong buttons
    const toHide = wrongButtons.sort(() => Math.random() - 0.5).slice(0, 2);
    toHide.forEach(btn => btn.classList.add('hidden-5050'));
  }

  useLifelineClue() {
    if (this.isAnswered) return;
    audioManager.playLifeline();
    document.getElementById('btn-hint-clue').disabled = true;

    const data = this.questions[this.currentIndex];

    // Populate and show Hint Modal
    document.getElementById('hint-modal-title').textContent = `${data.symbol} ${data.zodiacName}`;
    document.getElementById('hint-modal-text').textContent = data.hint;
    document.getElementById('modal-hint').classList.add('active');
  }

  handleOptionClick(selectedBtn, isCorrect, data) {
    if (this.isAnswered) return;
    this.stopTimer();
    this.isAnswered = true;

    // Disable all options
    const allButtons = document.querySelectorAll('.option-btn');
    allButtons.forEach(btn => {
      btn.disabled = true;
      if (btn.dataset.correct === 'true') {
        btn.classList.add('correct');
      }
    });

    // Always reveal Art Overlay on answering so children learn the visual connection!
    this.toggleOverlay(true);

    const feedbackCard = document.getElementById('feedback-card');
    const feedbackTitle = document.getElementById('feedback-title');
    const feedbackFunfact = document.getElementById('feedback-funfact');

    if (isCorrect) {
      selectedBtn.classList.add('correct');
      this.score += (100 + this.streak * 20);
      this.streak += 1;
      this.maxStreak = Math.max(this.maxStreak, this.streak);
      this.correctCount += 1;

      audioManager.playCorrect();
      if (this.streak >= 2) {
        audioManager.playStreak(this.streak);
      }
      this.confetti.burst(window.innerWidth / 2, window.innerHeight / 2, 40);

      feedbackTitle.className = 'feedback-header correct-head';
      feedbackTitle.innerHTML = `<span>✨🎉</span> ยอดเยี่ยมมาก! คำตอบคือ <strong>${data.correctAnswer}</strong>`;
    } else {
      selectedBtn.classList.add('wrong');
      this.streak = 0;
      audioManager.playWrong();

      feedbackTitle.className = 'feedback-header wrong-head';
      feedbackTitle.innerHTML = `<span>🔭</span> เกือบถูกแล้ว! คำตอบที่แท้จริงคือ <strong>${data.correctAnswer}</strong>`;
    }

    feedbackFunfact.innerHTML = `
      <strong>💡 เรื่องน่ารู้แห่งดวงดาว:</strong> ${data.funFact}
    `;

    feedbackCard.style.display = 'block';
    this.updateScoreHUD();
  }

  updateScoreHUD() {
    document.getElementById('quiz-score-display').textContent = this.score;
    const streakPill = document.getElementById('quiz-streak-counter');
    if (this.streak >= 2) {
      streakPill.style.display = 'inline-flex';
      streakPill.textContent = `🔥 Combo x${this.streak}`;
    } else {
      streakPill.style.display = 'none';
    }
  }

  nextQuestion() {
    if (this.currentIndex + 1 < this.questions.length) {
      this.loadQuestion(this.currentIndex + 1);
    } else {
      this.finishGame();
    }
  }

  finishGame() {
    audioManager.playVictory();
    this.confetti.burst(window.innerWidth / 2, window.innerHeight / 2, 100);

    const accuracy = Math.round((this.correctCount / this.questions.length) * 100);

    document.getElementById('res-score').textContent = this.score;
    document.getElementById('res-accuracy').textContent = `${accuracy}%`;
    document.getElementById('res-streak').textContent = `x${this.maxStreak}`;

    let statusMsg = "ยินดีด้วย! น้องคือนักดาราศาสตร์น้อยผู้เปี่ยมด้วยจินตนาการ";
    if (accuracy === 100) {
      statusMsg = "🌟 ยอดเยี่ยมไร้ที่ติ! น้องคือ 'ผู้พิชิต 12 จักราศี' ตัวจริง!";
    } else if (accuracy >= 70) {
      statusMsg = "🔭 สายตาเฉียบคมมาก! น้องมีแววเป็นนักดาราศาสตร์มือโปรแล้วนะ!";
    }

    document.getElementById('result-status-msg').textContent = statusMsg;
    this.showScreen('result');
  }

  buildCodex() {
    const list = document.getElementById('codex-list');
    list.innerHTML = '';

    CONSTELLATIONS_DATA.forEach(c => {
      const card = document.createElement('div');
      card.className = 'codex-card';
      card.innerHTML = `
        <div class="codex-card-top">
          <div class="codex-symbol">${c.symbol}</div>
          <div class="codex-card-title">
            <h4>${c.thaiName}</h4>
            <span>${c.zodiacName}</span>
          </div>
        </div>
        <div class="codex-card-shape">รูปร่าง: ${c.correctAnswer}</div>
        <div class="codex-card-desc">${c.funFact}</div>
        <div class="codex-card-stars" style="margin-top: 8px; font-size: 0.85rem; color: #00F0FF;">🔭 ${c.starGuide}</div>
      `;
      list.appendChild(card);
    });
  }

  generateCertificate() {
    const canvas = document.getElementById('certificate-canvas');
    const ctx = canvas.getContext('2d');
    const nameInput = document.getElementById('kid-name-input').value.trim() || 'นักดาราศาสตร์ตัวจิ๋ว';

    // Width: 1000, Height: 700
    const w = canvas.width;
    const h = canvas.height;

    // Background Gradient (Deep Space Navy with Nebula Gold)
    const bgGrad = ctx.createLinearGradient(0, 0, w, h);
    bgGrad.addColorStop(0, '#060B28');
    bgGrad.addColorStop(0.5, '#111740');
    bgGrad.addColorStop(1, '#050718');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, w, h);

    // Decorative Stars
    ctx.fillStyle = '#FFFFFF';
    for (let i = 0; i < 80; i++) {
      const sx = Math.random() * w;
      const sy = Math.random() * h;
      const sr = Math.random() * 2 + 0.5;
      ctx.globalAlpha = Math.random() * 0.7 + 0.3;
      ctx.beginPath();
      ctx.arc(sx, sy, sr, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1.0;

    // Elegant Outer Border
    ctx.strokeStyle = '#FFD700';
    ctx.lineWidth = 8;
    ctx.strokeRect(30, 30, w - 60, h - 60);

    // Inner Neon Border
    ctx.strokeStyle = '#00F0FF';
    ctx.lineWidth = 2;
    ctx.strokeRect(45, 45, w - 90, h - 90);

    // Corner Ornaments
    this.drawCornerOrnament(ctx, 45, 45);
    this.drawCornerOrnament(ctx, w - 45, 45);
    this.drawCornerOrnament(ctx, 45, h - 45);
    this.drawCornerOrnament(ctx, w - 45, h - 45);

    // Certificate Header
    ctx.textAlign = 'center';
    ctx.fillStyle = '#00F0FF';
    ctx.font = 'bold 24px Prompt, sans-serif';
    ctx.fillText('🪐 PB Earth Science & Astronomy Club 🪐', w / 2, 110);

    ctx.fillStyle = '#FFD700';
    ctx.font = 'bold 44px Mali, Prompt, sans-serif';
    ctx.fillText('ใบประกาศนียบัตรเกียรติคุณ', w / 2, 175);

    ctx.fillStyle = '#E2E8F0';
    ctx.font = '22px Prompt, sans-serif';
    ctx.fillText('ขอมอบเกียรติบัตรฉบับนี้เพื่อแสดงว่า', w / 2, 235);

    // Student's Name
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 46px Mali, Prompt, sans-serif';
    ctx.shadowColor = '#00F0FF';
    ctx.shadowBlur = 12;
    ctx.fillText(nameInput, w / 2, 310);
    ctx.shadowBlur = 0; // Reset shadow

    // Underline
    ctx.strokeStyle = '#FFD700';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(w / 2 - 220, 335);
    ctx.lineTo(w / 2 + 220, 335);
    ctx.stroke();

    // Achievement text
    ctx.fillStyle = '#CBD5E1';
    ctx.font = '22px Prompt, sans-serif';
    ctx.fillText('ได้ผ่านการทดสอบทักษะจินตนาการและการสังเกต', w / 2, 385);

    ctx.fillStyle = '#FFEAA7';
    ctx.font = 'bold 26px Prompt, sans-serif';
    ctx.fillText('🌟 "นักดาราศาสตร์น้อย ผู้พิชิตกลุ่มดาว 12 จักราศี" 🌟', w / 2, 430);

    const modeStr = this.currentMode === 'challenge' ? `โหมดนักล่า (${this.challengeTimePerQuestion}s/ข้อ)` : 'โหมดฝึกท่องอวกาศ';
    const accuracy = Math.round((this.correctCount / Math.max(1, this.questions.length)) * 100);

    ctx.fillStyle = '#94A3B8';
    ctx.font = '18px Prompt, sans-serif';
    ctx.fillText(`คะแนน: ${this.score} แต้ม | ความแม่นยำ: ${accuracy}% | ${modeStr}`, w / 2, 475);

    // Footer - Badge & Signature
    ctx.fillStyle = '#FFD700';
    ctx.font = 'bold 20px Prompt, sans-serif';
    ctx.fillText('🏆 สถาบันดวงดาวสำหรับเยาวชน', w / 4, 570);
    ctx.fillStyle = '#94A3B8';
    ctx.font = '16px Prompt, sans-serif';
    ctx.fillText('ประทับตราเกียรติยศ', w / 4, 600);

    // Date
    const today = new Date().toLocaleDateString('th-TH', { year: 'numeric', month: 'long', day: 'numeric' });
    ctx.fillStyle = '#FFD700';
    ctx.font = 'bold 20px Prompt, sans-serif';
    ctx.fillText(`วันที่ ${today}`, (w / 4) * 3, 570);
    ctx.fillStyle = '#94A3B8';
    ctx.font = '16px Prompt, sans-serif';
    ctx.fillText('Stargazer Space Mission', (w / 4) * 3, 600);

    // Golden Seal in center bottom
    this.drawGoldenSeal(ctx, w / 2, 570);
  }

  drawCornerOrnament(ctx, x, y) {
    ctx.save();
    ctx.strokeStyle = '#FFD700';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(x, y, 16, 0, Math.PI * 2);
    ctx.stroke();
    ctx.restore();
  }

  drawGoldenSeal(ctx, x, y) {
    ctx.save();
    ctx.fillStyle = '#F39C12';
    ctx.beginPath();
    ctx.arc(x, y, 36, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = '#FFD700';
    ctx.lineWidth = 4;
    ctx.stroke();

    ctx.fillStyle = '#060B28';
    ctx.font = '24px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('✨', x, y);
    ctx.restore();
  }

  downloadCertificate() {
    audioManager.playPop();
    const canvas = document.getElementById('certificate-canvas');
    const link = document.createElement('a');
    link.download = 'stargazer-kids-certificate.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  }

  printCertificate() {
    audioManager.playPop();
    const canvas = document.getElementById('certificate-canvas');
    const dataUrl = canvas.toDataURL('image/png');
    const windowContent = `
      <!DOCTYPE html>
      <html>
        <head><title>Print Certificate</title></head>
        <body style="margin:0; display:flex; justify-content:center; align-items:center; min-height:100vh;">
          <img src="${dataUrl}" style="max-width:100%; height:auto;" onload="window.print();window.close();" />
        </body>
      </html>
    `;
    const printWindow = window.open('', '', 'width=1100,height=800');
    printWindow.document.open();
    printWindow.document.write(windowContent);
    printWindow.document.close();
  }
}

// Initialize Application when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  window.stargazerApp = new StargazerApp();
});
