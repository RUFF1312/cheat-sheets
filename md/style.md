# TheLayer0Guide Styleguide

Dieser Styleguide definiert die visuellen Richtlinien, Farben, Typografie und UI-Komponenten für "TheLayer0Guide". Dies dient als Referenz für Entwickler und Agents, um beim Erstellen oder Erweitern von Inhalten den "Premium Dark Theme"-Look konsistent beizubehalten.

## 1. Farben (Color Palette)

Die Basis des Designs verwendet eine stark vom GitHub Dark-Theme inspirierte Farbpalette, gepaart mit spezifischen leuchtenden Akzentfarben.

### Base Colors (`index.css` & Global)
- **Background (`--bg`):** `#0d1117`
- **Surface / Cards (`--surface`):** `#161b22`
- **Surface Hover / Secondary (`--surface2`):** `#1c2330`
- **Border (`--border`):** `#30363d`
- **Base Text (`--text`):** `#e6edf3`
- **Muted Text (`--muted`):** `#7d8590`
- **Code Background (`--code-bg`):** `#10161d`

### Branding & Logo
- **Main Brand "0":** `#a371f7` (Violett)
- Die "0" in `TheLayer0Guide` verwendet spezifisch diese Farbe, kombiniert mit Terminal-Schriftart (`JetBrains Mono, monospace`) und erzwungener Text-Füllfarbe.

### Technologie-Spezifische Akzente
Jedes Sheet / jede Karte hat ihre eigene Akzentfarbe (`--ac`), sowie semi-transparente Hintergrundfarben für Hover-Status und Badges (`--acs` auf 15% Deckkraft, `--acb` auf 25% Deckkraft):
- **OpenStack:** `#e8541a`
- **tmux:** `#1aac8a`
- **vi/vim:** `#c778dd`
- **Ansible:** `#e8313a`
- **Python:** `#f7c948` (Secondary: `#4b8bbe`)
- **Bash:** `#4ec9b0` (Secondary: `#f0a030`)
- **Git:** `#f05033`
- **PowerShell:** `#2671be`
- **Proxmox:** `#e36209`
- **systemd:** `#30d475`

## 2. Typografie (Typography)

Die Seite verwendet ausschließlich **Google Fonts** (kein anderes CDN). Das Zusammenspiel aus modern-technischer Sans-Serif und einer stark strukturierten Monospace-Schrift prägt das Design.

- **Standardtext & Überschriften:** `'Syne', sans-serif`
- **Code, Tags, Badges, Header-Eyebrows:** `'JetBrains Mono', monospace`

### Hierarchie
- **Seiten-Titel (H1):** 
  - Schriftart: `Syne`
  - Font-Size: Dynamisch skalierend (z.B. `clamp(36px, 5vw, 64px)`) oder fest (`clamp(28px, 4vw, 48px)` auf Subpages)
  - Gewicht: `800` (Extra Bold)
  - Letter-spacing: `-1px` bis `-2px`
- **Section-Titel:**
  - Größe: `13px`
  - Gewicht: `600`
  - Text-Transform: `uppercase`
- **Tags & Badges:**
  - Font: `'JetBrains Mono'`
  - Font-Size: `10px` bis `11px`
  - Text-Transform: `uppercase` (oftmals)
  - Letter-Spacing: `0.3px` bis `3px`
  - Gewicht: `600`

## 3. UI-Komponenten (Components)

### Header
- Nutzt einen leichten linearen Gradienten: `linear-gradient(135deg, #0d1117 0%, #111820 60%, #0d1117 100%)`.
- Optionales, subtiles "Glow"-Highlight durch `:before` mit `radial-gradient(ellipse ... rgba(255,255,255,0.02), transparent)`.
- Nutzt auf den Unterseiten einen CSS Grid-Aufbau (`grid-template-columns: 1fr auto`), um Titel und Metadaten sauber zu trennen.

