# -*- coding: utf-8 -*-
"""
Full Dataset Generator for 12 Zodiac Constellations
Computes astronomical projection and pairs with precision Art Overlays & IAU Lines
"""
import math
import json

def ra_deg(h, m, s=0.0):
    return (h + m/60.0 + s/3600.0) * 15.0

def dec_deg(d, m, s=0.0):
    sign = -1.0 if d < 0 else 1.0
    return sign * (abs(d) + m/60.0 + s/3600.0)

# Full 12 Constellations data
DATA = [
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
            {"id": 5, "name": "ภารณี (Bharani - 41 Ari)", "bayer": "41 Ari", "ra": ra_deg(2, 49, 59.0), "dec": dec_deg(27, 15, 38), "mag": 3.61, "spect": "B8 V (ดาวฟ้าขาว)", "color": "#00F0FF", "bright": False}
        ],
        "lines": [
            [4, 1], [1, 2], [2, 3], [1, 5]
        ]
    },
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
        ]
    },
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
        "hint": "มีดาวสว่าง 2 ดวงคู่กันด้านบนเป็นศีรษะ (คาสเตอร์และพอลลักซ์) และมีเส้นลำตัวสองคนยืนเคียงคู่กัน!",
        "funFact": "คาสเตอร์และพอลลักซ์เป็นพี่น้องฝาแฝดในเทพนิยายกรีก หนึ่งคนเก่งการต่อสู้ อีกคนเป็นอมตะ!",
        "starGuide": "มองหาดาวฤกษ์สว่างคู่กันบนฟ้า พอลลักซ์สีส้มและคาสเตอร์สีขาว",
        "stars": [
            {"id": 1, "name": "คาสเตอร์ (Castor - α Gem หัวพี่)", "bayer": "α Gem", "ra": ra_deg(7, 34, 36.0), "dec": dec_deg(31, 53, 18), "mag": 1.58, "spect": "A1 V (ระบบดาวฤกษ์ 6 ดวง)", "color": "#FFFFFF", "bright": True},
            {"id": 2, "name": "พอลลักซ์ (Pollux - β Gem หัวน้อง)", "bayer": "β Gem", "ra": ra_deg(7, 45, 18.9), "dec": dec_deg(28, 1, 34), "mag": 1.14, "spect": "K0 III (ดาวยักษ์ส้ม มีดาวเคราะห์บริวาร)", "color": "#FFA502", "bright": True},
            {"id": 3, "name": "อัลฮีนา (Alhena - γ Gem เท้าพอลลักซ์)", "bayer": "γ Gem", "ra": ra_deg(6, 37, 42.7), "dec": dec_deg(16, 23, 57), "mag": 1.93, "spect": "A1.5 IV (ดาวย่อยยักษ์ขาว)", "color": "#FFFFFF", "bright": True},
            {"id": 4, "name": "วาซัต (Wasat - δ Gem เอวพอลลักซ์)", "bayer": "δ Gem", "ra": ra_deg(7, 20, 7.4), "dec": dec_deg(21, 58, 56), "mag": 3.50, "spect": "F0 IV (ดาวย่อยยักษ์เหลืองขาว)", "color": "#FFFFFF", "bright": False},
            {"id": 5, "name": "เมบซูดา (Mebsuta - ε Gem เอวคาสเตอร์)", "bayer": "ε Gem", "ra": ra_deg(6, 43, 55.9), "dec": dec_deg(25, 7, 52), "mag": 3.06, "spect": "G8 Ib (ดาวยักษ์ใหญ่เหลือง)", "color": "#FFD27D", "bright": False},
            {"id": 6, "name": "เมกบูดา (Mekbuda - ζ Gem เข่าพอลลักซ์)", "bayer": "ζ Gem", "ra": ra_deg(7, 4, 6.5), "dec": dec_deg(20, 34, 13), "mag": 4.01, "spect": "F7-G3 Ib (ดาวแปรแสงเซเฟอิด)", "color": "#FFD27D", "bright": False},
            {"id": 7, "name": "โพรพัส (Propus - η Gem ปลายเท้าคาสเตอร์)", "bayer": "η Gem", "ra": ra_deg(6, 14, 52.7), "dec": dec_deg(22, 30, 24), "mag": 3.32, "spect": "M3 III (ดาวยักษ์แดง)", "color": "#FF7675", "bright": False},
            {"id": 8, "name": "เทจัต (Tejat - μ Gem เท้าคาสเตอร์)", "bayer": "μ Gem", "ra": ra_deg(6, 22, 57.6), "dec": dec_deg(22, 30, 49), "mag": 2.87, "spect": "M3 III (ดาวยักษ์แดง)", "color": "#FF7675", "bright": True},
            {"id": 9, "name": "แคปปา เจมินอร์ม (κ Gem ไหล่พอลลักซ์)", "bayer": "κ Gem", "ra": ra_deg(7, 44, 26.9), "dec": dec_deg(24, 23, 53), "mag": 3.57, "spect": "G8 III (ดาวยักษ์ส้มเหลือง)", "color": "#FFA502", "bright": False},
            {"id": 10, "name": "ไอโอตา เจมินอร์ม (ι Gem ไหล่คาสเตอร์)", "bayer": "ι Gem", "ra": ra_deg(7, 25, 43.6), "dec": dec_deg(27, 47, 53), "mag": 3.78, "spect": "K0 III (ดาวยักษ์ส้ม)", "color": "#FFA502", "bright": False},
            {"id": 11, "name": "อัลซีร์ (Alzirr - ξ Gem ปลายเท้าพอลลักซ์)", "bayer": "ξ Gem", "ra": ra_deg(6, 45, 17.4), "dec": dec_deg(12, 53, 44), "mag": 3.35, "spect": "F5 IV (ดาวเหลืองขาว)", "color": "#FFD27D", "bright": False}
        ],
        "lines": [
            [1, 10], [10, 5], [5, 8], [8, 7],
            [2, 9], [9, 4], [4, 6], [6, 3], [3, 11],
            [10, 9], [5, 4]
        ]
    },
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
        ]
    },
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
        ]
    },
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
        ]
    },
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
        ]
    },
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
        ]
    },
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
        ]
    },
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
        ]
    },
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
        ]
    },
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
        ]
    }
]

def project_all():
    results = []
    width = 500
    height = 400
    padding = 50
    
    for c in DATA:
        stars = c["stars"]
        ras = [s["ra"] for s in stars]
        decs = [s["dec"] for s in stars]
        
        # Wrap-around for Pisces
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
            
        c_copy = dict(c)
        c_copy["viewBox"] = f"0 0 {width} {height}"
        c_copy["stars"] = projected_stars
        results.append(c_copy)
        
    return results

computed = project_all()
for c in computed:
    print(f"Constellation {c['id']}:")
    for s in c["stars"]:
        print(f"  {s['id']}: ({s['x']}, {s['y']}) - {s['name']}")
