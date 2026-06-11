# Sheet-Template — Kanonische HTML-Struktur

Dieses Template ist die verbindliche Vorlage für alle neuen Cheat-Sheets. Jedes Feld mit `{PLATZHALTER}` muss ersetzt werden.

---

## Platzhalter-Übersicht

| Platzhalter | Beispiel | Beschreibung |
|---|---|---|
| `{TOOL}` | `Docker Compose` | Vollständiger Tool-Name |
| `{TOOL_KEY}` | `docker-compose` | Kebab-case (für Datei/Asset-Namen) |
| `{LANG}` | `de` | Sprache (fast immer `de`) |
| `{PAGE_TITLE}` | `Docker Compose - TheLayer0Guide` | Browser-Tab-Titel |
| `{ACCENT}` | `#2496ed` | Primärfarbe — `--accent` |
| `{ACCENT2}` | `#0db7ed` | Sekundärfarbe — `--accent2` |
| `{ACCENT_R,G,B}` | `36,150,237` | RGB-Werte von `--accent` (für rgba()) |
| `{HEADER_MID}` | `#001629` | Mittelpunkt des Header-Gradienten (dunkler Hauch der Akzentfarbe) |
| `{BADGE_TEXT}` | `▸ Container Reference` | Badge-Beschriftung — spezifisch, nicht generisch |
| `{SUBTITLE}` | `$ docker compose up -d` | CLI-Befehl als Untertitel |
| `{META_STRONG}` | `docker compose` | Fetter Text im Meta-Block (rechts oben) |
| `{META_LINES}` | `Up · Down · Build<br>Scale · Logs · Exec` | Beschreibungszeilen im Meta-Block |
| `{ICON_FILTER}` | `invert(43%) sepia(80%) saturate(700%) hue-rotate(186deg)` | CSS-Filter für SVG-Logo |
| `{H1_PART1}` | `<span>Docker</span> Compose` | H1-Inhalt (farbiger Anteil in `<span>`) |
| `{GROUP}` | `Cloud & Infra` | Zugehörige Index-Gruppe |

---

## Vollständiges Template