### Karten (Cards - Index)
- **Design:** Hintergrund `--surface`, Border `--border`, 10px Border-Radius.
- **Hover-Effekt:** Leichte Aufwärtsbewegung `transform: translateY(-3px)`, Schattierung `box-shadow: 0 12px 40px rgba(0,0,0,0.4)` und Anpassung der Rahmenfarbe an das Tool-spezifische `--ac`.
- **Top Accent Line:** Ein 3px hoher `div` (`.card-accent`) als farbige Kopfzeile.
- **Icons:** Zentriert in einem 44x44px gerundeten Viereck, welches den semi-transparenten Farbton (`--acs`) des Tools nutzt.
- **Icon-Farbe:** Alle Icon-Grafiken (`img` innerhalb `.card-icon`) werden durch `filter: brightness(0)` einheitlich **schwarz** dargestellt. So bleiben die Icons neutral, während der farbige Hintergrund (`--acs`) die Tool-Identität transportiert.

### Sections & Command Lists (Cheatsheets)
- **Container (`.section`):** Umrandet mit `--border`, `8px` Radius, `break-inside: avoid;` (für sauberes Masonry-Muster in den CSS-Columns).
- **Section Header:** Farblicher Hintergrund basierend auf einem Theme (z. B. `.theme-cyan`), der die Section-Titel farblich hervorhebt (Icon und Text).
- **Befehle (`.cmd-entry`):** Getrennt durch leichte Rahmen (`1px solid rgba(48,54,61,0.5)`).

### Inline Code & Code-Blöcke
- **Design:** `padding: 5px 9px`, abgerundete Ecken (`4px`), `font-size: 11.5px`, Hintergrund `--code-bg`.
- **Syntax Highlighting Klassen:**
  - `.kw`  (Keywords) -> `#f7c948` oder theme-basierend
  - `.bi`  (Builtins) -> `#4b8bbe`
  - `.st`  (Strings) -> `#3fb950`
  - `.nu`  (Numbers) -> `#f47067`
  - `.cm`  (Comments) -> `#7d8590`, italic
  - `.fn`  (Functions) -> `#39c5cf`
  - `.tp`  (Typing) -> `#a371f7`

### Tipps & Info-Blöcke (`.tip`)
Kleine, farblich hinterlegte Hinweisblöcke (z. B. gelb, blau, lila), abgetrennt mit einer gestrichelten `border-top` (z. B. `1px dashed rgba({color}, 0.2)`). Schriftart ist hierbei meist Monospace.

## 4. Logo-Integration & "0" Styling

Wo auch immer der Markenname **"TheLayer0Guide"** im Layout sichtbar (`h1`, `footer`, `badges`) platziert wird:
1. Die "0" **muss** als Terminal-0 hervorgehoben sein:
   ```html
   <span style="color: #a371f7; font-family: 'JetBrains Mono', monospace; font-size: 1.25em; -webkit-text-fill-color: #a371f7;">0</span>
   ```
2. Auf Hauptseiten mit CSS-Gradients über Texten muss der `-webkit-text-fill-color` explizit überschrieben werden, um zu garantieren, dass die 0 satt-violett bleibt.

## 5. Responsive Design

- Das Layout besteht aus CSS Grid (Index) oder CSS Columns (Cheatsheets).
- Unter `1100px`/`900px`: Spalten verringern.
- Unter `700px`/`600px`: Einspaltiges Raster, reduziertes Header-Padding für mobile First-Ansicht.

## 6. Favicon

- **Datei:** `assets/favicon.svg`
- **Design:** Schwarzer abgerundeter quadratischer Hintergrund (`#0d1117`, `rx="20"`), zentrierte violette **"0"** (`fill: #a371f7`) in `JetBrains Mono` Bold.
- **Einbindung:** `<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">`
- Die "0" übernimmt dabei exakt die Brand-Farbe des Projekts (`#a371f7`) und spiegelt die visuelle Identität von `TheLayer0Guide` im Browser-Tab wider.
