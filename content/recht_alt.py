"""Recht: zweite Prüfungsfragestunde (`fz`) und Altfragen samt Inhalten vom Vorjahr (`fa`), beide über other/Jakob am 19.11.2026.
Daniel wollte alles einarbeiten, was noch nicht drin war. Antworten sind mit Skript und Folien belegt; was nur in einer Mitschrift steht, ist so gekennzeichnet.
Die offenen Altfragen kommen laut Mitschrift aus drei „Töpfen“; daraus zieht der Prüfungsmodus je eine Frage (`EXAM_TOPF`)."""

GROUP = "Altfragen voriges Jahr"
ALT = "Altfragen voriges Jahr"
# Topf -> Nummern der offenen Fragen. Bestehende Fernlehre-Fragen, die den Altfragen entsprechen, sind mit drin.
EXAM_TOPF = {"1": [52, 53], "2": [7, 28, 54, 55], "3": [17, 56, 57, 58, 59]}


def add(c):
    T, TRAP, OPEN, TERM = c.T, c.TRAP, c.OPEN, c.TERM

    def tag(block):
        if block:
            c.cards[-1]["pf"] = block

    def MC(b, t, lf, q, right, wrong, why, src):
        c.MC(t, lf, q, right, wrong, why, src); tag(b)

    def TF(b, t, lf, q, val, why, src):
        c.TF(t, lf, q, val, why, src); tag(b)

    def MU(b, t, lf, q, right, wrong, why, src):
        c.MULTI(t, lf, q, right, wrong, why, src); tag(b)

    def MA(b, t, lf, q, pairs, why, src):
        c.MATCH(t, lf, q, pairs, why, src); tag(b)

    def ORD(t, lf, q, items, why, src):
        c.ORD(t, lf, q, items, why, src)

    def BU(b, t, lf, q, buckets, items, why, src):
        c.BUCKET(t, lf, q, buckets, items, why, src); tag(b)

    import recht_fs
    V, AL, Z, X, S, M = recht_fs.BLOCKS

    # ---------------- neue Themen ----------------
    T("r-materiell", "rn", "Materielles und formelles Recht",
      "Materielles Recht regelt den Inhalt: Was gilt, welche Rechte und Pflichten bestehen? Dazu gehört, was ein Kaufvertrag ist, dass Eltern ihren Kindern Unterhalt schulden, was Diebstahl ist oder dass im Ortsgebiet höchstens 50 km/h erlaubt sind. Auch das Kindeswohl in § 138 ABGB ist materielles Recht. "
      "Formelles Recht regelt, wie materielle Rechte durchgesetzt werden: welches Gericht oder welche Behörde zuständig ist, welche Frist gilt und wie das Verfahren abläuft. Dass Eltern Unterhalt schulden, ist materiell; wie man ihn einklagt, ist formell. "
      "Merksatz aus der zweiten Prüfungsfragestunde: Inhalt, Rechte und Pflichten sind materielles Recht; Verfahren, Zuständigkeit, Fristen und Durchsetzung sind formelles Recht.",
      [("fz", 1), ("fz", 2)])
    T("r-auslegung", "rs", "Auslegung des Rechts",
      "Gesetze müssen ausgelegt werden. Die Folien nennen die Wortinterpretation (allgemeiner Sprachgebrauch oder Legaldefinition, wenn das Gesetz Begriffe selbst bestimmt), die logisch-grammatikalische, die systematische (mit Blick auf andere Normen), die historische (Gesetzesmaterialien wie Regierungsvorlagen), die teleologische (objektiver Sinn und Zweck einer Bestimmung) sowie die verfassungskonforme und die gemeinschaftsrechtskonforme Interpretation. "
      "Laut zweiter Prüfungsfragestunde muss man die Methoden nicht auswendig können, aber wiedererkennen. Eine „dynamische interpretative Auslegung“ nannte die Lehrende als falsche Antwortmöglichkeit.",
      [("rv", 21), ("fz", 2)])
    T("r-instanz", "ri", "Instanzenzug im Straf- und Zivilrecht",
      "Das gerichtliche Strafverfahren ist nur in 2 Instanzen angelegt: Urteilt das Bezirksgericht, geht die Berufung binnen 4 Wochen an das Landesgericht; im Strafprozess muss man das Rechtsmittel nach der Verkündung binnen 3 Tagen anmelden. Urteilt das Landesgericht, geht es laut Altfragen-Mitschrift mit Berufung an das Oberlandesgericht oder mit Nichtigkeitsbeschwerde an den OGH. "
      "Am Landesgericht entscheiden je nach Schwere Einzelrichter*innen, Schöff*innensenate oder Geschworenengerichte; die Mitwirkung von Schöff*innen und Geschworenen ist ein Grundsatz der Gerichtsbarkeit und Ausdruck des demokratischen Prinzips. "
      "Das Zivilverfahren hat grundsätzlich 3 Instanzen: Bezirksgericht, Landesgericht, OGH oder Landesgericht, Oberlandesgericht, OGH. Gegen Urteile erster Instanz gibt es Berufung (in der Regel vier Wochen), gegen Urteile zweiter Instanz Revision, gegen Beschlüsse Rekurs. Zum OGH kommt man nur in wichtigen Rechtssachen, wenn eine erhebliche Rechtsfrage vorliegt.",
      [("f3", 6), ("r2", 29), ("r2", 30), ("rv", 73), ("fa", 1), ("fa", 2)])
    T("r-gerichtspers", "ri", "Gerichtspersonen",
      "Berufsrichter*innen sind ausgebildete Jurist*innen, die nach Studium, Gerichtspraxis, richterlicher Vorbereitung und Richteramtsprüfung ernannt werden; sie sind unabhängig, unversetzbar und grundsätzlich unabsetzbar. "
      "Laienrichter*innen wirken nach Art 91 B-VG an der Rechtsprechung mit: im Strafprozess mit kontrollierender Funktion, im Zivilprozess als fachkundige Personen, etwa in der Arbeits- und Sozialgerichtsbarkeit. "
      "Rechtspfleger*innen sind besonders geschulte Beamt*innen des gehobenen Dienstes, die bestimmte Agenden selbständig erledigen, etwa Kindesunterhalt berechnen, Grundbuch, Firmenbuch und Exekution.",
      [("r2", 24), ("fa", 12)])
    T("r-ausserstreit", "rz", "Außerstreitverfahren",
      "Neben dem streitigen Zivilprozess nach der ZPO gibt es das Außerstreitverfahren nach dem Außerstreitgesetz (AußStrG). Es hat rechtsfürsorglichen Charakter und wird auf Antrag oder von Amts wegen eingeleitet, etwa für eine Erwachsenenvertretung. "
      "Laut Altfragen-Mitschrift gehören dazu auch Obsorge, Unterhalt, Verlassenschaft, einvernehmliche Scheidung und Adoption. Das Gericht ermittelt selbst, entscheidet mit Beschluss, und das Rechtsmittel ist der Rekurs. "
      "Der Zivilprozess ist dagegen formstrenger, hat ein höheres Kostenrisiko und wird nur auf Klage eingeleitet: „Wo kein*e Kläger*in, da kein*e Richter*in.“ Genauer behandelt wird das Außerstreitverfahren im zweiten Semester.",
      [("r2", 23), ("r2", 25), ("fa", 13), ("fa", 14)])
    T("r-bv", "rp", "Bundespräsident*in, Bundesversammlung, Immunität",
      "Die Bundespräsidentin oder der Bundespräsident wird unmittelbar auf 6 Jahre gewählt; laut Altfragen-Mitschrift ist eine einmalige Wiederwahl zulässig. Zu den Aufgaben gehören Ernennung und Angelobung der Bundesregierung, Beurkundung der Bundesgesetze, Oberbefehl über das Bundesheer, Vertretung nach außen und Auflösung des Nationalrats. Regierungschef*in ist nicht die Bundespräsidentin, sondern die Bundeskanzlerin; die Bundesregierung besteht aus Bundeskanzler*in, Vizekanzler*in und Bundesminister*innen. "
      "Die Bundesversammlung besteht aus den Mitgliedern von Nationalrat und Bundesrat. Sie ist zuständig für die Angelobung der Bundespräsidentin, die Entscheidung über eine Volksabstimmung zu ihrer Absetzung, die Zustimmung zu ihrer behördlichen Verfolgung, die Anklage vor dem VfGH und die Kriegserklärung. "
      "Abgeordnete genießen berufliche und außerberufliche Immunität: Für Abstimmungen und Äußerungen im Beruf dürfen sie nicht verfolgt werden, wegen anderer strafbarer Handlungen nur mit Zustimmung des Nationalrats verhaftet werden.",
      [("rv", 50), ("rv", 47), ("rv", 42), ("rv", 59), ("fa", 11), ("fa", 16), ("fa", 18)])
    T("r-neutral", "rp", "Neutralität und Staatszielbestimmungen",
      "Staatszielbestimmungen sind eher programmatisch gestaltet. Die Folien nennen das Verbot des Nationalsozialismus, die immerwährende Neutralität, ein atomfreies Österreich, umfassenden Umweltschutz und Landesverteidigung, die Gleichstellung von Frauen und Männern sowie von Menschen mit und ohne Behinderungen und das gesamtwirtschaftliche Gleichgewicht. "
      "Die Neutralität steht im Bundesverfassungsgesetz über die Neutralität Österreichs von 1955. Sie „gewährt“ also nicht die Volksanwaltschaft: Diese ist ein Kontrollorgan, das Missstände der Verwaltung prüft. Sie besteht aus 3 Volksanwält*innen, die der Nationalrat auf 6 Jahre wählt, gibt Empfehlungen ab, berichtet jährlich und kontrolliert seit 2012 auch präventiv Einrichtungen mit Freiheitsentzug.",
      [("rv", 77), ("rv", 35), ("rv", 70), ("fa", 7)])
    T("r-exbew", "rx", "Exekutionsantrag und Bewilligung",
      "Wer einen Exekutionstitel hat, etwa einen rechtskräftigen Zahlungsbefehl, stellt als betreibende*r Gläubiger*in einen Exekutionsantrag beim Bezirksgericht als Exekutionsgericht. Die Gegenseite heißt Verpflichtete*r. "
      "Für Forderungen bis 50.000 Euro gibt es ein vereinfachtes Bewilligungsverfahren, eine Ausfertigung des Titels ist nicht nötig. Ergreift die Verpflichtete einen Rechtsbehelf, ist auf Antrag eine Aufschiebung möglich; beantragt die betreibende Partei sie, ist erst nach 3 Monaten eine weitere Exekutionshandlung möglich. "
      "Die Arten sind Drittschuldner*innenexekution (meist Lohnpfändung), Fahrnisexekution (Pfändung beweglicher Sachen durch Gerichtsvollzieher*innen) und Immobiliarexekution (Zwangspfandrecht, Zwangsverwaltung, Zwangsversteigerung). Wie viel bleiben muss, regelt die Existenzminimum-Verordnung.",
      [("r2", 36), ("r2", 37), ("fa", 6), ("fa", 13), ("fz", 5)])
    T("r-schuldreg", "rx", "Schuldenregulierungsverfahren im Überblick",
      "Nach der Eröffnung des Schuldenregulierungsverfahrens werden zuerst vorhandene Vermögenswerte erhoben und verwertet: Grundbuchs- und KFZ-Abfrage, Inventarisierung durch Gerichtsvollzieher*innen, Lebensversicherungen. Exekutionen und Zinsenlauf stoppen, das pfändbare Einkommen kommt in die Insolvenzmasse. "
      "Dann gibt es drei Wege. Beim Sanierungsplan bietet die Schuldnerin mindestens 20 Prozent innerhalb von 2 Jahren an (für Privatpersonen bis zu 5 Jahre); er spielt bei Privatpersonen kaum eine Rolle und lohnt sich vor allem, wenn Vermögen erhalten bleiben soll. "
      "Beim Zahlungsplan muss die Quote der Einkommenslage der folgenden drei Jahre entsprechen, die Laufzeit höchstens 7 Jahre; beide Pläne brauchen Kopf- und Summenmehrheit der anwesenden Gläubiger*innen. "
      "Das Abschöpfungsverfahren leitet das Gericht auch gegen den Willen der Gläubiger*innen ein: Die pfändbaren Bezüge gehen 5 Jahre an eine Treuhänderin, danach folgt die Restschuldbefreiung. Danach gelten Sperrfristen: ein neuer Zahlungsplan erst nach 10 Jahren, eine neue Abschöpfung erst nach 20 Jahren, außer die frühere Abschöpfung ist nur an der alten 10%-Quote gescheitert.",
      [("r2", 49), ("r2", 50), ("r2", 51), ("fa", 4), ("fa", 5)])
    T("r-insneu", "rx", "Was sich bei der Privatinsolvenz geändert hat",
      "Früher brauchte ein Abschöpfungsverfahren eine Mindestquote von 10 %. Menschen ohne pfändbares Einkommen, etwa mit Mindestsicherung, kamen daher kaum zur Entschuldung, weil auch Zahlungspläne oft scheiterten. Laut Altfragen-Mitschrift ist seit 2018 der direkte Weg in die Abschöpfung auch mit einer Null-Quote möglich, außer bei Unredlichkeit. "
      "Später wurde wegen Covid eine dreijährige Variante, das Abschöpfungsverfahren mit Tilgungsplan, eingeführt. Laut Skript gilt sie nur für Anträge bis 16.7.2026; für Anträge ab 17.7.2026 dauert die Entschuldung wieder 5 Jahre. Gegen die Ungleichbehandlung mit Unternehmer*innen gibt es verfassungsrechtliche Bedenken. "
      "Wer früher nur an der 10%-Quote gescheitert ist, kann nach der neuen Rechtslage erneut ein Abschöpfungsverfahren beantragen; die 20-jährige Sperre gilt dann nicht.",
      [("r2", 50), ("r2", 51), ("fa", 8), ("fz", 4)])
    T("r-anw2", "rl", "Anwartschaft nach Alter",
      "Wer erstmals Arbeitslosengeld beantragt, braucht 52 Wochen arbeitslosenversicherungspflichtige Beschäftigung in den letzten 24 Monaten (Rahmenfrist). Unter 25 Jahren reichen 26 Wochen in den letzten 12 Monaten, bei weiterer Inanspruchnahme 28 Wochen in den letzten 12 Monaten („kleine Anwartschaft“). "
      "Eine Beschäftigung unter der Geringfügigkeitsgrenze ist nicht arbeitslosenversichert und zählt für die Anwartschaft nicht. "
      "Die Bezugsdauer hängt von der Versicherungsdauer und vom Alter ab, nicht von der Höhe des Lohns: Grundanspruch 20 Wochen, mit längerer Beschäftigung 30 Wochen, ab 40 Jahren bis 39, ab 50 bis 52 Wochen; Kurse verlängern den Bezug.",
      [("r3", 11), ("r3", 12), ("r3", 14), ("fa", 7), ("fa", 11)])
    T("r-eufrei", "re", "Grundfreiheiten und Rechtsakte der EU",
      "Die Einheitliche Europäische Akte (1986) brachte das Binnenmarktkonzept: einen Raum ohne Binnengrenzen mit Grundfreiheiten. Laut Altfragen sind das der freie Waren-, Personen-, Dienstleistungs- und Kapitalverkehr. "
      "EU-Verordnungen gelten in allen Mitgliedstaaten unmittelbar und gehen nationalem Recht vor; Richtlinien müssen innerhalb einer Frist in nationales Recht umgesetzt werden. Der EuGH sichert die einheitliche Auslegung des EU-Rechts, der EGMR ist dagegen ein Gericht des Europarats und wacht über die EMRK.",
      [("rv", 78), ("fa", 12), ("fa", 18), ("fa", 19)])

    # ---------------- offene Altfragen ----------------
    OPEN(52, GROUP, "Topf 1: Beschreibe den Instanzenzug im Strafrecht.", "Zwei Instanzen: BG, Berufung ans LG; oder LG, Berufung ans OLG bzw. Nichtigkeitsbeschwerde an den OGH. Am LG Einzelrichter*in, Schöff*innen oder Geschworene.",
         [("Das Strafverfahren ist nur in 2 Instanzen angelegt.", [("f3", 6)]),
          ("Bezirksgericht urteilt, Berufung binnen 4 Wochen an das Landesgericht, dann ist Schluss.", [("f3", 6), ("fa", 1)]),
          ("Landesgericht urteilt, dann Berufung an das Oberlandesgericht oder Nichtigkeitsbeschwerde an den OGH.", [("fa", 2)]),
          ("Das Rechtsmittel muss nach der Urteilsverkündung binnen 3 Tagen angemeldet werden, die 4-Wochen-Frist läuft ab der schriftlichen Ausfertigung.", [("f3", 6)]),
          ("Am Landesgericht je nach Strafdrohung Einzelrichter*in, Schöff*innensenat oder Geschworenengericht.", [("fa", 1)]),
          ("Schöff*innen und Geschworene sind Ausdruck des demokratischen Prinzips in der Gerichtsbarkeit.", [("rv", 73), ("fa", 1)])], "ri")
    OPEN(53, GROUP, "Topf 1: Beschreibe den Instanzenzug im Zivilrecht.", "Drei Instanzen: BG, LG, OGH oder LG, OLG, OGH; Berufung, Revision, Rekurs.",
         [("Das Zivilverfahren hat grundsätzlich 3 Instanzen.", [("r2", 29)]),
          ("Bezirksgericht, Berufung an das Landesgericht, Revision an den OGH.", [("r2", 30)]),
          ("Landesgericht, Berufung an das Oberlandesgericht, Revision an den OGH.", [("r2", 30)]),
          ("Berufung gegen Urteile erster Instanz in der Regel binnen vier Wochen, Rekurs gegen Beschlüsse.", [("r2", 29)]),
          ("Zum OGH nur bei einer erheblichen Rechtsfrage und über gewissen Wertgrenzen.", [("r2", 29), ("r2", 30)]),
          ("Daneben gibt es das Außerstreitverfahren, etwa für Obsorge und Unterhalt, mit Beschluss und Rekurs.", [("r2", 23), ("fa", 13), ("fa", 14)])], "ri")
    OPEN(54, GROUP, "Topf 2: Welche Möglichkeiten bietet das Schuldenregulierungsverfahren bei der Privatinsolvenz?", "Vermögensverwertung, dann Sanierungsplan, Zahlungsplan oder Abschöpfungsverfahren mit Restschuldbefreiung.",
         [("Einzige echte Voraussetzung ist die Zahlungsunfähigkeit; Antrag beim Bezirksgericht mit Vermögensverzeichnis und Gläubiger*innenliste.", [("r2", 48), ("fa", 4)]),
          ("Erster Schritt: Vermögensverwertung, Exekutionen und Zinsen stoppen, pfändbares Einkommen kommt in die Masse.", [("r2", 49)]),
          ("Sanierungsplan: mindestens 20 Prozent in 2 Jahren, braucht Gläubiger*innenmehrheit; bei Privatpersonen selten.", [("r2", 50)]),
          ("Zahlungsplan: Quote nach dem Einkommen der nächsten drei Jahre, höchstens 7 Jahre, Kopf- und Summenmehrheit.", [("r2", 50)]),
          ("Abschöpfungsverfahren: pfändbare Bezüge gehen an eine Treuhänderin, auch gegen den Willen der Gläubiger*innen, dann Restschuldbefreiung.", [("r2", 50), ("r2", 51)]),
          ("Obliegenheiten wie Erwerb suchen und Wohnungswechsel melden; Einleitungshindernisse wie betrügerische Krida.", [("r2", 51), ("r2", 52)])], "rx")
    OPEN(55, GROUP, "Topf 2: Paolo hat einen rechtskräftigen Zahlungsbefehl über 12.000 Euro gegen Jenny, sie zahlt nicht. Was kann er tun? Was hätte Jenny tun können?", "Exekutionsantrag, vereinfachtes Bewilligungsverfahren; Lohn-, Fahrnis- oder Immobiliarexekution. Jenny: Einspruch binnen 4 Wochen.",
         [("Der rechtskräftige Zahlungsbefehl ist ein Exekutionstitel; Paolo stellt einen Exekutionsantrag beim Bezirksgericht.", [("r2", 32), ("r2", 36)]),
          ("Unter 50.000 Euro gibt es das vereinfachte Bewilligungsverfahren ohne Ausfertigung des Titels.", [("r2", 36)]),
          ("Drittschuldner*innenexekution: Lohnpfändung beim Arbeitgeber über dem Existenzminimum.", [("r2", 38), ("fa", 6)]),
          ("Fahrnisexekution: Gerichtsvollzieher*in pfändet bewegliche Sachen, unpfändbar bleibt das Nötigste.", [("r2", 37)]),
          ("Immobiliarexekution: Zwangspfandrecht, Zwangsverwaltung oder Zwangsversteigerung.", [("fa", 6)]),
          ("Jenny hätte binnen 4 Wochen Einspruch erheben können, dann folgt ein ordentliches Verfahren.", [("r2", 32), ("fa", 6)])], "rx")
    OPEN(56, GROUP, "Topf 3: Marike (26) war im letzten Jahr 10 Monate für 800 Euro angestellt, Mariko (18) 10 Monate für 420 Euro. Haben sie Anspruch auf Arbeitslosengeld?", "Marike braucht 52 Wochen in 24 Monaten (Folgeantrag 28 in 12); Mariko war unter der Geringfügigkeitsgrenze nicht versichert.",
         [("Erstantrag über 25: 52 Wochen versicherungspflichtige Beschäftigung in den letzten 24 Monaten.", [("r3", 11)]),
          ("Bei weiterer Inanspruchnahme reichen 28 Wochen in den letzten 12 Monaten.", [("r3", 12)]),
          ("Unter 25 reichen 26 Wochen in den letzten 12 Monaten.", [("r3", 12)]),
          ("Wer nur geringfügig verdient, ist nicht arbeitslosenversichert: Mariko hat keinen Anspruch.", [("r3", 11), ("fa", 7)]),
          ("Es hängt zudem von Arbeitsfähigkeit, Arbeitswilligkeit und Verfügbarkeit ab.", [("r3", 8)])], "rl")
    OPEN(57, GROUP, "Topf 3: Was ist falsch an „Österreich ist neutral, das gewährt die Volksanwaltschaft“ und „Der Bundespräsident ist der Regierungschef Österreichs“?", "Neutralität ist eine Staatszielbestimmung im Verfassungsrang; Volksanwaltschaft kontrolliert die Verwaltung. Regierungschef*in ist die Bundeskanzlerin.",
         [("Die Neutralität ist eine Staatszielbestimmung, geregelt im Bundesverfassungsgesetz über die Neutralität von 1955.", [("rv", 35), ("rv", 77)]),
          ("Die Volksanwaltschaft prüft Missstände der Verwaltung und gibt Empfehlungen, sie gewährt keine Staatsziele.", [("rv", 70)]),
          ("Regierungschef*in ist der*die Bundeskanzler*in; die Bundesregierung besteht aus BK, Vizekanzler*in und Minister*innen.", [("rv", 59)]),
          ("Die Bundespräsidentin wird auf 6 Jahre gewählt, ernennt die Regierung, beurkundet Gesetze und hat den Oberbefehl über das Bundesheer.", [("rv", 50)]),
          ("Sie wird vor der Bundesversammlung angelobt.", [("rv", 47)])], "rp")
    OPEN(58, GROUP, "Topf 3: „Wenn ich die Obsorge nicht behalte, gehe ich bis zum VfGH. Die Jugendämter sollen ins Gesetz schreiben, dass Kinder zuerst eine Mutter brauchen.“ Stimmt das?", "Nein: Obsorge ist Zivilrecht im Außerstreitverfahren, Ende beim OGH; Jugendämter machen keine Gesetze; die Regel verstieße gegen den Gleichheitsgrundsatz.",
         [("Obsorge ist eine zivilrechtliche Angelegenheit im Außerstreitverfahren am Bezirksgericht; letzte Instanz ist der OGH, nicht der VfGH.", [("r2", 23), ("r2", 30), ("fa", 8)]),
          ("Jugendämter sind Verwaltung und keine gesetzgebenden Organe.", [("fa", 8)]),
          ("Gesetze beschließt der Nationalrat.", [("rv", 42)]),
          ("Eine Regel „Kinder brauchen zuerst die Mutter“ verstieße gegen den Gleichheitsgrundsatz.", [("rv", 76), ("fa", 8)]),
          ("Maßstab ist das Kindeswohl nach § 138 ABGB.", [("fz", 2)])], "ri")
    OPEN(59, GROUP, "Topf 3: Beschreibe in Stichworten, was sich bei der Privatinsolvenz in den letzten Jahren verändert hat.", "Früher 10%-Quote; dann Abschöpfung ohne Mindestquote; Tilgungsplan in 3 Jahren nur für Anträge bis 16.7.2026, seither wieder 5 Jahre.",
         [("Früher scheiterte die Abschöpfung oft an der Mindestquote von 10 %, Menschen ohne pfändbares Einkommen kamen kaum zur Entschuldung.", [("r2", 51), ("fa", 8)]),
          ("Seit 2018 laut Mitschrift Abschöpfung auch ohne Mindestquote, außer bei Unredlichkeit.", [("fa", 8)]),
          ("Wegen Covid kam die dreijährige Variante mit Tilgungsplan dazu.", [("fa", 8)]),
          ("Für Anträge ab 17.7.2026 gibt es nur noch die fünfjährige Abschöpfung.", [("r2", 50)]),
          ("Wer nur an der früheren 10%-Quote gescheitert ist, darf erneut eine Abschöpfung beantragen.", [("r2", 51), ("fz", 4)])], "rx")

    # ---------------- Karten zu den offenen Altfragen ----------------
    MC(None, "r-instanz", [52], "In wie vielen Instanzen ist das gerichtliche Strafverfahren angelegt?", "In 2 Instanzen", ["In 3 Instanzen", "In 4 Instanzen", "Nur in einer Instanz"],
       "Das Strafverfahren ist laut Fernlehre 3 nur in 2 Instanzen angelegt, anders als der Zivilprozess mit grundsätzlich 3 Instanzen.", [("f3", 6), ("r2", 29)])
    MC(ALT, "r-instanz", [52], "Das Bezirksgericht verurteilt A. wegen Diebstahls. Wohin geht die Berufung?", "An das Landesgericht, danach ist Schluss",
       ["An das Oberlandesgericht", "An den OGH", "An den VfGH"], "Berufung binnen 4 Wochen an das Landesgericht, einzubringen beim Bezirksgericht. Damit ist der Instanzenzug im Strafrecht erschöpft.", [("f3", 6)])
    MC(ALT, "r-instanz", [52], "Mit welchem Rechtsmittel kommt man im Strafrecht vom Landesgericht zum OGH?", "Nichtigkeitsbeschwerde",
       ["Revision", "Rekurs", "Einspruch"], "Laut Altfragen-Mitschrift: Landesgericht, Berufung an das OLG oder Nichtigkeitsbeschwerde an den OGH. Revision und Rekurs sind Rechtsmittel im Zivilverfahren.", [("fa", 2), ("fa", 16)])
    TF(None, "r-instanz", [52], "Im Strafprozess muss man das Rechtsmittel nach der Urteilsverkündung binnen 3 Tagen anmelden.", True,
       "Stimmt. Die 4-Wochen-Frist für die Ausführung beginnt erst mit der schriftlichen Urteilsausfertigung. Meldet niemand ein Rechtsmittel an, reicht eine gekürzte Urteilsausfertigung.", [("f3", 6)])
    MU(None, "r-instanz", [52], "Wer kann am Landesgericht in Strafsachen entscheiden?", ["Einzelrichter*in", "Schöff*innensenat", "Geschworenengericht"], ["Rechtspfleger*in", "Volksanwaltschaft"],
       "Je nach Schwere des Delikts: Einzelrichter*in bei leichteren Fällen, Schöff*innensenat bei schwereren, Geschworenengericht bei den schwersten und bei politischen Delikten. Schöff*innen und Geschworene sind Laien.", [("fa", 1), ("rv", 73)])
    TF(None, "r-instanz", [52], "Die Mitwirkung von Schöff*innen und Geschworenen gehört zu den Grundsätzen der Gerichtsbarkeit.", True,
       "Stimmt, die Folien nennen sie neben Mündlichkeit, Öffentlichkeit, Anklageprozess, fairem Verfahren und Unschuldsvermutung. Die Altfragen-Mitschrift sieht darin das demokratische Prinzip.", [("rv", 73), ("fa", 1)])
    ORD("r-instanz", [53], "Zivilverfahren: Bring den Instanzenzug ab dem Bezirksgericht in die richtige Reihenfolge.", ["Bezirksgericht: Urteil", "Berufung an das Landesgericht", "Revision an den OGH"],
        "Ab dem Bezirksgericht geht es über das Landesgericht zum OGH. Beginnt das Verfahren am Landesgericht, ist die zweite Instanz das Oberlandesgericht.", [("r2", 30)])
    ORD("r-instanz", [53], "Zivilverfahren: Bring den Instanzenzug ab dem Landesgericht in die richtige Reihenfolge.", ["Landesgericht: Urteil", "Berufung an das Oberlandesgericht", "Revision an den OGH"],
        "Österreich hat 4 OLG-Sprengel: Wien, Graz, Linz und Innsbruck. Der OGH entscheidet nur über erhebliche Rechtsfragen.", [("r2", 30)])
    MA(ALT, "r-instanz", [53], "Welches Rechtsmittel gehört wohin?", [["Gegen Urteile 1. Instanz im Zivilprozess", "Berufung"], ["Gegen Urteile 2. Instanz im Zivilprozess", "Revision"], ["Gegen Beschlüsse", "Rekurs"], ["Gegen Bescheide", "Beschwerde"]],
       "So steht es im Skript zu den Rechtsmitteln im Zivilprozess. In der Verwaltung heißt das Rechtsmittel gegen Bescheide Beschwerde und geht an das Verwaltungsgericht.", [("r2", 29), ("r2", 16)])
    TF(None, "r-instanz", [53], "Jede zivilrechtliche Streitigkeit kann bis zum OGH gebracht werden.", False,
       "Falsch. Eine Revision an den OGH ist nur zulässig, wenn gewisse Wertgrenzen überschritten sind und eine erhebliche Rechtsfrage vorliegt, etwa weil das Berufungsgericht von der OGH-Rechtsprechung abweicht.", [("r2", 29), ("r2", 30)])
    MC(None, "r-ausserstreit", [53, 58], "Was unterscheidet das Außerstreitverfahren vom Zivilprozess?", "Es ist rechtsfürsorglich und kann auch von Amts wegen eingeleitet werden",
       ["Es wird nur auf Klage eingeleitet", "Es ist formstrenger und teurer", "Es läuft vor Verwaltungsbehörden"], "Der Zivilprozess wird nur auf Klage eingeleitet und ist formstrenger mit höherem Kostenrisiko. Das Außerstreitverfahren läuft auch vor den Zivilgerichten, aber auf Antrag oder von Amts wegen.", [("r2", 23)])
    MU(ALT, "r-ausserstreit", [58], "Was wird laut Altfragen-Mitschrift im Außerstreitverfahren entschieden?", ["Obsorge", "Unterhalt", "Verlassenschaft", "Einvernehmliche Scheidung"], ["Schadenersatzklage", "Mahnklage"],
       "Das Außerstreitverfahren ist für privatrechtliche Angelegenheiten ohne klassischen Streit gedacht. Entschieden wird mit Beschluss, das Rechtsmittel ist der Rekurs.", [("fa", 13), ("fa", 14)])
    MC(None, "r-ausserstreit", [58], "Bis zu welcher Instanz kann ein Obsorgestreit gehen?", "Bis zum OGH",
       ["Bis zum VfGH", "Bis zum VwGH", "Nur bis zum Landesgericht"], "Obsorge ist Zivilrecht und läuft am Bezirksgericht im Außerstreitverfahren. Höchste Instanz ist der OGH. Den VfGH erreicht man nur, wenn ein Gesetz selbst verfassungswidrig wäre.", [("fa", 8), ("r2", 30)])
    TF(None, "r-ausserstreit", [58], "Das Jugendamt könnte ins Gesetz schreiben, dass Kinder in erster Linie die Mutter brauchen.", False,
       "Falsch. Jugendämter sind Verwaltung und machen keine Gesetze, das tut der Nationalrat. Und auch er könnte das nicht so regeln, weil es gegen den Gleichheitsgrundsatz verstieße.", [("fa", 8), ("rv", 76)])
    MU(None, "r-gerichtspers", [], "Welche Gerichtspersonen nennt das Skript?", ["Berufsrichter*innen", "Laienrichter*innen", "Rechtspfleger*innen"], ["Volksanwält*innen", "Exekutionsanwält*innen"],
       "Berufsrichter*innen sind unabhängig, unversetzbar und grundsätzlich unabsetzbar. Laienrichter*innen wirken nach Art 91 B-VG mit, Rechtspfleger*innen erledigen bestimmte Agenden selbständig.", [("r2", 24)])
    MC(ALT, "r-gerichtspers", [], "Wer berechnet am Gericht zum Beispiel den Kindesunterhalt oder trägt ins Grundbuch ein?", "Rechtspfleger*innen",
       ["Laienrichter*innen", "Schöff*innen", "Notar*innen"], "Rechtspfleger*innen sind besonders geschulte Beamt*innen des gehobenen Dienstes. Sie erledigen Kindesunterhalt, Grundbuch, Firmenbuch und Exekution selbständig.", [("r2", 24)])
    TF(ALT, "r-gerichtspers", [], "Berufsrichter*innen sind weisungsgebunden und jederzeit absetzbar.", False,
       "Falsch. Sie sind unabhängig, unversetzbar und grundsätzlich unabsetzbar. Auch in der zweiten Fragestunde war diese Aussage eine falsche Antwortmöglichkeit.", [("r2", 24), ("fz", 2)])

    MC(None, "r-schuldreg", [54], "Was passiert nach Eröffnung des Schuldenregulierungsverfahrens als Erstes?", "Vorhandenes Vermögen wird erhoben und verwertet",
       ["Die Restschuldbefreiung", "Die Abstimmung über den Zahlungsplan", "Die Abschöpfung beginnt sofort"], "Grundbuchs- und KFZ-Abfrage, Inventarisierung durch Gerichtsvollzieher*innen, Lebensversicherungen. Erst nach abgeschlossener Verwertung kann über einen Zahlungsplan abgestimmt werden.", [("r2", 49), ("r2", 50)])
    MC(None, "r-schuldreg", [54], "Was muss ein Sanierungsplan mindestens anbieten?", "20 Prozent innerhalb von 2 Jahren",
       ["10 Prozent in 7 Jahren", "Die Einkommenslage der nächsten drei Jahre", "Nichts, das Gericht entscheidet allein"], "Für Privatpersonen kann die Frist um bis zu 5 Jahre ausgedehnt werden. Sanierungspläne spielen bei natürlichen Personen kaum eine Rolle, ihr Vorteil: vorhandenes Vermögen bleibt erhalten.", [("r2", 50)])
    BU(ALT, "r-schuldreg", [54], "Sanierungsplan, Zahlungsplan oder Abschöpfungsverfahren?", ["Sanierungsplan", "Zahlungsplan", "Abschöpfungsverfahren"],
       [("Mindestens 20 Prozent in 2 Jahren", 0), ("Vermögen bleibt erhalten", 0), ("Quote nach dem Einkommen der nächsten drei Jahre", 1), ("Laufzeit höchstens 7 Jahre", 1), ("Auch gegen den Willen der Gläubiger*innen", 2), ("Pfändbare Bezüge an eine Treuhänderin", 2)],
       "Sanierungs- und Zahlungsplan brauchen die Kopf- und Summenmehrheit der anwesenden Gläubiger*innen. Das Abschöpfungsverfahren leitet das Gericht bei Vorliegen der Voraussetzungen auch gegen ihren Willen ein.", [("r2", 50), ("r2", 51)])
    TF(None, "r-schuldreg", [54], "Für den Zahlungsplan braucht es die Kopf- und Summenmehrheit der anwesenden Gläubiger*innen.", True,
       "Stimmt, das gilt für Sanierungs- und Zahlungsplan. Beim Abschöpfungsverfahren braucht es keine Zustimmung, das Gericht leitet es bei Vorliegen der Voraussetzungen ein.", [("r2", 50), ("r2", 51)])
    MC(None, "r-schuldreg", [54, 59], "Wann ist nach einem Abschöpfungsverfahren eine neue Abschöpfung zulässig?", "Erst 20 Jahre nach Eröffnung des letzten Verfahrens",
       ["Sofort", "Nach 5 Jahren", "Nie wieder"], "Ein neuer Zahlungsplan ist erst nach 10 Jahren, eine neue Abschöpfung erst nach 20 Jahren zulässig. Ausnahme: Die frühere Abschöpfung ist nur an der alten 10%-Quote gescheitert.", [("r2", 51)])
    MU(None, "r-schuldreg", [54], "Was ist ein Einleitungshindernis für das Abschöpfungsverfahren?", ["Verurteilung wegen betrügerischer Krida", "Vermögensverschleuderung kurz vor der Zahlungsunfähigkeit", "Verletzung der Auskunfts- und Mitwirkungspflichten"], ["Bezug von Mindestsicherung", "Schulden aus Online-Käufen an sich"],
       "§ 201 IO zählt diese Fälle auf, dazu unverhältnismäßig neue Schulden in den letzten 3 Jahren und fehlende Erwerbsbemühungen. Wenig Einkommen ist kein Hindernis.", [("r2", 51), ("r2", 52)])
    TF(None, "r-schuldreg", [54], "Mit der Restschuldbefreiung erlöschen auch Forderungen aus vorsätzlich begangenen strafbaren Handlungen.", False,
       "Falsch. Solche Forderungen sind von der Schuldbefreiung ausgenommen. Auch Rechte gegen Bürg*innen und Mitschuldner*innen bleiben unberührt.", [("r2", 51), ("r2", 49)])
    TF(None, "r-insneu", [59], "Wer früher nur an der Mindestquote von 10 % gescheitert ist, kann heute erneut eine Abschöpfung beantragen.", True,
       "Stimmt. Die 20-jährige Sperre entfällt dann. In der zweiten Fragestunde: Wer etwa 2017 mangels Einkommen gescheitert ist, kann es nach der Gesetzesänderung nochmal versuchen.", [("r2", 51), ("fz", 4)])
    MC(None, "r-insneu", [59], "Wem half der Wegfall der Mindestquote vor allem?", "Menschen ohne pfändbares Einkommen, etwa mit Mindestsicherung",
       ["Unternehmer*innen mit großem Vermögen", "Banken als Gläubigerinnen", "Bürg*innen"], "Ohne exekutierbares Einkommen war früher keine Abschöpfung möglich, und Zahlungspläne scheiterten oft. Laut Altfragen-Mitschrift geht seither auch eine Null-Quote, außer bei Unredlichkeit.", [("fa", 8)])
    ORD("r-insneu", [59], "Privatinsolvenz: Bring die Entwicklung in die richtige Reihenfolge.", ["Abschöpfung nur mit Mindestquote von 10 %", "Abschöpfung auch ohne Mindestquote", "Dreijährige Variante mit Tilgungsplan", "Für Anträge ab 17.7.2026 wieder nur fünf Jahre"],
        "Die Altfragen-Mitschrift datiert den Wegfall der Quote auf 2018 und die dreijährige Variante auf die Covid-Zeit. Das Skript bestätigt: ab 17.7.2026 nur noch fünf Jahre.", [("fa", 8), ("r2", 50), ("r2", 51)])

    MC(None, "r-exbew", [55], "Paolo hat einen rechtskräftigen Zahlungsbefehl. Was ist das rechtlich?", "Ein Exekutionstitel",
       ["Nur eine Mahnung", "Ein Bescheid", "Eine Klage"], "Ohne Einspruch wird der Zahlungsbefehl rechtskräftig und vollstreckbar. Mit diesem Titel kann Paolo einen Exekutionsantrag beim Bezirksgericht stellen.", [("r2", 32), ("r2", 36)])
    MC(ALT, "r-exbew", [55], "Bis zu welcher Forderung gibt es das vereinfachte Bewilligungsverfahren?", "Bis 50.000 Euro",
       ["Bis 5.000 Euro", "Bis 15.000 Euro", "Bis 75.000 Euro"], "Für Forderungen bis 50.000 Euro ist keine Ausfertigung des Exekutionstitels nötig. Exekutionsgerichte sind die Bezirksgerichte.", [("r2", 36)])
    MA(ALT, "r-exbew", [55], "Welche Exekutionsart passt?", [["Lohn wird beim Arbeitgeber gepfändet", "Drittschuldner*innenexekution"], ["Gerichtsvollzieher*in pfändet den Fernseher", "Fahrnisexekution"], ["Wohnung wird zwangsversteigert", "Immobiliarexekution"]],
       "Diese drei Arten nannte die Lehrende auch in der zweiten Fragestunde. „Hauptexekution“, „Zweckexekution“ und „Verfolgungsexekution“ waren dort falsche Antwortmöglichkeiten, solche Arten gibt es nicht.", [("fa", 6), ("fz", 5)])
    MU(X, "r-exbew", [], "Welche Exekutionsarten gibt es?", ["Drittschuldner*innenexekution", "Fahrnisexekution", "Immobiliarexekution"], ["Hauptexekution", "Zweckexekution", "Verfolgungsexekution"],
       "So eine Frage kam in der zweiten Fragestunde: Die falschen Begriffe klingen plausibel, existieren aber nicht. Für falsche Kreuze gibt es Minuspunkte.", [("fz", 5), ("fa", 13)])
    TF(None, "r-exbew", [55], "Ergreift die Verpflichtete einen Rechtsbehelf, kann die Exekution auf Antrag aufgeschoben werden.", True,
       "Stimmt. Beantragt die betreibende Partei die Aufschiebung, ist erst nach 3 Monaten eine weitere Exekutionshandlung möglich.", [("r2", 37)])
    MC(None, "r-exbew", [55], "Was hätte Jenny gegen den Zahlungsbefehl tun können?", "Binnen 4 Wochen Einspruch erheben",
       ["Binnen 14 Tagen Rekurs erheben", "Beschwerde an das Verwaltungsgericht", "Nichts, der Zahlungsbefehl ist sofort endgültig"], "Mit dem Einspruch wird aus dem Mahnverfahren ein ordentliches Verfahren. Im Zweifel lohnt sich der Einspruch, weil das Gericht die Forderung vorher nicht inhaltlich prüft.", [("r2", 32), ("fa", 6)])
    MU(X, "r-exbew", [55], "Was ist laut Skript unpfändbar?", ["Bett und Kleiderkasten", "Kühlschrank und Waschmaschine", "Einfache Kleidung und Brillen", "Für den Beruf notwendige Gegenstände"], ["Schmuck allgemein", "Zweitwagen"],
       "Diese Gegenstände ermöglichen das Weiterleben. Schmuck kann gepfändet werden, ein Ehering als höchstpersönlicher Gegenstand laut MATS-Skriptum aber nicht.", [("r2", 37), ("msk", 118)])
    TF(X, "r-exbew", [], "Ein Ehering kann bei der Fahrnisexekution gepfändet werden.", False,
       "Falsch. Höchstpersönliche Gegenstände wie der Ehering sind unpfändbar, ebenso Haustiere, zu denen eine gefühlsmäßige Verbindung besteht. Anderer Schmuck kann gepfändet werden.", [("msk", 118), ("fz", 5)])
    TF(X, "r-exbew", [], "Ein Laptop ist in jedem Fall unpfändbar.", False,
       "Falsch. Laut zweiter Fragestunde kommt es auf die Umstände an, etwa ob er für Beruf oder Ausbildung nötig ist. Unpfändbar sind für die Berufsausübung notwendige Gegenstände und Lernbehelfe.", [("fz", 5), ("msk", 118)])

    MC(None, "r-anw2", [56], "Welche Anwartschaft braucht eine 26-Jährige beim ersten Antrag auf Arbeitslosengeld?", "52 Wochen in den letzten 24 Monaten",
       ["26 Wochen in den letzten 12 Monaten", "28 Wochen in den letzten 12 Monaten", "12 Wochen im letzten Jahr"], "Das ist die Regel für die erstmalige Inanspruchnahme. Unter 25 reichen 26 Wochen in 12 Monaten, bei weiterer Inanspruchnahme 28 Wochen in 12 Monaten.", [("r3", 11), ("r3", 12)])
    MA(AL, "r-anw2", [56], "Welche Anwartschaft gilt?", [["Erstantrag ab 25", "52 Wochen in 24 Monaten"], ["Antrag vor dem 25. Geburtstag", "26 Wochen in 12 Monaten"], ["Weitere Inanspruchnahme", "28 Wochen in 12 Monaten"]],
       "Gezählt werden nur arbeitslosenversicherungspflichtige Beschäftigungen. Die „kleine Anwartschaft“ für die weitere Inanspruchnahme erleichtert den neuen Bezug.", [("r3", 11), ("r3", 12)])
    TF(None, "r-anw2", [56], "Mariko hat 10 Monate unter der Geringfügigkeitsgrenze gearbeitet und erfüllt damit die Anwartschaft.", False,
       "Falsch. Geringfügige Beschäftigung ist nicht arbeitslosenversichert und zählt nicht. Mariko hat daher keinen Anspruch auf Arbeitslosengeld.", [("r3", 11), ("fa", 7)])
    MC(AL, "r-anw2", [], "Wovon hängt die Höchstdauer des Arbeitslosengelds NICHT ab?", "Von der Höhe des letzten Lohns",
       ["Von der Dauer der versicherungspflichtigen Beschäftigung", "Vom Alter", "Von der Teilnahme an einer Kursmaßnahme"], "Grundanspruch 20 Wochen, je nach Versicherungsdauer 30 Wochen, ab 40 Jahren 39, ab 50 Jahren 52 Wochen. Kurse verlängern den Bezug. Der Lohn bestimmt nur die Höhe, nicht die Dauer.", [("r3", 14), ("fa", 11)])

    MC(None, "r-neutral", [57], "Wo ist die Neutralität Österreichs geregelt?", "Im Bundesverfassungsgesetz über die Neutralität, als Staatszielbestimmung",
       ["In einem Bescheid der Volksanwaltschaft", "Im ABGB", "In einer EU-Verordnung"], "Die Folien führen das Neutralitäts-BVG von 1955 unter den zentralen Verfassungsquellen und die immerwährende Neutralität unter den Staatszielbestimmungen.", [("rv", 35), ("rv", 77)])
    MU(ALT, "r-neutral", [57], "Welche Staatszielbestimmungen nennen die Folien?", ["Immerwährende Neutralität", "Atomfreies Österreich", "Umfassender Umweltschutz", "Gleichstellung von Menschen mit und ohne Behinderungen"], ["Recht auf Arbeit", "Mindestlohn"],
       "Staatszielbestimmungen sind eher programmatisch. Dazu gehören auch Verbot des Nationalsozialismus, Landesverteidigung, Gleichstellung der Geschlechter und gesamtwirtschaftliches Gleichgewicht.", [("rv", 77)])
    MC(None, "r-neutral", [57], "Was macht die Volksanwaltschaft?", "Sie prüft Missstände der Verwaltung und gibt Empfehlungen",
       ["Sie gewährt die Neutralität", "Sie erlässt Gesetze", "Sie entscheidet über Bescheidbeschwerden"], "3 Volksanwält*innen, vom Nationalrat auf 6 Jahre gewählt, eine Wiederwahl. Sie berichtet jährlich an Nationalrat und Landtag und kontrolliert seit 2012 präventiv die Menschenrechte, etwa nach dem HeimAufG.", [("rv", 70)])
    MC(ALT, "r-bv", [57], "Wer ist Regierungschef*in in Österreich?", "Der*die Bundeskanzler*in",
       ["Der*die Bundespräsident*in", "Der*die Nationalratspräsident*in", "Der*die Vizekanzler*in"], "Die Bundesregierung besteht aus Bundeskanzler*in, Vizekanzler*in und Bundesminister*innen. Die Bundespräsidentin ernennt und gelobt sie an, ist aber nicht Teil der Regierung.", [("rv", 59), ("rv", 50)])
    MC(ALT, "r-bv", [57], "Für wie lange wird die Bundespräsidentin gewählt?", "Auf 6 Jahre, laut Mitschrift einmal wiederwählbar",
       ["Auf 5 Jahre", "Auf 4 Jahre", "Auf 12 Jahre"], "Die Folie nennt die unmittelbare Wahl auf 6 Jahre, die Altfragen-Mitschrift ergänzt die einmalige Wiederwahl. 5 Jahre dauert die Legislaturperiode des Nationalrats.", [("rv", 50), ("fa", 11), ("rv", 42)])
    MU(None, "r-bv", [57], "Was gehört zu den Aufgaben der Bundespräsidentin?", ["Ernennung und Angelobung der Bundesregierung", "Beurkundung des verfassungsmäßigen Zustandekommens der Bundesgesetze", "Oberbefehl über das Bundesheer", "Auflösung des Nationalrats"], ["Leitung der Regierungssitzungen", "Beschluss von Bundesgesetzen"],
       "Dazu kommen Vertretung der Republik nach außen und Abschluss von Staatsverträgen. Gesetze beschließt der Nationalrat, die Regierung leitet der Bundeskanzler.", [("rv", 50)])
    MU(S, "r-bv", [], "Wofür ist die Bundesversammlung zuständig?", ["Angelobung der Bundespräsidentin", "Zustimmung zu ihrer behördlichen Verfolgung", "Anklage vor dem VfGH", "Kriegserklärung"], ["Wahl der Bundesregierung", "Beschluss des Budgets"],
       "Die Bundesversammlung besteht aus den Mitgliedern von Nationalrat und Bundesrat. Sie entscheidet auch über die Durchführung einer Volksabstimmung zur Absetzung der Bundespräsidentin.", [("rv", 47)])
    MC(S, "r-bv", [], "Was bedeutet die außerberufliche Immunität von Abgeordneten?", "Wegen einer strafbaren Handlung dürfen sie nur mit Zustimmung des Nationalrats verhaftet werden",
       ["Sie dürfen nie bestraft werden", "Sie müssen keine Steuern zahlen", "Sie sind an keine Gesetze gebunden"], "Berufliche Immunität schützt Abstimmungen und Äußerungen im Beruf. Außerberuflich braucht es die Zustimmung des Nationalrats, außer bei Ergreifung auf frischer Tat bei einem Verbrechen.", [("rv", 42), ("fa", 18), ("fa", 19)])
    MU(S, "r-bv", [], "Woraus besteht die Bundesregierung?", ["Bundeskanzler*in", "Vizekanzler*in", "Bundesminister*innen"], ["Bundespräsident*in", "Landeshauptleute"],
       "Sie wird von der Bundespräsidentin angelobt und besorgt die obersten Verwaltungsgeschäfte. Politisch kann der Nationalrat ihr das Misstrauen aussprechen.", [("rv", 59)])
    TF(None, "r-bv", [17], "Für die Abschaffung eines Grundprinzips der Verfassung braucht es eine Volksabstimmung.", True,
       "Stimmt, das ist eine Gesamtänderung. Vorher muss der Nationalrat mit Verfassungsmehrheit beschließen: Präsenzquorum mindestens 1/2 und Konsensquorum 2/3.", [("rv", 44), ("fa", 8)])

    MU(S, "r-eufrei", [], "Welche Grundfreiheiten des EU-Binnenmarkts nennt die Altfragen-Mitschrift?", ["Freier Warenverkehr", "Freier Personenverkehr", "Freier Dienstleistungsverkehr", "Freier Kapitalverkehr"], ["Freie Wahl des Gerichts", "Freier Zugang zu Sozialhilfe"],
       "Die Folien erwähnen die Grundfreiheiten beim Binnenmarktkonzept der Einheitlichen Europäischen Akte von 1986. Aufgezählt sind die vier in der Mitschrift vom Vorjahr.", [("fa", 12), ("rv", 78)])
    MC(None, "r-eufrei", [], "Wie wirken EU-Richtlinien?", "Sie müssen innerhalb einer Frist in nationales Recht umgesetzt werden",
       ["Sie gelten sofort unmittelbar", "Sie sind bloße Empfehlungen", "Sie gelten nur für EU-Organe"], "Verordnungen gelten dagegen unmittelbar in allen Mitgliedstaaten und gehen nationalem Recht vor (Anwendungsvorrang).", [("fa", 19)])

    # ---------------- weitere Altfragen (MC-Teil) ----------------
    MC(ALT, "r-anw2", [], "Wann kann man im ersten Antrag unter 25 Jahren Arbeitslosengeld bekommen?", "Mit 26 Wochen versicherungspflichtiger Beschäftigung in den letzten 12 Monaten",
       ["Mit 52 Wochen in 12 Monaten", "Ohne Anwartschaft", "Mit 4 Wochen Beschäftigung"], "Für junge Menschen gilt eine erleichterte Anwartschaft. Ab 25 braucht es beim ersten Antrag 52 Wochen in 24 Monaten.", [("r3", 12)])
    TF(ALT, "r-nh", [], "Ein Folgeantrag auf Notstandshilfe ist nur zweimal möglich.", False,
       "Falsch, Folgeanträge sind unbegrenzt möglich. Das bestätigten Altfragen-Mitschrift und zweite Fragestunde.", [("fa", 10), ("fz", 3)])
    TF(ALT, "r-alvweg", [], "Lehnt das AMS eine Kursbeihilfe ab, erhebt man Beschwerde an das Arbeits- und Sozialgericht.", False,
       "Falsch. Gegen AMS-Bescheide geht die Beschwerde an das Bundesverwaltungsgericht, nicht an ein Gericht der ordentlichen Gerichtsbarkeit. Auf Beihilfen besteht zudem kein Rechtsanspruch.", [("r3", 24), ("fa", 11), ("r3", 22)])
    MC(ALT, "r-nh", [], "Was kann man nach dem Arbeitslosengeld beantragen?", "Notstandshilfe",
       ["Hilfe in besonderen Lebenslagen beim AMS", "Pensionsvorschuss automatisch", "Nochmals Arbeitslosengeld ohne Anwartschaft"], "Die Notstandshilfe folgt auf das Arbeitslosengeld, wenn es ausgeschöpft ist. HibL ist eine Leistung der Mindestsicherung ohne Rechtsanspruch, nicht des AMS.", [("fa", 10), ("r3", 16)])
    MU(ALT, "r-fern", [], "Wann können Verbraucher*innen nach dem KSchG zurücktreten?", ["Bei Haustürgeschäften", "Bei Erklärung außerhalb der ständigen Geschäftsräume", "Bei Überrumpelung, etwa auf Werbefahrten"], ["Bei jedem Kauf im Geschäft", "Wenn ihnen die Farbe nicht gefällt"],
       "§ 3 KSchG erfasst Haustürgeschäfte und typische Überrumpelung. Für Fernabsatz wie Online-Bestellungen gilt das FAGG. Der Rücktritt muss schriftlich erfolgen, die Frist beträgt meist zwei Wochen.", [("r2", 55), ("r2", 56), ("fa", 12)])
    MC(ALT, "r-gewaehr", [], "Wie lange gilt die gesetzliche Gewährleistungsfrist für bewegliche Sachen?", "2 Jahre",
       ["6 Monate", "3 Jahre", "30 Jahre"], "Für bewegliche Sachen wie Bücher, Auto oder Handy 2 Jahre, für unbewegliche wie ein Haus 3 Jahre. Gewährleistung betrifft Mängel, die schon bei der Übergabe vorhanden waren.", [("r2", 58), ("fa", 11)])
    MC(ALT, "r-ins", [], "Wo stellt man den Antrag auf Privatinsolvenz?", "Beim örtlich zuständigen Bezirksgericht",
       ["Beim Landesgericht", "Bei der Schuldenberatung", "Beim AMS"], "Zuständig ist das Bezirksgericht, in dessen Sprengel die Schuldnerin wohnt. Die Schuldenberatung hilft bei der Vorbereitung.", [("r2", 48), ("fa", 13)])
    MU(Z, "r-zust", [], "Wofür ist die RSa-Zustellung laut Skript noch vorgesehen?", ["Urteile in Strafsachen", "Ladungen der Verwaltungsgerichte", "Einberufungsbefehle des Bundesheeres", "Aufforderung zum Geschworenendienst"], ["Zahlungsbefehle", "Reisepässe"],
       "Zahlungsbefehle, Klagen und Reisepässe gehen seit 2009 mit RSb. RSa, der blaue Brief, darf nur eigenhändig zugestellt werden.", [("r2", 41), ("r2", 42)])
    TF(Z, "r-zust", [], "Einen RSa-Brief darf auch jemand mit Postvollmacht übernehmen.", True,
       "Stimmt. Ersatzzustellung an Mitbewohner*innen ist bei RSa nicht zulässig, Ausnahmen gelten aber für Postbevollmächtigte und Rechtsanwält*innen. Einen zweiten Zustellversuch gibt es nicht.", [("r2", 42), ("fz", 4)])
    MU(None, "r-avg", [], "Welche Rechte haben Parteien im Verwaltungsverfahren?", ["Akteneinsicht", "Parteiengehör", "Zustellung des Bescheids", "Rechtsmittel"], ["Anwaltspflicht", "Geschworene"],
       "Die Altfragen nennen dazu Wiederaufnahme und Geltendmachung der Entscheidungspflicht. Im Verwaltungsverfahren gibt es keinen Anwaltszwang.", [("fa", 19), ("r2", 14)])
    MU(None, "r-bescheid", [], "Was muss ein Bescheid enthalten?", ["Ausdrückliche Bezeichnung als Bescheid", "Spruch", "Begründung", "Rechtsmittelbelehrung"], ["Unterschrift einer Richterin", "Zustimmung der Partei"],
       "Dazu kommen die Behörde, Unterschrift und Datum. Der Bescheid ist ein individueller, hoheitlicher, normativer Verwaltungsakt.", [("r2", 14), ("fa", 19)])

    # ---------------- zweite Prüfungsfragestunde ----------------
    BU(S, "r-materiell", [], "Materielles oder formelles Recht?", ["Materielles Recht", "Formelles Recht"],
       [("Eltern schulden ihren Kindern Unterhalt", 0), ("Im Ortsgebiet höchstens 50 km/h", 0), ("Was Kindeswohl bedeutet", 0), ("Welches Gericht für die Unterhaltsklage zuständig ist", 1), ("Wie ein Strafbescheid zugestellt wird", 1), ("Frist für ein Rechtsmittel", 1)],
       "Merksatz der Lehrenden: Inhalt, Rechte und Pflichten sind materielles Recht; Verfahren, Zuständigkeit, Fristen und Durchsetzung formelles Recht.", [("fz", 1), ("fz", 2)])
    MC(S, "r-materiell", [], "Die Frage, was das Kindeswohl inhaltlich bedeutet, betrifft …", "materielles Recht, geregelt in § 138 ABGB",
       ["formelles Recht in der ZPO", "formelles Recht in der StPO", "Verwaltungsstrafrecht"], "Was gilt, ist materielles Recht. Das Kindeswohl steht in § 138 ABGB, nicht in ZPO oder StPO, die Verfahren regeln.", [("fz", 2)])
    MC(S, "r-auslegung", [], "Welche Auslegungsmethode fragt nach dem objektiven Sinn und Zweck einer Bestimmung?", "Die teleologische Interpretation",
       ["Die dynamisch-interpretative Auslegung", "Die historische Interpretation", "Die Wortinterpretation"], "Die „dynamische interpretative Auslegung“ war in der Fragestunde eine falsche Antwort. Die historische Interpretation stützt sich auf Gesetzesmaterialien, die Wortinterpretation auf den Sprachgebrauch.", [("rv", 21), ("fz", 2)])
    MU(S, "r-auslegung", [], "Welche Auslegungsarten stehen auf den Folien?", ["Wortinterpretation", "Systematische Interpretation", "Historische Interpretation", "Teleologische Interpretation"], ["Dynamisch-interpretative Auslegung", "Emotionale Auslegung"],
       "Dazu kommen die logisch-grammatikalische, die verfassungskonforme und die gemeinschaftsrechtskonforme Interpretation. Auswendig lernen muss man sie laut Lehrender nicht, aber wiedererkennen.", [("rv", 21), ("fz", 2)])
    TF(S, "r-mandat", [], "Abgeordnete zum Nationalrat haben eine sanktionierte Anwesenheitspflicht.", False,
       "Falsch. Sie sollen grundsätzlich anwesend sein, Sanktionen bei bloßer Abwesenheit gibt es laut Fragestunde aber nicht. Auch die Altfragen beantworten das mit Nein.", [("fz", 2), ("fa", 11)])
    TF(S, "r-mandat", [], "An einer Regierungsbildung müssen mindestens drei Parteien beteiligt sein.", False,
       "Falsch, das verneinte die Lehrende in der zweiten Fragestunde ausdrücklich.", [("fz", 2)])
    TF(S, "r-gerecht", [], "Eine Rechtsnorm, die als ungerecht empfunden wird, ist automatisch ungültig.", False,
       "Falsch. Recht hat unter anderem eine Gerechtigkeits-, Friedens-, Sicherheits- und Ordnungsfunktion, daraus folgt aber nicht, dass jede Norm von allen als gerecht empfunden werden muss.", [("fz", 2)])
    MC(S, "r-stufen", [], "Was ist der Unterschied zwischen Verfassungsrecht und Verfassungsgerichtshof?", "Verfassungsrecht ist eine Normebene, der VfGH ein Gericht",
       ["Es gibt keinen", "Der VfGH steht im Stufenbau über der Verfassung", "Verfassungsrecht ist eine Behörde"], "Bei Fragen nach dem Stufenbau aufpassen: Gefragt ist nach Normen, nicht nach Organen. Der VfGH prüft Gesetze und Verordnungen am Maßstab der Verfassung.", [("fz", 2), ("rv", 69)])
    TF(M, "r-wmg", [], "Asylwerbende haben während des laufenden Asylverfahrens Anspruch auf Wiener Mindestsicherung.", False,
       "Falsch. Laut Fragestunde und Skript haben sie bis zum Abschluss des Verfahrens keinen Anspruch. Der Lebensmittelpunkt muss in Österreich liegen.", [("fz", 3)])
    MU(M, "r-wmg", [], "Was ist bei ausschließlichem Bezug von Mindestsicherung jedenfalls relevant?", ["Krankenversicherung", "Mobilpass"], ["Automatische Wohnbeihilfe", "Essen auf Rädern automatisch"],
       "Laut zweiter Fragestunde sind Krankenversicherung und Mobilpass jedenfalls dabei. Nicht jede Person bekommt automatisch Wohnbeihilfe, bei der WMS spricht man heute von Mietbeihilfe.", [("fz", 3)])
    TF(M, "r-wmg", [], "„Personen mit mehr als drei Kindern“ sind eine eigene Anspruchsgruppe der WMS.", False,
       "Falsch, das ist keine Anspruchsgruppe. Anspruchsberechtigt sind etwa Österreicher*innen und Gleichgestellte, und zwar unter weiteren Voraussetzungen.", [("fz", 3)])
    TF(M, "r-wmg", [], "Laut zweiter Fragestunde können nach einer VfGH-Entscheidung 2026 auch bestimmte Menschen mit befristetem Aufenthaltstitel Anspruch haben.", True,
       "Stimmt. Beispiel der Lehrenden: Rot-Weiß-Rot-Karte plus, schon verlängert, seit mehr als fünf Jahren dauerhaft niedergelassen. Die Lehrende will die Änderung noch in die Unterlagen aufnehmen.", [("fz", 3)])
    TF(AL, "r-nh", [], "Man muss „im Plus“ sein, um Mindestsicherung oder Arbeitslosengeld zu bekommen.", False,
       "Falsch, das verneinte die Lehrende in der zweiten Fragestunde. Schulden schließen die Leistungen nicht aus.", [("fz", 3)])
    TF(AL, "r-alvweg", [], "Gegen eine PVA-Entscheidung bringt man Klage ein, und das Gericht ist an die Beurteilung der PVA nicht gebunden.", True,
       "Stimmt. Laut Fragestunde beginnt das eigentliche Verfahren vor dem Arbeits- und Sozialgericht neu. Beschwerde gegen einen Bescheid und Klage sind unterschiedliche Rechtsinstrumente.", [("fz", 4), ("r3", 24)])
    TF(X, "r-ins", [], "Ehegatt*innen mit gemeinsamen Schulden können ein gemeinsames Insolvenzverfahren führen.", False,
       "Falsch. Jede Person muss ein eigenes Verfahren beantragen. Das stand im Skript mit zwei Rufzeichen und kam in beiden Fragestunden.", [("r2", 49), ("fz", 4)])
    TF(X, "r-ins", [], "Bei Menschen ohne pfändbares Einkommen kann es sinnvoll sein, mit dem Insolvenzantrag zuzuwarten.", True,
       "Laut zweiter Fragestunde ja, weil sie ohnehin keine Gläubiger*innen bevorzugen können. Das ist eine Überlegung zur Vorbereitung, keine starre Frist; Schuldenberatung ist wichtig.", [("fz", 4)])
    TF(V, "r-vertrag", [], "Ein Verein ist automatisch Unternehmer im Sinn des KSchG.", False,
       "Falsch als allgemeine Regel. Unternehmen ist jede auf Dauer angelegte Organisation selbständiger wirtschaftlicher Tätigkeit, auch ohne Gewinnabsicht. Ein Verein kann das sein, ist es aber nicht automatisch.", [("fz", 5), ("fz", 6), ("fa", 9)])
    MC(V, "r-ausfall", [], "Zwei Personen haften gemeinsam für eine Schuld. Was darf die Gläubigerin?", "Beide in Anspruch nehmen und auswählen, von wem sie die Zahlung verlangt",
       ["Nur die Hauptschuldnerin klagen", "Nur jeder*m die Hälfte abverlangen", "Erst nach Versteigerung fordern"], "Wer bezahlt hat, muss sich intern bei der anderen Person den Ausgleich holen. Anders bei der Ausfallsbürgschaft: Dort haftet die Bürgin erst, wenn bei der Hauptschuldnerin nichts mehr zu holen ist.", [("fz", 6)])
    TF(V, "r-ausfall", [], "Bei der Ausfallsbürgschaft können sich Gläubiger*innen aussuchen, ob sie Hauptschuldner*in oder Ausfallsbürg*in verfolgen.", False,
       "Falsch, das gilt bei der gewöhnlichen Bürgschaft. Ausfallsbürg*innen werden erst exekutiert, wenn alles bei der Hauptschuldnerin ausgeschöpft ist, etwa die Wohnung versteigert wurde.", [("fa", 10), ("fz", 6)])
    MC(AL, "r-kbgbeginn", [], "Was droht beim Kinderbetreuungsgeld, wenn die vorgeschriebene Hebammenberatung nicht nachgewiesen wird?", "Eine Kürzung der Leistung",
       ["Nichts", "Eine Verwaltungsstrafe", "Der Verlust der Familienbeihilfe"], "Laut zweiter Fragestunde droht bei fehlender Hebammenberatung eine Kürzung, bei nicht nachgewiesenen Eltern-Kind-Pass-Untersuchungen eine weitergehende Kürzung. Der Antrag geht an den Krankenversicherungsträger.", [("fz", 6), ("fa", 3)])

    # ---------------- Stolperfallen ----------------
    TRAP("Neutralität: 1955 oder 1959?", "Die Altfragen-Mitschrift schreibt, die Neutralität sei im BVG vom 26.10.1959 festgelegt. Die Folien nennen das Bundesverfassungsgesetz über die Neutralität Österreichs von 1955. Es gilt 1955.", [("fa", 7), ("rv", 35)])
    TRAP("Obsorge: Berufung oder Rekurs?", "Die Altfragen-Mitschrift beschreibt den Obsorge-Instanzenzug mit „Berufung“. Obsorge läuft aber im Außerstreitverfahren, dort wird mit Beschluss entschieden und das Rechtsmittel heißt Rekurs (Fernlehre 3: Beschluss, 2 Wochen Rekurs). Richtig bleibt: Ende beim OGH, nicht beim VfGH.", [("fa", 8), ("f3", 7), ("r2", 29)])
    TRAP("KBG-Antrag bei der Gebietskrankenkasse?", "Die Altfragen-Mitschrift nennt die Gebietskrankenkasse. Die gibt es seit der Reform 2020 nicht mehr: Zuständig ist der Krankenversicherungsträger, also meist die ÖGK.", [("fa", 10), ("s8", 8), ("fz", 6)])
    TRAP("Pensionsbezieher*innen ohne WMS-Anspruch?", "Die zweite Fragestunde gibt sinngemäß wieder, Pensionsbezieher*innen könnten keinen Anspruch haben. Laut Fernlehre 9 und Altfragen geht die Ausgleichszulage vor, man kann nicht wählen; liegt die Pension mit Ausgleichszulage über dem Mindeststandard, gibt es keine laufende WMS. Ein allgemeiner Ausschluss steht nicht im Skript.", [("fz", 3), ("fa", 10)])
    TRAP("„Kein Rechtsanspruch auf Familienbeihilfe“?", "So steht es in der Zusammenfassung der zweiten Fragestunde. In den Unterlagen ist die Familienbeihilfe eine Familienleistung, die bei der WMS anrechenfrei bleibt; kein Rechtsanspruch besteht laut Skript etwa bei HibL und AMS-Beihilfen. Vermutlich ein Hör- oder Transkriptionsfehler; im Zweifel nachfragen.", [("fz", 3), ("r3", 22)])
    TRAP("Geschworenengericht: wie besetzt?", "Die Altfragen-Mitschrift nennt 8 Geschworene und 3 Richter*innen sowie Strafgrenzen von 5 Jahren für Schöff*innen und Geschworene. Skript und Folien nennen diese Details nicht; sie sind nur Mitschrift.", [("fa", 1), ("rv", 73)])
    TRAP("Freies Mandat und Klubzwang", "Die Altfragen-Mitschrift sagt „kein Klubzwang“. Die zweite Fragestunde präzisiert: Ein informeller Klubzwang kann bestehen, rechtlich bindend ist er nicht.", [("fa", 11), ("fz", 2)])
    TRAP("Seit 2018 Abschöpfung ohne Quote?", "Die Jahreszahl 2018 und die Covid-Interimsregelung stammen aus der Altfragen-Mitschrift. Das Skript bestätigt nur die frühere 10%-Quote und den Wegfall der dreijährigen Variante für Anträge ab 17.7.2026.", [("fa", 8), ("r2", 50), ("r2", 51)])
    TERM("Materielles Recht", "Regelt den Inhalt: welche Rechte und Pflichten bestehen.", [("fz", 1)])
    TERM("Formelles Recht", "Regelt die Durchsetzung: Zuständigkeit, Fristen, Verfahren.", [("fz", 1)])
    TERM("Außerstreitverfahren", "Rechtsfürsorgliches Zivilverfahren nach dem AußStrG, auch von Amts wegen; Entscheidung mit Beschluss, Rechtsmittel Rekurs.", [("r2", 23), ("fa", 13)])
    TERM("Rechtspfleger*in", "Geschulte Beamt*in, erledigt selbständig etwa Unterhaltsberechnung, Grundbuch, Exekution.", [("r2", 24)])


