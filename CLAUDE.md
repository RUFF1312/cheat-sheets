# CLAUDE.md — TheLayer0Guide

Projektregeln für Claude-Sessions. Werden bei jedem Start automatisch geladen.

---

## Projektstruktur

```
cheat-sheets/
├── index.html              Hauptseite (111 Karten, Filter-System, JS)
├── sheets/                 Alle Cheat-Sheet HTML-Dateien
├── assets/                 SVG-Icons (ein Icon pro Tool)
└── md/
    ├── style.md            Design System — alle Farben, Komponenten, Regeln
    ├── sheet-template.md   Kanonisches HTML-Template für neue Sheets
    └── inventory.md        Vollständiges Verzeichnis aller 111 Sheets
```

Vor umfangreichen Änderungen immer `md/style.md`, `md/sheet-template.md` und `md/inventory.md` lesen.

---

## Kritische CSS-Regeln (häufige Fehlerquellen)

### accent vs. accent2 — die wichtigste Regel

**Immer `var(--accent)` für:**
```css
h1           { color: var(--text); }   /* explizit! nie weglassen */
h1 span      { color: var(--accent); }
.badge       { color: var(--accent); }
.nav-link    { color: var(--accent); }
.tip         { border-left: 3px solid var(--accent); }
.th-X .section-title { color: var(--accent); }  /* Primäres Theme */
.ch-X        { color: var(--accent); }           /* Primärer Chip */
header       { border-bottom: 2px solid var(--accent); }
```

**Nur `.meta strong` darf `var(--accent2)` verwenden:**
```css
.meta strong { color: var(--accent2); }
```

> Fehler `--accent2` statt `--accent` zu verwenden ist der häufigste Stilfehler bei KI-generierten Sheets.

### Kein `<code">` — kritischer Syntaxfehler

```html
<!-- FALSCH (häufiger KI-Fehler): -->
<code">befehl</code>

<!-- RICHTIG: -->
<code>befehl</code>
```

Nach KI-Generierung immer prüfen: `grep -c '<code">' sheets/NAME-cheatsheet.html`

### TheLayer0Guide „0" — unveränderliche Inline-Styles

```html
TheLayer<span style="color:#a371f7;font-family:'JetBrains Mono',monospace;font-size:1.25em;-webkit-text-fill-color:#a371f7;">0</span>Guide
```

Der `-webkit-text-fill-color` ist notwendig, wenn `h1` einen CSS-Textgradienten hat.

---

## Neue Sheets erstellen

1. `md/sheet-template.md` lesen — dort ist das kanonische HTML-Template
2. Checkliste am Ende des Templates Punkt für Punkt abarbeiten
3. Index-Eintrag hinzufügen: neue `.c-TOOL` CSS-Klasse + neue Karte im HTML
4. `data-group="GRUPPE"` und `data-subgroups="SG1 SG2"` (Leerzeichen-getrennt, mehre möglich) an der Karte setzen
5. Pill-Zähler in der Toolbar aktualisieren (Alle + Gruppe — werden auch dynamisch per JS aktualisiert)
6. Subgruppen-Pill: falls neue Subgruppe, Button in `.toolbar-subgroups` mit `data-for-group="GRUPPE"` ergänzen
7. Subgruppen-Pill-Farbe im CSS ergänzen:
   ```css
   .pill[data-subgroup="NAME"].active { border-color: #FARBE; color: #FARBE; background:rgba(...,.08); border-style:solid }
   ```

---

## Index-Seite — Filterlogik

```javascript
let activeFilter = 'all';    // aktive Hauptgruppe
let activeSubgroup = null;   // aktive Untergruppe (kontextsensitiv zur Hauptgruppe)
```

- Gruppen-Pills (`data-filter`) nullen `activeSubgroup` und zeigen nur Subgruppen-Pills der aktiven Gruppe
- Subgruppen-Pills (`data-subgroup`, `data-for-group`) werden per `sg-visible` CSS-Klasse ein-/ausgeblendet
- Subgruppen-Pill zweiter Klick → zurück zur Hauptgruppe (nicht zu "Alle")
- Multi-Subgroup: Karten haben `data-subgroups="SG1 SG2"` (Leerzeichen-getrennt)
- Filter: `(c.dataset.subgroups || '').split(' ').includes(activeSubgroup)`
- Group-Header nur anzeigen wenn: `activeFilter === 'all' && !activeSubgroup && !sortAZ && !term`

---

## SVG-Icons

- Ein Icon pro Tool, Dateiname = `{TOOL_KEY}.svg`
- Sheet-Header: `filter:invert(X%) sepia(Y%) saturate(Z%) hue-rotate(Wdeg)` inline am `<img>`
- Index-Card: gleicher Filter inline am `<img>` in `.card-icon`
- Globaler CSS macht alle Icons weiß (`brightness(0) invert(1)`) — Inline-Filter überschreibt das
- Bestehende Filter-Werte: `md/inventory.md` → Abschnitt „Header-Icon-Filter"

---

## Git-Workflow

Remote: `git@github.com:RUFF1312/cheat-sheets.git`, Branch `main`

Typische Commit-Struktur:
- Feature (neues Sheet): `Add {Tool} cheat sheet + index integration`
- Bugfix: `Fix {was} in {welche Sheets}`
- Style: `Fix CSS style errors in N sheets`

---

## Gruppen und Zähler (Stand: 101 Sheets)

| Gruppe | `data-group` | Anzahl | Subgruppen |
|---|---|---|---|
| Cloud & Infra | `"Cloud & Infra"` | 34 | Container, OpenStack, VMware, IaC, Monitoring, Proxy-HA, Storage |
| System & Netz | `"System & Netz"` | 18 | Shell, Netzwerk, SysAdmin, PKI |
| Security | `"Security"` | 16 | Recon, Web, Exploitation, Password |
| Development | `"Development"` | 30 | Sprachen, VCS, CI-CD, Datenformate, Automatisierung, ITSM |
| Daten & Office | `"Daten & Office"` | 13 | SQL, NoSQL, MS-Office, LibreOffice |

Sheets können in mehreren Subgruppen vertreten sein (`data-subgroups="SG1 SG2"`).  
Bei neuen Sheets: Gruppenanzahl im Toolbar-HTML aktualisieren (wird auch dynamisch per JS gesetzt).
