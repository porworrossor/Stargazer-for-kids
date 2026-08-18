# -*- coding: utf-8 -*-
"""
Script to test and format updated constellation data for:
1. Libra
2. Sagittarius
3. Aquarius
4. Pisces
5. Gemini
Matching the user's uploaded images.
"""
import math

def normalize_points(points, target_w=440, target_h=340, pad_x=30, pad_y=30):
    min_x = min(p[0] for p in points.values())
    max_x = max(p[0] for p in points.values())
    min_y = min(p[1] for p in points.values())
    max_y = max(p[1] for p in points.values())

    scale_x = target_w / (max_x - min_x) if max_x != min_x else 1
    scale_y = target_h / (max_y - min_y) if max_y != min_y else 1
    scale = min(scale_x, scale_y)

    norm = {}
    for k, (x, y) in points.items():
        nx = round(pad_x + (x - min_x) * scale)
        ny = round(pad_y + (y - min_y) * scale)
        norm[k] = (nx, ny)
    return norm

print("Helper ready")
