# Design System — Bodhi by Dinesh AI Academy

> **Kit standard — Dinesh AI Academy brand.** Every new project receives this file as `docs/DESIGN_SYSTEM.md`.
> The ux-designer may *extend* it for a project (new screens, client logo) but never weakens contrast or replaces brand tokens
> without the user's approval. Section references to the SPEC point to the project's own `docs/SPEC.md`.
>
> Bodhi is a premium **Agentic RAG** web app (Angular). This document is the single source of truth for how every
> screen looks, moves, reads and behaves. If a component and this file disagree, **this file wins**.
>
> Brand values are taken from the live Dinesh AI Academy stylesheet (`dineshaiacademy.com/.../assets/css/site.css`).
> Anything marked **Bodhi addition** is *not* a site colour — it was added for app needs (status, data viz, accessibility).

---

## 1. Principles

| # | Principle | What it means on screen |
|---|---|---|
| 1 | **Calm canvas** | Soft blue-grey canvas (`--bg`), white surfaces, generous whitespace, one centred reading column (max 760 px). |
| 2 | **Content first** | Chrome is quiet. The answer, its sources and its steps are the hero; controls recede until needed. |
| 3 | **Soft depth** | 1 px hairline borders + navy-tinted soft shadows. Never heavy boxes or dark drop shadows. |
| 4 | **One accent** | Amber is the only accent: primary action, active nav, focus, streaming cursor, score bars, selection. Never large amber backgrounds. |
| 5 | **Motion with purpose** | 200 ms for state changes, 420 ms for panels. Nothing bounces, nothing loops forever except "working" indicators. |
| 6 | **Trustworthy** | Every answer shows *where it came from* (sources) and *how* (steps, trace). "I couldn't find that" is calm, not red. Demo mode is labelled. |
| 7 | **Demo-ready** | Every state is designed (empty, loading, streaming, success, error, disabled). Compare / Lab / Explorer read well on a 1280×720 projector. |
| 8 | **Teachable** | Technique and mode names come with a one-line plain-English hint; technical ids are shown small in mono for students. |

---

## 2. Tokens

All tokens are CSS custom properties declared once in `frontend/src/styles.scss` (via `styles/_tokens.scss`).
Components use **only** `var(--…)`. No raw hex, rgba, px font sizes, radii or shadows in component SCSS.

### 2.1 Brand primitives (private — only referenced by semantic tokens)

| Primitive | Value | Source |
|---|---|---|
| `--brand-navy` | `#10233F` | site |
| `--brand-navy-deep` | `#0A1730` | site |
| `--brand-navy-soft` | `#1B3358` | site |
| `--brand-amber` | `#F59E0B` | site |
| `--brand-amber-bright` | `#FBBF24` | site |
| `--brand-amber-light` | `#FCD34D` | site (dark text gradient) |
| `--brand-amber-600` | `#D97706` | site |
| `--brand-amber-700` | `#B45309` | site |
| `--brand-amber-800` | `#92400E` | site |
| `--gradient-brand` | `linear-gradient(135deg, #FBBF24 0%, #F59E0B 55%, #D97706 100%)` | site |
| `--gradient-dark` | `linear-gradient(135deg, #0A1730 0%, #10233F 60%, #1B3358 100%)` | site |
| `--gradient-line` | `linear-gradient(90deg, transparent, #F59E0B, transparent)` | site |

### 2.2 Semantic colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#F3F6FB` | `#0A1730` | App canvas (chat column, pages) |
| `--surface` | `#FFFFFF` | `#10233F` | Sidebar, composer, cards, tables, side panels |
| `--surface-raised` | `#FFFFFF` + `--shadow-card` | `#1B3358` | Popovers, menus, select panels, toasts, dialogs |
| `--surface-sunken` | `#EEF3FA` | `rgba(255,255,255,0.04)` | User bubble, code blocks, toggle track, skeleton, score-bar track |
| `--surface-hover` | `#EEF3FA` | `rgba(255,255,255,0.06)` | Row / nav / ghost-button hover |
| `--glass` | `rgba(255,255,255,0.7)` | `rgba(10,23,48,0.7)` ¹ | Sticky header + composer dock, with `backdrop-filter: blur(12px)` |
| `--text-strong` | `#10233F` | `#FFFFFF` | Headings, selected labels |
| `--text` | `#1B2A41` | `#E7ECF4` | Body, answers |
| `--text-muted` | `#5B6B84` | `#C9D6EA` | Hints, meta, secondary labels |
| `--text-faint` | `#64748B` | `#9FB0C8` | Placeholders, timestamps — **only on `--surface`** in light (see 2.3) |
| `--border` | `#E1E8F3` | `rgba(201,214,234,0.18)` | Hairlines, card and table borders |
| `--border-input` | `#C9D6EA` | `rgba(201,214,234,0.3)` | Text inputs, composer, select triggers |
| `--border-control` ² | `#64748B` | `#9FB0C8` | Checkbox / radio / slider-thumb outlines (need 3:1) |
| `--border-accent` | `rgba(217,119,6,0.45)` | `rgba(245,158,11,0.5)` | Hover on chips / dropzone; selected card |
| `--accent` | `#F59E0B` | `#F59E0B` | Fills only: dots, bars, cursor, active indicator. **Never text on light.** |
| `--accent-strong` | `#B45309` | `#FBBF24` | Accent **text**, links, icons, focus ring, composer focus border |
| `--accent-ink` | `#92400E` | `#FCD34D` | Accent text ≤ 13 px or on `--surface-sunken` |
| `--accent-soft` ¹ | `rgba(245,158,11,0.10)` | `rgba(245,158,11,0.14)` | Tint behind selected items, citation hover, dropzone hover |
| `--on-accent` | `#0A1730` | `#0A1730` | Text/icons on amber gradient |
| `--gradient-accent` | `var(--gradient-brand)` | `var(--gradient-brand)` | Primary button, send button, avatar, logo mark |
| `--gradient-text` ² | `linear-gradient(135deg, #B45309 0%, #92400E 100%)` | `linear-gradient(135deg, #FCD34D 0%, #F59E0B 100%)` | Display text (welcome greeting, login title) |
| `--focus` | `#B45309` | `#FBBF24` | `outline` colour for `:focus-visible` |
| `--scrim` ¹ | `rgba(10,23,48,0.45)` | `rgba(0,0,0,0.55)` | Behind drawers and dialogs |

¹ Brand colour with alpha — a Bodhi addition, not a site token.
² Bodhi addition for accessibility. The site text gradient starts at `#D97706`, which is only **2.6:1** on `#F3F6FB` (fails even large-text 3:1), so Bodhi shifts it one step darker. The site's `--border-input` (`#C9D6EA`) is 1.5:1 on white — fine for text fields that also have a label and a filled shape, but too faint for small controls, hence `--border-control`.

### 2.3 Contrast facts (computed, WCAG 2.x)