# Prüfungsmodus: Aufbau laut zweiter Prüfungsfragestunde.
EXAM_INFO = ("Aufbau laut zweiter Prüfungsfragestunde: 30 Minuten, 23 Fragen, davon 3 offene mit zusammen 44 Punkten. Die geschlossenen Fragen kommen aus den Themenblöcken "
             "EU und Verfassung, Fallbeispiele mit Wahr/Falsch-Aussagen, Kinderbetreuungsgeld, Arbeitslosenversicherung, Zustellung, Privatinsolvenz, Gewährleistung und Garantie, Exekution, Wiener Mindestsicherung und Konsumentenschutz. "
             "Die offenen Fragen kommen laut Altfragen aus drei Töpfen; hier je eine pro Topf. Man kann zwischen den Fragen springen und Fragen markieren. "
             "Gewertet wird wie angekündigt mit Plus- und Minuspunkten: Bei Mehrfachauswahl zieht jedes falsche Kreuz so viel ab, wie ein richtiges bringt (zwei richtige und ein falsches Kreuz geben 50 %), eine Frage geht nicht unter null. "
             "Wie viele Punkte die geschlossenen Fragen bringen, wurde nicht gesagt; die App rechnet mit 100 Punkten insgesamt, also 56 für die 20 geschlossenen Fragen. Das ist eine Annahme.")
