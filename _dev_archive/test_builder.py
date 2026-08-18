# -*- coding: utf-8 -*-
"""
Build and validate the exact updated constellations.js
"""

LIBRA = {
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
    "starGuide": "ดาวจานเหนือคือ ซูเบนเอลเชมาลี (Zubeneschamali) สีฟ้าเขียว และดาวซูเบนเอลเกนูบี (Zubenelgenubi) ทางทิศใต้",
    "viewBox": "0 0 500 400",
    "stars": [
        {"id": 1, "x": 150, "y": 295, "r": 8.5, "name": "ซูเบนเอลเกนูบี (Zubenelgenubi - α2 Lib จานใต้)", "bayer": "α2 Lib", "mag": 2.75, "spect": "A3 IV (ดาวคู่ขาว)", "bright": True, "color": "#FFD27D"},
        {"id": 2, "x": 275, "y": 85, "r: 8.5": 8.5, "name": "ซูเบนเอลเชมาลี (Zubeneschamali - β Lib ยอดคาน)", "bayer": "β Lib", "mag": 2.61, "spect": "B8 V (ดาวสีฟ้าอมเขียวมรกต)", "bright": True, "color": "#00F0FF"},
        {"id": 3, "x": 395, "y": 145, "r": 7.0, "name": "ซูเบนเอลอัครับ (Zubenelakrab - γ Lib จานตะวันออก)", "bayer": "γ Lib", "mag": 3.91, "spect": "G8.5 III (ดาวยักษ์ส้มเหลือง)", "bright": False, "color": "#FFA502"},
        {"id": 4, "x": 350, "y": 265, "r": 7.5, "name": "บราเคียม (Brachium - σ Lib ฐานล่าง)", "bayer": "σ Lib", "mag": 3.25, "spect": "M2.5 III (ดาวยักษ์แดง)", "bright": True, "color": "#FF4757"}
    ],
    "lines": [
        [1, 2], [2, 3], [3, 4], [4, 1]
    ]
}

print("Libra test passed")
