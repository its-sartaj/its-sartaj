import os
import base64
import xml.etree.ElementTree as ET

def get_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

frames_b64 = [get_b64(f'assets/frames/frame_{i}.jpg') for i in range(8)]
b64_avatar = get_b64('assets/badge_avatar_opt.png')
b64_footer = get_b64('assets/footer_character_opt.png')

SHARED_DEFS = '''
    <linearGradient id="auroraGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22d3ee"/>
      <stop offset="50%" stop-color="#a78bfa"/>
      <stop offset="100%" stop-color="#f472b6"/>
    </linearGradient>

    <linearGradient id="auroraBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#f472b6" stop-opacity="0.45"/>
    </linearGradient>

    <pattern id="dotPattern" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.8" fill="#22d3ee" fill-opacity="0.08"/>
    </pattern>

    <filter id="auroraGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
'''

# ==============================================================================
# 1. HERO.SVG
# ==============================================================================
hero_frames_smil = f'''
    <!-- Video Frames with SMIL Switching (4s total loop, holds frame 7 for ~1.4s, fades, repeats) -->
    <image href="data:image/jpeg;base64,{frames_b64[0]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="1; 1; 0; 0" keyTimes="0; 0.06; 0.07; 1" />
    </image>
    <image href="data:image/jpeg;base64,{frames_b64[1]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0; 0; 1; 1; 0; 0" keyTimes="0; 0.06; 0.07; 0.13; 0.14; 1" />
    </image>
    <image href="data:image/jpeg;base64,{frames_b64[2]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0; 0; 1; 1; 0; 0" keyTimes="0; 0.13; 0.14; 0.20; 0.21; 1" />
    </image>
    <image href="data:image/jpeg;base64,{frames_b64[3]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0; 0; 1; 1; 0; 0" keyTimes="0; 0.20; 0.21; 0.27; 0.28; 1" />
    </image>
    <image href="data:image/jpeg;base64,{frames_b64[4]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0; 0; 1; 1; 0; 0" keyTimes="0; 0.27; 0.28; 0.35; 0.36; 1" />
    </image>
    <image href="data:image/jpeg;base64,{frames_b64[5]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0; 0; 1; 1; 0; 0" keyTimes="0; 0.35; 0.36; 0.43; 0.44; 1" />
    </image>
    <image href="data:image/jpeg;base64,{frames_b64[6]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0; 0; 1; 1; 0; 0" keyTimes="0; 0.43; 0.44; 0.52; 0.53; 1" />
    </image>
    <!-- Frame 7 holds until 3.65s, fades out by 3.95s, repeats -->
    <image href="data:image/jpeg;base64,{frames_b64[7]}" x="0" y="0" width="340" height="340" preserveAspectRatio="xMidYMid slice" mask="url(#videoFeatherMask)">
      <animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0; 0; 1; 1; 0; 0" keyTimes="0; 0.52; 0.53; 0.92; 0.98; 1" />
    </image>
'''

hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%" style="background: #0d0e16; border-radius: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;">
  <defs>
    {SHARED_DEFS}

    <!-- Video Feather Edge Mask (melts video into background) -->
    <mask id="videoFeatherMask">
      <radialGradient id="featherGrad" cx="50%" cy="50%" r="50%">
        <stop offset="68%" stop-color="#ffffff"/>
        <stop offset="98%" stop-color="#000000"/>
      </radialGradient>
      <rect width="340" height="340" fill="url(#featherGrad)"/>
    </mask>

    <!-- Rising Reveal Mask for Name -->
    <mask id="nameRevealMask">
      <rect x="0" y="0" width="400" height="80" fill="#ffffff">
        <animate attributeName="y" values="80; 0" dur="1.2s" fill="freeze" keyTimes="0; 1" calcMode="spline" keySplines="0.16 1 0.3 1" />
      </rect>
    </mask>
  </defs>

  <style>
    @keyframes recDotBlink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.15; }}
    }}
    @keyframes drawBracketsAnim {{
      0% {{ stroke-dashoffset: 80; }}
      100% {{ stroke-dashoffset: 0; }}
    }}
    @keyframes scrubberAnim {{
      0% {{ width: 0px; }}
      92% {{ width: 310px; }}
      100% {{ width: 310px; opacity: 0; }}
    }}
    @keyframes cursorBlink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}
    @keyframes pulseCollab {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.4); opacity: 0.4; }}
    }}

    @keyframes roleCycle1 {{
      0%, 22% {{ opacity: 1; transform: translateY(0px); }}
      25%, 100% {{ opacity: 0; transform: translateY(10px); }}
    }}
    @keyframes roleCycle2 {{
      0%, 24% {{ opacity: 0; transform: translateY(-10px); }}
      26%, 47% {{ opacity: 1; transform: translateY(0px); }}
      50%, 100% {{ opacity: 0; transform: translateY(10px); }}
    }}
    @keyframes roleCycle3 {{
      0%, 49% {{ opacity: 0; transform: translateY(-10px); }}
      51%, 72% {{ opacity: 1; transform: translateY(0px); }}
      75%, 100% {{ opacity: 0; transform: translateY(10px); }}
    }}
    @keyframes roleCycle4 {{
      0%, 74% {{ opacity: 0; transform: translateY(-10px); }}
      76%, 97% {{ opacity: 1; transform: translateY(0px); }}
      100% {{ opacity: 0; transform: translateY(10px); }}
    }}

    .rec-blink {{ animation: recDotBlink 1s infinite ease-in-out; }}
    .bracket-draw {{ stroke-dasharray: 80; animation: drawBracketsAnim 1.6s cubic-bezier(0.16, 1, 0.3, 1) forwards; }}
    .scrub-bar {{ animation: scrubberAnim 4s linear infinite; }}
    .cursor-flash {{ animation: cursorBlink 0.8s infinite; }}
    .pulse-dot {{ transform-origin: center; animation: pulseCollab 2s infinite ease-in-out; }}

    .role-text-1 {{ animation: roleCycle1 8s infinite; }}
    .role-text-2 {{ animation: roleCycle2 8s infinite; }}
    .role-text-3 {{ animation: roleCycle3 8s infinite; }}
    .role-text-4 {{ animation: roleCycle4 8s infinite; }}
  </style>

  <!-- Background Base & Dot Texture -->
  <rect width="900" height="480" rx="16" fill="#0d0e16" />
  <rect width="900" height="480" rx="16" fill="url(#dotPattern)" />
  <rect width="900" height="480" rx="16" fill="none" stroke="url(#auroraBorder)" stroke-width="1.2" />

  <!-- Ambient Glow Blobs -->
  <circle cx="200" cy="180" r="140" fill="#22d3ee" opacity="0.06" filter="url(#auroraGlow)"/>
  <circle cx="680" cy="220" r="160" fill="#a78bfa" opacity="0.07" filter="url(#auroraGlow)"/>

  <!-- ==================== LEFT COLUMN: INTRO & BIO ==================== -->
  <g transform="translate(45, 45)">
    <g>
      <rect width="180" height="26" rx="13" fill="rgba(16, 185, 129, 0.12)" stroke="rgba(16, 185, 129, 0.35)" stroke-width="1" />
      <circle class="pulse-dot" cx="13" cy="13" r="4.5" fill="#10b981" />
      <text x="24" y="17" fill="#34d399" font-size="10.5" font-weight="700" letter-spacing="0.5">OPEN TO COLLABS</text>
    </g>

    <!-- Typed "Hi there, I'm" -->
    <g transform="translate(0, 52)">
      <text fill="#94a3b8" font-size="14.5" font-weight="500" letter-spacing="1">Hi there, I'm<tspan class="cursor-flash" fill="#22d3ee"> |</tspan></text>
    </g>

    <!-- Name in big animated aurora gradient revealed by rising mask -->
    <g transform="translate(0, 72)" mask="url(#nameRevealMask)">
      <text x="0" y="52" fill="url(#auroraGrad)" font-size="52" font-weight="900" letter-spacing="1.5" filter="url(#auroraGlow)">SARTAJ</text>
    </g>

    <!-- Cycling Role Lines -->
    <g transform="translate(0, 145)">
      <rect width="395" height="34" rx="6" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(34, 211, 238, 0.2)" stroke-width="0.8" />
      <text x="12" y="22" fill="#22d3ee" font-size="13" font-family="monospace" font-weight="bold">&gt;</text>
      
      <g class="role-text-1">
        <text x="28" y="22" fill="#f8fafc" font-size="12.5" font-weight="700">🚀 Full-Stack Web Developer &amp; Engineer</text>
      </g>
      <g class="role-text-2">
        <text x="28" y="22" fill="#22d3ee" font-size="12.5" font-weight="700">⚛️ React 19 &amp; TypeScript Specialist</text>
      </g>
      <g class="role-text-3">
        <text x="28" y="22" fill="#a78bfa" font-size="12.5" font-weight="700">🏪 Digital Retail POS &amp; Cloud Architect</text>
      </g>
      <g class="role-text-4">
        <text x="28" y="22" fill="#f472b6" font-size="12.5" font-weight="700">🛡️ Linux, Cybersecurity &amp; Systems</text>
      </g>
    </g>

    <!-- One-line pitch -->
    <g transform="translate(0, 198)">
      <text fill="#cbd5e1" font-size="13" font-weight="400">
        <tspan x="0" dy="0">Building high-performance web systems, cloud POS platforms</tspan>
        <tspan x="0" dy="19">&amp; AI-integrated experiences with modern architecture.</tspan>
      </text>
    </g>

    <!-- Meta Row with small drawn icons -->
    <g transform="translate(0, 260)">
      <g transform="translate(0, 0)">
        <path d="M 6 0 C 2.7 0, 0 2.7, 0 6 C 0 10.5, 6 15, 6 15 C 6 15, 12 10.5, 12 6 C 12 2.7, 9.3 0, 6 0 Z M 6 8 C 4.9 8, 4 7.1, 4 6 C 4 4.9, 4.9 4, 6 4 C 7.1 4, 8 4.9, 8 6 C 8 7.1, 7.1 8, 6 8 Z" fill="#22d3ee" />
        <text x="18" y="12" fill="#94a3b8" font-size="11.5" font-weight="500">Delhi, India</text>
      </g>
      <g transform="translate(115, 0)">
        <path d="M 12 4 L 9 4 L 9 2 C 9 0.9, 8.1 0, 7 0 L 5 0 C 3.9 0, 3 0.9, 3 2 L 3 4 L 0 4 C 0 4.5, 0 11, 0 11 C 0 12.1, 0.9 13, 2 13 L 10 13 C 11.1 13, 12 12.1, 12 11 L 12 4 Z M 5 2 L 7 2 L 7 4 L 5 4 L 5 2 Z" fill="#a78bfa" />
        <text x="18" y="12" fill="#94a3b8" font-size="11.5" font-weight="500">Open for Hire</text>
      </g>
      <g transform="translate(235, 0)">
        <polygon points="6,0 7.8,4.2 12.4,4.6 8.9,7.6 10,12.1 6,9.6 2,12.1 3.1,7.6 -0.4,4.6 4.2,4.2" fill="#f472b6" />
        <text x="18" y="12" fill="#94a3b8" font-size="11.5" font-weight="500">12+ Production Repos</text>
      </g>
    </g>

    <!-- Buttons -->
    <g transform="translate(0, 310)">
      <rect width="185" height="36" rx="18" fill="url(#auroraGrad)" />
      <text x="92" y="23" fill="#0d0e16" font-size="12" font-weight="800" text-anchor="middle">VIEW PORTFOLIO 🚀</text>

      <rect x="200" width="185" height="36" rx="18" fill="rgba(34, 211, 238, 0.1)" stroke="rgba(34, 211, 238, 0.35)" stroke-width="1.2" />
      <text x="292" y="23" fill="#22d3ee" font-size="12" font-weight="700" text-anchor="middle">GET IN TOUCH 📬</text>
    </g>
  </g>

  <!-- ==================== RIGHT COLUMN: CAMERA VIEWFINDER VIDEO ==================== -->
  <g transform="translate(495, 45)">
    <rect width="360" height="390" rx="14" fill="#090a10" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" />

    <g transform="translate(10, 25)">
      {hero_frames_smil}
    </g>

    <!-- Corner brackets that draw in -->
    <g fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round">
      <path class="bracket-draw" d="M 30 50 L 30 30 L 50 30" />
      <path class="bracket-draw" d="M 330 50 L 330 30 L 310 30" />
      <path class="bracket-draw" d="M 30 340 L 30 360 L 50 360" />
      <path class="bracket-draw" d="M 330 340 L 330 360 L 310 360" />
    </g>

    <!-- Top Viewfinder Header HUD -->
    <g transform="translate(25, 22)">
      <circle class="rec-blink" cx="8" cy="8" r="5" fill="#ef4444" filter="url(#auroraGlow)" />
      <text x="20" y="12" fill="#ef4444" font-size="10.5" font-family="monospace" font-weight="bold" letter-spacing="1">REC</text>
      <text x="65" y="12" fill="#cbd5e1" font-size="10" font-family="monospace">sartaj_wave.mov [RAW]</text>
      <text x="310" y="12" fill="#22d3ee" font-size="9.5" font-family="monospace" text-anchor="end">4K 60FPS</text>
    </g>

    <!-- Center Reticle -->
    <g transform="translate(180, 195)" stroke="rgba(34, 211, 238, 0.4)" stroke-width="1.2">
      <circle cx="0" cy="0" r="16" fill="none" stroke-dasharray="4 4" />
      <line x1="-8" y1="0" x2="8" y2="0" />
      <line x1="0" y1="-8" x2="0" y2="8" />
    </g>

    <!-- Bottom Scrubber Bar -->
    <g transform="translate(25, 368)">
      <rect width="310" height="3" rx="1.5" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="scrub-bar" width="0" height="3" rx="1.5" fill="url(#auroraGrad)" />
      <text x="0" y="-8" fill="#94a3b8" font-size="9" font-family="monospace">00:00:02.14 / 00:00:04.00</text>
      <text x="310" y="-8" fill="#34d399" font-size="9" font-family="monospace" text-anchor="end">BUFFER 100%</text>
    </g>
  </g>
