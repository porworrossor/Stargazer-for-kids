# -*- coding: utf-8 -*-
"""
Deep verification of js/constellations.js
"""
import json
import re

with open("js/constellations.js", "r", encoding="utf-8") as f:
    code = f.read()

# Extract JSON from `const CONSTELLATIONS_DATA = ...;`
json_match = re.search(r'const\s+CONSTELLATIONS_DATA\s*=\s*(\[[\s\S]*?\]);', code)
assert json_match, "Could not find CONSTELLATIONS_DATA array"

data = json.loads(json_match.group(1))

print(f"Found {len(data)} constellations.")
assert len(data) == 12, "Must be 12 constellations"

for c in data:
    cid = c["id"]
    star_ids = [s["id"] for s in c["stars"]]
    lines = c["lines"]
    
    print(f"Constellation: {cid} | {len(star_ids)} stars | {len(lines)} lines | Answer: {c.get('correctAnswer')}")
    
    for p1, p2 in lines:
        assert p1 in star_ids, f"Line start {p1} not in stars for {cid}"
        assert p2 in star_ids, f"Line end {p2} not in stars for {cid}"
        
    assert "<g class=\"overlay-graphic\"" in c["artOverlay"], f"Overlay missing for {cid}"
    assert "</g>" in c["artOverlay"], f"Overlay tag unclosed for {cid}"

print("SUCCESS: All 12 constellations passed deep verification!")
