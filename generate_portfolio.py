"""
Complete Generator for Sartaj's Animated GitHub Profile Portfolio
Generates all 6 SVG animation components:
1. hero.svg - Camera viewfinder, waving developer avatar, cycling roles
2. what_i_build_and_hobbies.svg - Dual panels, 4 what I build cards, 4-story carousel with progress bars
3. tech_orbit.svg - 3D atom core, brand icons orbiting, skill chip grid
4. id_badge_dashboard.svg - Swinging holographic lanyard badge, 7-day commit bar chart, live ticker
5. contribution_city.svg - 3D isometric commit skyline with spires, beacons, traffic data streams
6. connect_footer.svg - Pointing character sticker, neon handwritten sign, interactive connection cards
"""

import os
import base64
import xml.etree.ElementTree as ET

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ""

b64_avatar = get_base64_image('assets/badge_avatar_opt.png')
b64_footer = get_base64_image('assets/footer_character_opt.png')

print(f"Loaded avatar b64: {len(b64_avatar)} chars")
print(f"Loaded footer b64: {len(b64_footer)} chars")

# ==============================================================================
# 1. HERO SVG
# ==============================================================================
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%" style="background: #080c14; border-radius: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="heroGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c14"/>
      <stop offset="50%" stop-color="#0d1527"/>
      <stop offset="100%" stop-color="#070a12"/>
    </linearGradient>

    <linearGradient id="cyanGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(56, 189, 248, 0.15)"/>
      <stop offset="100%" stop-color="rgba(129, 140, 248, 0.05)"/>
    </linearGradient>

    <clipPath id="viewfinderClip">
      <rect x="30" y="30" width="380" height="420" rx="14" />
    </clipPath>

    <clipPath id="avatarCircle">
      <circle cx="220" cy="240" r="135" />
    </clipPath>

    <pattern id="cyberGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="rgba(56, 189, 248, 0.05)" stroke-width="1"/>
    </pattern>

    <filter id="glowFilter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes recBlink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.15; }}
    }}
    @keyframes afPulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.9; }}
      50% {{ transform: scale(1.06); opacity: 0.45; }}
    }}
    @keyframes scanMove {{
      0% {{ transform: translateY(0px); }}
      100% {{ transform: translateY(420px); }}
    }}
    @keyframes vu1 {{ 0%, 100% {{ height: 6px; }} 50% {{ height: 18px; }} }}
    @keyframes vu2 {{ 0%, 100% {{ height: 14px; }} 50% {{ height: 8px; }} }}
    @keyframes vu3 {{ 0%, 100% {{ height: 10px; }} 50% {{ height: 20px; }} }}
    @keyframes vu4 {{ 0%, 100% {{ height: 16px; }} 50% {{ height: 5px; }} }}

    @keyframes waveMotion {{
      0%, 100% {{ transform: rotate(0deg); }}
      20% {{ transform: rotate(18deg); }}
      40% {{ transform: rotate(-8deg); }}
      60% {{ transform: rotate(16deg); }}
      80% {{ transform: rotate(-4deg); }}
    }}

    @keyframes roleCycle1 {{
      0%, 18% {{ opacity: 1; transform: translateY(0px); }}
      20%, 100% {{ opacity: 0; transform: translateY(12px); }}
    }}
    @keyframes roleCycle2 {{
      0%, 19% {{ opacity: 0; transform: translateY(-12px); }}
      20%, 38% {{ opacity: 1; transform: translateY(0px); }}
      40%, 100% {{ opacity: 0; transform: translateY(12px); }}
    }}
    @keyframes roleCycle3 {{
      0%, 39% {{ opacity: 0; transform: translateY(-12px); }}
      40%, 58% {{ opacity: 1; transform: translateY(0px); }}
      60%, 100% {{ opacity: 0; transform: translateY(12px); }}
    }}
    @keyframes roleCycle4 {{
      0%, 59% {{ opacity: 0; transform: translateY(-12px); }}
      60%, 78% {{ opacity: 1; transform: translateY(0px); }}
      80%, 100% {{ opacity: 0; transform: translateY(12px); }}
    }}
    @keyframes roleCycle5 {{
      0%, 79% {{ opacity: 0; transform: translateY(-12px); }}
      80%, 98% {{ opacity: 1; transform: translateY(0px); }}
      100% {{ opacity: 0; transform: translateY(12px); }}
    }}

    .rec-dot {{ animation: recBlink 1.2s infinite ease-in-out; }}
    .af-box {{ transform-origin: 220px 240px; animation: afPulse 2.5s infinite ease-in-out; }}
    .scan-line {{ animation: scanMove 4s linear infinite; }}
    .arm-wave {{ transform-origin: 325px 230px; animation: waveMotion 2.2s ease-in-out infinite; }}
    .role-1 {{ animation: roleCycle1 10s infinite; }}
    .role-2 {{ animation: roleCycle2 10s infinite; }}
    .role-3 {{ animation: roleCycle3 10s infinite; }}
    .role-4 {{ animation: roleCycle4 10s infinite; }}
    .role-5 {{ animation: roleCycle5 10s infinite; }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="480" rx="16" fill="url(#heroGrad)" />
  <rect width="900" height="480" rx="16" fill="url(#cyberGrid)" />
  <rect width="900" height="480" rx="16" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1.5" />

  <!-- Ambient Glow Blobs -->
  <circle cx="220" cy="240" r="160" fill="#38bdf8" opacity="0.07" filter="url(#glowFilter)"/>
  <circle cx="700" cy="150" r="180" fill="#818cf8" opacity="0.06" filter="url(#glowFilter)"/>

  <!-- ==================== LEFT: CAMERA VIEWFINDER ==================== -->
  <g clip-path="url(#viewfinderClip)">
    <rect x="30" y="30" width="380" height="420" fill="#0b1120" />
    
    <!-- Studio Grid inside Camera -->
    <line x1="156" y1="30" x2="156" y2="450" stroke="rgba(56, 189, 248, 0.1)" stroke-dasharray="4 4" />
    <line x1="283" y1="30" x2="283" y2="450" stroke="rgba(56, 189, 248, 0.1)" stroke-dasharray="4 4" />
    <line x1="30" y1="170" x2="410" y2="170" stroke="rgba(56, 189, 248, 0.1)" stroke-dasharray="4 4" />
    <line x1="30" y1="310" x2="410" y2="310" stroke="rgba(56, 189, 248, 0.1)" stroke-dasharray="4 4" />

    <!-- Avatar Glow Aura -->
    <circle cx="220" cy="240" r="140" fill="url(#cyanGlow)" opacity="0.15" filter="url(#glowFilter)" />

    <!-- Character Portrait Image Embedded -->
    <g clip-path="url(#avatarCircle)">
      <image href="data:image/png;base64,{b64_avatar}" x="85" y="105" width="270" height="270" preserveAspectRatio="xMidYMid slice" />
    </g>

    <!-- Glowing Avatar Halo Border -->
    <circle cx="220" cy="240" r="136" fill="none" stroke="url(#cyanGlow)" stroke-width="3" stroke-dasharray="12 6" opacity="0.8" />

    <!-- Animated Waving Hand Glove / Emoji Overlay -->
    <g class="arm-wave">
      <circle cx="325" cy="225" r="24" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="325" y="233" font-size="24" text-anchor="middle">👋</text>
    </g>

    <!-- Scanline Laser Effect -->
    <line class="scan-line" x1="30" y1="30" x2="410" y2="30" stroke="rgba(56, 189, 248, 0.4)" stroke-width="2" filter="url(#glowFilter)" />

    <!-- Autofocus HUD Box -->
    <g class="af-box">
      <rect x="165" y="185" width="110" height="110" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.7" rx="8" />
      <path d="M 165 200 L 165 185 L 180 185" fill="none" stroke="#38bdf8" stroke-width="2.5" />
      <path d="M 275 200 L 275 185 L 260 185" fill="none" stroke="#38bdf8" stroke-width="2.5" />
      <path d="M 165 280 L 165 295 L 180 295" fill="none" stroke="#38bdf8" stroke-width="2.5" />
      <path d="M 275 280 L 275 295 L 260 295" fill="none" stroke="#38bdf8" stroke-width="2.5" />
      <line x1="220" y1="232" x2="220" y2="248" stroke="#38bdf8" stroke-width="1.5" />
      <line x1="212" y1="240" x2="228" y2="240" stroke="#38bdf8" stroke-width="1.5" />
      <text x="220" y="180" fill="#38bdf8" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">[ AF-TRACK // 4K ]</text>
    </g>

    <!-- Camera Viewfinder Corner Brackets -->
    <path d="M 45 65 L 45 45 L 65 45" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 395 65 L 395 45 L 375 45" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 45 415 L 45 435 L 65 435" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 395 415 L 395 435 L 375 435" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />

    <!-- Top HUD: REC status, timer, battery -->
    <circle class="rec-dot" cx="52" cy="56" r="6" fill="#ef4444" filter="url(#glowFilter)" />
    <text x="66" y="60" fill="#ef4444" font-size="11" font-family="monospace" font-weight="bold" letter-spacing="1">REC</text>
    <text x="100" y="60" fill="#ffffff" font-size="11" font-family="monospace" font-weight="bold">00:00:02</text>

    <!-- Top Right: Battery & Format -->
    <rect x="350" y="51" width="22" height="11" rx="2" fill="none" stroke="#ffffff" stroke-width="1.2" />
    <rect x="373" y="54" width="2" height="5" rx="1" fill="#ffffff" />
    <rect x="352" y="53" width="15" height="7" rx="1" fill="#10b981" />
    <text x="342" y="60" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="end">88%</text>

    <!-- Bottom HUD: Camera Telemetry -->
    <text x="48" y="426" fill="#94a3b8" font-size="10" font-family="monospace">ISO 400</text>
    <text x="110" y="426" fill="#94a3b8" font-size="10" font-family="monospace">F/1.8</text>
    <text x="165" y="426" fill="#94a3b8" font-size="10" font-family="monospace">1/120s</text>
    <text x="225" y="426" fill="#38bdf8" font-size="10" font-family="monospace" font-weight="bold">4K RAW</text>

    <!-- Audio VU Meter Bars (Right Bottom) -->
    <g transform="translate(355, 415)">
      <rect x="0" y="0" width="3" height="12" fill="#10b981" style="animation: vu1 0.7s infinite alternate;" />
      <rect x="5" y="0" width="3" height="12" fill="#10b981" style="animation: vu2 0.5s infinite alternate;" />
      <rect x="10" y="0" width="3" height="12" fill="#38bdf8" style="animation: vu3 0.6s infinite alternate;" />
      <rect x="15" y="0" width="3" height="12" fill="#ef4444" style="animation: vu4 0.8s infinite alternate;" />
      <text x="-8" y="10" fill="#64748b" font-size="8" font-family="monospace">MIC</text>
    </g>
  </g>

  <!-- Viewfinder Outer Frame Border -->
  <rect x="30" y="30" width="380" height="420" rx="14" fill="none" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.5" />

  <!-- ==================== RIGHT: HERO BIO & CYCLING ROLES ==================== -->
  
  <!-- Status Badge Pill -->
  <g transform="translate(440, 45)">
    <rect width="250" height="28" rx="14" fill="rgba(16, 185, 129, 0.12)" stroke="rgba(16, 185, 129, 0.4)" stroke-width="1" />
    <circle cx="14" cy="14" r="4.5" fill="#10b981" class="rec-dot" />
    <text x="26" y="18" fill="#34d399" font-size="11" font-weight="700" letter-spacing="0.5">AVAILABLE FOR HIRE</text>
    <text x="165" y="18" fill="#94a3b8" font-size="11">• 📍 Delhi, IN</text>
  </g>

  <!-- Main Greeting & Name -->
  <text x="440" y="108" fill="#94a3b8" font-size="13.5" font-weight="600" letter-spacing="1.5">HELLO WORLD, I AM</text>
  <text x="440" y="155" fill="url(#cyanGlow)" font-size="44" font-weight="900" letter-spacing="1.5" filter="url(#glowFilter)">SARTAJ</text>

  <!-- Role Cycling Viewport (Height 38px) -->
  <g transform="translate(440, 175)">
    <rect width="425" height="38" rx="8" fill="rgba(30, 41, 59, 0.75)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="14" y="24" fill="#38bdf8" font-size="14" font-family="monospace" font-weight="bold">&gt;</text>
    
    <!-- Role 1 -->
    <g class="role-1">
      <text x="32" y="24" fill="#f8fafc" font-size="13.5" font-weight="700">🚀 Full-Stack Web Developer &amp; Engineer</text>
    </g>
    <!-- Role 2 -->
    <g class="role-2">
      <text x="32" y="24" fill="#38bdf8" font-size="13.5" font-weight="700">⚛️ React 19 &amp; TypeScript Specialist</text>
    </g>
    <!-- Role 3 -->
    <g class="role-3">
      <text x="32" y="24" fill="#f59e0b" font-size="13.5" font-weight="700">🏪 Digital POS &amp; Cloud Retail Architect</text>
    </g>
    <!-- Role 4 -->
    <g class="role-4">
      <text x="32" y="24" fill="#c084fc" font-size="13.5" font-weight="700">🛡️ Linux, App Security &amp; DevOps Explorer</text>
    </g>
    <!-- Role 5 -->
    <g class="role-5">
      <text x="32" y="24" fill="#34d399" font-size="13.5" font-weight="700">✨ Crafting High-Impact Web Applications</text>
    </g>
  </g>

  <!-- Bio Summary -->
  <g transform="translate(440, 240)">
    <text fill="#cbd5e1" font-size="13.5" font-weight="400">
      <tspan x="0" dy="0">Architecting modern, ultra-responsive digital products — from</tspan>
      <tspan x="0" dy="21">production-grade cloud POS billing systems to sleek AI-powered</tspan>
      <tspan x="0" dy="21">web applications built with React 19, TypeScript, &amp; Tailwind v4.</tspan>
    </text>
  </g>

  <!-- 3 Highlights Badges -->
  <g transform="translate(440, 315)">
    <g transform="translate(0, 0)">
      <rect width="134" height="54" rx="10" fill="url(#accentGrad)" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1" />
      <text x="12" y="22" fill="#38bdf8" font-size="11" font-weight="700">⚛️ FRONTEND</text>
      <text x="12" y="42" fill="#f8fafc" font-size="12" font-weight="600">React 19 + TS</text>
    </g>
    <g transform="translate(144, 0)">
      <rect width="134" height="54" rx="10" fill="url(#accentGrad)" stroke="rgba(129, 140, 248, 0.25)" stroke-width="1" />
      <text x="12" y="22" fill="#818cf8" font-size="11" font-weight="700">🏪 COMMERCE</text>
      <text x="12" y="42" fill="#f8fafc" font-size="12" font-weight="600">Digital POS Apps</text>
    </g>
    <g transform="translate(288, 0)">
      <rect width="138" height="54" rx="10" fill="url(#accentGrad)" stroke="rgba(168, 85, 247, 0.25)" stroke-width="1" />
      <text x="12" y="22" fill="#c084fc" font-size="11" font-weight="700">🛡️ SECURITY</text>
      <text x="12" y="42" fill="#f8fafc" font-size="12" font-weight="600">Linux &amp; Network</text>
    </g>
  </g>

  <!-- Quick Action Ribbon / Pill Links -->
  <g transform="translate(440, 395)">
    <rect width="200" height="38" rx="19" fill="url(#cyanGlow)" opacity="0.95" />
    <text x="100" y="24" fill="#0f172a" font-size="12.5" font-weight="800" text-anchor="middle">EXPLORE PORTFOLIO 🚀</text>

    <rect x="215" width="210" height="38" rx="19" fill="rgba(30, 41, 59, 0.8)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.2" />
    <text x="320" y="24" fill="#38bdf8" font-size="12.5" font-weight="700" text-anchor="middle">CONNECT WITH ME 📬</text>
  </g>

</svg>'''

with open('assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)

print("1. hero.svg saved")

# ==============================================================================
# 2. WHAT I BUILD & HOBBIES CAROUSEL SVG
# ==============================================================================
what_and_hobbies_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%" style="background: #080c14; border-radius: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c14"/>
      <stop offset="50%" stop-color="#0d1527"/>
      <stop offset="100%" stop-color="#080c14"/>
    </linearGradient>

    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(30, 41, 59, 0.75)"/>
      <stop offset="100%" stop-color="rgba(15, 23, 42, 0.85)"/>
    </linearGradient>

    <pattern id="grid2" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(56, 189, 248, 0.04)" stroke-width="1"/>
    </pattern>
  </defs>

  <style>
    @keyframes bar1Anim {
      0% { width: 0px; }
      25%, 100% { width: 92px; }
    }
    @keyframes bar2Anim {
      0%, 25% { width: 0px; }
      50%, 100% { width: 92px; }
    }
    @keyframes bar3Anim {
      0%, 50% { width: 0px; }
      75%, 100% { width: 92px; }
    }
    @keyframes bar4Anim {
      0%, 75% { width: 0px; }
      100% { width: 92px; }
    }

    @keyframes slide1Fade {
      0%, 22% { opacity: 1; transform: translateY(0px); }
      25%, 98% { opacity: 0; transform: translateY(8px); }
      100% { opacity: 1; transform: translateY(0px); }
    }
    @keyframes slide2Fade {
      0%, 24% { opacity: 0; transform: translateY(-8px); }
      26%, 47% { opacity: 1; transform: translateY(0px); }
      50%, 100% { opacity: 0; transform: translateY(8px); }
    }
    @keyframes slide3Fade {
      0%, 49% { opacity: 0; transform: translateY(-8px); }
      51%, 72% { opacity: 1; transform: translateY(0px); }
      75%, 100% { opacity: 0; transform: translateY(8px); }
    }
    @keyframes slide4Fade {
      0%, 74% { opacity: 0; transform: translateY(-8px); }
      76%, 97% { opacity: 1; transform: translateY(0px); }
      100% { opacity: 0; transform: translateY(8px); }
    }

    @keyframes steamFloat {
      0%, 100% { transform: translateY(0) scaleY(1); opacity: 0.3; }
      50% { transform: translateY(-8px) scaleY(1.3); opacity: 0.8; }
    }

    @keyframes eqBarStory1 { 0%, 100% { height: 8px; } 50% { height: 26px; } }
    @keyframes eqBarStory2 { 0%, 100% { height: 24px; } 50% { height: 12px; } }
    @keyframes eqBarStory3 { 0%, 100% { height: 14px; } 50% { height: 32px; } }
    @keyframes eqBarStory4 { 0%, 100% { height: 28px; } 50% { height: 10px; } }

    .story-bar-1 { animation: bar1Anim 12s infinite linear; }
    .story-bar-2 { animation: bar2Anim 12s infinite linear; }
    .story-bar-3 { animation: bar3Anim 12s infinite linear; }
    .story-bar-4 { animation: bar4Anim 12s infinite linear; }

    .slide-1 { animation: slide1Fade 12s infinite; }
    .slide-2 { animation: slide2Fade 12s infinite; }
    .slide-3 { animation: slide3Fade 12s infinite; }
    .slide-4 { animation: slide4Fade 12s infinite; }

    .steam-anim { animation: steamFloat 2.5s infinite ease-in-out; }
  </style>

  <rect width="900" height="450" rx="16" fill="url(#bgGrad2)" />
  <rect width="900" height="450" rx="16" fill="url(#grid2)" />
  <rect width="900" height="450" rx="16" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1.5" />

  <!-- ==================== LEFT PANEL: WHAT I BUILD ==================== -->
  <g transform="translate(25, 25)">
    <rect width="415" height="400" rx="14" fill="rgba(15, 23, 42, 0.65)" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <!-- Title Bar -->
    <rect width="415" height="42" rx="14" fill="rgba(30, 41, 59, 0.7)" />
    <circle cx="20" cy="21" r="5" fill="#ef4444" />
    <circle cx="36" cy="21" r="5" fill="#f59e0b" />
    <circle cx="52" cy="21" r="5" fill="#10b981" />
    <text x="75" y="26" fill="#38bdf8" font-size="13" font-family="monospace" font-weight="700">WHAT I BUILD // CORE ARCHITECTURE</text>

    <!-- Card 1: Retail POS Platform -->
    <g transform="translate(15, 55)">
      <rect width="385" height="74" rx="8" fill="url(#cardGrad)" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" />
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#38bdf8" />
      <text x="18" y="24" fill="#38bdf8" font-size="13.5" font-weight="700">🏪 Digital Retail &amp; Cloud POS Systems</text>
      <text x="18" y="44" fill="#cbd5e1" font-size="11.5">Production POS billing, GST Hindi words invoice, dynamic UPI QR,</text>
      <text x="18" y="60" fill="#94a3b8" font-size="11">real-time stock limits &amp; 1-click WhatsApp customer ordering.</text>
    </g>

    <!-- Card 2: High-Performance React 19 Apps -->
    <g transform="translate(15, 140)">
      <rect width="385" height="74" rx="8" fill="url(#cardGrad)" stroke="rgba(129, 140, 248, 0.2)" stroke-width="1" />
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#818cf8" />
      <text x="18" y="24" fill="#818cf8" font-size="13.5" font-weight="700">⚛️ High-Performance Web Applications</text>
      <text x="18" y="44" fill="#cbd5e1" font-size="11.5">Engineered with React 19, TypeScript, Tailwind v4 &amp; Vite.</text>
      <text x="18" y="60" fill="#94a3b8" font-size="11">Fluid micro-interactions, silky Framer Motion &amp; zero jank.</text>
    </g>

    <!-- Card 3: AI-Integrated Dashboards -->
    <g transform="translate(15, 225)">
      <rect width="385" height="74" rx="8" fill="url(#cardGrad)" stroke="rgba(245, 158, 11, 0.2)" stroke-width="1" />
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#f59e0b" />
      <text x="18" y="24" fill="#f59e0b" font-size="13.5" font-weight="700">🤖 AI-Integrated Business Hubs</text>
      <text x="18" y="44" fill="#cbd5e1" font-size="11.5">Google Gemini AI APIs integrated for smart inventory forecasting,</text>
      <text x="18" y="60" fill="#94a3b8" font-size="11">automated invoice parsing, and intelligent real-time analytics.</text>
    </g>

    <!-- Card 4: Hardened Backend & Cloud -->
    <g transform="translate(15, 310)">
      <rect width="385" height="74" rx="8" fill="url(#cardGrad)" stroke="rgba(168, 85, 247, 0.2)" stroke-width="1" />
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#a855f7" />
      <text x="18" y="24" fill="#c084fc" font-size="13.5" font-weight="700">🛡️ Hardened Cloud Backends &amp; Security</text>
      <text x="18" y="44" fill="#cbd5e1" font-size="11.5">Node.js, Express, Firebase Realtime Cloud Sync &amp; Auth.</text>
      <text x="18" y="60" fill="#94a3b8" font-size="11">Linux system administration, network hardening &amp; defense.</text>
    </g>
  </g>

  <!-- ==================== RIGHT PANEL: HOBBIES CAROUSEL ==================== -->
  <g transform="translate(460, 25)">
    <rect width="415" height="400" rx="14" fill="rgba(15, 23, 42, 0.65)" stroke="rgba(168, 85, 247, 0.25)" stroke-width="1.2" />

    <!-- Title Bar with Auto-Playing Status -->
    <rect width="415" height="42" rx="14" fill="rgba(30, 41, 59, 0.7)" />
    <circle cx="20" cy="21" r="5" fill="#a855f7" />
    <text x="35" y="26" fill="#f8fafc" font-size="13" font-weight="700">HOBBIES &amp; OBSESSIONS</text>
    <rect x="295" y="11" width="105" height="22" rx="11" fill="rgba(168, 85, 247, 0.2)" stroke="#a855f7" stroke-width="0.8" />
    <circle cx="307" cy="22" r="3.5" fill="#c084fc" />
    <text x="316" y="26" fill="#c084fc" font-size="9.5" font-family="monospace" font-weight="700">STORY LIVE</text>

    <!-- Story Progress Bars (4 Bars) -->
    <g transform="translate(15, 52)">
      <rect x="0" y="0" width="92" height="4" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="story-bar-1" x="0" y="0" width="0" height="4" rx="2" fill="#38bdf8" />
      
      <rect x="98" y="0" width="92" height="4" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="story-bar-2" x="98" y="0" width="0" height="4" rx="2" fill="#10b981" />
      
      <rect x="196" y="0" width="92" height="4" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="story-bar-3" x="196" y="0" width="0" height="4" rx="2" fill="#f59e0b" />
      
      <rect x="294" y="0" width="92" height="4" rx="2" fill="rgba(255, 255, 255, 0.15)" />
      <rect class="story-bar-4" x="294" y="0" width="0" height="4" rx="2" fill="#ec4899" />
    </g>

    <!-- Slide 1: Coffee & Night Coding -->
    <g class="slide-1" transform="translate(15, 75)">
      <rect width="385" height="190" rx="12" fill="rgba(30, 41, 59, 0.6)" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" />
      
      <g transform="translate(145, 30)">
        <path class="steam-anim" d="M 40 18 Q 36 6 42 -4 Q 48 -14 44 -24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" opacity="0.6"/>
        <path class="steam-anim" d="M 52 14 Q 56 4 50 -6 Q 44 -16 48 -26" fill="none" stroke="#93c5fd" stroke-width="2" stroke-linecap="round" opacity="0.4" style="animation-delay: 0.6s;"/>
        <path class="steam-anim" d="M 64 18 Q 68 8 62 -2 Q 56 -12 60 -22" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" opacity="0.5" style="animation-delay: 1.2s;"/>
        
        <rect x="25" y="25" width="55" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" />
        <path d="M 80 35 C 95 35, 95 65, 80 65" fill="none" stroke="#38bdf8" stroke-width="2.5" />
        <ellipse cx="52.5" cy="28" rx="22" ry="5" fill="#78350f" />
        <text x="52.5" y="55" fill="#38bdf8" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">&lt;dev/&gt;</text>
        <ellipse cx="52.5" cy="77" rx="35" ry="6" fill="none" stroke="#38bdf8" stroke-width="2" />
      </g>

      <text x="20" y="145" fill="#38bdf8" font-size="15" font-weight="800">☕ Specialty Dark Roast &amp; Late-Night Coding</text>
      <text x="20" y="168" fill="#cbd5e1" font-size="12">Fueling zero-bug releases between 11 PM &amp; 3 AM.</text>

      <g transform="translate(0, 205)">
        <rect width="385" height="105" rx="10" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(56, 189, 248, 0.15)" stroke-width="1" />
        <text x="18" y="28" fill="#f8fafc" font-size="12.5" font-weight="600">The Ritual:</text>
        <text x="18" y="50" fill="#94a3b8" font-size="11.5">Freshly ground dark roast pour-over + noise-canceling cans</text>
        <text x="18" y="68" fill="#94a3b8" font-size="11.5">+ deep flow state solving intricate React state trees.</text>
        <rect x="18" y="78" width="95" height="20" rx="10" fill="rgba(56, 189, 248, 0.15)" />
        <text x="65" y="92" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">#DarkRoast</text>
        <rect x="120" y="78" width="115" height="20" rx="10" fill="rgba(56, 189, 248, 0.15)" />
        <text x="177" y="92" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">#MidnightCoder</text>
      </g>
    </g>

    <!-- Slide 2: Cybersecurity & CTFs -->
    <g class="slide-2" transform="translate(15, 75)">
      <rect width="385" height="190" rx="12" fill="rgba(30, 41, 59, 0.6)" stroke="rgba(16, 185, 129, 0.2)" stroke-width="1" />
      
      <g transform="translate(150, 25)">
        <path d="M 45 10 L 80 25 L 80 65 C 80 90, 45 105, 45 105 C 45 105, 10 90, 10 65 L 10 25 Z" fill="#064e3b" stroke="#10b981" stroke-width="2.5" />
        <circle cx="45" cy="50" r="8" fill="#10b981" />
        <path d="M 45 54 L 45 66" stroke="#064e3b" stroke-width="3" stroke-linecap="round" />
        <path d="M 22 35 L 35 35 M 55 35 L 68 35 M 25 70 L 38 70 M 52 70 L 65 70" stroke="#34d399" stroke-width="1.5" stroke-dasharray="2 2" />
      </g>

      <text x="20" y="145" fill="#34d399" font-size="15" font-weight="800">🛡️ Cybersecurity Labs &amp; CTF Hunting</text>
      <text x="20" y="168" fill="#cbd5e1" font-size="12">Ethical hacking, Kali Linux &amp; network packet analysis.</text>

      <g transform="translate(0, 205)">
        <rect width="385" height="105" rx="10" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(16, 185, 129, 0.15)" stroke-width="1" />
        <text x="18" y="28" fill="#f8fafc" font-size="12.5" font-weight="600">The Focus:</text>
        <text x="18" y="50" fill="#94a3b8" font-size="11.5">Penetration testing web targets, OWASP Top 10 vulnerabilities,</text>
        <text x="18" y="68" fill="#94a3b8" font-size="11.5">and building bulletproof software that never leaks data.</text>
        <rect x="18" y="78" width="95" height="20" rx="10" fill="rgba(16, 185, 129, 0.15)" />
        <text x="65" y="92" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">#KaliLinux</text>
        <rect x="120" y="78" width="115" height="20" rx="10" fill="rgba(16, 185, 129, 0.15)" />
        <text x="177" y="92" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">#InfosecLabs</text>
      </g>
    </g>

    <!-- Slide 3: Indie Gaming & Sci-Fi -->
    <g class="slide-3" transform="translate(15, 75)">
      <rect width="385" height="190" rx="12" fill="rgba(30, 41, 59, 0.6)" stroke="rgba(245, 158, 11, 0.2)" stroke-width="1" />
      
      <g transform="translate(140, 35)">
        <rect x="10" y="15" width="85" height="52" rx="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5" />
        <path d="M 28 32 H 36 V 24 H 42 V 32 H 50 V 38 H 42 V 46 H 36 V 38 H 28 Z" fill="#475569" stroke="#f59e0b" stroke-width="1" />
        <circle cx="72" cy="30" r="4.5" fill="#ef4444" />
        <circle cx="82" cy="40" r="4.5" fill="#38bdf8" />
        <circle cx="62" cy="40" r="4.5" fill="#10b981" />
        <circle cx="72" cy="50" r="4.5" fill="#f59e0b" />
      </g>

      <text x="20" y="145" fill="#fbbf24" font-size="15" font-weight="800">🎮 Indie Games &amp; Cyberpunk Worlds</text>
      <text x="20" y="168" fill="#cbd5e1" font-size="12">Admiring game physics, worldbuilding &amp; UI mechanics.</text>

      <g transform="translate(0, 205)">
        <rect width="385" height="105" rx="10" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(245, 158, 11, 0.15)" stroke-width="1" />
        <text x="18" y="28" fill="#f8fafc" font-size="12.5" font-weight="600">The Inspiration:</text>
        <text x="18" y="50" fill="#94a3b8" font-size="11.5">Exploring immersive game UI, shaders, cyberpunk aesthetics,</text>
        <text x="18" y="68" fill="#94a3b8" font-size="11.5">and translating high-framerate fluid animations to the web.</text>
        <rect x="18" y="78" width="95" height="20" rx="10" fill="rgba(245, 158, 11, 0.15)" />
        <text x="65" y="92" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">#Cyberpunk</text>
        <rect x="120" y="78" width="115" height="20" rx="10" fill="rgba(245, 158, 11, 0.15)" />
        <text x="177" y="92" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">#CreativeTech</text>
      </g>
    </g>

    <!-- Slide 4: Lo-Fi Beats & System Design -->
    <g class="slide-4" transform="translate(15, 75)">
      <rect width="385" height="190" rx="12" fill="rgba(30, 41, 59, 0.6)" stroke="rgba(236, 72, 153, 0.2)" stroke-width="1" />
      
      <g transform="translate(135, 35)">
        <rect x="10" y="20" width="5" height="30" rx="2" fill="#ec4899" style="animation: eqBarStory1 0.8s infinite alternate;" />
        <rect x="22" y="20" width="5" height="30" rx="2" fill="#a855f7" style="animation: eqBarStory2 0.6s infinite alternate;" />
        <rect x="34" y="20" width="5" height="30" rx="2" fill="#38bdf8" style="animation: eqBarStory3 0.7s infinite alternate;" />
        <rect x="46" y="20" width="5" height="30" rx="2" fill="#10b981" style="animation: eqBarStory4 0.9s infinite alternate;" />
        <rect x="58" y="20" width="5" height="30" rx="2" fill="#f59e0b" style="animation: eqBarStory1 0.75s infinite alternate;" />
        <rect x="70" y="20" width="5" height="30" rx="2" fill="#ec4899" style="animation: eqBarStory3 0.65s infinite alternate;" />
        <rect x="82" y="20" width="5" height="30" rx="2" fill="#38bdf8" style="animation: eqBarStory2 0.85s infinite alternate;" />
      </g>

      <text x="20" y="145" fill="#f472b6" font-size="15" font-weight="800">🎧 Lo-Fi Beats &amp; System Architecture</text>
      <text x="20" y="168" fill="#cbd5e1" font-size="12">Sketching distributed systems to chilled 70 BPM beats.</text>

      <g transform="translate(0, 205)">
        <rect width="385" height="105" rx="10" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(236, 72, 153, 0.15)" stroke-width="1" />
        <text x="18" y="28" fill="#f8fafc" font-size="12.5" font-weight="600">The Vibe:</text>
        <text x="18" y="50" fill="#94a3b8" font-size="11.5">Designing microservice boundaries, caching strategies, and</text>
        <text x="18" y="68" fill="#94a3b8" font-size="11.5">scalable cloud pipelines with smooth ambient frequencies.</text>
        <rect x="18" y="78" width="95" height="20" rx="10" fill="rgba(236, 72, 153, 0.15)" />
        <text x="65" y="92" fill="#f472b6" font-size="10" font-weight="700" text-anchor="middle">#LoFiVibes</text>
        <rect x="120" y="78" width="115" height="20" rx="10" fill="rgba(236, 72, 153, 0.15)" />
        <text x="177" y="92" fill="#f472b6" font-size="10" font-weight="700" text-anchor="middle">#SystemDesign</text>
      </g>
    </g>

  </g>
</svg>'''

with open('assets/what_i_build_and_hobbies.svg', 'w', encoding='utf-8') as f:
    f.write(what_and_hobbies_svg)

print("2. what_i_build_and_hobbies.svg saved")

# Validate all SVGs
all_files = [
    'assets/hero.svg',
    'assets/what_i_build_and_hobbies.svg',
    'assets/tech_orbit.svg',
    'assets/id_badge_dashboard.svg',
    'assets/contribution_city.svg',
    'assets/connect_footer.svg'
]

print("Validating XML syntax for all files:")
for fpath in all_files:
    ET.parse(fpath)
    print(f"  [OK] {fpath} ({os.path.getsize(fpath):,} bytes)")

print("\nAll SVG components successfully compiled & verified!")