| Pair | Ratio | Verdict |
|---|---|---|
| `#1B2A41` on `#FFFFFF` / `#F3F6FB` | 14.5 / 13.4 | Body text ✅ |
| `#5B6B84` on `#FFFFFF` / `#F3F6FB` / `#EEF3FA` | 5.4 / 5.0 / 4.9 | Muted text ✅ everywhere |
| `#64748B` on `#FFFFFF` / `#F3F6FB` | 4.8 / 4.4 | Faint text ✅ on surface only, ❌ on `--bg` |
| **`#F59E0B` on `#FFFFFF`** | **2.2** | ❌ never use amber-500 for text or focus on light |
| `#D97706` on `#FFFFFF` | 2.8 | ❌ text |
| **`#B45309` on `#FFFFFF` / `#F3F6FB` / `#EEF3FA`** | **5.0 / 4.6 / 4.5** | ✅ the safe accent-text amber (borderline on sunken → use `--accent-ink`) |
| `#92400E` on `#FFFFFF` / `#EEF3FA` | 7.1 / 6.4 | ✅ small accent text |
| `#0A1730` on `#F59E0B` / `#D97706` | 8.3 / 6.3 | ✅ navy text on every stop of the button gradient |
| `#E7ECF4` / `#C9D6EA` / `#9FB0C8` on `#0A1730` | 15+ / 12.1 / 8.1 | Dark text ✅ |
| `#9FB0C8` on `#1B3358` (darkest raised surface) | 5.7 | ✅ |
| `#FBBF24` on `#0A1730` / `#1B3358` | 10.7 / 7.6 | Dark accent text ✅ |

### 2.4 Status colours — Bodhi additions (not site colours)

Chosen to harmonise with navy/amber and pass 4.5:1 as text. Always paired with an icon (never colour alone).
Warning is olive-gold, not amber, so it never reads as "the accent".

| Token | Light | Ratio on white | Dark | Ratio on `#0A1730` |
|---|---|---|---|---|
| `--success` | `#047857` | 5.5 | `#34D399` | 9.3 |
| `--warning` | `#A16207` | 4.9 | `#FCD34D` | 12+ |
| `--danger` | `#B91C1C` | 6.5 | `#F87171` | 6.4 |
| `--info` | `#1D4ED8` | 6.7 | `#60A5FA` | 7.0 |
| `--on-danger` | `#FFFFFF` | — | `#0A1730` | — |
| `--{status}-soft` | `color-mix(in srgb, var(--{status}) 8%, transparent)` | | same, 14 % | |

### 2.5 Data-visualisation palette — Bodhi addition

Document colours in the Vector Explorer map (Okabe–Ito based, colour-blind safe). Max 8; the 9th+ documents are grouped as **"Other"** in `--text-faint`.

| Token | Light | Dark |
|---|---|---|
| `--doc-1` … `--doc-8` | `#0072B2` `#D55E00` `#009E73` `#CC79A7` `#B45309` `#56B4E9` `#1B3358` `#8F7A2E` | `#56B4E9` `#E69F00` `#2BC59A` `#E3A3C8` `#FBBF24` `#9AD3F5` `#C9D6EA` `#D9C27A` |

### 2.6 Shadows

| Token | Light (site) | Dark (Bodhi addition) |
|---|---|---|
| `--shadow-none` | `none` | `none` |
| `--shadow-soft` | `0 2px 10px rgba(16,35,63,0.06)` | `0 2px 10px rgba(0,0,0,0.25)` |
| `--shadow-card` | `0 14px 30px -16px rgba(16,35,63,0.28)` | `0 14px 30px -16px rgba(0,0,0,0.6)` |
| `--shadow-glow` | `0 2px 10px rgba(16,35,63,0.06), 0 24px 48px -28px rgba(16,35,63,0.35)` | `0 2px 10px rgba(0,0,0,0.3), 0 24px 48px -28px rgba(245,158,11,0.25)` |

In dark, depth comes mainly from surface steps (`--bg` → `--surface` → `--surface-raised`) plus `--border`.

### 2.7 Radii, spacing, layers, motion

| Radius | Value | Use |
|---|---|---|
| `--radius-xs` ¹ | `6px` | Inline code, `kbd`, badges, score bars |
| `--radius-sm` | `10px` | Buttons, inputs, nav rows, avatar, chunk cards |
| `--radius-md` | `16px` | Cards, popovers, user bubble, side panel inner cards |
| `--radius-lg` | `24px` | Composer, dropzone, login card, dialogs |
| `--radius-pill` | `999px` | Chips, segmented toggle, status pill |

¹ Bodhi addition.

| Spacing (4 px base) | `--space-1` 4 · `--space-2` 8 · `--space-3` 12 · `--space-4` 16 · `--space-5` 20 · `--space-6` 24 · `--space-8` 32 · `--space-10` 40 · `--space-12` 48 · `--space-16` 64 |
|---|---|

| Layer | `--z-base` 0 · `--z-sticky` 10 (header, composer) · `--z-sidebar` 20 · `--z-scrim` 30 · `--z-drawer` 31 · `--z-popover` 40 · `--z-dialog` 50 · `--z-toast` 60 · `--z-tooltip` 70 |
|---|---|

| Motion token | Value | Use |
|---|---|---|
| `--ease-standard` | `cubic-bezier(0.4,0,0.2,1)` | Hover, colour, toggles |
| `--ease-emphasis` | `cubic-bezier(0.16,1,0.3,1)` | Panels, drawers, popovers entering |
| `--dur-fast` | `200ms` | Hover, focus, segment slide, chip state |
| `--dur-slow` | `420ms` | Side panel, drawer, timeline collapse, message enter |
| Message enter | `opacity 0→1`, `translateY(4px→0)`, `--dur-slow --ease-emphasis` | |
| Popover enter | `opacity 0→1`, `scale(.98→1)`, `--dur-fast --ease-emphasis`; exit 150 ms, no scale | |
| Skeleton shimmer | 1.4 s linear, infinite | |
| Streaming cursor pulse | opacity 1→.35→1, 1.1 s ease-in-out, infinite | |

### 2.8 Token block (copy into `styles/_tokens.scss`)

