# Montsera11y — Voortgang

## Wat is gelukt

- [x] Omgeving opgezet (FontForge, fonttools, brotli, mapstructuur)
- [x] 8 bronbestanden (Light, Regular, Medium, Bold + Italic varianten) gekopieerd naar `working/`
- [x] Scripts geschreven: `rename_font.py` (hernoemen + WOFF2) en `verify_font.py` (metadata-check)
- [x] Testpagina `test.html` aangemaakt met vergelijking origineel vs. aangepast
- [x] Licentiebestand `OFL.txt` met derivative copyright voor Eleven Ways
- [x] **Eerste aanpassing aan de letter `e`** in Montserrat-Regular.ttf (schuine crossbar) — gelukt!
- [x] Exporteren vanuit FontForge naar TTF → rename-script → WOFF2 → testpagina — werkt!
- [x] `e` — schuine crossbar
- [x] `l` — serif linksboven
- [x] `I` — bilaterale schreven boven en onder
- [x] `w` — serif linksboven

### De fontgewichten
De 4 glyphs moeten aangepast worden in alle deze gewichten:

- [ ] Montserrat-Light.ttf
- [ ] Montserrat-LightItalic.ttf
- [ ] Montserrat-Regular.ttf
- [ ] Montserrat-Italic.ttf (Regular Italic)
- [ ] Montserrat-Medium.ttf
- [ ] Montserrat-MediumItalic.ttf
- [ ] Montserrat-Bold.ttf
- [ ] Montserrat-BoldItalic.ttf

## Bekend probleem

- [ ] **Kerning klopt niet** na export uit FontForge — moet onderzocht worden. Mogelijk gaan kerning-tabellen (GPOS) verloren bij Generate Fonts, of moeten ze opnieuw worden opgebouwd.


### Afronding
- [ ] Kerningprobleem oplossen
- [ ] Alle fonts door rename-script halen
- [ ] Visuele controle via testpagina
- [ ] Optioneel: fontbakery validatie
