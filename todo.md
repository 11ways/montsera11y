# Montsera11y — Voortgang

## Wat is gelukt

- [x] Omgeving opgezet (FontForge, fonttools, brotli, mapstructuur)
- [x] 8 bronbestanden (Light, Regular, Medium, Bold + Italic varianten) gekopieerd naar `working/`
- [x] Scripts geschreven: `rename_font.py` (hernoemen + WOFF2) en `verify_font.py` (metadata-check)
- [x] Testpagina `test.html` aangemaakt met vergelijking origineel vs. aangepast
- [x] Licentiebestand `OFL.txt` met derivative copyright voor Eleven Ways
- [x] **Eerste aanpassing aan de letter `e`** in Montserrat-Regular.ttf (schuine crossbar) — gelukt!
- [x] Exporteren vanuit FontForge naar TTF → rename-script → WOFF2 → testpagina — werkt!

## Bekend probleem

- [ ] **Kerning klopt niet** na export uit FontForge — moet onderzocht worden. Mogelijk gaan kerning-tabellen (GPOS) verloren bij Generate Fonts, of moeten ze opnieuw worden opgebouwd.

## Nog te doen

### Glyph-aanpassingen in Montserrat-Regular.ttf
- [x] `e` — schuine crossbar
- [ ] `l` — serif linksboven (eerste poging gedaan, moet verfijnd worden)
- [ ] `I` — bilaterale schreven boven en onder
- [ ] `w` — serif linksboven

### Overige fontgewichten
Dezelfde 4 glyphs moeten aangepast worden in alle andere gewichten:

- [ ] Montserrat-Light.ttf
- [ ] Montserrat-LightItalic.ttf
- [ ] Montserrat-Italic.ttf (Regular Italic)
- [ ] Montserrat-Medium.ttf
- [ ] Montserrat-MediumItalic.ttf
- [ ] Montserrat-Bold.ttf
- [ ] Montserrat-BoldItalic.ttf

### Afronding
- [ ] Kerningprobleem oplossen
- [ ] Alle fonts door rename-script halen
- [ ] Visuele controle via testpagina
- [ ] Optioneel: fontbakery validatie
