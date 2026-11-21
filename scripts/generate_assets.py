#!/usr/bin/env python3
"""
Custom SVG Asset Generator for AlulCode45 GitHub Profile Repository.
Generates bespoke editorial & terminal-grade SVG graphics and renders github-header-banner.png via rsvg-convert.
"""

import os
import subprocess

BASE_DIR = "/Users/macbookair/Project/AlulCode45"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)


def write_svg(filename: str, content: str) -> str:
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated {path}")
    return path


# 1. HERO BANNER SVG (1200 x 380)
HERO_BANNER_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#07070B"/>
      <stop offset="50%" stop-color="#0C0A14"/>
      <stop offset="100%" stop-color="#080B12"/>
    </linearGradient>

    <radialGradient id="purpleGlow" cx="25%" cy="30%" r="55%">
      <stop offset="0%" stop-color="#9814DC" stop-opacity="0.22"/>
      <stop offset="50%" stop-color="#6366F1" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="#07070B" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="cyanGlow" cx="85%" cy="75%" r="50%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.16"/>
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#07070B" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C084FC"/>
      <stop offset="45%" stop-color="#9814DC"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>

    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#9814DC" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#334155" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="0.5"/>
    </linearGradient>

    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#13111C" stop-opacity="0.92"/>
      <stop offset="100%" stop-color="#0B0A10" stop-opacity="0.96"/>
    </linearGradient>

    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1E293B" stroke-width="0.7" stroke-opacity="0.45"/>
      <circle cx="40" cy="40" r="1" fill="#475569" fill-opacity="0.4"/>
    </pattern>

    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }
    .pulse { animation: pulseAnim 2.4s infinite ease-in-out; }
    @keyframes pulseAnim {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.35; }
    }
  </style>

  <!-- Base Canvas -->
  <rect width="1200" height="380" rx="18" fill="url(#bgGrad)"/>
  <rect width="1200" height="380" rx="18" fill="url(#purpleGlow)"/>
  <rect width="1200" height="380" rx="18" fill="url(#cyanGlow)"/>
  <rect width="1200" height="380" rx="18" fill="url(#gridPattern)"/>

  <!-- Top & Bottom Architectural Accent Lines -->
  <rect x="0" y="0" width="1200" height="3" fill="url(#accentGrad)"/>
  <line x1="56" y1="54" x2="1144" y2="54" stroke="#1E293B" stroke-width="1"/>
  <line x1="56" y1="334" x2="1144" y2="334" stroke="#1E293B" stroke-width="1"/>

  <!-- Outer Frame Border -->
  <rect x="1" y="1" width="1198" height="378" rx="17" fill="none" stroke="url(#borderGrad)" stroke-width="1.5"/>

  <!-- Top Editorial Metadata Bar -->
  <g transform="translate(56, 34)">
    <text x="0" y="0" fill="#94A3B8" font-size="11" font-weight="600" letter-spacing="2.5" class="font-mono">VOL. 2026 // DIGITAL MONOGRAPH &amp; ENGINEERING DOSSIER</text>
    <text x="595" y="0" fill="#64748B" font-size="11" font-weight="500" letter-spacing="1.5" class="font-mono">LOC: MALANG, ID (7.9666° S, 112.6326° E)</text>
    <circle cx="950" cy="-4" r="4" fill="#10B981" class="pulse"/>
    <text x="962" y="0" fill="#10B981" font-size="11" font-weight="600" letter-spacing="1.5" class="font-mono">SYS.STATUS: ONLINE</text>
  </g>

  <!-- Left Column: Identity & AC Monogram -->
  <g transform="translate(56, 82)">
    <!-- AC Monogram Badge -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="52" height="52" rx="12" fill="#151221" stroke="url(#accentGrad)" stroke-width="1.5"/>
      <text x="26" y="33" text-anchor="middle" fill="#F8FAFC" font-size="20" font-weight="800" letter-spacing="1" class="font-mono">AC</text>
    </g>

    <!-- Status Pill -->
    <g transform="translate(68, 6)">
      <rect x="0" y="0" width="335" height="24" rx="12" fill="#1A1228" stroke="#9814DC" stroke-width="1" stroke-opacity="0.6"/>
      <circle cx="14" cy="12" r="3.5" fill="#C084FC"/>
      <text x="26" y="16" fill="#E9D5FF" font-size="10.5" font-weight="600" letter-spacing="1.4" class="font-mono">LEAD FULLSTACK DEVELOPER &amp; ARCHITECT</text>
    </g>

    <text x="68" y="46" fill="#64748B" font-size="12" font-weight="500" letter-spacing="1" class="font-mono">@AlulCode45  •  alulcode.vercel.app</text>

    <!-- Full Name Headline -->
    <text x="0" y="102" fill="#F8FAFC" font-size="36" font-weight="800" letter-spacing="-0.5" class="font-sans">Muhammad Khoyron</text>
    <text x="0" y="144" fill="url(#accentGrad)" font-size="34" font-weight="800" letter-spacing="-0.5" class="font-sans">Ahlaqul Firdaus</text>

    <!-- Editorial Thesis Tagline -->
    <text x="0" y="182" fill="#CBD5E1" font-size="14.5" font-weight="400" class="font-sans">
      Building resilient digital systems with <tspan fill="#F8FAFC" font-weight="600">clarity</tspan>, <tspan fill="#C084FC" font-weight="600">substance</tspan>, and <tspan fill="#38BDF8" font-weight="600">mechanical rigor</tspan>.
    </text>

    <!-- Architecture Tags -->
    <g transform="translate(0, 202)">
      <rect x="0" y="0" width="142" height="28" rx="6" fill="#111827" stroke="#334155" stroke-width="1"/>
      <text x="71" y="18" text-anchor="middle" fill="#E2E8F0" font-size="11.5" font-weight="600" class="font-mono">Next.js / React</text>

      <rect x="152" y="0" width="146" height="28" rx="6" fill="#111827" stroke="#334155" stroke-width="1"/>
      <text x="225" y="18" text-anchor="middle" fill="#E2E8F0" font-size="11.5" font-weight="600" class="font-mono">Laravel / PHP 8+</text>

      <rect x="308" y="0" width="148" height="28" rx="6" fill="#111827" stroke="#334155" stroke-width="1"/>
      <text x="382" y="18" text-anchor="middle" fill="#E2E8F0" font-size="11.5" font-weight="600" class="font-mono">TypeScript / SQL</text>

      <rect x="466" y="0" width="142" height="28" rx="6" fill="#111827" stroke="#334155" stroke-width="1"/>
      <text x="537" y="18" text-anchor="middle" fill="#E2E8F0" font-size="11.5" font-weight="600" class="font-mono">Docker / Linux</text>
    </g>
  </g>

  <!-- Right Column: Architectural Telemetry Terminal Card -->
  <g transform="translate(715, 76)">
    <!-- Terminal Drop Shadow / Glow -->
    <rect x="-2" y="-2" width="433" height="236" rx="14" fill="none" stroke="url(#accentGrad)" stroke-width="1" stroke-opacity="0.4"/>
    <rect x="0" y="0" width="429" height="232" rx="12" fill="url(#cardBg)" stroke="#1E293B" stroke-width="1.5"/>

    <!-- Terminal Window Header -->
    <path d="M 0 12 Q 0 0 12 0 L 417 0 Q 429 0 429 12 L 429 34 L 0 34 Z" fill="#181524"/>
    <line x1="0" y1="34" x2="429" y2="34" stroke="#27233A" stroke-width="1"/>
    <circle cx="18" cy="17" r="5" fill="#EF4444"/>
    <circle cx="34" cy="17" r="5" fill="#F59E0B"/>
    <circle cx="50" cy="17" r="5" fill="#10B981"/>
    <text x="214" y="21" text-anchor="middle" fill="#94A3B8" font-size="11" font-weight="600" class="font-mono">alulcode@architect:~/telemetry</text>

    <!-- Terminal Code Body -->
    <g transform="translate(20, 56)" class="font-mono" font-size="12">
      <text x="0" y="0" fill="#64748B">01</text>
      <text x="28" y="0" fill="#C084FC">const</text>
      <text x="72" y="0" fill="#38BDF8">engineer</text>
      <text x="138" y="0" fill="#94A3B8">=</text>
      <text x="152" y="0" fill="#F8FAFC">{</text>

      <text x="0" y="22" fill="#64748B">02</text>
      <text x="44" y="22" fill="#94A3B8">role:</text>
      <text x="88" y="22" fill="#A7F3D0">"Project Lead Developer"</text>
      <text x="262" y="22" fill="#94A3B8">,</text>

      <text x="0" y="44" fill="#64748B">03</text>
      <text x="44" y="44" fill="#94A3B8">org:</text>
      <text x="88" y="44" fill="#FDE68A">"PT Pusat Andalan Sukses Terpadu"</text>
      <text x="328" y="44" fill="#94A3B8">,</text>

      <text x="0" y="66" fill="#64748B">04</text>
      <text x="44" y="66" fill="#94A3B8">venture:</text>
      <text x="110" y="66" fill="#DDD6FE">"Founder @ JagatByte Studio"</text>
      <text x="314" y="66" fill="#94A3B8">,</text>

      <text x="0" y="88" fill="#64748B">05</text>
      <text x="44" y="88" fill="#94A3B8">flagships:</text>
      <text x="122" y="88" fill="#F8FAFC">[</text>
      <text x="132" y="88" fill="#38BDF8">"ATraderTerminal"</text>
      <text x="255" y="88" fill="#94A3B8">,</text>
      <text x="266" y="88" fill="#C084FC">"Boostera.ai"</text>
      <text x="362" y="88" fill="#F8FAFC">]</text>
      <text x="370" y="88" fill="#94A3B8">,</text>

      <text x="0" y="110" fill="#64748B">06</text>
      <text x="44" y="110" fill="#94A3B8">honors:</text>
      <text x="102" y="110" fill="#FDBA74">"1st Nat'l WebDev &amp; Bug Hunter"</text>
      <text x="328" y="110" fill="#94A3B8">,</text>

      <text x="0" y="132" fill="#64748B">07</text>
      <text x="44" y="132" fill="#94A3B8">philosophy:</text>
      <text x="130" y="132" fill="#F472B6">"Design × Mechanical Rigor"</text>

      <text x="0" y="154" fill="#64748B">08</text>
      <text x="28" y="154" fill="#F8FAFC">};</text>
      <rect x="52" y="143" width="8" height="14" fill="#38BDF8" class="pulse"/>
    </g>
  </g>

  <!-- Bottom Editorial Footer Bar -->
  <g transform="translate(56, 357)" class="font-mono" font-size="11" fill="#64748B">
    <text x="0" y="0">[01] INTENTION: Zero Decorative Bloat</text>
    <text x="360" y="0">[02] PERFORMANCE: Sub-Second Response &amp; 60fps UI</text>
    <text x="795" y="0">[03] ARCHITECTURE: Clean Domain Boundaries</text>
  </g>