```scss
@mixin light-tokens {
  color-scheme: light;
  --bg: #F3F6FB; --surface: #FFFFFF; --surface-raised: #FFFFFF; --surface-sunken: #EEF3FA; --surface-hover: #EEF3FA;
  --glass: rgba(255,255,255,0.7);
  --text-strong: #10233F; --text: #1B2A41; --text-muted: #5B6B84; --text-faint: #64748B;
  --border: #E1E8F3; --border-input: #C9D6EA; --border-control: #64748B; --border-accent: rgba(217,119,6,0.45);
  --accent: #F59E0B; --accent-strong: #B45309; --accent-ink: #92400E; --accent-soft: rgba(245,158,11,0.10);
  --on-accent: #0A1730; --focus: #B45309; --scrim: rgba(10,23,48,0.45);
  --gradient-text: linear-gradient(135deg, #B45309 0%, #92400E 100%);
  --success: #047857; --warning: #A16207; --danger: #B91C1C; --info: #1D4ED8; --on-danger: #FFFFFF;
  --shadow-soft: 0 2px 10px rgba(16,35,63,0.06);
  --shadow-card: 0 14px 30px -16px rgba(16,35,63,0.28);
  --shadow-glow: 0 2px 10px rgba(16,35,63,0.06), 0 24px 48px -28px rgba(16,35,63,0.35);
}
@mixin dark-tokens {
  color-scheme: dark;
  --bg: #0A1730; --surface: #10233F; --surface-raised: #1B3358;
  --surface-sunken: rgba(255,255,255,0.04); --surface-hover: rgba(255,255,255,0.06); --glass: rgba(10,23,48,0.7);
  --text-strong: #FFFFFF; --text: #E7ECF4; --text-muted: #C9D6EA; --text-faint: #9FB0C8;
  --border: rgba(201,214,234,0.18); --border-input: rgba(201,214,234,0.3); --border-control: #9FB0C8;
  --border-accent: rgba(245,158,11,0.5);
  --accent: #F59E0B; --accent-strong: #FBBF24; --accent-ink: #FCD34D; --accent-soft: rgba(245,158,11,0.14);
  --on-accent: #0A1730; --focus: #FBBF24; --scrim: rgba(0,0,0,0.55);
  --gradient-text: linear-gradient(135deg, #FCD34D 0%, #F59E0B 100%);
  --success: #34D399; --warning: #FCD34D; --danger: #F87171; --info: #60A5FA; --on-danger: #0A1730;
  --shadow-soft: 0 2px 10px rgba(0,0,0,0.25);
  --shadow-card: 0 14px 30px -16px rgba(0,0,0,0.6);
  --shadow-glow: 0 2px 10px rgba(0,0,0,0.3), 0 24px 48px -28px rgba(245,158,11,0.25);
}
:root { @include light-tokens; /* + theme-independent tokens: radii, spacing, z, motion, fonts, --doc-* */ }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { @include dark-tokens; } }
:root[data-theme="dark"], .theme-dark { @include dark-tokens; }   // .theme-dark = local dark island (login card)
```

**Theme switching:** `ThemeService` writes `data-theme="light" | "dark"` on `<html>`, or removes it for **System** (default).
Choice persists in `localStorage["bodhi.theme"]`. To avoid a flash, apply it before bootstrap (small inline script in
`index.html` allowed by a CSP hash) — otherwise in an `APP_INITIALIZER`.

---

## 3. Typography

| Family token | Stack | Use |
|---|---|---|
| `--font-heading` | `"Poppins", "Inter", system-ui, sans-serif` | Headings, page titles, card titles, wordmark |
| `--font-body` | `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` | All UI and answer text |
| `--font-mono` | `"JetBrains Mono", ui-monospace, "Cascadia Code", Consolas, monospace` | Code, ids, scores, times, counts |
| `--font-flourish` | `"Dancing Script", cursive` | Tagline only (login, About). **Never** on controls, nav or data. |

Base `html { font-size: 100% }` (16 px). Sizes in `rem`; px shown for reference.

| Token | Family / weight | Size / line-height | Tracking | Use |
|---|---|---|---|---|
| `--type-display` | Poppins 700 | 40 / 48 (2.5rem) | -0.02em | Welcome greeting, login title (with `--gradient-text`) |
| `--type-h1` | Poppins 600 | 28 / 36 | -0.015em | Page titles (Compare, Retrieval Lab…) |
| `--type-h2` | Poppins 600 | 22 / 30 | -0.01em | Section titles, panel titles |
| `--type-h3` | Poppins 600 | 18 / 26 | -0.005em | Card titles, empty-state titles, `##` in answers |
| `--type-title` | Poppins 500 | 15 / 22 | 0 | Column headers, suggestion card titles |
| `--type-body-lg` | Inter 400 | 16 / 27 | 0 | Assistant answers, user messages |
| `--type-body` | Inter 400 | 15 / 24 | 0 | Default UI text, excerpts |
| `--type-body-sm` | Inter 400 | 14 / 20 | 0 | Table cells, hints in popovers |
| `--type-label` | Inter 500 | 13 / 18 | 0.005em | Buttons sm, chips, nav, field labels, step labels |
| `--type-caption` | Inter 400 | 12 / 16 | 0.01em | Disclaimer, meta lines, mode hint |
| `--type-overline` | Inter 600 | 11 / 16 | 0.08em, uppercase | Sidebar section labels ("RECENT") |
| `--type-mono` | JetBrains Mono 400 | 13 / 20 | 0 | Code blocks, ids (`hybrid`, model ids) |
| `--type-mono-num` | JetBrains Mono 600 | 12 / 16 | 0, `font-variant-numeric: tabular-nums` | Scores, durations, counts |
| `--type-flourish` | Dancing Script 600 | 22 / 30 | 0 | "Gyaan jo sach mein kaam aaye." |

Answer markdown: paragraphs 12 px apart; lists indent 20 px; tables with `--border` hairlines and `--radius-sm` outer
corners; code blocks `--surface-sunken`, 1 px `--border`, `--radius-sm`, 12×16 px padding, horizontal scroll inside the block
only; inline code `--surface-sunken`, `--radius-xs`, 2×6 px. Links `--accent-strong`, underline on hover/focus.
UI copy uses Indian/British spelling (summarise, colour) and sentence case everywhere (no Title Case Buttons).

---

## 4. Layout

### 4.1 App shell

```
┌──────────┬─────────────────────────────────────────────┬────────────┐
│ Sidebar  │ Header 56px (sticky, --glass)                │            │
│ 264px    ├─────────────────────────────────────────────┤ Side panel │
│ --surface│        Chat column (max 760px, centred)      │ 400px      │
│          │                                             │ (trace /   │
│          │ ─ Composer dock (sticky bottom, --glass) ─   │  detail)   │
└──────────┴─────────────────────────────────────────────┴────────────┘
```

| Region | Spec |
|---|---|
| **Sidebar** | 264 px, `--surface`, right 1 px `--border`, no shadow. Top: logo mark (28 px, `--radius-sm`, `--gradient-accent`, navy "L" glyph) + "Bodhi" (`--type-h3`, `--text-strong`) + "by Dinesh AI Academy" (`--type-caption`, `--text-muted`). Then **New chat** (secondary button, full width). Nav (in order): **Chat · Compare · Retrieval Lab · Vector Explorer · Documents · Admin** (Admin only for `admin` role). Then "RECENT" overline + conversation list (virtual-scrolled). Footer: user menu (avatar, name, theme, sign out). |
| **Nav row** | 40 px high, `--radius-sm`, 20 px icon + `--type-label`. Hover `--surface-hover`. Active: `--accent-soft` bg, `--text-strong`, 3 px × 20 px `--accent` bar on the left edge, `aria-current="page"`. |
| **Header** | 56 px, sticky, `--glass` + blur, bottom 1 px `--border`. Left: page / conversation title (`--type-title`, ellipsis). Right: **Model status pill**, **Demo mode** badge (when backend runs the fake LLM), theme toggle (icon button). |
| **Chat column** | `max-width: 760px; margin-inline: auto;` padding-top `--space-8`, bottom padding = composer height + `--space-6`. |
| **Composer dock** | Sticky bottom, `--glass` fading upward (`linear-gradient(to top, var(--bg) 60%, transparent)`), composer max 760 px centred, disclaimer below. |
| **Side panel** | 400 px, `--surface`, left 1 px `--border`. Header 56 px with title + close (Esc). Used by "How this was found", source excerpt (long), Explorer chunk detail. |
| **Gutters** | 16 px (xs/sm) · 24 px (md/lg) · 32 px (xl) |

