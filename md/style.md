# TheLayer0Guide — Design System

Verbindliche Designreferenz für alle Sheets und die Index-Seite. Alle neuen Inhalte müssen diesen Regeln exakt folgen.

---

## 1. Farb-System

### Global (index.html + alle Sheets)

| Variable | Wert | Verwendung |
|---|---|---|
| `--bg` | `#0d1117` | Seiten-Hintergrund |
| `--surface` | `#161b22` | Cards, Sections |
| `--surface2` | `#1c2330` | Hover-States (nur Index) |
| `--border` | `#30363d` | Alle Rahmen |
| `--text` | `#e6edf3` | Fließtext |
| `--muted` | `#7d8590` | Beschriftungen, Kommentare |
| `--code-bg` | `#10161d` | Code-Block-Hintergrund |

### Sheet-Variablen (`:root` je Sheet)

Jedes Sheet definiert zwei eigene Akzentfarben plus globale Farb-Hilfsvariablen:

```css
:root {
  --accent:  #XXXXXX;  /* Primärfarbe — alle UI-Chrome-Elemente */
  --accent2: #YYYYYY;  /* Sekundärfarbe — nur .meta strong */
  --green:   #3fb950;
  --purple:  #a371f7;
  --cyan:    #39c5cf;
  --red:     #f47067;
}
```

**Kritische Regel — `--accent` vs `--accent2`:**

| Selektor | Variable | Erklärung |
|---|---|---|
| `.badge { color: }` | `var(--accent)` | Header-Badge-Text |
| `h1 { color: }` | `var(--text)` | H1 braucht explizites `color:var(--text)` |
| `h1 span { color: }` | `var(--accent)` | Farbiger Teil des Titels |
| `.nav-link { color: }` | `var(--accent)` | Zurück-zum-Index-Link |
| `.tip { border-left: }` | `var(--accent)` | Linker Balken des Tipp-Blocks |
| `.th-X .section-title { color: }` | `var(--accent)` | Primäre Section-Titel |
| `.ch-X { color: }` | `var(--accent)` | Primäre Chips (passend zum Akzent) |
| `.meta strong { color: }` | `var(--accent2)` | **Einzige Ausnahme** — Sekundärfarbe |

> **Merksatz:** Alles, was der Benutzer als „Tool-Farbe" wahrnimmt, nutzt `--accent`. Nur `.meta strong` nutzt `--accent2`.

### Branding — Die „0" in TheLayer0Guide

Überall, wo der Markenname erscheint (`h1`, Footer, Badges):

```html
TheLayer<span style="color:#a371f7;font-family:'JetBrains Mono',monospace;font-size:1.25em;-webkit-text-fill-color:#a371f7;">0</span>Guide
```

- `-webkit-text-fill-color` muss explizit gesetzt werden, wenn die `h1` einen CSS-Gradienten hat.
- Die Farbe `#a371f7` (Violett) ist festgelegt und ändert sich nie.

---

## 2. Typografie

Ausschließlich **Google Fonts**. Kein anderes CDN.

```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Syne:wght@400;600;800&display=swap" rel="stylesheet">
```

| Kontext | Font | Gewicht |
|---|---|---|
| Fließtext, `<h1>` | `'Syne', sans-serif` | `800` (H1), `400` (Body) |
| Code, Badges, Tags, `.nav-link`, `.subtitle`, `.meta`, `.chip`, `.cmd-desc` | `'JetBrains Mono', monospace` | `600` (Badges), `400`/`700` (Code) |

### H1-Größen

- Index-Haupttitel: `clamp(36px, 5vw, 64px)`, `letter-spacing: -2px`
- Sheet-Titel: `clamp(28px, 4vw, 48px)`, `letter-spacing: -1px`

---

## 3. Index-Seite

### Karten-Farb-Klassen (`.c-*`)

Jede Karte hat eine CSS-Klasse, die drei Variablen setzt:

```css
.c-docker { --ac: #0db7ed; --acs: rgba(13,183,237,0.15); --acb: rgba(13,183,237,0.25); }
```

| Variable | Verwendung |
|---|---|
| `--ac` | Card-Top-Accent-Linie (`.card-accent`), Hover-Border |
| `--acs` | Icon-Hintergrund (15% Deckkraft) |
| `--acb` | Hover-Schatten / Badge-Border (25% Deckkraft) |

### Karten-Icon-Filter

Der globale CSS setzt alle Card-Icons auf **weiß**:
```css
.card-icon img { filter: brightness(0) invert(1); }
```