EXAM_BLOCKS = [  # (Name, Kapitel oder Themen); "tf" = nur Wahr/Falsch-Fallbeispiele
    ("EU, Verfassung und Rechtsstaat", ["rn", "rs", "rp", "rg", "re", "ri"]),
    ("Fallbeispiele: Wahr oder falsch?", "tf"),
    ("Kinderbetreuungsgeld", ["rkb"]),
    ("Arbeitslosenversicherung", ["rl"]),
    ("Zustellung", ["r-zust", "r-maengel", "r-frist"]),
    ("Privatinsolvenz", ["r-ins", "r-buerge", "r-ausfall", "r-anfecht", "r-abschoepf", "r-schuldreg", "r-insneu"]),
    ("Gewährleistung und Garantie", ["r-gewaehr", "r-gutschein", "r-form"]),
    ("Exekution", ["r-exe", "r-exmin", "r-exbew"]),
    ("Wiener Mindestsicherung", ["r9"]),
    ("Konsumentenschutz", ["r-vertrag", "r-agb", "r-6kschg", "r-25kschg", "r-fern", "r-schadenersatz"]),
]


def exam_meta(c):
    chs = {t["id"]: t["ch"] for t in c.topics}
    blocks = []
    for name, sel in EXAM_BLOCKS:
        if sel == "tf":
            blocks.append(dict(name=name, tf=True, topics=[]))
        else:
            blocks.append(dict(name=name, topics=sorted(t for t, ch in chs.items() if t in sel or ch in sel)))
    return dict(minutes=30, n=23, open=3, openPts=44, total=100, info=EXAM_INFO, blocks=blocks, topf=EXAM_TOPF)
