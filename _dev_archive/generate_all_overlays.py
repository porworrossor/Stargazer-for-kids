# -*- coding: utf-8 -*-
"""
Generate highly detailed, beautiful, and unmistakable SVG Art Overlays
for all 12 Zodiac Constellations.
"""

import json

def get_overlays():
    return {
        "aries": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Ram Golden Horn (Detailed Double Swirl following Hamal -> Sheratan -> Mesarthim) -->
        <path d="M 360 190 C 410 180, 465 210, 460 270 C 455 315, 410 330, 395 295 C 385 270, 410 240, 430 250" 
              fill="none" stroke="#FFD700" stroke-width="10" stroke-linecap="round" filter="drop-shadow(0 0 12px #FFD700)" />
        <path d="M 360 190 C 405 185, 450 215, 448 265 C 445 298, 415 310, 405 288" 
              fill="none" stroke="#FFA502" stroke-width="5" stroke-linecap="round" />
        
        <!-- Ram Head & Snout (at Hamal 383, 218) -->
        <ellipse cx="360" cy="225" rx="36" ry="30" fill="#FFEAA7" fill-opacity="0.6" stroke="#F1C40F" stroke-width="2.5" />
        <!-- Cute Muzzle & Nose -->
        <path d="M 380 235 Q 395 245 385 255 Q 365 255 360 245 Z" fill="#FFA502" fill-opacity="0.8" />
        <!-- Big Eye -->
        <circle cx="368" cy="218" r="5" fill="#060919" />
        <circle cx="370" cy="216" r="2" fill="#FFFFFF" />
        <!-- Cute Ear -->
        <ellipse cx="330" cy="215" rx="14" ry="7" transform="rotate(-20 330 215)" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <ellipse cx="330" cy="215" rx="9" ry="4" transform="rotate(-20 330 215)" fill="#FF7675" fill-opacity="0.6" />

        <!-- Fluffy Wool Clouds Body (covering 41 Ari 159, 132 to Botein 45, 304) -->
        <path d="M 330 230 Q 310 160 250 160 Q 200 120 150 140 Q 90 140 70 200 Q 40 240 50 290 Q 70 330 130 330 Q 180 340 230 320 Q 290 330 330 280 Z" 
              fill="#70A1FF" fill-opacity="0.3" stroke="#00F0FF" stroke-width="3" filter="drop-shadow(0 0 10px rgba(0, 240, 255, 0.4))" />
        
        <!-- Wool Texture Fluffs -->
        <circle cx="160" cy="180" r="28" fill="#70A1FF" fill-opacity="0.35" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,4" />
        <circle cx="230" cy="200" r="32" fill="#70A1FF" fill-opacity="0.35" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,4" />
        <circle cx="120" cy="240" r="30" fill="#70A1FF" fill-opacity="0.35" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,4" />

        <!-- 4 Legs with Golden Hooves -->
        <path d="M 280 310 L 275 375 L 290 375 L 295 310" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <rect x="272" y="365" width="20" height="12" rx="3" fill="#FFD700" />
        
        <path d="M 220 320 L 215 375 L 230 375 L 235 320" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <rect x="212" y="365" width="20" height="12" rx="3" fill="#FFD700" />

        <path d="M 130 325 L 120 375 L 135 375 L 145 325" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <rect x="117" y="365" width="20" height="12" rx="3" fill="#FFD700" />

        <path d="M 80 310 L 70 370 L 85 370 L 95 310" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <rect x="67" y="360" width="20" height="12" rx="3" fill="#FFD700" />

        <!-- Little Fluffy Tail -->
        <ellipse cx="40" cy="260" rx="14" ry="10" transform="rotate(-30 40 260)" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
      </g>
        """,

        "taurus": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- North Long Sharp Horn to Elnath (81, 75) -->
        <path d="M 262 200 C 230 150, 160 100, 81 75" 
              fill="none" stroke="#FFD700" stroke-width="9" stroke-linecap="round" filter="drop-shadow(0 0 10px #FFD700)" />
        <path d="M 262 200 C 230 150, 160 100, 81 75" 
              fill="none" stroke="#FFA502" stroke-width="4" stroke-linecap="round" />
        <polygon points="81,75 95,85 85,95" fill="#FFD700" filter="drop-shadow(0 0 8px #FFD700)" />

        <!-- South Long Sharp Horn to Tianguan (45, 174) -->
        <path d="M 239 235 C 190 220, 110 195, 45 174" 
              fill="none" stroke="#FFD700" stroke-width="9" stroke-linecap="round" filter="drop-shadow(0 0 10px #FFD700)" />
        <path d="M 239 235 C 190 220, 110 195, 45 174" 
              fill="none" stroke="#FFA502" stroke-width="4" stroke-linecap="round" />
        <polygon points="45,174 60,180 52,192" fill="#FFD700" filter="drop-shadow(0 0 8px #FFD700)" />

        <!-- Bull Head / Forehead (Hyades V-cluster) -->
        <polygon points="262,200 239,235 290,265 310,230" fill="#FF4757" fill-opacity="0.5" stroke="#FF6B81" stroke-width="3" />
        <!-- Broad Bull Muzzle / Snout -->
        <path d="M 285 245 Q 330 265 320 295 Q 280 300 270 270 Z" fill="#E17055" fill-opacity="0.8" stroke="#D63031" stroke-width="2" />
        <!-- Nostrils -->
        <ellipse cx="305" cy="275" rx="5" ry="3" fill="#2D3436" />
        <ellipse cx="290" cy="278" rx="5" ry="3" fill="#2D3436" />

        <!-- Fierce Glowing Red Eye at Aldebaran (239, 235) -->
        <circle cx="239" cy="235" r="14" fill="#FF0000" fill-opacity="0.5" filter="drop-shadow(0 0 12px #FF0000)" />
        <circle cx="239" cy="235" r="6" fill="#FFFFFF" />
        <circle cx="239" cy="235" r="3" fill="#000000" />

        <!-- Left Eye at Ain (262, 200) -->
        <circle cx="262" cy="200" r="5" fill="#FFD27D" />
        <circle cx="262" cy="200" r="2" fill="#000000" />

        <!-- Bull Ears -->
        <path d="M 270 185 Q 310 170 305 195 Z" fill="#FF6B81" stroke="#D63031" stroke-width="2" />
        <path d="M 230 250 Q 240 285 220 275 Z" fill="#FF6B81" stroke="#D63031" stroke-width="2" />

        <!-- Powerful Muscular Body & Shoulder Hump -->
        <path d="M 262 200 Q 330 140 400 170 Q 460 210 460 310 L 370 340 L 320 295 Z" 
              fill="#FF4757" fill-opacity="0.3" stroke="#FF6B81" stroke-width="2.5" />
        
        <!-- Forelegs Galloping Forward -->
        <path d="M 370 320 L 455 335 L 450 355 L 360 340 Z" fill="#E17055" fill-opacity="0.6" stroke="#D63031" stroke-width="2" />
        <!-- Golden Hoof -->
        <polygon points="455,335 470,340 465,360 450,355" fill="#FFD700" />

        <!-- Pleiades Cluster (Seven Sisters) Sparkling Nebula at (391, 135) -->
        <circle cx="391" cy="135" r="28" fill="#00F0FF" fill-opacity="0.25" filter="drop-shadow(0 0 16px #00F0FF)" />
        <circle cx="391" cy="135" r="16" fill="#FFFFFF" fill-opacity="0.3" />
        <text x="360" y="115" fill="#00F0FF" font-size="10" font-family="sans-serif" font-weight="bold">✨ กระจุกดาวลูกไก่</text>
      </g>
        """,

        "gemini": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Castor (Right Brother - White/Cyan) -->
        <g stroke="#70A1FF" stroke-width="2" fill="none">
          <!-- Head with Golden Laurel -->
          <circle cx="215" cy="85" r="24" fill="#FFEAA7" fill-opacity="0.7" stroke="#F1C40F" stroke-width="2.5" />
          <!-- Hair & Laurel Wreath -->
          <path d="M 195 75 Q 215 55 235 75 Q 215 70 195 75 Z" fill="#F1C40F" />
          <!-- Face Details -->
          <circle cx="210" cy="82" r="3" fill="#060919" /><circle cx="211" cy="81" r="1" fill="#fff" />
          <path d="M 205 94 Q 215 100 225 94" stroke="#D63031" stroke-width="2" stroke-linecap="round" />

          <!-- Torso & Greek Chiton Tunic -->
          <path d="M 200 108 L 245 125 L 310 195 L 260 215 L 210 145 Z" fill="#70A1FF" fill-opacity="0.5" stroke="#1E90FF" stroke-width="2" />
          <!-- Belt / Sash -->
          <line x1="260" y1="215" x2="310" y2="195" stroke="#FFD700" stroke-width="4" />

          <!-- Raised Right Arm (α -> θ -> τ) -->
          <path d="M 235 100 L 315 75 L 265 125" fill="#FFEAA7" fill-opacity="0.6" stroke="#F1C40F" stroke-width="3" stroke-linecap="round" />
          <circle cx="315" cy="75" r="6" fill="#FFD700" />

          <!-- Left & Right Legs -->
          <path d="M 270 215 L 335 260 L 370 285" stroke="#FFEAA7" stroke-width="7" stroke-linecap="round" />
          <path d="M 290 205 L 385 235 L 410 235 L 445 225" stroke="#FFEAA7" stroke-width="7" stroke-linecap="round" />
          <!-- Sandals -->
          <rect x="365" y="280" width="16" height="10" rx="3" fill="#FFD700" />
          <rect x="435" y="220" width="16" height="10" rx="3" fill="#FFD700" />
        </g>

        <!-- Pollux (Left Brother - Orange/Gold) -->
        <g stroke="#FFA502" stroke-width="2" fill="none">
          <!-- Head with Golden Laurel -->
          <circle cx="155" cy="125" r="24" fill="#FFEAA7" fill-opacity="0.7" stroke="#F1C40F" stroke-width="2.5" />
          <!-- Hair & Laurel Wreath -->
          <path d="M 135 115 Q 155 95 175 115 Q 155 110 135 115 Z" fill="#E67E22" />
          <!-- Face Details -->
          <circle cx="150" cy="122" r="3" fill="#060919" /><circle cx="151" cy="121" r="1" fill="#fff" />
          <path d="M 145 134 Q 155 140 165 134" stroke="#D63031" stroke-width="2" stroke-linecap="round" />

          <!-- Torso & Greek Chiton Tunic -->
          <path d="M 145 148 L 135 180 L 205 230 L 245 190 L 185 145 Z" fill="#FFA502" fill-opacity="0.5" stroke="#E67E22" stroke-width="2" />
          <!-- Belt / Sash -->
          <line x1="205" y1="230" x2="245" y2="190" stroke="#FFD700" stroke-width="4" />

          <!-- Left Arm reaching out -->
          <path d="M 135 180 L 115 210 L 125 235" stroke="#FFEAA7" stroke-width="6" stroke-linecap="round" />

          <!-- Left & Right Legs -->
          <path d="M 205 230 L 235 280 L 335 335" stroke="#FFEAA7" stroke-width="7" stroke-linecap="round" />
          <path d="M 195 230 L 200 300 L 275 365" stroke="#FFEAA7" stroke-width="7" stroke-linecap="round" />
          <!-- Sandals -->
          <rect x="330" y="330" width="16" height="10" rx="3" fill="#FFD700" />
          <rect x="270" y="360" width="16" height="10" rx="3" fill="#FFD700" />
        </g>

        <!-- Affectionate Embracing Arms & Hands -->
        <path d="M 175 135 Q 205 120 235 135" stroke="#FFEAA7" stroke-width="8" stroke-linecap="round" />
        <circle cx="205" cy="130" r="7" fill="#FFD700" filter="drop-shadow(0 0 6px #FFD700)" />
      </g>
        """,

        "cancer": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Big Crab Shell / Carapace over M44 Praesepe (239, 189) -->
        <ellipse cx="239" cy="189" rx="65" ry="48" fill="#FF4757" fill-opacity="0.65" stroke="#FF6B81" stroke-width="3.5" filter="drop-shadow(0 0 14px rgba(255, 71, 87, 0.4))" />
        <ellipse cx="239" cy="189" rx="45" ry="32" fill="#FF6B81" fill-opacity="0.3" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="5,5" />

        <!-- Glowing Beehive Cluster M44 Core -->
        <circle cx="239" cy="189" r="22" fill="#00F0FF" fill-opacity="0.35" filter="drop-shadow(0 0 12px #00F0FF)" />
        <text x="210" y="193" fill="#FFFFFF" font-size="11" font-weight="bold">✨ M44</text>

        <!-- Big Right Pinching Claw (to Iota Cnc 215, 45) -->
        <path d="M 215 145 C 190 90, 160 50, 215 45 C 230 45, 250 80, 225 105 C 265 75, 275 110, 235 135 Z" 
              fill="#FF4757" stroke="#FF6B81" stroke-width="3" filter="drop-shadow(0 0 8px rgba(255, 71, 87, 0.5))" />
        <!-- Big Left Pinching Claw -->
        <path d="M 265 145 C 290 90, 320 50, 265 45 C 250 45, 230 80, 255 105 C 215 75, 205 110, 245 135 Z" 
              fill="#FF4757" stroke="#FF6B81" stroke-width="3" filter="drop-shadow(0 0 8px rgba(255, 71, 87, 0.5))" />

        <!-- Crab Stalk Eyes with Pupils -->
        <rect x="220" y="130" width="8" height="18" rx="3" fill="#FF4757" />
        <circle cx="224" cy="130" r="9" fill="#FFFFFF" stroke="#FF4757" stroke-width="2" />
        <circle cx="224" cy="130" r="4.5" fill="#060919" />
        <circle cx="226" cy="128" r="1.5" fill="#FFFFFF" />

        <rect x="250" y="130" width="8" height="18" rx="3" fill="#FF4757" />
        <circle cx="254" cy="130" r="9" fill="#FFFFFF" stroke="#FF4757" stroke-width="2" />
        <circle cx="254" cy="130" r="4.5" fill="#060919" />
        <circle cx="256" cy="128" r="1.5" fill="#FFFFFF" />

        <!-- Cute Smile -->
        <path d="M 230 165 Q 239 175 248 165" stroke="#060919" stroke-width="2.5" stroke-linecap="round" fill="none" />

        <!-- Left Walking Legs to Acubens (171, 313) -->
        <path d="M 185 180 Q 130 220 150 280 Q 155 310 171 313" stroke="#FFA502" stroke-width="6" stroke-linecap="round" fill="none" />
        <path d="M 185 200 Q 120 250 130 320" stroke="#FFA502" stroke-width="5" stroke-linecap="round" fill="none" />
        <path d="M 195 220 Q 140 280 145 350" stroke="#FFA502" stroke-width="5" stroke-linecap="round" fill="none" />

        <!-- Right Walking Legs to Altarf (329, 355) -->
        <path d="M 290 180 Q 350 220 330 280 Q 325 310 329 355" stroke="#FFA502" stroke-width="6" stroke-linecap="round" fill="none" />
        <path d="M 290 200 Q 360 250 350 320" stroke="#FFA502" stroke-width="5" stroke-linecap="round" fill="none" />
        <path d="M 280 220 Q 340 280 335 350" stroke="#FFA502" stroke-width="5" stroke-linecap="round" fill="none" />
      </g>
        """,

        "leo": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Lion Head & Magnificent Flowing Mane outlining The Sickle (455, 133 -> 380, 299) -->
        <path d="M 370 270 C 430 250, 480 200, 475 120 C 470 60, 400 40, 360 80 C 330 110, 330 160, 350 200 C 320 220, 330 270, 370 270 Z" 
              fill="#FFA502" fill-opacity="0.5" stroke="#FFD700" stroke-width="3" filter="drop-shadow(0 0 12px #FFA502)" />
        
        <!-- Noble Lion Face Profile -->
        <circle cx="410" cy="140" r="32" fill="#FFEAA7" fill-opacity="0.8" stroke="#F1C40F" stroke-width="2" />
        <!-- Eye -->
        <ellipse cx="425" cy="130" rx="6" ry="4" fill="#060919" />
        <circle cx="427" cy="128" r="1.5" fill="#FFFFFF" />
        <!-- Nose & Whiskers -->
        <polygon points="440,145 448,140 448,150" fill="#D63031" />
        <line x1="435" y1="152" x2="455" y2="155" stroke="#2D3436" stroke-width="1.5" />
        <line x1="435" y1="156" x2="455" y2="162" stroke="#2D3436" stroke-width="1.5" />
        <!-- Ear -->
        <path d="M 390 115 Q 400 95 415 110 Z" fill="#FFA502" stroke="#E67E22" stroke-width="2" />

        <!-- Lion Mane Swirls -->
        <path d="M 455 133 Q 480 80 432 101 Q 380 70 352 138 Q 320 180 341 188 Q 350 250 380 299" 
              fill="none" stroke="#FFD700" stroke-width="6" stroke-linecap="round" />

        <!-- Glowing Heart at Regulus (380, 299) -->
        <circle cx="380" cy="299" r="18" fill="#00F0FF" fill-opacity="0.4" filter="drop-shadow(0 0 14px #00F0FF)" />
        <circle cx="380" cy="299" r="8" fill="#FFFFFF" />

        <!-- Powerful Muscular Body (extending West to Denebola 45, 262) -->
        <path d="M 350 200 Q 250 160 161 178 Q 90 200 45 262 L 120 280 Q 200 240 280 270 L 350 260 Z" 
              fill="#FFA502" fill-opacity="0.35" stroke="#FF7F50" stroke-width="2.5" />

        <!-- Forelegs and Paws -->
        <path d="M 330 260 L 320 370 L 345 370 L 360 270" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <ellipse cx="332" cy="370" rx="14" ry="7" fill="#FFD700" />

        <path d="M 270 265 L 260 365 L 285 365 L 295 270" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <ellipse cx="272" cy="365" rx="14" ry="7" fill="#FFD700" />

        <!-- Hind Legs -->
        <path d="M 160 210 Q 140 290 130 365 L 155 365 Q 170 300 190 240" fill="#FFEAA7" stroke="#F1C40F" stroke-width="2" />
        <ellipse cx="142" cy="365" rx="14" ry="7" fill="#FFD700" />

        <!-- Long Majestic Tail with Bushy Tuft at Denebola (45, 262) -->
        <path d="M 120 220 Q 70 170 45 262" fill="none" stroke="#FF7F50" stroke-width="5" stroke-linecap="round" />
        <circle cx="45" cy="262" r="16" fill="#FF7F50" stroke="#FFD700" stroke-width="2.5" filter="drop-shadow(0 0 10px #FF7F50)" />
      </g>
        """,

        "virgo": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Maiden Goddess Head at Zavijava (455, 179) -->
        <circle cx="440" cy="165" r="22" fill="#FFEAA7" fill-opacity="0.75" stroke="#FDA7DF" stroke-width="2" />
        <!-- Flowing Celestial Hair -->
        <path d="M 420 150 Q 455 120 465 160 Q 460 200 425 185 Z" fill="#F1C40F" fill-opacity="0.9" />
        <!-- Serene Face -->
        <circle cx="435" cy="162" r="3" fill="#060919" />
        <path d="M 430 172 Q 436 177 442 172" stroke="#D63031" stroke-width="1.5" fill="none" stroke-linecap="round" />

        <!-- Magnificent Angelic Wings (sweeping up to Vindemiatrix 253, 75) -->
        <path d="M 330 190 Q 290 100 253 75 Q 310 110 330 140 Q 360 80 410 70 Q 380 120 360 170 Z" 
              fill="#70A1FF" fill-opacity="0.45" stroke="#00F0FF" stroke-width="2.5" filter="drop-shadow(0 0 12px #00F0FF)" />
        <path d="M 330 190 Q 280 110 253 75 Q 260 120 290 160" stroke="#FFFFFF" stroke-width="1.5" fill="none" />

        <!-- Flowing Celestial Starlit Gown (from Porrima 311, 215 down to Feet 45, 267) -->
        <path d="M 425 185 L 311 215 L 272 161 L 162 192 L 188 325 L 45 267 L 54 315 L 140 360 L 280 340 Z" 
              fill="#9980FA" fill-opacity="0.4" stroke="#833471" stroke-width="2" />

        <!-- Glowing Radiant Wheat Sheaf at Spica (188, 325) -->
        <ellipse cx="188" cy="325" rx="28" ry="16" transform="rotate(-30 188 325)" fill="#FFD700" fill-opacity="0.8" stroke="#F1C40F" stroke-width="3" filter="drop-shadow(0 0 16px #FFD700)" />
        <path d="M 160 340 L 220 310 M 170 330 L 210 315 M 175 350 L 205 305" stroke="#FFA502" stroke-width="3" stroke-linecap="round" />
        <circle cx="188" cy="325" r="8" fill="#FFFFFF" />
        <text x="145" y="365" fill="#FFD700" font-size="11" font-weight="bold">🌾 รวงข้าวสาลี</text>
      </g>
        """,

        "libra": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Scale Diamond Body Framework -->
        <polygon points="275,85 395,150 350,265 155,290" fill="#FFA502" fill-opacity="0.15" stroke="#FFD700" stroke-width="2" stroke-dasharray="6,6" />

        <!-- Main Ornate Balance Beam (Top) -->
        <path d="M 100 185 L 410 95" stroke="#FFD700" stroke-width="8" stroke-linecap="round" filter="drop-shadow(0 0 10px #FFD700)" />
        <path d="M 100 185 L 410 95" stroke="#FFA502" stroke-width="4" stroke-linecap="round" />
        
        <!-- Central Fulcrum & Decorative Pillar at Star 2 (275, 85) -->
        <circle cx="260" cy="138" r="14" fill="#FFA502" stroke="#FFD700" stroke-width="3" filter="drop-shadow(0 0 8px #FFD700)" />
        <circle cx="260" cy="138" r="5" fill="#FFFFFF" />
        <!-- Vertical Balance Needle / Indicator -->
        <line x1="260" y1="138" x2="275" y2="85" stroke="#FFD700" stroke-width="5" stroke-linecap="round" />
        <line x1="260" y1="138" x2="295" y2="230" stroke="#FFD700" stroke-width="4" stroke-linecap="round" />

        <!-- Left Pan (Upper-Left at 100, 185) with 3 Hanging Chains -->
        <line x1="100" y1="185" x2="70" y2="245" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2,2" />
        <line x1="100" y1="185" x2="100" y2="250" stroke="#FFFFFF" stroke-width="2" />
        <line x1="100" y1="185" x2="130" y2="245" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2,2" />
        <!-- Left Pan 3D Dish -->
        <path d="M 60 245 Q 100 285 140 245 Z" fill="#FFA502" fill-opacity="0.75" stroke="#FFD700" stroke-width="3" filter="drop-shadow(0 0 8px #FFA502)" />
        <ellipse cx="100" cy="245" rx="40" ry="10" fill="#FFD700" fill-opacity="0.5" stroke="#FFD700" stroke-width="2" />
        <!-- Weight in Left Pan -->
        <circle cx="100" cy="240" r="8" fill="#00F0FF" stroke="#FFFFFF" stroke-width="1.5" />

        <!-- Right Pan (Lower-Left at Zubenelgenubi 155, 290) with 3 Hanging Chains -->
        <line x1="200" y1="210" x2="170" y2="295" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2,2" />
        <line x1="200" y1="210" x2="200" y2="300" stroke="#FFFFFF" stroke-width="2" />
        <line x1="200" y1="210" x2="230" y2="295" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2,2" />
        <!-- Right Pan 3D Dish -->
        <path d="M 160 295 Q 200 335 240 295 Z" fill="#FFA502" fill-opacity="0.75" stroke="#FFD700" stroke-width="3" filter="drop-shadow(0 0 8px #FFA502)" />
        <ellipse cx="200" cy="295" rx="40" ry="10" fill="#FFD700" fill-opacity="0.5" stroke="#FFD700" stroke-width="2" />
        <!-- Weight in Right Pan -->
        <circle cx="200" cy="290" r="8" fill="#00F0FF" stroke="#FFFFFF" stroke-width="1.5" />
      </g>
        """,

        "scorpio": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- 3 Front Sharp Pincer Claws spreading from Dschubba (396, 82) -->
        <path d="M 396 82 L 382 45 Q 420 20 410 65 Q 430 40 450 60 Z" fill="#FF4757" stroke="#FF6B81" stroke-width="2.5" />
        <path d="M 396 82 L 400 128 Q 440 120 445 150 Q 455 120 470 140 Z" fill="#FF4757" stroke="#FF6B81" stroke-width="2.5" />
        <path d="M 396 82 L 440 85 Q 470 80 460 105 Z" fill="#FF4757" stroke="#FF6B81" stroke-width="2" />

        <!-- Segmented Armored Body over Antares (316, 133) -->
        <ellipse cx="316" cy="133" rx="34" ry="24" fill="#D63031" fill-opacity="0.7" stroke="#FF4757" stroke-width="3" filter="drop-shadow(0 0 12px #D63031)" />
        <ellipse cx="280" cy="170" rx="26" ry="18" fill="#D63031" fill-opacity="0.7" stroke="#FF4757" stroke-width="2.5" />
        <ellipse cx="258" cy="237" rx="22" ry="16" fill="#D63031" fill-opacity="0.7" stroke="#FF4757" stroke-width="2.5" />

        <!-- Glowing Red Heart at Antares (316, 133) -->
        <circle cx="316" cy="133" r="16" fill="#FF0000" fill-opacity="0.5" filter="drop-shadow(0 0 14px #FF0000)" />
        <circle cx="316" cy="133" r="6" fill="#FFFFFF" />

        <!-- Walking Legs (4 pairs) -->
        <path d="M 330 115 Q 360 80 370 100" stroke="#FFA502" stroke-width="4" stroke-linecap="round" fill="none" />
        <path d="M 310 115 Q 330 60 345 85" stroke="#FFA502" stroke-width="4" stroke-linecap="round" fill="none" />
        <path d="M 290 150 Q 300 90 320 120" stroke="#FFA502" stroke-width="4" stroke-linecap="round" fill="none" />
        <path d="M 270 180 Q 280 120 300 150" stroke="#FFA502" stroke-width="4" stroke-linecap="round" fill="none" />

        <!-- J-Curve Segmented Tail curving to Stinger (139, 274) -->
        <path d="M 258 237 C 270 340, 230 400, 128 352 C 80 320, 100 260, 139 274" 
              fill="none" stroke="#D63031" stroke-width="16" stroke-linecap="round" filter="drop-shadow(0 0 10px rgba(214, 48, 49, 0.5))" />
        <path d="M 258 237 C 270 340, 230 400, 128 352 C 80 320, 100 260, 139 274" 
              fill="none" stroke="#FF7675" stroke-width="8" stroke-linecap="round" />

        <!-- Venom Bulb & Stinger Needle at Shaula & Lesath (139, 274 / 147, 276) -->
        <circle cx="139" cy="274" r="14" fill="#D63031" stroke="#FF4757" stroke-width="2.5" />
        <!-- Sharp Curved Needle Tip with Glowing Cyan Poison -->
        <path d="M 139 265 Q 165 240 170 225" stroke="#00F0FF" stroke-width="5" stroke-linecap="round" fill="none" filter="drop-shadow(0 0 10px #00F0FF)" />
        <circle cx="170" cy="225" r="4" fill="#FFFFFF" />
      </g>
        """,

        "sagittarius": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Recurve Bow (Aiming West / Right) -->
        <path d="M 370 115 Q 405 195 380 275" stroke="#FFD700" stroke-width="8" stroke-linecap="round" fill="none" filter="drop-shadow(0 0 12px #FFD700)" />
        <path d="M 370 115 Q 405 195 380 275" stroke="#FFA502" stroke-width="4" stroke-linecap="round" fill="none" />
        <!-- Bowstring pulled back to Nunki (250, 150) -->
        <line x1="370" y1="115" x2="250" y2="150" stroke="#FFFFFF" stroke-width="2" stroke-opacity="0.8" />
        <line x1="380" y1="275" x2="250" y2="150" stroke="#FFFFFF" stroke-width="2" stroke-opacity="0.8" />
        <!-- Golden Arrow -->
        <line x1="445" y1="215" x2="250" y2="150" stroke="#FFD700" stroke-width="4" stroke-linecap="round" filter="drop-shadow(0 0 8px #FFD700)" />
        <polygon points="445,215 425,205 425,225" fill="#FFD700" />

        <!-- Centaur Human Torso & Head (at Albaldah 220, 65) -->
        <circle cx="220" cy="65" r="20" fill="#FFEAA7" fill-opacity="0.8" stroke="#F1C40F" stroke-width="2" />
        <!-- Archer Helmet / Headband -->
        <path d="M 205 55 Q 220 40 235 55" stroke="#FFD700" stroke-width="4" fill="none" />
        <!-- Archer Eye & Face -->
        <circle cx="230" cy="62" r="2.5" fill="#060919" />
        <!-- Muscular Torso -->
        <path d="M 220 85 L 295 165 L 240 230 L 180 180 Z" fill="#E17055" fill-opacity="0.6" stroke="#D63031" stroke-width="2" />
        <!-- Flowing Royal Cape -->
        <path d="M 220 65 Q 150 40 130 95 Q 170 85 240 150 Z" fill="#70A1FF" fill-opacity="0.6" stroke="#1E90FF" stroke-width="2" filter="drop-shadow(0 0 8px #1E90FF)" />

        <!-- Horse Equine Body (Galloping to the right) -->
        <path d="M 180 180 Q 140 190 115 205 Q 120 280 170 350 L 235 360 Q 230 280 240 230 Z" 
              fill="#FFA502" fill-opacity="0.45" stroke="#FF7F50" stroke-width="3" />
        
        <!-- Horse Hind Legs & Hooves (Rukbat 170, 350 & Arkab 235, 360) -->
        <path d="M 150 240 L 170 350 L 185 350" stroke="#FFA502" stroke-width="8" stroke-linecap="round" />
        <rect x="165" y="345" width="20" height="12" rx="3" fill="#FFD700" />

        <path d="M 200 240 L 235 360 L 250 360" stroke="#FFA502" stroke-width="8" stroke-linecap="round" />
        <rect x="230" y="355" width="20" height="12" rx="3" fill="#FFD700" />

        <!-- Horse Front Legs & Hooves (Eta Sgr 340, 335 & Theta Sgr 380, 365) -->
        <path d="M 260 220 L 340 335 L 380 365" stroke="#FFA502" stroke-width="8" stroke-linecap="round" />
        <rect x="375" y="360" width="20" height="12" rx="3" fill="#FFD700" />

        <!-- Horse Tail -->
        <path d="M 115 205 Q 80 230 75 280" stroke="#FFEAA7" stroke-width="6" stroke-linecap="round" fill="none" />
      </g>
        """,

        "capricorn": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Goat Head (at Algedi & Dabih 441, 104) -->
        <circle cx="435" cy="115" r="26" fill="#FFEAA7" fill-opacity="0.8" stroke="#F1C40F" stroke-width="2.5" />
        <!-- Big Curved Goat Horns -->
        <path d="M 445 95 Q 470 50 490 70 Q 460 75 440 90" fill="#FFD700" stroke="#FFA502" stroke-width="2.5" filter="drop-shadow(0 0 8px #FFD700)" />
        <path d="M 430 95 Q 445 40 465 55 Q 440 65 425 90" fill="#FFD700" stroke="#FFA502" stroke-width="2" />
        <!-- Goat Eye & Beard -->
        <circle cx="445" cy="112" r="3" fill="#060919" />
        <path d="M 450 135 Q 465 155 450 160" stroke="#FFEAA7" stroke-width="4" stroke-linecap="round" fill="none" />

        <!-- Goat Front Legs & Hooves -->
        <path d="M 400 160 L 420 230 L 435 230" stroke="#FFEAA7" stroke-width="7" stroke-linecap="round" />
        <rect x="420" y="225" width="16" height="10" rx="3" fill="#FFD700" />
        <path d="M 370 170 L 380 240 L 395 240" stroke="#FFEAA7" stroke-width="7" stroke-linecap="round" />
        <rect x="380" y="235" width="16" height="10" rx="3" fill="#FFD700" />

        <!-- Sea-Goat Hull & Curved Fish Tail (from 348, 340 curving up to Deneb Algedi 45, 130) -->
        <path d="M 410 140 Q 360 220 300 330 Q 200 340 140 252 Q 90 200 45 130 Q 110 130 160 144 Q 260 150 350 140 Z" 
              fill="#1DD1A1" fill-opacity="0.45" stroke="#10AC84" stroke-width="3" filter="drop-shadow(0 0 12px rgba(29, 209, 161, 0.4))" />
        
        <!-- Fish Scales Texture -->
        <path d="M 280 270 Q 260 250 240 270 M 240 250 Q 220 230 200 250 M 190 220 Q 170 200 150 220" 
              stroke="#FFFFFF" stroke-width="2" fill="none" opacity="0.6" />

        <!-- Wide Spreading Fish Tail Fin at Deneb Algedi (45, 130) & Nashira (77, 140) -->
        <path d="M 45 130 Q 10 90 20 60 Q 45 110 50 130 Q 35 150 15 180 Q 35 150 77 140 Z" 
              fill="#1DD1A1" fill-opacity="0.8" stroke="#10AC84" stroke-width="2.5" filter="drop-shadow(0 0 10px #1DD1A1)" />
      </g>
        """,

        "aquarius": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Youthful Water Bearer (Ganymede) Kneeling Profile -->
        <circle cx="340" cy="80" r="22" fill="#FFEAA7" fill-opacity="0.8" stroke="#F1C40F" stroke-width="2" />
        <!-- Headband & Hair -->
        <path d="M 320 70 Q 340 55 360 70" stroke="#F1C40F" stroke-width="4" fill="none" />
        <circle cx="348" cy="78" r="3" fill="#060919" />

        <!-- Raised Right Arm reaching high to 98 Aqr (430, 55) -->
        <path d="M 340 80 L 430 55" stroke="#FFEAA7" stroke-width="8" stroke-linecap="round" />
        <circle cx="430" cy="55" r="6" fill="#FFD700" />

        <!-- Torso & Grecian Tunic -->
        <polygon points="335,125 245,175 265,270 385,205" fill="#70A1FF" fill-opacity="0.5" stroke="#1E90FF" stroke-width="2" />
        
        <!-- Kneeling Legs -->
        <path d="M 265 270 L 220 335 L 235 380" stroke="#FFEAA7" stroke-width="8" stroke-linecap="round" />
        <path d="M 265 270 L 320 350" stroke="#FFEAA7" stroke-width="8" stroke-linecap="round" />

        <!-- Large Classical Amphora / Water Urn at (175, 180) -->
        <ellipse cx="180" cy="180" rx="26" ry="36" transform="rotate(-35 180 180)" fill="#E17055" fill-opacity="0.8" stroke="#D63031" stroke-width="3" filter="drop-shadow(0 0 10px #E17055)" />
        <ellipse cx="160" cy="165" rx="14" ry="8" transform="rotate(-35 160 165)" fill="#2D3436" stroke="#FFD700" stroke-width="2" />
        <!-- Urn Handle -->
        <path d="M 195 160 Q 220 180 190 205" stroke="#D63031" stroke-width="4" fill="none" />

        <!-- Cascading Luminous Ribbons of Flowing Water (175, 180 -> 235, 380) -->
        <path d="M 155 165 C 130 220, 140 260, 155 260 C 170 290, 175 320, 185 320 C 205 345, 215 360, 235 380" 
              fill="none" stroke="#00F0FF" stroke-width="12" stroke-linecap="round" opacity="0.8" filter="drop-shadow(0 0 14px #00F0FF)" />
        <path d="M 155 165 C 130 220, 140 260, 155 260 C 170 290, 175 320, 185 320 C 205 345, 215 360, 235 380" 
              fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity="0.9" />

        <!-- Sparkling Pool Splash at Bottom (88 Aqr 235, 380) -->
        <ellipse cx="235" cy="380" rx="55" ry="16" fill="#00F0FF" fill-opacity="0.4" stroke="#00F0FF" stroke-width="2.5" filter="drop-shadow(0 0 14px #00F0FF)" />
        <circle cx="200" cy="395" r="6" fill="#FFFFFF" filter="drop-shadow(0 0 6px #00F0FF)" />
        <circle cx="270" cy="390" r="6" fill="#FFFFFF" filter="drop-shadow(0 0 6px #00F0FF)" />
        <circle cx="235" cy="360" r="4" fill="#00F0FF" />
        <circle cx="250" cy="350" r="3" fill="#FFFFFF" />
      </g>
        """,

        "pisces": """
      <g class="overlay-graphic" opacity="0.95">
        <!-- Northern Celestial Fish (Swimming North/Up at 405, 65) -->
        <g stroke="#55EFC4" stroke-width="2.5" fill="none">
          <ellipse cx="405" cy="110" rx="45" ry="24" transform="rotate(75 405 110)" fill="#55EFC4" fill-opacity="0.5" stroke="#1DD1A1" stroke-width="3" filter="drop-shadow(0 0 12px #1DD1A1)" />
          <!-- Fish Head & Mouth -->
          <polygon points="405,65 388,40 422,40" fill="#1DD1A1" opacity="0.85" />
          <!-- Eye -->
          <circle cx="405" cy="72" r="4" fill="#060919" /><circle cx="406" cy="70" r="1.5" fill="#FFFFFF" />
          <!-- Gills & Scales -->
          <path d="M 390 95 Q 405 105 420 95" stroke="#FFFFFF" stroke-width="1.5" opacity="0.7" />
          <path d="M 390 115 Q 405 125 420 115" stroke="#FFFFFF" stroke-width="1.5" opacity="0.7" />
          <!-- Side Fins -->
          <path d="M 380 95 Q 355 105 375 125 Z" fill="#1DD1A1" opacity="0.7" />
          <path d="M 430 95 Q 455 105 435 125 Z" fill="#1DD1A1" opacity="0.7" />
          <!-- Tail Fin at Upsilon Psc (430, 155) -->
          <path d="M 405 150 Q 375 185 390 195 Q 405 170 420 195 Q 435 185 405 150 Z" fill="#1DD1A1" fill-opacity="0.8" stroke="#1DD1A1" stroke-width="2" />
        </g>

        <!-- Western Celestial Fish (Swimming West/Left at 125, 240) -->
        <g stroke="#FF6B81" stroke-width="2.5" fill="none">
          <ellipse cx="190" cy="250" rx="60" ry="28" fill="#FF6B81" fill-opacity="0.5" stroke="#FF4757" stroke-width="3" filter="drop-shadow(0 0 12px #FF4757)" />
          <!-- Fish Head & Mouth (at 7 Psc 125, 240) -->
          <polygon points="125,240 98,225 98,255" fill="#FF4757" opacity="0.85" />
          <!-- Eye -->
          <circle cx="138" cy="238" r="4" fill="#060919" /><circle cx="139" cy="236" r="1.5" fill="#FFFFFF" />
          <!-- Gills & Scales -->
          <path d="M 160 235 Q 170 250 160 265" stroke="#FFFFFF" stroke-width="1.5" opacity="0.7" />
          <path d="M 180 235 Q 190 250 180 265" stroke="#FFFFFF" stroke-width="1.5" opacity="0.7" />
          <!-- Dorsal and Ventral Fins -->
          <path d="M 175 222 Q 200 200 215 225 Z" fill="#FF4757" opacity="0.7" />
          <path d="M 175 278 Q 200 300 215 275 Z" fill="#FF4757" opacity="0.7" />
          <!-- Tail Fin at TX Psc (260, 255) -->
          <path d="M 245 250 Q 280 220 290 235 Q 265 250 290 265 Q 280 280 245 250 Z" fill="#FF4757" fill-opacity="0.8" stroke="#FF4757" stroke-width="2" />
        </g>

        <!-- Shimmering Golden Ribbon / Cord Connecting Both Fish -->
        <!-- North Fish Cord (405, 170 -> Alrescha 320, 385) -->
        <path d="M 405 170 C 375 220, 355 265, 345 320 C 340 360, 335 375, 320 385" 
              fill="none" stroke="#FFD700" stroke-width="5" stroke-linecap="round" opacity="0.85" filter="drop-shadow(0 0 8px #FFD700)" />
        <!-- West Fish Cord (260, 255 -> Alrescha 320, 385) -->
        <path d="M 260 255 C 250 300, 265 330, 290 365 C 300 375, 310 380, 320 385" 
              fill="none" stroke="#FFD700" stroke-width="5" stroke-linecap="round" opacity="0.85" filter="drop-shadow(0 0 8px #FFD700)" />

        <!-- Golden Tied Ribbon Knot with Shimmering Bow at Alrescha (320, 385) -->
        <circle cx="320" cy="385" r="14" fill="#FFD700" stroke="#FFA502" stroke-width="3" filter="drop-shadow(0 0 14px #FFD700)" />
        <path d="M 320 385 Q 300 365 305 385 Q 310 395 320 385 Q 340 365 335 385 Q 330 395 320 385 Z" fill="#FFA502" stroke="#FFD700" stroke-width="1.5" />
        <circle cx="320" cy="385" r="5" fill="#FFFFFF" />
      </g>
        """
    }

print("Overlay definitions ready.")