Karten, deren Icon farbig (akzentfarbig) erscheinen soll, überschreiben das mit einem Inline-`filter` am `<img>`-Tag:
```html
<img src="assets/nova.svg" style="width:24px;height:24px;filter:invert(28%) sepia(85%) saturate(700%) hue-rotate(325deg)">
```

OpenStack- und VMware-Karten haben solche Inline-Filter. Ältere Karten verwenden den Weiß-Fallback.

### Gruppen und Subgruppen

| Gruppe | `data-group` | Anzahl | Pill-Farbe |
|---|---|---|---|
| Cloud & Infra | `"Cloud & Infra"` | 30 | `#0db7ed` |
| System & Netz | `"System & Netz"` | 17 | `#3fb950` |
| Programmiersprachen | `"Programmiersprachen"` | 13 | `#f7df1e` |
| Dev & Automation | `"Dev & Automation"` | 9 | `#a371f7` |
| VMware | `"VMware"` | 4 | `#5ba8e0` |
| Datenbanken | `"Datenbanken"` | 4 | `#f0c040` |

Subgruppen mit `data-subgroup`:
- `"OpenStack"` (6 Sheets in Cloud & Infra) — Pill-Farbe `#e84040`
- `"VMware"` (4 Sheets in VMware-Gruppe) — Pill-Farbe `#5ba8e0`

### Toolbar-Filterlogik (JS)

```javascript
let activeFilter = 'all';
let activeSubgroup = null;
```

- Hauptgruppen-Pills setzen `activeFilter`, nullen `activeSubgroup`
- Subgruppen-Pills setzen `activeSubgroup`, zweiter Klick toggelt (null)
- Group-Headers werden nur gezeigt wenn `activeFilter === 'all' && !activeSubgroup && !sortAZ && !term`

---

## 4. Sheet-Aufbau

### Header

```css
header {
  background: linear-gradient(135deg, #0d1117 0%, #XXXXXX 50%, #0d1117 100%);
  border-bottom: 2px solid var(--accent);  /* immer --accent, nie --accent2 */
}
header::before {
  background: radial-gradient(ellipse 600px 200px at 60% 50%, rgba(R,G,B,.08), transparent);
}
```

Der mittlere Gradientpunkt ist ein sehr dunkler Hauch der Akzentfarbe (z. B. `#001629` für Blau, `#160800` für Orange).

### Section-Themes

Vier Standard-Themes für wiederverwendbare Abschnitte:

| Klasse | Farbe | Variable |
|---|---|---|
| `.th-bl` | Blau | `var(--accent)` oder `rgba(36,150,237,…)` |
| `.th-gn` | Grün | `var(--green)` = `#3fb950` |
| `.th-cy` | Cyan | `var(--cyan)` = `#39c5cf` |
| `.th-pu` | Lila | `var(--purple)` = `#a371f7` |
| `.th-re` | Rot | `var(--red)` = `#f47067` |
| `.th-or` | Orange | Literal `rgba(…)` |
| `.th-yl` | Gelb | Literal `rgba(…)` |

Jedes Theme definiert drei Regeln:
```css
.th-gn .section-header { background: rgba(63,185,80,.06); }
.th-gn .section-icon   { background: rgba(63,185,80,.15); }
.th-gn .section-title  { color: var(--green); }
```

Das **primäre** Theme (das zum `--accent` des Sheets passt) nutzt **immer `var(--accent)`** als `section-title`-Farbe, nie `--accent2`.

### Syntax-Highlighting-Klassen

| Klasse | Bedeutung | Farbe |
|---|---|---|
| `.kw` | Keywords | Literal `--accent`-Hex (leicht heller für Lesbarkeit) |
| `.st` | Strings | `#3fb950` |
| `.nu` | Numbers | `#f47067` |
| `.cm` | Comments | `#7d8590`, `font-style: italic` |
| `.fn` | Functions | `#39c5cf`, `font-weight: 600` |
| `.tp` | Types | `#a371f7` |

### Inline-Code

```css
code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  color: var(--text);
  background: var(--code-bg);
  display: block;
  padding: 5px 9px;
  border-radius: 4px;
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-all;
}
```

**Wichtig:** `<code>` nie mit `<code">` schreiben — kein Anführungszeichen im öffnenden Tag.

### Tip-Block

```css
.tip {
  padding: 8px 16px;
  background: rgba(R,G,B,.06);   /* --accent rgba */
  border-left: 3px solid var(--accent);  /* immer --accent */
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--muted);
  line-height: 1.6;
}
.tip strong { color: var(--text); }
```

### Responsive

```css
@media(max-width:1100px) { main { columns: 2; } }
@media(max-width:700px)  { main { columns: 1; padding: 16px; } header { padding: 24px 16px; } }
```