</svg>'''

with open('hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
with open('assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)

print("hero.svg written.")

# ==============================================================================
# 2. ABOUT-LIFE.SVG
# ==============================================================================
about_life_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%" style="background: #0d0e16; border-radius: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    {SHARED_DEFS}

    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(22, 27, 46, 0.75)"/>
      <stop offset="100%" stop-color="rgba(13, 14, 22, 0.85)"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes urlCursor {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    @keyframes seg1 {{ 0% {{ width: 0px; }} 25%, 100% {{ width: 92px; }} }}
    @keyframes seg2 {{ 0%, 25% {{ width: 0px; }} 50%, 100% {{ width: 92px; }} }}
    @keyframes seg3 {{ 0%, 50% {{ width: 0px; }} 75%, 100% {{ width: 92px; }} }}
    @keyframes seg4 {{ 0%, 75% {{ width: 0px; }} 100% {{ width: 92px; }} }}

    @keyframes slide1Fade {{
      0%, 22% {{ opacity: 1; transform: translateY(0px); }}
      25%, 98% {{ opacity: 0; transform: translateY(8px); }}
      100% {{ opacity: 1; transform: translateY(0px); }}
    }}
    @keyframes slide2Fade {{
      0%, 24% {{ opacity: 0; transform: translateY(-8px); }}
      26%, 47% {{ opacity: 1; transform: translateY(0px); }}
      50%, 100% {{ opacity: 0; transform: translateY(8px); }}
    }}
    @keyframes slide3Fade {{
      0%, 49% {{ opacity: 0; transform: translateY(-8px); }}
      51%, 72% {{ opacity: 1; transform: translateY(0px); }}
      75%, 100% {{ opacity: 0; transform: translateY(8px); }}
    }}
    @keyframes slide4Fade {{
      0%, 74% {{ opacity: 0; transform: translateY(-8px); }}
      76%, 97% {{ opacity: 1; transform: translateY(0px); }}
      100% {{ opacity: 0; transform: translateY(8px); }}
    }}

    @keyframes ringFill1 {{ 0% {{ stroke-dashoffset: 264; }} 50%, 100% {{ stroke-dashoffset: 45; }} }}
    @keyframes ringFill2 {{ 0% {{ stroke-dashoffset: 188; }} 50%, 100% {{ stroke-dashoffset: 35; }} }}
    @keyframes ringFill3 {{ 0% {{ stroke-dashoffset: 113; }} 50%, 100% {{ stroke-dashoffset: 20; }} }}

    .cursor-blink {{ animation: urlCursor 0.8s infinite; }}
    .bar-seg-1 {{ animation: seg1 16s infinite linear; }}
    .bar-seg-2 {{ animation: seg2 16s infinite linear; }}
    .bar-seg-3 {{ animation: seg3 16s infinite linear; }}
    .bar-seg-4 {{ animation: seg4 16s infinite linear; }}

    .c-slide-1 {{ animation: slide1Fade 16s infinite; }}
    .c-slide-2 {{ animation: slide2Fade 16s infinite; }}
    .c-slide-3 {{ animation: slide3Fade 16s infinite; }}
    .c-slide-4 {{ animation: slide4Fade 16s infinite; }}

    .ring-1 {{ stroke-dasharray: 264; animation: ringFill1 6s ease-in-out infinite alternate; }}
    .ring-2 {{ stroke-dasharray: 188; animation: ringFill2 6s ease-in-out infinite alternate; }}
    .ring-3 {{ stroke-dasharray: 113; animation: ringFill3 6s ease-in-out infinite alternate; }}
  </style>

  <rect width="900" height="460" rx="16" fill="#0d0e16" />
  <rect width="900" height="460" rx="16" fill="url(#dotPattern)" />
  <rect width="900" height="460" rx="16" fill="none" stroke="url(#auroraBorder)" stroke-width="1.2" />

  <!-- LEFT CARD: FAKE BROWSER & CAPABILITIES -->
  <g transform="translate(25, 25)">
    <rect width="415" height="410" rx="14" fill="rgba(18, 22, 38, 0.75)" stroke="url(#auroraBorder)" stroke-width="1" />
    
    <rect width="415" height="38" rx="14" fill="rgba(13, 14, 22, 0.9)" />
    <circle cx="20" cy="19" r="4.5" fill="#ef4444" />
    <circle cx="35" cy="19" r="4.5" fill="#f59e0b" />
    <circle cx="50" cy="19" r="4.5" fill="#10b981" />
    
    <rect x="70" y="8" width="330" height="22" rx="6" fill="rgba(255, 255, 255, 0.05)" stroke="rgba(34, 211, 238, 0.25)" stroke-width="0.8" />
    <text x="82" y="23" fill="#22d3ee" font-size="10" font-family="monospace">🔒 https://sartaj.dev/capabilities<tspan class="cursor-blink" fill="#f472b6">|</tspan></text>

    <!-- Mini Terminal Illustration -->
    <g transform="translate(15, 48)">
      <rect width="385" height="85" rx="8" fill="rgba(9, 10, 16, 0.9)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="0.8" />
      <text x="14" y="24" fill="#a78bfa" font-size="11" font-family="monospace">const engineer = new FullStackArchitect(&#123;</text>
      <text x="28" y="44" fill="#cbd5e1" font-size="11" font-family="monospace">frontend: [&quot;React 19&quot;, &quot;TypeScript&quot;, &quot;Tailwind v4&quot;],</text>
      <text x="28" y="62" fill="#22d3ee" font-size="11" font-family="monospace">impact: &quot;Real-World POS Billing, Cloud Sync &amp; AI Tools&quot;</text>
      <text x="14" y="78" fill="#a78bfa" font-size="11" font-family="monospace">&#125;);</text>
    </g>

    <!-- 3 Capability Rows with Icon Tiles -->
    <g transform="translate(15, 145)">
      <!-- Capability 1 -->
      <g transform="translate(0, 0)">
        <rect width="385" height="76" rx="10" fill="url(#cardGrad)" stroke="rgba(34, 211, 238, 0.25)" stroke-width="1" />
        <rect x="12" y="14" width="48" height="48" rx="8" fill="rgba(34, 211, 238, 0.12)" stroke="#22d3ee" stroke-width="1" />
        <text x="36" y="44" font-size="22" text-anchor="middle">🏪</text>
        <text x="70" y="32" fill="#22d3ee" font-size="13" font-weight="700">Digital Commerce &amp; POS Systems</text>
        <text x="70" y="50" fill="#cbd5e1" font-size="11">Production billing, GST Hindi invoice words, dynamic UPI QR,</text>
        <text x="70" y="64" fill="#94a3b8" font-size="10.5">real-time stock limits &amp; 1-click WhatsApp customer ordering.</text>
      </g>
      <!-- Capability 2 -->
      <g transform="translate(0, 86)">
        <rect width="385" height="76" rx="10" fill="url(#cardGrad)" stroke="rgba(167, 139, 250, 0.25)" stroke-width="1" />
        <rect x="12" y="14" width="48" height="48" rx="8" fill="rgba(167, 139, 250, 0.12)" stroke="#a78bfa" stroke-width="1" />
        <text x="36" y="44" font-size="22" text-anchor="middle">⚛️</text>
        <text x="70" y="32" fill="#a78bfa" font-size="13" font-weight="700">High-Performance Web Frontends</text>
        <text x="70" y="50" fill="#cbd5e1" font-size="11">Engineered with React 19, TypeScript, Tailwind v4 &amp; Vite.</text>
        <text x="70" y="64" fill="#94a3b8" font-size="10.5">Fluid motion choreography, type safety &amp; instant zero jank.</text>
      </g>
      <!-- Capability 3 -->
      <g transform="translate(0, 172)">
        <rect width="385" height="76" rx="10" fill="url(#cardGrad)" stroke="rgba(244, 114, 182, 0.25)" stroke-width="1" />
        <rect x="12" y="14" width="48" height="48" rx="8" fill="rgba(244, 114, 182, 0.12)" stroke="#f472b6" stroke-width="1" />
        <text x="36" y="44" font-size="22" text-anchor="middle">🤖</text>
        <text x="70" y="32" fill="#f472b6" font-size="13" font-weight="700">AI Integration &amp; Cloud Security</text>
        <text x="70" y="50" fill="#cbd5e1" font-size="11">Google Gemini AI APIs, Node.js, Express &amp; Firebase Cloud DB.</text>
        <text x="70" y="64" fill="#94a3b8" font-size="10.5">Hardened Linux administration, network audits &amp; defense.</text>
      </g>
    </g>
  </g>

  <!-- RIGHT CARD: HOBBIES CAROUSEL & DAILY RINGS -->
  <g transform="translate(460, 25)">
    <rect width="415" height="410" rx="14" fill="rgba(18, 22, 38, 0.75)" stroke="url(#auroraBorder)" stroke-width="1" />

    <rect width="415" height="38" rx="14" fill="rgba(13, 14, 22, 0.9)" />
    <circle cx="20" cy="19" r="4.5" fill="#f472b6" />
    <text x="34" y="23" fill="#f8fafc" font-size="12.5" font-weight="700">HOBBIES CAROUSEL &amp; DAILY RINGS</text>
    <rect x="300" y="8" width="100" height="22" rx="11" fill="rgba(244, 114, 182, 0.15)" stroke="#f472b6" stroke-width="0.8" />
    <text x="350" y="22" fill="#f472b6" font-size="9.5" font-family="monospace" font-weight="bold" text-anchor="middle">AUTO-CYCLE</text>

    <!-- Segment Progress Bars -->
    <g transform="translate(15, 48)">
      <rect x="0" y="0" width="92" height="3.5" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="bar-seg-1" x="0" y="0" width="0" height="3.5" rx="2" fill="#22d3ee" />

      <rect x="98" y="0" width="92" height="3.5" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="bar-seg-2" x="98" y="0" width="0" height="3.5" rx="2" fill="#a78bfa" />

      <rect x="196" y="0" width="92" height="3.5" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="bar-seg-3" x="196" y="0" width="0" height="3.5" rx="2" fill="#f472b6" />

      <rect x="294" y="0" width="92" height="3.5" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="bar-seg-4" x="294" y="0" width="0" height="3.5" rx="2" fill="#38bdf8" />
    </g>

    <!-- HOBBY CAROUSEL SLIDES -->
    <g class="c-slide-1" transform="translate(15, 65)">
      <rect width="385" height="185" rx="10" fill="url(#cardGrad)" stroke="rgba(34, 211, 238, 0.25)" stroke-width="1" />
      <text x="20" y="38" font-size="28">☕</text>
      <text x="65" y="32" fill="#22d3ee" font-size="14.5" font-weight="800">Specialty Dark Roast Coffee</text>
      <text x="65" y="48" fill="#94a3b8" font-size="11">Midnight Brewing &amp; Code Refactoring</text>
      <text x="20" y="85" fill="#f8fafc" font-size="12.5" font-weight="600">The Caption:</text>
      <text x="20" y="105" fill="#cbd5e1" font-size="11.5">Pour-over brews fueling zero-bug midnight release sprints.</text>
      <text x="20" y="123" fill="#cbd5e1" font-size="11.5">Extracting peak aroma while untangling recursive state trees.</text>
      <rect x="20" y="142" width="105" height="22" rx="11" fill="rgba(34, 211, 238, 0.15)" />
      <text x="72" y="157" fill="#22d3ee" font-size="10" font-weight="700" text-anchor="middle">#DarkRoast</text>
      <rect x="135" y="142" width="115" height="22" rx="11" fill="rgba(34, 211, 238, 0.15)" />
      <text x="192" y="157" fill="#22d3ee" font-size="10" font-weight="700" text-anchor="middle">#MidnightCoder</text>
    </g>

    <g class="c-slide-2" transform="translate(15, 65)">
      <rect width="385" height="185" rx="10" fill="url(#cardGrad)" stroke="rgba(167, 139, 250, 0.25)" stroke-width="1" />
      <text x="20" y="38" font-size="28">🛡️</text>
      <text x="65" y="32" fill="#a78bfa" font-size="14.5" font-weight="800">Cybersecurity Labs &amp; CTFs</text>
      <text x="65" y="48" fill="#94a3b8" font-size="11">Ethical Hacking &amp; Network Defense</text>
      <text x="20" y="85" fill="#f8fafc" font-size="12.5" font-weight="600">The Caption:</text>
      <text x="20" y="105" fill="#cbd5e1" font-size="11.5">Ethical hacking, Kali Linux &amp; network vulnerability auditing.</text>
      <text x="20" y="123" fill="#cbd5e1" font-size="11.5">Penetration testing web targets so data never leaks.</text>
      <rect x="20" y="142" width="105" height="22" rx="11" fill="rgba(167, 139, 250, 0.15)" />
      <text x="72" y="157" fill="#a78bfa" font-size="10" font-weight="700" text-anchor="middle">#KaliLinux</text>
      <rect x="135" y="142" width="115" height="22" rx="11" fill="rgba(167, 139, 250, 0.15)" />
      <text x="192" y="157" fill="#a78bfa" font-size="10" font-weight="700" text-anchor="middle">#InfosecLabs</text>
    </g>

    <g class="c-slide-3" transform="translate(15, 65)">
      <rect width="385" height="185" rx="10" fill="url(#cardGrad)" stroke="rgba(244, 114, 182, 0.25)" stroke-width="1" />
      <text x="20" y="38" font-size="28">🎮</text>
      <text x="65" y="32" fill="#f472b6" font-size="14.5" font-weight="800">Indie Games &amp; Cyberpunk Worlds</text>
      <text x="65" y="48" fill="#94a3b8" font-size="11">Game Physics &amp; Synthwave Aesthetics</text>
      <text x="20" y="85" fill="#f8fafc" font-size="12.5" font-weight="600">The Caption:</text>
      <text x="20" y="105" fill="#cbd5e1" font-size="11.5">World mechanics, low-poly aesthetics &amp; cyberpunk sound design.</text>
      <text x="20" y="123" fill="#cbd5e1" font-size="11.5">Studying smooth 60 FPS shaders to bring fluid motion to web UI.</text>
      <rect x="20" y="142" width="105" height="22" rx="11" fill="rgba(244, 114, 182, 0.15)" />
      <text x="72" y="157" fill="#f472b6" font-size="10" font-weight="700" text-anchor="middle">#Cyberpunk</text>
      <rect x="135" y="142" width="115" height="22" rx="11" fill="rgba(244, 114, 182, 0.15)" />
      <text x="192" y="157" fill="#f472b6" font-size="10" font-weight="700" text-anchor="middle">#IndieDev</text>
    </g>

    <g class="c-slide-4" transform="translate(15, 65)">
      <rect width="385" height="185" rx="10" fill="url(#cardGrad)" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1" />
      <text x="20" y="38" font-size="28">🎧</text>
      <text x="65" y="32" fill="#38bdf8" font-size="14.5" font-weight="800">Lo-Fi Beats &amp; System Architecture</text>
      <text x="65" y="48" fill="#94a3b8" font-size="11">Distributed Topologies &amp; Chill Grooves</text>
      <text x="20" y="85" fill="#f8fafc" font-size="12.5" font-weight="600">The Caption:</text>
      <text x="20" y="105" fill="#cbd5e1" font-size="11.5">Designing distributed microservices to relaxed 70 BPM grooves.</text>
      <text x="20" y="123" fill="#cbd5e1" font-size="11.5">Sketching caching tiers, database shards, and pub/sub queues.</text>
      <rect x="20" y="142" width="105" height="22" rx="11" fill="rgba(56, 189, 248, 0.15)" />
      <text x="72" y="157" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">#SystemDesign</text>
      <rect x="135" y="142" width="115" height="22" rx="11" fill="rgba(56, 189, 248, 0.15)" />
      <text x="192" y="157" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">#LoFiBeats</text>
    </g>

    <!-- DAILY RINGS -->
    <g transform="translate(15, 265)">
      <rect width="385" height="130" rx="10" fill="rgba(13, 14, 22, 0.85)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" />
      <g transform="translate(85, 65) rotate(-90)">
        <circle cx="0" cy="0" r="42" fill="none" stroke="rgba(34, 211, 238, 0.18)" stroke-width="8" />
        <circle cx="0" cy="0" r="30" fill="none" stroke="rgba(167, 139, 250, 0.18)" stroke-width="8" />
        <circle cx="0" cy="0" r="18" fill="none" stroke="rgba(244, 114, 182, 0.18)" stroke-width="8" />
        <circle class="ring-1" cx="0" cy="0" r="42" fill="none" stroke="#22d3ee" stroke-width="8" stroke-linecap="round" />
        <circle class="ring-2" cx="0" cy="0" r="30" fill="none" stroke="#a78bfa" stroke-width="8" stroke-linecap="round" />
        <circle class="ring-3" cx="0" cy="0" r="18" fill="none" stroke="#f472b6" stroke-width="8" stroke-linecap="round" />
      </g>
      <g transform="translate(160, 22)">
        <text y="0" fill="#f8fafc" font-size="11.5" font-weight="700" letter-spacing="0.5">DAILY DEV ACTIVITY RINGS</text>
        <g transform="translate(0, 18)">
          <circle cx="5" cy="5" r="4.5" fill="#22d3ee" />
          <text x="16" y="9" fill="#22d3ee" font-size="11" font-weight="700">Code Velocity:</text>
          <text x="96" y="9" fill="#cbd5e1" font-size="11">48+ commits / wk</text>
        </g>
        <g transform="translate(0, 42)">
          <circle cx="5" cy="5" r="4.5" fill="#a78bfa" />
          <text x="16" y="9" fill="#a78bfa" font-size="11" font-weight="700">Focus Hours:</text>
          <text x="96" y="9" fill="#cbd5e1" font-size="11">8.5 hrs / day</text>
        </g>
        <g transform="translate(0, 66)">
          <circle cx="5" cy="5" r="4.5" fill="#f472b6" />
          <text x="16" y="9" fill="#f472b6" font-size="11" font-weight="700">Coffee Intake:</text>
          <text x="96" y="9" fill="#cbd5e1" font-size="11">3 cups dark roast</text>
        </g>
      </g>
    </g>
  </g>
</svg>'''

