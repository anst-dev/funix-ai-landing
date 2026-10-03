---
name: Vietnamese EdTech AI Masterclass
colors:
  surface: '#faf8ff'
  surface-dim: '#d3d9f3'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dce2fb'
  on-surface: '#141b2d'
  on-surface-variant: '#424655'
  inverse-surface: '#293043'
  inverse-on-surface: '#eef0ff'
  outline: '#727687'
  outline-variant: '#c2c6d8'
  surface-tint: '#0055d4'
  primary: '#0052cc'
  on-primary: '#ffffff'
  primary-container: '#0068ff'
  on-primary-container: '#fbf9ff'
  inverse-primary: '#b2c5ff'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#006375'
  on-tertiary: '#ffffff'
  tertiary-container: '#007e94'
  on-tertiary-container: '#f1fbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#acedff'
  tertiary-fixed-dim: '#4cd7f6'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#004e5c'
  background: '#faf8ff'
  on-background: '#141b2d'
  surface-variant: '#dce2fb'
typography:
  display-hero:
    fontFamily: Be Vietnam Pro
    fontSize: 56px
    fontWeight: '800'
    lineHeight: 68px
  display-hero-mobile:
    fontFamily: Be Vietnam Pro
    fontSize: 36px
    fontWeight: '800'
    lineHeight: 46px
  headline-xl:
    fontFamily: Be Vietnam Pro
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 52px
  headline-xl-mobile:
    fontFamily: Be Vietnam Pro
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 38px
  headline-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 42px
  headline-lg-mobile:
    fontFamily: Be Vietnam Pro
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Be Vietnam Pro
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 30px
  headline-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 30px
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  label-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 20px
  label-md:
    fontFamily: Be Vietnam Pro
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
  label-caps:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2rem
  margin-mobile: 1.25rem
  space-xs: 0.375rem
  space-sm: 0.75rem
  space-md: 1.25rem
  space-lg: 2rem
  space-xl: 3.5rem
---

## Brand & Style

This design system powers a high-converting Vietnamese educational technology platform delivering practical, mentor-guided artificial intelligence training. The platform communicates prestige, technological rigor, and approachability. It directly counters the anxiety of being left behind in the AI revolution by presenting mentorship as warm, accessible, and grounded in industry application.

The design movement combines **Modern High-Trust Corporate** with **Precision Tech Glow**. 
- The hero and focal intake zones employ immersive deep-space navy canvases pierced by ethereal cyan gradients, establishing forward-looking tech authority.
- The core marketing and syllabus discovery zones transition cleanly into an ultra-clean, clinical-grade light canvas that minimizes eye fatigue and maximizes syllabus readability.
- The interface feels authoritative yet encouraging, eliminating cognitive overload through scannable modular chunks, explicit typographic hierarchy, and unambiguous calls to action.

## Colors

The palette balances conversion psychology, cultural resonance in Vietnam, and modern high-tech visual cues:

- **Primary Action (Zalo Blue - `#0068FF`):** Reserved exclusively for conversion drivers, primary enrollment triggers, WhatsApp/Zalo direct inquiries, and live consultation buttons. It represents instant connectivity, frictionless communication, and high local recognition.
- **Secondary (Electric Royal Blue - `#2563EB`):** Applied to active states, secondary interactive elements, tab switches, badge fills, and structural links.
- **Tertiary (Cyber Cyan - `#06B6D4`):** Represents artificial intelligence, mentor presence, and real-time guidance. Used for radiant pill badges, decorative radial glows over deep backdrops, dynamic progress gauges, and key metric callouts.
- **Surface Navy Anchor (`#0B1224` to `#12224E`):** Serves as the dark immersion canvas for the hero, mentor showcase headers, and final conversion anchors.
- **Canvas Body Neutral (`#F6F8FC`):** The primary light background for course modules, curriculum breakdown, mentor bios, and trust proofs.
- **Card Surfaces (`#FFFFFF`):** Crisp pure white containers with 1px border perimeter (`#E2E8F0`) maintaining spatial definition over `#F6F8FC`.
- **Text & Editorial:**
  - High-contrast body text (`#0F172A`) ensures AAA contrast on white cards.
  - Subdued explanatory text (`#475569`) provides clear optical hierarchy.
  - Dark-mode typography relies on `#FFFFFF` for headlines and `#94A3B8` for secondary labels.

