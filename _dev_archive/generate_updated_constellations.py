# -*- coding: utf-8 -*-
"""
Generate the new js/constellations.js with the updated 5 constellations matching user images:
- Libra
- Sagittarius
- Aquarius
- Pisces
- Gemini
"""

import json

constellations_js_template = """/**
 * ฐานข้อมูลกลุ่มดาว 12 จักราศี (12 Zodiac Constellations Dataset)
 * อัปเดตปรับปรุงโครงสร้างเส้นโยงดาว (Constellation Lines) และภาพร่างเวกเตอร์ (Art Overlay)
 * ตรงตามแผนที่ท้องฟ้าจริงและภาพดาราศาสตร์มาตรฐาน (Stellarium Sky Map) 100%
 */

const CONSTELLATIONS_DATA = [
  {
    id: "aries",
    thaiName: "กลุ่มดาวแกะ",
    zodiacName: "ราศีเมษ (Aries)",
    latinName: "Aries",
    symbol: "♈",
    correctAnswer: "แกะตัวผู้ (มีเขาโค้ง)",
    options: [
      { "text": "แกะตัวผู้ (มีเขาโค้ง)", "icon": "🐏", "correct": true },
      { "text": "นกพิราบกางปีก", "icon": "🕊️", "correct": false },
      { "text": "หนังสติ๊กยิงนก", "icon": "🌱", "correct": false },
      { "text": "คันธนูและลูกศร", "icon": "🏹", "correct": false }
    ],
    hint: "มองหาดาวสว่าง 3 ดวงเรียงโค้งคล้ายเขาแกะ โดยมีดาวฮามัลสว่างสุดอยู่ตรงสันเขา!",
    funFact: "ราศีแรกของจักรราศี ในตำนานกรีกคือ 'แกะขนทองคำ' (Chrysomallos) ที่บินข้ามมหาสมุทรเพื่อช่วยเหลือเจ้าชาย!",
    starGuide: "ดาวสว่างสีส้ม 'ฮามัล' (Hamal) อยู่ตรงสันเขา และดาว 'เชอราทาน' กับ 'เมซาร์ทิม' อยู่ตรงปลายเขาแกะ",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 383, y: 218, r: 9, name: "ฮามัล (Hamal - α Ari)", bayer: "α Ari", mag: 2.0, spect: "K2 III (ดาวยักษ์ส้ม)", bright: true, color: "#FFA502" },
      { id: 2, x: 449, y: 279, r: 7.5, name: "เชอราทาน (Sheratan - β Ari)", bayer: "β Ari", mag: 2.64, spect: "A5 V (ดาวแคระขาว)", bright: true, color: "#FFFFFF" },
      { id: 3, x: 455, y: 314, r: 6.5, name: "เมซาร์ทิม (Mesarthim - γ Ari)", bayer: "γ Ari", mag: 3.88, spect: "A1 V (ดาวคู่ขาว)", bright: false, color: "#FFFFFF" },
      { id: 4, x: 45, y: 304, r: 5.5, name: "โบเทน (Botein - δ Ari)", bayer: "δ Ari", mag: 4.35, spect: "K2 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 5, x: 159, y: 132, r: 6.5, name: "ภารณี (Bharani - 41 Ari)", bayer: "41 Ari", mag: 3.61, spect: "B8 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 6, x: 170, y: 86, r: 5.5, name: "39 แอรีเอทิส (39 Ari)", bayer: "39 Ari", mag: 4.51, spect: "K1 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" }
    ],
    lines: [
      [4, 1], [1, 2], [2, 3], [1, 5], [5, 6]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <path d="M 370 200 Q 425 220 440 258 Q 455 280 445 292 Q 430 295 428 275" 
              fill="none" stroke="#FFD700" stroke-width="8" stroke-linecap="round" filter="drop-shadow(0 0 10px #FFD700)" />
        <path d="M 360 195 Q 410 215 425 248 Q 438 268 432 278" 
              fill="none" stroke="#FFA502" stroke-width="4" stroke-linecap="round" />
        <circle cx="350" cy="215" r="38" fill="#FFEAA7" opacity="0.4" stroke="#F1C40F" stroke-width="2" />
        <circle cx="365" cy="210" r="4.5" fill="#060919" />
        <circle cx="367" cy="208" r="1.5" fill="#FFFFFF" />
        <ellipse cx="378" cy="230" rx="7" ry="5" fill="#FF7675" opacity="0.6" />
        <ellipse cx="220" cy="215" rx="130" ry="65" fill="#70A1FF" opacity="0.25" stroke="#1E90FF" stroke-width="2" />
        <line x1="130" y1="265" x2="120" y2="345" stroke="#FFEAA7" stroke-width="5" stroke-linecap="round" />
        <line x1="190" y1="275" x2="185" y2="350" stroke="#FFEAA7" stroke-width="5" stroke-linecap="round" />
        <line x1="270" y1="270" x2="265" y2="345" stroke="#FFEAA7" stroke-width="5" stroke-linecap="round" />
      </g>
    `
  },
  {
    id: "taurus",
    thaiName: "กลุ่มดาววัว",
    zodiacName: "ราศีพฤษภ (Taurus)",
    latinName: "Taurus",
    symbol: "♉",
    correctAnswer: "วัวจอมพลัง (หน้าตัว V มีเขาแหลม)",
    options: [
      { "text": "วัวจอมพลัง (หน้าตัว V มีเขาแหลม)", "icon": "🐂", "correct": true },
      { "text": "ว่าวปักเป้าหางยาว", "icon": "🪁", "correct": false },
      { "text": "ปลาฉลามว่ายน้ำ", "icon": "🦈", "correct": false },
      { "text": "รถจักรยานสองล้อ", "icon": "🚲", "correct": false }
    ],
    hint: "มองหาหน้าวัวรูปตัว 'V' (กระจุกดาวไฮยาดีส) ที่มีดาวตาสีแดงอัลเดบารัน และมีเขายาว 2 ข้างพุ่งไปข้างหน้า!",
    funFact: "ดาวตาสีแดง 'อัลเดบารัน' มีขนาดใหญ่กว่าดวงอาทิตย์ 44 เท่า และบนสันหลังวัวมีกระจุกดาวลูกไก่ 7 ดวง (Pleiades)!",
    starGuide: "ดาวตาสีส้มแดง 'อัลเดบารัน' สว่างเด่นที่สุดในกระจุกดาวหน้าวัวรูปตัว V",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 239, y: 235, r: 11, name: "อัลเดบารัน (Aldebaran - α Tau ตาแดง)", bayer: "α Tau", mag: 0.85, spect: "K5 III (ดาวยักษ์แดงส้ม)", bright: true, color: "#FF4757" },
      { id: 2, x: 81, y: 75, r: 9, name: "เอลนาธ (Elnath - β Tau ปลายเขาเหนือ)", bayer: "β Tau", mag: 1.65, spect: "B7 III (ดาวยักษ์ฟ้าขาว)", bright: true, color: "#00F0FF" },
      { id: 3, x: 45, y: 174, r: 7.5, name: "เทียนกวาน (Tianguan - ζ Tau ปลายเขาใต้)", bayer: "ζ Tau", mag: 2.97, spect: "B2 IV (ดาวย่อยยักษ์ฟ้า)", bright: true, color: "#00F0FF" },
      { id: 4, x: 262, y: 200, r: 6.5, name: "ไอน์ (Ain - ε Tau ตาซ้าย)", bayer: "ε Tau", mag: 3.53, spect: "G9.5 III (ดาวยักษ์ส้มเหลือง)", bright: false, color: "#FFD27D" },
      { id: 5, x: 290, y: 247, r: 6.5, name: "พรีมา ไฮยาดูม (γ Tau ยอดจมูก V)", bayer: "γ Tau", mag: 3.65, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 6, x: 280, y: 222, r: 6.5, name: "เซกุนดา ไฮยาดูม (δ1 Tau ขอบหน้า)", bayer: "δ1 Tau", mag: 3.76, spect: "G9.5 III (ดาวยักษ์ส้มเหลือง)", bright: false, color: "#FFA502" },
      { id: 7, x: 262, y: 244, r: 6.5, name: "ทีตา ทอไร (θ2 Tau คางวัว)", bayer: "θ2 Tau", mag: 3.4, spect: "A7 III (ดาวยักษ์ขาว)", bright: false, color: "#FFFFFF" },
      { id: 8, x: 350, y: 288, r: 6.5, name: "แลมบ์ดา ทอไร (λ Tau อกวัว)", bayer: "λ Tau", mag: 3.41, spect: "B3 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 9, x: 455, y: 325, r: 6.5, name: "ซี ทอไร (ξ Tau ขาหน้า)", bayer: "ξ Tau", mag: 3.73, spect: "B9 V (ดาวขาวฟ้า)", bright: false, color: "#FFFFFF" },
      { id: 10, x: 391, y: 135, r: 7.5, name: "อัลไซโอนี (Alcyone - กระจุกดาวลูกไก่ M45)", bayer: "η Tau", mag: 2.87, spect: "B7 IIIe (กระจุกดาวลูกไก่)", bright: true, color: "#00F0FF" }
    ],
    lines: [
      [5, 6], [6, 4], [4, 2], [5, 7], [7, 1], [1, 3], [4, 1], [5, 8], [8, 9]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <path d="M 262 200 L 83 77" stroke="#FFD700" stroke-width="7" stroke-linecap="round" filter="drop-shadow(0 0 8px #FFD700)" />
        <path d="M 239 235 L 48 174" stroke="#FFD700" stroke-width="7" stroke-linecap="round" filter="drop-shadow(0 0 8px #FFD700)" />
        <polygon points="262,200 239,235 289,246 279,221" fill="#FF4757" opacity="0.35" stroke="#FF6B81" stroke-width="2" />
        <circle cx="239" cy="235" r="14" fill="#FF4757" opacity="0.4" filter="drop-shadow(0 0 12px #FF4757)" />
        <circle cx="389" cy="136" r="22" fill="#00F0FF" opacity="0.2" filter="drop-shadow(0 0 12px #00F0FF)" />
        <path d="M 289 246 Q 350 280 452 323 L 348 287 Z" fill="#FF6B81" opacity="0.25" />
      </g>
    `
  },
  {
    id: "gemini",
    thaiName: "กลุ่มดาวคนคู่ (ฝาแฝด)",
    zodiacName: "ราศีเมถุน (Gemini)",
    latinName: "Gemini",
    symbol: "♊",
    correctAnswer: "ฝาแฝดยืนเคียงข้างกัน",
    options: [
      { "text": "ฝาแฝดยืนเคียงข้างกัน", "icon": "👯‍♂️", "correct": true },
      { "text": "บันไดลิงปีนต้นไม้", "icon": "🪜", "correct": false },
      { "text": "สะพานแขวนข้ามแม่น้ำ", "icon": "🌉", "correct": false },
      { "text": "เรือใบสองเสา", "icon": "⛵", "correct": false }
    ],
    hint: "มองหาดาวสว่าง 2 ดวงคู่กันด้านบนเป็นศีรษะ (พอลลักซ์ซ้ายและคาสเตอร์ขวา) มีแขนยกโอบกอดกัน และมีขาทอดยาวลงมาเคียงคู่กัน!",
    funFact: "คาสเตอร์และพอลลักซ์เป็นพี่น้องฝาแฝดในเทพนิยายกรีก หนึ่งคนเก่งการต่อสู้ อีกคนเป็นอมตะ คอยปกป้องชาวเรือ!",
    starGuide: "ดาวพอลลักซ์ (Pollux) สีส้มทองอยู่ทางซ้าย และดาวคาสเตอร์ (Castor) สีขาวสว่างอยู่ทางขวา แขนของทั้งสองโอบกอดกันอย่างอบอุ่น",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 155, y: 125, r: 10, name: "พอลลักซ์ (Pollux - β Gem ศีรษะน้อง)", bayer: "β Gem", mag: 1.14, spect: "K0 III (ดาวยักษ์ส้ม มีดาวเคราะห์บริวาร)", bright: true, color: "#FFA502" },
      { id: 2, x: 145, y: 180, r: 6.5, name: "แคปปา เจมินอร์ม (κ Gem ไหล่ซ้ายพอลลักซ์)", bayer: "κ Gem", mag: 3.57, spect: "G8 III (ดาวยักษ์ส้มเหลือง)", bright: false, color: "#FFA502" },
      { id: 3, x: 195, y: 145, r: 5.5, name: "อิปซิลอน เจมินอร์ม (υ Gem แขนขวาพอลลักซ์)", bayer: "υ Gem", mag: 4.06, spect: "M0 III (ดาวยักษ์แดง)", bright: false, color: "#FF7675" },
      { id: 4, x: 205, y: 230, r: 7.0, name: "วาซัต (Wasat - δ Gem เอวพอลลักซ์)", bayer: "δ Gem", mag: 3.50, spect: "F0 IV (ดาวย่อยยักษ์เหลืองขาว)", bright: false, color: "#FFFFFF" },
      { id: 5, x: 235, y: 280, r: 6.0, name: "เมกบูดา (Mekbuda - ζ Gem เข่าขวาพอลลักซ์)", bayer: "ζ Gem", mag: 4.01, spect: "F7-G3 Ib (ดาวแปรแสงเซเฟอิด)", bright: false, color: "#FFD27D" },
      { id: 6, x: 335, y: 335, r: 9.0, name: "อัลฮีนา (Alhena - γ Gem ปลายเท้าพอลลักซ์)", bayer: "γ Gem", mag: 1.93, spect: "A1.5 IV (ดาวย่อยยักษ์ขาว)", bright: true, color: "#FFFFFF" },
      { id: 7, x: 200, y: 300, r: 6.5, name: "แลมบ์ดา เจมินอร์ม (λ Gem เข่าซ้ายพอลลักซ์)", bayer: "λ Gem", mag: 3.58, spect: "A3 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 8, x: 275, y: 365, r: 6.5, name: "อัลซีร์ (Alzirr - ξ Gem ปลายเท้าซ้ายพอลลักซ์)", bayer: "ξ Gem", mag: 3.35, spect: "F5 IV (ดาวเหลืองขาว)", bright: false, color: "#FFD27D" },

      { id: 9, x: 215, y: 85, r: 9.5, name: "คาสเตอร์ (Castor - α Gem ศีรษะพี่)", bayer: "α Gem", mag: 1.58, spect: "A1 V (ระบบดาวฤกษ์ 6 ดวง)", bright: true, color: "#FFFFFF" },
      { id: 10, x: 315, y: 75, r: 6.5, name: "ทีตา เจมินอร์ม (θ Gem ศอกขวายกคาสเตอร์)", bayer: "θ Gem", mag: 3.60, spect: "A3 III (ดาวยักษ์ขาว)", bright: false, color: "#FFFFFF" },
      { id: 11, x: 265, y: 125, r: 5.5, name: "เทา เจมินอร์ม (τ Gem มือขวาคาสเตอร์)", bayer: "τ Gem", mag: 4.41, spect: "K2 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 12, x: 235, y: 135, r: 6.5, name: "ไอโอตา เจมินอร์ม (ι Gem ไหล่ซ้ายคาสเตอร์)", bayer: "ι Gem", mag: 3.78, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 13, x: 305, y: 195, r: 7.5, name: "เมบซูดา (Mebsuta - ε Gem เอวคาสเตอร์)", bayer: "ε Gem", mag: 3.06, spect: "G8 Ib (ดาวยักษ์ใหญ่เหลือง)", bright: true, color: "#FFD27D" },
      { id: 14, x: 335, y: 260, r: 6.0, name: "นิว เจมินอร์ม (ν Gem เข่าขวาคาสเตอร์)", bayer: "ν Gem", mag: 4.13, spect: "B6 III (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 15, x: 370, y: 285, r: 5.5, name: "30 เจมินอร์ม (30 Gem ปลายเท้าขวาคาสเตอร์)", bayer: "30 Gem", mag: 4.49, spect: "K1 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 16, x: 385, y: 235, r: 7.5, name: "เทจัต (Tejat - μ Gem เข่าซ้ายคาสเตอร์)", bayer: "μ Gem", mag: 2.87, spect: "M3 III (ดาวยักษ์แดง)", bright: true, color: "#FF7675" },
      { id: 17, x: 410, y: 235, r: 6.5, name: "โพรพัส (Propus - η Gem ข้อเท้าซ้ายคาสเตอร์)", bayer: "η Gem", mag: 3.32, spect: "M3 III (ดาวยักษ์แดง)", bright: false, color: "#FF7675" },
      { id: 18, x: 445, y: 225, r: 5.5, name: "1 เจมินอร์ม (1 Gem ปลายเท้าซ้ายคาสเตอร์)", bayer: "1 Gem", mag: 4.15, spect: "G5 III (ดาวยักษ์เหลือง)", bright: false, color: "#FFD27D" }
    ],
    lines: [
      [1, 2], [1, 3], [2, 4], [4, 5], [5, 6], [4, 7], [7, 8],
      [9, 10], [10, 11], [11, 9], [9, 12], [12, 13], [13, 14], [14, 15], [13, 16], [16, 17], [17, 18],
      [3, 12], [4, 13], [5, 14]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <!-- Castor Silhouette (Right Brother) -->
        <g stroke="#70A1FF" stroke-width="2" fill="none" opacity="0.85">
          <!-- Head -->
          <circle cx="215" cy="85" r="22" fill="#70A1FF" fill-opacity="0.3" stroke="#1E90FF" stroke-width="2" />
          <!-- Torso & Tunic -->
          <path d="M 210 107 L 235 135 L 305 195 L 260 210 L 220 160 Z" fill="#70A1FF" fill-opacity="0.25" />
          <!-- Raised Right Arm -->
          <path d="M 215 85 L 315 75 L 265 125 Z" fill="#70A1FF" fill-opacity="0.2" stroke-width="3" stroke-linecap="round" />
          <!-- Legs -->
          <path d="M 305 195 L 335 260 L 370 285" stroke="#70A1FF" stroke-width="5" stroke-linecap="round" stroke-opacity="0.4" />
          <path d="M 305 195 L 385 235 L 410 235 L 445 225" stroke="#70A1FF" stroke-width="5" stroke-linecap="round" stroke-opacity="0.4" />
        </g>

        <!-- Pollux Silhouette (Left Brother) -->
        <g stroke="#FFA502" stroke-width="2" fill="none" opacity="0.85">
          <!-- Head -->
          <circle cx="155" cy="125" r="22" fill="#FFA502" fill-opacity="0.3" stroke="#FF7F50" stroke-width="2" />
          <!-- Torso & Tunic -->
          <path d="M 155 147 L 145 180 L 205 230 L 245 190 L 195 145 Z" fill="#FFA502" fill-opacity="0.25" />
          <!-- Left Arm -->
          <path d="M 145 180 L 125 210 L 135 240" stroke="#FFA502" stroke-width="4" stroke-linecap="round" stroke-opacity="0.4" />
          <!-- Legs -->
          <path d="M 205 230 L 235 280 L 335 335" stroke="#FFA502" stroke-width="5" stroke-linecap="round" stroke-opacity="0.4" />
          <path d="M 205 230 L 200 300 L 275 365" stroke="#FFA502" stroke-width="5" stroke-linecap="round" stroke-opacity="0.4" />
        </g>

        <!-- Warm Embracing Arms & Hands Connection -->
        <line x1="195" y1="145" x2="235" y2="135" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" filter="drop-shadow(0 0 6px #FFFFFF)" />
        <line x1="205" y1="230" x2="305" y2="195" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-dasharray="4,4" opacity="0.7" />
        <line x1="235" y1="280" x2="335" y2="260" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-dasharray="4,4" opacity="0.7" />
      </g>
    `
  },
  {
    id: "cancer",
    thaiName: "กลุ่มดาวปู",
    zodiacName: "ราศีกรกฎ (Cancer)",
    latinName: "Cancer",
    symbol: "♋",
    correctAnswer: "ปูน้อยก้ามโต",
    options: [
      { "text": "ปูน้อยก้ามโต", "icon": "🦀", "correct": true },
      { "text": "ผีเสื้อแสนสวย", "icon": "🦋", "correct": false },
      { "text": "ร่มกันฝน", "icon": "☂️", "correct": false },
      { "text": "กบกระโดด", "icon": "🐸", "correct": false }
    ],
    hint: "มีรูปตัว 'Y' กลับหัว โดยตรงกลางตัวมี 'กระจุกดาวรังผึ้ง' ระยิบระยับ และมีก้ามปูแยกออก!",
    funFact: "ใจกลางกระดองปูมีกระจุกดาวเปิดชื่อว่า 'รังผึ้ง' (Praesepe / M44) ประกอบด้วยดาวฤกษ์กว่า 1,000 ดวง!",
    starGuide: "กลุ่มดาวรูปตัว Y คว่ำ อยู่ตรงกลางระหว่างกลุ่มดาวคนคู่และกลุ่มดาวสิงโต",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 329, y: 355, r: 6.5, name: "อัลตาร์ฟ (Altarf - β Cnc ปลายก้ามใต้)", bayer: "β Cnc", mag: 3.53, spect: "K4 III (ดาวยักษ์ส้ม)", bright: true, color: "#FFA502" },
      { id: 2, x: 171, y: 313, r: 5.5, name: "อาคูเบนส์ (Acubens - α Cnc ก้ามตะวันออก)", bayer: "α Cnc", mag: 4.26, spect: "A5 m (ดาวระบบ 4 ดวง)", bright: false, color: "#FFFFFF" },
      { id: 3, x: 223, y: 213, r: 6.5, name: "อาเซลลัส ออสตราลิส (δ Cnc กลางกระดองใต้)", bayer: "δ Cnc", mag: 3.94, spect: "K0 III (ดาวยักษ์ส้ม)", bright: true, color: "#FFA502" },
      { id: 4, x: 228, y: 160, r: 5.5, name: "อาเซลลัส บอเรียลิส (γ Cnc กลางกระดองเหนือ)", bayer: "γ Cnc", mag: 4.66, spect: "A1 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 5, x: 215, y: 45, r: 5.5, name: "ไอโอตา แคนครี (ι Cnc ก้ามเหนือ)", bayer: "ι Cnc", mag: 4.03, spect: "G8 III (ดาวยักษ์เหลือง)", bright: false, color: "#FFD27D" },
      { id: 6, x: 239, y: 189, r: 7.5, name: "กระจุกดาวรังผึ้ง (Beehive / M44 Praesepe)", bayer: "M44", mag: 3.1, spect: "กระจุกดาวเปิด", bright: true, color: "#00F0FF" }
    ],
    lines: [
      [5, 4], [4, 3], [3, 2], [3, 1]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <ellipse cx="266" cy="200" rx="55" ry="42" fill="#FF4757" opacity="0.35" stroke="#FF6B81" stroke-width="2" />
        <circle cx="270" cy="203" r="25" fill="#00F0FF" opacity="0.2" filter="drop-shadow(0 0 10px #00F0FF)" />
        <path d="M 267 172 Q 220 110 263 50 Q 290 110 267 172 Z" fill="#FF4757" opacity="0.6" stroke="#FF6B81" stroke-width="2" />
        <path d="M 265 230 Q 210 280 165 335" stroke="#FFA502" stroke-width="6" stroke-linecap="round" />
        <path d="M 265 230 Q 300 300 335 381" stroke="#FFA502" stroke-width="6" stroke-linecap="round" />
        <circle cx="255" cy="165" r="5" fill="#FFFFFF" /><circle cx="255" cy="165" r="2.5" fill="#060919" />
        <circle cx="275" cy="165" r="5" fill="#FFFFFF" /><circle cx="275" cy="165" r="2.5" fill="#060919" />
      </g>
    `
  },
  {
    id: "leo",
    thaiName: "กลุ่มดาวสิงโต",
    zodiacName: "ราศีสิงห์ (Leo)",
    latinName: "Leo",
    symbol: "♌",
    correctAnswer: "สิงโตเจ้าป่า (หัวรูปเคียวเกี่ยวข้าว)",
    options: [
      { "text": "สิงโตเจ้าป่า (หัวรูปเคียวเกี่ยวข้าว)", "icon": "🦁", "correct": true },
      { "text": "กระรอกหางพวง", "icon": "🐿️", "correct": false },
      { "text": "ช้างตัวโต", "icon": "🐘", "correct": false },
      { "text": "เตารีดผ้าโบราณ", "icon": "🧼", "correct": false }
    ],
    hint: "มีส่วนหัวเป็นรูปโค้งเคียวเกี่ยวข้าว (The Sickle) และมีลำตัวรูปสามเหลี่ยมทอดไปหาหางสิงโต!",
    funFact: "ดาวที่สว่างที่สุดคือ 'เรกูลัส' (Regulus) หรือหัวใจสิงห์ หมุนรอบตัวเองเร็วมากจนตัวแบนคล้ายผลส้ม!",
    starGuide: "มองหาเคียวเกี่ยวข้าวทางทิศตะวันตกและดาวหัวใจสิงห์สีฟ้าขาวสว่างจ้า",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 380, y: 299, r: 9, name: "เรกูลัส (Regulus - α Leo หัวใจสิงห์)", bayer: "α Leo", mag: 1.36, spect: "B7 V (ดาวสีฟ้าขาว สว่างที่สุดในกลุ่มดาว)", bright: true, color: "#00F0FF" },
      { id: 2, x: 45, y: 262, r: 9, name: "เดเนโบลา (Denebola - β Leo หางสิงโต)", bayer: "β Leo", mag: 2.14, spect: "A3 V (ดาวแคระขาว)", bright: true, color: "#FFFFFF" },
      { id: 3, x: 341, y: 188, r: 9, name: "แอลเจอบา (Algieba - γ Leo คอสิงโต)", bayer: "γ Leo", mag: 2.01, spect: "K0 III (ดาวยักษ์ส้มคู่)", bright: true, color: "#FFA502" },
      { id: 4, x: 161, y: 178, r: 7.5, name: "โซสมา (Zosma - δ Leo สะโพกบน)", bayer: "δ Leo", mag: 2.56, spect: "A4 V (ดาวแคระขาว)", bright: true, color: "#FFFFFF" },
      { id: 5, x: 455, y: 133, r: 7.5, name: "อัลเกนูบี (Algenubi - ε Leo ยอดหัวสิงโต)", bayer: "ε Leo", mag: 2.97, spect: "G1 II (ดาวยักษ์สว่างเหลือง)", bright: false, color: "#FFD27D" },
      { id: 6, x: 352, y: 138, r: 6.5, name: "อัดฮาเฟรา (Adhafera - ζ Leo แผงคอ)", bayer: "ζ Leo", mag: 3.43, spect: "F0 III (ดาวยักษ์ขาว)", bright: false, color: "#FFFFFF" },
      { id: 7, x: 384, y: 231, r: 6.5, name: "อัลจับฮาห์ (Al Jabhah - η Leo อกสิงโต)", bayer: "η Leo", mag: 3.48, spect: "A0 Ib (ดาวยักษ์ใหญ่ขาว)", bright: false, color: "#FFFFFF" },
      { id: 8, x: 161, y: 250, r: 6.5, name: "เชอร์ทาน (Chertan - θ Leo สะโพกล่าง)", bayer: "θ Leo", mag: 3.33, spect: "A2 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 9, x: 432, y: 101, r: 6.5, name: "ราซาลาส (Rasalas - μ Leo ปลายจมูกสิงห์)", bayer: "μ Leo", mag: 3.88, spect: "K2 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" }
    ],
    lines: [
      [1, 7], [7, 3], [3, 6], [6, 9], [9, 5], [3, 4], [4, 2], [2, 8], [8, 1], [4, 8]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <circle cx="420" cy="110" r="50" fill="#FFA502" opacity="0.35" stroke="#FF7F50" stroke-width="2" />
        <circle cx="450" cy="85" r="4.5" fill="#060919" />
        <circle cx="452" cy="83" r="1.5" fill="#FFFFFF" />
        <path d="M 407 282 Q 430 200 376 153 Q 410 90 449 50 Q 480 80 469 87" 
              fill="none" stroke="#FFD700" stroke-width="4" stroke-linecap="round" />
        <path d="M 376 153 L 223 142 L 125 238 L 223 226 L 407 282 Z" fill="#FFA502" opacity="0.25" />
        <circle cx="407" cy="282" r="15" fill="#00F0FF" opacity="0.35" filter="drop-shadow(0 0 10px #00F0FF)" />
        <circle cx="125" cy="238" r="12" fill="#FF7F50" opacity="0.8" />
      </g>
    `
  },
  {
    id: "virgo",
    thaiName: "กลุ่มดาวหญิงสาว (เทพีพรหมจารี)",
    zodiacName: "ราศีกันย์ (Virgo)",
    latinName: "Virgo",
    symbol: "♍",
    correctAnswer: "หญิงสาวถือรวงข้าวสาลี",
    options: [
      { "text": "หญิงสาวถือรวงข้าวสาลี", "icon": "🌾", "correct": true },
      { "text": "ม้าน้ำในมหาสมุทร", "icon": "🫧", "correct": false },
      { "text": "กระต่ายหูยาว", "icon": "🐰", "correct": false },
      { "text": "ต้นสนวันคริสต์มาส", "icon": "🎄", "correct": false }
    ],
    hint: "มีดาวฤกษ์สว่างสีฟ้าขาว 'สไปกา' อยู่ที่รวงข้าวสาลี และมีเส้นลำตัวหญิงสาวกางปีกกว้าง!",
    funFact: "ดาว 'สไปกา' (Spica) เป็นระบบดาวคู่สีฟ้าขาว สว่างกว่าดวงอาทิตย์ถึง 12,000 เท่า!",
    starGuide: "ลากเส้นโค้งต่อจากด้ามกระบวยกลุ่มดาวหมีใหญ่ ผ่านดาวอาร์คทูรัส แล้วจะพุ่งตรงมายังดาวสไปกา",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 188, y: 325, r: 11, name: "สไปกา (Spica - α Vir รวงข้าวสาลี)", bayer: "α Vir", mag: 0.98, spect: "B1 III-IV (ดาวคู่ยักษ์ฟ้าขาว สว่างที่สุด)", bright: true, color: "#00F0FF" },
      { id: 2, x: 455, y: 179, r: 6.5, name: "ซาวิยาวา (Zavijava - β Vir ศีรษะ)", bayer: "β Vir", mag: 3.59, spect: "F9 V (ดาวสีเหลืองนวล)", bright: false, color: "#FFD27D" },
      { id: 3, x: 311, y: 215, r: 7.5, name: "พอริมา (Porrima - γ Vir ไหล่/อก)", bayer: "γ Vir", mag: 2.74, spect: "F0 V (ดาวคู่ขาวบริสุทธิ์)", bright: true, color: "#FFFFFF" },
      { id: 4, x: 272, y: 161, r: 6.5, name: "มิเนเลาวา (Minelauva - δ Vir เอว)", bayer: "δ Vir", mag: 3.38, spect: "M3 III (ดาวยักษ์แดง)", bright: false, color: "#FF4757" },
      { id: 5, x: 253, y: 75, r: 7.5, name: "วินเดเมียทริกซ์ (Vindemiatrix - ε Vir ปลายปีกขวา)", bayer: "ε Vir", mag: 2.85, spect: "G8 III (ดาวยักษ์เหลืองทอง)", bright: true, color: "#FFD27D" },
      { id: 6, x: 162, y: 192, r: 6.5, name: "เฮเซ (Heze - ζ Vir สะโพก)", bayer: "ζ Vir", mag: 3.38, spect: "A3 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 7, x: 373, y: 191, r: 6.5, name: "ซาเนียห์ (Zaniah - η Vir แขนซ้าย)", bayer: "η Vir", mag: 3.89, spect: "A2 IV (ดาวขาว)", bright: false, color: "#FFFFFF" },
      { id: 8, x: 45, y: 267, r: 5.5, name: "เซียร์มา (Syrma - ι Vir ชายกระโปรง/เท้า)", bayer: "ι Vir", mag: 4.07, spect: "F7 III (ดาวยักษ์เหลือง)", bright: false, color: "#FFD27D" },
      { id: 9, x: 54, y: 315, r: 5.5, name: "คัง (Kang - κ Vir ปลายเท้า)", bayer: "κ Vir", mag: 4.18, spect: "K2.5 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" }
    ],
    lines: [
      [2, 7], [7, 3], [3, 4], [4, 5], [4, 6], [6, 1], [3, 1], [1, 8], [8, 9]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <circle cx="444" cy="153" r="22" fill="#FDA7DF" opacity="0.4" stroke="#D980FA" stroke-width="2" />
        <path d="M 339 211 Q 310 100 296 50 Q 350 120 339 211" fill="#70A1FF" opacity="0.35" stroke="#1E90FF" stroke-width="2" />
        <polygon points="339,211 310,122 229,193 247,396 142,298 150,381" fill="#9980FA" opacity="0.25" stroke="#833471" stroke-width="2" />
        <ellipse cx="247" cy="396" rx="20" ry="14" fill="#F1C40F" opacity="0.7" stroke="#FFD700" stroke-width="2" filter="drop-shadow(0 0 12px #FFD700)" />
      </g>
    `
  },
  {
    id: "libra",
    thaiName: "กลุ่มดาวคันชั่ง",
    zodiacName: "ราศีตุล (Libra)",
    latinName: "Libra",
    symbol: "♎",
    correctAnswer: "ตาชั่งวัดความสมดุล",
    options: [
      { "text": "ตาชั่งวัดความสมดุล", "icon": "⚖️", "correct": true },
      { "text": "ว่าวสามเหลี่ยม", "icon": "🪁", "correct": false },
      { "text": "เต็นท์ตั้งแคมป์", "icon": "⛺", "correct": false },
      { "text": "เพชรประกายแสง", "icon": "💎", "correct": false }
    ],
    hint: "มีรูปทรงสี่เหลี่ยมข้าวหลามตัด มีคานบนและจานตาชั่งสองข้างถ่วงสมดุลกันอย่างสง่างาม!",
    funFact: "เป็นราศีเดียวใน 12 จักราศีที่เป็นสิ่งของเครื่องใช้ ดาวซูเบนเอลเชมาลีมีประกายสีเขียวมรกตที่หาได้ยากบนฟ้า!",
    starGuide: "ดาวซูเบนเอลเชมาลี (Zubeneschamali) อยู่ที่ยอดบน และดาวซูเบนเอลเกนูบี (Zubenelgenubi) อยู่ที่มุมล่างซ้าย",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 155, y: 290, r: 8.5, name: "ซูเบนเอลเกนูบี (Zubenelgenubi - α2 Lib จานใต้)", bayer: "α2 Lib", mag: 2.75, spect: "A3 IV (ดาวคู่ขาวสว่าง)", bright: true, color: "#FFD27D" },
      { id: 2, x: 275, y: 85, r: 9.0, name: "ซูเบนเอลเชมาลี (Zubeneschamali - β Lib ยอดคาน)", bayer: "β Lib", mag: 2.61, spect: "B8 V (ดาวสีฟ้าอมเขียวมรกต)", bright: true, color: "#00F0FF" },
      { id: 3, x: 395, y: 150, r: 7.0, name: "ซูเบนเอลอัครับ (Zubenelakrab - γ Lib จานตะวันออก)", bayer: "γ Lib", mag: 3.91, spect: "G8.5 III (ดาวยักษ์ส้มเหลือง)", bright: false, color: "#FFA502" },
      { id: 4, x: 350, y: 265, r: 7.5, name: "บราเคียม (Brachium - σ Lib ฐานล่าง)", bayer: "σ Lib", mag: 3.25, spect: "M2.5 III (ดาวยักษ์แดง)", bright: true, color: "#FF4757" }
    ],
    lines: [
      [1, 2], [2, 3], [3, 4], [4, 1]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <!-- Scale Balance Beam traversing through stars -->
        <path d="M 275 85 L 395 150 L 350 265 L 155 290 Z" fill="#FFA502" fill-opacity="0.12" stroke="#FFD700" stroke-width="1.5" stroke-dasharray="4,4" />
        
        <!-- Antique Balance Main Beam -->
        <path d="M 120 180 L 380 90" stroke="#FFD700" stroke-width="6" stroke-linecap="round" filter="drop-shadow(0 0 8px #FFD700)" />
        <circle cx="250" cy="135" r="9" fill="#FFA502" stroke="#FFD700" stroke-width="2" />
        
        <!-- Center Handle / Pointer -->
        <line x1="250" y1="135" x2="275" y2="85" stroke="#FFD700" stroke-width="4" stroke-linecap="round" />
        <line x1="250" y1="135" x2="290" y2="210" stroke="#FFA502" stroke-width="4" stroke-linecap="round" />

        <!-- Left Scale Pan (Upper-Left) with 3 Hanging Chains -->
        <line x1="120" y1="180" x2="95" y2="235" stroke="#FFFFFF" stroke-width="2" opacity="0.7" />
        <line x1="120" y1="180" x2="120" y2="240" stroke="#FFFFFF" stroke-width="2" opacity="0.7" />
        <line x1="120" y1="180" x2="145" y2="235" stroke="#FFFFFF" stroke-width="2" opacity="0.7" />
        <!-- Pan Dish -->
        <path d="M 85 235 Q 120 270 155 235 Z" fill="#FFA502" fill-opacity="0.45" stroke="#FFD700" stroke-width="2.5" />
        <ellipse cx="120" cy="235" rx="35" ry="8" fill="#FFD700" fill-opacity="0.3" stroke="#FFD700" stroke-width="1.5" />

        <!-- Right Scale Pan (Lower-Left / Bottom) with 3 Hanging Chains -->
        <line x1="200" y1="210" x2="175" y2="295" stroke="#FFFFFF" stroke-width="2" opacity="0.7" />
        <line x1="200" y1="210" x2="200" y2="300" stroke="#FFFFFF" stroke-width="2" opacity="0.7" />
        <line x1="200" y1="210" x2="225" y2="295" stroke="#FFFFFF" stroke-width="2" opacity="0.7" />
        <!-- Pan Dish -->
        <path d="M 165 295 Q 200 330 235 295 Z" fill="#FFA502" fill-opacity="0.45" stroke="#FFD700" stroke-width="2.5" />
        <ellipse cx="200" cy="295" rx="35" ry="8" fill="#FFD700" fill-opacity="0.3" stroke="#FFD700" stroke-width="1.5" />
      </g>
    `
  },
  {
    id: "scorpio",
    thaiName: "กลุ่มดาวแมงป่อง",
    zodiacName: "ราศีพิจิก (Scorpius)",
    latinName: "Scorpius",
    symbol: "♏",
    correctAnswer: "แมงป่องหางงอแหลมคม",
    options: [
      { "text": "แมงป่องหางงอแหลมคม", "icon": "🦂", "correct": true },
      { "text": "เบ็ดตกปลาโบราณ", "icon": "🎣", "correct": false },
      { "text": "ไดโนเสาร์คอยาว", "icon": "🦕", "correct": false },
      { "text": "มังกรพ่นไฟ", "icon": "🐉", "correct": false }
    ],
    hint: "มีก้าม 3 แฉกด้านหน้า มีหัวใจสีแดงแอนทาเรส และมีหางโค้งยาวรูปตัว J งอตวัดขึ้นพร้อมเหล็กใน!",
    funFact: "ใจกลางลำตัวมีดาว 'แอนทาเรส' ดาวยักษ์แดงมหึมาขนาดใหญ่กว่าดวงอาทิตย์กว่า 700 เท่า!",
    starGuide: "กลุ่มดาวรูปตัว J ชัดเจนที่สุดบนท้องฟ้าฤดูฝน มองหาดาวสีแดงแอนทาเรส",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 316, y: 133, r: 11, name: "แอนทาเรส (Antares - α Sco หัวใจสีแดง)", bayer: "α Sco", mag: 1.06, spect: "M1.5 Iab (ดาวยักษ์ใหญ่แดง สว่างสุด)", bright: true, color: "#FF4757" },
      { id: 2, x: 139, y: 274, r: 9, name: "ชอลา (Shaula - λ Sco ปลายเหล็กใน)", bayer: "λ Sco", mag: 1.62, spect: "B2 IV (ดาวย่อยยักษ์ฟ้าขาว)", bright: true, color: "#00F0FF" },
      { id: 3, x: 128, y: 352, r: 9, name: "ซาร์กัส (Sargas - θ Sco โค้งหางล่าง)", bayer: "θ Sco", mag: 1.86, spect: "F0 II (ดาวยักษ์สว่างเหลืองขาว)", bright: true, color: "#FFD27D" },
      { id: 4, x: 396, y: 82, r: 7.5, name: "ดชูบา (Dschubba - δ Sco หน้าผากแมงป่อง)", bayer: "δ Sco", mag: 2.29, spect: "B0.3 IV (ดาวย่อยยักษ์ฟ้า)", bright: true, color: "#00F0FF" },
      { id: 5, x: 258, y: 237, r: 7.5, name: "ลาราวาก (Larawag - ε Sco โคนหาง)", bayer: "ε Sco", mag: 2.29, spect: "K2.5 III (ดาวยักษ์ส้ม)", bright: true, color: "#FFA502" },
      { id: 6, x: 114, y: 299, r: 7.5, name: "เกอร์แทบ (Girtab - κ Sco หางตวัด)", bayer: "κ Sco", mag: 2.39, spect: "B1.5 III (ดาวยักษ์ฟ้าขาว)", bright: true, color: "#00F0FF" },
      { id: 7, x: 382, y: 45, r: 7.5, name: "กราฟเฟียส (Acrab - β Sco ก้ามบน)", bayer: "β Sco", mag: 2.56, spect: "B1 V (ดาวคู่ฟ้าขาว)", bright: true, color: "#00F0FF" },
      { id: 8, x: 147, y: 276, r: 7.5, name: "เลซัท (Lesath - υ Sco ปลายเหล็กในคู่)", bayer: "υ Sco", mag: 2.7, spect: "B2 IV (ดาวฟ้าขาว)", bright: true, color: "#00F0FF" },
      { id: 9, x: 400, y: 128, r: 7.5, name: "ฟาง (Fang - π Sco ก้ามล่าง)", bayer: "π Sco", mag: 2.89, spect: "B1 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 10, x: 338, y: 122, r: 7.5, name: "อัลนิยัต (Alniyat - σ Sco อกแมงป่อง)", bayer: "σ Sco", mag: 2.9, spect: "B1 III (ดาวยักษ์ฟ้า)", bright: false, color: "#00F0FF" },
      { id: 11, x: 298, y: 156, r: 7.5, name: "ไพเคาฮาเล (Tau Sco อกล่าง)", bayer: "τ Sco", mag: 2.82, spect: "B0.2 V (ดาวแคระน้ำเงินร้อนจัด)", bright: false, color: "#00F0FF" },
      { id: 12, x: 254, y: 286, r: 7.5, name: "มิว สกอร์ปี (μ1 Sco ท้อง)", bayer: "μ1 Sco", mag: 3.0, spect: "B1.5 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 13, x: 246, y: 343, r: 6.5, name: "เซตา สกอร์ปี (ζ2 Sco ก้นหาง)", bayer: "ζ2 Sco", mag: 3.62, spect: "K4 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 14, x: 198, y: 355, r: 6.5, name: "อีตา สกอร์ปี (η Sco)", bayer: "η Sco", mag: 3.32, spect: "F3 III-IV (ดาวย่อยยักษ์ขาว)", bright: false, color: "#FFFFFF" },
      { id: 15, x: 100, y: 314, r: 7.5, name: "ไอโอตา สกอร์ปี (ι1 Sco)", bayer: "ι1 Sco", mag: 2.99, spect: "F2 Ia (ดาวยักษ์ใหญ่เหลืองขาว)", bright: false, color: "#FFD27D" }
    ],
    lines: [
      [7, 4], [4, 9], [4, 10], [10, 1], [1, 11], [11, 5], [5, 12], [12, 13], [13, 14], [14, 3], [3, 15], [15, 6], [6, 2], [2, 8]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <path d="M 425 128 L 413 76 M 425 128 L 429 191" stroke="#FF4757" stroke-width="4" stroke-linecap="round" />
        <ellipse cx="357" cy="196" rx="26" ry="18" fill="#FF4757" opacity="0.4" stroke="#FF6B81" stroke-width="2" />
        <path d="M 342 229 C 310 320, 310 470, 195 497 C 150 490, 160 410, 203 388" 
              fill="none" stroke="#FF4757" stroke-width="12" stroke-linecap="round" opacity="0.35" />
        <circle cx="203" cy="388" r="14" fill="#00F0FF" opacity="0.5" filter="drop-shadow(0 0 10px #00F0FF)" />
      </g>
    `
  },
  {
    id: "sagittarius",
    thaiName: "กลุ่มดาวคนยิงธนู",
    zodiacName: "ราศีธนู (Sagittarius)",
    latinName: "Sagittarius",
    symbol: "♐",
    correctAnswer: "คนยิงธนู (เซนทอร์ครึ่งคนครึ่งม้า)",
    options: [
      { "text": "คนยิงธนู (เซนทอร์ครึ่งคนครึ่งม้า)", "icon": "🏹", "correct": true },
      { "text": "ปราสาทเจ้าหญิง", "icon": "🏰", "correct": false },
      { "text": "นกอินทรีสยายปีก", "icon": "🦅", "correct": false },
      { "text": "รถไฟเหาะตีลังกา", "icon": "🎢", "correct": false }
    ],
    hint: "มีเซนทอร์ครึ่งคนครึ่งม้ากำลังง้างคันธนูเล็งไปทางทิศตะวันตก มีทั้งคันธนู หัวธนู ผ้าคลุมไหล่ และขาม้า 4 ข้างครบถ้วน!",
    funFact: "ใจกลางทางช้างเผือก (Milky Way Galaxy) อันเป็นที่ตั้งของหลุมดำยักษ์มวลมหาศาล Sagittarius A* อยู่ตรงกลุ่มดาวนี้พอดี!",
    starGuide: "ดาวปลายลูกศรคือ อัลนาสล์ (Alnasl) อยู่ทางขวา เล็งคันธนูไปทางศูนย์กลางทางช้างเผือก",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 445, y: 215, r: 8.0, name: "อัลนาสล์ (Alnasl - γ2 Sgr ปลายลูกศร)", bayer: "γ2 Sgr", mag: 2.98, spect: "K0 III (ดาวยักษ์ส้ม)", bright: true, color: "#FFA502" },
      { id: 2, x: 375, y: 205, r: 8.0, name: "เคาส์ มีเดีย (Kaus Media - δ Sgr กลางคันธนู)", bayer: "δ Sgr", mag: 2.72, spect: "K3 III (ดาวยักษ์ส้ม)", bright: true, color: "#FFA502" },
      { id: 3, x: 370, y: 115, r: 8.0, name: "เคาส์ โบเรียลิส (Kaus Borealis - λ Sgr ปลายคันธนูบน)", bayer: "λ Sgr", mag: 2.82, spect: "K1 III (ดาวยักษ์ส้ม)", bright: true, color: "#FFA502" },
      { id: 4, x: 380, y: 275, r: 9.5, name: "เคาส์ ออสตราลิส (Kaus Australis - ε Sgr ปลายคันธนูล่าง)", bayer: "ε Sgr", mag: 1.79, spect: "B9.5 III (ดาวยักษ์ฟ้าขาว สว่างสุด)", bright: true, color: "#00F0FF" },
      { id: 5, x: 295, y: 165, r: 7.5, name: "ฟาย ซากิตตารี (φ Sgr ไหล่/อกคน)", bayer: "φ Sgr", mag: 3.17, spect: "B8.5 III (ดาวยักษ์ฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 6, x: 250, y: 150, r: 9.0, name: "นูนาคี (Nunki - σ Sgr หลัง/สายธนู)", bayer: "σ Sgr", mag: 2.05, spect: "B2.5 V (ดาวฟ้าขาว)", bright: true, color: "#00F0FF" },
      { id: 7, x: 240, y: 230, r: 8.0, name: "อัสเซลลา (Ascella - ζ Sgr ลำตัวม้า/ท้อง)", bayer: "ζ Sgr", mag: 2.60, spect: "A2.5 Va (ดาวคู่ขาว)", bright: true, color: "#FFFFFF" },
      { id: 8, x: 180, y: 180, r: 6.5, name: "เทา ซากิตตารี (τ Sgr สะโพกม้าบน)", bayer: "τ Sgr", mag: 3.32, spect: "K1 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 9, x: 220, y: 65, r: 7.5, name: "อัลบัลดาห์ (Albaldah - π Sgr ศีรษะคนยิงธนู)", bayer: "π Sgr", mag: 2.88, spect: "F2 II (ดาวยักษ์สว่างเหลืองขาว)", bright: true, color: "#FFD27D" },
      { id: 10, x: 185, y: 85, r: 6.5, name: "ซี2 ซากิตตารี (ξ2 Sgr ผ้าคลุมไหล่)", bayer: "ξ2 Sgr", mag: 3.52, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 11, x: 115, y: 205, r: 6.0, name: "52 ซากิตตารี (52 Sgr บั้นท้ายม้า)", bayer: "52 Sgr", mag: 4.59, spect: "B8 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 12, x: 170, y: 350, r: 6.5, name: "รุคบัต (Rukbat - α Sgr ขาหลังม้า)", bayer: "α Sgr", mag: 3.96, spect: "B8 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 13, x: 235, y: 360, r: 6.5, name: "อาร์คับ (Arkab - β Sgr กีบเท้าหลังม้า)", bayer: "β Sgr", mag: 3.96, spect: "B9 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 14, x: 340, y: 335, r: 7.0, name: "อีตา ซากิตตารี (η Sgr ขาหน้าม้า)", bayer: "η Sgr", mag: 3.10, spect: "M3.5 III (ดาวยักษ์แดง)", bright: false, color: "#FF7675" },
      { id: 15, x: 380, y: 365, r: 6.0, name: "ทีตา1 ซากิตตารี (θ1 Sgr กีบเท้าหน้าม้า)", bayer: "θ1 Sgr", mag: 4.35, spect: "B2.5 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" }
    ],
    lines: [
      [1, 2], [3, 2], [2, 4], [1, 4],
      [3, 5], [5, 2], [5, 6], [6, 8], [8, 7], [7, 4], [7, 5],
      [6, 9], [9, 10], [10, 8], [10, 6],
      [8, 11], [11, 12], [12, 13], [13, 7],
      [4, 14], [14, 15]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <!-- Bow and Arrow (Aiming West / Right) -->
        <path d="M 370 115 Q 395 195 380 275" stroke="#FFD700" stroke-width="6" stroke-linecap="round" fill="none" filter="drop-shadow(0 0 8px #FFD700)" />
        <line x1="445" y1="215" x2="250" y2="150" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />
        <polygon points="445,215 425,205 425,225" fill="#FFD700" />

        <!-- Centaur Human Torso & Head -->
        <circle cx="220" cy="65" r="18" fill="#FFEAA7" opacity="0.4" stroke="#F1C40F" stroke-width="2" />
        <path d="M 220 83 L 295 165 L 240 230 L 180 180 Z" fill="#9980FA" fill-opacity="0.3" stroke="#833471" stroke-width="1.5" />
        <!-- Flowing Cape -->
        <path d="M 220 65 Q 160 50 140 100 Q 185 85 250 150 Z" fill="#70A1FF" fill-opacity="0.4" stroke="#1E90FF" stroke-width="1.5" />

        <!-- Centaur Horse Body & Legs -->
        <path d="M 180 180 L 115 205 L 170 350 L 235 360 L 240 230 Z" fill="#FFA502" fill-opacity="0.25" stroke="#FF7F50" stroke-width="2" />
        <!-- Front Horse Legs -->
        <path d="M 240 230 L 340 335 L 380 365" stroke="#FFA502" stroke-width="6" stroke-linecap="round" stroke-opacity="0.4" />
      </g>
    `
  },
  {
    id: "capricorn",
    thaiName: "กลุ่มดาวมกร (แพะทะเล)",
    zodiacName: "ราศีมังกร (Capricornus)",
    latinName: "Capricornus",
    symbol: "♑",
    correctAnswer: "แพะทะเล (ตัวเป็นแพะ หางเป็นปลา)",
    options: [
      { "text": "แพะทะเล (ตัวเป็นแพะ หางเป็นปลา)", "icon": "🐐", "correct": true },
      { "text": "หมวกโจรสลัด", "icon": "🏴‍☠️", "correct": false },
      { "text": "ชิ้นพิซซ่าสามเหลี่ยม", "icon": "🍕", "correct": false },
      { "text": "กางเกงใน", "icon": "🩲", "correct": false }
    ],
    hint: "มีรูปสามเหลี่ยมโค้งขนาดใหญ่ คล้ายรูปทรงเรือหรือแพะวิเศษที่มีหางปลาแหวกว่ายน้ำ!",
    funFact: "ในตำนาน เทพแพะแพนโดดหนีสัตว์ประหลาดไทฟอนลงแม่น้ำไนล์ ร่างกายครึ่งล่างจึงกลายเป็นหางปลา!",
    starGuide: "ดาวหัวแพะคู่คือ อัลเจดี และ ดาบิห์ ทางทิศตะวันตก",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 45, y: 130, r: 7.5, name: "เดเนบ อัลเจดี (Deneb Algedi - δ Cap หางปลา)", bayer: "δ Cap", mag: 2.85, spect: "A7m III (ดาวยักษ์ขาว สว่างสุด)", bright: true, color: "#FFFFFF" },
      { id: 2, x: 441, y: 104, r: 7.5, name: "ดาบิห์ (Dabih - β Cap เขาแพะ)", bayer: "β Cap", mag: 3.05, spect: "F8 V (ดาวระบบหลายดวง)", bright: true, color: "#FFA502" },
      { id: 3, x: 455, y: 60, r: 6.5, name: "อัลเจดี (Algedi - α2 Cap เขาแพะบน)", bayer: "α2 Cap", mag: 3.58, spect: "G8.5 III (ดาวยักษ์เหลือง)", bright: false, color: "#FFD27D" },
      { id: 4, x: 77, y: 140, r: 6.5, name: "นาชิรา (Nashira - γ Cap ครีบหาง)", bayer: "γ Cap", mag: 3.69, spect: "A7m III-IV (ดาวย่อยยักษ์ขาว)", bright: false, color: "#FFFFFF" },
      { id: 5, x: 139, y: 252, r: 6.5, name: "เซตา แคปริคอร์นิ (ζ Cap ท้องปลาล่าง)", bayer: "ζ Cap", mag: 3.77, spect: "G4 Ib (ดาวยักษ์ใหญ่เหลือง)", bright: false, color: "#FFD27D" },
      { id: 6, x: 234, y: 151, r: 5.5, name: "ทีตา แคปริคอร์นิ (θ Cap สันหลังกลาง)", bayer: "θ Cap", mag: 4.08, spect: "A1 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 7, x: 299, y: 340, r: 5.5, name: "โอเมกา แคปริคอร์นิ (ω Cap ก้นสามเหลี่ยม)", bayer: "ω Cap", mag: 4.12, spect: "K4 III (ดาวยักษ์ส้มแดง)", bright: false, color: "#FFA502" },
      { id: 8, x: 326, y: 308, r: 5.5, name: "ไซ แคปริคอร์นิ (ψ Cap ท้องล่างหน้า)", bayer: "ψ Cap", mag: 4.13, spect: "F5 V (ดาวเหลืองขาว)", bright: false, color: "#FFD27D" },
      { id: 9, x: 159, y: 144, r: 5.5, name: "ไอโอตา แคปริคอร์นิ (ι Cap หลัง)", bayer: "ι Cap", mag: 4.28, spect: "G8 III (ดาวยักษ์เหลือง)", bright: false, color: "#FFD27D" }
    ],
    lines: [
      [3, 2], [2, 8], [8, 7], [7, 5], [5, 4], [4, 1], [2, 6], [6, 9], [9, 4]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <circle cx="435" cy="120" r="26" fill="#FFEAA7" opacity="0.4" stroke="#F1C40F" stroke-width="2" />
        <path d="M 439 102 Q 460 60 480 80" fill="none" stroke="#FFD700" stroke-width="6" stroke-linecap="round" />
        <polygon points="431,139 348,340 203,161" fill="#1DD1A1" opacity="0.25" stroke="#10AC84" stroke-width="2" />
        <path d="M 203 161 Q 150 120 170 130 Q 140 180 203 161 Z" fill="#1DD1A1" opacity="0.7" stroke="#10AC84" stroke-width="2" />
      </g>
    `
  },
  {
    id: "aquarius",
    thaiName: "กลุ่มดาวคนแบกหม้อน้ำ",
    zodiacName: "ราศีกุมภ์ (Aquarius)",
    latinName: "Aquarius",
    symbol: "♒",
    correctAnswer: "คนเทน้ำจากเหยือกวิเศษ",
    options: [
      { "text": "คนเทน้ำจากเหยือกวิเศษ", "icon": "🏺", "correct": true },
      { "text": "จรวดพุ่งสู่ดวงจันทร์", "icon": "🚀", "correct": false },
      { "text": "พัดลมตั้งโต๊ะ", "icon": "🪭", "correct": false },
      { "text": "แมวเหมียวกำลังนอน", "icon": "🐱", "correct": false }
    ],
    hint: "มีรูปคนยกแขนถือเหยือกน้ำรูปตัว 'Y' บนบ่า และเทสายน้ำทอดคดเคี้ยวลงมาเกิดเป็นแอ่งน้ำกระเซ็นอยู่ด้านล่าง!",
    funFact: "น้ำที่เทลงมาจากเหยือกคือสายน้ำแห่งชีวิตในตำนาน ไหลลงสู่ปากปลาในกลุ่มดาวปลาทางใต้ (Piscis Austrinus)!",
    starGuide: "มองหาดาว 'ซาดาลซูด' (Sadalsuud) และ 'ซาดาลเมลิก' (Sadalmelik) ตรงหัวไหล่คนเทน้ำ และสายน้ำที่ไหลลงด้านล่าง",
    viewBox: "0 0 500 400",
    stars: [
      { id: 1, x: 430, y: 55, r: 6.5, name: "98 แอควารี (b2 Aqr มือขวายกสูง)", bayer: "b2 Aqr", mag: 3.97, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 2, x: 335, y: 125, r: 8.5, name: "ซาดาลซูด (Sadalsuud - β Aqr ไหล่ซ้าย)", bayer: "β Aqr", mag: 2.90, spect: "G0 Ib (ดาวยักษ์ใหญ่เหลือง สว่างสุด)", bright: true, color: "#FFD27D" },
      { id: 3, x: 245, y: 175, r: 8.5, name: "ซาดาลเมลิก (Sadalmelik - α Aqr ไหล่ขวา)", bayer: "α Aqr", mag: 2.95, spect: "G2 Ib (ดาวยักษ์ใหญ่เหลือง)", bright: true, color: "#FFD27D" },
      { id: 4, x: 195, y: 190, r: 6.5, name: "ซาดาคเบีย (Sadachbia - γ Aqr คอเหยือก Y)", bayer: "γ Aqr", mag: 3.86, spect: "A0 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 5, x: 175, y: 180, r: 6.5, name: "เซตา แอควารี (ζ Aqr กลางปากเหยือก)", bayer: "ζ Aqr", mag: 3.65, spect: "F2 IV (ดาวคู่ขาว)", bright: false, color: "#FFFFFF" },
      { id: 6, x: 160, y: 160, r: 6.0, name: "อีตา แอควารี (η Aqr ปลายเหยือกบน)", bayer: "η Aqr", mag: 4.04, spect: "B9 IV-Vn (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 7, x: 155, y: 205, r: 5.5, name: "พาย แอควารี (π Aqr ยอดเหยือกล่าง)", bayer: "π Aqr", mag: 4.66, spect: "B1 Ve (ดาวสีฟ้า)", bright: false, color: "#00F0FF" },
      { id: 8, x: 265, y: 270, r: 6.5, name: "อันชา (Ancha - θ Aqr สะโพก/เอว)", bayer: "θ Aqr", mag: 4.17, spect: "G8 III-IV (ดาวย่อยยักษ์เหลือง)", bright: false, color: "#FFD27D" },
      { id: 9, x: 385, y: 205, r: 6.5, name: "อัลบาลิ (Albali - ε Aqr มือซ้ายจับเหยือก)", bayer: "ε Aqr", mag: 3.78, spect: "A1.5 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 10, x: 155, y: 260, r: 7.0, name: "ไฮดอร์ (Hydor - λ Aqr สายน้ำช่วงบน)", bayer: "λ Aqr", mag: 3.73, spect: "M2.5 IIIa (ดาวยักษ์แดง)", bright: false, color: "#FF7675" },
      { id: 11, x: 185, y: 320, r: 6.0, name: "เทา2 แอควารี (τ2 Aqr สายน้ำช่วงกลาง)", bayer: "τ2 Aqr", mag: 4.01, spect: "M0 III (ดาวยักษ์แดงส้ม)", bright: false, color: "#FFA502" },
      { id: 12, x: 220, y: 335, r: 7.5, name: "สแคต (Skat - δ Aqr ขา/สายน้ำ)", bayer: "δ Aqr", mag: 3.27, spect: "A3 V (ดาวแคระขาว)", bright: true, color: "#FFFFFF" },
      { id: 13, x: 235, y: 380, r: 7.0, name: "88 แอควารี (c2 Aqr แอ่งน้ำกระเซ็นล่าง)", bayer: "c2 Aqr", mag: 3.68, spect: "K1 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 14, x: 200, y: 395, r: 5.5, name: "ไซ1 แอควารี (ψ1 Aqr ละอองน้ำซ้าย)", bayer: "ψ1 Aqr", mag: 4.21, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 15, x: 270, y: 390, r: 5.5, name: "ไซ2 แอควารี (ψ2 Aqr ละอองน้ำขวา)", bayer: "ψ2 Aqr", mag: 4.39, spect: "B5 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" },
      { id: 16, x: 320, y: 350, r: 6.0, name: "ไอโอตา แอควารี (ι Aqr ขาหลัง)", bayer: "ι Aqr", mag: 4.29, spect: "B9 V (ดาวฟ้าขาว)", bright: false, color: "#00F0FF" }
    ],
    lines: [
      [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [5, 7],
      [3, 8], [2, 9], [9, 8], [8, 16], [8, 12],
      [5, 10], [10, 11], [11, 12], [12, 13], [13, 14], [13, 15]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <!-- Water Bearer Silhouette -->
        <circle cx="340" cy="80" r="20" fill="#FFEAA7" opacity="0.4" stroke="#F1C40F" stroke-width="2" />
        <!-- Raised Right Arm -->
        <path d="M 340 80 L 430 55" stroke="#FFEAA7" stroke-width="5" stroke-linecap="round" opacity="0.4" />
        <!-- Torso & Robe -->
        <polygon points="335,125 245,175 265,270 385,205" fill="#70A1FF" fill-opacity="0.3" stroke="#1E90FF" stroke-width="1.5" />
        <!-- Legs Kneeling -->
        <path d="M 265 270 L 220 335 L 235 380" stroke="#70A1FF" stroke-width="5" stroke-linecap="round" stroke-opacity="0.35" />
        <path d="M 265 270 L 320 350" stroke="#70A1FF" stroke-width="5" stroke-linecap="round" stroke-opacity="0.35" />

        <!-- Water Urn at Stars 3 / 4 / 5 -->
        <ellipse cx="180" cy="180" rx="22" ry="30" transform="rotate(-30 180 180)" fill="#E17055" fill-opacity="0.5" stroke="#FF7675" stroke-width="2.5" />

        <!-- Cascading Luminous Flowing Water Stream -->
        <path d="M 175 180 Q 140 240 155 260 Q 170 290 185 320 Q 210 350 235 380" 
              fill="none" stroke="#00F0FF" stroke-width="8" stroke-linecap="round" opacity="0.75" filter="drop-shadow(0 0 10px #00F0FF)" />
        <path d="M 185 190 Q 150 250 165 270 Q 180 300 195 330 Q 220 360 235 380" 
              fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.8" />

        <!-- Splashing Pool Water at Bottom -->
        <ellipse cx="235" cy="385" rx="45" ry="14" fill="#00F0FF" fill-opacity="0.3" stroke="#00F0FF" stroke-width="2" filter="drop-shadow(0 0 8px #00F0FF)" />
      </g>
    `
  },
  {
    id: "pisces",
    thaiName: "กลุ่มดาวปลาคู่",
    zodiacName: "ราศีมีน (Pisces)",
    latinName: "Pisces",
    symbol: "♓",
    correctAnswer: "ปลา 2 ตัวผูกริบบิ้นที่หาง",
    options: [
      { "text": "ปลา 2 ตัวผูกริบบิ้นที่หาง", "icon": "🐟", "correct": true },
      { "text": "แว่นตาขยาย", "icon": "🔍", "correct": false },
      { "text": "กรรไกรตัดกระดาษ", "icon": "✂️", "correct": false },
      { "text": "ผึ้งน้อยบินตอมดอกไม้", "icon": "🐝", "correct": false }
    ],
    hint: "มีปลาสองตัว ตัวหนึ่งว่ายขึ้นสู่ทิศเหนือ อีกตัวว่ายไปทางทิศตะวันตก โดยหางของทั้งสองผูกริบบิ้นเชื่อมติดกันที่ดาวอัลริชา!",
    funFact: "ปลาสองตัวนี้คือ เทพีอโฟรไดต์กับบุตรชายคิวปิด แปลงร่างเป็นปลาแล้วผูกริบบิ้นไว้ด้วยกันเพื่อไม่ให้พลัดหลงในสายน้ำ!",
    starGuide: "ดาวตรงปมริบบิ้นเชื่อมปลาทั้งสองตัวคือ 'อัลริชา' (Alrescha) อยู่ที่จุดล่างสุดรูปตัว V",
    viewBox: "0 0 500 400",
    stars: [
      // Northern Fish (Upper Right)
      { id: 1, x: 405, y: 65, r: 8.5, name: "อัลเฟิร์ก (Alpherg - η Psc หัวปลาเหนือ)", bayer: "η Psc", mag: 3.62, spect: "G7 IIIa (ดาวยักษ์เหลือง สว่างสุด)", bright: true, color: "#FFD27D" },
      { id: 2, x: 380, y: 95, r: 6.5, name: "ไค พิสเซียม (χ Psc ครีบซ้ายปลาเหนือ)", bayer: "χ Psc", mag: 4.66, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 3, x: 385, y: 140, r: 6.5, name: "ฟาย พิสเซียม (φ Psc หลังปลาเหนือ)", bayer: "φ Psc", mag: 4.65, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 4, x: 430, y: 155, r: 7.0, name: "อิปซิลอน พิสเซียม (υ Psc โคนหางปลาเหนือ)", bayer: "υ Psc", mag: 4.74, spect: "A3 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 5, x: 425, y: 105, r: 6.5, name: "โร พิสเซียม (ρ Psc ท้องปลาเหนือ)", bayer: "ρ Psc", mag: 5.35, spect: "F2 V (ดาวเหลืองขาว)", bright: false, color: "#FFD27D" },

      // Western Fish Circlet (Center Left)
      { id: 6, x: 125, y: 240, r: 6.5, name: "7 พิสเซียม (7 Psc ปลายปากปลาตะวันตก)", bayer: "7 Psc", mag: 5.05, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 7, x: 150, y: 215, r: 7.5, name: "แกมมา พิสเซียม (γ Psc หน้าผากปลา)", bayer: "γ Psc", mag: 3.70, spect: "G8 III (ดาวยักษ์เหลืองส้ม)", bright: true, color: "#FFA502" },
      { id: 8, x: 190, y: 215, r: 6.5, name: "ทีตา พิสเซียม (θ Psc สันหลังปลา)", bayer: "θ Psc", mag: 4.27, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 9, x: 230, y: 245, r: 6.5, name: "ไอโอตา พิสเซียม (ι Psc โคนหางปลา)", bayer: "ι Psc", mag: 4.13, spect: "F7 V (ดาวเหลืองขาว)", bright: false, color: "#FFD27D" },
      { id: 10, x: 260, y: 255, r: 6.0, name: "ทีเอ็กซ์ พิสเซียม (TX Psc ปลายหางปลา)", bayer: "19 Psc", mag: 4.95, spect: "C5 II (ดาวคาร์บอนแดง)", bright: false, color: "#FF7675" },
      { id: 11, x: 215, y: 285, r: 6.5, name: "แลมบ์ดา พิสเซียม (λ Psc ท้องปลา)", bayer: "λ Psc", mag: 4.49, spect: "A7 V (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },
      { id: 12, x: 160, y: 265, r: 6.5, name: "แคปปา พิสเซียม (κ Psc คางปลา)", bayer: "κ Psc", mag: 4.95, spect: "A0p (ดาวแคระขาว)", bright: false, color: "#FFFFFF" },

      // Northern Cord (Connecting North Fish Tail to Alrescha)
      { id: 13, x: 375, y: 205, r: 6.0, name: "โอไมครอน พิสเซียม (ο Psc สายริบบิ้นเหนือ 1)", bayer: "ο Psc", mag: 4.26, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 14, x: 355, y: 265, r: 6.0, name: "นิว พิสเซียม (ν Psc สายริบบิ้นเหนือ 2)", bayer: "ν Psc", mag: 4.45, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 15, x: 350, y: 320, r: 6.0, name: "มิว พิสเซียม (μ Psc สายริบบิ้นเหนือ 3)", bayer: "μ Psc", mag: 4.84, spect: "K4 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 16, x: 340, y: 360, r: 6.0, name: "ไซ พิสเซียม (ξ Psc สายริบบิ้นเหนือ 4)", bayer: "ξ Psc", mag: 4.61, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },

      // Knot Star
      { id: 17, x: 320, y: 385, r: 9.0, name: "อัลริชา (Alrescha - α Psc ปมผูกริบบิ้น)", bayer: "α Psc", mag: 3.82, spect: "A0p (ดาวคู่ขาว ปมริบบิ้น)", bright: true, color: "#FFFFFF" },

      // Western Cord (Connecting West Fish Tail to Alrescha)
      { id: 18, x: 250, y: 285, r: 6.0, name: "เดลตา พิสเซียม (δ Psc สายริบบิ้นตะวันตก 1)", bayer: "δ Psc", mag: 4.44, spect: "K5 III (ดาวยักษ์ส้มแดง)", bright: false, color: "#FFA502" },
      { id: 19, x: 265, y: 330, r: 6.0, name: "เอปซิลอน พิสเซียม (ε Psc สายริบบิ้นตะวันตก 2)", bayer: "ε Psc", mag: 4.27, spect: "K0 III (ดาวยักษ์ส้ม)", bright: false, color: "#FFA502" },
      { id: 20, x: 290, y: 365, r: 6.0, name: "เซตา พิสเซียม (ζ Psc สายริบบิ้นตะวันตก 3)", bayer: "ζ Psc", mag: 5.21, spect: "A7 IV (ดาวขาว)", bright: false, color: "#FFFFFF" }
    ],
    lines: [
      // Northern Fish Body
      [1, 2], [2, 3], [3, 4], [4, 5], [5, 1],
      // Western Fish Body (Circlet)
      [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 6],
      // Northern Cord
      [4, 13], [13, 14], [14, 15], [15, 16], [16, 17],
      // Western Cord
      [10, 18], [18, 19], [19, 20], [20, 17]
    ],
    artOverlay: `
      <g class="overlay-graphic" opacity="0.9">
        <!-- Northern Fish Artwork (Swimming North/Up) -->
        <g stroke="#55EFC4" stroke-width="2" fill="none">
          <ellipse cx="405" cy="110" rx="42" ry="22" transform="rotate(75 405 110)" fill="#55EFC4" fill-opacity="0.35" stroke="#1DD1A1" stroke-width="2" />
          <polygon points="405,65 390,40 420,40" fill="#1DD1A1" opacity="0.7" />
          <!-- Tail Fin -->
          <path d="M 405 155 Q 380 185 390 195 Q 405 170 420 195 Q 430 185 405 155 Z" fill="#1DD1A1" fill-opacity="0.6" />
        </g>

        <!-- Western Fish Artwork (Swimming West/Left) -->
        <g stroke="#FF6B81" stroke-width="2" fill="none">
          <ellipse cx="190" cy="250" rx="55" ry="26" fill="#FF6B81" fill-opacity="0.35" stroke="#FF4757" stroke-width="2" />
          <polygon points="125,240 100,225 100,255" fill="#FF4757" opacity="0.7" />
          <!-- Tail Fin -->
          <path d="M 245 250 Q 275 225 285 235 Q 260 250 285 265 Q 275 275 245 250 Z" fill="#FF4757" fill-opacity="0.6" />
        </g>

        <!-- Flowing Ribbon / Cord -->
        <!-- North Ribbon -->
        <path d="M 405 170 Q 380 205 355 265 Q 345 320 320 385" 
              fill="none" stroke="#FFD700" stroke-width="4" stroke-linecap="round" opacity="0.8" filter="drop-shadow(0 0 6px #FFD700)" />
        <!-- West Ribbon -->
        <path d="M 260 255 Q 255 300 270 335 Q 290 365 320 385" 
              fill="none" stroke="#FFD700" stroke-width="4" stroke-linecap="round" opacity="0.8" filter="drop-shadow(0 0 6px #FFD700)" />

        <!-- Shimmering Ribbon Knot at Star 17 Alrescha -->
        <circle cx="320" cy="385" r="13" fill="#FFD700" stroke="#FFA502" stroke-width="3" filter="drop-shadow(0 0 10px #FFD700)" />
        <circle cx="320" cy="385" r="5" fill="#FFFFFF" />
      </g>
    `
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CONSTELLATIONS_DATA };
}
"""

with open("js/constellations.js", "w", encoding="utf-8") as f:
    f.write(constellations_js_template)

print("Generated js/constellations.js successfully!")
