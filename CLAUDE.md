# Sprengel

Mobiles Lernzentrum fuer das Studium Soziale Arbeit, statisch auf GitHub Pages. Derzeit eine LV: Geschichte der Sozialen Arbeit.

- `content/geschichte.py`: alle Lerninhalte (Karten, Themen, 26 Leitfragen, Zeitstrahl, Stolperfallen), jede Aussage mit Folienverweis `("doc", seite)`.
- `tools/build_content.py`: baut `site/data/geschichte.json` und prueft Verweise. Jede Zahl in Antwort oder Erklaerung muss auf einer zitierten Seite stehen, sonst bricht der Build ab.
- `tools/build_slides.py`: rendert `source/*.pdf` und legt die Seiten AES-GCM-verschluesselt nach `site/slides/`. Code liegt in `.slide-passphrase`.
- `site/`: die App (Vanilla JS, kein Build), `sw.js` fuer offline. Fortschritt nur im localStorage.
- Deploy: Push auf `main`, Action veroeffentlicht `site/`.

Regeln:
- Inhalt kommt nur aus den LV-Unterlagen. Widersprueche zwischen Unterlagen kommen in `TRAPS`, nicht stillschweigend aufloesen.
- `source/` und `.slide-passphrase` bleiben ausserhalb von Git: Die Folien gehoeren der Lehrveranstaltung, das Repo ist oeffentlich.
- Kapitel mit `sober=True` (NS) bekommen keine Spiel-Effekte.
- Abhaengigkeiten der Tools: `pymupdf`, `cryptography`.