### 4.2 Breakpoints

| Name | Width | Shell behaviour |
|---|---|---|
| `xs` | < 480 (design target **375**) | Sidebar = off-canvas drawer (hamburger in header, `--scrim`). Composer: mode toggle on its own row; technique/model/advanced collapse into one **Options** button → bottom sheet. Side panel = bottom sheet (max 90 vh, drag handle, Esc/close). Compare and Lab = tabs. Explorer table → card list. |
| `sm` | 480–767 | As `xs`, wider gutters. |
| `md` | 768–1023 | Sidebar = 72 px icon rail (tooltips on icons); expands as overlay. Side panel = overlay drawer from the right. |
| `lg` | 1024–1279 | Full sidebar. Side panel overlays the chat column. |
| `xl` | ≥ 1280 | Full sidebar. Side panel **docks** (pushes content). Lab grid shows 3 columns per row. |
| Projector | 1280 × 720 | Also `@media (max-height: 760px)`: welcome spacing halves, composer textarea max 5 lines, header stays 56 px. **Presenter view** (user menu toggle) sets `--font-scale: 1.125` on Compare / Lab / Explorer, collapses the sidebar to the rail, and thickens score bars 6 → 10 px. |

Rules: no horizontal page scroll at any width ≥ 320 px (wide tables and code scroll **inside** their container);
touch targets ≥ 44 × 44 px under `@media (pointer: coarse)`; safe-area insets on the composer dock (`env(safe-area-inset-bottom)`).

---

## 5. Components

Shared primitives live in `frontend/src/app/shared/ui/` (each one job). Feature components live under `features/<feature>/`.
CLAUDE.md lists `button, toggle, select, chip, card, toast, skeleton, empty-state`; this spec also needs
**`icon`, `tooltip`, `popover`, `side-panel`, `score-bar`, `status-pill`** in `shared/ui/` (architect to confirm).

**Icons:** a single `IconComponent` with inline SVGs drawn from the Lucide set (ISC licence), stroke 1.75, `currentColor`,
16 / 20 / 24 px. Vendored as static SVG — no runtime icon library. Icon names below are Lucide's; verify against the vendored version.

### 5.1 Button (`shared/ui/button`)

| Variant | Rest | Hover | Pressed | Disabled |
|---|---|---|---|---|
| **Primary** | `--gradient-accent`, text `--on-accent` (600), `--shadow-soft`, 1 px transparent border | `--shadow-glow`, gradient shifts darker (`background-position` 0→100 %, `background-size: 200%`) | shadow none | `--surface-sunken` bg, `--text-muted`, no gradient, `cursor: not-allowed` |
| **Secondary** | `--surface`, 1 px `--border-input`, `--text` | `--surface-hover` | `--surface-sunken` | same as primary-disabled |
| **Ghost** | transparent, `--text-muted` | `--surface-hover`, `--text` | `--surface-sunken` | `--text-faint` |
| **Danger** | `--danger`, text `--on-danger` | `color-mix(in srgb, var(--danger) 88%, black)` | — | as primary-disabled |

Sizes: **sm** 32 px / `--type-label` / 12 px x-pad · **md** 40 px / 14 px Inter 500 / 16 px · **lg** 48 px / 15 px / 20 px.
Radius `--radius-sm`; icon gap 8 px; icon-only buttons are square and **must** have `aria-label` + tooltip.
**Loading:** 16 px spinner replaces the leading icon, label stays, `aria-busy="true"`, clicks ignored.
**Focus:** `outline: 2px solid var(--focus); outline-offset: 2px` (all components, `:focus-visible` only).

### 5.2 Segmented toggle — Mode (`shared/ui/toggle`)

| Part | Spec |
|---|---|
| Track | `--surface-sunken`, `--radius-pill`, 3 px padding, `role="radiogroup"` `aria-label="Answer mode"` |
| Segment | 32 px high, 12 px x-pad, icon 16 + `--type-label`. Options: **Quick answer** (`zap`) · **Deep research** (`telescope`). `role="radio"`, `aria-checked` |
| Selected | `--surface` (dark: `--surface-raised`) pill, `--shadow-soft`, text `--text-strong`, icon `--accent-strong`. Pill slides `--dur-fast --ease-standard` |
| Unselected | `--text-muted`; hover `--text` |
| Hint | One line under the composer (`--type-caption`, `--text-muted`, `aria-describedby` on the group) — text in §6.2 |
| Disabled | While streaming: `opacity: .6`, `aria-disabled="true"`, tooltip "You can switch after this answer." |
| Keyboard | Tab enters the group (focus on selected); ← / → move and select; roving `tabindex` |

### 5.3 Select with hints (`shared/ui/select`, CDK Overlay + `ActiveDescendantKeyManager`)

| Part | Spec |
|---|---|
| Trigger | 32 px (composer) / 40 px (forms); `--surface`, 1 px `--border-input`, `--radius-pill` in composer, `--radius-sm` in forms; label + `chevron-down`. `role="combobox"`, `aria-expanded`, `aria-controls` |
| Panel | `--surface-raised`, `--radius-md`, `--shadow-card`, 1 px `--border`, 6 px padding, min-width 280 px, max-height 360 px (scroll). `role="listbox"` |
| Option | 2-line: **label** (`--type-label`, `--text`) + mono id (`--type-mono` 12 px, `--text-faint`) on the right; **hint** below (`--type-caption`, `--text-muted`). Active (keyboard) `--surface-hover`; selected: `check` icon `--accent-strong` + `aria-selected="true"` |
| Group header | `--type-overline`, `--text-muted`, not focusable (`role="presentation"`), e.g. **GOOGLE**, **OPENAI**, **ANTHROPIC**, **OLLAMA** |
| Badges | "Recommended" (technique default) / "Default" (model): `--accent-soft` bg, `--accent-ink`, `--radius-xs`, 11 px 600 |
| States | Loading list → 3 skeleton rows · Empty (no models configured) → disabled trigger "No models available" + tooltip "Ask an admin to add an API key." · Error → "Couldn't load models. Retry" link inside panel |
| Keyboard | Enter/Space/↓ opens; ↑/↓ move (skips headers); Home/End; type-ahead; Enter selects; Esc closes and returns focus |

**Technique select** — six options, labels and hints in §6.3. **Model select** — only allow-listed models whose key is
configured (from the API); grouped by provider; label = display name, id = model id. With one model only, the trigger shows it
as a static, non-interactive chip.

### 5.4 Advanced popover (`features/chat/advanced-popover`)

