/**
 * ฐานข้อมูลกลุ่มดาว 12 จักราศี (12 Zodiac Constellations Dataset)
 * ปรับปรุงภาพร่างเวกเตอร์ (Art Overlay) ให้ชัดเจน สวยงาม และตรงตามรูปร่างกลุ่มดาว 100%
 */

const CONSTELLATIONS_DATA = [
  {
    "id": "aries",
    "thaiName": "กลุ่มดาวแกะ",
    "zodiacName": "ราศีเมษ (Aries)",
    "latinName": "Aries",
    "symbol": "♈",
    "correctAnswer": "แกะ",
    "options": [
      {
        "text": "แกะ",
        "icon": "🐏",
        "correct": true
      },
      {
        "text": "นก",
        "icon": "🕊️",
        "correct": false
      },
      {
        "text": "หนังสติ๊ก",
        "icon": "🌱",
        "correct": false
      },
      {
        "text": "คันธนูและลูกศร",
        "icon": "🏹",
        "correct": false
      }
    ],
    "hint": "มองหาดาวสว่าง 3 ดวงเรียงโค้งคล้ายเขาแกะ โดยมีดาวฮามัลสว่างสุดอยู่ตรงสันเขา!",
    "funFact": "ราศีแรกของจักรราศี ในตำนานกรีกคือ 'แกะขนทองคำ' (Chrysomallos) ที่บินข้ามมหาสมุทรเพื่อช่วยเหลือเจ้าชาย!",
    "starGuide": "ดาวสว่างสีส้ม 'ฮามัล' (Hamal) อยู่ตรงสันเขา และดาว 'เชอราทาน' กับ 'เมซาร์ทิม' อยู่ตรงปลายเขาแกะ",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 383,
        "y": 218,
        "r": 9,
        "name": "ฮามัล (Hamal - α Ari)",
        "bayer": "α Ari",
        "mag": 2,
        "spect": "K2 III (ดาวยักษ์ส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 2,
        "x": 449,
        "y": 279,
        "r": 7.5,
        "name": "เชอราทาน (Sheratan - β Ari)",
        "bayer": "β Ari",
        "mag": 2.64,
        "spect": "A5 V (ดาวแคระขาว)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 3,
        "x": 455,
        "y": 314,
        "r": 6.5,
        "name": "เมซาร์ทิม (Mesarthim - γ Ari)",
        "bayer": "γ Ari",
        "mag": 3.88,
        "spect": "A1 V (ดาวคู่ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 4,
        "x": 45,
        "y": 304,
        "r": 5.5,
        "name": "โบเทน (Botein - δ Ari)",
        "bayer": "δ Ari",
        "mag": 4.35,
        "spect": "K2 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 5,
        "x": 159,
        "y": 132,
        "r": 6.5,
        "name": "ภารณี (Bharani - 41 Ari)",
        "bayer": "41 Ari",
        "mag": 3.61,
        "spect": "B8 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 6,
        "x": 170,
        "y": 86,
        "r": 5.5,
        "name": "39 แอรีเอทิส (39 Ari)",
        "bayer": "39 Ari",
        "mag": 4.51,
        "spect": "K1 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      }
    ],
    "lines": [
      [
        4,
        1
      ],
      [
        1,
        2
      ],
      [
        2,
        3
      ],
      [
        1,
        5
      ],
      [
        5,
        6
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Ram Golden Horn (Detailed Double Swirl following Hamal -> Sheratan -> Mesarthim) -->\n        <path d=\"M 360 190 C 410 180, 465 210, 460 270 C 455 315, 410 330, 395 295 C 385 270, 410 240, 430 250\" \n              fill=\"none\" stroke=\"#FFD700\" stroke-width=\"10\" stroke-linecap=\"round\" filter=\"drop-shadow(0 0 12px #FFD700)\" />\n        <path d=\"M 360 190 C 405 185, 450 215, 448 265 C 445 298, 415 310, 405 288\" \n              fill=\"none\" stroke=\"#FFA502\" stroke-width=\"5\" stroke-linecap=\"round\" />\n        \n        <!-- Ram Head & Snout (at Hamal 383, 218) -->\n        <ellipse cx=\"360\" cy=\"225\" rx=\"36\" ry=\"30\" fill=\"#FFEAA7\" fill-opacity=\"0.6\" stroke=\"#F1C40F\" stroke-width=\"2.5\" />\n        <!-- Cute Muzzle & Nose -->\n        <path d=\"M 380 235 Q 395 245 385 255 Q 365 255 360 245 Z\" fill=\"#FFA502\" fill-opacity=\"0.8\" />\n        <!-- Big Eye -->\n        <circle cx=\"368\" cy=\"218\" r=\"5\" fill=\"#060919\" />\n        <circle cx=\"370\" cy=\"216\" r=\"2\" fill=\"#FFFFFF\" />\n        <!-- Cute Ear -->\n        <ellipse cx=\"330\" cy=\"215\" rx=\"14\" ry=\"7\" transform=\"rotate(-20 330 215)\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <ellipse cx=\"330\" cy=\"215\" rx=\"9\" ry=\"4\" transform=\"rotate(-20 330 215)\" fill=\"#FF7675\" fill-opacity=\"0.6\" />\n\n        <!-- Fluffy Wool Clouds Body (covering 41 Ari 159, 132 to Botein 45, 304) -->\n        <path d=\"M 330 230 Q 310 160 250 160 Q 200 120 150 140 Q 90 140 70 200 Q 40 240 50 290 Q 70 330 130 330 Q 180 340 230 320 Q 290 330 330 280 Z\" \n              fill=\"#70A1FF\" fill-opacity=\"0.3\" stroke=\"#00F0FF\" stroke-width=\"3\" filter=\"drop-shadow(0 0 10px rgba(0, 240, 255, 0.4))\" />\n        \n        <!-- Wool Texture Fluffs -->\n        <circle cx=\"160\" cy=\"180\" r=\"28\" fill=\"#70A1FF\" fill-opacity=\"0.35\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" stroke-dasharray=\"4,4\" />\n        <circle cx=\"230\" cy=\"200\" r=\"32\" fill=\"#70A1FF\" fill-opacity=\"0.35\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" stroke-dasharray=\"4,4\" />\n        <circle cx=\"120\" cy=\"240\" r=\"30\" fill=\"#70A1FF\" fill-opacity=\"0.35\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" stroke-dasharray=\"4,4\" />\n\n        <!-- 4 Legs with Golden Hooves -->\n        <path d=\"M 280 310 L 275 375 L 290 375 L 295 310\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <rect x=\"272\" y=\"365\" width=\"20\" height=\"12\" rx=\"3\" fill=\"#FFD700\" />\n        \n        <path d=\"M 220 320 L 215 375 L 230 375 L 235 320\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <rect x=\"212\" y=\"365\" width=\"20\" height=\"12\" rx=\"3\" fill=\"#FFD700\" />\n\n        <path d=\"M 130 325 L 120 375 L 135 375 L 145 325\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <rect x=\"117\" y=\"365\" width=\"20\" height=\"12\" rx=\"3\" fill=\"#FFD700\" />\n\n        <path d=\"M 80 310 L 70 370 L 85 370 L 95 310\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <rect x=\"67\" y=\"360\" width=\"20\" height=\"12\" rx=\"3\" fill=\"#FFD700\" />\n\n        <!-- Little Fluffy Tail -->\n        <ellipse cx=\"40\" cy=\"260\" rx=\"14\" ry=\"10\" transform=\"rotate(-30 40 260)\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n      </g>"
  },
  {
    "id": "taurus",
    "thaiName": "กลุ่มดาววัว",
    "zodiacName": "ราศีพฤษภ (Taurus)",
    "latinName": "Taurus",
    "symbol": "♉",
    "correctAnswer": "วัว",
    "options": [
      {
        "text": "วัว",
        "icon": "🐂",
        "correct": true
      },
      {
        "text": "ว่าวหางยาว",
        "icon": "🪁",
        "correct": false
      },
      {
        "text": "ปลาฉลามว่ายน้ำ",
        "icon": "🦈",
        "correct": false
      },
      {
        "text": "รถจักรยาน",
        "icon": "🚲",
        "correct": false
      }
    ],
    "hint": "มองหาหน้ารูปตัว V ที่มีดาวตาสีแดงอัลเดบารัน และมีเขายาว 2 ข้าง!",
    "funFact": "ดาวตาสีส้มแดง 'อัลเดบารัน' มีขนาดใหญ่กว่าดวงอาทิตย์ 44 เท่า และบนสันหลังวัวมีกระจุกดาวลูกไก่ 7 ดวง (Pleiades)!",
    "starGuide": "ดาวตาสีส้มแดง 'อัลเดบารัน' สว่างเด่นที่สุดในกระจุกดาวหน้าวัวรูปตัว V",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 239,
        "y": 235,
        "r": 11,
        "name": "อัลเดบารัน (Aldebaran - α Tau ตาแดง)",
        "bayer": "α Tau",
        "mag": 0.85,
        "spect": "K5 III (ดาวยักษ์แดงส้ม)",
        "bright": true,
        "color": "#FF4757"
      },
      {
        "id": 2,
        "x": 81,
        "y": 75,
        "r": 9,
        "name": "เอลนาธ (Elnath - β Tau ปลายเขาเหนือ)",
        "bayer": "β Tau",
        "mag": 1.65,
        "spect": "B7 III (ดาวยักษ์ฟ้าขาว)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 3,
        "x": 45,
        "y": 174,
        "r": 7.5,
        "name": "เทียนกวาน (Tianguan - ζ Tau ปลายเขาใต้)",
        "bayer": "ζ Tau",
        "mag": 2.97,
        "spect": "B2 IV (ดาวย่อยยักษ์ฟ้า)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 4,
        "x": 262,
        "y": 200,
        "r": 6.5,
        "name": "ไอน์ (Ain - ε Tau ตาซ้าย)",
        "bayer": "ε Tau",
        "mag": 3.53,
        "spect": "G9.5 III (ดาวยักษ์ส้มเหลือง)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 5,
        "x": 290,
        "y": 247,
        "r": 6.5,
        "name": "พรีมา ไฮยาดูม (γ Tau ยอดจมูก V)",
        "bayer": "γ Tau",
        "mag": 3.65,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 6,
        "x": 280,
        "y": 222,
        "r": 6.5,
        "name": "เซกุนดา ไฮยาดูม (δ1 Tau ขอบหน้า)",
        "bayer": "δ1 Tau",
        "mag": 3.76,
        "spect": "G9.5 III (ดาวยักษ์ส้มเหลือง)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 7,
        "x": 262,
        "y": 244,
        "r": 6.5,
        "name": "ทีตา ทอไร (θ2 Tau คางวัว)",
        "bayer": "θ2 Tau",
        "mag": 3.4,
        "spect": "A7 III (ดาวยักษ์ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 8,
        "x": 350,
        "y": 288,
        "r": 6.5,
        "name": "แลมบ์ดา ทอไร (λ Tau อกวัว)",
        "bayer": "λ Tau",
        "mag": 3.41,
        "spect": "B3 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 9,
        "x": 455,
        "y": 325,
        "r": 6.5,
        "name": "ซี ทอไร (ξ Tau ขาหน้า)",
        "bayer": "ξ Tau",
        "mag": 3.73,
        "spect": "B9 V (ดาวขาวฟ้า)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 10,
        "x": 391,
        "y": 135,
        "r": 7.5,
        "name": "อัลไซโอนี (Alcyone - กระจุกดาวลูกไก่ M45)",
        "bayer": "η Tau",
        "mag": 2.87,
        "spect": "B7 IIIe (กระจุกดาวลูกไก่)",
        "bright": true,
        "color": "#00F0FF"
      }
    ],
    "lines": [
      [
        5,
        6
      ],
      [
        6,
        4
      ],
      [
        4,
        2
      ],
      [
        5,
        7
      ],
      [
        7,
        1
      ],
      [
        1,
        3
      ],
      [
        5,
        8
      ],
      [
        8,
        9
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- North Long Sharp Horn to Elnath (81, 75) -->\n        <path d=\"M 262 200 C 230 150, 160 100, 81 75\" \n              fill=\"none\" stroke=\"#FFD700\" stroke-width=\"9\" stroke-linecap=\"round\" filter=\"drop-shadow(0 0 10px #FFD700)\" />\n        <path d=\"M 262 200 C 230 150, 160 100, 81 75\" \n              fill=\"none\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" />\n        <polygon points=\"81,75 95,85 85,95\" fill=\"#FFD700\" filter=\"drop-shadow(0 0 8px #FFD700)\" />\n\n        <!-- South Long Sharp Horn to Tianguan (45, 174) -->\n        <path d=\"M 239 235 C 190 220, 110 195, 45 174\" \n              fill=\"none\" stroke=\"#FFD700\" stroke-width=\"9\" stroke-linecap=\"round\" filter=\"drop-shadow(0 0 10px #FFD700)\" />\n        <path d=\"M 239 235 C 190 220, 110 195, 45 174\" \n              fill=\"none\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" />\n        <polygon points=\"45,174 60,180 52,192\" fill=\"#FFD700\" filter=\"drop-shadow(0 0 8px #FFD700)\" />\n\n        <!-- Bull Head / Forehead (Hyades V-cluster) -->\n        <polygon points=\"262,200 239,235 290,265 310,230\" fill=\"#FF4757\" fill-opacity=\"0.5\" stroke=\"#FF6B81\" stroke-width=\"3\" />\n        <!-- Broad Bull Muzzle / Snout -->\n        <path d=\"M 285 245 Q 330 265 320 295 Q 280 300 270 270 Z\" fill=\"#E17055\" fill-opacity=\"0.8\" stroke=\"#D63031\" stroke-width=\"2\" />\n        <!-- Nostrils -->\n        <ellipse cx=\"305\" cy=\"275\" rx=\"5\" ry=\"3\" fill=\"#2D3436\" />\n        <ellipse cx=\"290\" cy=\"278\" rx=\"5\" ry=\"3\" fill=\"#2D3436\" />\n\n        <!-- Fierce Glowing Red Eye at Aldebaran (239, 235) -->\n        <circle cx=\"239\" cy=\"235\" r=\"14\" fill=\"#FF0000\" fill-opacity=\"0.5\" filter=\"drop-shadow(0 0 12px #FF0000)\" />\n        <circle cx=\"239\" cy=\"235\" r=\"6\" fill=\"#FFFFFF\" />\n        <circle cx=\"239\" cy=\"235\" r=\"3\" fill=\"#000000\" />\n\n        <!-- Left Eye at Ain (262, 200) -->\n        <circle cx=\"262\" cy=\"200\" r=\"5\" fill=\"#FFD27D\" />\n        <circle cx=\"262\" cy=\"200\" r=\"2\" fill=\"#000000\" />\n\n        <!-- Bull Ears -->\n        <path d=\"M 270 185 Q 310 170 305 195 Z\" fill=\"#FF6B81\" stroke=\"#D63031\" stroke-width=\"2\" />\n        <path d=\"M 230 250 Q 240 285 220 275 Z\" fill=\"#FF6B81\" stroke=\"#D63031\" stroke-width=\"2\" />\n\n        <!-- Powerful Muscular Body & Shoulder Hump -->\n        <path d=\"M 262 200 Q 330 140 400 170 Q 460 210 460 310 L 370 340 L 320 295 Z\" \n              fill=\"#FF4757\" fill-opacity=\"0.3\" stroke=\"#FF6B81\" stroke-width=\"2.5\" />\n        \n        <!-- Forelegs Galloping Forward -->\n        <path d=\"M 370 320 L 455 335 L 450 355 L 360 340 Z\" fill=\"#E17055\" fill-opacity=\"0.6\" stroke=\"#D63031\" stroke-width=\"2\" />\n        <!-- Golden Hoof -->\n        <polygon points=\"455,335 470,340 465,360 450,355\" fill=\"#FFD700\" />\n\n        <!-- Pleiades Cluster (Seven Sisters) Sparkling Nebula at (391, 135) -->\n        <circle cx=\"391\" cy=\"135\" r=\"28\" fill=\"#00F0FF\" fill-opacity=\"0.25\" filter=\"drop-shadow(0 0 16px #00F0FF)\" />\n        <circle cx=\"391\" cy=\"135\" r=\"16\" fill=\"#FFFFFF\" fill-opacity=\"0.3\" />\n        <text x=\"360\" y=\"115\" fill=\"#00F0FF\" font-size=\"10\" font-family=\"sans-serif\" font-weight=\"bold\">✨ กระจุกดาวลูกไก่</text>\n      </g>"
  },
  {
    "id": "gemini",
    "thaiName": "กลุ่มดาวคนคู่ (ฝาแฝด)",
    "zodiacName": "ราศีเมถุน (Gemini)",
    "latinName": "Gemini",
    "symbol": "♊",
    "correctAnswer": "ฝาแฝดยืนข้างกัน",
    "options": [
      {
        "text": "ฝาแฝดยืนข้างกัน",
        "icon": "👯‍♂️",
        "correct": true
      },
      {
        "text": "บันไดลิง",
        "icon": "🪜",
        "correct": false
      },
      {
        "text": "สะพานแขวน",
        "icon": "🌉",
        "correct": false
      },
      {
        "text": "เรือใบสองเสา",
        "icon": "⛵",
        "correct": false
      }
    ],
    "hint": "มองหาดาวสว่าง 2 ดวงคู่กันด้านบนเป็นศีรษะ (พอลลักซ์ซ้ายและคาสเตอร์ขวา) มีแขนยกโอบกอดกัน และมีขาทอดยาวลงมาเคียงคู่กัน!",
    "funFact": "คาสเตอร์และพอลลักซ์เป็นพี่น้องฝาแฝดในเทพนิยายกรีก หนึ่งคนเก่งการต่อสู้ อีกคนเป็นอมตะ คอยปกป้องชาวเรือ!",
    "starGuide": "ดาวพอลลักซ์ (Pollux) สีส้มทองอยู่ทางซ้าย และดาวคาสเตอร์ (Castor) สีขาวสว่างอยู่ทางขวา แขนของทั้งสองโอบกอดกันอย่างอบอุ่น",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 137,
        "y": 127,
        "r": 10,
        "name": "พอลลักซ์ (Pollux - β Gem ศีรษะน้อง)",
        "bayer": "β Gem",
        "mag": 1.14,
        "spect": "K0 III (ดาวยักษ์ส้ม มีดาวเคราะห์บริวาร)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 2,
        "x": 130,
        "y": 183,
        "r": 6.5,
        "name": "แคปปา เจมินอร์ม (κ Gem ไหล่ซ้ายพอลลักซ์)",
        "bayer": "κ Gem",
        "mag": 3.57,
        "spect": "G8 III (ดาวยักษ์ส้มเหลือง)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 3,
        "x": 171,
        "y": 153,
        "r": 5.5,
        "name": "อิปซิลอน เจมินอร์ม (υ Gem แขนขวาพอลลักซ์)",
        "bayer": "υ Gem",
        "mag": 4.06,
        "spect": "M0 III (ดาวยักษ์แดง)",
        "bright": false,
        "color": "#FF7675"
      },
      {
        "id": 4,
        "x": 201,
        "y": 219,
        "r": 7,
        "name": "วาซัต (Wasat - δ Gem เอวพอลลักซ์)",
        "bayer": "δ Gem",
        "mag": 3.5,
        "spect": "F0 IV (ดาวย่อยยักษ์เหลืองขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 5,
        "x": 262,
        "y": 253,
        "r": 6,
        "name": "เมกบูดา (Mekbuda - ζ Gem เข่าขวาพอลลักซ์)",
        "bayer": "ζ Gem",
        "mag": 4.01,
        "spect": "F7-G3 Ib (ดาวแปรแสงเซเฟอิด)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 6,
        "x": 325,
        "y": 320,
        "r": 9,
        "name": "อัลฮีนา (Alhena - γ Gem ปลายเท้าพอลลักซ์)",
        "bayer": "γ Gem",
        "mag": 1.93,
        "spect": "A1.5 IV (ดาวย่อยยักษ์ขาว)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 7,
        "x": 200,
        "y": 300,
        "r": 6.5,
        "name": "แลมบ์ดา เจมินอร์ม (λ Gem เข่าซ้ายพอลลักซ์)",
        "bayer": "λ Gem",
        "mag": 3.58,
        "spect": "A3 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 8,
        "x": 275,
        "y": 365,
        "r": 6.5,
        "name": "อัลซีร์ (Alzirr - ξ Gem ปลายเท้าซ้ายพอลลักซ์)",
        "bayer": "ξ Gem",
        "mag": 3.35,
        "spect": "F5 IV (ดาวเหลืองขาว)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 9,
        "x": 213,
        "y": 75,
        "r": 9.5,
        "name": "คาสเตอร์ (Castor - α Gem ศีรษะพี่)",
        "bayer": "α Gem",
        "mag": 1.58,
        "spect": "A1 V (ระบบดาวฤกษ์ 6 ดวง)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 10,
        "x": 315,
        "y": 75,
        "r": 6.5,
        "name": "ทีตา เจมินอร์ม (θ Gem ศอกขวายกคาสเตอร์)",
        "bayer": "θ Gem",
        "mag": 3.6,
        "spect": "A3 III (ดาวยักษ์ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 11,
        "x": 276,
        "y": 113,
        "r": 5.5,
        "name": "เทา เจมินอร์ม (τ Gem มือขวาคาสเตอร์)",
        "bayer": "τ Gem",
        "mag": 4.41,
        "spect": "K2 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 12,
        "x": 219,
        "y": 145,
        "r": 6.5,
        "name": "ไอโอตา เจมินอร์ม (ι Gem ไหล่ซ้ายคาสเตอร์)",
        "bayer": "ι Gem",
        "mag": 3.78,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 13,
        "x": 326,
        "y": 204,
        "r": 7.5,
        "name": "เมบซูดา (Mebsuta - ε Gem เอวคาสเตอร์)",
        "bayer": "ε Gem",
        "mag": 3.06,
        "spect": "G8 Ib (ดาวยักษ์ใหญ่เหลือง)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 14,
        "x": 372,
        "y": 288,
        "r": 6,
        "name": "นิว เจมินอร์ม (ν Gem เข่าขวาคาสเตอร์)",
        "bayer": "ν Gem",
        "mag": 4.13,
        "spect": "B6 III (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 16,
        "x": 414,
        "y": 242,
        "r": 7.5,
        "name": "เทจัต (Tejat - μ Gem เข่าซ้ายคาสเตอร์)",
        "bayer": "μ Gem",
        "mag": 2.87,
        "spect": "M3 III (ดาวยักษ์แดง)",
        "bright": true,
        "color": "#FF7675"
      },
      {
        "id": 17,
        "x": 455,
        "y": 239,
        "r": 6.5,
        "name": "โพรพัส (Propus - η Gem ข้อเท้าซ้ายคาสเตอร์)",
        "bayer": "η Gem",
        "mag": 3.32,
        "spect": "M3 III (ดาวยักษ์แดง)",
        "bright": false,
        "color": "#FF7675"
      }
    ],
    "lines": [
      [
        1,
        3
      ],
      [
        2,
        3
      ],
      [
        12,
        3
      ],
      [
        4,
        3
      ],
      [
        4,
        7
      ],
      [
        8,
        7
      ],
      [
        4,
        5
      ],
      [
        6,
        5
      ],
      [
        9,
        11
      ],
      [
        12,
        11
      ],
      [
        10,
        11
      ],
      [
        13,
        11
      ],
      [
        13,
        14
      ],
      [
        13,
        16
      ],
      [
        17,
        16
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Castor (Right Brother - White/Cyan) -->\n        <g stroke=\"#70A1FF\" stroke-width=\"2\" fill=\"none\">\n          <!-- Head with Golden Laurel -->\n          <circle cx=\"215\" cy=\"85\" r=\"24\" fill=\"#FFEAA7\" fill-opacity=\"0.7\" stroke=\"#F1C40F\" stroke-width=\"2.5\" />\n          <!-- Hair & Laurel Wreath -->\n          <path d=\"M 195 75 Q 215 55 235 75 Q 215 70 195 75 Z\" fill=\"#F1C40F\" />\n          <!-- Face Details -->\n          <circle cx=\"210\" cy=\"82\" r=\"3\" fill=\"#060919\" /><circle cx=\"211\" cy=\"81\" r=\"1\" fill=\"#fff\" />\n          <path d=\"M 205 94 Q 215 100 225 94\" stroke=\"#D63031\" stroke-width=\"2\" stroke-linecap=\"round\" />\n\n          <!-- Torso & Greek Chiton Tunic -->\n          <path d=\"M 200 108 L 245 125 L 310 195 L 260 215 L 210 145 Z\" fill=\"#70A1FF\" fill-opacity=\"0.5\" stroke=\"#1E90FF\" stroke-width=\"2\" />\n          <!-- Belt / Sash -->\n          <line x1=\"260\" y1=\"215\" x2=\"310\" y2=\"195\" stroke=\"#FFD700\" stroke-width=\"4\" />\n\n          <!-- Raised Right Arm (α -> θ -> τ) -->\n          <path d=\"M 235 100 L 315 75 L 265 125\" fill=\"#FFEAA7\" fill-opacity=\"0.6\" stroke=\"#F1C40F\" stroke-width=\"3\" stroke-linecap=\"round\" />\n          <circle cx=\"315\" cy=\"75\" r=\"6\" fill=\"#FFD700\" />\n\n          <!-- Left & Right Legs -->\n          <path d=\"M 270 215 L 335 260 L 370 285\" stroke=\"#FFEAA7\" stroke-width=\"7\" stroke-linecap=\"round\" />\n          <path d=\"M 290 205 L 385 235 L 410 235 L 445 225\" stroke=\"#FFEAA7\" stroke-width=\"7\" stroke-linecap=\"round\" />\n          <!-- Sandals -->\n          <rect x=\"365\" y=\"280\" width=\"16\" height=\"10\" rx=\"3\" fill=\"#FFD700\" />\n          <rect x=\"435\" y=\"220\" width=\"16\" height=\"10\" rx=\"3\" fill=\"#FFD700\" />\n        </g>\n\n        <!-- Pollux (Left Brother - Orange/Gold) -->\n        <g stroke=\"#FFA502\" stroke-width=\"2\" fill=\"none\">\n          <!-- Head with Golden Laurel -->\n          <circle cx=\"155\" cy=\"125\" r=\"24\" fill=\"#FFEAA7\" fill-opacity=\"0.7\" stroke=\"#F1C40F\" stroke-width=\"2.5\" />\n          <!-- Hair & Laurel Wreath -->\n          <path d=\"M 135 115 Q 155 95 175 115 Q 155 110 135 115 Z\" fill=\"#E67E22\" />\n          <!-- Face Details -->\n          <circle cx=\"150\" cy=\"122\" r=\"3\" fill=\"#060919\" /><circle cx=\"151\" cy=\"121\" r=\"1\" fill=\"#fff\" />\n          <path d=\"M 145 134 Q 155 140 165 134\" stroke=\"#D63031\" stroke-width=\"2\" stroke-linecap=\"round\" />\n\n          <!-- Torso & Greek Chiton Tunic -->\n          <path d=\"M 145 148 L 135 180 L 205 230 L 245 190 L 185 145 Z\" fill=\"#FFA502\" fill-opacity=\"0.5\" stroke=\"#E67E22\" stroke-width=\"2\" />\n          <!-- Belt / Sash -->\n          <line x1=\"205\" y1=\"230\" x2=\"245\" y2=\"190\" stroke=\"#FFD700\" stroke-width=\"4\" />\n\n          <!-- Left Arm reaching out -->\n          <path d=\"M 135 180 L 115 210 L 125 235\" stroke=\"#FFEAA7\" stroke-width=\"6\" stroke-linecap=\"round\" />\n\n          <!-- Left & Right Legs -->\n          <path d=\"M 205 230 L 235 280 L 335 335\" stroke=\"#FFEAA7\" stroke-width=\"7\" stroke-linecap=\"round\" />\n          <path d=\"M 195 230 L 200 300 L 275 365\" stroke=\"#FFEAA7\" stroke-width=\"7\" stroke-linecap=\"round\" />\n          <!-- Sandals -->\n          <rect x=\"330\" y=\"330\" width=\"16\" height=\"10\" rx=\"3\" fill=\"#FFD700\" />\n          <rect x=\"270\" y=\"360\" width=\"16\" height=\"10\" rx=\"3\" fill=\"#FFD700\" />\n        </g>\n\n        <!-- Affectionate Embracing Arms & Hands -->\n        <path d=\"M 175 135 Q 205 120 235 135\" stroke=\"#FFEAA7\" stroke-width=\"8\" stroke-linecap=\"round\" />\n        <circle cx=\"205\" cy=\"130\" r=\"7\" fill=\"#FFD700\" filter=\"drop-shadow(0 0 6px #FFD700)\" />\n      </g>"
  },
  {
    "id": "cancer",
    "thaiName": "กลุ่มดาวปู",
    "zodiacName": "ราศีกรกฎ (Cancer)",
    "latinName": "Cancer",
    "symbol": "♋",
    "correctAnswer": "ปู",
    "options": [
      {
        "text": "ปู",
        "icon": "🦀",
        "correct": true
      },
      {
        "text": "ผีเสื้อ",
        "icon": "🦋",
        "correct": false
      },
      {
        "text": "ร่มกันฝน",
        "icon": "☂️",
        "correct": false
      },
      {
        "text": "กบกระโดด",
        "icon": "🐸",
        "correct": false
      }
    ],
    "hint": "มีรูปตัว 'Y' กลับหัว โดยตรงกลางตัวมี 'กระจุกดาวรังผึ้ง' ระยิบระยับ และมีก้ามแยกออก!",
    "funFact": "ใจกลางกระดองปูมีกระจุกดาวเปิดชื่อว่า 'รังผึ้ง' (Praesepe / M44) ประกอบด้วยดาวฤกษ์กว่า 1,000 ดวง!",
    "starGuide": "กลุ่มดาวรูปตัว Y คว่ำ อยู่ตรงกลางระหว่างกลุ่มดาวคนคู่และกลุ่มดาวสิงโต",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 329,
        "y": 355,
        "r": 6.5,
        "name": "อัลตาร์ฟ (Altarf - β Cnc ปลายก้ามใต้)",
        "bayer": "β Cnc",
        "mag": 3.53,
        "spect": "K4 III (ดาวยักษ์ส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 2,
        "x": 171,
        "y": 313,
        "r": 5.5,
        "name": "อาคูเบนส์ (Acubens - α Cnc ก้ามตะวันออก)",
        "bayer": "α Cnc",
        "mag": 4.26,
        "spect": "A5 m (ดาวระบบ 4 ดวง)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 3,
        "x": 223,
        "y": 213,
        "r": 6.5,
        "name": "อาเซลลัส ออสตราลิส (δ Cnc กลางกระดองใต้)",
        "bayer": "δ Cnc",
        "mag": 3.94,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 4,
        "x": 228,
        "y": 160,
        "r": 5.5,
        "name": "อาเซลลัส บอเรียลิส (γ Cnc กลางกระดองเหนือ)",
        "bayer": "γ Cnc",
        "mag": 4.66,
        "spect": "A1 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 5,
        "x": 215,
        "y": 45,
        "r": 5.5,
        "name": "ไอโอตา แคนครี (ι Cnc ก้ามเหนือ)",
        "bayer": "ι Cnc",
        "mag": 4.03,
        "spect": "G8 III (ดาวยักษ์เหลือง)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 6,
        "x": 239,
        "y": 189,
        "r": 7.5,
        "name": "กระจุกดาวรังผึ้ง (Beehive / M44 Praesepe)",
        "bayer": "M44",
        "mag": 3.1,
        "spect": "กระจุกดาวเปิด",
        "bright": true,
        "color": "#00F0FF"
      }
    ],
    "lines": [
      [
        5,
        4
      ],
      [
        4,
        3
      ],
      [
        3,
        2
      ],
      [
        3,
        1
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Big Crab Shell / Carapace over M44 Praesepe (239, 189) -->\n        <ellipse cx=\"239\" cy=\"189\" rx=\"65\" ry=\"48\" fill=\"#FF4757\" fill-opacity=\"0.65\" stroke=\"#FF6B81\" stroke-width=\"3.5\" filter=\"drop-shadow(0 0 14px rgba(255, 71, 87, 0.4))\" />\n        <ellipse cx=\"239\" cy=\"189\" rx=\"45\" ry=\"32\" fill=\"#FF6B81\" fill-opacity=\"0.3\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" stroke-dasharray=\"5,5\" />\n\n        <!-- Glowing Beehive Cluster M44 Core -->\n        <circle cx=\"239\" cy=\"189\" r=\"22\" fill=\"#00F0FF\" fill-opacity=\"0.35\" filter=\"drop-shadow(0 0 12px #00F0FF)\" />\n        <text x=\"210\" y=\"193\" fill=\"#FFFFFF\" font-size=\"11\" font-weight=\"bold\">✨ M44</text>\n\n        <!-- Big Right Pinching Claw (to Iota Cnc 215, 45) -->\n        <path d=\"M 215 145 C 190 90, 160 50, 215 45 C 230 45, 250 80, 225 105 C 265 75, 275 110, 235 135 Z\" \n              fill=\"#FF4757\" stroke=\"#FF6B81\" stroke-width=\"3\" filter=\"drop-shadow(0 0 8px rgba(255, 71, 87, 0.5))\" />\n        <!-- Big Left Pinching Claw -->\n        <path d=\"M 265 145 C 290 90, 320 50, 265 45 C 250 45, 230 80, 255 105 C 215 75, 205 110, 245 135 Z\" \n              fill=\"#FF4757\" stroke=\"#FF6B81\" stroke-width=\"3\" filter=\"drop-shadow(0 0 8px rgba(255, 71, 87, 0.5))\" />\n\n        <!-- Crab Stalk Eyes with Pupils -->\n        <rect x=\"220\" y=\"130\" width=\"8\" height=\"18\" rx=\"3\" fill=\"#FF4757\" />\n        <circle cx=\"224\" cy=\"130\" r=\"9\" fill=\"#FFFFFF\" stroke=\"#FF4757\" stroke-width=\"2\" />\n        <circle cx=\"224\" cy=\"130\" r=\"4.5\" fill=\"#060919\" />\n        <circle cx=\"226\" cy=\"128\" r=\"1.5\" fill=\"#FFFFFF\" />\n\n        <rect x=\"250\" y=\"130\" width=\"8\" height=\"18\" rx=\"3\" fill=\"#FF4757\" />\n        <circle cx=\"254\" cy=\"130\" r=\"9\" fill=\"#FFFFFF\" stroke=\"#FF4757\" stroke-width=\"2\" />\n        <circle cx=\"254\" cy=\"130\" r=\"4.5\" fill=\"#060919\" />\n        <circle cx=\"256\" cy=\"128\" r=\"1.5\" fill=\"#FFFFFF\" />\n\n        <!-- Cute Smile -->\n        <path d=\"M 230 165 Q 239 175 248 165\" stroke=\"#060919\" stroke-width=\"2.5\" stroke-linecap=\"round\" fill=\"none\" />\n\n        <!-- Left Walking Legs to Acubens (171, 313) -->\n        <path d=\"M 185 180 Q 130 220 150 280 Q 155 310 171 313\" stroke=\"#FFA502\" stroke-width=\"6\" stroke-linecap=\"round\" fill=\"none\" />\n        <path d=\"M 185 200 Q 120 250 130 320\" stroke=\"#FFA502\" stroke-width=\"5\" stroke-linecap=\"round\" fill=\"none\" />\n        <path d=\"M 195 220 Q 140 280 145 350\" stroke=\"#FFA502\" stroke-width=\"5\" stroke-linecap=\"round\" fill=\"none\" />\n\n        <!-- Right Walking Legs to Altarf (329, 355) -->\n        <path d=\"M 290 180 Q 350 220 330 280 Q 325 310 329 355\" stroke=\"#FFA502\" stroke-width=\"6\" stroke-linecap=\"round\" fill=\"none\" />\n        <path d=\"M 290 200 Q 360 250 350 320\" stroke=\"#FFA502\" stroke-width=\"5\" stroke-linecap=\"round\" fill=\"none\" />\n        <path d=\"M 280 220 Q 340 280 335 350\" stroke=\"#FFA502\" stroke-width=\"5\" stroke-linecap=\"round\" fill=\"none\" />\n      </g>"
  },
  {
    "id": "leo",
    "thaiName": "กลุ่มดาวสิงโต",
    "zodiacName": "ราศีสิงห์ (Leo)",
    "latinName": "Leo",
    "symbol": "♌",
    "correctAnswer": "สิงโต",
    "options": [
      {
        "text": "สิงโต",
        "icon": "🦁",
        "correct": true
      },
      {
        "text": "กระรอก",
        "icon": "🐿️",
        "correct": false
      },
      {
        "text": "แมวน้ำ",
        "icon": "🦭",
        "correct": false
      },
      {
        "text": "เตารีด",
        "icon": "🧼",
        "correct": false
      }
    ],
    "hint": "มีส่วนหัวเป็นรูปโค้งเคียวเกี่ยวข้าว (The Sickle) และมีลำตัวรูปสามเหลี่ยมทอดไปหาหางสิงโต!",
    "funFact": "ดาวที่สว่างที่สุดคือ 'เรกูลัส' (Regulus) หรือหัวใจสิงห์ หมุนรอบตัวเองเร็วมากจนตัวแบนคล้ายผลส้ม!",
    "starGuide": "มองหาเคียวเกี่ยวข้าวทางทิศตะวันตกและดาวหัวใจสิงห์สีฟ้าขาวสว่างจ้า",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 361,
        "y": 245,
        "r": 9,
        "name": "เรกูลัส (Regulus - α Leo หัวใจสิงห์)",
        "bayer": "α Leo",
        "mag": 1.36,
        "spect": "B7 V (ดาวสีฟ้าขาว สว่างที่สุดในกลุ่มดาว)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 2,
        "x": 63,
        "y": 243,
        "r": 9,
        "name": "เดเนโบลา (Denebola - β Leo หางสิงโต)",
        "bayer": "β Leo",
        "mag": 2.14,
        "spect": "A3 V (ดาวแคระขาว)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 3,
        "x": 306,
        "y": 167,
        "r": 9,
        "name": "แอลเจอบา (Algieba - γ Leo คอสิงโต)",
        "bayer": "γ Leo",
        "mag": 2.01,
        "spect": "K0 III (ดาวยักษ์ส้มคู่)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 4,
        "x": 166,
        "y": 174,
        "r": 7.5,
        "name": "โซสมา (Zosma - δ Leo สะโพกบน)",
        "bayer": "δ Leo",
        "mag": 2.56,
        "spect": "A4 V (ดาวแคระขาว)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 5,
        "x": 381,
        "y": 119,
        "r": 7.5,
        "name": "อัลเกนูบี (Algenubi - ε Leo ยอดหัวสิงโต)",
        "bayer": "ε Leo",
        "mag": 2.97,
        "spect": "G1 II (ดาวยักษ์สว่างเหลือง)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 6,
        "x": 313,
        "y": 119,
        "r": 6.5,
        "name": "อัดฮาเฟรา (Adhafera - ζ Leo แผงคอ)",
        "bayer": "ζ Leo",
        "mag": 3.43,
        "spect": "F0 III (ดาวยักษ์ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 7,
        "x": 354,
        "y": 192,
        "r": 6.5,
        "name": "อัลจับฮาห์ (Al Jabhah - η Leo อกสิงโต)",
        "bayer": "η Leo",
        "mag": 3.48,
        "spect": "A0 Ib (ดาวยักษ์ใหญ่ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 8,
        "x": 173,
        "y": 238,
        "r": 6.5,
        "name": "เชอร์ทาน (Chertan - θ Leo สะโพกล่าง)",
        "bayer": "θ Leo",
        "mag": 3.33,
        "spect": "A2 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 9,
        "x": 369,
        "y": 78,
        "r": 6.5,
        "name": "ราซาลาส (Rasalas - μ Leo ปลายจมูกสิงห์)",
        "bayer": "μ Leo",
        "mag": 3.88,
        "spect": "K2 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 10,
        "x": 427,
        "y": 110,
        "r": 7,
        "name": "Alterf (Lambda Leonis)",
        "bayer": "λ Leo",
        "mag": 4.28,
        "spect": "V",
        "bright": false,
        "color": "#ffa502"
      },
      {
        "id": 11,
        "x": 434,
        "y": 68,
        "r": 7,
        "name": "Kappa Leonis",
        "bayer": "κ Leo",
        "mag": 4.44,
        "spect": "V",
        "bright": false,
        "color": "#ffa502"
      },
      {
        "id": 12,
        "x": 439,
        "y": 246,
        "r": 7,
        "name": "Subra",
        "bayer": "ο Leo",
        "mag": 3.52,
        "spect": "V",
        "bright": false,
        "color": "#94f8ff"
      }
    ],
    "lines": [
      [
        1,
        7
      ],
      [
        7,
        3
      ],
      [
        3,
        6
      ],
      [
        6,
        9
      ],
      [
        9,
        5
      ],
      [
        3,
        4
      ],
      [
        4,
        2
      ],
      [
        2,
        8
      ],
      [
        8,
        1
      ],
      [
        4,
        8
      ],
      [
        11,
        9
      ],
      [
        11,
        10
      ],
      [
        5,
        10
      ],
      [
        5,
        7
      ],
      [
        12,
        1
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Lion Head & Magnificent Flowing Mane outlining The Sickle (455, 133 -> 380, 299) -->\n        <path d=\"M 370 270 C 430 250, 480 200, 475 120 C 470 60, 400 40, 360 80 C 330 110, 330 160, 350 200 C 320 220, 330 270, 370 270 Z\" \n              fill=\"#FFA502\" fill-opacity=\"0.5\" stroke=\"#FFD700\" stroke-width=\"3\" filter=\"drop-shadow(0 0 12px #FFA502)\" />\n        \n        <!-- Noble Lion Face Profile -->\n        <circle cx=\"410\" cy=\"140\" r=\"32\" fill=\"#FFEAA7\" fill-opacity=\"0.8\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <!-- Eye -->\n        <ellipse cx=\"425\" cy=\"130\" rx=\"6\" ry=\"4\" fill=\"#060919\" />\n        <circle cx=\"427\" cy=\"128\" r=\"1.5\" fill=\"#FFFFFF\" />\n        <!-- Nose & Whiskers -->\n        <polygon points=\"440,145 448,140 448,150\" fill=\"#D63031\" />\n        <line x1=\"435\" y1=\"152\" x2=\"455\" y2=\"155\" stroke=\"#2D3436\" stroke-width=\"1.5\" />\n        <line x1=\"435\" y1=\"156\" x2=\"455\" y2=\"162\" stroke=\"#2D3436\" stroke-width=\"1.5\" />\n        <!-- Ear -->\n        <path d=\"M 390 115 Q 400 95 415 110 Z\" fill=\"#FFA502\" stroke=\"#E67E22\" stroke-width=\"2\" />\n\n        <!-- Lion Mane Swirls -->\n        <path d=\"M 455 133 Q 480 80 432 101 Q 380 70 352 138 Q 320 180 341 188 Q 350 250 380 299\" \n              fill=\"none\" stroke=\"#FFD700\" stroke-width=\"6\" stroke-linecap=\"round\" />\n\n        <!-- Glowing Heart at Regulus (380, 299) -->\n        <circle cx=\"380\" cy=\"299\" r=\"18\" fill=\"#00F0FF\" fill-opacity=\"0.4\" filter=\"drop-shadow(0 0 14px #00F0FF)\" />\n        <circle cx=\"380\" cy=\"299\" r=\"8\" fill=\"#FFFFFF\" />\n\n        <!-- Powerful Muscular Body (extending West to Denebola 45, 262) -->\n        <path d=\"M 350 200 Q 250 160 161 178 Q 90 200 45 262 L 120 280 Q 200 240 280 270 L 350 260 Z\" \n              fill=\"#FFA502\" fill-opacity=\"0.35\" stroke=\"#FF7F50\" stroke-width=\"2.5\" />\n\n        <!-- Forelegs and Paws -->\n        <path d=\"M 330 260 L 320 370 L 345 370 L 360 270\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <ellipse cx=\"332\" cy=\"370\" rx=\"14\" ry=\"7\" fill=\"#FFD700\" />\n\n        <path d=\"M 270 265 L 260 365 L 285 365 L 295 270\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <ellipse cx=\"272\" cy=\"365\" rx=\"14\" ry=\"7\" fill=\"#FFD700\" />\n\n        <!-- Hind Legs -->\n        <path d=\"M 160 210 Q 140 290 130 365 L 155 365 Q 170 300 190 240\" fill=\"#FFEAA7\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <ellipse cx=\"142\" cy=\"365\" rx=\"14\" ry=\"7\" fill=\"#FFD700\" />\n\n        <!-- Long Majestic Tail with Bushy Tuft at Denebola (45, 262) -->\n        <path d=\"M 120 220 Q 70 170 45 262\" fill=\"none\" stroke=\"#FF7F50\" stroke-width=\"5\" stroke-linecap=\"round\" />\n        <circle cx=\"45\" cy=\"262\" r=\"16\" fill=\"#FF7F50\" stroke=\"#FFD700\" stroke-width=\"2.5\" filter=\"drop-shadow(0 0 10px #FF7F50)\" />\n      </g>"
  },
  {
    "id": "virgo",
    "thaiName": "กลุ่มดาวหญิงสาว (เทพีพรหมจารี)",
    "zodiacName": "ราศีกันย์ (Virgo)",
    "latinName": "Virgo",
    "symbol": "♍",
    "correctAnswer": "หญิงสาว",
    "options": [
      {
        "text": "หญิงสาว",
        "icon": "👧",
        "correct": true
      },
      {
        "text": "ม้าน้ำ",
        "icon": "🫧",
        "correct": false
      },
      {
        "text": "กระต่ายหูยาว",
        "icon": "🐰",
        "correct": false
      },
      {
        "text": "ต้นสน",
        "icon": "🎄",
        "correct": false
      }
    ],
    "hint": "มีดาวฤกษ์สว่างสีฟ้าขาว 'สไปกา' อยู่ที่รวงข้าวสาลี และมีเส้นลำตัวหญิงสาวกางปีกกว้าง!",
    "funFact": "ดาว 'สไปกา' (Spica) เป็นระบบดาวคู่สีฟ้าขาว สว่างกว่าดวงอาทิตย์ถึง 12,000 เท่า!",
    "starGuide": "ลากเส้นโค้งต่อจากด้ามกระบวยกลุ่มดาวหมีใหญ่ ผ่านดาวอาร์คทูรัส แล้วจะพุ่งตรงมายังดาวสไปกา",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 334,
        "y": 224,
        "r": 11,
        "name": "สไปกา (Spica - α Vir รวงข้าวสาลี)",
        "bayer": "α Vir",
        "mag": 0.98,
        "spect": "B1 III-IV (ดาวคู่ยักษ์ฟ้าขาว สว่างที่สุด)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 2,
        "x": 407,
        "y": 41,
        "r": 6.5,
        "name": "ซาวิยาวา (Zavijava - β Vir ศีรษะ)",
        "bayer": "β Vir",
        "mag": 3.59,
        "spect": "F9 V (ดาวสีเหลืองนวล)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 3,
        "x": 330,
        "y": 113,
        "r": 7.5,
        "name": "พอริมา (Porrima - γ Vir ไหล่/อก)",
        "bayer": "γ Vir",
        "mag": 2.74,
        "spect": "F0 V (ดาวคู่ขาวบริสุทธิ์)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 4,
        "x": 284,
        "y": 116,
        "r": 6.5,
        "name": "มิเนเลาวา (Minelauva - δ Vir เอว)",
        "bayer": "δ Vir",
        "mag": 3.38,
        "spect": "M3 III (ดาวยักษ์แดง)",
        "bright": false,
        "color": "#FF4757"
      },
      {
        "id": 5,
        "x": 235,
        "y": 73,
        "r": 7.5,
        "name": "วินเดเมียทริกซ์ (Vindemiatrix - ε Vir ปลายปีกขวา)",
        "bayer": "ε Vir",
        "mag": 2.85,
        "spect": "G8 III (ดาวยักษ์เหลืองทอง)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 6,
        "x": 261,
        "y": 192,
        "r": 6.5,
        "name": "เฮเซ (Heze - ζ Vir สะโพก)",
        "bayer": "ζ Vir",
        "mag": 3.38,
        "spect": "A3 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 7,
        "x": 377,
        "y": 85,
        "r": 6.5,
        "name": "ซาเนียห์ (Zaniah - η Vir แขนซ้าย)",
        "bayer": "η Vir",
        "mag": 3.89,
        "spect": "A2 IV (ดาวขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 8,
        "x": 253,
        "y": 281,
        "r": 5.5,
        "name": "เซียร์มา (Syrma - ι Vir ชายกระโปรง/เท้า)",
        "bayer": "ι Vir",
        "mag": 4.07,
        "spect": "F7 III (ดาวยักษ์เหลือง)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 9,
        "x": 297,
        "y": 299,
        "r": 5.5,
        "name": "คัง (Kang - κ Vir ปลายเท้า)",
        "bayer": "κ Vir",
        "mag": 4.18,
        "spect": "K2.5 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 10,
        "x": 216,
        "y": 346,
        "r": 7,
        "name": "Mu Virginis",
        "bayer": "μ Vir",
        "mag": 3.88,
        "spect": "V",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 11,
        "x": 153,
        "y": 310,
        "r": 7,
        "name": "Maenalus (109 Virginis)",
        "bayer": "109 Vir",
        "mag": 3.72,
        "spect": "V",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 12,
        "x": 204,
        "y": 231,
        "r": 7,
        "name": "Tau Virginis",
        "bayer": "τ Vir",
        "mag": 4.28,
        "spect": "V",
        "bright": false,
        "color": "#ffffff"
      }
    ],
    "lines": [
      [
        2,
        7
      ],
      [
        7,
        3
      ],
      [
        3,
        4
      ],
      [
        4,
        5
      ],
      [
        4,
        6
      ],
      [
        3,
        1
      ],
      [
        8,
        9
      ],
      [
        6,
        12
      ],
      [
        11,
        12
      ],
      [
        11,
        10
      ],
      [
        8,
        10
      ],
      [
        9,
        1
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Maiden Goddess Head at Zavijava (455, 179) -->\n        <circle cx=\"440\" cy=\"165\" r=\"22\" fill=\"#FFEAA7\" fill-opacity=\"0.75\" stroke=\"#FDA7DF\" stroke-width=\"2\" />\n        <!-- Flowing Celestial Hair -->\n        <path d=\"M 420 150 Q 455 120 465 160 Q 460 200 425 185 Z\" fill=\"#F1C40F\" fill-opacity=\"0.9\" />\n        <!-- Serene Face -->\n        <circle cx=\"435\" cy=\"162\" r=\"3\" fill=\"#060919\" />\n        <path d=\"M 430 172 Q 436 177 442 172\" stroke=\"#D63031\" stroke-width=\"1.5\" fill=\"none\" stroke-linecap=\"round\" />\n\n        <!-- Magnificent Angelic Wings (sweeping up to Vindemiatrix 253, 75) -->\n        <path d=\"M 330 190 Q 290 100 253 75 Q 310 110 330 140 Q 360 80 410 70 Q 380 120 360 170 Z\" \n              fill=\"#70A1FF\" fill-opacity=\"0.45\" stroke=\"#00F0FF\" stroke-width=\"2.5\" filter=\"drop-shadow(0 0 12px #00F0FF)\" />\n        <path d=\"M 330 190 Q 280 110 253 75 Q 260 120 290 160\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" fill=\"none\" />\n\n        <!-- Flowing Celestial Starlit Gown (from Porrima 311, 215 down to Feet 45, 267) -->\n        <path d=\"M 425 185 L 311 215 L 272 161 L 162 192 L 188 325 L 45 267 L 54 315 L 140 360 L 280 340 Z\" \n              fill=\"#9980FA\" fill-opacity=\"0.4\" stroke=\"#833471\" stroke-width=\"2\" />\n\n        <!-- Glowing Radiant Wheat Sheaf at Spica (188, 325) -->\n        <ellipse cx=\"188\" cy=\"325\" rx=\"28\" ry=\"16\" transform=\"rotate(-30 188 325)\" fill=\"#FFD700\" fill-opacity=\"0.8\" stroke=\"#F1C40F\" stroke-width=\"3\" filter=\"drop-shadow(0 0 16px #FFD700)\" />\n        <path d=\"M 160 340 L 220 310 M 170 330 L 210 315 M 175 350 L 205 305\" stroke=\"#FFA502\" stroke-width=\"3\" stroke-linecap=\"round\" />\n        <circle cx=\"188\" cy=\"325\" r=\"8\" fill=\"#FFFFFF\" />\n        <text x=\"145\" y=\"365\" fill=\"#FFD700\" font-size=\"11\" font-weight=\"bold\">🌾 รวงข้าวสาลี</text>\n      </g>"
  },
  {
    "id": "libra",
    "thaiName": "กลุ่มดาวคันชั่ง",
    "zodiacName": "ราศีตุล (Libra)",
    "latinName": "Libra",
    "symbol": "♎",
    "correctAnswer": "ตาชั่ง",
    "options": [
      {
        "text": "ตาชั่ง",
        "icon": "⚖️",
        "correct": true
      },
      {
        "text": "ว่าวสามเหลี่ยม",
        "icon": "🪁",
        "correct": false
      },
      {
        "text": "เต็นท์ตั้งแคมป์",
        "icon": "⛺",
        "correct": false
      },
      {
        "text": "เพชร",
        "icon": "💎",
        "correct": false
      }
    ],
    "hint": "มีรูปทรงสี่เหลี่ยมข้าวหลามตัด มีคานบนและจานตาชั่งสองข้างถ่วงสมดุลกันอย่างสง่างาม!",
    "funFact": "เป็นราศีเดียวใน 12 จักราศีที่เป็นสิ่งของเครื่องใช้ ดาวซูเบนเอลเชมาลีมีประกายสีเขียวมรกตที่หาได้ยากบนฟ้า!",
    "starGuide": "ดาวซูเบนเอลเชมาลี (Zubeneschamali) อยู่ที่ยอดบน และดาวซูเบนเอลเกนูบี (Zubenelgenubi) อยู่ที่มุมล่างซ้าย",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 155,
        "y": 290,
        "r": 8.5,
        "name": "ซูเบนเอลเกนูบี (Zubenelgenubi - α2 Lib จานใต้)",
        "bayer": "α2 Lib",
        "mag": 2.75,
        "spect": "A3 IV (ดาวคู่ขาวสว่าง)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 2,
        "x": 275,
        "y": 85,
        "r": 9,
        "name": "ซูเบนเอลเชมาลี (Zubeneschamali - β Lib ยอดคาน)",
        "bayer": "β Lib",
        "mag": 2.61,
        "spect": "B8 V (ดาวสีฟ้าอมเขียวมรกต)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 3,
        "x": 395,
        "y": 150,
        "r": 7,
        "name": "ซูเบนเอลอัครับ (Zubenelakrab - γ Lib จานตะวันออก)",
        "bayer": "γ Lib",
        "mag": 3.91,
        "spect": "G8.5 III (ดาวยักษ์ส้มเหลือง)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 4,
        "x": 350,
        "y": 265,
        "r": 7.5,
        "name": "บราเคียม (Brachium - σ Lib ฐานล่าง)",
        "bayer": "σ Lib",
        "mag": 3.25,
        "spect": "M2.5 III (ดาวยักษ์แดง)",
        "bright": true,
        "color": "#FF4757"
      }
    ],
    "lines": [
      [
        1,
        2
      ],
      [
        2,
        3
      ],
      [
        3,
        4
      ],
      [
        4,
        1
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Scale Diamond Body Framework -->\n        <polygon points=\"275,85 395,150 350,265 155,290\" fill=\"#FFA502\" fill-opacity=\"0.15\" stroke=\"#FFD700\" stroke-width=\"2\" stroke-dasharray=\"6,6\" />\n\n        <!-- Main Ornate Balance Beam (Top) -->\n        <path d=\"M 100 185 L 410 95\" stroke=\"#FFD700\" stroke-width=\"8\" stroke-linecap=\"round\" filter=\"drop-shadow(0 0 10px #FFD700)\" />\n        <path d=\"M 100 185 L 410 95\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" />\n        \n        <!-- Central Fulcrum & Decorative Pillar at Star 2 (275, 85) -->\n        <circle cx=\"260\" cy=\"138\" r=\"14\" fill=\"#FFA502\" stroke=\"#FFD700\" stroke-width=\"3\" filter=\"drop-shadow(0 0 8px #FFD700)\" />\n        <circle cx=\"260\" cy=\"138\" r=\"5\" fill=\"#FFFFFF\" />\n        <!-- Vertical Balance Needle / Indicator -->\n        <line x1=\"260\" y1=\"138\" x2=\"275\" y2=\"85\" stroke=\"#FFD700\" stroke-width=\"5\" stroke-linecap=\"round\" />\n        <line x1=\"260\" y1=\"138\" x2=\"295\" y2=\"230\" stroke=\"#FFD700\" stroke-width=\"4\" stroke-linecap=\"round\" />\n\n        <!-- Left Pan (Upper-Left at 100, 185) with 3 Hanging Chains -->\n        <line x1=\"100\" y1=\"185\" x2=\"70\" y2=\"245\" stroke=\"#FFFFFF\" stroke-width=\"2\" stroke-dasharray=\"2,2\" />\n        <line x1=\"100\" y1=\"185\" x2=\"100\" y2=\"250\" stroke=\"#FFFFFF\" stroke-width=\"2\" />\n        <line x1=\"100\" y1=\"185\" x2=\"130\" y2=\"245\" stroke=\"#FFFFFF\" stroke-width=\"2\" stroke-dasharray=\"2,2\" />\n        <!-- Left Pan 3D Dish -->\n        <path d=\"M 60 245 Q 100 285 140 245 Z\" fill=\"#FFA502\" fill-opacity=\"0.75\" stroke=\"#FFD700\" stroke-width=\"3\" filter=\"drop-shadow(0 0 8px #FFA502)\" />\n        <ellipse cx=\"100\" cy=\"245\" rx=\"40\" ry=\"10\" fill=\"#FFD700\" fill-opacity=\"0.5\" stroke=\"#FFD700\" stroke-width=\"2\" />\n        <!-- Weight in Left Pan -->\n        <circle cx=\"100\" cy=\"240\" r=\"8\" fill=\"#00F0FF\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" />\n\n        <!-- Right Pan (Lower-Left at Zubenelgenubi 155, 290) with 3 Hanging Chains -->\n        <line x1=\"200\" y1=\"210\" x2=\"170\" y2=\"295\" stroke=\"#FFFFFF\" stroke-width=\"2\" stroke-dasharray=\"2,2\" />\n        <line x1=\"200\" y1=\"210\" x2=\"200\" y2=\"300\" stroke=\"#FFFFFF\" stroke-width=\"2\" />\n        <line x1=\"200\" y1=\"210\" x2=\"230\" y2=\"295\" stroke=\"#FFFFFF\" stroke-width=\"2\" stroke-dasharray=\"2,2\" />\n        <!-- Right Pan 3D Dish -->\n        <path d=\"M 160 295 Q 200 335 240 295 Z\" fill=\"#FFA502\" fill-opacity=\"0.75\" stroke=\"#FFD700\" stroke-width=\"3\" filter=\"drop-shadow(0 0 8px #FFA502)\" />\n        <ellipse cx=\"200\" cy=\"295\" rx=\"40\" ry=\"10\" fill=\"#FFD700\" fill-opacity=\"0.5\" stroke=\"#FFD700\" stroke-width=\"2\" />\n        <!-- Weight in Right Pan -->\n        <circle cx=\"200\" cy=\"290\" r=\"8\" fill=\"#00F0FF\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" />\n      </g>"
  },
  {
    "id": "scorpio",
    "thaiName": "กลุ่มดาวแมงป่อง",
    "zodiacName": "ราศีพิจิก (Scorpius)",
    "latinName": "Scorpius",
    "symbol": "♏",
    "correctAnswer": "แมงป่อง",
    "options": [
      {
        "text": "แมงป่อง",
        "icon": "🦂",
        "correct": true
      },
      {
        "text": "เบ็ดตกปลา",
        "icon": "🎣",
        "correct": false
      },
      {
        "text": "ไดโนเสาร์",
        "icon": "🦕",
        "correct": false
      },
      {
        "text": "มังกร",
        "icon": "🐉",
        "correct": false
      }
    ],
    "hint": "มีก้าม 3 แฉกด้านหน้า มีหัวใจสีแดงแอนทาเรส และมีหางโค้งยาวรูปตัว J งอตวัดขึ้นพร้อมเหล็กใน!",
    "funFact": "ใจกลางลำตัวมีดาว 'แอนทาเรส' ดาวยักษ์แดงมหึมาขนาดใหญ่กว่าดวงอาทิตย์กว่า 700 เท่า!",
    "starGuide": "กลุ่มดาวรูปตัว J ชัดเจนที่สุดบนท้องฟ้าฤดูฝน มองหาดาวสีแดงแอนทาเรส",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 316,
        "y": 133,
        "r": 11,
        "name": "แอนทาเรส (Antares - α Sco หัวใจสีแดง)",
        "bayer": "α Sco",
        "mag": 1.06,
        "spect": "M1.5 Iab (ดาวยักษ์ใหญ่แดง สว่างสุด)",
        "bright": true,
        "color": "#FF4757"
      },
      {
        "id": 2,
        "x": 139,
        "y": 274,
        "r": 9,
        "name": "ชอลา (Shaula - λ Sco ปลายเหล็กใน)",
        "bayer": "λ Sco",
        "mag": 1.62,
        "spect": "B2 IV (ดาวย่อยยักษ์ฟ้าขาว)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 3,
        "x": 128,
        "y": 352,
        "r": 9,
        "name": "ซาร์กัส (Sargas - θ Sco โค้งหางล่าง)",
        "bayer": "θ Sco",
        "mag": 1.86,
        "spect": "F0 II (ดาวยักษ์สว่างเหลืองขาว)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 4,
        "x": 396,
        "y": 82,
        "r": 7.5,
        "name": "ดชูบา (Dschubba - δ Sco หน้าผากแมงป่อง)",
        "bayer": "δ Sco",
        "mag": 2.29,
        "spect": "B0.3 IV (ดาวย่อยยักษ์ฟ้า)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 5,
        "x": 258,
        "y": 237,
        "r": 7.5,
        "name": "ลาราวาก (Larawag - ε Sco โคนหาง)",
        "bayer": "ε Sco",
        "mag": 2.29,
        "spect": "K2.5 III (ดาวยักษ์ส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 6,
        "x": 114,
        "y": 299,
        "r": 7.5,
        "name": "เกอร์แทบ (Girtab - κ Sco หางตวัด)",
        "bayer": "κ Sco",
        "mag": 2.39,
        "spect": "B1.5 III (ดาวยักษ์ฟ้าขาว)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 7,
        "x": 382,
        "y": 44,
        "r": 7.5,
        "name": "กราฟเฟียส (Acrab - β Sco ก้ามบน)",
        "bayer": "β Sco",
        "mag": 2.56,
        "spect": "B1 V (ดาวคู่ฟ้าขาว)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 8,
        "x": 147,
        "y": 276,
        "r": 7.5,
        "name": "เลซัท (Lesath - υ Sco ปลายเหล็กในคู่)",
        "bayer": "υ Sco",
        "mag": 2.7,
        "spect": "B2 IV (ดาวฟ้าขาว)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 9,
        "x": 400,
        "y": 128,
        "r": 7.5,
        "name": "ฟาง (Fang - π Sco ก้ามล่าง)",
        "bayer": "π Sco",
        "mag": 2.89,
        "spect": "B1 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 10,
        "x": 338,
        "y": 122,
        "r": 7.5,
        "name": "อัลนิยัต (Alniyat - σ Sco อกแมงป่อง)",
        "bayer": "σ Sco",
        "mag": 2.9,
        "spect": "B1 III (ดาวยักษ์ฟ้า)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 11,
        "x": 298,
        "y": 156,
        "r": 7.5,
        "name": "ไพเคาฮาเล (Tau Sco อกล่าง)",
        "bayer": "τ Sco",
        "mag": 2.82,
        "spect": "B0.2 V (ดาวแคระน้ำเงินร้อนจัด)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 12,
        "x": 254,
        "y": 286,
        "r": 7.5,
        "name": "มิว สกอร์ปี (μ1 Sco ท้อง)",
        "bayer": "μ1 Sco",
        "mag": 3,
        "spect": "B1.5 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 13,
        "x": 246,
        "y": 343,
        "r": 6.5,
        "name": "เซตา สกอร์ปี (ζ2 Sco ก้นหาง)",
        "bayer": "ζ2 Sco",
        "mag": 3.62,
        "spect": "K4 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 14,
        "x": 198,
        "y": 355,
        "r": 6.5,
        "name": "อีตา สกอร์ปี (η Sco)",
        "bayer": "η Sco",
        "mag": 3.32,
        "spect": "F3 III-IV (ดาวย่อยยักษ์ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 15,
        "x": 100,
        "y": 314,
        "r": 7.5,
        "name": "ไอโอตา สกอร์ปี (ι1 Sco)",
        "bayer": "ι1 Sco",
        "mag": 2.99,
        "spect": "F2 Ia (ดาวยักษ์ใหญ่เหลืองขาว)",
        "bright": false,
        "color": "#FFD27D"
      }
    ],
    "lines": [
      [
        4,
        10
      ],
      [
        10,
        1
      ],
      [
        1,
        11
      ],
      [
        11,
        5
      ],
      [
        5,
        12
      ],
      [
        12,
        13
      ],
      [
        13,
        14
      ],
      [
        14,
        3
      ],
      [
        3,
        15
      ],
      [
        15,
        6
      ],
      [
        6,
        2
      ],
      [
        2,
        8
      ],
      [
        7,
        10
      ],
      [
        9,
        10
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- 3 Front Sharp Pincer Claws spreading from Dschubba (396, 82) -->\n        <path d=\"M 396 82 L 382 45 Q 420 20 410 65 Q 430 40 450 60 Z\" fill=\"#FF4757\" stroke=\"#FF6B81\" stroke-width=\"2.5\" />\n        <path d=\"M 396 82 L 400 128 Q 440 120 445 150 Q 455 120 470 140 Z\" fill=\"#FF4757\" stroke=\"#FF6B81\" stroke-width=\"2.5\" />\n        <path d=\"M 396 82 L 440 85 Q 470 80 460 105 Z\" fill=\"#FF4757\" stroke=\"#FF6B81\" stroke-width=\"2\" />\n\n        <!-- Segmented Armored Body over Antares (316, 133) -->\n        <ellipse cx=\"316\" cy=\"133\" rx=\"34\" ry=\"24\" fill=\"#D63031\" fill-opacity=\"0.7\" stroke=\"#FF4757\" stroke-width=\"3\" filter=\"drop-shadow(0 0 12px #D63031)\" />\n        <ellipse cx=\"280\" cy=\"170\" rx=\"26\" ry=\"18\" fill=\"#D63031\" fill-opacity=\"0.7\" stroke=\"#FF4757\" stroke-width=\"2.5\" />\n        <ellipse cx=\"258\" cy=\"237\" rx=\"22\" ry=\"16\" fill=\"#D63031\" fill-opacity=\"0.7\" stroke=\"#FF4757\" stroke-width=\"2.5\" />\n\n        <!-- Glowing Red Heart at Antares (316, 133) -->\n        <circle cx=\"316\" cy=\"133\" r=\"16\" fill=\"#FF0000\" fill-opacity=\"0.5\" filter=\"drop-shadow(0 0 14px #FF0000)\" />\n        <circle cx=\"316\" cy=\"133\" r=\"6\" fill=\"#FFFFFF\" />\n\n        <!-- Walking Legs (4 pairs) -->\n        <path d=\"M 330 115 Q 360 80 370 100\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" fill=\"none\" />\n        <path d=\"M 310 115 Q 330 60 345 85\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" fill=\"none\" />\n        <path d=\"M 290 150 Q 300 90 320 120\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" fill=\"none\" />\n        <path d=\"M 270 180 Q 280 120 300 150\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" fill=\"none\" />\n\n        <!-- J-Curve Segmented Tail curving to Stinger (139, 274) -->\n        <path d=\"M 258 237 C 270 340, 230 400, 128 352 C 80 320, 100 260, 139 274\" \n              fill=\"none\" stroke=\"#D63031\" stroke-width=\"16\" stroke-linecap=\"round\" filter=\"drop-shadow(0 0 10px rgba(214, 48, 49, 0.5))\" />\n        <path d=\"M 258 237 C 270 340, 230 400, 128 352 C 80 320, 100 260, 139 274\" \n              fill=\"none\" stroke=\"#FF7675\" stroke-width=\"8\" stroke-linecap=\"round\" />\n\n        <!-- Venom Bulb & Stinger Needle at Shaula & Lesath (139, 274 / 147, 276) -->\n        <circle cx=\"139\" cy=\"274\" r=\"14\" fill=\"#D63031\" stroke=\"#FF4757\" stroke-width=\"2.5\" />\n        <!-- Sharp Curved Needle Tip with Glowing Cyan Poison -->\n        <path d=\"M 139 265 Q 165 240 170 225\" stroke=\"#00F0FF\" stroke-width=\"5\" stroke-linecap=\"round\" fill=\"none\" filter=\"drop-shadow(0 0 10px #00F0FF)\" />\n        <circle cx=\"170\" cy=\"225\" r=\"4\" fill=\"#FFFFFF\" />\n      </g>"
  },
  {
    "id": "sagittarius",
    "thaiName": "กลุ่มดาวคนยิงธนู",
    "zodiacName": "ราศีธนู (Sagittarius)",
    "latinName": "Sagittarius",
    "symbol": "♐",
    "correctAnswer": "คนยิงธนู",
    "options": [
      {
        "text": "คนยิงธนู",
        "icon": "🏹",
        "correct": true
      },
      {
        "text": "ปราสาทเจ้าหญิง",
        "icon": "🏰",
        "correct": false
      },
      {
        "text": "นกอินทรี",
        "icon": "🦅",
        "correct": false
      },
      {
        "text": "รถไฟเหาะ",
        "icon": "🎢",
        "correct": false
      }
    ],
    "hint": "มีเซนทอร์ครึ่งคนครึ่งม้ากำลังง้างคันธนูเล็งไปทางทิศตะวันตก มีทั้งคันธนู หัวธนู ผ้าคลุมไหล่ และขาม้า 4 ข้างครบถ้วน!",
    "funFact": "ใจกลางทางช้างเผือก (Milky Way Galaxy) อันเป็นที่ตั้งของหลุมดำยักษ์มวลมหาศาล Sagittarius A* อยู่ตรงกลุ่มดาวนี้พอดี!",
    "starGuide": "ดาวปลายลูกศรคือ อัลนาสล์ (Alnasl) อยู่ทางขวา เล็งคันธนูไปทางศูนย์กลางทางช้างเผือก",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 426,
        "y": 211,
        "r": 8,
        "name": "อัลนาสล์ (Alnasl - γ2 Sgr ปลายลูกศร)",
        "bayer": "γ2 Sgr",
        "mag": 2.98,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 2,
        "x": 383,
        "y": 198,
        "r": 8,
        "name": "เคาส์ มีเดีย (Kaus Media - δ Sgr กลางคันธนู)",
        "bayer": "δ Sgr",
        "mag": 2.72,
        "spect": "K3 III (ดาวยักษ์ส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 3,
        "x": 358,
        "y": 143,
        "r": 8,
        "name": "เคาส์ โบเรียลิส (Kaus Borealis - λ Sgr ปลายคันธนูบน)",
        "bayer": "λ Sgr",
        "mag": 2.82,
        "spect": "K1 III (ดาวยักษ์ส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 4,
        "x": 377,
        "y": 277,
        "r": 9.5,
        "name": "เคาส์ ออสตราลิส (Kaus Australis - ε Sgr ปลายคันธนูล่าง)",
        "bayer": "ε Sgr",
        "mag": 1.79,
        "spect": "B9.5 III (ดาวยักษ์ฟ้าขาว สว่างสุด)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 5,
        "x": 295,
        "y": 165,
        "r": 7.5,
        "name": "ฟาย ซากิตตารี (φ Sgr ไหล่/อกคน)",
        "bayer": "φ Sgr",
        "mag": 3.17,
        "spect": "B8.5 III (ดาวยักษ์ฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 6,
        "x": 253,
        "y": 154,
        "r": 9,
        "name": "นูนาคี (Nunki - σ Sgr หลัง/สายธนู)",
        "bayer": "σ Sgr",
        "mag": 2.05,
        "spect": "B2.5 V (ดาวฟ้าขาว)",
        "bright": true,
        "color": "#00F0FF"
      },
      {
        "id": 7,
        "x": 240,
        "y": 230,
        "r": 8,
        "name": "อัสเซลลา (Ascella - ζ Sgr ลำตัวม้า/ท้อง)",
        "bayer": "ζ Sgr",
        "mag": 2.6,
        "spect": "A2.5 Va (ดาวคู่ขาว)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 8,
        "x": 221,
        "y": 182,
        "r": 6.5,
        "name": "เทา ซากิตตารี (τ Sgr สะโพกม้าบน)",
        "bayer": "τ Sgr",
        "mag": 3.32,
        "spect": "K1 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 9,
        "x": 238,
        "y": 64,
        "r": 7.5,
        "name": "อัลบัลดาห์ (Albaldah - π Sgr ศีรษะคนยิงธนู)",
        "bayer": "π Sgr",
        "mag": 2.88,
        "spect": "F2 II (ดาวยักษ์สว่างเหลืองขาว)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 10,
        "x": 185,
        "y": 92,
        "r": 6.5,
        "name": "ซี2 ซากิตตารี (ξ2 Sgr ผ้าคลุมไหล่)",
        "bayer": "ξ2 Sgr",
        "mag": 3.52,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 11,
        "x": 127,
        "y": 199,
        "r": 6,
        "name": "52 ซากิตตารี (52 Sgr บั้นท้ายม้า)",
        "bayer": "52 Sgr",
        "mag": 4.59,
        "spect": "B8 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 12,
        "x": 134,
        "y": 346,
        "r": 6.5,
        "name": "รุคบัต (Rukbat - α Sgr ขาหลังม้า)",
        "bayer": "α Sgr",
        "mag": 3.96,
        "spect": "B8 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 13,
        "x": 202,
        "y": 367,
        "r": 6.5,
        "name": "อาร์คับ (Arkab - β Sgr กีบเท้าหลังม้า)",
        "bayer": "β Sgr",
        "mag": 3.96,
        "spect": "B9 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 14,
        "x": 400,
        "y": 317,
        "r": 7,
        "name": "อีตา ซากิตตารี (η Sgr ขาหน้าม้า)",
        "bayer": "η Sgr",
        "mag": 3.1,
        "spect": "M3.5 III (ดาวยักษ์แดง)",
        "bright": false,
        "color": "#FF7675"
      }
    ],
    "lines": [
      [
        1,
        2
      ],
      [
        3,
        2
      ],
      [
        2,
        4
      ],
      [
        1,
        4
      ],
      [
        3,
        5
      ],
      [
        5,
        2
      ],
      [
        5,
        6
      ],
      [
        6,
        8
      ],
      [
        8,
        7
      ],
      [
        7,
        4
      ],
      [
        7,
        5
      ],
      [
        6,
        9
      ],
      [
        9,
        10
      ],
      [
        8,
        11
      ],
      [
        11,
        12
      ],
      [
        12,
        13
      ],
      [
        4,
        14
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Recurve Bow (Aiming West / Right) -->\n        <path d=\"M 370 115 Q 405 195 380 275\" stroke=\"#FFD700\" stroke-width=\"8\" stroke-linecap=\"round\" fill=\"none\" filter=\"drop-shadow(0 0 12px #FFD700)\" />\n        <path d=\"M 370 115 Q 405 195 380 275\" stroke=\"#FFA502\" stroke-width=\"4\" stroke-linecap=\"round\" fill=\"none\" />\n        <!-- Bowstring pulled back to Nunki (250, 150) -->\n        <line x1=\"370\" y1=\"115\" x2=\"250\" y2=\"150\" stroke=\"#FFFFFF\" stroke-width=\"2\" stroke-opacity=\"0.8\" />\n        <line x1=\"380\" y1=\"275\" x2=\"250\" y2=\"150\" stroke=\"#FFFFFF\" stroke-width=\"2\" stroke-opacity=\"0.8\" />\n        <!-- Golden Arrow -->\n        <line x1=\"445\" y1=\"215\" x2=\"250\" y2=\"150\" stroke=\"#FFD700\" stroke-width=\"4\" stroke-linecap=\"round\" filter=\"drop-shadow(0 0 8px #FFD700)\" />\n        <polygon points=\"445,215 425,205 425,225\" fill=\"#FFD700\" />\n\n        <!-- Centaur Human Torso & Head (at Albaldah 220, 65) -->\n        <circle cx=\"220\" cy=\"65\" r=\"20\" fill=\"#FFEAA7\" fill-opacity=\"0.8\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <!-- Archer Helmet / Headband -->\n        <path d=\"M 205 55 Q 220 40 235 55\" stroke=\"#FFD700\" stroke-width=\"4\" fill=\"none\" />\n        <!-- Archer Eye & Face -->\n        <circle cx=\"230\" cy=\"62\" r=\"2.5\" fill=\"#060919\" />\n        <!-- Muscular Torso -->\n        <path d=\"M 220 85 L 295 165 L 240 230 L 180 180 Z\" fill=\"#E17055\" fill-opacity=\"0.6\" stroke=\"#D63031\" stroke-width=\"2\" />\n        <!-- Flowing Royal Cape -->\n        <path d=\"M 220 65 Q 150 40 130 95 Q 170 85 240 150 Z\" fill=\"#70A1FF\" fill-opacity=\"0.6\" stroke=\"#1E90FF\" stroke-width=\"2\" filter=\"drop-shadow(0 0 8px #1E90FF)\" />\n\n        <!-- Horse Equine Body (Galloping to the right) -->\n        <path d=\"M 180 180 Q 140 190 115 205 Q 120 280 170 350 L 235 360 Q 230 280 240 230 Z\" \n              fill=\"#FFA502\" fill-opacity=\"0.45\" stroke=\"#FF7F50\" stroke-width=\"3\" />\n        \n        <!-- Horse Hind Legs & Hooves (Rukbat 170, 350 & Arkab 235, 360) -->\n        <path d=\"M 150 240 L 170 350 L 185 350\" stroke=\"#FFA502\" stroke-width=\"8\" stroke-linecap=\"round\" />\n        <rect x=\"165\" y=\"345\" width=\"20\" height=\"12\" rx=\"3\" fill=\"#FFD700\" />\n\n        <path d=\"M 200 240 L 235 360 L 250 360\" stroke=\"#FFA502\" stroke-width=\"8\" stroke-linecap=\"round\" />\n        <rect x=\"230\" y=\"355\" width=\"20\" height=\"12\" rx=\"3\" fill=\"#FFD700\" />\n\n        <!-- Horse Front Legs & Hooves (Eta Sgr 340, 335 & Theta Sgr 380, 365) -->\n        <path d=\"M 260 220 L 340 335 L 380 365\" stroke=\"#FFA502\" stroke-width=\"8\" stroke-linecap=\"round\" />\n        <rect x=\"375\" y=\"360\" width=\"20\" height=\"12\" rx=\"3\" fill=\"#FFD700\" />\n\n        <!-- Horse Tail -->\n        <path d=\"M 115 205 Q 80 230 75 280\" stroke=\"#FFEAA7\" stroke-width=\"6\" stroke-linecap=\"round\" fill=\"none\" />\n      </g>"
  },
  {
    "id": "capricorn",
    "thaiName": "กลุ่มดาวมกร (แพะทะเล)",
    "zodiacName": "ราศีมังกร (Capricornus)",
    "latinName": "Capricornus",
    "symbol": "♑",
    "correctAnswer": "แพะทะเล",
    "options": [
      {
        "text": "แพะทะเล",
        "icon": "🐐",
        "correct": true
      },
      {
        "text": "หมวกโจรสลัด",
        "icon": "🏴‍☠️",
        "correct": false
      },
      {
        "text": "พิซซ่า",
        "icon": "🍕",
        "correct": false
      },
      {
        "text": "กางเกงใน",
        "icon": "🩲",
        "correct": false
      }
    ],
    "hint": "มีรูปสามเหลี่ยมโค้งขนาดใหญ่ คล้ายรูปทรงเรือหรือแพะวิเศษที่มีหางปลาแหวกว่ายน้ำ!",
    "funFact": "ในตำนาน เทพแพะแพนโดดหนีสัตว์ประหลาดไทฟอนลงแม่น้ำไนล์ ร่างกายครึ่งล่างจึงกลายเป็นหางปลา!",
    "starGuide": "ดาวหัวแพะคู่คือ อัลเจดี และ ดาบิห์ ทางทิศตะวันตก",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 45,
        "y": 130,
        "r": 7.5,
        "name": "เดเนบ อัลเจดี (Deneb Algedi - δ Cap หางปลา)",
        "bayer": "δ Cap",
        "mag": 2.85,
        "spect": "A7m III (ดาวยักษ์ขาว สว่างสุด)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 2,
        "x": 441,
        "y": 104,
        "r": 7.5,
        "name": "ดาบิห์ (Dabih - β Cap เขาแพะ)",
        "bayer": "β Cap",
        "mag": 3.05,
        "spect": "F8 V (ดาวระบบหลายดวง)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 3,
        "x": 455,
        "y": 60,
        "r": 6.5,
        "name": "อัลเจดี (Algedi - α2 Cap เขาแพะบน)",
        "bayer": "α2 Cap",
        "mag": 3.58,
        "spect": "G8.5 III (ดาวยักษ์เหลือง)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 4,
        "x": 77,
        "y": 140,
        "r": 6.5,
        "name": "นาชิรา (Nashira - γ Cap ครีบหาง)",
        "bayer": "γ Cap",
        "mag": 3.69,
        "spect": "A7m III-IV (ดาวย่อยยักษ์ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 5,
        "x": 139,
        "y": 252,
        "r": 6.5,
        "name": "เซตา แคปริคอร์นิ (ζ Cap ท้องปลาล่าง)",
        "bayer": "ζ Cap",
        "mag": 3.77,
        "spect": "G4 Ib (ดาวยักษ์ใหญ่เหลือง)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 6,
        "x": 234,
        "y": 151,
        "r": 5.5,
        "name": "ทีตา แคปริคอร์นิ (θ Cap สันหลังกลาง)",
        "bayer": "θ Cap",
        "mag": 4.08,
        "spect": "A1 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 7,
        "x": 299,
        "y": 340,
        "r": 5.5,
        "name": "โอเมกา แคปริคอร์นิ (ω Cap ก้นสามเหลี่ยม)",
        "bayer": "ω Cap",
        "mag": 4.12,
        "spect": "K4 III (ดาวยักษ์ส้มแดง)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 8,
        "x": 326,
        "y": 308,
        "r": 5.5,
        "name": "ไซ แคปริคอร์นิ (ψ Cap ท้องล่างหน้า)",
        "bayer": "ψ Cap",
        "mag": 4.13,
        "spect": "F5 V (ดาวเหลืองขาว)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 9,
        "x": 159,
        "y": 144,
        "r": 5.5,
        "name": "ไอโอตา แคปริคอร์นิ (ι Cap หลัง)",
        "bayer": "ι Cap",
        "mag": 4.28,
        "spect": "G8 III (ดาวยักษ์เหลือง)",
        "bright": false,
        "color": "#FFD27D"
      }
    ],
    "lines": [
      [
        3,
        2
      ],
      [
        2,
        8
      ],
      [
        8,
        7
      ],
      [
        7,
        5
      ],
      [
        4,
        1
      ],
      [
        2,
        6
      ],
      [
        6,
        9
      ],
      [
        9,
        4
      ],
      [
        1,
        5
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Goat Head (at Algedi & Dabih 441, 104) -->\n        <circle cx=\"435\" cy=\"115\" r=\"26\" fill=\"#FFEAA7\" fill-opacity=\"0.8\" stroke=\"#F1C40F\" stroke-width=\"2.5\" />\n        <!-- Big Curved Goat Horns -->\n        <path d=\"M 445 95 Q 470 50 490 70 Q 460 75 440 90\" fill=\"#FFD700\" stroke=\"#FFA502\" stroke-width=\"2.5\" filter=\"drop-shadow(0 0 8px #FFD700)\" />\n        <path d=\"M 430 95 Q 445 40 465 55 Q 440 65 425 90\" fill=\"#FFD700\" stroke=\"#FFA502\" stroke-width=\"2\" />\n        <!-- Goat Eye & Beard -->\n        <circle cx=\"445\" cy=\"112\" r=\"3\" fill=\"#060919\" />\n        <path d=\"M 450 135 Q 465 155 450 160\" stroke=\"#FFEAA7\" stroke-width=\"4\" stroke-linecap=\"round\" fill=\"none\" />\n\n        <!-- Goat Front Legs & Hooves -->\n        <path d=\"M 400 160 L 420 230 L 435 230\" stroke=\"#FFEAA7\" stroke-width=\"7\" stroke-linecap=\"round\" />\n        <rect x=\"420\" y=\"225\" width=\"16\" height=\"10\" rx=\"3\" fill=\"#FFD700\" />\n        <path d=\"M 370 170 L 380 240 L 395 240\" stroke=\"#FFEAA7\" stroke-width=\"7\" stroke-linecap=\"round\" />\n        <rect x=\"380\" y=\"235\" width=\"16\" height=\"10\" rx=\"3\" fill=\"#FFD700\" />\n\n        <!-- Sea-Goat Hull & Curved Fish Tail (from 348, 340 curving up to Deneb Algedi 45, 130) -->\n        <path d=\"M 410 140 Q 360 220 300 330 Q 200 340 140 252 Q 90 200 45 130 Q 110 130 160 144 Q 260 150 350 140 Z\" \n              fill=\"#1DD1A1\" fill-opacity=\"0.45\" stroke=\"#10AC84\" stroke-width=\"3\" filter=\"drop-shadow(0 0 12px rgba(29, 209, 161, 0.4))\" />\n        \n        <!-- Fish Scales Texture -->\n        <path d=\"M 280 270 Q 260 250 240 270 M 240 250 Q 220 230 200 250 M 190 220 Q 170 200 150 220\" \n              stroke=\"#FFFFFF\" stroke-width=\"2\" fill=\"none\" opacity=\"0.6\" />\n\n        <!-- Wide Spreading Fish Tail Fin at Deneb Algedi (45, 130) & Nashira (77, 140) -->\n        <path d=\"M 45 130 Q 10 90 20 60 Q 45 110 50 130 Q 35 150 15 180 Q 35 150 77 140 Z\" \n              fill=\"#1DD1A1\" fill-opacity=\"0.8\" stroke=\"#10AC84\" stroke-width=\"2.5\" filter=\"drop-shadow(0 0 10px #1DD1A1)\" />\n      </g>"
  },
  {
    "id": "aquarius",
    "thaiName": "กลุ่มดาวคนแบกหม้อน้ำ",
    "zodiacName": "ราศีกุมภ์ (Aquarius)",
    "latinName": "Aquarius",
    "symbol": "♒",
    "correctAnswer": "คนเทน้ำจากเหยือก",
    "options": [
      {
        "text": "คนเทน้ำจากเหยือก",
        "icon": "🏺",
        "correct": true
      },
      {
        "text": "จรวด",
        "icon": "🚀",
        "correct": false
      },
      {
        "text": "พัดลม",
        "icon": "🪭",
        "correct": false
      },
      {
        "text": "แมวกำลังนอน",
        "icon": "🐱",
        "correct": false
      }
    ],
    "hint": "มีรูปคนยกแขนถือเหยือกน้ำรูปตัว 'Y' บนบ่า และเทสายน้ำทอดคดเคี้ยวลงมาเกิดเป็นแอ่งน้ำกระเซ็นอยู่ด้านล่าง!",
    "funFact": "น้ำที่เทลงมาจากเหยือกคือสายน้ำแห่งชีวิตในตำนาน ไหลลงสู่ปากปลาในกลุ่มดาวปลาทางใต้ (Piscis Austrinus)!",
    "starGuide": "มองหาดาว 'ซาดาลซูด' (Sadalsuud) และ 'ซาดาลเมลิก' (Sadalmelik) ตรงหัวไหล่คนเทน้ำ และสายน้ำที่ไหลลงด้านล่าง",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 316,
        "y": 374,
        "r": 6.5,
        "name": "98 แอควารี (b2 Aqr)",
        "bayer": "b2 Aqr",
        "mag": 3.97,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 2,
        "x": 375,
        "y": 78,
        "r": 8.5,
        "name": "ซาดาลซูด (Sadalsuud - β Aqr)",
        "bayer": "β Aqr",
        "mag": 2.9,
        "spect": "G0 Ib (ดาวยักษ์ใหญ่เหลือง สว่างสุด)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 3,
        "x": 285,
        "y": 100,
        "r": 8.5,
        "name": "ซาดาลเมลิก (Sadalmelik - α Aqr)",
        "bayer": "α Aqr",
        "mag": 2.95,
        "spect": "G2 Ib (ดาวยักษ์ใหญ่เหลือง)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 4,
        "x": 262,
        "y": 136,
        "r": 6.5,
        "name": "ซาดาคเบีย (Sadachbia - γ Aqr)",
        "bayer": "γ Aqr",
        "mag": 3.86,
        "spect": "A0 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 5,
        "x": 227,
        "y": 137,
        "r": 6.5,
        "name": "เซตา แอควารี (ζ Aqr)",
        "bayer": "ζ Aqr",
        "mag": 3.65,
        "spect": "F2 IV (ดาวคู่ขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 6,
        "x": 212,
        "y": 162,
        "r": 6,
        "name": "อีตา แอควารี (η Aqr)",
        "bayer": "η Aqr",
        "mag": 4.04,
        "spect": "B9 IV-Vn (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      },
      {
        "id": 8,
        "x": 325,
        "y": 173,
        "r": 6.5,
        "name": "อันชา (Ancha - θ Aqr)",
        "bayer": "θ Aqr",
        "mag": 4.17,
        "spect": "G8 III-IV (ดาวย่อยยักษ์เหลือง)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 9,
        "x": 454,
        "y": 48,
        "r": 6.5,
        "name": "อัลบาลิ (Albali - ε Aqr)",
        "bayer": "ε Aqr",
        "mag": 3.78,
        "spect": "A1.5 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 10,
        "x": 244,
        "y": 239,
        "r": 7,
        "name": "ไฮดอร์ (Hydor - λ Aqr)",
        "bayer": "λ Aqr",
        "mag": 3.73,
        "spect": "M2.5 IIIa (ดาวยักษ์แดง)",
        "bright": false,
        "color": "#FF7675"
      },
      {
        "id": 11,
        "x": 323,
        "y": 220,
        "r": 6,
        "name": "เทา2 แอควารี (τ2 Aqr)",
        "bayer": "τ2 Aqr",
        "mag": 4.01,
        "spect": "M0 III (ดาวยักษ์แดงส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 12,
        "x": 322,
        "y": 287,
        "r": 7.5,
        "name": "สแคต (Skat - δ Aqr)",
        "bayer": "δ Aqr",
        "mag": 3.27,
        "spect": "A3 V (ดาวแคระขาว)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 13,
        "x": 344,
        "y": 345,
        "r": 7,
        "name": "88 แอควารี (c2 Aqr)",
        "bayer": "c2 Aqr",
        "mag": 3.68,
        "spect": "K1 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 14,
        "x": 239,
        "y": 298,
        "r": 5.5,
        "name": "ไซ1 แอควารี (ψ1 Aqr)",
        "bayer": "ψ1 Aqr",
        "mag": 4.21,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 16,
        "x": 395,
        "y": 198,
        "r": 6,
        "name": "ไอโอตา แอควารี (ι Aqr)",
        "bayer": "ι Aqr",
        "mag": 4.29,
        "spect": "B9 V (ดาวฟ้าขาว)",
        "bright": false,
        "color": "#00F0FF"
      }
    ],
    "lines": [
      [
        9,
        2
      ],
      [
        2,
        3
      ],
      [
        4,
        3
      ],
      [
        4,
        5
      ],
      [
        6,
        5
      ],
      [
        6,
        10
      ],
      [
        14,
        10
      ],
      [
        14,
        1
      ],
      [
        3,
        8
      ],
      [
        16,
        8
      ],
      [
        11,
        8
      ],
      [
        11,
        12
      ],
      [
        12,
        13
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Youthful Water Bearer (Ganymede) Kneeling Profile -->\n        <circle cx=\"340\" cy=\"80\" r=\"22\" fill=\"#FFEAA7\" fill-opacity=\"0.8\" stroke=\"#F1C40F\" stroke-width=\"2\" />\n        <!-- Headband & Hair -->\n        <path d=\"M 320 70 Q 340 55 360 70\" stroke=\"#F1C40F\" stroke-width=\"4\" fill=\"none\" />\n        <circle cx=\"348\" cy=\"78\" r=\"3\" fill=\"#060919\" />\n\n        <!-- Raised Right Arm reaching high to 98 Aqr (430, 55) -->\n        <path d=\"M 340 80 L 430 55\" stroke=\"#FFEAA7\" stroke-width=\"8\" stroke-linecap=\"round\" />\n        <circle cx=\"430\" cy=\"55\" r=\"6\" fill=\"#FFD700\" />\n\n        <!-- Torso & Grecian Tunic -->\n        <polygon points=\"335,125 245,175 265,270 385,205\" fill=\"#70A1FF\" fill-opacity=\"0.5\" stroke=\"#1E90FF\" stroke-width=\"2\" />\n        \n        <!-- Kneeling Legs -->\n        <path d=\"M 265 270 L 220 335 L 235 380\" stroke=\"#FFEAA7\" stroke-width=\"8\" stroke-linecap=\"round\" />\n        <path d=\"M 265 270 L 320 350\" stroke=\"#FFEAA7\" stroke-width=\"8\" stroke-linecap=\"round\" />\n\n        <!-- Large Classical Amphora / Water Urn at (175, 180) -->\n        <ellipse cx=\"180\" cy=\"180\" rx=\"26\" ry=\"36\" transform=\"rotate(-35 180 180)\" fill=\"#E17055\" fill-opacity=\"0.8\" stroke=\"#D63031\" stroke-width=\"3\" filter=\"drop-shadow(0 0 10px #E17055)\" />\n        <ellipse cx=\"160\" cy=\"165\" rx=\"14\" ry=\"8\" transform=\"rotate(-35 160 165)\" fill=\"#2D3436\" stroke=\"#FFD700\" stroke-width=\"2\" />\n        <!-- Urn Handle -->\n        <path d=\"M 195 160 Q 220 180 190 205\" stroke=\"#D63031\" stroke-width=\"4\" fill=\"none\" />\n\n        <!-- Cascading Luminous Ribbons of Flowing Water (175, 180 -> 235, 380) -->\n        <path d=\"M 155 165 C 130 220, 140 260, 155 260 C 170 290, 175 320, 185 320 C 205 345, 215 360, 235 380\" \n              fill=\"none\" stroke=\"#00F0FF\" stroke-width=\"12\" stroke-linecap=\"round\" opacity=\"0.8\" filter=\"drop-shadow(0 0 14px #00F0FF)\" />\n        <path d=\"M 155 165 C 130 220, 140 260, 155 260 C 170 290, 175 320, 185 320 C 205 345, 215 360, 235 380\" \n              fill=\"none\" stroke=\"#FFFFFF\" stroke-width=\"4\" stroke-linecap=\"round\" opacity=\"0.9\" />\n\n        <!-- Sparkling Pool Splash at Bottom (88 Aqr 235, 380) -->\n        <ellipse cx=\"235\" cy=\"380\" rx=\"55\" ry=\"16\" fill=\"#00F0FF\" fill-opacity=\"0.4\" stroke=\"#00F0FF\" stroke-width=\"2.5\" filter=\"drop-shadow(0 0 14px #00F0FF)\" />\n        <circle cx=\"200\" cy=\"395\" r=\"6\" fill=\"#FFFFFF\" filter=\"drop-shadow(0 0 6px #00F0FF)\" />\n        <circle cx=\"270\" cy=\"390\" r=\"6\" fill=\"#FFFFFF\" filter=\"drop-shadow(0 0 6px #00F0FF)\" />\n        <circle cx=\"235\" cy=\"360\" r=\"4\" fill=\"#00F0FF\" />\n        <circle cx=\"250\" cy=\"350\" r=\"3\" fill=\"#FFFFFF\" />\n      </g>"
  },
  {
    "id": "pisces",
    "thaiName": "กลุ่มดาวปลาคู่",
    "zodiacName": "ราศีมีน (Pisces)",
    "latinName": "Pisces",
    "symbol": "♓",
    "correctAnswer": "ปลาคู่",
    "options": [
      {
        "text": "ปลาคู่",
        "icon": "🐟",
        "correct": true
      },
      {
        "text": "แว่นขยาย",
        "icon": "🔍",
        "correct": false
      },
      {
        "text": "กรรไกร",
        "icon": "✂️",
        "correct": false
      },
      {
        "text": "ผึ้ง",
        "icon": "🐝",
        "correct": false
      }
    ],
    "hint": "มีปลาสองตัว ตัวหนึ่งว่ายขึ้นสู่ทิศเหนือ อีกตัวว่ายไปทางทิศตะวันตก โดยหางของทั้งสองผูกริบบิ้นเชื่อมติดกันที่ดาวอัลริชา!",
    "funFact": "ปลาสองตัวนี้คือ เทพีอโฟรไดต์กับบุตรชายคิวปิด แปลงร่างเป็นปลาแล้วผูกริบบิ้นไว้ด้วยกันเพื่อไม่ให้พลัดหลงในสายน้ำ!",
    "starGuide": "ดาวตรงปมริบบิ้นเชื่อมปลาทั้งสองตัวคือ 'อัลริชา' (Alrescha) อยู่ที่จุดล่างสุดรูปตัว V",
    "viewBox": "0 0 500 400",
    "stars": [
      {
        "id": 1,
        "x": 238,
        "y": 262,
        "r": 8.5,
        "name": "อัลเฟิร์ก (Alpherg - η Psc)",
        "bayer": "η Psc",
        "mag": 3.62,
        "spect": "G7 IIIa (ดาวยักษ์เหลือง สว่างสุด)",
        "bright": true,
        "color": "#FFD27D"
      },
      {
        "id": 3,
        "x": 171,
        "y": 218,
        "r": 6.5,
        "name": "ฟาย พิสเซียม (φ Psc หลังปลาเหนือ)",
        "bayer": "φ Psc",
        "mag": 4.65,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 4,
        "x": 123,
        "y": 216,
        "r": 7,
        "name": "อิปซิลอน พิสเซียม (υ Psc โคนหางปลาเหนือ)",
        "bayer": "υ Psc",
        "mag": 4.74,
        "spect": "A3 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 7,
        "x": 431,
        "y": 40,
        "r": 7.5,
        "name": "แกมมา พิสเซียม (γ Psc หน้าผากปลา)",
        "bayer": "γ Psc",
        "mag": 3.7,
        "spect": "G8 III (ดาวยักษ์เหลืองส้ม)",
        "bright": true,
        "color": "#FFA502"
      },
      {
        "id": 8,
        "x": 383,
        "y": 64,
        "r": 6.5,
        "name": "ทีตา พิสเซียม (θ Psc สันหลังปลา)",
        "bayer": "θ Psc",
        "mag": 4.27,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 9,
        "x": 392,
        "y": 107,
        "r": 6.5,
        "name": "ไอโอตา พิสเซียม (ι Psc โคนหางปลา)",
        "bayer": "ι Psc",
        "mag": 4.13,
        "spect": "F7 V (ดาวเหลืองขาว)",
        "bright": false,
        "color": "#FFD27D"
      },
      {
        "id": 11,
        "x": 438,
        "y": 112,
        "r": 6.5,
        "name": "แลมบ์ดา พิสเซียม (λ Psc ท้องปลา)",
        "bayer": "λ Psc",
        "mag": 4.49,
        "spect": "A7 V (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 12,
        "x": 454,
        "y": 72,
        "r": 6.5,
        "name": "แคปปา พิสเซียม (κ Psc คางปลา)",
        "bayer": "κ Psc",
        "mag": 4.95,
        "spect": "A0p (ดาวแคระขาว)",
        "bright": false,
        "color": "#FFFFFF"
      },
      {
        "id": 13,
        "x": 316,
        "y": 322,
        "r": 6,
        "name": "โอไมครอน พิสเซียม (ο Psc สายริบบิ้นเหนือ 1)",
        "bayer": "ο Psc",
        "mag": 4.26,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 14,
        "x": 362,
        "y": 318,
        "r": 6,
        "name": "นิว พิสเซียม (ν Psc สายริบบิ้นเหนือ 2)",
        "bayer": "ν Psc",
        "mag": 4.45,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 15,
        "x": 361,
        "y": 287,
        "r": 6,
        "name": "มิว พิสเซียม (μ Psc สายริบบิ้นเหนือ 3)",
        "bayer": "μ Psc",
        "mag": 4.84,
        "spect": "K4 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 16,
        "x": 382,
        "y": 350,
        "r": 6,
        "name": "ไซ พิสเซียม (ξ Psc สายริบบิ้นเหนือ 4)",
        "bayer": "ξ Psc",
        "mag": 4.61,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 17,
        "x": 383,
        "y": 374,
        "r": 9,
        "name": "อัลริชา (Alrescha - α Psc ปมผูกริบบิ้น)",
        "bayer": "α Psc",
        "mag": 3.82,
        "spect": "A0p (ดาวคู่ขาว ปมริบบิ้น)",
        "bright": true,
        "color": "#FFFFFF"
      },
      {
        "id": 18,
        "x": 381,
        "y": 168,
        "r": 6,
        "name": "เดลตา พิสเซียม (δ Psc สายริบบิ้นตะวันตก 1)",
        "bayer": "δ Psc",
        "mag": 4.44,
        "spect": "K5 III (ดาวยักษ์ส้มแดง)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 19,
        "x": 359,
        "y": 222,
        "r": 6,
        "name": "เอปซิลอน พิสเซียม (ε Psc สายริบบิ้นตะวันตก 2)",
        "bayer": "ε Psc",
        "mag": 4.27,
        "spect": "K0 III (ดาวยักษ์ส้ม)",
        "bright": false,
        "color": "#FFA502"
      },
      {
        "id": 21,
        "x": 101,
        "y": 159,
        "r": 7,
        "name": "ซิกมา พิสเซียม",
        "bayer": "σ Psc",
        "mag": 5.5,
        "spect": "V",
        "bright": false,
        "color": "#00F0FF"
      }
    ],
    "lines": [
      [
        7,
        8
      ],
      [
        7,
        12
      ],
      [
        12,
        11
      ],
      [
        9,
        11
      ],
      [
        9,
        8
      ],
      [
        9,
        18
      ],
      [
        18,
        19
      ],
      [
        19,
        15
      ],
      [
        14,
        15
      ],
      [
        14,
        16
      ],
      [
        17,
        16
      ],
      [
        17,
        13
      ],
      [
        1,
        13
      ],
      [
        1,
        3
      ],
      [
        21,
        3
      ],
      [
        21,
        4
      ],
      [
        3,
        4
      ]
    ],
    "artOverlay": "<g class=\"overlay-graphic\" opacity=\"0.95\">\n        <!-- Northern Celestial Fish (Swimming North/Up at 405, 65) -->\n        <g stroke=\"#55EFC4\" stroke-width=\"2.5\" fill=\"none\">\n          <ellipse cx=\"405\" cy=\"110\" rx=\"45\" ry=\"24\" transform=\"rotate(75 405 110)\" fill=\"#55EFC4\" fill-opacity=\"0.5\" stroke=\"#1DD1A1\" stroke-width=\"3\" filter=\"drop-shadow(0 0 12px #1DD1A1)\" />\n          <!-- Fish Head & Mouth -->\n          <polygon points=\"405,65 388,40 422,40\" fill=\"#1DD1A1\" opacity=\"0.85\" />\n          <!-- Eye -->\n          <circle cx=\"405\" cy=\"72\" r=\"4\" fill=\"#060919\" /><circle cx=\"406\" cy=\"70\" r=\"1.5\" fill=\"#FFFFFF\" />\n          <!-- Gills & Scales -->\n          <path d=\"M 390 95 Q 405 105 420 95\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" opacity=\"0.7\" />\n          <path d=\"M 390 115 Q 405 125 420 115\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" opacity=\"0.7\" />\n          <!-- Side Fins -->\n          <path d=\"M 380 95 Q 355 105 375 125 Z\" fill=\"#1DD1A1\" opacity=\"0.7\" />\n          <path d=\"M 430 95 Q 455 105 435 125 Z\" fill=\"#1DD1A1\" opacity=\"0.7\" />\n          <!-- Tail Fin at Upsilon Psc (430, 155) -->\n          <path d=\"M 405 150 Q 375 185 390 195 Q 405 170 420 195 Q 435 185 405 150 Z\" fill=\"#1DD1A1\" fill-opacity=\"0.8\" stroke=\"#1DD1A1\" stroke-width=\"2\" />\n        </g>\n\n        <!-- Western Celestial Fish (Swimming West/Left at 125, 240) -->\n        <g stroke=\"#FF6B81\" stroke-width=\"2.5\" fill=\"none\">\n          <ellipse cx=\"190\" cy=\"250\" rx=\"60\" ry=\"28\" fill=\"#FF6B81\" fill-opacity=\"0.5\" stroke=\"#FF4757\" stroke-width=\"3\" filter=\"drop-shadow(0 0 12px #FF4757)\" />\n          <!-- Fish Head & Mouth (at 7 Psc 125, 240) -->\n          <polygon points=\"125,240 98,225 98,255\" fill=\"#FF4757\" opacity=\"0.85\" />\n          <!-- Eye -->\n          <circle cx=\"138\" cy=\"238\" r=\"4\" fill=\"#060919\" /><circle cx=\"139\" cy=\"236\" r=\"1.5\" fill=\"#FFFFFF\" />\n          <!-- Gills & Scales -->\n          <path d=\"M 160 235 Q 170 250 160 265\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" opacity=\"0.7\" />\n          <path d=\"M 180 235 Q 190 250 180 265\" stroke=\"#FFFFFF\" stroke-width=\"1.5\" opacity=\"0.7\" />\n          <!-- Dorsal and Ventral Fins -->\n          <path d=\"M 175 222 Q 200 200 215 225 Z\" fill=\"#FF4757\" opacity=\"0.7\" />\n          <path d=\"M 175 278 Q 200 300 215 275 Z\" fill=\"#FF4757\" opacity=\"0.7\" />\n          <!-- Tail Fin at TX Psc (260, 255) -->\n          <path d=\"M 245 250 Q 280 220 290 235 Q 265 250 290 265 Q 280 280 245 250 Z\" fill=\"#FF4757\" fill-opacity=\"0.8\" stroke=\"#FF4757\" stroke-width=\"2\" />\n        </g>\n\n        <!-- Shimmering Golden Ribbon / Cord Connecting Both Fish -->\n        <!-- North Fish Cord (405, 170 -> Alrescha 320, 385) -->\n        <path d=\"M 405 170 C 375 220, 355 265, 345 320 C 340 360, 335 375, 320 385\" \n              fill=\"none\" stroke=\"#FFD700\" stroke-width=\"5\" stroke-linecap=\"round\" opacity=\"0.85\" filter=\"drop-shadow(0 0 8px #FFD700)\" />\n        <!-- West Fish Cord (260, 255 -> Alrescha 320, 385) -->\n        <path d=\"M 260 255 C 250 300, 265 330, 290 365 C 300 375, 310 380, 320 385\" \n              fill=\"none\" stroke=\"#FFD700\" stroke-width=\"5\" stroke-linecap=\"round\" opacity=\"0.85\" filter=\"drop-shadow(0 0 8px #FFD700)\" />\n\n        <!-- Golden Tied Ribbon Knot with Shimmering Bow at Alrescha (320, 385) -->\n        <circle cx=\"320\" cy=\"385\" r=\"14\" fill=\"#FFD700\" stroke=\"#FFA502\" stroke-width=\"3\" filter=\"drop-shadow(0 0 14px #FFD700)\" />\n        <path d=\"M 320 385 Q 300 365 305 385 Q 310 395 320 385 Q 340 365 335 385 Q 330 395 320 385 Z\" fill=\"#FFA502\" stroke=\"#FFD700\" stroke-width=\"1.5\" />\n        <circle cx=\"320\" cy=\"385\" r=\"5\" fill=\"#FFFFFF\" />\n      </g>"
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CONSTELLATIONS_DATA };
}