```html
<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{PAGE_TITLE}</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Syne:wght@400;600;800&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="../assets/{TOOL_KEY}.svg">
<style>
  :root{--bg:#0d1117;--surface:#161b22;--border:#30363d;--accent:{ACCENT};--accent2:{ACCENT2};--green:#3fb950;--purple:#a371f7;--cyan:#39c5cf;--red:#f47067;--text:#e6edf3;--muted:#7d8590;--code-bg:#10161d;}
  *{margin:0;padding:0;box-sizing:border-box;}
  body{background:var(--bg);color:var(--text);font-family:'Syne',sans-serif;min-height:100vh;}
  header{background:linear-gradient(135deg,#0d1117 0%,{HEADER_MID} 50%,#0d1117 100%);border-bottom:2px solid var(--accent);padding:40px 48px 32px;position:relative;overflow:hidden;}
  header::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 600px 200px at 60% 50%,rgba({ACCENT_R,G,B},.08),transparent);}
  .header-grid{display:grid;grid-template-columns:1fr auto;align-items:end;gap:24px;position:relative;}
  .badge{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:600;color:var(--accent);background:rgba({ACCENT_R,G,B},.1);border:1px solid rgba({ACCENT_R,G,B},.3);padding:3px 10px;border-radius:3px;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;}
  h1{font-size:clamp(28px,4vw,48px);font-weight:800;letter-spacing:-1px;line-height:1.1;color:var(--text);}
  h1 span{color:var(--accent);}
  .subtitle{color:var(--muted);font-size:14px;margin-top:8px;font-family:'JetBrains Mono',monospace;}
  .meta{text-align:right;font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);line-height:1.8;}
  .meta strong{color:var(--accent2);}
  .version-legend{margin-top:18px;display:flex;gap:10px;flex-wrap:wrap;}
  .chip{font-family:'JetBrains Mono',monospace;font-size:11px;border-radius:4px;padding:4px 12px;font-weight:600;}
  .ch-ac{background:rgba({ACCENT_R,G,B},.1);border:1px solid rgba({ACCENT_R,G,B},.3);color:var(--accent);}
  .ch-gn{background:rgba(63,185,80,.1);border:1px solid rgba(63,185,80,.3);color:var(--green);}
  .ch-cy{background:rgba(57,197,207,.1);border:1px solid rgba(57,197,207,.3);color:var(--cyan);}
  .ch-pu{background:rgba(163,113,247,.1);border:1px solid rgba(163,113,247,.3);color:var(--purple);}
  main{padding:32px 48px;max-width:1400px;margin:0 auto;columns:3;column-gap:20px;}
  .section{break-inside:avoid;margin-bottom:20px;background:var(--surface);border:1px solid var(--border);border-radius:8px;overflow:hidden;}
  .section-header{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--border);}
  .section-icon{width:28px;height:28px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;}
  .section-title{font-size:13px;font-weight:600;letter-spacing:.5px;text-transform:uppercase;}
  .th-ac .section-header{background:rgba({ACCENT_R,G,B},.06);} .th-ac .section-icon{background:rgba({ACCENT_R,G,B},.15);} .th-ac .section-title{color:var(--accent);}
  .th-gn .section-header{background:rgba(63,185,80,.06);} .th-gn .section-icon{background:rgba(63,185,80,.15);} .th-gn .section-title{color:var(--green);}
  .th-cy .section-header{background:rgba(57,197,207,.06);} .th-cy .section-icon{background:rgba(57,197,207,.15);} .th-cy .section-title{color:var(--cyan);}
  .th-pu .section-header{background:rgba(163,113,247,.06);} .th-pu .section-icon{background:rgba(163,113,247,.15);} .th-pu .section-title{color:var(--purple);}
  .th-re .section-header{background:rgba(244,112,103,.06);} .th-re .section-icon{background:rgba(244,112,103,.15);} .th-re .section-title{color:var(--red);}
  .command-list{padding:8px 0;}
  .cmd-entry{padding:6px 16px;border-bottom:1px solid rgba(48,54,61,.5);}
  .cmd-entry:last-child{border-bottom:none;}
  .cmd-desc{font-size:10px;color:var(--muted);margin-bottom:3px;letter-spacing:.3px;text-transform:uppercase;}
  code{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--text);background:var(--code-bg);display:block;padding:5px 9px;border-radius:4px;line-height:1.6;white-space:pre-wrap;word-break:break-all;}
  .kw{color:{ACCENT_HEX_LIGHT};font-weight:700;} .st{color:#3fb950;} .nu{color:#f47067;}
  .cm{color:#7d8590;font-style:italic;} .fn{color:#39c5cf;font-weight:600;}
  .tip{padding:8px 16px;background:rgba({ACCENT_R,G,B},.06);border-left:3px solid var(--accent);font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);line-height:1.6;}
  .tip strong{color:var(--text);}
  .nav-link{position:absolute;top:40px;right:48px;z-index:10;font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--accent);text-decoration:none;border:1px solid rgba({ACCENT_R,G,B},.3);padding:4px 12px;border-radius:4px;background:rgba({ACCENT_R,G,B},.08);}
  .nav-link:hover{background:rgba({ACCENT_R,G,B},.15);}
  @media(max-width:1100px){main{columns:2;}}
  @media(max-width:700px){main{columns:1;padding:16px;}header{padding:24px 16px;}}
</style>
</head>
<body>
<header>
  <a href="../index.html" class="nav-link">← Index</a>
  <div class="header-grid">
    <div>
      <div class="badge">{BADGE_TEXT}</div>
      <img src="../assets/{TOOL_KEY}.svg" alt="Logo" style="width:48px;height:48px;margin-bottom:12px;display:block;filter:{ICON_FILTER}">
      <h1>{H1_PART1}<br>TheLayer<span style="color:#a371f7;font-family:'JetBrains Mono',monospace;font-size:1.25em;-webkit-text-fill-color:#a371f7;">0</span>Guide</h1>
      <p class="subtitle">{SUBTITLE}</p>
      <div class="version-legend">
        <div class="chip ch-ac">{CHIP1}</div>
        <div class="chip ch-gn">{CHIP2}</div>
        <div class="chip ch-cy">{CHIP3}</div>
        <div class="chip ch-pu">{CHIP4}</div>
      </div>
    </div>
    <div class="meta"><strong>{META_STRONG}</strong><br>{META_LINES}</div>
  </div>
</header>
<main>

<!-- SECTIONS hier einfügen -->

<div class="section th-ac">
  <div class="section-header"><div class="section-icon">🔧</div><div class="section-title">Abschnitt-Titel</div></div>
  <div class="command-list">
    <div class="cmd-entry">
      <div class="cmd-desc">Beschreibung</div>
      <code>befehl --option argument
weiterer befehl</code>
    </div>
    <div class="cmd-entry">
      <div class="cmd-desc">Mit Kommentaren</div>
      <code>befehl --flag   <span class="cm"># Kommentar</span>
<span class="cm"># Erklärender Kommentar:</span>
befehl --verbose</code>
    </div>
    <div class="tip"><strong>Hinweis:</strong> Erklärungstext mit <strong>Betonung</strong>.</div>
  </div>
</div>

</main>
</body>
</html>
```