Trigger: ghost icon button `sliders-horizontal`, `aria-label="Advanced settings"`; a 6 px `--accent` dot appears when any value
differs from the default. Panel: CDK overlay, 320 px, `--surface-raised`, `--radius-md`, `--shadow-card`, 16 px padding, focus trapped.

| Field | Control | Label · hint |
|---|---|---|
| Top-k | slider + mono value | **Passages to read** · "More gives broader answers but is slower." |
| Temperature | slider (step 0.1) + mono value | **Creativity** · "Lower is focused and repeatable. Higher varies the wording." |
| Document scope | radio "All documents" / "Only these" + checkbox list (search box when > 8 docs) | **Search in** · "Bodhi only reads the documents you pick." |
| Footer | ghost **Reset to defaults** · primary sm **Done** | |

Min / max / default values come from the server settings — never hard-coded in the component.
Sliders: track 4 px `--surface-sunken`, fill `--accent`, thumb 16 px `--surface` with 2 px `--border-control`, focus ring on thumb.

### 5.5 Composer (`features/chat/composer`)

| Part | Spec |
|---|---|
| Container | `--surface`, 1 px `--border-input`, `--radius-lg`, `--shadow-glow`, 12 px padding. `:focus-within` → border `--accent-strong` + `box-shadow: 0 0 0 3px var(--accent-soft)` |
| Textarea | `--type-body-lg`, autosize 1–8 lines (5 on short screens), placeholder "Ask anything about your documents…" (`--text-faint`), `aria-label="Message Bodhi"` |
| Toolbar (left) | Mode toggle · Technique select · Model select · Advanced |
| Toolbar (right) | **Send**: 40 px circle, `--gradient-accent`, `arrow-up` in `--on-accent`, `aria-label="Send message"`. Disabled (empty / no docs): `--surface-sunken`, `--text-faint` |
| While streaming | Send becomes **Stop**: 40 px circle secondary, `square` icon, `aria-label="Stop generating"` |
| Below | Mode hint (`--type-caption`, `--text-muted`) · disclaimer centred "Bodhi can make mistakes. Check important answers against the sources." |
| xs | Row 1 textarea + send; row 2 mode toggle (full width); row 3 **Options** button (`sliders-horizontal`, shows "Hybrid · Gemini …") → bottom sheet with technique, model, advanced fields |

### 5.6 Messages (`features/chat/message-user`, `message-assistant`)

| Part | Spec |
|---|---|
| User | Right-aligned, max-width 85 %, `--surface-sunken`, `--radius-md` with bottom-right `--radius-xs`, 12×16 px padding, `--type-body-lg`, rendered with `{{ }}` (whitespace preserved) |
| Assistant | No bubble; full-width on canvas. 28 px avatar (`--radius-sm`, `--gradient-accent`, navy "L") on the left, 12 px gap. Markdown via a **sanitised** renderer |
| Meta line | Under the answer: "Hybrid · Deep research · 6.1 s" (`--type-caption`, `--text-muted`, numbers `--type-mono-num`) |
| Actions | Row of ghost icon buttons (sm): **Copy** (`copy` → "Copied" 2 s), **Retry** (`rotate-ccw`), **How this was found** (`route`, opens trace panel). Visible on hover / `:focus-within`; always visible on touch and on the latest message |
| Enter | Message-enter motion (§2.7) |
| Spacing | 24 px between messages, 32 px between turns |

**Streaming cursor:** inline block 0.5 em × 1.1 em, `--accent`, `--radius-xs`, pulse (§2.7), placed after the last token;
removed on completion. Reduced motion: static. **Before first token:** a muted line with pulsing 6 px `--accent` dot:
"Searching your documents…" (Quick) or the live timeline (Deep).

**Honest no-answer:** a normal assistant message — no red, no error icon. Text "I couldn't find that in your documents."
followed by `--text-muted` sub-line (see §6.4) and two ghost buttons: **Try Deep research** · **Check document scope**.

**Interrupted stream:** partial text stays; below it an inline note (`alert-circle` `--warning`) "The answer stopped early." + **Retry**.

### 5.7 Agent-step timeline (`features/chat/agent-steps`)

Live during Deep research; collapses after the answer into a summary row.

| Part | Spec |
|---|---|
| Container | Above the answer, `--type-label`, no card — a 1 px `--border` left rail at x = 12 px |
| Row | 28 px min height: node icon in 24 px circle · label · detail (`--text-muted`) · duration right-aligned (`--type-mono-num`, `--text-faint`) |
| Nodes · icons | **Understand** `lightbulb` · **Search** `search` · **Check** `list-checks` · **Rewrite** `refresh-cw` · **Answer** `message-square-text` · **Verify** `shield-check` |
| Pending | Circle 1 px `--border`, icon `--text-faint` (only shown for the next expected node; future nodes are not pre-listed) |
| Running | Circle 1.5 px `--accent` with a rotating 90° arc (1 s linear), icon `--accent-strong`, label `--text-strong`, detail ends with "…" |
| Done | Circle `--surface-sunken`, icon `--text-muted`; duration shown ("0.8 s") |
| Skipped | Label + "Skipped" in `--text-faint`; no duration |
| Failed | Icon `--danger`, detail = friendly reason (§6.4), timeline stops |
| Loops | A second Search after Rewrite shows "Search · 2nd pass" |
| Collapsed | One row: `chevron-right` + "Researched in {n} steps · {t} s" (`--text-muted`); button `aria-expanded`. Expands with `--dur-slow` height transition |
| Limit hit | Final row with `info` `--info`: "Stopped after {n} searches (safety limit)." |

Step detail copy is in §6.5. The list is `role="list"`; each completed step is announced politely (§7.3).

### 5.8 Source chips + excerpt (`shared/ui/chip`, `features/chat/sources`)

| Part | Spec |
|---|---|
| Row | Under the answer, 8 px gap, wraps; `role="list"` `aria-label="Sources"` |
| Chip | 28 px, `--radius-pill`, `--surface`, 1 px `--border`, 10 px x-pad, `[1]` in `--type-mono-num` `--accent-ink` + "policy.pdf · p.3" (`--type-label`, `--text`, name ellipsis at 180 px, full name in `title`) |
| Hover / open | Border `--border-accent`, bg `--accent-soft`; `aria-expanded="true"` when its excerpt is open |
| Excerpt | Inline card under the row: `--surface`, 1 px `--border`, `--radius-md`, 16 px padding; header "[1] policy.pdf · page 3" + score badge `0.82` (mono, `--surface-sunken`); body excerpt (max 600 chars, `--type-body`, matched terms in `<mark>` with `--accent-soft` bg, `--text` colour); footer ghost link "View in Vector Explorer". Esc closes and returns focus to the chip |
| Inline citations | `[1]` in the answer = superscript button (`--accent-strong`, `--type-mono-num`); click focuses + opens the matching chip |
| Empty | No chips row when the answer is the honest no-answer |

### 5.9 "How this was found" trace panel (`features/chat/trace-panel`)

Side panel (§4.1). Progressive disclosure: a normal user sees the summary; students open the details.