</svg>
"""


# 2. ARCHITECTURE & ENGINEERING THESIS SVG (1200 x 270)
THESIS_CARD_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 270" width="100%" height="100%">
  <defs>
    <linearGradient id="bgCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0A10"/>
      <stop offset="100%" stop-color="#0E131F"/>
    </linearGradient>
    <linearGradient id="accentA" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#9814DC"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="accentC" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06B6D4"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="accentMid" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }
  </style>

  <!-- Card 1: Motif A (Architecture & Application) -->
  <g transform="translate(0, 0)">
    <rect x="1" y="1" width="384" height="268" rx="14" fill="url(#bgCard)" stroke="#1E293B" stroke-width="1.5"/>
    <rect x="1" y="1" width="384" height="4" rx="2" fill="url(#accentA)"/>
    
    <rect x="24" y="24" width="110" height="22" rx="6" fill="#1F122B" stroke="#9814DC" stroke-width="1" stroke-opacity="0.5"/>
    <text x="79" y="39" text-anchor="middle" fill="#E9D5FF" font-size="10.5" font-weight="700" letter-spacing="1.2" class="font-mono">[ MOTIF A // 01 ]</text>

    <text x="24" y="76" fill="#F8FAFC" font-size="19" font-weight="800" class="font-sans">Backend &amp; Systems Rigor</text>
    <text x="24" y="98" fill="#94A3B8" font-size="12.5" class="font-sans">Mechanical reliability behind every interaction.</text>

    <line x1="24" y1="114" x2="360" y2="114" stroke="#1E293B" stroke-width="1"/>

    <g transform="translate(24, 138)" class="font-sans" font-size="12.5" fill="#CBD5E1">
      <circle cx="6" cy="-4" r="3" fill="#C084FC"/>
      <text x="18" y="0"><tspan fill="#F8FAFC" font-weight="600">Relational Integrity:</tspan> Normalized PostgreSQL</text>
      <text x="18" y="18" fill="#94A3B8">schemas, ACID transactions &amp; B-Tree/GIN indexing.</text>

      <circle cx="6" cy="44" r="3" fill="#C084FC"/>
      <text x="18" y="48"><tspan fill="#F8FAFC" font-weight="600">Service Orchestration:</tspan> Laravel queues, Redis</text>
      <text x="18" y="66" fill="#94A3B8">atomic locks, policy auth &amp; idempotent pipelines.</text>

      <circle cx="6" cy="92" r="3" fill="#C084FC"/>
      <text x="18" y="96"><tspan fill="#F8FAFC" font-weight="600">Reproducible Infra:</tspan> Multi-stage Docker builds,</text>
      <text x="18" y="114" fill="#94A3B8">Nginx reverse proxies &amp; Linux daemon hardening.</text>
    </g>
  </g>

  <!-- Card 2: Motif C (Code & Creativity) -->
  <g transform="translate(408, 0)">
    <rect x="1" y="1" width="384" height="268" rx="14" fill="url(#bgCard)" stroke="#1E293B" stroke-width="1.5"/>
    <rect x="1" y="1" width="384" height="4" rx="2" fill="url(#accentC)"/>

    <rect x="24" y="24" width="110" height="22" rx="6" fill="#0D222E" stroke="#06B6D4" stroke-width="1" stroke-opacity="0.5"/>
    <text x="79" y="39" text-anchor="middle" fill="#A5F3FC" font-size="10.5" font-weight="700" letter-spacing="1.2" class="font-mono">[ MOTIF C // 02 ]</text>

    <text x="24" y="76" fill="#F8FAFC" font-size="19" font-weight="800" class="font-sans">Frontend &amp; Tactile Emotion</text>
    <text x="24" y="98" fill="#94A3B8" font-size="12.5" class="font-sans">Editorial clarity meets sub-second responsiveness.</text>

    <line x1="24" y1="114" x2="360" y2="114" stroke="#1E293B" stroke-width="1"/>

    <g transform="translate(24, 138)" class="font-sans" font-size="12.5" fill="#CBD5E1">
      <circle cx="6" cy="-4" r="3" fill="#38BDF8"/>
      <text x="18" y="0"><tspan fill="#F8FAFC" font-weight="600">State Architecture:</tspan> Strictly typed React &amp;</text>
      <text x="18" y="18" fill="#94A3B8">Next.js App Router with deterministic state flows.</text>

      <circle cx="6" cy="44" r="3" fill="#38BDF8"/>
      <text x="18" y="48"><tspan fill="#F8FAFC" font-weight="600">Zero-CLS Choreography:</tspan> Rapid paint times, 60fps</text>
      <text x="18" y="66" fill="#94A3B8">motion physics &amp; Web Worker client filtering.</text>

      <circle cx="6" cy="92" r="3" fill="#38BDF8"/>
      <text x="18" y="96"><tspan fill="#F8FAFC" font-weight="600">Design Systems:</tspan> Custom Tailwind tokens, high</text>
      <text x="18" y="114" fill="#94A3B8">contrast typography &amp; accessible component primitives.</text>
    </g>
  </g>

  <!-- Card 3: Security & Execution Discipline -->
  <g transform="translate(816, 0)">
    <rect x="1" y="1" width="383" height="268" rx="14" fill="url(#bgCard)" stroke="#1E293B" stroke-width="1.5"/>
    <rect x="1" y="1" width="383" height="4" rx="2" fill="url(#accentMid)"/>

    <rect x="24" y="24" width="130" height="22" rx="6" fill="#0B261E" stroke="#10B981" stroke-width="1" stroke-opacity="0.5"/>
    <text x="89" y="39" text-anchor="middle" fill="#A7F3D0" font-size="10.5" font-weight="700" letter-spacing="1.2" class="font-mono">[ DISCIPLINE // 03 ]</text>

    <text x="24" y="76" fill="#F8FAFC" font-size="19" font-weight="800" class="font-sans">Security &amp; Product Impact</text>
    <text x="24" y="98" fill="#94A3B8" font-size="12.5" class="font-sans">Verified resilience under real-world pressure.</text>

    <line x1="24" y1="114" x2="359" y2="114" stroke="#1E293B" stroke-width="1"/>

    <g transform="translate(24, 138)" class="font-sans" font-size="12.5" fill="#CBD5E1">
      <circle cx="6" cy="-4" r="3" fill="#10B981"/>
      <text x="18" y="0"><tspan fill="#F8FAFC" font-weight="600">Offensive &amp; Defensive Mindset:</tspan> Recognized Bug</text>
      <text x="18" y="18" fill="#94A3B8">Hunter (Responsible Vulnerability Disclosures).</text>

      <circle cx="6" cy="44" r="3" fill="#10B981"/>
      <text x="18" y="48"><tspan fill="#F8FAFC" font-weight="600">Real-Time &amp; AI Pipelines:</tspan> Low-latency WebSocket</text>
      <text x="18" y="66" fill="#94A3B8">feeds (12ms) &amp; DeepSeek/Gemini LLM synthesis.</text>

      <circle cx="6" cy="92" r="3" fill="#10B981"/>
      <text x="18" y="96"><tspan fill="#F8FAFC" font-weight="600">Championship Execution:</tspan> 2× 1st Place National</text>
      <text x="18" y="114" fill="#94A3B8">Web Dev Winner &amp; 29+ verified credentials.</text>
    </g>
  </g>
</svg>
"""