## Typography

The design system exclusively implements **Be Vietnam Pro**, specifically engineered for optimal diacritical rendering in the Vietnamese language. Vietnamese tone marks (dấu hỏi, dấu ngã, dấu nặng, dấu sắc, dấu huyền) require generous vertical bounding boxes; without appropriate line heights, accented glyphs collide with adjacent lines.

### Rules of Usage
- **Diacritical Protection:** Line heights must never dip below 1.35x for titles and 1.6x for continuous body text.
- **Weight Pairing:** Headlines utilize ExtraBold (`800`) and Bold (`700`) to guarantee authoritative visual weight against luminous gradient fills.
- **Letter Spacing:** Do not tighten letter-spacing on uppercase or diacritic-heavy headlines; keep tracking at `0` or `+0.01em` to prevent accent clipping.
- **Numeric Figures:** Financial counters (tuition, salary ROI, statistical metrics) use Tabular Lining figures for clear scanning.

## Layout & Spacing

The layout is built upon an 8pt base grid with a max-width container of `1240px`, structured to encourage rapid lateral scanning across complex curriculum information.

- **Desktop (1024px+):** 12-column layout with 24px (`1.5rem`) gutters and section vertical pacing using `space-xl` (56px) to 96px for breathing room.
- **Tablet (768px - 1023px):** 8-column fluid layout with 20px gutters. Dual-card grids collapse from 3 or 4 columns down to 2 columns.
- **Mobile (< 768px):** 4-column layout with 16px (`1rem`) gutters and a 20px outer margin. Layout shifts to vertical stacking, while quick-filter tags and mentor credentials use horizontal scroll carousels with peek hints.
- **Sticky CTA Dock:** Mobile viewports pin a primary consultation action to the screen bottom using a safe-area-padded dock elevated over the content.

## Elevation & Depth

Visual hierarchy leverages crisp surface separation on light canvases and ambient neon diffusion across dark surfaces.

### Light Canvas Hierarchy
- **Level 0 (Canvas):** Flat `#F6F8FC` body tone.
- **Level 1 (Crisp Cards):** Solid `#FFFFFF` with a single 1px border (`#E2E8F0`) and an extra-diffuse ambient drop shadow: `0 4px 20px -2px rgba(11, 18, 36, 0.04), 0 2px 6px -1px rgba(11, 18, 36, 0.02)`.
- **Level 2 (Hovered / Active Cards):** Elevated with a subtle upward translate (`-2px`) and expanded shadow: `0 12px 32px -4px rgba(0, 104, 255, 0.08), 0 4px 12px -2px rgba(11, 18, 36, 0.04)`. The border transitions to `#BFDBFE`.
- **Level 3 (Floating UI / Modals):** `0 24px 48px -12px rgba(11, 18, 36, 0.16)`.

### Dark Hero Depth & AI Glow
- The `#0B1224` to `#12224E` gradient serves as the deep space baseline.
- **AI Aura:** Semi-transparent Cyan (`rgba(6, 182, 212, 0.12)`) and Electric Blue (`rgba(37, 99, 235, 0.18)`) radial gradient discs with 80px Gaussian blur sit behind mentor badges, hero graphics, and key value propositions.
- **Glass Inset:** Translucent floating badges on dark hero canvases use `rgba(255, 255, 255, 0.06)` background, `backdrop-filter: blur(12px)`, and a 1px border in `rgba(255, 255, 255, 0.15)`.

## Shapes

The geometric architecture relies on **Roundedness Level 2** (`rounded-lg` = 16px / `1rem`), generating a balanced aesthetic that feels modern and friendly without sacrificing structure.