| Section | Content |
|---|---|
| What am I looking at? | Muted note (§6.6) |
| Summary | Key–value grid: Technique ("Hybrid" + mono `hybrid`) · Mode · Model · Total time · Passages used "{u} of {k}" |
| Passages | Ranked list: rank `#1` mono · "policy.pdf · p.3" · **score bar** (`shared/ui/score-bar`: 6 px, track `--surface-sunken`, fill `--accent`, `--radius-xs`, value mono right) · `check` `--success` + "Used" when cited |
| Steps | The agent timeline, expanded (Deep) or "Searched once" single row (Quick) |
| Technical details | Collapsed disclosure **Show technical details**: per-chunk component scores (e.g. meaning / keyword / fused / re-rank), rewritten queries, per-step timings, token counts if provided. Table `--type-body-sm`, numbers mono |
| Footer | Ghost **Copy trace as JSON** |

States: loading = skeleton rows; unavailable (old message) = empty state "No trace saved for this answer."

### 5.10 Compare (`features/compare`)

| Part | Spec |
|---|---|
| Top | Question input (same composer styling, no mode toggle) + technique + model selects; primary **Compare** |
| Columns | 2 equal columns, 24 px gap, each a card (`--surface`, `--radius-md`, 1 px `--border`). Header: mode name (`--type-title`) + hint (caption) + metrics row: time · LLM calls · passages (mono) |
| Body | Answer (streams independently), sources, timeline (Deep expanded) |
| Shared sources | Chips cited by both columns get a small "In both" badge (`--accent-soft`, `--accent-ink`) |
| States | Empty: "Ask one question. See both answers side by side." · one column fails → that column shows the error card, the other continues |
| xs–sm | Segmented tabs "Quick answer · Deep research" above a single column; metrics stay visible in each tab label (e.g. "Quick · 1.4 s") |

### 5.11 Retrieval Lab (`features/retrieval-lab`)

| Part | Spec |
|---|---|
| Top | Question input + top-k + technique filter chips (all six on by default) + primary **Run** |
| Teaching note | Under the header (caption, `info` icon): "Scores use different scales per technique. Compare the order, not the numbers." |
| Grid | `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))`, 16 px gap. At 1280 (sidebar rail) = 3 per row |
| Column header | Technique label (`--type-title`) + mono id + hint (caption, 2-line clamp) + time "84 ms" (mono) |
| Chunk card | `--surface`, 1 px `--border`, `--radius-sm`, 12 px padding: rank `#1` (mono, `--text-muted`) · "policy.pdf · p.3" · excerpt 3-line clamp (`--type-body-sm`) · score bar (width = score ÷ column max) + raw score mono |
| Shared highlight | Chunk returned by ≥ 2 techniques: badge "In {n} of {m}" (`--accent-soft`/`--accent-ink`) + 3 px `--accent` left border. Hover or focus on a card outlines the **same chunk in every column** (2 px `--accent-strong` outline) — text is never dimmed |
| States | Per column: skeleton (3 cards) → results → "No passages found." (muted) → error card with Retry. Columns finish independently |
| xs–sm | Technique tabs (scrollable tab strip inside its own container) — one column at a time; shared badge still shown |
| Projector | Presenter view (§4.2): body-sm → body, bars 10 px |

### 5.12 Vector Explorer (`features/vector-explorer`) — read-only

Header shows a neutral **Read-only** badge (`lock` icon, `--surface-sunken`, `--text-muted`). There are **no** delete, edit or
re-index buttons on this screen. Each section has a "What am I looking at?" disclosure (`info` ghost button → muted paragraph, §6.6).

| Part | Spec |
|---|---|
| Overview cards | 4 cards in a row (2×2 at md, 1 col at xs): **Documents**, **Chunks**, **Embedding model** (name + "{d} dimensions"), **Average chunk size** ("{n} characters"). Card: `--surface`, `--radius-md`, `--shadow-soft`; label `--type-label` muted; value `--type-h2` (numbers mono) |
| Chunks table | Columns: # · Document · Page · Size · Preview (1-line ellipsis). Header `--type-overline`, rows 44 px, zebra off, hover `--surface-hover`, selected row `--accent-soft` + 3 px `--accent` left bar. Filter by document (select). Paged: 25 per page, footer "1–25 of 1,240" + Previous / Next (ghost). Rows are buttons (`Enter` opens detail) |
| Chunk detail | Side panel: doc · page header; full text (`--type-body`, `{{ }}`); metadata key–value list (mono values); **Embedding preview** "First 8 of {d} numbers" in mono; **Nearest neighbours** (5 rows with score bars) — clicking one opens its detail |
| 2-D map | Card with SVG (≤ 2,000 points) or `<canvas>` (more). Dots 6 px, `--doc-n` fill, 1 px `--surface` stroke; hover/focus 10 px + tooltip "policy.pdf · p.3 — first 80 characters…"; click opens detail; selected dot ringed `--accent-strong`. Legend = toggle chips per document (colour swatch + name) to show/hide. Caption: "Projected to 2-D with {method}." `role="img"` with `aria-label` summary; the table is the accessible equivalent |
| States | Empty store → empty state (§6.6). Loading → skeleton cards, 8 skeleton rows, grey map placeholder. Error → error card per section (others still load) |

### 5.13 Documents — dropzone + job status (`features/documents`)

| Part | Spec |
|---|---|
| Dropzone | 1.5 px dashed `--border-input`, `--radius-lg`, 32 px padding, centred `upload` icon (24, `--text-muted`), "Drop files here or **browse**" (`--type-body`, "browse" `--accent-strong`), caption "{types} · up to {max} MB each" (from server). Hover/drag-over: `--border-accent` solid, `--accent-soft` bg. A real `<input type="file" multiple>` behind a `<label>`; keyboard Enter/Space opens picker |
| Job row | File icon (`file-text`) · name (ellipsis) · size (mono) · status · action. Status sequence: **Queued** → **Uploading {p}%** (progress bar 4 px `--accent`) → **Reading** → **Splitting into chunks** → **Embedding {i} of {n}** → **Ready · {n} chunks** (`check` `--success`) · **Failed** (`x-circle` `--danger` + reason) with **Retry** |
| Documents table | Name · Type · Chunks · Added · ghost icon **Delete** (`trash-2`, `aria-label="Delete {name}"`) |
| Delete confirm | CDK dialog, `--radius-lg`: title "Delete “{name}”?" body "This removes the document and its {n} chunks from search. You can't undo this." Buttons **Cancel** (secondary, default focus) · **Delete document** (danger) |
| Empty | Empty state + dropzone visible |

### 5.14 Feedback

