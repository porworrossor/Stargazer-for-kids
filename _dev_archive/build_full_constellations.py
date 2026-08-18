# -*- coding: utf-8 -*-
"""
Upgraded Generator for all 12 Zodiac Constellations with FULL star details and IAU stick figures
Includes complete Gemini (both twins with both arms and legs), complete Leo, Taurus, Virgo, Scorpius, etc.
"""
import math
import json

def ra_deg(h, m, s=0.0):
    return (h + m/60.0 + s/3600.0) * 15.0

def dec_deg(d, m, s=0.0):
    sign = -1.0 if d < 0 else 1.0
    return sign * (abs(d) + m/60.0 + s/3600.0)

DATA = [
    # 1. ARIES (แกะ)
    {
        "id": "aries",
        "thaiName": "กลุ่มดาวแกะ",
        "zodiacName": "ราศีเมษ (Aries)",
        "latinName": "Aries",
        "symbol": "♈",
        "correctAnswer": "แกะตัวผู้ (มีเขาโค้ง)",
        "options": [
            {"text": "แกะตัวผู้ (มีเขาโค้ง)", "icon": "🐏", "correct": True},
            {"text": "นกพิราบกางปีก", "icon": "🕊️", "correct": False},
            {"text": "หนังสติ๊กยิงนก", "icon": "🌱", "correct": False},
            {"text": "คันธนูและลูกศร", "icon": "🏹", "correct": False}
        ],
        "hint": "มองหาดาวสว่าง 3 ดวงเรียงโค้งคล้ายเขาแกะ โดยมีดาวฮามัลสว่างสุดอยู่ตรงสันเขา!",
        "funFact": "ราศีแรกของจักรราศี ในตำนานกรีกคือ 'แกะขนทองคำ' (Chrysomallos) ที่บินข้ามมหาสมุทรเพื่อช่วยเหลือเจ้าชาย!",
        "starGuide": "ดาวสว่างสีส้ม 'ฮามัล' (Hamal) อยู่ตรงสันเขา และดาว 'เชอราทาน' กับ 'เมซาร์ทิม' อยู่ตรงปลายเขาแกะ",
        "stars": [
            {"id": 1, "name": "ฮามัล (Hamal - α Ari)", "bayer": "α Ari", "ra": ra_deg(2, 7, 10.4), "dec": dec_deg(23, 27, 45), "mag": 2.00, "spect": "K2 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": True},
            {"id": 2, "name": "เชอราทาน (Sheratan - β Ari)", "bayer": "β Ari", "ra": ra_deg(1, 54, 38.4), "dec": dec_deg(20, 48, 29), "mag": 2.64, "spect": "A5 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 3, "name": "เมซาร์ทิม (Mesarthim - γ Ari)", "bayer": "γ Ari", "ra": ra_deg(1, 53, 31.8), "dec": dec_deg(19, 17, 38), "mag": 3.88, "spect": "A1 V (ดาวคู่ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 4, "name": "โบเทน (Botein - δ Ari)", "bayer": "δ Ari", "ra": ra_deg(3, 11, 37.7), "dec": dec_deg(19, 43, 36), "mag": 4.35, "spect": "K2 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 5, "name": "ภารณี (Bharani - 41 Ari)", "bayer": "41 Ari", "ra": ra_deg(2, 49, 59.0), "dec": dec_deg(27, 15, 38), "mag": 3.61, "spect": "B8 V (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False},
            {"id": 6, "name": "39 แอรีเอทิส (39 Ari)", "bayer": "39 Ari", "ra": ra_deg(2, 47, 54.4), "dec": dec_deg(29, 14, 51), "mag": 4.51, "spect": "K1 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [4, 1], [1, 2], [2, 3], [1, 5], [5, 6]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Ram Curved Horn (tracing stars 1 Hamal -> 2 Sheratan -> 3 Mesarthim) -->
        <path d="M 370 200 Q 425 220 440 258 Q 455 280 445 292 Q 430 295 428 275" 
              fill="none" stroke="#FFD700" stroke-width="8" stroke-linecap="round" filter="drop-shadow(0 0 10px #FFD700)" />
        <path d="M 360 195 Q 410 215 425 248 Q 438 268 432 278" 
              fill="none" stroke="#FFA502" stroke-width="4" stroke-linecap="round" />
        <!-- Ram Head Profile at Star 1 Hamal -->
        <circle cx="350" cy="215" r="38" fill="#FFEAA7" opacity="0.4" stroke="#F1C40F" stroke-width="2" />
        <circle cx="365" cy="210" r="4.5" fill="#060919" />
        <circle cx="367" cy="208" r="1.5" fill="#FFFFFF" />
        <ellipse cx="378" cy="230" rx="7" ry="5" fill="#FF7675" opacity="0.6" />
        <!-- Ram Body extending west to 41 Ari and Botein -->
        <ellipse cx="220" cy="215" rx="130" ry="65" fill="#70A1FF" opacity="0.25" stroke="#1E90FF" stroke-width="2" />
        <!-- Legs -->
        <line x1="130" y1="265" x2="120" y2="345" stroke="#FFEAA7" stroke-width="5" stroke-linecap="round" />
        <line x1="190" y1="275" x2="185" y2="350" stroke="#FFEAA7" stroke-width="5" stroke-linecap="round" />
        <line x1="270" y1="270" x2="265" y2="345" stroke="#FFEAA7" stroke-width="5" stroke-linecap="round" />
      </g>"""
    },

    # 2. TAURUS (วัว)
    {
        "id": "taurus",
        "thaiName": "กลุ่มดาววัว",
        "zodiacName": "ราศีพฤษภ (Taurus)",
        "latinName": "Taurus",
        "symbol": "♉",
        "correctAnswer": "วัวจอมพลัง (หน้าตัว V มีเขาแหลม)",
        "options": [
            {"text": "วัวจอมพลัง (หน้าตัว V มีเขาแหลม)", "icon": "🐂", "correct": True},
            {"text": "ว่าวปักเป้าหางยาว", "icon": "🪁", "correct": False},
            {"text": "ปลาฉลามว่ายน้ำ", "icon": "🦈", "correct": False},
            {"text": "รถจักรยานสองล้อ", "icon": "🚲", "correct": False}
        ],
        "hint": "มองหาหน้าวัวรูปตัว 'V' (กระจุกดาวไฮยาดีส) ที่มีดาวตาสีแดงอัลเดบารัน และมีเขายาว 2 ข้างพุ่งไปข้างหน้า!",
        "funFact": "ดาวตาสีแดง 'อัลเดบารัน' มีขนาดใหญ่กว่าดวงอาทิตย์ 44 เท่า และบนสันหลังวัวมีกระจุกดาวลูกไก่ 7 ดวง (Pleiades)!",
        "starGuide": "ดาวตาสีส้มแดง 'อัลเดบารัน' สว่างเด่นที่สุดในกระจุกดาวหน้าวัวรูปตัว V",
        "stars": [
            {"id": 1, "name": "อัลเดบารัน (Aldebaran - α Tau ตาแดง)", "bayer": "α Tau", "ra": ra_deg(4, 35, 55.2), "dec": dec_deg(16, 30, 33), "mag": 0.85, "spect": "K5 III (ดาวยักษ์แดงส้ม)", "color": "#FF4757", "bright": True},
            {"id": 2, "name": "เอลนาธ (Elnath - β Tau ปลายเขาเหนือ)", "bayer": "β Tau", "ra": ra_deg(5, 26, 17.5), "dec": dec_deg(28, 36, 27), "mag": 1.65, "spect": "B7 III (ดาวยักษ์ฟ้าขาว)", "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "เทียนกวาน (Tianguan - ζ Tau ปลายเขาใต้)", "bayer": "ζ Tau", "ra": ra_deg(5, 37, 38.7), "dec": dec_deg(21, 8, 33), "mag": 2.97, "spect": "B2 IV (ดาวย่อยยักษ์ฟ้า)", "color": "#00F0FF", "bright": True},
            {"id": 4, "name": "ไอน์ (Ain - ε Tau ตาซ้าย)", "bayer": "ε Tau", "ra": ra_deg(4, 28, 37.0), "dec": dec_deg(19, 10, 50), "mag": 3.53, "spect": "G9.5 III (ดาวยักษ์ส้มเหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 5, "name": "พรีมา ไฮยาดูม (γ Tau ยอดจมูก V)", "bayer": "γ Tau", "ra": ra_deg(4, 19, 47.6), "dec": dec_deg(15, 37, 40), "mag": 3.65, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 6, "name": "เซกุนดา ไฮยาดูม (δ1 Tau ขอบหน้า)", "bayer": "δ1 Tau", "ra": ra_deg(4, 22, 56.0), "dec": dec_deg(17, 32, 33), "mag": 3.76, "spect": "G9.5 III (ดาวยักษ์ส้มเหลือง)", "color": "#FFA502", "bright": False},
            {"id": 7, "name": "ทีตา ทอไร (θ2 Tau คางวัว)", "bayer": "θ2 Tau", "ra": ra_deg(4, 28, 39.7), "dec": dec_deg(15, 52, 15), "mag": 3.40, "spect": "A7 III (ดาวยักษ์ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 8, "name": "แลมบ์ดา ทอไร (λ Tau อกวัว)", "bayer": "λ Tau", "ra": ra_deg(4, 0, 40.8), "dec": dec_deg(12, 29, 25), "mag": 3.41, "spect": "B3 V (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False},
            {"id": 9, "name": "ซี ทอไร (ξ Tau ขาหน้า)", "bayer": "ξ Tau", "ra": ra_deg(3, 27, 10.1), "dec": dec_deg(9, 43, 58), "mag": 3.73, "spect": "B9 V (ดาวขาวฟ้า)", "color": "#FFFFFF", "bright": False},
            {"id": 10, "name": "อัลไซโอนี (Alcyone - กระจุกดาวลูกไก่ M45)", "bayer": "η Tau", "ra": ra_deg(3, 47, 29.1), "dec": dec_deg(24, 6, 18), "mag": 2.87, "spect": "B7 IIIe (กระจุกดาวลูกไก่)", "color": "#00F0FF", "bright": True}
        ],
        "lines": [
            [5, 6], [6, 4], [4, 2],
            [5, 7], [7, 1], [1, 3],
            [4, 1],
            [5, 8], [8, 9]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- North Horn extending to Star 2 Elnath -->
        <path d="M 262 200 L 83 77" stroke="#FFD700" stroke-width="7" stroke-linecap="round" filter="drop-shadow(0 0 8px #FFD700)" />
        <!-- South Horn extending to Star 3 Tianguan -->
        <path d="M 239 235 L 48 174" stroke="#FFD700" stroke-width="7" stroke-linecap="round" filter="drop-shadow(0 0 8px #FFD700)" />
        <!-- Bull V-Head Snout -->
        <polygon points="262,200 239,235 289,246 279,221" fill="#FF4757" opacity="0.35" stroke="#FF6B81" stroke-width="2" />
        <!-- Glowing Red Eye at Aldebaran (Star 1) -->
        <circle cx="239" cy="235" r="14" fill="#FF4757" opacity="0.4" filter="drop-shadow(0 0 12px #FF4757)" />
        <!-- Pleiades Cluster Halo at Star 10 -->
        <circle cx="389" cy="136" r="22" fill="#00F0FF" opacity="0.2" filter="drop-shadow(0 0 12px #00F0FF)" />
        <!-- Bull Forequarters Silhouette -->
        <path d="M 289 246 Q 350 280 452 323 L 348 287 Z" fill="#FF6B81" opacity="0.25" />
      </g>"""
    },

    # 3. GEMINI (คนคู่ - 17 ดาว ครบสมบูรณ์ 2 คน 4 แขน 4 ขา)
    {
        "id": "gemini",
        "thaiName": "กลุ่มดาวคนคู่ (ฝาแฝด)",
        "zodiacName": "ราศีเมถุน (Gemini)",
        "latinName": "Gemini",
        "symbol": "♊",
        "correctAnswer": "ฝาแฝดยืนเคียงข้างกัน",
        "options": [
            {"text": "ฝาแฝดยืนเคียงข้างกัน", "icon": "👯‍♂️", "correct": True},
            {"text": "บันไดลิงปีนต้นไม้", "icon": "🪜", "correct": False},
            {"text": "สะพานแขวนข้ามแม่น้ำ", "icon": "🌉", "correct": False},
            {"text": "เรือใบสองเสา", "icon": "⛵", "correct": False}
        ],
        "hint": "มีดาวสว่าง 2 ดวงคู่กันด้านบนเป็นศีรษะ (คาสเตอร์และพอลลักซ์) และมีเส้นโครงร่างคน 2 คนยืนกอดคอเคียงข้างกันครบทั้งแขนและขา!",
        "funFact": "คาสเตอร์และพอลลักซ์เป็นพี่น้องฝาแฝดในเทพนิยายกรีก หนึ่งคนเก่งการต่อสู้ อีกคนเป็นอมตะ คอยปกป้องชาวเรือ!",
        "starGuide": "มองหาดาวฤกษ์สว่างคู่กันบนฟ้า พอลลักซ์สีส้มและคาสเตอร์สีขาว สองพี่น้องยืนกอดคอเคียงข้างกัน",
        "stars": [
            {"id": 1, "name": "คาสเตอร์ (Castor - α Gem หัวพี่)", "bayer": "α Gem", "ra": ra_deg(7, 34, 36.0), "dec": dec_deg(31, 53, 18), "mag": 1.58, "spect": "A1 V (ระบบดาวฤกษ์ 6 ดวง)", "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "พอลลักซ์ (Pollux - β Gem หัวน้อง)", "bayer": "β Gem", "ra": ra_deg(7, 45, 18.9), "dec": dec_deg(28, 1, 34), "mag": 1.14, "spect": "K0 III (ดาวยักษ์ส้ม มีดาวเคราะห์บริวาร)", "color": "#FFA502", "bright": True},
            {"id": 3, "name": "อัลฮีนา (Alhena - γ Gem เท้าพอลลักซ์ขวา)", "bayer": "γ Gem", "ra": ra_deg(6, 37, 42.7), "dec": dec_deg(16, 23, 57), "mag": 1.93, "spect": "A1.5 IV (ดาวย่อยยักษ์ขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "วาซัต (Wasat - δ Gem เอวพอลลักซ์)", "bayer": "δ Gem", "ra": ra_deg(7, 20, 7.4), "dec": dec_deg(21, 58, 56), "mag": 3.50, "spect": "F0 IV (ดาวย่อยยักษ์เหลืองขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "เมบซูดา (Mebsuta - ε Gem เอวคาสเตอร์)", "bayer": "ε Gem", "ra": ra_deg(6, 43, 55.9), "dec": dec_deg(25, 7, 52), "mag": 3.06, "spect": "G8 Ib (ดาวยักษ์ใหญ่เหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "เมกบูดา (Mekbuda - ζ Gem เข่าพอลลักซ์ขวา)", "bayer": "ζ Gem", "ra": ra_deg(7, 4, 6.5), "dec": dec_deg(20, 34, 13), "mag": 4.01, "spect": "F7-G3 Ib (ดาวแปรแสงเซเฟอิด)", "color": "#FFD27D", "bright": False},
            {"id": 7, "name": "โพรพัส (Propus - η Gem ปลายเท้าคาสเตอร์)", "bayer": "η Gem", "ra": ra_deg(6, 14, 52.7), "dec": dec_deg(22, 30, 24), "mag": 3.32, "spect": "M3 III (ดาวยักษ์แดง)", "color": "#FF7675", "bright": False},
            {"id": 8, "name": "เทจัต (Tejat - μ Gem เข่าคาสเตอร์ซ้าย)", "bayer": "μ Gem", "ra": ra_deg(6, 22, 57.6), "dec": dec_deg(22, 30, 49), "mag": 2.87, "spect": "M3 III (ดาวยักษ์แดง)", "color": "#FF7675", "bright": True},
            {"id": 9, "name": "นิว เจมินอร์ม (ν Gem ขาคาสเตอร์ขวา)", "bayer": "ν Gem", "ra": ra_deg(6, 28, 57.8), "dec": dec_deg(20, 12, 44), "mag": 4.13, "spect": "B6 III (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False},
            {"id": 10, "name": "อัลซีร์ (Alzirr - ξ Gem ปลายเท้าพอลลักซ์ซ้าย)", "bayer": "ξ Gem", "ra": ra_deg(6, 45, 17.4), "dec": dec_deg(12, 53, 44), "mag": 3.35, "spect": "F5 IV (ดาวเหลืองขาว)", "color": "#FFD27D", "bright": False},
            {"id": 11, "name": "แลมบ์ดา เจมินอร์ม (λ Gem เข่าพอลลักซ์ซ้าย)", "bayer": "λ Gem", "ra": ra_deg(7, 18, 5.6), "dec": dec_deg(16, 32, 25), "mag": 3.58, "spect": "A3 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 12, "name": "แคปปา เจมินอร์ม (κ Gem ไหล่พอลลักซ์)", "bayer": "κ Gem", "ra": ra_deg(7, 44, 26.9), "dec": dec_deg(24, 23, 53), "mag": 3.57, "spect": "G8 III (ดาวยักษ์ส้มเหลือง)", "color": "#FFA502", "bright": False},
            {"id": 13, "name": "อิปซิลอน เจมินอร์ม (υ Gem แขนพอลลักซ์ขวา)", "bayer": "υ Gem", "ra": ra_deg(7, 35, 55.4), "dec": dec_deg(26, 53, 45), "mag": 4.06, "spect": "M0 III (ดาวยักษ์แดง)", "color": "#FF7675", "bright": False},
            {"id": 14, "name": "ไอโอตา เจมินอร์ม (ι Gem ไหล่คาสเตอร์)", "bayer": "ι Gem", "ra": ra_deg(7, 25, 43.6), "dec": dec_deg(27, 47, 53), "mag": 3.78, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 15, "name": "ทีตา เจมินอร์ม (θ Gem ไหล่บนคาสเตอร์)", "bayer": "θ Gem", "ra": ra_deg(6, 52, 47.3), "dec": dec_deg(33, 57, 41), "mag": 3.60, "spect": "A3 III (ดาวยักษ์ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 16, "name": "เทา เจมินอร์ม (τ Gem แขนคาสเตอร์ซ้าย)", "bayer": "τ Gem", "ra": ra_deg(7, 11, 8.4), "dec": dec_deg(30, 14, 43), "mag": 4.41, "spect": "K2 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 17, "name": "1 เจมินอร์ม (1 Gem ปลายเท้าคาสเตอร์ 2)", "bayer": "1 Gem", "ra": ra_deg(6, 4, 0.0), "dec": dec_deg(23, 15, 47), "mag": 4.15, "spect": "G5 III (ดาวยักษ์เหลือง)", "color": "#FFD27D", "bright": False}
        ],
        "lines": [
            # Castor Twin Body & Limbs
            [1, 15], [15, 16],               # Castor Left Arm: Castor -> Theta -> Tau
            [1, 14], [14, 5],                 # Castor Torso: Castor -> Iota -> Mebsuta
            [5, 8], [8, 7], [7, 17],          # Castor Left Leg: Mebsuta -> Tejat -> Propus -> 1 Gem
            [5, 9],                           # Castor Right Leg: Mebsuta -> Nu
            # Pollux Twin Body & Limbs
            [2, 12], [12, 13],                # Pollux Right Arm: Pollux -> Kappa -> Upsilon
            [12, 4],                          # Pollux Torso: Kappa -> Wasat
            [4, 6], [6, 3],                   # Pollux Right Leg: Wasat -> Mekbuda -> Alhena
            [4, 11], [11, 10],                # Pollux Left Leg: Wasat -> Lambda -> Alzirr
            # Friendly Link between Twins (Holding hands / chest links)
            [14, 12], [5, 4], [9, 6]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Castor Head (Star 1) -->
        <circle cx="116" cy="76" r="24" fill="#70A1FF" opacity="0.4" stroke="#1E90FF" stroke-width="2" />
        <!-- Castor Arm & Body Silhouette -->
        <path d="M 116 76 L 256 45 L 195 100" stroke="#70A1FF" stroke-width="5" stroke-linecap="round" opacity="0.3" />
        <path d="M 116 76 L 145 136 L 286 175 L 357 213 L 384 214 L 420 202" stroke="#70A1FF" stroke-width="7" stroke-linecap="round" opacity="0.35" />
        <path d="M 286 175 L 336 247" stroke="#70A1FF" stroke-width="6" stroke-linecap="round" opacity="0.35" />
        
        <!-- Pollux Head (Star 2) -->
        <circle cx="80" cy="132" r="26" fill="#FFA502" opacity="0.4" stroke="#FF7F50" stroke-width="2" />
        <!-- Pollux Arm & Body Silhouette -->
        <path d="M 80 132 L 82 186 L 111 149" stroke="#FFA502" stroke-width="5" stroke-linecap="round" opacity="0.3" />
        <path d="M 80 132 L 82 186 L 164 221 L 218 242 L 307 303" stroke="#FFA502" stroke-width="7" stroke-linecap="round" opacity="0.35" />
        <path d="M 164 221 L 171 301 L 282 355" stroke="#FFA502" stroke-width="6" stroke-linecap="round" opacity="0.35" />
        
        <!-- Friendly Holding Hands Links -->
        <line x1="145" y1="136" x2="82" y2="186" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" filter="drop-shadow(0 0 6px #FFFFFF)" />
        <line x1="286" y1="175" x2="164" y2="221" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" />
        <line x1="336" y1="247" x2="218" y2="242" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.6" />
      </g>"""
    },

    # 4. CANCER (ปู)
    {
        "id": "cancer",
        "thaiName": "กลุ่มดาวปู",
        "zodiacName": "ราศีกรกฎ (Cancer)",
        "latinName": "Cancer",
        "symbol": "♋",
        "correctAnswer": "ปูน้อยก้ามโต",
        "options": [
            {"text": "ปูน้อยก้ามโต", "icon": "🦀", "correct": True},
            {"text": "ผีเสื้อแสนสวย", "icon": "🦋", "correct": False},
            {"text": "ร่มกันฝน", "icon": "☂️", "correct": False},
            {"text": "กบกระโดด", "icon": "🐸", "correct": False}
        ],
        "hint": "มีรูปตัว 'Y' กลับหัว โดยตรงกลางตัวมี 'กระจุกดาวรังผึ้ง' ระยิบระยับ และมีก้ามปูแยกออก!",
        "funFact": "ใจกลางกระดองปูมีกระจุกดาวเปิดชื่อว่า 'รังผึ้ง' (Praesepe / M44) ประกอบด้วยดาวฤกษ์กว่า 1,000 ดวง!",
        "starGuide": "กลุ่มดาวรูปตัว Y คว่ำ อยู่ตรงกลางระหว่างกลุ่มดาวคนคู่และกลุ่มดาวสิงโต",
        "stars": [
            {"id": 1, "name": "อัลตาร์ฟ (Altarf - β Cnc ปลายก้ามใต้)", "bayer": "β Cnc", "ra": ra_deg(8, 16, 30.9), "dec": dec_deg(9, 11, 8), "mag": 3.53, "spect": "K4 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": True},
            {"id": 2, "name": "อาคูเบนส์ (Acubens - α Cnc ก้ามตะวันออก)", "bayer": "α Cnc", "ra": ra_deg(8, 58, 29.2), "dec": dec_deg(11, 51, 28), "mag": 4.26, "spect": "A5 m (ดาวระบบ 4 ดวง)", "color": "#FFFFFF", "bright": False},
            {"id": 3, "name": "อาเซลลัส ออสตราลิส (δ Cnc กลางกระดองใต้)", "bayer": "δ Cnc", "ra": ra_deg(8, 44, 41.1), "dec": dec_deg(18, 9, 15), "mag": 3.94, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": True},
            {"id": 4, "name": "อาเซลลัส บอเรียลิส (γ Cnc กลางกระดองเหนือ)", "bayer": "γ Cnc", "ra": ra_deg(8, 43, 17.2), "dec": dec_deg(21, 28, 6), "mag": 4.66, "spect": "A1 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "ไอโอตา แคนครี (ι Cnc ก้ามเหนือ)", "bayer": "ι Cnc", "ra": ra_deg(8, 46, 41.8), "dec": dec_deg(28, 45, 36), "mag": 4.03, "spect": "G8 III (ดาวยักษ์เหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "กระจุกดาวรังผึ้ง (Beehive / M44 Praesepe)", "bayer": "M44", "ra": ra_deg(8, 40, 24.0), "dec": dec_deg(19, 40, 0), "mag": 3.10, "spect": "กระจุกดาวเปิด", "color": "#00F0FF", "bright": True}
        ],
        "lines": [
            [5, 4], [4, 3], [3, 2], [3, 1]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Crab Shell around Stars 4 & 3 and M44 -->
        <ellipse cx="266" cy="200" rx="55" ry="42" fill="#FF4757" opacity="0.35" stroke="#FF6B81" stroke-width="2" />
        <!-- Beehive Cluster Sparkle Glow -->
        <circle cx="270" cy="203" r="25" fill="#00F0FF" opacity="0.2" filter="drop-shadow(0 0 10px #00F0FF)" />
        <!-- Big Claws at Top to Star 5 -->
        <path d="M 267 172 Q 220 110 263 50 Q 290 110 267 172 Z" fill="#FF4757" opacity="0.6" stroke="#FF6B81" stroke-width="2" />
        <!-- Bottom Left & Right Legs to Star 2 (Acubens) & Star 1 (Altarf) -->
        <path d="M 265 230 Q 210 280 165 335" stroke="#FFA502" stroke-width="6" stroke-linecap="round" />
        <path d="M 265 230 Q 300 300 335 381" stroke="#FFA502" stroke-width="6" stroke-linecap="round" />
        <!-- Crab Eyes -->
        <circle cx="255" cy="165" r="5" fill="#FFFFFF" /><circle cx="255" cy="165" r="2.5" fill="#060919" />
        <circle cx="275" cy="165" r="5" fill="#FFFFFF" /><circle cx="275" cy="165" r="2.5" fill="#060919" />
      </g>"""
    },

    # 5. LEO (สิงโต)
    {
        "id": "leo",
        "thaiName": "กลุ่มดาวสิงโต",
        "zodiacName": "ราศีสิงห์ (Leo)",
        "latinName": "Leo",
        "symbol": "♌",
        "correctAnswer": "สิงโตเจ้าป่า (หัวรูปเคียวเกี่ยวข้าว)",
        "options": [
            {"text": "สิงโตเจ้าป่า (หัวรูปเคียวเกี่ยวข้าว)", "icon": "🦁", "correct": True},
            {"text": "กระรอกหางพวง", "icon": "🐿️", "correct": False},
            {"text": "ช้างตัวโต", "icon": "🐘", "correct": False},
            {"text": "เตารีดผ้าโบราณ", "icon": "🧼", "correct": False}
        ],
        "hint": "มีส่วนหัวเป็นรูปโค้งเคียวเกี่ยวข้าว (The Sickle) และมีลำตัวรูปสามเหลี่ยมทอดไปหาหางสิงโต!",
        "funFact": "ดาวที่สว่างที่สุดคือ 'เรกูลัส' (Regulus) หรือหัวใจสิงห์ หมุนรอบตัวเองเร็วมากจนตัวแบนคล้ายผลส้ม!",
        "starGuide": "มองหาเคียวเกี่ยวข้าวทางทิศตะวันตกและดาวหัวใจสิงห์สีฟ้าขาวสว่างจ้า",
        "stars": [
            {"id": 1, "name": "เรกูลัส (Regulus - α Leo หัวใจสิงห์)", "bayer": "α Leo", "ra": ra_deg(10, 8, 22.3), "dec": dec_deg(11, 58, 2), "mag": 1.36, "spect": "B7 V (ดาวสีฟ้าขาว สว่างที่สุดในกลุ่มดาว)", "color": "#00F0FF", "bright": True},
            {"id": 2, "name": "เดเนโบลา (Denebola - β Leo หางสิงโต)", "bayer": "β Leo", "ra": ra_deg(11, 49, 3.6), "dec": dec_deg(14, 34, 19), "mag": 2.14, "spect": "A3 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 3, "name": "แอลเจอบา (Algieba - γ Leo คอสิงโต)", "bayer": "γ Leo", "ra": ra_deg(10, 19, 58.3), "dec": dec_deg(19, 50, 30), "mag": 2.01, "spect": "K0 III (ดาวยักษ์ส้มคู่)", "color": "#FFA502", "bright": True},
            {"id": 4, "name": "โซสมา (Zosma - δ Leo สะโพกบน)", "bayer": "δ Leo", "ra": ra_deg(11, 14, 6.5), "dec": dec_deg(20, 31, 25), "mag": 2.56, "spect": "A4 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 5, "name": "อัลเกนูบี (Algenubi - ε Leo ยอดหัวสิงโต)", "bayer": "ε Leo", "ra": ra_deg(9, 45, 51.1), "dec": dec_deg(23, 46, 27), "mag": 2.97, "spect": "G1 II (ดาวยักษ์สว่างเหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "อัดฮาเฟรา (Adhafera - ζ Leo แผงคอ)", "bayer": "ζ Leo", "ra": ra_deg(10, 16, 41.4), "dec": dec_deg(23, 25, 2), "mag": 3.43, "spect": "F0 III (ดาวยักษ์ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "อัลจับฮาห์ (Al Jabhah - η Leo อกสิงโต)", "bayer": "η Leo", "ra": ra_deg(10, 7, 19.9), "dec": dec_deg(16, 45, 46), "mag": 3.48, "spect": "A0 Ib (ดาวยักษ์ใหญ่ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 8, "name": "เชอร์ทาน (Chertan - θ Leo สะโพกล่าง)", "bayer": "θ Leo", "ra": ra_deg(11, 14, 14.4), "dec": dec_deg(15, 25, 46), "mag": 3.33, "spect": "A2 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 9, "name": "ราซาลาส (Rasalas - μ Leo ปลายจมูกสิงห์)", "bayer": "μ Leo", "ra": ra_deg(9, 52, 45.8), "dec": dec_deg(26, 0, 25), "mag": 3.88, "spect": "K2 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [1, 7], [7, 3], [3, 6], [6, 9], [9, 5],
            [3, 4], [4, 2], [2, 8], [8, 1],
            [4, 8]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Lion Head & Mane around The Sickle (West / Right) -->
        <circle cx="420" cy="110" r="50" fill="#FFA502" opacity="0.35" stroke="#FF7F50" stroke-width="2" />
        <circle cx="450" cy="85" r="4.5" fill="#060919" />
        <circle cx="452" cy="83" r="1.5" fill="#FFFFFF" />
        <!-- Sickle Mane Outline -->
        <path d="M 407 282 Q 430 200 376 153 Q 410 90 449 50 Q 480 80 469 87" 
              fill="none" stroke="#FFD700" stroke-width="4" stroke-linecap="round" />
        <!-- Lion Body extending East (Left) to Denebola -->
        <path d="M 376 153 L 223 142 L 125 238 L 223 226 L 407 282 Z" fill="#FFA502" opacity="0.25" />
        <!-- Regulus Glowing Heart (Star 1) -->
        <circle cx="407" cy="282" r="15" fill="#00F0FF" opacity="0.35" filter="drop-shadow(0 0 10px #00F0FF)" />
        <!-- Denebola Tuft Tail (Star 2) -->
        <circle cx="125" cy="238" r="12" fill="#FF7F50" opacity="0.8" />
      </g>"""
    },

    # 6. VIRGO (หญิงสาว)
    {
        "id": "virgo",
        "thaiName": "กลุ่มดาวหญิงสาว (เทพีพรหมจารี)",
        "zodiacName": "ราศีกันย์ (Virgo)",
        "latinName": "Virgo",
        "symbol": "♍",
        "correctAnswer": "หญิงสาวถือรวงข้าวสาลี",
        "options": [
            {"text": "หญิงสาวถือรวงข้าวสาลี", "icon": "🌾", "correct": True},
            {"text": "ม้าน้ำในมหาสมุทร", "icon": "🫧", "correct": False},
            {"text": "กระต่ายหูยาว", "icon": "🐰", "correct": False},
            {"text": "ต้นสนวันคริสต์มาส", "icon": "🎄", "correct": False}
        ],
        "hint": "มีดาวฤกษ์สว่างสีฟ้าขาว 'สไปกา' อยู่ที่รวงข้าวสาลี และมีเส้นลำตัวหญิงสาวกางปีกกว้าง!",
        "funFact": "ดาว 'สไปกา' (Spica) เป็นระบบดาวคู่สีฟ้าขาว สว่างกว่าดวงอาทิตย์ถึง 12,000 เท่า!",
        "starGuide": "ลากเส้นโค้งต่อจากด้ามกระบวยกลุ่มดาวหมีใหญ่ ผ่านดาวอาร์คทูรัส แล้วจะพุ่งตรงมายังดาวสไปกา",
        "stars": [
            {"id": 1, "name": "สไปกา (Spica - α Vir รวงข้าวสาลี)", "bayer": "α Vir", "ra": ra_deg(13, 25, 11.6), "dec": dec_deg(-11, 9, 41), "mag": 0.98, "spect": "B1 III-IV (ดาวคู่ยักษ์ฟ้าขาว สว่างที่สุด)", "color": "#00F0FF", "bright": True},
            {"id": 2, "name": "ซาวิยาวา (Zavijava - β Vir ศีรษะ)", "bayer": "β Vir", "ra": ra_deg(11, 50, 41.7), "dec": dec_deg(1, 45, 53), "mag": 3.59, "spect": "F9 V (ดาวสีเหลืองนวล)", "color": "#FFD27D", "bright": False},
            {"id": 3, "name": "พอริมา (Porrima - γ Vir ไหล่/อก)", "bayer": "γ Vir", "ra": ra_deg(12, 41, 39.6), "dec": dec_deg(-1, 26, 58), "mag": 2.74, "spect": "F0 V (ดาวคู่ขาวบริสุทธิ์)", "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "มิเนเลาวา (Minelauva - δ Vir เอว)", "bayer": "δ Vir", "ra": ra_deg(12, 55, 36.2), "dec": dec_deg(3, 23, 51), "mag": 3.38, "spect": "M3 III (ดาวยักษ์แดง)", "color": "#FF4757", "bright": False},
            {"id": 5, "name": "วินเดเมียทริกซ์ (Vindemiatrix - ε Vir ปลายปีกขวา)", "bayer": "ε Vir", "ra": ra_deg(13, 2, 10.6), "dec": dec_deg(10, 57, 33), "mag": 2.85, "spect": "G8 III (ดาวยักษ์เหลืองทอง)", "color": "#FFD27D", "bright": True},
            {"id": 6, "name": "เฮเซ (Heze - ζ Vir สะโพก)", "bayer": "ζ Vir", "ra": ra_deg(13, 34, 41.6), "dec": dec_deg(-0, 35, 45), "mag": 3.38, "spect": "A3 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "ซาเนียห์ (Zaniah - η Vir แขนซ้าย)", "bayer": "η Vir", "ra": ra_deg(12, 19, 54.4), "dec": dec_deg(-0, 40, 0), "mag": 3.89, "spect": "A2 IV (ดาวขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 8, "name": "เซียร์มา (Syrma - ι Vir ชายกระโปรง/เท้า)", "bayer": "ι Vir", "ra": ra_deg(14, 16, 0.9), "dec": dec_deg(-6, 0, 2), "mag": 4.07, "spect": "F7 III (ดาวยักษ์เหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 9, "name": "คัง (Kang - κ Vir ปลายเท้า)", "bayer": "κ Vir", "ra": ra_deg(14, 12, 53.7), "dec": dec_deg(-10, 16, 26), "mag": 4.18, "spect": "K2.5 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [2, 7], [7, 3],
            [3, 4], [4, 5],
            [4, 6], [6, 1],
            [3, 1],
            [1, 8], [8, 9]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Maiden Head at Star 2 Zavijava -->
        <circle cx="444" cy="153" r="22" fill="#FDA7DF" opacity="0.4" stroke="#D980FA" stroke-width="2" />
        <!-- Wing extending to Star 5 Vindemiatrix -->
        <path d="M 339 211 Q 310 100 296 50 Q 350 120 339 211" fill="#70A1FF" opacity="0.35" stroke="#1E90FF" stroke-width="2" />
        <!-- Flowing Gown Silhouette -->
        <polygon points="339,211 310,122 229,193 247,396 142,298 150,381" fill="#9980FA" opacity="0.25" stroke="#833471" stroke-width="2" />
        <!-- Glowing Wheat Sheaf at Spica (Star 1) -->
        <ellipse cx="247" cy="396" rx="20" ry="14" fill="#F1C40F" opacity="0.7" stroke="#FFD700" stroke-width="2" filter="drop-shadow(0 0 12px #FFD700)" />
      </g>"""
    },

    # 7. LIBRA (คันชั่ง)
    {
        "id": "libra",
        "thaiName": "กลุ่มดาวคันชั่ง",
        "zodiacName": "ราศีตุล (Libra)",
        "latinName": "Libra",
        "symbol": "♎",
        "correctAnswer": "ตาชั่งวัดความสมดุล",
        "options": [
            {"text": "ตาชั่งวัดความสมดุล", "icon": "⚖️", "correct": True},
            {"text": "ว่าวสามเหลี่ยม", "icon": "🪁", "correct": False},
            {"text": "เต็นท์ตั้งแคมป์", "icon": "⛺", "correct": False},
            {"text": "เพชรประกายแสง", "icon": "💎", "correct": False}
        ],
        "hint": "มีรูปทรงสี่เหลี่ยมข้าวหลามตัด มีคานบนและจานตาชั่งสองข้างถ่วงสมดุลกัน!",
        "funFact": "เป็นราศีเดียวใน 12 จักราศีที่เป็นสิ่งของเครื่องใช้ ดาวซูเบนเอลเชมาลีมีประกายสีเขียวมรกตที่หาได้ยากบนฟ้า!",
        "starGuide": "ดาวจานเหนือคือ ซูเบนเอลเชมาลี (Zubeneschamali) สีเขียวมรกตแปลกตา",
        "stars": [
            {"id": 1, "name": "ซูเบนเอลเกนูบี (Zubenelgenubi - α2 Lib จานใต้)", "bayer": "α2 Lib", "ra": ra_deg(14, 50, 52.7), "dec": dec_deg(-16, 2, 30), "mag": 2.75, "spect": "A3 IV (ดาวคู่ขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "ซูเบนเอลเชมาลี (Zubeneschamali - β Lib จานเหนือ)", "bayer": "β Lib", "ra": ra_deg(15, 17, 0.5), "dec": dec_deg(-9, 22, 58), "mag": 2.61, "spect": "B8 V (ดาวสีฟ้าอมเขียวมรกต)", "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "ซูเบนเอลอัครับ (Zubenelakrab - γ Lib ขอบจานตะวันออก)", "bayer": "γ Lib", "ra": ra_deg(15, 35, 31.5), "dec": dec_deg(-14, 47, 22), "mag": 3.91, "spect": "G8.5 III (ดาวยักษ์ส้มเหลือง)", "color": "#FFA502", "bright": False},
            {"id": 4, "name": "บราเคียม (Brachium - σ Lib ฐานล่าง)", "bayer": "σ Lib", "ra": ra_deg(15, 4, 4.3), "dec": dec_deg(-25, 16, 55), "mag": 3.25, "spect": "M2.5 III (ดาวยักษ์แดง)", "color": "#FF4757", "bright": True},
            {"id": 5, "name": "อิปซิลอน ไลบรี (υ Lib สายถ่วง)", "bayer": "υ Lib", "ra": ra_deg(15, 37, 1.5), "dec": dec_deg(-28, 8, 7), "mag": 3.60, "spect": "K3.5 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 6, "name": "เทา ไลบรี (τ Lib)", "bayer": "τ Lib", "ra": ra_deg(15, 38, 39.4), "dec": dec_deg(-29, 46, 40), "mag": 3.66, "spect": "B2.5 V (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False}
        ],
        "lines": [
            [2, 1], [2, 3], [3, 4], [4, 1],
            [3, 5], [4, 6]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Scale Top Balance Beam between Stars 2 & 1 -->
        <line x1="281" y1="50" x2="416" y2="185" stroke="#FFD700" stroke-width="7" stroke-linecap="round" filter="drop-shadow(0 0 8px #FFD700)" />
        <!-- Center Fulcrum -->
        <circle cx="281" cy="50" r="12" fill="#FFA502" stroke="#FFD700" stroke-width="3" />
        <!-- Diamond Body Fill -->
        <polygon points="281,50 188,160 349,369 416,185" fill="#FFA502" opacity="0.25" stroke="#FFD700" stroke-width="2" />
        <!-- Weighing Pans hanging down -->
        <path d="M 168 180 Q 188 220 208 180 Z" fill="#FFA502" opacity="0.6" stroke="#FFD700" stroke-width="2" />
        <path d="M 396 205 Q 416 245 436 205 Z" fill="#FFA502" opacity="0.6" stroke="#FFD700" stroke-width="2" />
      </g>"""
    },

    # 8. SCORPIUS (แมงป่อง)
    {
        "id": "scorpio",
        "thaiName": "กลุ่มดาวแมงป่อง",
        "zodiacName": "ราศีพิจิก (Scorpius)",
        "latinName": "Scorpius",
        "symbol": "♏",
        "correctAnswer": "แมงป่องหางงอแหลมคม",
        "options": [
            {"text": "แมงป่องหางงอแหลมคม", "icon": "🦂", "correct": True},
            {"text": "เบ็ดตกปลาโบราณ", "icon": "🎣", "correct": False},
            {"text": "ไดโนเสาร์คอยาว", "icon": "🦕", "correct": False},
            {"text": "มังกรพ่นไฟ", "icon": "🐉", "correct": False}
        ],
        "hint": "มีก้าม 3 แฉกด้านหน้า มีหัวใจสีแดงแอนทาเรส และมีหางโค้งยาวรูปตัว J งอตวัดขึ้นพร้อมเหล็กใน!",
        "funFact": "ใจกลางลำตัวมีดาว 'แอนทาเรส' ดาวยักษ์แดงมหึมาขนาดใหญ่กว่าดวงอาทิตย์กว่า 700 เท่า!",
        "starGuide": "กลุ่มดาวรูปตัว J ชัดเจนที่สุดบนท้องฟ้าฤดูฝน มองหาดาวสีแดงแอนทาเรส",
        "stars": [
            {"id": 1, "name": "แอนทาเรส (Antares - α Sco หัวใจสีแดง)", "bayer": "α Sco", "ra": ra_deg(16, 29, 24.4), "dec": dec_deg(-26, 25, 55), "mag": 1.06, "spect": "M1.5 Iab (ดาวยักษ์ใหญ่แดง สว่างสุด)", "color": "#FF4757", "bright": True},
            {"id": 2, "name": "ชอลา (Shaula - λ Sco ปลายเหล็กใน)", "bayer": "λ Sco", "ra": ra_deg(17, 33, 36.5), "dec": dec_deg(-37, 6, 14), "mag": 1.62, "spect": "B2 IV (ดาวย่อยยักษ์ฟ้าขาว)", "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "ซาร์กัส (Sargas - θ Sco โค้งหางล่าง)", "bayer": "θ Sco", "ra": ra_deg(17, 37, 19.1), "dec": dec_deg(-42, 59, 52), "mag": 1.86, "spect": "F0 II (ดาวยักษ์สว่างเหลืองขาว)", "color": "#FFD27D", "bright": True},
            {"id": 4, "name": "ดชูบา (Dschubba - δ Sco หน้าผากแมงป่อง)", "bayer": "δ Sco", "ra": ra_deg(16, 0, 20.0), "dec": dec_deg(-22, 37, 18), "mag": 2.29, "spect": "B0.3 IV (ดาวย่อยยักษ์ฟ้า)", "color": "#00F0FF", "bright": True},
            {"id": 5, "name": "ลาราวาก (Larawag - ε Sco โคนหาง)", "bayer": "ε Sco", "ra": ra_deg(16, 50, 10.2), "dec": dec_deg(-34, 17, 36), "mag": 2.29, "spect": "K2.5 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": True},
            {"id": 6, "name": "เกอร์แทบ (Girtab - κ Sco หางตวัด)", "bayer": "κ Sco", "ra": ra_deg(17, 42, 29.3), "dec": dec_deg(-39, 1, 48), "mag": 2.39, "spect": "B1.5 III (ดาวยักษ์ฟ้าขาว)", "color": "#00F0FF", "bright": True},
            {"id": 7, "name": "กราฟเฟียส (Acrab - β Sco ก้ามบน)", "bayer": "β Sco", "ra": ra_deg(16, 5, 26.2), "dec": dec_deg(-19, 48, 19), "mag": 2.56, "spect": "B1 V (ดาวคู่ฟ้าขาว)", "color": "#00F0FF", "bright": True},
            {"id": 8, "name": "เลซัท (Lesath - υ Sco ปลายเหล็กในคู่)", "bayer": "υ Sco", "ra": ra_deg(17, 30, 45.8), "dec": dec_deg(-37, 17, 45), "mag": 2.70, "spect": "B2 IV (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": True},
            {"id": 9, "name": "ฟาง (Fang - π Sco ก้ามล่าง)", "bayer": "π Sco", "ra": ra_deg(15, 58, 51.1), "dec": dec_deg(-26, 6, 51), "mag": 2.89, "spect": "B1 V (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False},
            {"id": 10, "name": "อัลนิยัต (Alniyat - σ Sco อกแมงป่อง)", "bayer": "σ Sco", "ra": ra_deg(16, 21, 11.3), "dec": dec_deg(-25, 35, 34), "mag": 2.90, "spect": "B1 III (ดาวยักษ์ฟ้า)", "color": "#00F0FF", "bright": False},
            {"id": 11, "name": "ไพเคาฮาเล (Tau Sco อกล่าง)", "bayer": "τ Sco", "ra": ra_deg(16, 35, 53.0), "dec": dec_deg(-28, 12, 58), "mag": 2.82, "spect": "B0.2 V (ดาวแคระน้ำเงินร้อนจัด)", "color": "#00F0FF", "bright": False},
            {"id": 12, "name": "มิว สกอร์ปี (μ1 Sco ท้อง)", "bayer": "μ1 Sco", "ra": ra_deg(16, 51, 52.2), "dec": dec_deg(-38, 2, 50), "mag": 3.00, "spect": "B1.5 V (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False},
            {"id": 13, "name": "เซตา สกอร์ปี (ζ2 Sco ก้นหาง)", "bayer": "ζ2 Sco", "ra": ra_deg(16, 54, 35.1), "dec": dec_deg(-42, 21, 41), "mag": 3.62, "spect": "K4 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 14, "name": "อีตา สกอร์ปี (η Sco)", "bayer": "η Sco", "ra": ra_deg(17, 12, 9.2), "dec": dec_deg(-43, 14, 21), "mag": 3.32, "spect": "F3 III-IV (ดาวย่อยยักษ์ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 15, "name": "ไอโอตา สกอร์ปี (ι1 Sco)", "bayer": "ι1 Sco", "ra": ra_deg(17, 47, 35.1), "dec": dec_deg(-40, 7, 37), "mag": 2.99, "spect": "F2 Ia (ดาวยักษ์ใหญ่เหลืองขาว)", "color": "#FFD27D", "bright": False}
        ],
        "lines": [
            [7, 4], [4, 9],
            [4, 10], [10, 1], [1, 11],
            [11, 5], [5, 12], [12, 13], [13, 14], [14, 3],
            [3, 15], [15, 6], [6, 2], [2, 8]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- 3 Claws at Top-Right from Dschubba -->
        <path d="M 425 128 L 413 76 M 425 128 L 429 191" stroke="#FF4757" stroke-width="4" stroke-linecap="round" />
        <!-- Scorpion Body around Antares (Star 1) -->
        <ellipse cx="357" cy="196" rx="26" ry="18" fill="#FF4757" opacity="0.4" stroke="#FF6B81" stroke-width="2" />
        <!-- J-Curve Tail to Stinger (Stars 2 Shaula & 8 Lesath) -->
        <path d="M 342 229 C 310 320, 310 470, 195 497 C 150 490, 160 410, 203 388" 
              fill="none" stroke="#FF4757" stroke-width="12" stroke-linecap="round" opacity="0.35" />
        <!-- Poison Stinger Tip Glow -->
        <circle cx="203" cy="388" r="14" fill="#00F0FF" opacity="0.5" filter="drop-shadow(0 0 10px #00F0FF)" />
      </g>"""
    },

    # 9. SAGITTARIUS (คนยิงธนู / กาน้ำชา)
    {
        "id": "sagittarius",
        "thaiName": "กลุ่มดาวคนยิงธนู",
        "zodiacName": "ราศีธนู (Sagittarius)",
        "latinName": "Sagittarius",
        "symbol": "♐",
        "correctAnswer": "คนยิงธนู / กาน้ำชาพ่นไอ",
        "options": [
            {"text": "คนยิงธนู / กาน้ำชาพ่นไอ", "icon": "🏹", "correct": True},
            {"text": "ปราสาทเจ้าหญิง", "icon": "🏰", "correct": False},
            {"text": "นกอินทรีสยายปีก", "icon": "🦅", "correct": False},
            {"text": "รถไฟเหาะตีลังกา", "icon": "🎢", "correct": False}
        ],
        "hint": "มีกลุ่มดาวรูป 'กาน้ำชา' (The Teapot) ชัดเจนมาก มีพวยกา ฝากา และหูจับ!",
        "funFact": "ใจกลางทางช้างเผือก (Milky Way Galaxy) อันเป็นที่ตั้งของหลุมดำยักษ์มวลมหาศาล อยู่ตรงกลุ่มดาวนี้พอดี!",
        "starGuide": "มองหากลุ่มดาวรูปกาน้ำชาข้างๆ หางแมงป่อง พวยกาชี้ไปทางทิศตะวันตก",
        "stars": [
            {"id": 1, "name": "เคาส์ ออสตราลิส (Kaus Australis - ε Sgr ฐานกาน้ำ)", "bayer": "ε Sgr", "ra": ra_deg(18, 24, 10.3), "dec": dec_deg(-34, 23, 5), "mag": 1.79, "spect": "B9.5 III (ดาวยักษ์ฟ้าขาว สว่างสุด)", "color": "#00F0FF", "bright": True},
            {"id": 2, "name": "นูนาคี (Nunki - σ Sgr หูกาบน)", "bayer": "σ Sgr", "ra": ra_deg(18, 55, 15.9), "dec": dec_deg(-26, 17, 48), "mag": 2.05, "spect": "B2.5 V (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "อัสเซลลา (Ascella - ζ Sgr หูกาล่าง)", "bayer": "ζ Sgr", "ra": ra_deg(19, 2, 36.7), "dec": dec_deg(-29, 52, 48), "mag": 2.60, "spect": "A2.5 Va (ดาวคู่ขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "เคาส์ มีเดีย (Kaus Media - δ Sgr กลางพวยกา)", "bayer": "δ Sgr", "ra": ra_deg(18, 20, 59.7), "dec": dec_deg(-29, 49, 41), "mag": 2.72, "spect": "K3 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": True},
            {"id": 5, "name": "เคาส์ โบเรียลิส (Kaus Borealis - λ Sgr ยอดฝากา)", "bayer": "λ Sgr", "ra": ra_deg(18, 27, 58.2), "dec": dec_deg(-25, 25, 18), "mag": 2.82, "spect": "K1 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": True},
            {"id": 6, "name": "อัลนาสล์ (Alnasl - γ2 Sgr ปลายพวยกา)", "bayer": "γ2 Sgr", "ra": ra_deg(18, 5, 48.5), "dec": dec_deg(-30, 25, 27), "mag": 2.98, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": True},
            {"id": 7, "name": "ฟาย ซากิตตารี (φ Sgr ฝากาหลัง)", "bayer": "φ Sgr", "ra": ra_deg(18, 45, 39.4), "dec": dec_deg(-27, 0, 11), "mag": 3.17, "spect": "B8.5 III (ดาวยักษ์ฟ้าขาว)", "color": "#00F0FF", "bright": False},
            {"id": 8, "name": "เทา ซากิตตารี (τ Sgr หูกลาง)", "bayer": "τ Sgr", "ra": ra_deg(19, 6, 56.4), "dec": dec_deg(-27, 40, 14), "mag": 3.32, "spect": "K1 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 9, "name": "อัลบัลดาห์ (Albaldah - π Sgr หัวคนยิงธนู)", "bayer": "π Sgr", "ra": ra_deg(19, 9, 45.8), "dec": dec_deg(-21, 1, 25), "mag": 2.88, "spect": "F2 II (ดาวยักษ์สว่างเหลืองขาว)", "color": "#FFD27D", "bright": True},
            {"id": 10, "name": "อีตา ซากิตตารี (η Sgr ปลายคันธนูล่าง)", "bayer": "η Sgr", "ra": ra_deg(18, 17, 37.7), "dec": dec_deg(-36, 45, 42), "mag": 3.10, "spect": "M3.5 III (ดาวยักษ์แดงแปรแสง)", "color": "#FF4757", "bright": False}
        ],
        "lines": [
            [6, 4], [4, 1], [1, 6],
            [4, 5], [5, 7],
            [4, 1], [1, 3], [3, 7], [7, 4],
            [7, 2], [2, 8], [8, 3],
            [1, 10], [5, 9]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Teapot Bowl Polygon -->
        <polygon points="396,258 376,177 328,206 282,258 387,340" fill="#9980FA" opacity="0.3" stroke="#D980FA" stroke-width="2" />
        <!-- Teapot Spout to Star 6 Alnasl -->
        <polygon points="396,258 438,269 387,340" fill="#70A1FF" opacity="0.35" stroke="#1E90FF" stroke-width="2" />
        <!-- Milky Way Steam Puffs coming out of the Spout (West / Right) -->
        <path d="M 438 269 Q 470 240 480 210 Q 450 180 490 140" fill="none" stroke="#00F0FF" stroke-width="6" stroke-linecap="round" opacity="0.5" filter="drop-shadow(0 0 8px #00F0FF)" />
        <!-- Teapot Handle -->
        <path d="M 328 206 Q 250 200 282 258" fill="none" stroke="#D980FA" stroke-width="5" stroke-linecap="round" />
      </g>"""
    },

    # 10. CAPRICORNUS (แพะทะเล)
    {
        "id": "capricorn",
        "thaiName": "กลุ่มดาวมกร (แพะทะเล)",
        "zodiacName": "ราศีมังกร (Capricornus)",
        "latinName": "Capricornus",
        "symbol": "♑",
        "correctAnswer": "แพะทะเล (ตัวเป็นแพะ หางเป็นปลา)",
        "options": [
            {"text": "แพะทะเล (ตัวเป็นแพะ หางเป็นปลา)", "icon": "🐐", "correct": True},
            {"text": "หมวกโจรสลัด", "icon": "🏴‍☠️", "correct": False},
            {"text": "ชิ้นพิซซ่าสามเหลี่ยม", "icon": "🍕", "correct": False},
            {"text": "กางเกงใน", "icon": "🩲", "correct": False}
        ],
        "hint": "มีรูปสามเหลี่ยมโค้งขนาดใหญ่ คล้ายรูปทรงเรือหรือแพะวิเศษที่มีหางปลาแหวกว่ายน้ำ!",
        "funFact": "ในตำนาน เทพแพะแพนโดดหนีสัตว์ประหลาดไทฟอนลงแม่น้ำไนล์ ร่างกายครึ่งล่างจึงกลายเป็นหางปลา!",
        "starGuide": "ดาวหัวแพะคู่คือ อัลเจดี และ ดาบิห์ ทางทิศตะวันตก",
        "stars": [
            {"id": 1, "name": "เดเนบ อัลเจดี (Deneb Algedi - δ Cap หางปลา)", "bayer": "δ Cap", "ra": ra_deg(21, 47, 2.4), "dec": dec_deg(-16, 7, 38), "mag": 2.85, "spect": "A7m III (ดาวยักษ์ขาว สว่างสุด)", "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "ดาบิห์ (Dabih - β Cap เขาแพะ)", "bayer": "β Cap", "ra": ra_deg(20, 21, 0.7), "dec": dec_deg(-14, 46, 53), "mag": 3.05, "spect": "F8 V (ดาวระบบหลายดวง)", "color": "#FFA502", "bright": True},
            {"id": 3, "name": "อัลเจดี (Algedi - α2 Cap เขาแพะบน)", "bayer": "α2 Cap", "ra": ra_deg(20, 18, 3.2), "dec": dec_deg(-12, 32, 41), "mag": 3.58, "spect": "G8.5 III (ดาวยักษ์เหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 4, "name": "นาชิรา (Nashira - γ Cap ครีบหาง)", "bayer": "γ Cap", "ra": ra_deg(21, 40, 5.3), "dec": dec_deg(-16, 39, 44), "mag": 3.69, "spect": "A7m III-IV (ดาวย่อยยักษ์ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "เซตา แคปริคอร์นิ (ζ Cap ท้องปลาล่าง)", "bayer": "ζ Cap", "ra": ra_deg(21, 26, 40.0), "dec": dec_deg(-22, 24, 41), "mag": 3.77, "spect": "G4 Ib (ดาวยักษ์ใหญ่เหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "ทีตา แคปริคอร์นิ (θ Cap สันหลังกลาง)", "bayer": "θ Cap", "ra": ra_deg(21, 5, 56.8), "dec": dec_deg(-17, 13, 58), "mag": 4.08, "spect": "A1 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "โอเมกา แคปริคอร์นิ (ω Cap ก้นสามเหลี่ยม)", "bayer": "ω Cap", "ra": ra_deg(20, 51, 49.3), "dec": dec_deg(-26, 55, 9), "mag": 4.12, "spect": "K4 III (ดาวยักษ์ส้มแดง)", "color": "#FFA502", "bright": False},
            {"id": 8, "name": "ไซ แคปริคอร์นิ (ψ Cap ท้องล่างหน้า)", "bayer": "ψ Cap", "ra": ra_deg(20, 46, 5.8), "dec": dec_deg(-25, 16, 14), "mag": 4.13, "spect": "F5 V (ดาวเหลืองขาว)", "color": "#FFD27D", "bright": False},
            {"id": 9, "name": "ไอโอตา แคปริคอร์นิ (ι Cap หลัง)", "bayer": "ι Cap", "ra": ra_deg(21, 22, 14.8), "dec": dec_deg(-16, 50, 4), "mag": 4.28, "spect": "G8 III (ดาวยักษ์เหลือง)", "color": "#FFD27D", "bright": False}
        ],
        "lines": [
            [3, 2], [2, 8], [8, 7], [7, 5], [5, 4], [4, 1],
            [2, 6], [6, 9], [9, 4]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Goat Head on West (Right) at Stars 3 & 2 -->
        <circle cx="435" cy="120" r="26" fill="#FFEAA7" opacity="0.4" stroke="#F1C40F" stroke-width="2" />
        <path d="M 439 102 Q 460 60 480 80" fill="none" stroke="#FFD700" stroke-width="6" stroke-linecap="round" />
        <!-- Sea-Goat Hull Triangle -->
        <polygon points="431,139 348,340 203,161" fill="#1DD1A1" opacity="0.25" stroke="#10AC84" stroke-width="2" />
        <!-- Fish Tail Fin at Deneb Algedi (Star 1) -->
        <path d="M 203 161 Q 150 120 170 130 Q 140 180 203 161 Z" fill="#1DD1A1" opacity="0.7" stroke="#10AC84" stroke-width="2" />
      </g>"""
    },

    # 11. AQUARIUS (คนแบกหม้อน้ำ)
    {
        "id": "aquarius",
        "thaiName": "กลุ่มดาวคนแบกหม้อน้ำ",
        "zodiacName": "ราศีกุมภ์ (Aquarius)",
        "latinName": "Aquarius",
        "symbol": "♒",
        "correctAnswer": "คนเทน้ำจากเหยือกวิเศษ",
        "options": [
            {"text": "คนเทน้ำจากเหยือกวิเศษ", "icon": "🏺", "correct": True},
            {"text": "จรวดพุ่งสู่ดวงจันทร์", "icon": "🚀", "correct": False},
            {"text": "พัดลมตั้งโต๊ะ", "icon": "🪭", "correct": False},
            {"text": "แมวเหมียวกำลังนอน", "icon": "🐱", "correct": False}
        ],
        "hint": "มีปากหม้อน้ำรูปตัว 'Y' บนบ่า และมีสายน้ำไหลคดเคี้ยวลงมาทางทิศใต้!",
        "funFact": "น้ำที่เทลงมาจากเหยือกคือสายน้ำแห่งชีวิตในตำนาน ไหลลงสู่ปากปลาในกลุ่มดาวปลาทางใต้ (Piscis Austrinus)!",
        "starGuide": "มองหาดาวฤกษ์สว่าง 'ซาดาลซูด' และ 'ซาดาลเมลิก' บนบ่าคนเทน้ำ",
        "stars": [
            {"id": 1, "name": "ซาดาลซูด (Sadalsuud - β Aqr ไหล่ซ้าย)", "bayer": "β Aqr", "ra": ra_deg(21, 31, 33.5), "dec": dec_deg(-5, 34, 16), "mag": 2.90, "spect": "G0 Ib (ดาวยักษ์ใหญ่เหลือง สว่างสุด)", "color": "#FFD27D", "bright": True},
            {"id": 2, "name": "ซาดาลเมลิก (Sadalmelik - α Aqr ไหล่ขวา)", "bayer": "α Aqr", "ra": ra_deg(22, 5, 47.0), "dec": dec_deg(-0, 19, 11), "mag": 2.95, "spect": "G2 Ib (ดาวยักษ์ใหญ่เหลือง)", "color": "#FFD27D", "bright": True},
            {"id": 3, "name": "สแคต (Skat - δ Aqr ขา/ปลายสายน้ำ)", "bayer": "δ Aqr", "ra": ra_deg(22, 54, 39.0), "dec": dec_deg(-15, 49, 15), "mag": 3.27, "spect": "A3 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "อัลบาลิ (Albali - ε Aqr มือซ้าย)", "bayer": "ε Aqr", "ra": ra_deg(20, 47, 40.5), "dec": dec_deg(-9, 29, 45), "mag": 3.78, "spect": "A1.5 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "ซาดาคเบีย (Sadachbia - γ Aqr ปากเหยือก Y)", "bayer": "γ Aqr", "ra": ra_deg(22, 21, 39.3), "dec": dec_deg(-1, 23, 14), "mag": 3.86, "spect": "A0 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 6, "name": "เซตา แอควารี (ζ Aqr กลางปากเหยือก)", "bayer": "ζ Aqr", "ra": ra_deg(22, 28, 49.9), "dec": dec_deg(-0, 1, 12), "mag": 3.65, "spect": "F2 IV (ดาวคู่ขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "อีตา แอควารี (η Aqr ปลายเหยือกบน)", "bayer": "η Aqr", "ra": ra_deg(22, 35, 21.3), "dec": dec_deg(0, 7, 2), "mag": 4.04, "spect": "B9 IV-Vn (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False},
            {"id": 8, "name": "อันชา (Ancha - θ Aqr สะโพก)", "bayer": "θ Aqr", "ra": ra_deg(22, 16, 50.0), "dec": dec_deg(-7, 46, 59), "mag": 4.17, "spect": "G8 III-IV (ดาวย่อยยักษ์เหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 9, "name": "แลมบ์ดา แอควารี (λ Aqr สายน้ำ)", "bayer": "λ Aqr", "ra": ra_deg(22, 52, 36.9), "dec": dec_deg(-7, 34, 47), "mag": 3.73, "spect": "M2.5 IIIa (ดาวยักษ์แดง)", "color": "#FF4757", "bright": False},
            {"id": 10, "name": "พาย แอควารี (π Aqr ยอดเหยือก)", "bayer": "π Aqr", "ra": ra_deg(22, 25, 16.6), "dec": dec_deg(1, 22, 39), "mag": 4.66, "spect": "B1 Ve (ดาวสีฟ้า)", "color": "#00F0FF", "bright": False},
            {"id": 11, "name": "88 แอควารี (c2 Aqr ปลายสายน้ำล่าง)", "bayer": "c2 Aqr", "ra": ra_deg(23, 9, 26.8), "dec": dec_deg(-21, 10, 21), "mag": 3.68, "spect": "K1 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [4, 1], [1, 2], [2, 8],
            [2, 5], [5, 6], [6, 7], [6, 10],
            [6, 9], [9, 3], [3, 11]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- Water-Bearer Head & Body -->
        <circle cx="340" cy="50" r="18" fill="#FFEAA7" opacity="0.4" stroke="#F1C40F" stroke-width="2" />
        <!-- Greek Water Urn at Stars 2 / 5 / 6 -->
        <ellipse cx="270" cy="45" rx="20" ry="26" fill="#E17055" opacity="0.5" stroke="#FF7675" stroke-width="2" />
        <!-- Cascading Water Streams flowing South towards Skat (Star 3) & 88 Aqr (Star 11) -->
        <path d="M 263 29 Q 214 148 210 278 Q 180 320 180 360" fill="none" stroke="#00F0FF" stroke-width="8" stroke-linecap="round" opacity="0.7" filter="drop-shadow(0 0 8px #00F0FF)" />
      </g>"""
    },

    # 12. PISCES (ปลาคู่)
    {
        "id": "pisces",
        "thaiName": "กลุ่มดาวปลาคู่",
        "zodiacName": "ราศีมีน (Pisces)",
        "latinName": "Pisces",
        "symbol": "♓",
        "correctAnswer": "ปลา 2 ตัวผูกริบบิ้นที่หาง",
        "options": [
            {"text": "ปลา 2 ตัวผูกริบบิ้นที่หาง", "icon": "🐟", "correct": True},
            {"text": "แว่นตาขยาย", "icon": "🔍", "correct": False},
            {"text": "กรรไกรตัดกระดาษ", "icon": "✂️", "correct": False},
            {"text": "ผึ้งน้อยบินตอมดอกไม้", "icon": "🐝", "correct": False}
        ],
        "hint": "มีริบบิ้นรูปตัว 'V' เชื่อมปลาสองตัว ตัวหนึ่งอยู่ทางเหนือ และอีกตัวเป็นวงกลมอยู่ทางทิศตะวันตก!",
        "funFact": "ปลาสองตัวนี้คือ เทพีอโฟรไดต์กับบุตรชายคิวปิด แปลงร่างเป็นปลาแล้วผูกริบบิ้นไว้ด้วยกันเพื่อไม่ให้พลัดหลง!",
        "starGuide": "ดาวตรงปมริบบิ้นเชื่อมปลาทั้งสองคือ 'อัลริชา' (Alrescha)",
        "stars": [
            {"id": 1, "name": "อัลริชา (Alrescha - α Psc ปมผูกริบบิ้น)", "bayer": "α Psc", "ra": ra_deg(2, 2, 2.8), "dec": dec_deg(2, 45, 50), "mag": 3.82, "spect": "A0p (ดาวคู่ขาว ปมริบบิ้น)", "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "อัลเฟิร์ก (Alpherg - η Psc ปลาเหนือ)", "bayer": "η Psc", "ra": ra_deg(1, 31, 29.0), "dec": dec_deg(15, 20, 45), "mag": 3.62, "spect": "G7 IIIa (ดาวยักษ์เหลือง สว่างสุด)", "color": "#FFD27D", "bright": True},
            {"id": 3, "name": "แกมมา พิสเซียม (γ Psc วงปลาตะวันตก)", "bayer": "γ Psc", "ra": ra_deg(23, 17, 10.0), "dec": dec_deg(3, 16, 56), "mag": 3.70, "spect": "G8 III (ดาวยักษ์เหลืองส้ม)", "color": "#FFA502", "bright": True},
            {"id": 4, "name": "โอไมครอน พิสเซียม (ο Psc สายเหนือ 1)", "bayer": "ο Psc", "ra": ra_deg(1, 45, 23.6), "dec": dec_deg(9, 9, 28), "mag": 4.26, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 5, "name": "นิว พิสเซียม (ν Psc สายเหนือ 2)", "bayer": "ν Psc", "ra": ra_deg(1, 41, 25.9), "dec": dec_deg(5, 29, 15), "mag": 4.45, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 6, "name": "มิว พิสเซียม (μ Psc สายเหนือ 3)", "bayer": "μ Psc", "ra": ra_deg(1, 30, 11.0), "dec": dec_deg(6, 8, 38), "mag": 4.84, "spect": "K4 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 7, "name": "ไซ พิสเซียม (ξ Psc สายเหนือ 4)", "bayer": "ξ Psc", "ra": ra_deg(1, 53, 33.3), "dec": dec_deg(3, 11, 15), "mag": 4.61, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 8, "name": "เดลตา พิสเซียม (δ Psc สายตะวันตก 1)", "bayer": "δ Psc", "ra": ra_deg(0, 48, 40.9), "dec": dec_deg(7, 35, 6), "mag": 4.44, "spect": "K5 III (ดาวยักษ์ส้มแดง)", "color": "#FFA502", "bright": False},
            {"id": 9, "name": "เอปซิลอน พิสเซียม (ε Psc สายตะวันตก 2)", "bayer": "ε Psc", "ra": ra_deg(1, 2, 56.6), "dec": dec_deg(7, 53, 24), "mag": 4.27, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 10, "name": "เซตา พิสเซียม (ζ Psc สายตะวันตก 3)", "bayer": "ζ Psc", "ra": ra_deg(1, 13, 43.8), "dec": dec_deg(7, 34, 32), "mag": 5.21, "spect": "A7 IV (ดาวขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 11, "name": "ทีตา พิสเซียม (θ Psc วงปลา)", "bayer": "θ Psc", "ra": ra_deg(23, 27, 58.2), "dec": dec_deg(6, 22, 44), "mag": 4.27, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 12, "name": "ไอโอตา พิสเซียม (ι Psc วงปลา)", "bayer": "ι Psc", "ra": ra_deg(23, 39, 57.0), "dec": dec_deg(5, 37, 35), "mag": 4.13, "spect": "F7 V (ดาวเหลืองขาว)", "color": "#FFD27D", "bright": False},
            {"id": 13, "name": "แลมบ์ดา พิสเซียม (λ Psc วงปลา)", "bayer": "λ Psc", "ra": ra_deg(23, 42, 2.8), "dec": dec_deg(1, 46, 46), "mag": 4.49, "spect": "A7 V (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 14, "name": "แคปปา พิสเซียม (κ Psc วงปลา)", "bayer": "κ Psc", "ra": ra_deg(23, 26, 55.9), "dec": dec_deg(1, 15, 20), "mag": 4.95, "spect": "A0p (ดาวแคระขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 15, "name": "7 พิสเซียม (7 Psc วงปลา)", "bayer": "7 Psc", "ra": ra_deg(23, 11, 2.0), "dec": dec_deg(5, 5, 23), "mag": 5.05, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [1, 7], [7, 5], [5, 6], [6, 4], [4, 2],
            [1, 10], [10, 9], [9, 8], [8, 12],
            [12, 11], [11, 15], [15, 3], [3, 14], [14, 13], [13, 12]
        ],
        "artOverlay": """
      <g class="overlay-graphic" opacity="0.9">
        <!-- North Fish at Star 2 Alpherg -->
        <ellipse cx="198" cy="137" rx="30" ry="16" transform="rotate(-25 198 137)" fill="#55EFC4" opacity="0.6" stroke="#1DD1A1" stroke-width="2" />
        <polygon points="220,150 240,165 235,140" fill="#55EFC4" opacity="0.7" />
        <!-- West Fish at Circlet of Pisces (Stars 12, 11, 15, 3, 14, 13) -->
        <ellipse cx="390" cy="330" rx="36" ry="22" fill="#FF6B81" opacity="0.6" stroke="#FF4757" stroke-width="2" />
        <!-- Ribbon Knot at Star 1 Alrescha -->
        <circle cx="114" cy="342" r="14" fill="#FFD700" stroke="#FF7675" stroke-width="3" filter="drop-shadow(0 0 10px #FFD700)" />
      </g>"""
    }
]

def generate_js():
    width = 500
    height = 400
    padding = 45
    
    js_entries = []
    
    for c in DATA:
        stars = c["stars"]
        ras = [s["ra"] for s in stars]
        decs = [s["dec"] for s in stars]
        
        # Pisces wrap-around handling
        min_ra, max_ra = min(ras), max(ras)
        if max_ra - min_ra > 180.0:
            ras_unwrapped = [ra + 360.0 if ra < 180.0 else ra for ra in ras]
        else:
            ras_unwrapped = ras
            
        ra0 = sum(ras_unwrapped) / len(ras_unwrapped)
        dec0 = sum(decs) / len(decs)
        dec0_rad = math.radians(dec0)
        
        proj_points = []
        for i, s in enumerate(stars):
            dra = ras_unwrapped[i] - ra0
            ddec = decs[i] - dec0
            x_sky = -math.radians(dra) * math.cos(dec0_rad)
            y_sky = math.radians(ddec)
            proj_points.append((x_sky, y_sky, s))
            
        xs = [p[0] for p in proj_points]
        ys = [p[1] for p in proj_points]
        
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        span_x = max_x - min_x if max_x != min_x else 1.0
        span_y = max_y - min_y if max_y != min_y else 1.0
        
        avail_w = width - 2 * padding
        avail_h = height - 2 * padding
        scale = min(avail_w / span_x, avail_h / span_y)
        
        mid_proj_x = (min_x + max_x) / 2.0
        mid_proj_y = (min_y + max_y) / 2.0
        
        projected_stars = []
        for x_sky, y_sky, s in proj_points:
            svg_x = round((width / 2.0) + (x_sky - mid_proj_x) * scale)
            svg_y = round((height / 2.0) - (y_sky - mid_proj_y) * scale)
            
            mag = s["mag"]
            if mag < 1.2:
                r = 11
            elif mag < 2.2:
                r = 9
            elif mag < 3.2:
                r = 7.5
            elif mag < 4.0:
                r = 6.5
            else:
                r = 5.5
                
            projected_stars.append({
                "id": s["id"],
                "x": svg_x,
                "y": svg_y,
                "r": r,
                "name": s["name"],
                "bayer": s["bayer"],
                "mag": s["mag"],
                "spect": s["spect"],
                "bright": s["bright"],
                "color": s["color"]
            })
            
        # Format options as JSON
        options_js = json.dumps(c["options"], ensure_ascii=False, indent=6)
        
        # Format stars as JS objects
        stars_lines = []
        for ps in projected_stars:
            stars_lines.append(f'      {{ id: {ps["id"]}, x: {ps["x"]}, y: {ps["y"]}, r: {ps["r"]}, name: "{ps["name"]}", bayer: "{ps["bayer"]}", mag: {ps["mag"]}, spect: "{ps["spect"]}", bright: {"true" if ps["bright"] else "false"}, color: "{ps["color"]}" }}')
        stars_js = ",\n".join(stars_lines)
        
        # Format lines
        lines_js = ", ".join([f"[{p1}, {p2}]" for p1, p2 in c["lines"]])
        
        entry = f"""  {{
    id: "{c['id']}",
    thaiName: "{c['thaiName']}",
    zodiacName: "{c['zodiacName']}",
    latinName: "{c['latinName']}",
    symbol: "{c['symbol']}",
    correctAnswer: "{c['correctAnswer']}",
    options: {options_js.replace("\n      ", "\n    ")},
    hint: "{c['hint']}",
    funFact: "{c['funFact']}",
    starGuide: "{c['starGuide']}",
    viewBox: "0 0 {width} {height}",
    stars: [
{stars_js}
    ],
    lines: [
      {lines_js}
    ],
    artOverlay: `{c['artOverlay']}
    `
  }}"""
        js_entries.append(entry)

    full_js = f"""/**
 * ฐานข้อมูลกลุ่มดาว 12 จักราศี (12 Zodiac Constellations Dataset)
 * คำนวณตำแหน่งพิกัดดาว (x, y) จากพิกัดทรงกลมฟ้าจริง (J2000 Right Ascension & Declination) 100%
 * อ้างอิงตามฐานข้อมูลดาราศาสตร์สากล IAU / Hipparcos / Yale Bright Star Catalog
 * พร้อมเส้นโยงดาวตามมาตรฐาน IAU ครบทุกกิ่งก้านแขนขา และภาพร่างเวกเตอร์ (Art Overlay) ที่ตรงกับแนวเส้นดาวจริงทุกประการ
 */

const CONSTELLATIONS_DATA = [
{",\n".join(js_entries)}
];

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ CONSTELLATIONS_DATA }};
}}
"""
    with open("js/constellations.js", "w", encoding="utf-8") as f:
        f.write(full_js)
    print("Successfully wrote full js/constellations.js with complete constellation stars and stick figures.")

if __name__ == "__main__":
    generate_js()
