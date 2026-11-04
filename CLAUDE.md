# Sprengel

Mobiles Lernzentrum fuer das Studium Soziale Arbeit, statisch auf GitHub Pages. LVs: Geschichte der Sozialen Arbeit und das Modul Grundsicherung (Materielle Sicherung, Recht, Sozialpolitik, Fallwerkstatt). Uebergreifend: XP, Level, Streak, Tagesauftraege, Abzeichen, Exkurse.

- `content/geschichte.py`: alle Lerninhalte (Karten, Themen, 26 Leitfragen, Zeitstrahl, Stolperfallen), jede Aussage mit Folienverweis `("doc", seite)`.
- `tools/build_content.py`: baut `site/data/geschichte.json` und prueft Verweise. Jede Zahl in Antwort oder Erklaerung muss auf einer zitierten Seite stehen, sonst bricht der Build ab.
- `tools/build_slides.py`: rendert `source/*.pdf` und `source/gs/*.pdf` und legt die Seiten AES-GCM-verschluesselt nach `site/slides/`. Code liegt in `.slide-passphrase`.
- `site/`: die App (Vanilla JS, kein Build), `sw.js` fuer offline. Fortschritt nur im localStorage.
- Deploy: Push auf `main`, Action veroeffentlicht `site/`.

Dokument `j` ist der Zusatztext „100 Jahre Wiener Jugendamt“ (Seiten entsprechen dem Druck). Karten nur daraus sind `extra`: gekennzeichnet, seltener, zaehlen nicht gegen den Stempel. `build_slides.py j` baut einzelne Dokumente, ohne die uebrigen Dateien zu aendern.

## Modul Grundsicherung

- `content/matsi.py`, `recht.py`, `sopol.py`, `faelle.py`: Kursinhalte mit den Bausteinen aus `content/dsl.py`. `content/links.py`: Exkurse zwischen LVs. `content/docs.py`: Dokumente (`source/gs/`), Web-Quellen, Grafikzahlen.
- `tools/build_all.py` baut diese Kurse und `links.json`. Harte Pruefung: Seite existiert, jede Zahl steht auf einer zitierten Seite. Grafikzahlen in `docs.FIG`, gerechnete Fallwerte in `docs.DERIVED`. Geschichte baut weiter `tools/build_content.py`.
- Karten-Typen zusaetzlich zu Geschichte: `bucket` (zuordnen), `chain` (Fallkette), `calc` (Rechnen). Ein `ord` ohne Jahreszahlen nimmt die Listenreihenfolge.
- Neue Fernlehren oder Einheiten: PDF nach `source/gs/`, in `docs.py` eintragen, `build_slides.py <id>` und Inhalte ergaenzen; den Eintrag mit `pending=True` im Kurs ersetzen. Es fehlen noch 4 Fernlehren und 4 SoPol-Einheiten.
- Bettinger und Talos/Obinger sind Scans: Ihr OCR-Text liegt in `source/gs/*.ocr.json`.
- Fall-Loesungspunkte stammen von Claude, nicht von den Lehrenden; das steht auch in der App.
- Notizen aus den PDFs sind nachrangig und als „Deine Notiz“ gekennzeichnet. Bei Widerspruechen in `TRAP`.

Regeln:
- Inhalt kommt nur aus den LV-Unterlagen. Widersprueche zwischen Unterlagen kommen in `TRAPS`, nicht stillschweigend aufloesen.
- `source/` und `.slide-passphrase` bleiben ausserhalb von Git: Die Folien gehoeren der Lehrveranstaltung, das Repo ist oeffentlich.
- Kapitel mit `sober=True` (NS) bekommen keine Spiel-Effekte.
- Abhaengigkeiten der Tools: `pymupdf`, `cryptography`.