# 3. FLAGSHIP CASE STUDIES SVG (1200 x 430)
PROJECTS_SHOWCASE_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 430" width="100%" height="100%">
  <defs>
    <linearGradient id="pCardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0C14"/>
      <stop offset="100%" stop-color="#090D16"/>
    </linearGradient>
    <linearGradient id="gradPurple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#9814DC"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
    <linearGradient id="gradEmerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="gradAmber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <linearGradient id="gradIndigo" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366F1"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }
  </style>

  <!-- Project 01: ATraderTerminal Pro -->
  <g transform="translate(0, 0)">
    <rect x="1" y="1" width="588" height="202" rx="14" fill="url(#pCardBg)" stroke="#1E293B" stroke-width="1.5"/>
    <rect x="1" y="1" width="588" height="4" rx="2" fill="url(#gradPurple)"/>

    <text x="26" y="34" fill="#C084FC" font-size="11" font-weight="700" letter-spacing="1.5" class="font-mono">01 // FINANCIAL MARKET INTELLIGENCE</text>
    <rect x="442" y="18" width="122" height="22" rx="11" fill="#112220" stroke="#10B981" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="456" cy="29" r="3.5" fill="#10B981"/>
    <text x="467" y="33" fill="#A7F3D0" font-size="10" font-weight="700" letter-spacing="1" class="font-mono">PRODUCTION</text>

    <text x="26" y="68" fill="#F8FAFC" font-size="22" font-weight="800" class="font-sans">ATraderTerminal Pro</text>
    <text x="26" y="95" fill="#CBD5E1" font-size="13" class="font-sans">Bloomberg-grade institutional financial &amp; macro analytics terminal with 12ms</text>
    <text x="26" y="114" fill="#CBD5E1" font-size="13" class="font-sans">WebSocket quote streaming, Macro Bias Engine (0–100), CFTC COT positioning,</text>
    <text x="26" y="133" fill="#CBD5E1" font-size="13" class="font-sans">and DeepSeek &amp; Gemini AI Macro Strategist synthesis.</text>

    <!-- Tech Pills -->
    <g transform="translate(26, 156)" class="font-mono" font-size="11" fill="#E2E8F0">
      <rect x="0" y="0" width="74" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="37" y="16.5" text-anchor="middle">Next.js</text>

      <rect x="82" y="0" width="90" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="127" y="16.5" text-anchor="middle">TypeScript</text>

      <rect x="180" y="0" width="88" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="224" y="16.5" text-anchor="middle">WebSocket</text>

      <rect x="276" y="0" width="98" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="325" y="16.5" text-anchor="middle">DeepSeek AI</text>

      <rect x="382" y="0" width="124" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="444" y="16.5" text-anchor="middle">Python Scrapers</text>
    </g>
  </g>

  <!-- Project 02: Boostera Indonesia -->
  <g transform="translate(612, 0)">
    <rect x="1" y="1" width="587" height="202" rx="14" fill="url(#pCardBg)" stroke="#1E293B" stroke-width="1.5"/>
    <rect x="1" y="1" width="587" height="4" rx="2" fill="url(#gradEmerald)"/>

    <text x="26" y="34" fill="#38BDF8" font-size="11" font-weight="700" letter-spacing="1.5" class="font-mono">02 // AI MARKETING AUTOMATION SUITE</text>
    <rect x="442" y="18" width="122" height="22" rx="11" fill="#112220" stroke="#10B981" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="456" cy="29" r="3.5" fill="#10B981"/>
    <text x="467" y="33" fill="#A7F3D0" font-size="10" font-weight="700" letter-spacing="1" class="font-mono">PRODUCTION</text>

    <text x="26" y="68" fill="#F8FAFC" font-size="22" font-weight="800" class="font-sans">Boostera Indonesia</text>
    <text x="26" y="95" fill="#CBD5E1" font-size="13" class="font-sans">AI-powered marketing &amp; social media automation platform tailored for Indonesian</text>
    <text x="26" y="114" fill="#CBD5E1" font-size="13" class="font-sans">MSMEs (UMKM)—generating high-converting ad copy, instant campaign visuals,</text>
    <text x="26" y="133" fill="#CBD5E1" font-size="13" class="font-sans">WhatsApp storefront integration, and multi-channel content scheduling.</text>

    <!-- Tech Pills -->
    <g transform="translate(26, 156)" class="font-mono" font-size="11" fill="#E2E8F0">
      <rect x="0" y="0" width="74" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="37" y="16.5" text-anchor="middle">Next.js</text>

      <rect x="82" y="0" width="90" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="127" y="16.5" text-anchor="middle">TypeScript</text>

      <rect x="180" y="0" width="96" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="228" y="16.5" text-anchor="middle">PostgreSQL</text>

      <rect x="284" y="0" width="106" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="337" y="16.5" text-anchor="middle">WhatsApp API</text>

      <rect x="398" y="0" width="112" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="454" y="16.5" text-anchor="middle">LLM Pipelines</text>
    </g>
  </g>

  <!-- Project 03: JagatByte Studio -->
  <g transform="translate(0, 224)">
    <rect x="1" y="1" width="588" height="202" rx="14" fill="url(#pCardBg)" stroke="#1E293B" stroke-width="1.5"/>
    <rect x="1" y="1" width="588" height="4" rx="2" fill="url(#gradIndigo)"/>

    <text x="26" y="34" fill="#818CF8" font-size="11" font-weight="700" letter-spacing="1.5" class="font-mono">03 // FOUNDED DIGITAL PRODUCT STUDIO</text>
    <rect x="424" y="18" width="140" height="22" rx="11" fill="#1D1633" stroke="#818CF8" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="438" cy="29" r="3.5" fill="#818CF8"/>
    <text x="449" y="33" fill="#E0E7FF" font-size="10" font-weight="700" letter-spacing="1" class="font-mono">FOUNDER &amp; LEAD</text>

    <text x="26" y="68" fill="#F8FAFC" font-size="22" font-weight="800" class="font-sans">JagatByte Digital Startup</text>
    <text x="26" y="95" fill="#CBD5E1" font-size="13" class="font-sans">Independent digital product studio engineering institutional-grade web systems—</text>
    <text x="26" y="114" fill="#CBD5E1" font-size="13" class="font-sans">helping businesses and ambitious teams ship software with architectural clarity,</text>
    <text x="26" y="133" fill="#CBD5E1" font-size="13" class="font-sans">rapid release momentum, and long-term operational durability.</text>

    <!-- Tech Pills -->
    <g transform="translate(26, 156)" class="font-mono" font-size="11" fill="#E2E8F0">
      <rect x="0" y="0" width="118" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="59" y="16.5" text-anchor="middle">Design Systems</text>

      <rect x="126" y="0" width="74" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="163" y="16.5" text-anchor="middle">Laravel</text>

      <rect x="208" y="0" width="74" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="245" y="16.5" text-anchor="middle">Next.js</text>

      <rect x="290" y="0" width="70" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="325" y="16.5" text-anchor="middle">Docker</text>

      <rect x="368" y="0" width="136" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="436" y="16.5" text-anchor="middle">State Architecture</text>
    </g>
  </g>

  <!-- Project 04: Malang Alam Property -->
  <g transform="translate(612, 224)">
    <rect x="1" y="1" width="587" height="202" rx="14" fill="url(#pCardBg)" stroke="#1E293B" stroke-width="1.5"/>
    <rect x="1" y="1" width="587" height="4" rx="2" fill="url(#gradAmber)"/>

    <text x="26" y="34" fill="#FBBF24" font-size="11" font-weight="700" letter-spacing="1.5" class="font-mono">04 // CURATED REAL ESTATE DISCOVERY</text>
    <rect x="442" y="18" width="122" height="22" rx="11" fill="#271C10" stroke="#F59E0B" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="456" cy="29" r="3.5" fill="#F59E0B"/>
    <text x="467" y="33" fill="#FDE68A" font-size="10" font-weight="700" letter-spacing="1" class="font-mono">LIVE SYSTEM</text>

    <text x="26" y="68" fill="#F8FAFC" font-size="22" font-weight="800" class="font-sans">Malang Alam Property</text>
    <text x="26" y="95" fill="#CBD5E1" font-size="13" class="font-sans">Architectural magazine-inspired real estate discovery platform for Greater Malang.</text>
    <text x="26" y="114" fill="#CBD5E1" font-size="13" class="font-sans">Combines high-fashion editorial serif typography, cinematic image choreography,</text>
    <text x="26" y="133" fill="#CBD5E1" font-size="13" class="font-sans">interactive geospatial mapping, SEO engine, and private consultation workflows.</text>

    <!-- Tech Pills -->
    <g transform="translate(26, 156)" class="font-mono" font-size="11" fill="#E2E8F0">
      <rect x="0" y="0" width="74" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="37" y="16.5" text-anchor="middle">Next.js</text>

      <rect x="82" y="0" width="90" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="127" y="16.5" text-anchor="middle">TypeScript</text>

      <rect x="180" y="0" width="124" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="242" y="16.5" text-anchor="middle">Interactive Maps</text>

      <rect x="312" y="0" width="96" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="360" y="16.5" text-anchor="middle">PostgreSQL</text>

      <rect x="416" y="0" width="94" height="25" rx="6" fill="#161B26" stroke="#334155"/>
      <text x="463" y="16.5" text-anchor="middle">SEO Engine</text>
    </g>
  </g>
