# -*- coding: utf-8 -*-
"""
Script to compute mathematically accurate celestial projections for the 12 Zodiac constellations
Using official Hipparcos / Yale Bright Star Catalog coordinates (J2000)
"""
import math
import json

# Utility to convert RA (h, m, s) and Dec (deg, m, s) to decimal degrees
def ra_deg(h, m, s=0.0):
    return (h + m/60.0 + s/3600.0) * 15.0

def dec_deg(d, m, s=0.0):
    sign = -1.0 if d < 0 else 1.0
    return sign * (abs(d) + m/60.0 + s/3600.0)

# Real astronomical data for 12 Zodiac Constellations
CONSTELLATIONS_ASTRO = {
    "aries": {
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
        "hint": "มีดาว 4 ดวงหลักเรียงเป็นเส้นโค้งแล้วหักงอลงมา คล้ายเขาโค้งของแกะตัวผู้!",
        "funFact": "กลุ่มดาวราศีแรก มีดาวฤกษ์สว่างสีส้ม 'ฮามัล' และดาว 'เชอราทาน' กับ 'เมซาร์ทิม' ที่ปลายเขาแกะ!",
        "starGuide": "สังเกตดาวสว่างสีส้ม 'ฮามัล' (Hamal) อยู่ตรงสันเขาแกะ",
        "stars": [
            {"id": 1, "name": "ฮามัล (Hamal - α Ari)", "ra": ra_deg(2, 7, 10.4), "dec": dec_deg(23, 27, 45), "mag": 2.00, "color": "#FFA502", "bright": True},
            {"id": 2, "name": "เชอราทาน (Sheratan - β Ari)", "ra": ra_deg(1, 54, 38.4), "dec": dec_deg(20, 48, 29), "mag": 2.64, "color": "#FFFFFF", "bright": True},
            {"id": 3, "name": "เมซาร์ทิม (Mesarthim - γ Ari)", "ra": ra_deg(1, 53, 31.8), "dec": dec_deg(19, 17, 38), "mag": 3.88, "color": "#FFFFFF", "bright": False},
            {"id": 4, "name": "โบเทน (Botein - δ Ari)", "ra": ra_deg(3, 11, 37.7), "dec": dec_deg(19, 43, 36), "mag": 4.35, "color": "#FFA502", "bright": False},
            {"id": 5, "name": "ภารณี (Bharani - 41 Ari)", "ra": ra_deg(2, 49, 59.0), "dec": dec_deg(27, 15, 38), "mag": 3.61, "color": "#A8DADC", "bright": False}
        ],
        "lines": [
            [4, 1], [1, 2], [2, 3], [1, 5]
        ]
    },

    "taurus": {
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
        "hint": "มองหาหน้าวัวรูปตัว 'V' (กระจุกดาวไฮยาดีส) ที่มีดาวตาสีแดงอัลเดบารัน และเขายาว 2 ข้างพุ่งไปข้างหน้า!",
        "funFact": "ตรงตาขวาของวัวคือดาวยักษ์แดง 'อัลเดบารัน' และบนโหนกหลังมีกระจุกดาวลูกไก่ 7 ดวง (Pleiades) ระยิบระยับ!",
        "starGuide": "ดาวตาสีส้มแดง 'อัลเดบารัน' สว่างเด่นที่สุดในกระจุกดาวหน้าวัวรูปตัว V",
        "stars": [
            {"id": 1, "name": "อัลเดบารัน (Aldebaran - α Tau ตาแดง)", "ra": ra_deg(4, 35, 55.2), "dec": dec_deg(16, 30, 33), "mag": 0.85, "color": "#FF4757", "bright": True},
            {"id": 2, "name": "เอลนาธ (Elnath - β Tau ปลายเขาเหนือ)", "ra": ra_deg(5, 26, 17.5), "dec": dec_deg(28, 36, 27), "mag": 1.65, "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "เทียนกวาน (Tianguan - ζ Tau ปลายเขาใต้)", "ra": ra_deg(5, 37, 38.7), "dec": dec_deg(21, 8, 33), "mag": 2.97, "color": "#00F0FF", "bright": True},
            {"id": 4, "name": "ไอน์ (Ain - ε Tau ตาซ้าย)", "ra": ra_deg(4, 28, 37.0), "dec": dec_deg(19, 10, 50), "mag": 3.53, "color": "#FFD27D", "bright": False},
            {"id": 5, "name": "พรีมา ไฮยาดูม (γ Tau ยอดจมูก V)", "ra": ra_deg(4, 19, 47.6), "dec": dec_deg(15, 37, 40), "mag": 3.65, "color": "#FFA502", "bright": False},
            {"id": 6, "name": "เซกุนดา ไฮยาดูม (δ1 Tau)", "ra": ra_deg(4, 22, 56.0), "dec": dec_deg(17, 32, 33), "mag": 3.76, "color": "#FFA502", "bright": False},
            {"id": 7, "name": "ทีตา ทอไร (θ2 Tau)", "ra": ra_deg(4, 28, 39.7), "dec": dec_deg(15, 52, 15), "mag": 3.40, "color": "#FFFFFF", "bright": False},
            {"id": 8, "name": "แลมบ์ดา ทอไร (λ Tau อกวัว)", "ra": ra_deg(4, 0, 40.8), "dec": dec_deg(12, 29, 25), "mag": 3.41, "color": "#00F0FF", "bright": False},
            {"id": 9, "name": "ซี ทอไร (ξ Tau ขาหน้า)", "ra": ra_deg(3, 27, 10.1), "dec": dec_deg(9, 43, 58), "mag": 3.73, "color": "#FFFFFF", "bright": False},
            {"id": 10, "name": "อัลไซโอนี (Alcyone - กระจุกดาวลูกไก่ M45)", "ra": ra_deg(3, 47, 29.1), "dec": dec_deg(24, 6, 18), "mag": 2.87, "color": "#00F0FF", "bright": True}
        ],
        "lines": [
            [5, 6], [6, 4], [4, 2], # North horn: Nose -> Delta -> Ain -> Elnath
            [5, 7], [7, 1], [1, 3], # South horn: Nose -> Theta -> Aldebaran -> Tianguan
            [4, 1],                 # V bridge
            [5, 8], [8, 9]          # Bull chest & front legs
        ]
    },

    "gemini": {
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
        "hint": "มีดาวสว่าง 2 ดวงคู่กันด้านบนเป็นศีรษะ (คาสเตอร์และพอลลักซ์) และมีเส้นลำตัวสองคนยืนเคียงคู่กัน!",
        "funFact": "คาสเตอร์และพอลลักซ์เป็นพี่น้องฝาแฝดในเทพนิยายกรีก หนึ่งคนเก่งการต่อสู้ อีกคนเป็นอมตะ!",
        "starGuide": "มองหาดาวฤกษ์สว่างคู่กันบนฟ้า พอลลักซ์สีส้มและคาสเตอร์สีขาว",
        "stars": [
            {"id": 1, "name": "คาสเตอร์ (Castor - α Gem หัวพี่)", "ra": ra_deg(7, 34, 36.0), "dec": dec_deg(31, 53, 18), "mag": 1.58, "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "พอลลักซ์ (Pollux - β Gem หัวน้อง)", "ra": ra_deg(7, 45, 18.9), "dec": dec_deg(28, 1, 34), "mag": 1.14, "color": "#FFA502", "bright": True},
            {"id": 3, "name": "อัลฮีนา (Alhena - γ Gem เท้าพอลลักซ์)", "ra": ra_deg(6, 37, 42.7), "dec": dec_deg(16, 23, 57), "mag": 1.93, "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "วาซัต (Wasat - δ Gem เอวพอลลักซ์)", "ra": ra_deg(7, 20, 7.4), "dec": dec_deg(21, 58, 56), "mag": 3.50, "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "เมบซูดา (Mebsuta - ε Gem เอวคาสเตอร์)", "ra": ra_deg(6, 43, 55.9), "dec": dec_deg(25, 7, 52), "mag": 3.06, "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "เมกบูดา (Mekbuda - ζ Gem เข่าพอลลักซ์)", "ra": ra_deg(7, 4, 6.5), "dec": dec_deg(20, 34, 13), "mag": 4.01, "color": "#FFD27D", "bright": False},
            {"id": 7, "name": "โพรพัส (Propus - η Gem ปลายเท้าคาสเตอร์)", "ra": ra_deg(6, 14, 52.7), "dec": dec_deg(22, 30, 24), "mag": 3.32, "color": "#FF7675", "bright": False},
            {"id": 8, "name": "เทจัต (Tejat - μ Gem เท้าคาสเตอร์)", "ra": ra_deg(6, 22, 57.6), "dec": dec_deg(22, 30, 49), "mag": 2.87, "color": "#FF7675", "bright": True},
            {"id": 9, "name": "แคปปา เจมินอร์ม (κ Gem ไหล่พอลลักซ์)", "ra": ra_deg(7, 44, 26.9), "dec": dec_deg(24, 23, 53), "mag": 3.57, "color": "#FFA502", "bright": False},
            {"id": 10, "name": "ไอโอตา เจมินอร์ม (ι Gem ไหล่คาสเตอร์)", "ra": ra_deg(7, 25, 43.6), "dec": dec_deg(27, 47, 53), "mag": 3.78, "color": "#FFA502", "bright": False},
            {"id": 11, "name": "อัลซีร์ (Alzirr - ξ Gem ปลายเท้าพอลลักซ์)", "ra": ra_deg(6, 45, 17.4), "dec": dec_deg(12, 53, 44), "mag": 3.35, "color": "#FFD27D", "bright": False}
        ],
        "lines": [
            [1, 10], [10, 5], [5, 8], [8, 7],   # Castor Twin line: Head -> Shoulder -> Waist -> Foot
            [2, 9], [9, 4], [4, 6], [6, 3], [3, 11], # Pollux Twin line: Head -> Shoulder -> Waist -> Knee -> Foot
            [10, 9], [5, 4]                       # Holding hands / torso links
        ]
    },

    "cancer": {
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
        "funFact": "ใจกลางกระดองปูมีกระจุกดาวเปิดชื่อว่า 'รังผึ้ง' (Praesepe / M44) มองเห็นเป็นฝ้าหมอกประกายดาวสวยงามมาก!",
        "starGuide": "กลุ่มดาวรูปตัว Y คว่ำ อยู่ตรงกลางระหว่างกลุ่มดาวคนคู่และกลุ่มดาวสิงโต",
        "stars": [
            {"id": 1, "name": "อัลตาร์ฟ (Altarf - β Cnc ปลายก้ามใต้)", "ra": ra_deg(8, 16, 30.9), "dec": dec_deg(9, 11, 8), "mag": 3.53, "color": "#FFA502", "bright": True},
            {"id": 2, "name": "อาคูเบนส์ (Acubens - α Cnc ก้ามตะวันออก)", "ra": ra_deg(8, 58, 29.2), "dec": dec_deg(11, 51, 28), "mag": 4.26, "color": "#FFFFFF", "bright": False},
            {"id": 3, "name": "อาเซลลัส ออสตราลิส (δ Cnc กลางกระดองใต้)", "ra": ra_deg(8, 44, 41.1), "dec": dec_deg(18, 9, 15), "mag": 3.94, "color": "#FFA502", "bright": True},
            {"id": 4, "name": "อาเซลลัส บอเรียลิส (γ Cnc กลางกระดองเหนือ)", "ra": ra_deg(8, 43, 17.2), "dec": dec_deg(21, 28, 6), "mag": 4.66, "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "ไอโอตา แคนครี (ι Cnc ก้ามเหนือ)", "ra": ra_deg(8, 46, 41.8), "dec": dec_deg(28, 45, 36), "mag": 4.03, "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "กระจุกดาวรังผึ้ง (Beehive / M44 Praesepe)", "ra": ra_deg(8, 40, 24.0), "dec": dec_deg(19, 40, 0), "mag": 3.10, "color": "#00F0FF", "bright": True}
        ],
        "lines": [
            [5, 4], [4, 3], [3, 2], [3, 1] # Inverted Y: Iota -> Gamma -> Delta -> (Acubens & Altarf)
        ]
    },

    "leo": {
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
        "funFact": "ดาวฤกษ์ที่สว่างที่สุดคือ 'เรกูลัส' (Regulus) หรือหัวใจสิงห์ และมีดาว 'เดเนโบลา' (Denebola) แปลว่าพู่หางสิงโต!",
        "starGuide": "มองหาเคียวเกี่ยวข้าวทางทิศตะวันตกและดาวหัวใจสิงห์สีฟ้าขาวสว่างจ้า",
        "stars": [
            {"id": 1, "name": "เรกูลัส (Regulus - α Leo หัวใจสิงห์)", "ra": ra_deg(10, 8, 22.3), "dec": dec_deg(11, 58, 2), "mag": 1.36, "color": "#00F0FF", "bright": True},
            {"id": 2, "name": "เดเนโบลา (Denebola - β Leo หางสิงโต)", "ra": ra_deg(11, 49, 3.6), "dec": dec_deg(14, 34, 19), "mag": 2.14, "color": "#FFFFFF", "bright": True},
            {"id": 3, "name": "แอลเจอบา (Algieba - γ Leo คอสิงโต)", "ra": ra_deg(10, 19, 58.3), "dec": dec_deg(19, 50, 30), "mag": 2.01, "color": "#FFA502", "bright": True},
            {"id": 4, "name": "โซสมา (Zosma - δ Leo สะโพกบน)", "ra": ra_deg(11, 14, 6.5), "dec": dec_deg(20, 31, 25), "mag": 2.56, "color": "#FFFFFF", "bright": True},
            {"id": 5, "name": "อัลเกนูบี (Algenubi - ε Leo ยอดหัวสิงโต)", "ra": ra_deg(9, 45, 51.1), "dec": dec_deg(23, 46, 27), "mag": 2.97, "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "อัดฮาเฟรา (Adhafera - ζ Leo แผงคอ)", "ra": ra_deg(10, 16, 41.4), "dec": dec_deg(23, 25, 2), "mag": 3.43, "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "อัลจับฮาห์ (Al Jabhah - η Leo อกสิงโต)", "ra": ra_deg(10, 7, 19.9), "dec": dec_deg(16, 45, 46), "mag": 3.48, "color": "#FFFFFF", "bright": False},
            {"id": 8, "name": "เชอร์ทาน (Chertan - θ Leo สะโพกล่าง)", "ra": ra_deg(11, 14, 14.4), "dec": dec_deg(15, 25, 46), "mag": 3.33, "color": "#FFFFFF", "bright": False},
            {"id": 9, "name": "ราซาลาส (Rasalas - μ Leo ปลายจมูกสิงห์)", "ra": ra_deg(9, 52, 45.8), "dec": dec_deg(26, 0, 25), "mag": 3.88, "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [1, 7], [7, 3], [3, 6], [6, 9], [9, 5], # The Sickle / Mane (Regulus -> Eta -> Algieba -> Zeta -> Mu -> Epsilon)
            [3, 4], [4, 2], [2, 8], [8, 1],          # Body rectangle & tail (Algieba -> Zosma -> Denebola -> Chertan -> Regulus)
            [4, 8]                                  # Hindquarters vertical link (Zosma -> Chertan)
        ]
    },

    "virgo": {
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
        "funFact": "ดาวที่สว่างที่สุดคือ 'สไปกา' (Spica) แปลว่ารวงข้าวสาลี เป็นสัญลักษณ์ของเทพีแห่งการเกษตรและความอุดมสมบูรณ์!",
        "starGuide": "ลากเส้นโค้งต่อจากด้ามกระบวยกลุ่มดาวหมีใหญ่ ผ่านดาวอาร์คทูรัส แล้วจะพุ่งตรงมายังดาวสไปกา",
        "stars": [
            {"id": 1, "name": "สไปกา (Spica - α Vir รวงข้าวสาลี)", "ra": ra_deg(13, 25, 11.6), "dec": dec_deg(-11, 9, 41), "mag": 0.98, "color": "#00F0FF", "bright": True},
            {"id": 2, "name": "ซาวิยาวา (Zavijava - β Vir ศีรษะ)", "ra": ra_deg(11, 50, 41.7), "dec": dec_deg(1, 45, 53), "mag": 3.59, "color": "#FFD27D", "bright": False},
            {"id": 3, "name": "พอริมา (Porrima - γ Vir ไหล่/อก)", "ra": ra_deg(12, 41, 39.6), "dec": dec_deg(-1, 26, 58), "mag": 2.74, "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "มิเนเลาวา (Minelauva - δ Vir เอว)", "ra": ra_deg(12, 55, 36.2), "dec": dec_deg(3, 23, 51), "mag": 3.38, "color": "#FF4757", "bright": False},
            {"id": 5, "name": "วินเดเมียทริกซ์ (Vindemiatrix - ε Vir ปลายปีกขวา)", "ra": ra_deg(13, 2, 10.6), "dec": dec_deg(10, 57, 33), "mag": 2.85, "color": "#FFD27D", "bright": True},
            {"id": 6, "name": "เฮเซ (Heze - ζ Vir สะโพก)", "ra": ra_deg(13, 34, 41.6), "dec": dec_deg(-0, 35, 45), "mag": 3.38, "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "ซาเนียห์ (Zaniah - η Vir แขนซ้าย)", "ra": ra_deg(12, 19, 54.4), "dec": dec_deg(-0, 40, 0), "mag": 3.89, "color": "#FFFFFF", "bright": False},
            {"id": 8, "name": "เซียร์มา (Syrma - ι Vir ชายกระโปรง/เท้า)", "ra": ra_deg(14, 16, 0.9), "dec": dec_deg(-6, 0, 2), "mag": 4.07, "color": "#FFD27D", "bright": False},
            {"id": 9, "name": "คัง (Kang - κ Vir ปลายเท้า)", "ra": ra_deg(14, 12, 53.7), "dec": dec_deg(-10, 16, 26), "mag": 4.18, "color": "#00F0FF", "bright": False}
        ],
        "lines": [
            [2, 7], [7, 3],                         # Head to Shoulders (Zavijava -> Zaniah -> Porrima)
            [3, 4], [4, 5],                         # Torso to Wing (Porrima -> Minelauva -> Vindemiatrix)
            [4, 6], [6, 1],                         # Waist to Spica (Minelauva -> Heze -> Spica)
            [3, 1],                                 # Porrima to Spica
            [1, 8], [8, 9]                          # Spica to Gown / Feet (Spica -> Syrma -> Kang)
        ]
    },

    "libra": {
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
        "funFact": "เป็นราศีเดียวใน 12 จักราศีที่เป็นสิ่งของเครื่องใช้ แสดงถึงความยุติธรรมและสมดุล!",
        "starGuide": "ดาวจานเหนือคือ ซูเบนเอลเชมาลี (Zubeneschamali) สีเขียวมรกตแปลกตา",
        "stars": [
            {"id": 1, "name": "ซูเบนเอลเกนูบี (Zubenelgenubi - α2 Lib จานใต้)", "ra": ra_deg(14, 50, 52.7), "dec": dec_deg(-16, 2, 30), "mag": 2.75, "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "ซูเบนเอลเชมาลี (Zubeneschamali - β Lib จานเหนือ)", "ra": ra_deg(15, 17, 0.5), "dec": dec_deg(-9, 22, 58), "mag": 2.61, "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "ซูเบนเอลอัครับ (Zubenelakrab - γ Lib ขอบจานตะวันออก)", "ra": ra_deg(15, 35, 31.5), "dec": dec_deg(-14, 47, 22), "mag": 3.91, "color": "#FFA502", "bright": False},
            {"id": 4, "name": "บราเคียม (Brachium - σ Lib ฐานล่าง)", "ra": ra_deg(15, 4, 4.3), "dec": dec_deg(-25, 16, 55), "mag": 3.25, "color": "#FF4757", "bright": True},
            {"id": 5, "name": "อิปซิลอน ไลบรี (υ Lib สายถ่วง)", "ra": ra_deg(15, 37, 1.5), "dec": dec_deg(-28, 8, 7), "mag": 3.60, "color": "#FFA502", "bright": False},
            {"id": 6, "name": "เทา ไลบรี (τ Lib)", "ra": ra_deg(15, 38, 39.4), "dec": dec_deg(-29, 46, 40), "mag": 3.66, "color": "#00F0FF", "bright": False}
        ],
        "lines": [
            [2, 1], [2, 3], [3, 4], [4, 1], # Balance Beam & Central Diamond
            [3, 5], [4, 6]                   # Scale strings hanging down
        ]
    },

    "scorpio": {
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
            {"id": 1, "name": "แอนทาเรส (Antares - α Sco หัวใจสีแดง)", "ra": ra_deg(16, 29, 24.4), "dec": dec_deg(-26, 25, 55), "mag": 1.06, "color": "#FF4757", "bright": True},
            {"id": 2, "name": "ชอลา (Shaula - λ Sco ปลายเหล็กใน)", "ra": ra_deg(17, 33, 36.5), "dec": dec_deg(-37, 6, 14), "mag": 1.62, "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "ซาร์กัส (Sargas - θ Sco โค้งหางล่าง)", "ra": ra_deg(17, 37, 19.1), "dec": dec_deg(-42, 59, 52), "mag": 1.86, "color": "#FFD27D", "bright": True},
            {"id": 4, "name": "ดชูบา (Dschubba - δ Sco หน้าผากแมงป่อง)", "ra": ra_deg(16, 0, 20.0), "dec": dec_deg(-22, 37, 18), "mag": 2.29, "color": "#00F0FF", "bright": True},
            {"id": 5, "name": "ลาราวาก (Larawag - ε Sco โคนหาง)", "ra": ra_deg(16, 50, 10.2), "dec": dec_deg(-34, 17, 36), "mag": 2.29, "color": "#FFA502", "bright": True},
            {"id": 6, "name": "เกอร์แทบ (Girtab - κ Sco หางตวัด)", "ra": ra_deg(17, 42, 29.3), "dec": dec_deg(-39, 1, 48), "mag": 2.39, "color": "#00F0FF", "bright": True},
            {"id": 7, "name": "กราฟเฟียส (Acrab - β Sco ก้ามบน)", "ra": ra_deg(16, 5, 26.2), "dec": dec_deg(-19, 48, 19), "mag": 2.56, "color": "#00F0FF", "bright": True},
            {"id": 8, "name": "เลซัท (Lesath - υ Sco ปลายเหล็กในคู่)", "ra": ra_deg(17, 30, 45.8), "dec": dec_deg(-37, 17, 45), "mag": 2.70, "color": "#00F0FF", "bright": True},
            {"id": 9, "name": "ฟาง (Fang - π Sco ก้ามล่าง)", "ra": ra_deg(15, 58, 51.1), "dec": dec_deg(-26, 6, 51), "mag": 2.89, "color": "#00F0FF", "bright": False},
            {"id": 10, "name": "อัลนิยัต (Alniyat - σ Sco อกแมงป่อง)", "ra": ra_deg(16, 21, 11.3), "dec": dec_deg(-25, 35, 34), "mag": 2.90, "color": "#00F0FF", "bright": False},
            {"id": 11, "name": "ไพเคาฮาเล (Tau Sco อกล่าง)", "ra": ra_deg(16, 35, 53.0), "dec": dec_deg(-28, 12, 58), "mag": 2.82, "color": "#00F0FF", "bright": False},
            {"id": 12, "name": "มิว สกอร์ปี (μ1 Sco ท้อง)", "ra": ra_deg(16, 51, 52.2), "dec": dec_deg(-38, 2, 50), "mag": 3.00, "color": "#00F0FF", "bright": False},
            {"id": 13, "name": "เซตา สกอร์ปี (ζ2 Sco ก้นหาง)", "ra": ra_deg(16, 54, 35.1), "dec": dec_deg(-42, 21, 41), "mag": 3.62, "color": "#FFA502", "bright": False},
            {"id": 14, "name": "อีตา สกอร์ปี (η Sco)", "ra": ra_deg(17, 12, 9.2), "dec": dec_deg(-43, 14, 21), "mag": 3.32, "color": "#FFFFFF", "bright": False},
            {"id": 15, "name": "ไอโอตา สกอร์ปี (ι1 Sco)", "ra": ra_deg(17, 47, 35.1), "dec": dec_deg(-40, 7, 37), "mag": 2.99, "color": "#FFD27D", "bright": False}
        ],
        "lines": [
            [7, 4], [4, 9],               # Claws to Head (Acrab -> Dschubba -> Fang)
            [4, 10], [10, 1], [1, 11],    # Head to Heart (Dschubba -> Sigma -> Antares -> Tau)
            [11, 5], [5, 12], [12, 13], [13, 14], [14, 3], # J-Curve Spine (Tau -> Larawag -> Mu -> Zeta -> Eta -> Sargas)
            [3, 15], [15, 6], [6, 2], [2, 8]                 # Stinger curve (Sargas -> Iota -> Girtab -> Shaula -> Lesath)
        ]
    },

    "sagittarius": {
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
        "funFact": "ใจกลางทางช้างเผือก (Milky Way Galaxy) อันเป็นที่ตั้งของหลุมดำยักษ์ อยู่ตรงกลุ่มดาวนี้พอดี!",
        "starGuide": "มองหากลุ่มดาวรูปกาน้ำชาข้างๆ หางแมงป่อง พวยกาชี้ไปทางทิศตะวันตก",
        "stars": [
            {"id": 1, "name": "เคาส์ ออสตราลิส (Kaus Australis - ε Sgr ฐานกาน้ำ)", "ra": ra_deg(18, 24, 10.3), "dec": dec_deg(-34, 23, 5), "mag": 1.79, "color": "#00F0FF", "bright": True},
            {"id": 2, "name": "นูนาคี (Nunki - σ Sgr หูกาบน)", "ra": ra_deg(18, 55, 15.9), "dec": dec_deg(-26, 17, 48), "mag": 2.05, "color": "#00F0FF", "bright": True},
            {"id": 3, "name": "อัสเซลลา (Ascella - ζ Sgr หูกาล่าง)", "ra": ra_deg(19, 2, 36.7), "dec": dec_deg(-29, 52, 48), "mag": 2.60, "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "เคาส์ มีเดีย (Kaus Media - δ Sgr กลางพวยกา)", "ra": ra_deg(18, 20, 59.7), "dec": dec_deg(-29, 49, 41), "mag": 2.72, "color": "#FFA502", "bright": True},
            {"id": 5, "name": "เคาส์ โบเรียลิส (Kaus Borealis - λ Sgr ยอดฝากา)", "ra": ra_deg(18, 27, 58.2), "dec": dec_deg(-25, 25, 18), "mag": 2.82, "color": "#FFA502", "bright": True},
            {"id": 6, "name": "อัลนาสล์ (Alnasl - γ2 Sgr ปลายพวยกา)", "ra": ra_deg(18, 5, 48.5), "dec": dec_deg(-30, 25, 27), "mag": 2.98, "color": "#FFA502", "bright": True},
            {"id": 7, "name": "ฟาย ซากิตตารี (φ Sgr ฝากาหลัง)", "ra": ra_deg(18, 45, 39.4), "dec": dec_deg(-27, 0, 11), "mag": 3.17, "color": "#00F0FF", "bright": False},
            {"id": 8, "name": "เทา ซากิตตารี (τ Sgr หูกลาง)", "ra": ra_deg(19, 6, 56.4), "dec": dec_deg(-27, 40, 14), "mag": 3.32, "color": "#FFA502", "bright": False},
            {"id": 9, "name": "อัลบัลดาห์ (Albaldah - π Sgr หัวคนยิงธนู)", "ra": ra_deg(19, 9, 45.8), "dec": dec_deg(-21, 1, 25), "mag": 2.88, "color": "#FFD27D", "bright": True},
            {"id": 10, "name": "อีตา ซากิตตารี (η Sgr ปลายคันธนูล่าง)", "ra": ra_deg(18, 17, 37.7), "dec": dec_deg(-36, 45, 42), "mag": 3.10, "color": "#FF4757", "bright": False}
        ],
        "lines": [
            [6, 4], [4, 1], [1, 6],         # Spout triangle (Alnasl -> Kaus Media -> Kaus Australis)
            [4, 5], [5, 7],                 # Teapot Lid (Kaus Media -> Kaus Borealis -> Phi)
            [4, 1], [1, 3], [3, 7], [7, 4], # Teapot Bowl (Kaus Media -> Kaus Australis -> Ascella -> Phi)
            [7, 2], [2, 8], [8, 3],         # Teapot Handle (Phi -> Nunki -> Tau -> Ascella)
            [1, 10], [5, 9]                 # Bow & Arrow extensions
        ]
    },

    "capricorn": {
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
        "funFact": "ในตำนาน เทพแพะโดดหนีสัตว์ประหลาดลงน้ำ ร่างกายท่อนล่างเลยกลายเป็นหางปลา!",
        "starGuide": "ดาวหัวแพะคู่คือ อัลเจดี และ ดาบิห์ ทางทิศตะวันตก",
        "stars": [
            {"id": 1, "name": "เดเนบ อัลเจดี (Deneb Algedi - δ Cap หางปลา)", "ra": ra_deg(21, 47, 2.4), "dec": dec_deg(-16, 7, 38), "mag": 2.85, "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "ดาบิห์ (Dabih - β Cap เขาแพะ)", "ra": ra_deg(20, 21, 0.7), "dec": dec_deg(-14, 46, 53), "mag": 3.05, "color": "#FFA502", "bright": True},
            {"id": 3, "name": "อัลเจดี (Algedi - α2 Cap เขาแพะบน)", "ra": ra_deg(20, 18, 3.2), "dec": dec_deg(-12, 32, 41), "mag": 3.58, "color": "#FFD27D", "bright": False},
            {"id": 4, "name": "นาชิรา (Nashira - γ Cap ครีบหาง)", "ra": ra_deg(21, 40, 5.3), "dec": dec_deg(-16, 39, 44), "mag": 3.69, "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "เซตา แคปริคอร์นิ (ζ Cap ท้องปลาล่าง)", "ra": ra_deg(21, 26, 40.0), "dec": dec_deg(-22, 24, 41), "mag": 3.77, "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "ทีตา แคปริคอร์นิ (θ Cap สันหลังกลาง)", "ra": ra_deg(21, 5, 56.8), "dec": dec_deg(-17, 13, 58), "mag": 4.08, "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "โอเมกา แคปริคอร์นิ (ω Cap ก้นสามเหลี่ยม)", "ra": ra_deg(20, 51, 49.3), "dec": dec_deg(-26, 55, 9), "mag": 4.12, "color": "#FFA502", "bright": False},
            {"id": 8, "name": "ไซ แคปริคอร์นิ (ψ Cap ท้องล่างหน้า)", "ra": ra_deg(20, 46, 5.8), "dec": dec_deg(-25, 16, 14), "mag": 4.13, "color": "#FFD27D", "bright": False},
            {"id": 9, "name": "ไอโอตา แคปริคอร์นิ (ι Cap หลัง)", "ra": ra_deg(21, 22, 14.8), "dec": dec_deg(-16, 50, 4), "mag": 4.28, "color": "#FFD27D", "bright": False}
        ],
        "lines": [
            [3, 2], [2, 8], [8, 7], [7, 5], [5, 4], [4, 1], # Outer Triangle (Horn -> Belly -> Tail)
            [2, 6], [6, 9], [9, 4]                           # Top Spine Bar
        ]
    },

    "aquarius": {
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
        "funFact": "น้ำที่เทลงมาจากเหยือกคือสายน้ำอมฤตแห่งดวงดาว ไหลลงสู่ปากกลุ่มดาวปลาทางใต้!",
        "starGuide": "มองหาดาวฤกษ์สว่าง 'ซาดาลซูด' และ 'ซาดาลเมลิก' บนบ่าคนเทน้ำ",
        "stars": [
            {"id": 1, "name": "ซาดาลซูด (Sadalsuud - β Aqr ไหล่ซ้าย)", "ra": ra_deg(21, 31, 33.5), "dec": dec_deg(-5, 34, 16), "mag": 2.90, "color": "#FFD27D", "bright": True},
            {"id": 2, "name": "ซาดาลเมลิก (Sadalmelik - α Aqr ไหล่ขวา)", "ra": ra_deg(22, 5, 47.0), "dec": dec_deg(-0, 19, 11), "mag": 2.95, "color": "#FFD27D", "bright": True},
            {"id": 3, "name": "สแคต (Skat - δ Aqr ขา/ปลายสายน้ำ)", "ra": ra_deg(22, 54, 39.0), "dec": dec_deg(-15, 49, 15), "mag": 3.27, "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "อัลบาลิ (Albali - ε Aqr มือซ้าย)", "ra": ra_deg(20, 47, 40.5), "dec": dec_deg(-9, 29, 45), "mag": 3.78, "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "ซาดาคเบีย (Sadachbia - γ Aqr ปากเหยือก Y)", "ra": ra_deg(22, 21, 39.3), "dec": dec_deg(-1, 23, 14), "mag": 3.86, "color": "#FFFFFF", "bright": False},
            {"id": 6, "name": "เซตา แอควารี (ζ Aqr กลางปากเหยือก)", "ra": ra_deg(22, 28, 49.9), "dec": dec_deg(-0, 1, 12), "mag": 3.65, "color": "#FFFFFF", "bright": False},
            {"id": 7, "name": "อีตา แอควารี (η Aqr ปลายเหยือกบน)", "ra": ra_deg(22, 35, 21.3), "dec": dec_deg(0, 7, 2), "mag": 4.04, "color": "#00F0FF", "bright": False},
            {"id": 8, "name": "อันชา (Ancha - θ Aqr สะโพก)", "ra": ra_deg(22, 16, 50.0), "dec": dec_deg(-7, 46, 59), "mag": 4.17, "color": "#FFD27D", "bright": False},
            {"id": 9, "name": "แลมบ์ดา แอควารี (λ Aqr สายน้ำ)", "ra": ra_deg(22, 52, 36.9), "dec": dec_deg(-7, 34, 47), "mag": 3.73, "color": "#FF4757", "bright": False},
            {"id": 10, "name": "พาย แอควารี (π Aqr ยอดเหยือก)", "ra": ra_deg(22, 25, 16.6), "dec": dec_deg(1, 22, 39), "mag": 4.66, "color": "#00F0FF", "bright": False},
            {"id": 11, "name": "88 แอควารี (c2 Aqr ปลายสายน้ำล่าง)", "ra": ra_deg(23, 9, 26.8), "dec": dec_deg(-21, 10, 21), "mag": 3.68, "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [4, 1], [1, 2], [2, 8],          # Arms & Shoulders (Albali -> Sadalsuud -> Sadalmelik -> Ancha)
            [2, 5], [5, 6], [6, 7], [6, 10], # Water Urn Y-asterism (Sadalmelik -> Gamma -> Zeta -> Eta / Pi)
            [6, 9], [9, 3], [3, 11]          # Cascading Stream (Zeta -> Lambda -> Skat -> 88 Aqr)
        ]
    },

    "pisces": {
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
            {"id": 1, "name": "อัลริชา (Alrescha - α Psc ปมผูกริบบิ้น)", "ra": ra_deg(2, 2, 2.8), "dec": dec_deg(2, 45, 50), "mag": 3.82, "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "อัลเฟิร์ก (Alpherg - η Psc ปลาเหนือ)", "ra": ra_deg(1, 31, 29.0), "dec": dec_deg(15, 20, 45), "mag": 3.62, "color": "#FFD27D", "bright": True},
            {"id": 3, "name": "แกมมา พิสเซียม (γ Psc วงปลาตะวันตก)", "ra": ra_deg(23, 17, 10.0), "dec": dec_deg(3, 16, 56), "mag": 3.70, "color": "#FFA502", "bright": True},
            {"id": 4, "name": "โอไมครอน พิสเซียม (ο Psc สายเหนือ 1)", "ra": ra_deg(1, 45, 23.6), "dec": dec_deg(9, 9, 28), "mag": 4.26, "color": "#FFA502", "bright": False},
            {"id": 5, "name": "นิว พิสเซียม (ν Psc สายเหนือ 2)", "ra": ra_deg(1, 41, 25.9), "dec": dec_deg(5, 29, 15), "mag": 4.45, "color": "#FFA502", "bright": False},
            {"id": 6, "name": "มิว พิสเซียม (μ Psc สายเหนือ 3)", "ra": ra_deg(1, 30, 11.0), "dec": dec_deg(6, 8, 38), "mag": 4.84, "color": "#FFA502", "bright": False},
            {"id": 7, "name": "ไซ พิสเซียม (ξ Psc สายเหนือ 4)", "ra": ra_deg(1, 53, 33.3), "dec": dec_deg(3, 11, 15), "mag": 4.61, "color": "#FFA502", "bright": False},
            {"id": 8, "name": "เดลตา พิสเซียม (δ Psc สายตะวันตก 1)", "ra": ra_deg(0, 48, 40.9), "dec": dec_deg(7, 35, 6), "mag": 4.44, "color": "#FFA502", "bright": False},
            {"id": 9, "name": "เอปซิลอน พิสเซียม (ε Psc สายตะวันตก 2)", "ra": ra_deg(1, 2, 56.6), "dec": dec_deg(7, 53, 24), "mag": 4.27, "color": "#FFA502", "bright": False},
            {"id": 10, "name": "เซตา พิสเซียม (ζ Psc สายตะวันตก 3)", "ra": ra_deg(1, 13, 43.8), "dec": dec_deg(7, 34, 32), "mag": 5.21, "color": "#FFFFFF", "bright": False},
            {"id": 11, "name": "ทีตา พิสเซียม (θ Psc วงปลา)", "ra": ra_deg(23, 27, 58.2), "dec": dec_deg(6, 22, 44), "mag": 4.27, "color": "#FFA502", "bright": False},
            {"id": 12, "name": "ไอโอตา พิสเซียม (ι Psc วงปลา)", "ra": ra_deg(23, 39, 57.0), "dec": dec_deg(5, 37, 35), "mag": 4.13, "color": "#FFD27D", "bright": False},
            {"id": 13, "name": "แลมบ์ดา พิสเซียม (λ Psc วงปลา)", "ra": ra_deg(23, 42, 2.8), "dec": dec_deg(1, 46, 46), "mag": 4.49, "color": "#FFFFFF", "bright": False},
            {"id": 14, "name": "แคปปา พิสเซียม (κ Psc วงปลา)", "ra": ra_deg(23, 26, 55.9), "dec": dec_deg(1, 15, 20), "mag": 4.95, "color": "#FFFFFF", "bright": False},
            {"id": 15, "name": "7 พิสเซียม (7 Psc วงปลา)", "ra": ra_deg(23, 11, 2.0), "dec": dec_deg(5, 5, 23), "mag": 5.05, "color": "#FFA502", "bright": False}
        ],
        "lines": [
            [1, 7], [7, 5], [5, 6], [6, 4], [4, 2],         # North Cord: Alrescha -> Xi -> Nu -> Mu -> Omicron -> Alpherg
            [1, 10], [10, 9], [9, 8], [8, 12],             # West Cord: Alrescha -> Zeta -> Epsilon -> Delta -> Iota
            [12, 11], [11, 15], [15, 3], [3, 14], [14, 13], [13, 12] # Circlet of Pisces loop
        ]
    }
}

# Project spherical celestial coordinates (RA, Dec) onto a 2D plane (Standard Sky Chart: East = Left, North = Up)
# In SVG: X increases Right, Y increases Down
def project_constellation(const_data, width=500, height=400, padding=48):
    stars = const_data["stars"]
    
    # Standard sky coordinates (radians)
    ras = [s["ra"] for s in stars]
    decs = [s["dec"] for s in stars]
    
    # Handle RA wrap-around near 0h/24h (e.g. Pisces: 23h to 2h)
    min_ra = min(ras)
    max_ra = max(ras)
    if max_ra - min_ra > 180.0:
        # Wrap stars with ra < 180 by +360
        ras_unwrapped = [ra + 360.0 if ra < 180.0 else ra for ra in ras]
    else:
        ras_unwrapped = ras
        
    ra0 = sum(ras_unwrapped) / len(ras_unwrapped)
    dec0 = sum(decs) / len(decs)
    
    # Gnomonic / Orthographic sky projection
    # X_sky = -(RA - RA0) * cos(Dec0)  [East is left, West is right]
    # Y_sky = (Dec - Dec0)             [North is up, South is down]
    proj_points = []
    dec0_rad = math.radians(dec0)
    
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
    
    # Keep uniform aspect ratio (1:1 sky geometry)
    scale = min(avail_w / span_x, avail_h / span_y)
    
    # Center inside viewBox
    center_x = width / 2.0
    center_y = height / 2.0
    mid_proj_x = (min_x + max_x) / 2.0
    mid_proj_y = (min_y + max_y) / 2.0
    
    svg_stars = []
    for x_sky, y_sky, s in proj_points:
        # SVG X = center_x + (x_sky - mid_proj_x) * scale
        # SVG Y = center_y - (y_sky - mid_proj_y) * scale  (flip Y because Dec+ is Up, SVG+ is Down)
        svg_x = round(center_x + (x_sky - mid_proj_x) * scale)
        svg_y = round(center_y - (y_sky - mid_proj_y) * scale)
        
        # Calculate visual radius based on apparent magnitude Vmag
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
            
        svg_stars.append({
            "id": s["id"],
            "x": svg_x,
            "y": svg_y,
            "r": r,
            "name": s["name"],
            "mag": s["mag"],
            "bright": s["bright"],
            "color": s["color"]
        })
        
    return svg_stars

# Test all 12 constellations
all_projected = {}
for cid, cdata in CONSTELLATIONS_ASTRO.items():
    svg_stars = project_constellation(cdata)
    all_projected[cid] = svg_stars
    print(f"Projected {cid}: {len(svg_stars)} stars processed successfully.")

with open("scratch/projected_stars.json", "w", encoding="utf-8") as f:
    json.dump(all_projected, f, indent=2, ensure_ascii=False)
print("Saved to scratch/projected_stars.json")