- **Primary Cards & Modals:** Standardized strictly at 16px (`1rem`). This includes course module cards, mentor profiles, testimonial callouts, and curriculum accordions.
- **Interactive Controls (Inputs, Dropdowns):** Built with 10px to 12px corner rounding to create natural visual containers for user input.
- **Conversion CTA Buttons:** Set to 12px border radius for solid authority, or full pill (`9999px`) exclusively for fast social chat prompts (e.g., "Chat cùng Mentor trên Zalo").
- **Badges & Chips:** Full pill (`9999px`) to distinguish meta labels from structural cards.

## Components

### Buttons
- **Primary CTA ("Đăng ký tư vấn" / "Nhận lộ trình"):**
  - Background: `#0068FF` (Zalo Blue).
  - Text: `#FFFFFF`, weight 700.
  - Padding: `14px 28px` (desktop), `16px 20px` (mobile).
  - Hover: Background shifts to `#0055D6`, paired with an energetic box shadow (`0 8px 24px rgba(0, 104, 255, 0.35)`). Active state applies a scale transform (`0.98`).
- **Secondary CTA ("Xem đề cương chi tiết"):**
  - Background: `#FFFFFF` on light canvas, or `rgba(255, 255, 255, 0.08)` on hero dark.
  - Border: 1.5px solid `#2563EB` (or `rgba(255, 255, 255, 0.2)` on dark).
  - Text: `#2563EB` (or `#FFFFFF`).
- **Mentor Direct Inquire Button:**
  - Includes a leading 20px Zalo icon, pill border radius, bold typography, and micro-pulse glow.

### Cards
- **Curriculum & Feature Cards:**
  - Canvas: Pure `#FFFFFF`, border-radius 16px, border 1px solid `#E2E8F0`.
  - Padding: `24px` internal padding.
  - Header: Contains a 40px rounded icon container with a soft cyan/blue tint (`rgba(6, 182, 212, 0.1)`), housing high-contrast SVG glyphs.
  - Micro-metric: Features a bold stat pill (e.g., "1 kèm 1", "3 Dự án Capstone") sitting at the card's top right.
- **Mentor Profile Card:**
  - Split presentation: Left/Top avatar with 1:1 ratio, 12px rounded image frame, and a "Live Mentor Online" status pill (`#10B981`). Right/Bottom content displaying current AI industry role (e.g., "Senior AI Engineer @ VinAI"), verified projects, and response time guarantee (< 15 mins).

### Input Fields & Lead Intake Form
- **Form Containers:** Encapsulated in elevated white cards with subtle cyan-tinted top accent bar (3px gradient from `#0068FF` to `#06B6D4`).
- **Inputs:** Height 52px, border 1.5px solid `#E2E8F0`, background `#F8FAFC`.
- **Focus State:** Border transitions cleanly to `#0068FF`, accompanied by an outer halo ring `0 0 0 3px rgba(0, 104, 255, 0.15)`.
- **Labels:** Crisp 14px SemiBold (`#334155`), placed above the field with optional micro-badge helper (e.g., "Bảo mật SĐT 100%").

### Chips & Micro-Badges
- **Status & Urgency Chips:**
  - Pill-shaped (`9999px`), padding `6px 14px`.
  - Type: AI Indicator (`bg: rgba(6, 182, 212, 0.12)`, `text: #0891B2`, `border: 1px solid rgba(6, 182, 212, 0.25)`).
  - Type: Early-Bird Discount (`bg: #EFF6FF`, `text: #1D4ED8`, `font-weight: 700`).

### Curriculum Accordion
- Collapsible syllabus units built with subtle dividers (`#E2E8F0`).
- Left-aligned numeric indices in bold monospace-friendly weights ("Module 01", "Module 02").
- Right-side disclosure chevron smoothly rotates 180 degrees on expansion, revealing practical outputs, tools taught (e.g., LangChain, Llama, OpenAI APIs), and hands-on project milestones.