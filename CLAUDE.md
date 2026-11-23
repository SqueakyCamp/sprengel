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
- Neue Fernlehren oder Einheiten: PDF nach `source/gs/`, in `docs.py` eintragen, `build_slides.py <id>` und Inhalte ergaenzen; den Eintrag mit `pending=True` im Kurs ersetzen. SoPol ist vollständig (Einheiten 1 bis 8); Armut-Gastvortrag ohne Folien und nicht prüfungsrelevant, Wiederholung 23.11. bringt keine neuen Inhalte.
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

## Ausbau 15.11.2026

- Stufen: `ETAPPEN` in app.js, 40 Stufen in 6 Etappen (Berufsweg Soziale Arbeit, nicht Geschichte), Schwelle `60k²+90k` gerundet, danach Ehrenstufen alle `HONOR` XP. Aufstieg zeigt nach der Runde ein Overlay (`celebrate`, `S.lvSeen`). Geschichte behält die alten Namen als LV-Ränge (`GESCH_RANKS`). LV-Ränge stehen in den Kursdateien, nach dem letzten Rang gibt es Sterne.
- Abzeichen: `BADGES` mit Stufen Bronze bis Platin, gefeierte Stufe in `S.bd`.
- Blitzrunde: 3 XP je richtige Antwort, 15 für neuen Rekord.
- Prüfungsplan (nur auf der Startseite der LV, nicht im Hub): `planFor` rechnet aus offenen Karten (neu/falsch 2, Box 1 eine, fällig eine) und Tagen bis zum Termin ein Tagesziel, fixiert pro Tag in `S.plan`.
- Kapitel-Boss: ab 80 % gelernt (`bossState`), 10 schwere Karten, 2 Herzen, Sieg in `S.boss`. Nicht für `sober`-Kapitel und Fälle.
- Akten: Fallwerkstatt-Fälle haben 8 Vermerke (6 Rasterschritte ab 50 %, Fallkette, Prioritäten einmal richtig, `S.aktOk`); geschlossen in `S.akten`.
- Offene Fragen in 3 Stufen: Erkennen (eigene Punkte zwischen fremden derselben LV), Ergänzen (Schlüsselwort-Lücken, automatisch gewählt), frei. Normale Runden nehmen die nächste offene Stufe (`nextLfItem`), Probeläufe immer frei. Jede offene Frage und Stufe hat „Überspringen“ ohne Wertung.
- Sicherung als JSON-Datei (`backupFile`/`restoreState`), Hinweis im Hub nach 7 Tagen ohne Sicherung.
- Grafiken: `content/figs.py` (kinds lanes, pyramid, compare), je Kapitel; gebaut in `figs` der Kurs-JSON, Zahlen und Seiten geprüft wie Karten. Lange Wörter mit `­` trennen.
- Recht: Fernlehre-Kapitel aufgelöst und thematisch einsortiert (r8 Verträge/Miete, r9 Sozialhilfe, rx Insolvenz, rl ALV, rkb KBG/Karenz). Die Fragenseite gruppiert nach Fernlehre (`course.groupedLf`).
- Hub verlinkt die Sozialarbeitskarte unten unter „Mehr zum Studium“.

## Prüfungsfragestunde Recht und offene Fragen im Fortschritt (17.11.2026)

- Dokument `fs` = Mitschrift der Prüfungsfragestunde Recht (über other/Jakob). `content/recht_fs.py`: neue Themen (r-form, r-gutschein, r-alvweg, r-beweis, r-mandat, r-ngo, r-wmg) und 64 Karten mit `pf`, Tab „Prüfungsfragen“ in Recht (6 Blöcke, Simulation 20 Fragen in 30 Min., Zeit ist geschätzt). Antworten mit Skript/Folien belegt; Abweichungen der Mitschrift als TRAP. „Hebel“ in der Mitschrift = vermutlich HibL.
- Recht-Skript Teil 2: Seitenzahl im PDF ist gedruckte Seite + 1 (Gutscheine stehen auf PDF-Seite 59).
- App: Offene Fragen zählen zum Kapitel- und LV-Prozent (`lfDone`: Stufe 2 Lückentext geschafft oder freie Antwort ab 50 %). Stempel braucht weiter die freie Antwort. `pickLf` nimmt erst Stufe 1 aller Fragen, dann Stufe 2, dann frei. Kapitelrunde: Fehlen höchstens 3 Karten, kommen bis zu 4 offene Fragen dazu (`mixIn` verteilt sie).

## Altfragen, Fragestunde 2, Prüfungsmodus, SoPol 7 und 8 (19.11.2026)

- Recht: Dokumente `fz` (zweite Prüfungsfragestunde) und `fa` (Altfragen und Inhalte vom Vorjahr, Mitschrift). `content/recht_alt.py`: neue Themen (materiell/formell, Auslegung, Instanzenzug, Gerichtspersonen, Außerstreit, BP/Bundesversammlung, Neutralität, Exekutionsbewilligung, Schuldenregulierung, Insolvenz-Änderungen, Anwartschaft, EU-Grundfreiheiten), offene Altfragen 52 bis 59 (Gruppe „Altfragen voriges Jahr“), pf-Block „Altfragen voriges Jahr“, TRAPs zu Abweichungen der Mitschriften.
- Prüfungsmodus (`course.exam`, nur Recht, `recht_alt.exam_meta`): 23 Fragen in 30 Min., 20 geschlossene (2 je Themenblock aus `EXAM_BLOCKS`, nur mc/tf/multi), 3 offene je eine aus Topf 1/2/3 (`EXAM_TOPF`). Frei springen, markieren, abgeben; danach Selbsteinschätzung der offenen Fragen, dann Auswertung. Plus/Minus: (richtige minus falsche Kreuze) durch Anzahl richtiger, min. 0. 44 Punkte für offene Fragen sind genannt, 100 gesamt ist eine Annahme. Code: `startPx`/`renderPx`/`pxResult` in app.js, Route `#/pruefung`, Zustand `PX`.
- Lückentext (Stufe 2): Punkte bleiben in der Reihenfolge der Antwort (vorher gemischt).
- SoPol: `content/sopol_kg.py` mit Einheit 7 (Klima, `s7`) und 8 (Gesundheit, `s8`), offene Fragen 11 bis 14. Bildfolien abgeschrieben in `docs.FIG`. Kapitel „Standpunkte“ und Wahlkabine-Quelle entfernt (nicht prüfungsrelevant).

## Korrekturen 23.11.2026

- Offene Fragen: Jeder Antwortpunkt muss zur angezeigten Frage passen. Beantwortet ein Punkt eine Teilfrage der Fernlehre, die nicht im Fragetext steht, die Teilfrage in den Fragetext aufnehmen oder den Punkt streichen (Fälle waren Nr. 13, 15, 18, 21, 23).
- Keine Geld-Rechenaufgaben (weder `calc` noch MC mit ausgerechneten Summen) und keine Fristrechnungen mit Datum, in keiner LV. Stattdessen abfragen, wie sich ein Betrag zusammensetzt bzw. wann eine Frist beginnt und endet.
- Instanzen: Karten zur Zuständigkeit nach Strafdrohung (BG bis 1 Jahr, LG Einzelrichter*in bis 5 Jahre, Schöff*innen darüber, Geschworene bei den schwersten Delikten) und Streitwert in `recht_alt.py`.
