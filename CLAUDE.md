# Sprengel

Mobiles Lernzentrum fuer das Studium Soziale Arbeit, statisch auf GitHub Pages. LVs: Geschichte der Sozialen Arbeit, ORBE (Orientierung und Berufsfelder) und das Modul Grundsicherung (Materielle Sicherung, Recht, Sozialpolitik, Fallwerkstatt). Uebergreifend: XP, Level, Streak, Tagesauftraege, Abzeichen, Exkurse.

- `content/geschichte.py`: alle Lerninhalte (Karten, Themen, 26 Leitfragen, Zeitstrahl, Stolperfallen), jede Aussage mit Folienverweis `("doc", seite)`.
- `tools/build_content.py`: baut `site/data/geschichte.json` und prueft Verweise. Jede Zahl in Antwort oder Erklaerung muss auf einer zitierten Seite stehen, sonst bricht der Build ab.
- `tools/build_slides.py`: rendert `source/*.pdf` und `source/gs/*.pdf` und legt die Seiten AES-GCM-verschluesselt nach `site/slides/`. Code liegt in `.slide-passphrase`.
- `site/`: die App (Vanilla JS, kein Build), `sw.js` fuer offline. Fortschritt nur im localStorage.
- Deploy: Push auf `main`, Action veroeffentlicht `site/`.

Dokument `j` ist der Zusatztext „100 Jahre Wiener Jugendamt“ (Seiten entsprechen dem Druck). Zusatztexte und Web-Zusatzquellen sind nur Lese- und Belegquellen: keine Quizkarten, die sich nur auf sie stuetzen (Wunsch vom 8.11.2026). `build_slides.py j` baut einzelne Dokumente, ohne die uebrigen Dateien zu aendern.

## Modul Grundsicherung

- `content/matsi.py` (+ `matsi_plus.py`), `recht.py` (+ `recht_fl.py`, Fernlehren 8 bis 11), `sopol.py`, `faelle.py`: Kursinhalte mit den Bausteinen aus `content/dsl.py`. `content/links.py`: Exkurse zwischen LVs. `content/docs.py`: Dokumente (`source/gs/`), Web-Quellen, Grafikzahlen.
- `tools/build_all.py` baut diese Kurse und `links.json`. Harte Pruefung: Seite existiert, jede Zahl steht auf einer zitierten Seite. Grafikzahlen in `docs.FIG`, gerechnete Fallwerte in `docs.DERIVED`. Geschichte baut weiter `tools/build_content.py`.
- MatSi: Betraege nicht abfragen (aendern sich jaehrlich), nur Regeln, Prozentsaetze, Fristen; Betraege duerfen in Erklaerungen stehen. Keine `calc`-Karten in MatSi.
- Fragen muessen ohne Nachbarkarte verstaendlich sein (keine Titel wie „Welches Regime?“). Erklaerungen 2 bis 3 Saetze. Jeder Punkt einer offenen Frage soll auch als Quizkarte (mit `lf`) vorkommen.
- App: Kapitel-Button oeffnet die erste zitierte Seite der Kapitelthemen; neue Karten haben Vorrang (max. 35 % faellige, reihum aus wenig gesehenen Themen); offene Antwort zaehlt ab 70 % der Punkte voll (`OPEN_FULL`). Bei App-Aenderungen `SHELL` in `sw.js` hochzaehlen.
- Karten-Typen zusaetzlich zu Geschichte: `bucket` (zuordnen), `chain` (Fallkette), `calc` (Rechnen). Ein `ord` ohne Jahreszahlen nimmt die Listenreihenfolge.
- Kurzname MATS (nicht MatSi), so an der FH. Der Kurs-id bleibt `matsi`.
- Erklaerungen, Themen und Exkurse ausfuehrlich in ganzen Saetzen, Niveau wie MATS; keine Stichwortketten.
- Modul-Mix: Karten der Fallwerkstatt nur mit `solo=True` (ohne Fall verstaendlich), keine Fallketten und Reihungen.
- Fernlehren 8 bis 11 kamen ohne Musterantworten: Antworten von Claude aus Skripten und RIS-Gesetzestexten (`@kschg`, `@mrg` usw. in `docs.WEB`). Recht-Skript Teil 2: PDF-Seite = gedruckte Seite + 1, Verweise nutzen die PDF-Seite.
- Studierenden-Fragensammlungen (z. B. „Potenzielle Prüfungsfragen MATS“) nur als Themenhinweis, nie als Quelle oder Dokument.
- Neue Fernlehren oder Einheiten: PDF nach `source/gs/`, in `docs.py` eintragen, `build_slides.py <id>` und Inhalte ergaenzen; den Eintrag mit `pending=True` im Kurs ersetzen. Es fehlen noch SoPol-Einheiten (Klima, Gesundheit, Wiederholung) und die Armut-Folien.
- Bettinger und Talos/Obinger sind Scans: Ihr OCR-Text liegt in `source/gs/*.ocr.json`.
- Fall-Loesungspunkte stammen von Claude, nicht von den Lehrenden; das steht auch in der App.
- Notizen aus den PDFs sind nachrangig und als „Deine Notiz“ gekennzeichnet. Bei Widerspruechen in `TRAP`.

Regeln:
- Inhalt kommt nur aus den LV-Unterlagen. Widersprueche zwischen Unterlagen kommen in `TRAPS`, nicht stillschweigend aufloesen.
- `source/` und `.slide-passphrase` bleiben ausserhalb von Git: Die Folien gehoeren der Lehrveranstaltung, das Repo ist oeffentlich.
- Kapitel mit `sober=True` (NS) bekommen keine Spiel-Effekte.
- Abhaengigkeiten der Tools: `pymupdf`, `cryptography`.

## Prüfungsfragen-Tab und ORBE (11.11.2026)

- Karten mit `pf="<Block>"` erscheinen im Tab „Prüfungsfragen“ bzw. „Altfragen“ neben den Kernfragen (`course.pf` = blocks, info, n, minutes). Dort gibt es Üben je Block, „Falsche wiederholen“ und eine Simulation ohne Zwischen-Rückmeldung mit Timer.
- MATS: `content/matsi_pf.py`, Fragen aus der Sammlung „MATS Fragen“ (Ausnahme zur Regel oben, ausdrücklicher Wunsch). Antworten kommen aus Präsentation/Skriptum; Abweichungen der Mitschrift als TRAP.
- MATS-Kernfragen sind nach der Reihung der Linie nummeriert (`ORDER` in matsi.py). `course.renumber` (alt -> neu) zieht in der App den gespeicherten Fortschritt einmal mit (`S.migMatsi1`). Neue Kernfragen hinten anhängen geht, die Nummern werden automatisch neu vergeben.
- ORBE: `content/orbe.py`, Skriptum `ob`. Klein gehalten. Nicht abfragen: die langen Texte zu Behinderung und Alter, Einrichtungslisten. Die Altfragen (Mitschrift) sind die `pf`-Karten. Altfrage 39 stützt sich auf den MA-13-Folder `@kja`.
- `#/stufen`: Übersicht der globalen Stufen und der Ränge je LV, erreichbar über das Level im Hub und unter „Ich“.
