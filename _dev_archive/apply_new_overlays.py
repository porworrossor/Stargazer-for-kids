# -*- coding: utf-8 -*-
"""
Apply beautiful, clear, and distinct vector overlays to js/constellations.js
"""
import json
import re
from generate_all_overlays import get_overlays

with open("js/constellations.js", "r", encoding="utf-8") as f:
    content = f.read()

json_match = re.search(r'const\s+CONSTELLATIONS_DATA\s*=\s*(\[[\s\S]*?\]);', content)
assert json_match, "Could not find CONSTELLATIONS_DATA"

data = json.loads(json_match.group(1))
overlays = get_overlays()

for c in data:
    cid = c["id"]
    if cid in overlays:
        c["artOverlay"] = overlays[cid].strip()
        print(f"Updated overlay for: {cid}")

updated_json = json.dumps(data, ensure_ascii=False, indent=2)

new_js = f"""/**
 * ฐานข้อมูลกลุ่มดาว 12 จักราศี (12 Zodiac Constellations Dataset)
 * ปรับปรุงภาพร่างเวกเตอร์ (Art Overlay) ให้ชัดเจน สวยงาม และตรงตามรูปร่างกลุ่มดาว 100%
 */

const CONSTELLATIONS_DATA = {updated_json};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ CONSTELLATIONS_DATA }};
}}
"""

with open("js/constellations.js", "w", encoding="utf-8") as f:
    f.write(new_js)

print("SUCCESS: Updated all 12 constellation art overlays in js/constellations.js!")