---

## 5. Akzentfarben — alle Sheets

### Cloud & Infra (inkl. OpenStack Sub-Sheets)

| Sheet | `--accent` | `--accent2` |
|---|---|---|
| OpenStack CLI | `#007ac1` | — |
| Proxmox VE | `#e57000` | — |
| Kubernetes | `#326CE5` | — |
| Helm | `#277DC1` | — |
| Docker | `#0db7ed` | — |
| Docker Compose | `#2496ed` | `#0db7ed` |
| Ceph | `#e33a2e` | — |
| Terraform | `#7b42bc` | — |
| Open vSwitch/OVN | `#00b4a0` | — |
| HAProxy | `#106490` | — |
| Pacemaker/Corosync | `#c41e3a` | — |
| HashiCorp Vault | `#c9a227` | — |
| Prometheus/PromQL | `#e6522c` | — |
| Podman | `#892ca0` | — |
| KVM/libvirt | `#c0392b` | — |
| RabbitMQ | `#f26122` | — |
| Keepalived | `#7e57c2` | — |
| Kolla-Ansible | `#ed1944` | — |
| nginx | `#269539` | — |
| Grafana | `#f46800` | — |
| ArgoCD | `#ef7b4d` | — |
| Loki/LogQL | `#f5a623` | — |
| Alertmanager | `#e67e22` | — |
| containerd/crictl | `#4a90d9` | — |
| Nova (Compute) | `#e84040` | `#ff7070` |
| Neutron (Network) | `#1a85c9` | `#5ba8e0` |
| Cinder (Storage) | `#e07b39` | `#f4a261` |
| Glance (Images) | `#9c5cc7` | `#c084fc` |
| Keystone (Identity) | `#d4a017` | `#fbbf24` |
| Heat (Orchestration) | `#e0652a` | `#fb923c` |

### System & Netz

| Sheet | `--accent` |
|---|---|
| tmux | `#1aac8a` |
| vi / vim | `#199c07` |
| Bash | `#a371f7` |
| PowerShell | `#5391fe` |
| nmcli | `#3584e4` |
| iptables/nftables | `#e53e3e` |
| SSH | `#22863a` |
| LVM | `#c45f17` |
| OpenSSL/PKI | `#5a40d4` |
| tcpdump/ss | `#0070c0` |
| chronyc/NTP | `#2563eb` |
| systemd | `#30D475` |
| Package Manager | `#e88a2f` |
| sed & awk | `#1aac8a` |
| Linux Performance | `#9b59b6` |
| rsync | `#00b4a0` |
| firewalld | `#e05a00` |

### Dev & Automation

| Sheet | `--accent` |
|---|---|
| Ansible | `#ee0000` |
| Python | `#3776ab` |
| Git | `#f1502f` |
| jq/yq | `#d4a017` |
| curl | `#0081c2` |
| GitLab CI / GitHub Actions | `#fc6d26` |
| Make/Makefile | `#2e7c5e` |
| Regex | `#16a34a` |
| Kickstart | `#c42b2b` |

### Programmiersprachen

| Sheet | `--accent` |
|---|---|
| C | `#a8b9cc` |
| C++ | `#00599c` |
| C# | `#c678dd` |
| Java | `#ed8b00` |
| JavaScript | `#f7df1e` |
| TypeScript | `#3178c6` |
| Go | `#00add8` |
| Rust | `#ce422b` |
| Python | `#3776ab` |
| PHP | `#8892be` |
| Ruby | `#cc342d` |
| Kotlin | `#7f52ff` |
| Swift | `#f05138` |
| Lua | `#79a8ff` |

### Datenbanken

| Sheet | `--accent` |
|---|---|
| SQL | `#336791` |
| MariaDB/MySQL | `#0074c1` |
| PostgreSQL | `#6495ed` |
| Redis | `#dc382d` |

### VMware

| Sheet | `--accent` (Sheet) | `--accent2` (Sheet) | `--ac` (Index-Card) |
|---|---|---|---|
| PowerCLI | `#007DC1` | `#5ba8e0` | `#5ba8e0` |
| esxcli/vim-cmd | `#00C1D3` | `#39c5cf` | `#00C1D3` |
| govc | `#5AC8FA` | `#79d9ff` | `#5AC8FA` |
| vSphere/VCSA | `#1565C0` | `#79b8ff` | `#79b8ff` |

---

## 6. Favicon

```html
<link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
```

SVG: Schwarzes Quadrat (`#0d1117`, `rx="20"`), zentrierte violette `0` (`#a371f7`) in JetBrains Mono Bold.
