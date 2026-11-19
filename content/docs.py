"""Alle Dokumente der Grundsicherungs-LVs. id -> (Datei unter source/gs/, Anzeigename, Zusatz?)"""
DOCS = {
  # Materielle Sicherung
  "msp": ("SA29VZPräsentation_MatSi__202610.pdf", "MATS Präsentation", False),
  "msk": ("Edits - Materielle Sicherung_Skriptum_WiSe2026_27.pdf", "MATS Skriptum", False),
  # Recht
  "rv": ("Verfassung 2026_neu.pdf", "Recht: Folien Verfassung", False),
  "r2": ("Skript Grundsicherung Teil 2 _2026_2027.pdf", "Recht: Skript Teil 2", False),
  "r3": ("Skript Grundsicherung Teil 3 _2026_2027.pdf", "Recht: Skript Teil 3", False),
  "f2": ("Antworten 2. fl-einheit.pdf", "Fernlehre 2", False),
  "f3": ("Antworten 3 fl-einheitl.pdf", "Fernlehre 3", False),
  "f4": ("Antworten 4. fl-einheit.pdf", "Fernlehre 4", False),
  "f5": ("Antworten 5. fl-einheit.pdf", "Fernlehre 5", False),
  "f6": ("Antworten 6. fl-einheit.pdf", "Fernlehre 6", False),
  "f7": ("Antworten 7 fl-einheitl.pdf", "Fernlehre 7", False),
  "fs": ("Pruefungsfragestunde_Recht_der_sozialen_Arbeit.pdf", "Recht: Prüfungsfragestunde (Mitschrift)", False),
  "fz": ("Pruefungsfragestunde_Recht_der_sozialen_Arbeit_2.pdf", "Recht: Prüfungsfragestunde 2 (Mitschrift)", False),
  "fa": ("Recht Fragen voriges Jahr.pdf", "Recht: Altfragen und Inhalte voriges Jahr (Mitschrift)", False),
  # Sozialpolitik
  "s1": ("WS26 SOPOL Einheit 1.pdf", "SoPol Einheit 1", False),
  "s2": ("WS26 SOPOL Einheit 2.pdf", "SoPol Einheit 2", False),
  "s3": ("WS26 SOPOL Einheit 3.pdf", "SoPol Einheit 3", False),
  "s4": ("WS26 SOPOL Einheit 4.pdf", "SoPol Einheit 4", False),
  "s5": ("WS26 SOPOL Einheit 5 Arbeitsmarktpolitik.pdf", "SoPol Einheit 5", False),
  "s6": ("WS26 SOPOL Einheit 6.pdf", "SoPol Einheit 6", False),
  "s7": ("WS26 SOPOL Einheit 7_aktualisiert.pdf", "SoPol Einheit 7: Klima", False),
  "s8": ("WS26 SOPOL Einheit 8.pdf", "SoPol Einheit 8: Gesundheit", False),
  "zb": ("Bettinger 2010.pdf", "Zusatztext: Bettinger 2010", True),
  "zf": ("FALTER_20240612_SEITE_18.pdf", "Zusatztext: Falter 24/24", True),
  "zn": ("Nullmeier 2019 - Begründungen des Wohlfahrtsstaats.pdf", "Zusatztext: Nullmeier 2019", True),
  "zt": ("Tálos Obinger 2020, S. 9-23.pdf", "Zusatztext: Tálos/Obinger 2020", True),
  "zw": ("WuG_2023_3_02+WEB.pdf", "Zusatztext: Wirtschaft & Gesellschaft 2023", True),
  # Orientierung und Berufsfelder
  "ob": ("VO_OR_Berufsfelder_Skriptum_2026_27.pdf", "ORBE Skriptum", False),
  # Fälle
  "cr": ("Fallanalyseraster-1.pdf", "Fallanalyseraster", False),
  "c1": ("2026 Teamteaching_Fall 1 Herr Z..pdf", "Fall 1: Herr Z.", False),
  "c2": ("2026 Teamteaching_Fall 2 Herr K..pdf", "Fall 2: Herr K.", False),
  "c3": ("2026 Teamteaching_Fall 3 Herr M..pdf", "Fall 3: Herr M.", False),
  "c4": ("2026 Teamteaching_Fall 4 Herr B..pdf", "Fall 4: Herr B.", False),
  "c5": ("2026 Teamteaching_Fall 5 Frau M..pdf", "Fall 5: Frau M.", False),
  "c6": ("2026 Teamteaching_Fall 6 Herr F..pdf", "Fall 6: Herr F.", False),
  "c7": ("2026 Teamteaching_Fall 7 Herr C..pdf", "Fall 7: Herr C.", False),
  "c8": ("2026 Teamteaching_Fall 8 Frau E..pdf", "Fall 8: Frau E.", False),
  "c9": ("2026 Teamteaching_Fall 9 Frau K..pdf", "Fall 9: Frau K.", False),
  "cu": ("2026_Übungsfall.pdf", "Übungsfall: Frau S.", False),
  "cb": ("BA_Fall_Sozialzentrum.pdf", "Fall Sozialzentrum: Frau A.", False),
}
OCR = {"zb": "bettinger.ocr.json", "zt": "talos.ocr.json"}
EXTRA = {k for k, v in DOCS.items() if v[2]}
# Web-Zusatzquellen: key -> (Titel, URL)
WEB = {
  "armut": ("Armutskonferenz: aktuelle Armuts- und Verteilungszahlen", "https://www.armutskonferenz.at/armut-in-oesterreich/aktuelle-armuts-und-verteilungszahlen.html"),
  # Gesetzestexte im RIS, fuer die Fernlehren 8 bis 11
  "kschg": ("RIS: Konsumentenschutzgesetz (§§ 1, 6, 25a bis 25d)", "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002462"),
  "abgb": ("RIS: ABGB (§§ 234, 864a, 879, 922, 1118, 1295, 1355, 1356)", "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001622"),
  "mrg": ("RIS: Mietrechtsgesetz (§§ 1, 11, 29, 30, 33)", "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002531"),
  "fagg": ("RIS: Fern- und Auswärtsgeschäfte-Gesetz (§§ 1, 3, 11)", "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847"),
  "io": ("RIS: Insolvenzordnung (§§ 28, 29, 43, 199)", "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001736"),
  "eheg": ("RIS: Ehegesetz (§ 98 Ausfallsbürgschaft)", "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001871"),
  "mschg": ("RIS: Mutterschutzgesetz (§§ 15, 15a Karenz)", "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008464"),
  "kja": ("Stadt Wien, MA 13: Folder Wiener Kinder- und Jugendarbeit (im Skriptum S. 86 zitiert)", "https://www.wien.gv.at/freizeit/bildungjugend/pdf/leporello-folder.pdf"),
  "shneu": ("Bundeskanzleramt: Ministerratsvortrag zur Sozialhilfe NEU", "https://www.bundeskanzleramt.gv.at/dam/jcr:4aedd2b4-539a-4e30-81e4-53fae18b6699/21a_1_mrv.pdf"),
}
# Nur zum Weiterlesen, daraus stammt keine Aussage in der App.
MORE = {
  "matsi": [("Fonds Soziales Wien", "https://www.fsw.at/"), ("Schuldenberatung Wien", "https://www.schuldenberatung.wien/"), ("Stadt Wien", "https://www.wien.gv.at/")],
  "recht": [("oesterreich.gv.at: Themen", "https://www.oesterreich.gv.at/de/themen"), ("Jusline", "https://www.jusline.at/"), ("RIS", "https://www.ris.bka.gv.at/")],
  "orbe": [("Fonds Soziales Wien", "https://www.fsw.at/"), ("Sozialinfo Wien", "https://sozialinfo.wien.at/"), ("Neustart", "https://www.neustart.at/")],
  "sopol": [("Armutskonferenz", "https://www.armutskonferenz.at/armut-in-oesterreich/aktuelle-armuts-und-verteilungszahlen.html"), ("verteilung.at", "https://www.verteilung.at")],
}
# Zahlen, die nur in Grafiken stehen (von Hand abgelesen), damit die Zahlenpruefung sie kennt.
FIG = {
  ("s3", 13): "99,6 0,4 64,9 35,1 93,8 6,2 86,6 13,4 81,3 18,7 13,0 87,0 90,7 9,3",
  ("s3", 16): "75 20 5", ("s3", 18): "51 30 19", ("s3", 20): "40 34 26",
  ("s6", 11): "1.969.000 50,1 1.591.000 40,5 305.000 7,8 52.000 1,3 16.000 0,4",
  ("s6", 12): "3,1 5,8 20,7 1,5 35,6 0,7 5,7 9,1 17,7 2019",
  ("s6", 13): "49,3 44,0 28,0 31,1 34,3 45,9 1,6 1,4 2,2",
}
FIG[("s4", 19)] = "59 20 8 16 48 60 84 57 51 25 23 5 37 40 68 41 31"
# Gerechnete Werte aus den Fallbeispielen; stehen auf keiner Seite, sind aber geprueft: 1229,89-1050 und 1229,89+2*332,07; 40*30.
DERIVED = {"179,89", "1.894,03", "1.200", "132,07", "1.494,03", "200"}  # dazu Fernlehre 9 D: 332,07-200 und 1229,89+2*132,07
# ETHOS-Tabelle im Skriptum ist ein Bild (Seite 83): Woerter fuer die Pruefung abgeschrieben.
FIG[("msk", 83)] = "Obdachlose Menschen öffentlichen Raum Verschlägen Brücken Notunterkünften Notschlafstellen Wärmestuben Wohnungsloseneinrichtungen Übergangswohnheime Asyle Herbergen Übergangswohnungen Frauenhäusern Frauenhäuser Einrichtungen MigrantInnen AsylwerberInnen Auffangstellen Quartiere ArbeitsmigrantInnen Institutionen entlassen Gefängnisse Strafanstalten Spitäler Heilanstalten Jugendheime Dauereinrichtungen Langzeitwohnheime ältere ambulante Wohnbetreuung Einzelwohnungen ungesicherten Wohnverhältnissen temporäre Unterkunft Freunden Bekannten Verwandten bestandsrechtliche Absicherung illegale Hausbesetzung Delogierung bedroht Gerichtliches Verfahren Auflösung Delogierungsbeschluss Enteignungsbeschluss Gewalt Strafanzeige Wegweisungsbeschluss Wohnprovisorien Wohnwägen Garagen Keller Dachböden Abbruchhäuser Zelte ungeeigneten Räumen Abbruchgebäuden überfüllten Räumen Mindestquadratmeter 1.1 2.1 3.1 3.2 3.3 4.1 5.1 5.2 6.1 6.2 6.3 7.1 7.2 8.1 8.2 8.3 9.1 9.2 9.3 10.1 11.1 11.2 11.3 12.1 13.1"
# SoPol Einheiten 7 und 8: Grafiken und Tabellen, die nur als Bild auf den Folien stehen (abgeschrieben).
FIG[("s7", 7)] = "Ökologische Belastungsgrenzen Klimakrise Unversehrtheit der Biosphäre Einbringung neuartiger Substanzen Ozonloch Partikelverschmutzung Ozeanversauerung Biogeochemische Kreisläufe Süßwasserverbrauch Landnutzungsänderungen"
FIG[("s7", 8)] = "Country Overshoot Days 2025 Earth Overshoot Day"
FIG[("s7", 9)] = "Folgen der Erderhitzung Stand 2021 1,1 Grad derzeitiger Pfad 3,2 Grad bis 2100 Extremwetterereignisse häufiger heftiger Ernteerträge Hitzewellen Überschwemmungen Dürreperioden Nahrungsmittelknappheit"
FIG[("s7", 11)] = "Konsumemissionen Einkommen Oxfam reichste 5 % verantwortlich für 37 % reichste 10 % für 46 % des Emissionswachstums mittlere 40 % für 49 % ärmste 50 % für 6 % 1990 2015"
FIG[("s7", 12)] = "CO2-Fußabdruck Haushalte EU Top 1 % Top 10 % Middle 40 % Bottom 50 % Bottom 5 % Land travel Air travel Flugreisen"
FIG[("s7", 17)] = "Sustainable Development Goals Economy Society Biosphere Wirtschaft Gesellschaft Biosphäre"
FIG[("s7", 18)] = "Doughnut Economics ecological ceiling ökologische Decke social foundation soziales Fundament ecological overshoot social shortfall"
FIG[("s7", 19)] = "Overconsumption Underconsumption Corridors balanced consumption Environmental and just ceiling Social floor Überkonsum Unterkonsum Obergrenze Untergrenze"
FIG[("s7", 25)] = "Klimasozialpolitik Soziale Klimapolitik Berücksichtigung sozialer Aspekte in Klimapolitik Energiepolitik Mobilität Wohnen Finanzpolitik Ernährung Landwirtschaft Klimaresiliente Sozialpolitik Klimaschutz Klimaanpassung in Diensten Einrichtungen Sozial- Gesundheitswesens Sozialversicherungssystemen Sozialleistungen Arbeitsmarktpolitik Gesundheitspolitik Versicherungswesen"
FIG[("s7", 27)] = "Finanzielle Ressourcen Ökologisch-ökonomische Umverteilung Klimageld sozial gerechte Lastenverteilung Klimaschutzmaßnahmen Grundsicherung Transformationsteilhabe Ermöglichung klimafreundlichen Lebensstils Finanzierung klimafreundlichen Maßnahmen Nachhaltige Beschaffungsrichtlinien Wohlfahrtspflege Bundesförderprogramm Klima-Manager Finanzielle Anreize Abschaffung klimaschädlicher Strukturen Divestment Renten Pensionsfonds fossilen Ressourcen"
FIG[("s7", 28)] = "Infrastruktur Ökologische Daseinsvorsorge Kostenloser kostengünstiger Zugang sozialer Infrastruktur Pflegebereich Soziale Mobilitätswende Versorgungswege Barrierefreiheit Ober- Untergrenzen Energie Wohnen Suffizienz-Orientierung Energiesparanreize Personen hohem Einkommen Schutzprogramme Klimaauswirkungen Hitzeaktionspläne älterer pflegebedürftiger Menschen Institutionalisierung Ökologische Zeitpolitik Telearbeit familienfreundliche Arbeitsorganisation Klimasozialer Rechtsrahmen Ökosozialversicherung zusätzlich Sozialversicherung Integration Klimaaspekten Versicherungen Verankerung ökologischen Nachhaltigkeitsziels Sozialrecht"
FIG[("s8", 3)] = FIG[("s7", 25)]
FIG[("s8", 5)] = "Gesundheit Wohlbefinden Physisch Mental Sozial Sexuell Sozioökonomische Resilienz Kognitiv Funktional Generelle Anliegen"
FIG[("s8", 7)] = "Sozialausgaben Bruttoinlandsprodukt 2024 161,5 Mrd 32,7 % Krankenversicherung 5,6 % Pensionsversicherung 12,9 % Unfallversicherung 0,4 % Sonstige Sozialausgaben 13,8 %"
FIG[("s8", 9)] = "Steuern Sozialversicherungsbeiträge Mobile Dienste Pflegeheime Spitäler Rehabilitation extramurale ärztliche Versorgung Medikamente Medizinprodukte therapeutische Patienten Privatversicherung"
FIG[("s8", 10)] = "57,8 Mrd 2024 44,1 % Sozialversicherung Krankenversicherung 31,6 % Staat Bund Länder Gemeinden 16,7 % Selbstzahlungen privaten Haushalte 5,5 % Private Krankenversicherung 2,0 % Sonstige"
FIG[("s8", 11)] = "57,8 Mrd 2024 31,8 % Stationär tagesklinisch 28,7 % Ambulante Gesundheitsversorgung 15,2 % Medizinische Güter Medikamente 14,3 % Langzeitpflege 4,4 % Verwaltung 3,2 % Hilfsleistungen 2,5 % Prävention 0,1 % Häusliche"
FIG[("s8", 12)] = "Ungedeckter medizinischer Bedarf Einkommen 2024 People at risk of poverty"
FIG[("s8", 18)] = "Schulbildung Männer Pflichtschule 58,8 26,2 15,0 Höhere Schule Akademie Hochschule 83,8 12,9 3,3 Frauen Pflichtschule 58,8 29,5 11,7 Höhere 82,4 13,3 4,3 sehr guter sehr schlechter Gesundheitszustand Gesundheitsbefragung 2019"
FIG[("s8", 19)] = "Einkommensklassen medianen Haushaltsäquivalenzeinkommens Männer unter 60 % 60,7 25,3 14,1 150 % 86,0 11,6 2,4 Frauen unter 60 % 64,8 26,6 8,6 150 % 86,7 10,9 2,4 sehr guter sehr schlechter Gesundheitszustand"
FIG[("s8", 20)] = "Migrationshintergrund Männer Österreich 76,1 18,1 5,8 Ehemaliges Jugoslawien Türkei 61,9 19,9 18,2 Frauen Österreich 76,0 18,6 5,4 Ehemaliges Jugoslawien Türkei 55,9 30,4 13,7 sehr schlechter Gesundheitszustand"