| Component | Spec |
|---|---|
| **Toast** (`shared/ui/toast`) | `--surface-raised`, `--radius-md`, `--shadow-card`, 1 px `--border`, 12×16 px, max-width 380 px; status icon (success/info/warning/danger colour) + one line + optional action link. Desktop bottom-right above the composer; xs top-centre under the header. Max 3 stacked, newest on top. Success/info auto-dismiss 4 s (paused on hover/focus); warning/error stay until closed. `role="status"` (errors `role="alert"`) |
| **Error card** | `--surface`, `--radius-md`, 1 px `--border`, 3 px left border `--danger` (or `--warning`), icon + title (`--type-title`) + one-line fix (`--text-muted`) + actions. Optional "Ref: {requestId}" in mono `--text-faint`. Never raw errors or stack traces |
| **Empty state** (`shared/ui/empty-state`) | Centred, max-width 420 px: 48 px circle `--accent-soft` with 24 px icon `--accent-strong`, title `--type-h3`, body `--text-muted`, one primary action (optional secondary) |
| **Skeleton** (`shared/ui/skeleton`) | `--surface-sunken` blocks, `--radius-xs`, shimmer (a `--surface-hover` band). Shown only after 300 ms (avoid flashes); `aria-hidden="true"`, parent has `aria-busy="true"` |
| **Model status pill** | `--radius-pill`, `--surface`, 1 px `--border`, 28 px; 8 px dot + display name. Dot: Ready `--success` · Slow `--warning` · Unavailable `--danger` · Checking `--text-faint` (pulse). Click → popover with provider, model id (mono), latency, "Change model" |
| **Demo mode badge** | `--info-soft` bg, `--info` text, `flask-conical` icon, "Demo mode", tooltip "Answers are simulated. No real AI model is called." |

### 5.15 Welcome screen (empty chat)

Vertically centred in the chat column: greeting `--type-display` with `--gradient-text` ("What would you like to know?"),
sub-line `--text-muted` "Ask about your documents. Every answer shows its sources."
2 × 2 suggestion cards (1 column at xs): `--surface`, 1 px `--border`, `--radius-md`, 16 px; title `--type-title`, hint caption;
hover `--shadow-card` + border `--border-accent`. Real `<button>`s that fill the composer and send. Cards: **Summarise** · "Give me the key points of my documents" · **Explain** · "Explain the main idea in simple words" · **Find** · "What do my documents say about deadlines?" · **Compare** · "How do my files differ on this topic?"
With **no documents**: cards are replaced by the "No documents" empty state (§6.4).

### 5.16 Login (`features/login`)

Full-viewport `--gradient-dark` background (both themes) with a faint `--gradient-line` 1 px rule near the top.
Centred card 400 px (the login page wrapper has class `.theme-dark`, so it always uses dark tokens), `--radius-lg`, `--shadow-glow`, 32 px padding:
logo mark 40 px · "Bodhi" (`--type-display`, `--gradient-text`) · "by Dinesh AI Academy" (caption muted) · tagline
"Gyaan jo sach mein kaam aaye." (`--type-flourish`, `--text-muted`) · Email field · Password field (show/hide icon button) ·
primary lg full-width **Sign in**. Fields: label above (`--type-label`), 44 px input, `--radius-sm`, error text below in
`--danger` with `alert-circle`, `aria-invalid` + `aria-describedby`. Loading: button spinner "Signing in…", fields disabled.

---

## 6. Microcopy

Voice: short, calm, specific, second person. Sentence case. No exclamation marks, no blame ("you did X wrong").

### 6.1 Labels

| Element | Label | `aria-label` / tooltip |
|---|---|---|
| New chat | New chat | "Start a new chat" |
| Send / Stop | — | "Send message" / "Stop generating" |
| Composer placeholder | Ask anything about your documents… | "Message Bodhi" |
| Advanced | — | "Advanced settings" |
| Options (xs) | Options | "Answer options" |
| Trace | How this was found | "Show how this answer was found" |
| Copy / done | Copy · Copied | "Copy answer" |
| Retry | Retry | "Try again" |
| Theme | Light · Dark · System | "Change theme" |
| Sources | — | "Sources" (list) · chip: "Source 1: policy.pdf, page 3" |
| Disclaimer | Bodhi can make mistakes. Check important answers against the sources. | |

### 6.2 Modes

| Mode | Label | Hint (one line) |
|---|---|---|
| Normal RAG | **Quick answer** | Searches your documents once, then answers. Fastest. |
| Agentic RAG | **Deep research** | Plans, searches, checks and searches again if needed. Slower, more thorough. |

### 6.3 Retrieval techniques

| id | Label | Hint |
|---|---|---|
| `dense` | Meaning search | Finds passages with similar meaning, even when the words differ. |
| `keyword` | Keyword search | Finds passages with your exact words — best for names, codes and numbers. |
| `hybrid` | Hybrid · *Recommended* | Combines meaning and exact words. A strong default. |
| `mmr` | Diverse results (MMR) | Picks relevant passages that don't repeat each other. |
| `multi_query` | Multi-question | Rewrites your question a few ways and searches with each. |
| `rerank` | Re-rank | Gathers more candidates, then re-scores them to put the best first. |

### 6.4 Errors and empty states

| Case | Title | Body / fix | Actions |
|---|---|---|---|
| 401 | Your session has ended. | Please sign in again to continue. | Redirect to login (toast) |
| 403 | You don't have access to this. | Ask an admin if you need it. | Back to chat |
| 413 | “{file}” is too large. | Files can be up to {max} MB. Try a smaller file or split it. | — |
| 415 | “{file}” isn't supported. | Use {types}. | — |
| 429 | Lots of requests right now. | Try again in {s} s. *(no Retry-After: "Try again in a moment.")* | Retry (enabled after countdown) |
| Provider down | {Provider} isn't responding. | Try again, or switch to another model. | Retry · Change model |
| Network offline | You're offline. | We'll reconnect when you're back. | — (warning toast) |
| Server error (5xx) | Something went wrong on our side. | Please try again. Ref: {requestId} | Retry |
| No documents | Add a document to get started | Bodhi answers only from documents you upload. | Upload documents |
| Couldn't find | I couldn't find that in your documents. | Try different words, switch to Deep research, or check which documents are in scope. | Try Deep research · Check document scope |
| Login failed | — | That email and password don't match. | — (no hint about which one) |
| Stream stopped | The answer stopped early. | — | Retry |

### 6.5 Agent steps (running → done)

| Node | Running | Done |
|---|---|---|
| Understand | Understanding your question… | Understood the question |
| Search | Searching '{query}'… | Searched '{query}' · {n} passages |
| Check | Checking the passages… | {k} of {n} passages are relevant |
| Rewrite | Rewriting the search… | New search: '{query}' |
| Answer | Writing the answer… | Answer written |
| Verify | Checking the answer against sources… | Supported by sources · *or* Some parts aren't fully supported (marked in the answer) |

### 6.6 "What am I looking at?" notes

| Where | Note |
|---|---|
| Trace panel | Bodhi searched your documents with {technique}, then wrote the answer from the best-scoring passages. A higher score means a closer match. |
| Overview cards | Your documents are split into small passages called chunks. Each chunk is turned into a list of numbers (an embedding) that captures its meaning. |
| Chunks table | Every row is one chunk Bodhi can search. Pick one to see its full text and its closest neighbours. |
| Chunk detail | These numbers are the chunk's embedding. Chunks with similar numbers have similar meaning. |
| 2-D map | Each dot is a chunk. Dots close together have similar meaning. Squeezing {d} dimensions into 2 loses detail, so distances are approximate. |
| Explorer empty | Nothing to explore yet · Upload a document and its chunks will appear here. · **Upload documents** |