</svg>
"""


# 4. CREDENTIALS & LEADERSHIP TIMELINE SVG (1200 x 260)
CREDENTIALS_BANNER_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 260" width="100%" height="100%">
  <defs>
    <linearGradient id="credBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0A12"/>
      <stop offset="100%" stop-color="#0A101D"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="50%" stop-color="#C084FC"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }
  </style>

  <rect x="1" y="1" width="1198" height="258" rx="14" fill="url(#credBg)" stroke="#1E293B" stroke-width="1.5"/>
  <rect x="1" y="1" width="1198" height="4" rx="2" fill="url(#goldGrad)"/>

  <!-- Vertical Divider -->
  <line x1="600" y1="24" x2="600" y2="236" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Left Half: Career & Academic Leadership -->
  <g transform="translate(32, 34)">
    <text x="0" y="0" fill="#38BDF8" font-size="11" font-weight="700" letter-spacing="2" class="font-mono">01 // LEADERSHIP &amp; ACADEMIC RECORD</text>

    <!-- Item 1 -->
    <g transform="translate(0, 28)">
      <circle cx="8" cy="6" r="4" fill="#C084FC"/>
      <line x1="8" y1="14" x2="8" y2="54" stroke="#334155" stroke-width="1.5"/>
      <text x="24" y="10" fill="#F8FAFC" font-size="15" font-weight="700" class="font-sans">Project Lead Developer — PT Pusat Andalan Sukses Terpadu</text>
      <text x="24" y="30" fill="#94A3B8" font-size="12.5" class="font-sans">Leading fullstack architecture, Next.js/Laravel systems &amp; Docker deployments (2025–Present)</text>
    </g>

    <!-- Item 2 -->
    <g transform="translate(0, 86)">
      <circle cx="8" cy="6" r="4" fill="#38BDF8"/>
      <line x1="8" y1="14" x2="8" y2="54" stroke="#334155" stroke-width="1.5"/>
      <text x="24" y="10" fill="#F8FAFC" font-size="15" font-weight="700" class="font-sans">Founder &amp; Independent Consultant — JagatByte &amp; AlulCode Studio</text>
      <text x="24" y="30" fill="#94A3B8" font-size="12.5" class="font-sans">Architecting custom enterprise platforms, AI suites &amp; performance audits (2019–Present)</text>
    </g>

    <!-- Item 3 -->
    <g transform="translate(0, 144)">
      <circle cx="8" cy="6" r="4" fill="#10B981"/>
      <text x="24" y="10" fill="#F8FAFC" font-size="15" font-weight="700" class="font-sans">B.Sc. in Computer Science (Teknik Informatika) — Institut Asia Malang</text>
      <text x="24" y="30" fill="#94A3B8" font-size="12.5" class="font-sans">Co-Founder @ iTmind Community • Alumni Software Engineering SMKN 4 Bojonegoro</text>
    </g>
  </g>

  <!-- Right Half: Verified Honors & Security Disclosures (29 Official Docs) -->
  <g transform="translate(632, 34)">
    <text x="0" y="0" fill="#FBBF24" font-size="11" font-weight="700" letter-spacing="2" class="font-mono">02 // VERIFIED HONORS &amp; SECURITY DISCLOSURES (29 CREDENTIALS)</text>

    <!-- Award 1 -->
    <g transform="translate(0, 22)">
      <rect x="0" y="0" width="536" height="46" rx="8" fill="#131622" stroke="#262B3D" stroke-width="1"/>
      <rect x="14" y="10" width="74" height="26" rx="5" fill="#2A1E0D" stroke="#F59E0B" stroke-width="1" stroke-opacity="0.6"/>
      <text x="51" y="27" text-anchor="middle" fill="#FDE68A" font-size="10.5" font-weight="700" class="font-mono">1ST NAT'L</text>
      <text x="100" y="20" fill="#F8FAFC" font-size="13.5" font-weight="700" class="font-sans">Web Development Competition — INCOFEST 2024</text>
      <text x="100" y="36" fill="#94A3B8" font-size="11.5" class="font-mono">UPN "Veteran" Jawa Timur • National Championship Winner</text>
    </g>

    <!-- Award 2 -->
    <g transform="translate(0, 76)">
      <rect x="0" y="0" width="536" height="46" rx="8" fill="#131622" stroke="#262B3D" stroke-width="1"/>
      <rect x="14" y="10" width="74" height="26" rx="5" fill="#2A1E0D" stroke="#F59E0B" stroke-width="1" stroke-opacity="0.6"/>
      <text x="51" y="27" text-anchor="middle" fill="#FDE68A" font-size="10.5" font-weight="700" class="font-mono">1ST NAT'L</text>
      <text x="100" y="20" fill="#F8FAFC" font-size="13.5" font-weight="700" class="font-sans">Web Development Competition — Technifest 2022</text>
      <text x="100" y="36" fill="#94A3B8" font-size="11.5" class="font-mono">Fakultas Teknik UNJ • National Level Winner</text>
    </g>

    <!-- Award 3 -->
    <g transform="translate(0, 130)">
      <rect x="0" y="0" width="536" height="46" rx="8" fill="#131622" stroke="#262B3D" stroke-width="1"/>
      <rect x="14" y="10" width="74" height="26" rx="5" fill="#0B261E" stroke="#10B981" stroke-width="1" stroke-opacity="0.6"/>
      <text x="51" y="27" text-anchor="middle" fill="#A7F3D0" font-size="10.5" font-weight="700" class="font-mono">SEC / HOF</text>
      <text x="100" y="20" fill="#F8FAFC" font-size="13.5" font-weight="700" class="font-sans">2× Responsible Vulnerability Disclosure (Bug Hunter)</text>
      <text x="100" y="36" fill="#94A3B8" font-size="11.5" class="font-mono">ITESA Muhammadiyah &amp; Amanah Solution + KOMINFO Cyber Finalist</text>
    </g>
  </g>
</svg>
"""


def main():
    hero_path = write_svg("hero-banner.svg", HERO_BANNER_SVG)
    write_svg("engineering-thesis.svg", THESIS_CARD_SVG)
    write_svg("flagship-projects.svg", PROJECTS_SHOWCASE_SVG)
    write_svg("credentials-timeline.svg", CREDENTIALS_BANNER_SVG)

    # Convert hero-banner.svg to github-header-banner.png (2400x760 for crisp 2x retina)
    png_path = os.path.join(BASE_DIR, "github-header-banner.png")
    subprocess.run(
        ["/opt/homebrew/bin/rsvg-convert", "-w", "2400", "-h", "760", hero_path, "-o", png_path],
        check=True,
    )
    print(f"Rendered high-DPI PNG banner to {png_path}")


if __name__ == "__main__":
    main()