with open('about-life.svg', 'w', encoding='utf-8') as f:
    f.write(about_life_svg)
with open('assets/about-life.svg', 'w', encoding='utf-8') as f:
    f.write(about_life_svg)

print("about-life.svg written.")

# ==============================================================================
# 3. STACK.SVG
# ==============================================================================
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 490" width="100%" height="100%" style="background: #0d0e16; border-radius: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    {SHARED_DEFS}

    <radialGradient id="atomCoreGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#22d3ee"/>
      <stop offset="50%" stop-color="#a78bfa"/>
      <stop offset="100%" stop-color="#f472b6"/>
    </radialGradient>

    <filter id="iconDropShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="rgba(0,0,0,0.8)" />
    </filter>
  </defs>

  <style>
    @keyframes orbit1 {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    @keyframes counterOrbit1 {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(-360deg); }} }}
    @keyframes orbit2 {{ 0% {{ transform: rotate(360deg); }} 100% {{ transform: rotate(0deg); }} }}
    @keyframes counterOrbit2 {{ 0% {{ transform: rotate(-360deg); }} 100% {{ transform: rotate(0deg); }} }}
    @keyframes orbit3 {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    @keyframes counterOrbit3 {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(-360deg); }} }}

    @keyframes moonRevolve {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    @keyframes pulseCore {{ 0%, 100% {{ transform: scale(1); opacity: 0.9; }} 50% {{ transform: scale(1.15); opacity: 0.7; }} }}

    @keyframes borderGlowChase {{
      0%, 100% {{ stroke: rgba(34, 211, 238, 0.2); stroke-width: 1; }}
      50% {{ stroke: #22d3ee; stroke-width: 2; filter: drop-shadow(0 0 6px rgba(34, 211, 238, 0.8)); }}
    }}

    .orbit-plane-1 {{ transform-origin: 450px 160px; animation: orbit1 22s linear infinite; }}
    .orbit-plane-2 {{ transform-origin: 450px 160px; animation: orbit2 28s linear infinite; }}
    .orbit-plane-3 {{ transform-origin: 450px 160px; animation: orbit3 24s linear infinite; }}

    .counter-icon-1 {{ animation: counterOrbit1 22s linear infinite; }}
    .counter-icon-2 {{ animation: counterOrbit2 28s linear infinite; }}
    .counter-icon-3 {{ animation: counterOrbit3 24s linear infinite; }}

    .moons-container {{ transform-origin: 0px 0px; animation: moonRevolve 4.5s linear infinite; }}
    .core-pulse-node {{ transform-origin: 450px 160px; animation: pulseCore 3s ease-in-out infinite; }}
    .chase-chip {{ animation: borderGlowChase 4.8s infinite ease-in-out; }}
  </style>

  <rect width="900" height="490" rx="16" fill="#0d0e16" />
  <rect width="900" height="490" rx="16" fill="url(#dotPattern)" />
  <rect width="900" height="490" rx="16" fill="none" stroke="url(#auroraBorder)" stroke-width="1.2" />

  <g transform="translate(35, 22)">
    <text fill="#22d3ee" font-size="11.5" font-family="monospace" font-weight="700" letter-spacing="1.5">TECH STACK // ORBITAL MATRIX</text>
    <text y="20" fill="#f8fafc" font-size="16" font-weight="800">Core Technologies, Tooling &amp; Satellite Moons</text>
  </g>

  <g transform="translate(710, 25)">
    <rect width="155" height="24" rx="12" fill="rgba(34, 211, 238, 0.12)" stroke="rgba(34, 211, 238, 0.35)" stroke-width="1" />
    <circle cx="12" cy="12" r="3.5" fill="#22d3ee" />
    <text x="22" y="16" fill="#22d3ee" font-size="9.5" font-family="monospace" font-weight="700">ORBIT ENGINE ONLINE</text>
  </g>

  <ellipse cx="450" cy="160" rx="205" ry="66" fill="none" stroke="rgba(34, 211, 238, 0.35)" stroke-width="1.2" stroke-dasharray="5 5" transform="rotate(-25 450 160)" />
  <ellipse cx="450" cy="160" rx="240" ry="78" fill="none" stroke="rgba(167, 139, 250, 0.35)" stroke-width="1.2" stroke-dasharray="5 5" transform="rotate(28 450 160)" />
  <ellipse cx="450" cy="160" rx="215" ry="70" fill="none" stroke="rgba(244, 114, 182, 0.35)" stroke-width="1.2" stroke-dasharray="5 5" transform="rotate(80 450 160)" />

  <g class="core-pulse-node">
    <circle cx="450" cy="160" r="42" fill="#22d3ee" opacity="0.18" filter="url(#auroraGlow)" />
    <circle cx="450" cy="160" r="26" fill="url(#atomCoreGrad)" filter="url(#auroraGlow)" />
    <circle cx="450" cy="160" r="22" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="8 6" opacity="0.8" />
    <text x="450" y="167" fill="#ffffff" font-size="20" font-weight="bold" text-anchor="middle">⚛</text>
  </g>

  <!-- ORBIT 1: REACT ICON + TWO SMALL MOONS -->
  <g transform="rotate(-25 450 160)">
    <g class="orbit-plane-1">
      <g transform="translate(655, 160)">
        <g class="counter-icon-1" style="transform-origin: 0px 0px;">
          <circle cx="0" cy="0" r="20" fill="#0b1120" stroke="#22d3ee" stroke-width="2" filter="url(#iconDropShadow)" />
          <ellipse cx="0" cy="0" rx="13" ry="5" fill="none" stroke="#22d3ee" stroke-width="1.2" />
          <ellipse cx="0" cy="0" rx="13" ry="5" fill="none" stroke="#22d3ee" stroke-width="1.2" transform="rotate(60)" />
          <ellipse cx="0" cy="0" rx="13" ry="5" fill="none" stroke="#22d3ee" stroke-width="1.2" transform="rotate(120)" />
          <circle cx="0" cy="0" r="2.5" fill="#22d3ee" />

          <!-- Two Small Moons Orbiting React (radius 28px) -->
          <circle cx="0" cy="0" r="28" fill="none" stroke="rgba(34, 211, 238, 0.25)" stroke-width="0.8" stroke-dasharray="2 2" />
          <g class="moons-container">
            <g transform="translate(28, 0)">
              <circle cx="0" cy="0" r="9" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1" filter="url(#iconDropShadow)" />
              <text x="0" y="3.5" fill="#ffffff" font-size="8" font-family="monospace" font-weight="900" text-anchor="middle">TS</text>
            </g>
            <g transform="translate(-28, 0)">
              <circle cx="0" cy="0" r="9" fill="#083344" stroke="#22d3ee" stroke-width="1" filter="url(#iconDropShadow)" />
              <text x="0" y="3" fill="#22d3ee" font-size="7" font-weight="900" text-anchor="middle">TW</text>
            </g>
          </g>
        </g>
      </g>

      <g transform="translate(245, 160)">
        <g class="counter-icon-1" style="transform-origin: 0px 0px;">
          <circle cx="0" cy="0" r="18" fill="#1e1b4b" stroke="#a78bfa" stroke-width="1.8" filter="url(#iconDropShadow)" />
          <path d="M -5 -9 L 3 -9 L -1 -1 L 5 -1 L -4 9 L -1 1 L -5 1 Z" fill="#fbbf24" stroke="#f59e0b" stroke-width="0.8" />
        </g>
      </g>
    </g>
  </g>

  <!-- ORBIT 2 -->
  <g transform="rotate(28 450 160)">
    <g class="orbit-plane-2">
      <g transform="translate(690, 160)">
        <g class="counter-icon-2" style="transform-origin: 0px 0px;">
          <circle cx="0" cy="0" r="19" fill="#052e16" stroke="#22c55e" stroke-width="2" filter="url(#iconDropShadow)" />
          <path d="M 0 -10 L 9 -5 L 9 5 L 0 10 L -9 5 L -9 -5 Z" fill="#15803d" stroke="#4ade80" stroke-width="1" />
          <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">JS</text>
        </g>
      </g>
      <g transform="translate(210, 160)">
        <g class="counter-icon-2" style="transform-origin: 0px 0px;">
          <circle cx="0" cy="0" r="19" fill="#451a03" stroke="#f59e0b" stroke-width="2" filter="url(#iconDropShadow)" />
          <path d="M -4 9 L 4 9 L 6 3 L 1 -9 L -3 0 L -6 4 Z" fill="#fbbf24" />
        </g>
      </g>
      <g transform="translate(450, 82)">
        <g class="counter-icon-2" style="transform-origin: 0px 0px;">
          <circle cx="0" cy="0" r="17" fill="#1e293b" stroke="#94a3b8" stroke-width="1.8" filter="url(#iconDropShadow)" />
          <text x="0" y="4" fill="#f8fafc" font-size="9.5" font-family="monospace" font-weight="900" text-anchor="middle">EX</text>
        </g>
      </g>
    </g>
  </g>

  <!-- ORBIT 3 -->
  <g transform="rotate(80 450 160)">
    <g class="orbit-plane-3">
      <g transform="translate(665, 160)">
        <g class="counter-icon-3" style="transform-origin: 0px 0px;">
          <circle cx="0" cy="0" r="19" fill="#0b1120" stroke="#22d3ee" stroke-width="2" filter="url(#iconDropShadow)" />
          <text x="0" y="5" font-size="16" text-anchor="middle">🐧</text>
        </g>
      </g>
      <g transform="translate(235, 160)">
        <g class="counter-icon-3" style="transform-origin: 0px 0px;">
          <circle cx="0" cy="0" r="19" fill="#1e1b4b" stroke="#a78bfa" stroke-width="2" filter="url(#iconDropShadow)" />
          <path d="M 0 -9 Q 0 0, -9 0 Q 0 0, 0 9 Q 0 0, 9 0 Q 0 0, 0 -9 Z" fill="#c084fc" />
        </g>
      </g>
    </g>
  </g>

  <!-- GROUPED CHIP GRID (SEQUENTIAL BORDER CHASE) -->
  <g transform="translate(25, 305)">
    <rect width="850" height="165" rx="12" fill="rgba(18, 22, 38, 0.75)" stroke="url(#auroraBorder)" stroke-width="1" />

    <!-- 1. Frontend Group -->
    <g transform="translate(18, 14)">
      <text fill="#22d3ee" font-size="11" font-weight="700" letter-spacing="1">⚛️ FRONTEND:</text>
      <g transform="translate(130, -11)">
        <rect class="chase-chip" style="animation-delay: 0.0s;" x="0" y="0" width="84" height="24" rx="6" fill="rgba(34, 211, 238, 0.1)" stroke="rgba(34, 211, 238, 0.3)" />
        <text x="42" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">React 19</text>
        <rect class="chase-chip" style="animation-delay: 0.3s;" x="92" y="0" width="94" height="24" rx="6" fill="rgba(34, 211, 238, 0.1)" stroke="rgba(34, 211, 238, 0.3)" />
        <text x="139" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">TypeScript</text>
        <rect class="chase-chip" style="animation-delay: 0.6s;" x="194" y="0" width="98" height="24" rx="6" fill="rgba(34, 211, 238, 0.1)" stroke="rgba(34, 211, 238, 0.3)" />
        <text x="243" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Tailwind v4</text>
        <rect class="chase-chip" style="animation-delay: 0.9s;" x="300" y="0" width="60" height="24" rx="6" fill="rgba(34, 211, 238, 0.1)" stroke="rgba(34, 211, 238, 0.3)" />
        <text x="330" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Vite</text>
        <rect class="chase-chip" style="animation-delay: 1.2s;" x="368" y="0" width="98" height="24" rx="6" fill="rgba(34, 211, 238, 0.1)" stroke="rgba(34, 211, 238, 0.3)" />
        <text x="417" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">HTML5 / CSS3</text>
        <rect class="chase-chip" style="animation-delay: 1.5s;" x="474" y="0" width="102" height="24" rx="6" fill="rgba(34, 211, 238, 0.1)" stroke="rgba(34, 211, 238, 0.3)" />
        <text x="525" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">JavaScript ES6+</text>
      </g>
    </g>

    <!-- 2. Motion & 3D Group -->
    <g transform="translate(18, 52)">
      <text fill="#a78bfa" font-size="11" font-weight="700" letter-spacing="1">✨ MOTION &amp; 3D:</text>
      <g transform="translate(130, -11)">
        <rect class="chase-chip" style="animation-delay: 1.8s;" x="0" y="0" width="112" height="24" rx="6" fill="rgba(167, 139, 250, 0.1)" stroke="rgba(167, 139, 250, 0.3)" />
        <text x="56" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Framer Motion</text>
        <rect class="chase-chip" style="animation-delay: 2.1s;" x="120" y="0" width="108" height="24" rx="6" fill="rgba(167, 139, 250, 0.1)" stroke="rgba(167, 139, 250, 0.3)" />
        <text x="174" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">CSS Keyframes</text>
        <rect class="chase-chip" style="animation-delay: 2.4s;" x="236" y="0" width="86" height="24" rx="6" fill="rgba(167, 139, 250, 0.1)" stroke="rgba(167, 139, 250, 0.3)" />
        <text x="279" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">SVG SMIL</text>
        <rect class="chase-chip" style="animation-delay: 2.7s;" x="330" y="0" width="116" height="24" rx="6" fill="rgba(167, 139, 250, 0.1)" stroke="rgba(167, 139, 250, 0.3)" />
        <text x="388" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Canvas Confetti</text>
        <rect class="chase-chip" style="animation-delay: 3.0s;" x="454" y="0" width="82" height="24" rx="6" fill="rgba(167, 139, 250, 0.1)" stroke="rgba(167, 139, 250, 0.3)" />
        <text x="495" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Recharts</text>
      </g>
    </g>

    <!-- 3. Data Group -->
    <g transform="translate(18, 90)">
      <text fill="#f472b6" font-size="11" font-weight="700" letter-spacing="1">💾 DATA &amp; CLOUD:</text>
      <g transform="translate(130, -11)">
        <rect class="chase-chip" style="animation-delay: 3.3s;" x="0" y="0" width="76" height="24" rx="6" fill="rgba(244, 114, 182, 0.1)" stroke="rgba(244, 114, 182, 0.3)" />
        <text x="38" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Node.js</text>
        <rect class="chase-chip" style="animation-delay: 3.6s;" x="84" y="0" width="80" height="24" rx="6" fill="rgba(244, 114, 182, 0.1)" stroke="rgba(244, 114, 182, 0.3)" />
        <text x="124" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Express</text>
        <rect class="chase-chip" style="animation-delay: 3.9s;" x="172" y="0" width="138" height="24" rx="6" fill="rgba(244, 114, 182, 0.1)" stroke="rgba(244, 114, 182, 0.3)" />
        <text x="241" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Firebase Realtime DB</text>
        <rect class="chase-chip" style="animation-delay: 4.2s;" x="318" y="0" width="94" height="24" rx="6" fill="rgba(244, 114, 182, 0.1)" stroke="rgba(244, 114, 182, 0.3)" />
        <text x="365" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">REST APIs</text>
      </g>
    </g>

    <!-- 4. AI Group -->
    <g transform="translate(18, 128)">
      <text fill="#38bdf8" font-size="11" font-weight="700" letter-spacing="1">🤖 AI &amp; OPS:</text>
      <g transform="translate(130, -11)">
        <rect class="chase-chip" style="animation-delay: 4.5s;" x="0" y="0" width="132" height="24" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="rgba(56, 189, 248, 0.3)" />
        <text x="66" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Google Gemini AI</text>
        <rect class="chase-chip" style="animation-delay: 4.8s;" x="140" y="0" width="138" height="24" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="rgba(56, 189, 248, 0.3)" />
        <text x="209" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Agentic Workflows</text>
        <rect class="chase-chip" style="animation-delay: 0.15s;" x="286" y="0" width="136" height="24" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="rgba(56, 189, 248, 0.3)" />
        <text x="354" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Linux (Kali / Ubuntu)</text>
        <rect class="chase-chip" style="animation-delay: 0.45s;" x="430" y="0" width="102" height="24" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="rgba(56, 189, 248, 0.3)" />
        <text x="481" y="16" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Git &amp; GitHub</text>
      </g>
    </g>
  </g>
</svg>'''

with open('stack.svg', 'w', encoding='utf-8') as f:
    f.write(stack_svg)
with open('assets/stack.svg', 'w', encoding='utf-8') as f:
    f.write(stack_svg)

print("stack.svg written.")

# ==============================================================================
# 4. ID-DASHBOARD.SVG
# ==============================================================================
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%" style="background: #0d0e16; border-radius: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    {SHARED_DEFS}

    <linearGradient id="holoSweepGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(34, 211, 238, 0)"/>
      <stop offset="25%" stop-color="rgba(34, 211, 238, 0.3)"/>
      <stop offset="45%" stop-color="rgba(167, 139, 250, 0.32)"/>
      <stop offset="65%" stop-color="rgba(244, 114, 182, 0.35)"/>
      <stop offset="85%" stop-color="rgba(251, 191, 36, 0.3)"/>
      <stop offset="100%" stop-color="rgba(34, 211, 238, 0)"/>
    </linearGradient>

    <linearGradient id="goldChipGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#eab308"/>
      <stop offset="80%" stop-color="#ca8a04"/>
      <stop offset="100%" stop-color="#a16207"/>
    </linearGradient>

    <linearGradient id="lanyardStrap" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111827"/>
      <stop offset="50%" stop-color="#1f2937"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>

    <clipPath id="badgeCardClip">
      <rect x="55" y="65" width="270" height="365" rx="16" />
    </clipPath>

    <clipPath id="avatarFrameClip">
      <rect x="75" y="115" width="230" height="155" rx="8" />
    </clipPath>

    <filter id="badgeShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="rgba(0,0,0,0.7)" />
    </filter>
  </defs>

  <style>
    @keyframes badgeDropDamped {{
      0% {{ transform: translateY(-160px) rotate(14deg); }}
      20% {{ transform: translateY(0px) rotate(-10deg); }}
      40% {{ transform: translateY(0px) rotate(7deg); }}
      60% {{ transform: translateY(0px) rotate(-4deg); }}
      80% {{ transform: translateY(0px) rotate(2deg); }}
      100% {{ transform: translateY(0px) rotate(-1.5deg); }}
    }}

    @keyframes badgeAmbientSway {{
      0%, 100% {{ transform: rotate(-2.5deg); }}
      50% {{ transform: rotate(2.5deg); }}
    }}

    @keyframes lightTraveling {{
      0% {{ stroke-dashoffset: 0; }}
      100% {{ stroke-dashoffset: -770; }}
    }}

    @keyframes holoPass {{
      0% {{ transform: translateX(-260px) translateY(-40px) rotate(25deg); }}
      100% {{ transform: translateX(360px) translateY(40px) rotate(25deg); }}
    }}

    @keyframes barGrowSingle {{
      0% {{ transform: scaleY(0.05); }}
      100% {{ transform: scaleY(1); }}
    }}

    @keyframes eqLive1 {{ 0%, 100% {{ height: 5px; }} 50% {{ height: 18px; }} }}
    @keyframes eqLive2 {{ 0%, 100% {{ height: 15px; }} 50% {{ height: 7px; }} }}
    @keyframes eqLive3 {{ 0%, 100% {{ height: 10px; }} 50% {{ height: 22px; }} }}
    @keyframes eqLive4 {{ 0%, 100% {{ height: 20px; }} 50% {{ height: 9px; }} }}
    @keyframes eqLive5 {{ 0%, 100% {{ height: 7px; }} 50% {{ height: 16px; }} }}

    .badge-damped-group {{
      transform-origin: 190px 15px;
      animation: badgeDropDamped 2.2s cubic-bezier(0.25, 1, 0.5, 1) forwards, badgeAmbientSway 5s ease-in-out 2.2s infinite;
    }}

    .racing-light-border {{
      stroke-dasharray: 90 295;
      animation: lightTraveling 3.5s linear infinite;
    }}

    .holo-foil-sweep {{
      transform-origin: 190px 250px;
      animation: holoPass 4.5s ease-in-out infinite alternate;
    }}

    .repo-bar {{
      transform-origin: bottom;
      animation: barGrowSingle 1.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
  </style>

  <rect width="900" height="450" rx="16" fill="#0d0e16" />
  <rect width="900" height="450" rx="16" fill="url(#dotPattern)" />
  <rect width="900" height="450" rx="16" fill="none" stroke="url(#auroraBorder)" stroke-width="1.2" />

  <!-- LEFT: LANYARD ID BADGE -->
  <g>
    <path d="M 158 0 L 174 26 L 206 26 L 222 0 Z" fill="url(#lanyardStrap)" stroke="#22d3ee" stroke-width="0.8" />
    <text x="190" y="16" fill="#22d3ee" font-size="8" font-family="monospace" font-weight="900" text-anchor="middle" letter-spacing="1">DEV // SARTAJ</text>
    
    <circle cx="190" cy="28" r="6" fill="none" stroke="#94a3b8" stroke-width="3" />
    <rect x="186" y="32" width="8" height="16" rx="2" fill="#64748b" stroke="#cbd5e1" stroke-width="1" />
    <path d="M 183 48 C 183 58, 197 58, 197 48" fill="none" stroke="#e2e8f0" stroke-width="2.5" />
  </g>

  <g class="badge-damped-group">
    <g filter="url(#badgeShadow)">
      <rect x="55" y="65" width="270" height="365" rx="16" fill="#0d0e16" stroke="url(#auroraBorder)" stroke-width="1.5" />
      <rect x="58" y="68" width="264" height="359" rx="13" fill="#090a12" />

      <rect x="165" y="74" width="50" height="8" rx="4" fill="#05060a" stroke="#475569" stroke-width="1" />

      <rect x="58" y="90" width="264" height="20" fill="rgba(34, 211, 238, 0.12)" />
      <text x="190" y="103" fill="#22d3ee" font-size="9" font-family="monospace" font-weight="900" text-anchor="middle" letter-spacing="1.2">★ CORE OPERATIVE // LVL 5 ★</text>

      <g clip-path="url(#avatarFrameClip)">
        <rect x="75" y="115" width="230" height="155" fill="#1e293b" />
        <image href="data:image/png;base64,{b64_avatar}" x="80" y="80" width="220" height="220" preserveAspectRatio="xMidYMid slice" />
      </g>
      
      <rect x="75" y="115" width="230" height="155" rx="8" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" />
      <rect class="racing-light-border" x="75" y="115" width="230" height="155" rx="8" fill="none" stroke="url(#auroraGrad)" stroke-width="2.5" filter="url(#auroraGlow)" />

      <!-- Gold Smart-Card Microchip -->
      <g transform="translate(75, 282)">
        <rect width="36" height="26" rx="4" fill="url(#goldChipGrad)" stroke="#78350f" stroke-width="0.8" />
        <line x1="12" y1="0" x2="12" y2="26" stroke="#78350f" stroke-width="0.8" />
        <line x1="24" y1="0" x2="24" y2="26" stroke="#78350f" stroke-width="0.8" />
        <line x1="0" y1="13" x2="36" y2="13" stroke="#78350f" stroke-width="0.8" />
        <circle cx="18" cy="13" r="3.5" fill="#ca8a04" />
      </g>

      <g transform="translate(122, 284)">
        <text y="0" fill="#94a3b8" font-size="8" font-family="monospace">OPERATIVE NAME</text>
        <text y="13" fill="#f8fafc" font-size="13.5" font-weight="900" letter-spacing="0.5">SARTAJ</text>
        <text y="25" fill="#22d3ee" font-size="8.5" font-weight="700">FULL-STACK ARCHITECT</text>
      </g>

      <g transform="translate(75, 326)">
        <text y="0" fill="#64748b" font-size="7.5" font-family="monospace">CLEARANCE: ALPHA-01 // ROOT</text>
        <text y="11" fill="#64748b" font-size="7.5" font-family="monospace">SERIAL NO: #SRT-2026-DEV</text>
      </g>

      <g transform="translate(245, 320)">
        <circle cx="16" cy="16" r="15" fill="none" stroke="rgba(34, 211, 238, 0.35)" stroke-width="1.5" stroke-dasharray="3 2" />
        <circle cx="16" cy="16" r="10" fill="rgba(34, 211, 238, 0.08)" />
        <text x="16" y="20" fill="#22d3ee" font-size="10" font-weight="900" text-anchor="middle">✓</text>
      </g>

      <!-- Barcode Graphic -->
      <g transform="translate(75, 355)">
        <rect x="0" y="0" width="3" height="22" fill="#cbd5e1" />
        <rect x="5" y="0" width="1.5" height="22" fill="#cbd5e1" />
        <rect x="9" y="0" width="4" height="22" fill="#cbd5e1" />
        <rect x="15" y="0" width="1.5" height="22" fill="#cbd5e1" />
        <rect x="19" y="0" width="3" height="22" fill="#cbd5e1" />
        <rect x="25" y="0" width="5" height="22" fill="#cbd5e1" />
        <rect x="33" y="0" width="2" height="22" fill="#cbd5e1" />
        <rect x="37" y="0" width="4" height="22" fill="#cbd5e1" />
        <rect x="44" y="0" width="1.5" height="22" fill="#cbd5e1" />
        <rect x="48" y="0" width="3" height="22" fill="#cbd5e1" />
        <rect x="54" y="0" width="5" height="22" fill="#cbd5e1" />
        <rect x="62" y="0" width="2" height="22" fill="#cbd5e1" />
        <rect x="66" y="0" width="3" height="22" fill="#cbd5e1" />
        <rect x="71" y="0" width="1.5" height="22" fill="#cbd5e1" />
        <rect x="75" y="0" width="4" height="22" fill="#cbd5e1" />
        <rect x="81" y="0" width="2" height="22" fill="#cbd5e1" />
        <rect x="85" y="0" width="4" height="22" fill="#cbd5e1" />
        <rect x="91" y="0" width="2" height="22" fill="#cbd5e1" />
        <rect x="95" y="0" width="5" height="22" fill="#cbd5e1" />
        <rect x="103" y="0" width="1.5" height="22" fill="#cbd5e1" />
        <rect x="107" y="0" width="3" height="22" fill="#cbd5e1" />
        
        <rect x="185" y="0" width="22" height="22" fill="#cbd5e1" />
        <rect x="187" y="2" width="18" height="18" fill="#090a12" />
        <rect x="189" y="4" width="6" height="6" fill="#cbd5e1" />
        <rect x="197" y="4" width="6" height="6" fill="#cbd5e1" />
        <rect x="189" y="12" width="6" height="6" fill="#cbd5e1" />
        <rect x="197" y="12" width="6" height="6" fill="#22d3ee" />
        <text x="55" y="32" fill="#94a3b8" font-size="7.5" font-family="monospace" text-anchor="middle">GITHUB.COM/ITS-SARTAJ</text>
      </g>

      <g clip-path="url(#badgeCardClip)">
        <rect class="holo-foil-sweep" x="0" y="0" width="150" height="500" fill="url(#holoSweepGrad)" pointer-events="none" />
      </g>
    </g>
  </g>

  <!-- RIGHT: DEV DASHBOARD -->
  <g transform="translate(380, 25)">
    <rect width="495" height="400" rx="14" fill="rgba(18, 22, 38, 0.75)" stroke="url(#auroraBorder)" stroke-width="1" />

    <rect width="495" height="38" rx="14" fill="rgba(13, 14, 22, 0.9)" />
    <circle cx="20" cy="19" r="4.5" fill="#22d3ee" />
    <text x="35" y="23" fill="#f8fafc" font-size="12.5" font-weight="700">DEV TELEMETRY // REAL-TIME DASHBOARD</text>
    <rect x="365" y="8" width="115" height="22" rx="11" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="0.8" />
    <text x="422" y="22" fill="#34d399" font-size="9.5" font-family="monospace" font-weight="700" text-anchor="middle">ONLINE 99.9%</text>

    <!-- KPI Tiles -->
    <g transform="translate(18, 50)">
      <g transform="translate(0, 0)">
        <rect width="108" height="56" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(34, 211, 238, 0.3)" stroke-width="1" />
        <text x="12" y="20" fill="#22d3ee" font-size="10" font-weight="700">⚡ COMMITS</text>
        <text x="12" y="44" fill="#f8fafc" font-size="18" font-weight="900">48+<tspan font-size="10" fill="#94a3b8">/wk</tspan></text>
      </g>
      <g transform="translate(118, 0)">
        <rect width="108" height="56" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(167, 139, 250, 0.3)" stroke-width="1" />
        <text x="12" y="20" fill="#a78bfa" font-size="10" font-weight="700">⏱️ CODE TIME</text>
        <text x="12" y="44" fill="#f8fafc" font-size="18" font-weight="900">1,850+<tspan font-size="10" fill="#94a3b8">h</tspan></text>
      </g>
      <g transform="translate(236, 0)">
        <rect width="108" height="56" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(244, 114, 182, 0.3)" stroke-width="1" />
        <text x="12" y="20" fill="#f472b6" font-size="10" font-weight="700">🚀 SHIPPED</text>
        <text x="12" y="44" fill="#f8fafc" font-size="18" font-weight="900">12+<tspan font-size="10" fill="#94a3b8"> apps</tspan></text>
      </g>
      <g transform="translate(354, 0)">
        <rect width="105" height="56" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(16, 185, 129, 0.3)" stroke-width="1" />
        <text x="12" y="20" fill="#34d399" font-size="10" font-weight="700">🎯 PR MERGE</text>
        <text x="12" y="44" fill="#f8fafc" font-size="18" font-weight="900">99.4%</text>
      </g>
    </g>

    <!-- Single-Hue Bar Chart -->
    <g transform="translate(18, 118)">
      <rect width="459" height="186" rx="10" fill="rgba(13, 14, 22, 0.85)" stroke="rgba(34, 211, 238, 0.2)" stroke-width="1" />
      <text x="16" y="20" fill="#f8fafc" font-size="12" font-weight="700">⭐ Top Production Repositories</text>
      <text x="440" y="20" fill="#22d3ee" font-size="10" font-family="monospace" text-anchor="end">METRIC: STAR VELOCITY</text>

      <g transform="translate(16, 36)">
        <text x="0" y="13" fill="#cbd5e1" font-size="11" font-family="monospace" font-weight="600">BARAKA-Bizz</text>
        <rect x="120" y="2" width="245" height="13" rx="4" fill="rgba(34, 211, 238, 0.15)" />
        <rect class="repo-bar" x="120" y="2" width="240" height="13" rx="4" fill="#22d3ee" />
        <text x="372" y="13" fill="#22d3ee" font-size="10.5" font-family="monospace" font-weight="bold">158 ★</text>
      </g>
      <g transform="translate(16, 59)">
        <text x="0" y="13" fill="#cbd5e1" font-size="11" font-family="monospace" font-weight="600">ganeralstore</text>
        <rect x="120" y="2" width="245" height="13" rx="4" fill="rgba(34, 211, 238, 0.15)" />
        <rect class="repo-bar" x="120" y="2" width="215" height="13" rx="4" fill="#06b6d4" />
        <text x="345" y="13" fill="#22d3ee" font-size="10.5" font-family="monospace" font-weight="bold">142 ★</text>
      </g>
      <g transform="translate(16, 82)">
        <text x="0" y="13" fill="#cbd5e1" font-size="11" font-family="monospace" font-weight="600">Apex-Tech</text>
        <rect x="120" y="2" width="245" height="13" rx="4" fill="rgba(34, 211, 238, 0.15)" />
        <rect class="repo-bar" x="120" y="2" width="180" height="13" rx="4" fill="#0891b2" />
        <text x="310" y="13" fill="#22d3ee" font-size="10.5" font-family="monospace" font-weight="bold">118 ★</text>
      </g>
      <g transform="translate(16, 105)">
        <text x="0" y="13" fill="#cbd5e1" font-size="11" font-family="monospace" font-weight="600">Leovra</text>
        <rect x="120" y="2" width="245" height="13" rx="4" fill="rgba(34, 211, 238, 0.15)" />
        <rect class="repo-bar" x="120" y="2" width="155" height="13" rx="4" fill="#0e7490" />
        <text x="285" y="13" fill="#22d3ee" font-size="10.5" font-family="monospace" font-weight="bold">104 ★</text>
      </g>
      <g transform="translate(16, 128)">
        <text x="0" y="13" fill="#cbd5e1" font-size="11" font-family="monospace" font-weight="600">Sajid-Tax</text>
        <rect x="120" y="2" width="245" height="13" rx="4" fill="rgba(34, 211, 238, 0.15)" />
        <rect class="repo-bar" x="120" y="2" width="135" height="13" rx="4" fill="#155e75" />
        <text x="265" y="13" fill="#22d3ee" font-size="10.5" font-family="monospace" font-weight="bold">96 ★</text>
      </g>
      <g transform="translate(16, 151)">
        <text x="0" y="13" fill="#cbd5e1" font-size="11" font-family="monospace" font-weight="600">Grocery</text>
        <rect x="120" y="2" width="245" height="13" rx="4" fill="rgba(34, 211, 238, 0.15)" />
        <rect class="repo-bar" x="120" y="2" width="115" height="13" rx="4" fill="#164e63" />
        <text x="245" y="13" fill="#22d3ee" font-size="10.5" font-family="monospace" font-weight="bold">84 ★</text>
      </g>
    </g>

    <!-- "Now" Panel -->
    <g transform="translate(18, 314)">
      <rect width="459" height="72" rx="8" fill="rgba(22, 27, 46, 0.75)" stroke="rgba(16, 185, 129, 0.35)" stroke-width="1" />
      <circle cx="16" cy="18" r="4" fill="#10b981" />
      <text x="28" y="22" fill="#34d399" font-size="10.5" font-family="monospace" font-weight="700">NOW PANEL // CURRENTLY BUILDING</text>

      <g transform="translate(415, 12)">
        <rect x="0" y="0" width="3" height="12" fill="#10b981" style="animation: eqLive1 0.7s infinite alternate;" />
        <rect x="5" y="0" width="3" height="12" fill="#22d3ee" style="animation: eqLive2 0.5s infinite alternate;" />
        <rect x="10" y="0" width="3" height="12" fill="#10b981" style="animation: eqLive3 0.6s infinite alternate;" />
        <rect x="15" y="0" width="3" height="12" fill="#a78bfa" style="animation: eqLive4 0.8s infinite alternate;" />
        <rect x="20" y="0" width="3" height="12" fill="#22d3ee" style="animation: eqLive5 0.65s infinite alternate;" />
      </g>

      <text x="16" y="44" fill="#f8fafc" font-size="11.5" font-family="monospace" font-weight="700">&gt; Building Next-Gen Cloud POS, B2B Wholesale &amp; Enterprise Platforms</text>
      <text x="16" y="59" fill="#94a3b8" font-size="10.5" font-family="monospace">&gt; git commit -m &quot;feat: real-time Firebase RTDB, OTP verify &amp; auto invoices&quot;</text>
    </g>
  </g>
</svg>'''

with open('id-dashboard.svg', 'w', encoding='utf-8') as f:
    f.write(id_dashboard_svg)
with open('assets/id-dashboard.svg', 'w', encoding='utf-8') as f:
    f.write(id_dashboard_svg)

print("id-dashboard.svg written.")

# ==============================================================================
# 5. CONNECT.SVG
# ==============================================================================
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%" style="background: #0d0e16; border-radius: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    {SHARED_DEFS}

    <filter id="neonSignGlow2" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur1" />
      <feGaussianBlur stdDeviation="16" result="blur2" />
      <feMerge>
        <feMergeNode in="blur2" />
        <feMergeNode in="blur1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes charFloatAnim {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-7px); }}
    }}

    @keyframes neonFlickerAnim {{
      0%, 100% {{ opacity: 1; }}
      42% {{ opacity: 0.85; }}
      44% {{ opacity: 1; }}
      88% {{ opacity: 0.9; }}
      90% {{ opacity: 0.75; }}
      92% {{ opacity: 1; }}
    }}

    @keyframes nudgeArrow {{
      0%, 100% {{ transform: translateX(0px); }}
      50% {{ transform: translateX(6px); }}
    }}

    @keyframes floatParticleRising {{
      0% {{ transform: translateY(0px) scale(0.8); opacity: 0; }}
      20% {{ opacity: 0.8; }}
      80% {{ opacity: 0.8; }}
      100% {{ transform: translateY(-50px) scale(1.1); opacity: 0; }}
    }}

    .char-float-node {{ animation: charFloatAnim 3.8s ease-in-out infinite; }}
    .neon-pulse-sign {{ animation: neonFlickerAnim 4s infinite; }}
    .arrow-nudge {{ animation: nudgeArrow 1.5s ease-in-out infinite; }}
    .floating-sparkle {{ animation: floatParticleRising 3.5s infinite linear; }}
  </style>

  <rect width="900" height="450" rx="16" fill="#0d0e16" />
  <rect width="900" height="450" rx="16" fill="url(#dotPattern)" />
  <rect width="900" height="450" rx="16" fill="none" stroke="url(#auroraBorder)" stroke-width="1.2" />

  <circle cx="210" cy="220" r="160" fill="#22d3ee" opacity="0.08" filter="url(#neonSignGlow2)" />
  <circle cx="340" cy="280" r="130" fill="#f472b6" opacity="0.08" filter="url(#neonSignGlow2)" />

  <!-- LEFT: CHARACTER & NEON SIGN -->
  <g class="char-float-node" transform="translate(10, 20)">
    <image href="data:image/png;base64,{b64_footer}" x="15" y="15" width="410" height="410" preserveAspectRatio="xMidYMid meet" />

    <g class="floating-sparkle" style="animation-delay: 0.2s;">
      <text x="350" y="140" fill="#22d3ee" font-size="16" filter="url(#neonSignGlow2)">✦</text>
    </g>
    <g class="floating-sparkle" style="animation-delay: 1.4s;">
      <text x="380" y="190" fill="#f472b6" font-size="20" filter="url(#neonSignGlow2)">★</text>
    </g>
    <g class="floating-sparkle" style="animation-delay: 2.1s;">
      <text x="40" y="160" fill="#fbbf24" font-size="14" filter="url(#neonSignGlow2)">✨</text>
    </g>
    <g class="floating-sparkle" style="animation-delay: 0.9s;">
      <text x="365" y="270" fill="#ec4899" font-size="16" filter="url(#neonSignGlow2)">♥</text>
    </g>
  </g>

  <!-- RIGHT: LINK CARDS WITH BRAND ICONS & NUDGING ARROWS -->
  <g transform="translate(435, 25)">
    <text fill="#22d3ee" font-size="11" font-family="monospace" font-weight="700" letter-spacing="1.5">LET'S CONNECT // INQUIRIES &amp; COLLABORATIONS</text>
    <text y="24" fill="#f8fafc" font-size="20" font-weight="800">Ready to build something iconic?</text>

    <!-- Card 1: LinkedIn -->
    <g transform="translate(0, 48)">
      <rect width="435" height="66" rx="12" fill="rgba(18, 22, 38, 0.75)" stroke="rgba(34, 211, 238, 0.3)" stroke-width="1.2" />
      <rect x="0" y="0" width="5" height="66" rx="2.5" fill="#0a66c2" />
      <circle cx="36" cy="33" r="18" fill="#0a66c2" />
      <text x="36" y="39" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">in</text>
      <text x="68" y="27" fill="#f8fafc" font-size="14" font-weight="700">LinkedIn Network</text>
      <text x="68" y="47" fill="#94a3b8" font-size="11.5">Engineering updates, architecture insights &amp; networking</text>
      <g class="arrow-nudge" transform="translate(390, 33)">
        <circle cx="0" cy="0" r="14" fill="rgba(10, 102, 194, 0.2)" stroke="#0a66c2" stroke-width="1" />
        <path d="M -4 -4 L 3 0 L -4 4" fill="none" stroke="#22d3ee" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      </g>
    </g>

    <!-- Card 2: GitHub -->
    <g transform="translate(0, 124)">
      <rect width="435" height="66" rx="12" fill="rgba(18, 22, 38, 0.75)" stroke="rgba(167, 139, 250, 0.3)" stroke-width="1.2" />
      <rect x="0" y="0" width="5" height="66" rx="2.5" fill="#a78bfa" />
      <circle cx="36" cy="33" r="18" fill="#1e1b4b" stroke="#a78bfa" stroke-width="1" />
      <text x="36" y="40" font-size="18" text-anchor="middle">🐙</text>
      <text x="68" y="27" fill="#f8fafc" font-size="14" font-weight="700">GitHub Profile (@its-sartaj)</text>
      <text x="68" y="47" fill="#94a3b8" font-size="11.5">Open source code, repositories &amp; commit telemetry</text>
      <g class="arrow-nudge" transform="translate(390, 33)">
        <circle cx="0" cy="0" r="14" fill="rgba(167, 139, 250, 0.2)" stroke="#a78bfa" stroke-width="1" />
        <path d="M -4 -4 L 3 0 L -4 4" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      </g>
    </g>

    <!-- Card 3: Email Direct -->
    <g transform="translate(0, 200)">
      <rect width="435" height="66" rx="12" fill="rgba(18, 22, 38, 0.75)" stroke="rgba(239, 68, 68, 0.3)" stroke-width="1.2" />
      <rect x="0" y="0" width="5" height="66" rx="2.5" fill="#ef4444" />
      <circle cx="36" cy="33" r="18" fill="#450a0a" stroke="#ef4444" stroke-width="1" />
      <text x="36" y="40" font-size="16" text-anchor="middle">✉️</text>
      <text x="68" y="27" fill="#f8fafc" font-size="14" font-weight="700">Direct Email Inquiries</text>
      <text x="68" y="47" fill="#94a3b8" font-size="11.5">mrbeast797996@gmail.com • Inquiries &amp; hiring discussions</text>
      <g class="arrow-nudge" transform="translate(390, 33)">
        <circle cx="0" cy="0" r="14" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444" stroke-width="1" />
        <path d="M -4 -4 L 3 0 L -4 4" fill="none" stroke="#f87171" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      </g>
    </g>

    <!-- Card 4: Portfolio & Live Projects -->
    <g transform="translate(0, 276)">
      <rect width="435" height="66" rx="12" fill="rgba(18, 22, 38, 0.75)" stroke="rgba(16, 185, 129, 0.3)" stroke-width="1.2" />
      <rect x="0" y="0" width="5" height="66" rx="2.5" fill="#10b981" />
      <circle cx="36" cy="33" r="18" fill="#064e3b" stroke="#10b981" stroke-width="1" />
      <text x="36" y="40" font-size="16" text-anchor="middle">🌐</text>
      <text x="68" y="27" fill="#f8fafc" font-size="14" font-weight="700">Live Demos &amp; Web Platforms</text>
      <text x="68" y="47" fill="#94a3b8" font-size="11.5">Apex Tech, Khurshid Store POS, &amp; interactive web apps</text>
      <g class="arrow-nudge" transform="translate(390, 33)">
        <circle cx="0" cy="0" r="14" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="1" />
        <path d="M -4 -4 L 3 0 L -4 4" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      </g>
    </g>

    <!-- Bottom Opportunity Pill -->
    <g transform="translate(0, 355)">
      <rect width="435" height="38" rx="19" fill="rgba(34, 211, 238, 0.12)" stroke="url(#auroraBorder)" stroke-width="1" />
      <circle cx="20" cy="19" r="4.5" fill="#22d3ee" />
      <text x="34" y="23" fill="#22d3ee" font-size="11.5" font-weight="700">AVAILABLE FOR HIRE • FULL-STACK ROLES &amp; FREELANCE</text>
    </g>
  </g>
</svg>'''

with open('connect.svg', 'w', encoding='utf-8') as f:
    f.write(connect_svg)
with open('assets/connect.svg', 'w', encoding='utf-8') as f:
    f.write(connect_svg)

print("connect.svg written.")

# Validate XML for all 5 SVGs in root
all_files = [
    'hero.svg',
    'about-life.svg',
    'stack.svg',
    'id-dashboard.svg',
    'connect.svg'
]

print("\n--- XML Syntax Verification ---")
for fpath in all_files:
    ET.parse(fpath)
    print(f"  [PASS] {fpath} ({os.path.getsize(fpath):,} bytes)")

print("\nAll files successfully verified!")