---

## Regeln für Sektions-Theme-Klassen

Sheets verwenden unterschiedliche Klassen je nach Akzentfarbe:

| Akzentfarbe | Primär-Theme-Klasse | Sekundäre Klassen |
|---|---|---|
| Blau-Töne | `.th-bl` | `.th-gn`, `.th-cy`, `.th-pu`, `.th-re` |
| Rot-Töne | `.th-re` | `.th-gn`, `.th-cy`, `.th-pu` |
| Orange-Töne | `.th-or` | `.th-gn`, `.th-cy`, `.th-pu`, `.th-re` |
| Grün-Töne | `.th-gn` | `.th-bl`, `.th-cy`, `.th-pu`, `.th-re` |
| Lila-Töne | `.th-pu` | `.th-gn`, `.th-cy`, `.th-re` |
| Gelb-Töne | `.th-yl` | `.th-gn`, `.th-cy`, `.th-pu`, `.th-re` |
| Cyan-Töne | `.th-cy` | `.th-gn`, `.th-pu`, `.th-re` |

Das Primär-Theme-CSS muss immer `color:var(--accent)` verwenden, nie `--accent2`.

Im Template oben wurde `.th-ac` als generischer Platzhalter verwendet — ersetze ihn mit dem passenden `.th-bl`, `.th-re`, usw.

---

## Checkliste vor Commit

- [ ] `<code>` korrekt — kein `<code">` (häufiger Tippfehler bei KI-Generierung)
- [ ] `h1 { color: var(--text); }` vorhanden
- [ ] `h1 span { color: var(--accent); }` — `--accent`, nicht `--accent2`
- [ ] `.badge { color: var(--accent); }` — `--accent`, nicht `--accent2`
- [ ] `.nav-link { color: var(--accent); }` — `--accent`, nicht `--accent2`
- [ ] `.tip { border-left: 3px solid var(--accent); }` — `--accent`, nicht `--accent2`
- [ ] `.th-X .section-title { color: var(--accent); }` für das Primär-Theme
- [ ] `.meta strong { color: var(--accent2); }` — hier darf `--accent2` stehen
- [ ] `header { border-bottom: 2px solid var(--accent); }` — `--accent`, nicht `--accent2`
- [ ] Badge-Text spezifisch (z. B. `▸ OpenStack Block Storage`) — nicht generisch
- [ ] TheLayer0Guide „0" korrekt (`color:#a371f7`, `font-family:'JetBrains Mono'`, `-webkit-text-fill-color:#a371f7`)
- [ ] Icon-Filter `filter:...` am `<img>` — nicht vergessen
- [ ] Index-Eintrag mit korrektem `data-group`, `data-subgroup` (falls nötig), `--ac`/`--acs`/`--acb`
- [ ] Index-Card-Icon-Filter als Inline-Style am `<img>` in `.card-icon`

---

## Neue Karte in index.html einfügen

```html
<a href="sheets/{TOOL_KEY}-cheatsheet.html" class="card c-{TOOL_KEY}" data-title="{TITLE}" data-group="{GROUP}">
  <div class="card-accent"></div>
  <div class="card-body">
    <div class="card-icon-row">
      <div class="card-icon"><img src="assets/{TOOL_KEY}.svg" alt="{TOOL_KEY}.svg" style="width:24px;height:24px;filter:{ICON_FILTER_24}"></div>
      <div class="card-name">{TITLE}</div>
    </div>
    <div class="card-tagline">{CLI_EXAMPLE} -- {TAGLINE}<br>{KEYWORDS}</div>
    <div class="card-tags">
      <span class="tag">{TAG1}</span><span class="tag">{TAG2}</span><span class="tag">{TAG3}</span><span class="tag">{TAG4}</span>
    </div>
    <div class="card-arrow">→</div>
  </div>
</a>
```

CSS für die Karte (in den `<style>`-Block von index.html, alphabetisch/thematisch einordnen):

```css
.c-{TOOL_KEY}{--ac:{ACCENT};--acs:rgba({ACCENT_R,G,B},0.15);--acb:rgba({ACCENT_R,G,B},0.25)}
```

Pill-Zähler und Gesamt-Zähler in der Toolbar aktualisieren.