---

## 7. Accessibility and responsive rules

### 7.1 Rules

| Area | Rule |
|---|---|
| Contrast | Text ≥ 4.5:1 (≥ 3:1 for ≥ 24 px or ≥ 19 px bold); UI boundaries and focus ≥ 3:1. Use §2.3. Amber text = `--accent-strong` / `--accent-ink` only |
| Focus | `:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }` globally; never `outline: none` without a replacement. Composer uses its focus-within border (§5.5) |
| Labels | Every control has a visible label or `aria-label`; icon buttons also get a tooltip (CDK, 400 ms delay, also on focus) |
| Colour | Never the only signal: status = icon + text; map = legend + tooltip + table; selection = bar + `aria-selected` |
| Forced colours | `@media (forced-colors: active)`: buttons keep a 1 px border, focus uses `Highlight`, score bars get a `CanvasText` border |
| Reduced motion | `@media (prefers-reduced-motion: reduce)`: all durations → `0.01ms`, no translate/scale, cursor and spinners static (spinner replaced by `loader` icon + "Working…" text), shimmer off, scroll-behavior auto |
| Auto-scroll | Follow streaming output only if the user is within 80 px of the bottom; otherwise show a "Jump to latest" pill (`arrow-down`) |
| Language | `<html lang="en">`; the Hinglish tagline wrapped in `<span lang="hi-Latn">` |

### 7.2 Keyboard map

| Key | Where | Action |
|---|---|---|
| Enter | Composer | Send |
| Shift + Enter | Composer | New line |
| Esc | Streaming | Stop generating |
| Esc | Popover / select / dialog / side panel / drawer | Close and return focus to its trigger |
| `/` | Anywhere outside a text field | Focus the composer |
| ← / → | Mode toggle, tabs | Move + select |
| ↑ / ↓, Home / End, type-ahead | Select, menus, Explorer table | Move |
| Enter / Space | Chips, rows, cards, disclosures | Open / toggle |
| Tab order | Sidebar → header → main content → composer (textarea → mode → technique → model → advanced → send) → side panel (when open, focus moves into it) |

Skip link "Skip to chat" is the first focusable element (visible on focus).

### 7.3 Live regions

| Region | Setup |
|---|---|
| Streaming answer | Message container `aria-busy="true"` while streaming. A visually hidden `aria-live="polite"` region receives text **per sentence** (not per token); on completion it announces "Answer ready. {n} sources." |
| Agent steps | `LiveAnnouncer` (polite) announces each *done* label, e.g. "Searched 'refund policy', 4 passages." |
| Errors | `role="alert"` on error cards and error toasts |
| Upload jobs | Polite announcement on Ready / Failed only (not every percent) |

---

## 8. Angular implementation notes

| Topic | Rule |
|---|---|
| Token files | `src/styles/_tokens.scss` (§2.8), `_typography.scss` (type tokens as CSS vars + utility classes `.t-h1`, `.t-label`…), `_base.scss` (reset, focus, reduced motion, forced colours), imported by `src/styles.scss` |
| No raw values | Component SCSS uses only `var(--…)`. Enforce with Stylelint: `color-no-hex`, `function-disallowed-list: [rgb, rgba, hsl]`, `declaration-property-value-disallowed-list` for `font-size`/`border-radius`/`box-shadow` px values, applied to `src/app/**/*.scss` |
| Fonts | Self-host with `@fontsource/poppins` (500,600,700,800), `@fontsource/inter` (400–700), `@fontsource/jetbrains-mono` (400,600), `@fontsource/dancing-script` (600,700) imported in `styles.scss` — works offline for demos and needs no third-party request (simpler CSP, no visitor data to Google). Alternative: Google Fonts `<link>` with `preconnect` and `display=swap`. Load Dancing Script only on the login route if bundle size matters |
| Components | Standalone, `ChangeDetectionStrategy.OnPush`, signals for state, one job each. Inputs typed; no `any` |
| No UI library | Angular CDK only: `Overlay` (select, popover, tooltip), `Dialog`, `A11yModule` (`FocusTrap`, `LiveAnnouncer`, `FocusMonitor`, `ActiveDescendantKeyManager`), `ScrollingModule` (conversation list, long document lists), `LayoutModule` (`BreakpointObserver`) |
| Untrusted text | User, file and model text via `{{ }}`. Markdown → HTML via a sanitising renderer bound with `[innerHTML]` (Angular sanitises); **never** `bypassSecurityTrust…`. Links in answers get `rel="noopener noreferrer"` and `target="_blank"` |
| Charts | Explorer map in plain SVG / Canvas — no chart library unless an ADR approves it |
| `data-testid` | kebab-case `{feature}-{element}[-{variant}]`. Repeated items share one testid and expose identity via `data-*` (e.g. `data-node="search"`, `data-state="done"`, `data-technique="hybrid"`) — never database ids in testids |

### 8.1 Required `data-testid`s

| Area | testids |
|---|---|
| Shell | `nav-chat` `nav-compare` `nav-retrieval-lab` `nav-vector-explorer` `nav-documents` `nav-admin` `new-chat-button` `conversation-item` `theme-toggle` `model-status-pill` `demo-mode-badge` `user-menu` |
| Composer | `composer-input` `composer-send` `composer-stop` `mode-toggle` `mode-option` (`data-mode="quick"|"deep"`) `mode-hint` `technique-select` `technique-option` `model-select` `model-option` `advanced-button` `advanced-top-k` `advanced-temperature` `advanced-scope` `advanced-reset` `composer-options` (xs) |
| Messages | `message-user` `message-assistant` (`data-state="streaming"|"done"|"error"|"no-answer"`) `streaming-cursor` `message-copy` `message-retry` `trace-open` `agent-steps` `agent-step` (`data-node`, `data-state`) `agent-steps-toggle` `source-chip` `source-excerpt` `citation` |
| Trace | `trace-panel` `trace-summary` `trace-passage` `trace-details-toggle` `trace-copy-json` |
| Compare | `compare-input` `compare-run` `compare-column` (`data-mode`) |
| Lab | `lab-input` `lab-run` `lab-technique-filter` `lab-column` (`data-technique`) `lab-chunk` (`data-chunk-key`, `data-shared="true"`) |
| Explorer | `explorer-readonly-badge` `explorer-overview-card` (`data-metric`) `explorer-table` `explorer-row` `explorer-page-next` `explorer-page-prev` `explorer-doc-filter` `explorer-detail` `explorer-map` `explorer-legend-item` `explorer-help` |
| Documents | `upload-dropzone` `upload-input` `upload-job` (`data-status`) `document-row` `document-delete` `confirm-delete` `cancel-delete` |
| Feedback | `toast` (`data-kind`) `error-card` `empty-state` `skeleton` |
| Login | `login-email` `login-password` `login-submit` `login-error` |
