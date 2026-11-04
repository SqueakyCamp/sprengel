from dsl import Course
c = Course("recht", name="Rechtliche Bezüge zur materiellen Sicherung", short="Recht", term="WS 2026/27", lecturer="Verena Musil",
           exams=[], accent="#3B3F8F", lineTitle="Der Instanzenzug", stopWord="Station",
           openName="Fernlehre-Frage", openNamePl="Fernlehre-Fragen", openLead="Die Themen der Fernlehren sind das Wichtigste. Hier sind ihre Fragen: Erst selbst antworten, dann mit der Antwort aus der Fernlehre vergleichen. Offene Rechercheaufgaben sind auf das Kernwissen gekürzt.",
           ranks=[[0,"Rechtsunterworfen"],[100,"Partei"],[300,"Beschwerde eingebracht"],[650,"Landesverwaltungsgericht"],[1100,"VwGH"],[1700,"VfGH"],[2500,"EGMR"]],
           modes=["chains","blitz"], source="Fernlehre-Antworten 2 bis 7, Folien Verfassungs- und Verwaltungsrecht und Skript Teil 2 und 3. Vier Fernlehren fehlen noch.",
           upcoming="Noch 4 Fernlehre-Aufgaben folgen und werden hier ergänzt.")
CH,T,MC,TF,ORD,MATCH,MULTI,BUCKET,CHAIN,CALC,OPEN,TERM,TRAP = c.CH,c.T,c.MC,c.TF,c.ORD,c.MATCH,c.MULTI,c.BUCKET,c.CHAIN,c.CALC,c.OPEN,c.TERM,c.TRAP

CH("rn","Recht und Normen","Fernlehre 3 C","Recht, Moral, Gerechtigkeit",["rv"])
CH("rs","Stufenbau","Fernlehre 2","Was steht über wem?",["f2"])
CH("rp","Verfassungsprinzipien","Fernlehre 4 und 5","Sechs Baugesetze, Bund und Länder",["f4"])
CH("rg","Grundrechte","Fernlehre 2 D, 5 D","Gelten gegenüber dem Staat",["f5"])
CH("ri","Wer entscheidet?","Fernlehre 3 D","Gericht oder Behörde, Frist, Instanz",["f3"])
CH("rw","Verwaltungsverfahren","Fernlehre 7 A","Partei, Bescheid, Beschwerde",["f7"])
CH("rz","Zivilverfahren und Mahnklage","Fernlehre 7 B","Zahlungsbefehl, Einspruch, Kosten",["f7"])
CH("rf","Zustellung und Fristen","Fernlehre 7 B","RSa, RSb, Hinterlegung, Fristenlauf",["r2"])
CH("rx","Exekution und Insolvenz","Skript Teil 2","Titel, Pfändung, Abschöpfung",["r2"])
CH("re","EU und Europa","Fernlehre 6","Nur was auf den Folien steht",["f6"])
CH("rl","Sozialhilfe und Arbeitslosenversicherung","Skript Teil 2 und 3","Art 12, Versicherung, Versorgung, Fürsorge",["r3"])
CH("rk","Fernlehren 8 bis 11","folgt noch","Vier Aufgaben kommen noch",[],pending=True)

# ------------------------------------------------------------ Themen
T("r-norm","rn","Recht und andere Normen","Normen sagen, wie etwas sein soll. Rechtsnormen setzt eine staatliche Autorität, sie werden kundgemacht und können mit staatlichem Zwang durchgesetzt werden. Moral und Sitte setzt der Staat nicht, sie können aber bei der Auslegung einfließen.",[("rv",3),("rv",7),("f3",2)])
T("r-gerecht","rn","Recht und Gerechtigkeit","Recht ist nicht dasselbe wie Gerechtigkeit: Auch als ungerecht empfundenes Recht gilt. Kelsens reine Rechtslehre trennt Recht und Moral streng. Radbruch: Erreicht die Ungerechtigkeit ein unerträgliches Maß, muss das Gesetz der Gerechtigkeit weichen.",[("f3",3),("rv",10),("rv",11)])
T("r-einteil","rn","Öffentliches Recht und Privatrecht","Vier Theorien grenzen ab: Interessen-, Subordinations-, Subjekts- und Rechtswegtheorie; keine überzeugt abschließend. Die Unterscheidung entscheidet über Zuständigkeit: Privatrecht geht zu Gerichten, öffentliches Recht meist zu Behörden.",[("f3",1),("f3",2),("rv",25),("rv",26)])
T("r-formen","rn","Urteil, Beschluss, Bescheid","Gerichte entscheiden mit Urteil oder Beschluss durch unabhängige Richter*innen. Verwaltungsbehörden entscheiden mit Bescheid durch weisungsgebundene Organe.",[("f3",3),("rv",29),("rv",30)])
T("r-gesetzesstaat","rs","Gesetzesstaat statt case law","Österreich ist ein Gesetzesstaat: Nach dem Legalitätsprinzip braucht jede Entscheidung eine gesetzliche Grundlage. Die Rechtsprechung der Höchstgerichte gibt aber den Interpretationsrahmen vor, an den sich untere Behörden und Gerichte halten.",[("f2",1),("rv",53)])
T("r-stufen","rs","Stufenbau der Rechtsordnung","Von oben nach unten: Baugesetze, Verfassung, einfache Gesetze, Verordnungen, dann Urteile, Bescheide und Verträge, zuletzt die Exekution. Untere Stufen dürfen oberen nicht widersprechen.",[("rv",27),("f2",5),("f2",6)])
T("r-eurecht","rs","EU-Recht im Stufenbau","Die Grundprinzipien der Verfassung stehen über dem EU-Recht, sonst hat EU-Recht Vorrang. EU-Richtlinien müssen die Staaten umsetzen, EU-Verordnungen gelten unmittelbar.",[("f2",3),("rv",28),("f3",3)])
T("r-recherche","rs","RIS und Jusline","Das RIS ist die amtliche Quelle, hat aber keine Fehlertoleranz: gut, wenn man schon weiß, was man sucht. Für das erste Suchen eignet sich Jusline besser. Im RIS stehen unter Judikatur auch Entscheidungen.",[("f2",2),("rv",16)])
T("r-prinz","rp","Sechs Baugesetze","Demokratisch, republikanisch, bundesstaatlich, rechtsstaatlich, gewaltenteilend, liberal. Sie abzuschaffen oder auszuhöhlen braucht eine Volksabstimmung.",[("rv",36),("rv",37),("f2",3),("f4",5)])
T("r-bp","rp","Was die Bundespräsidentin tut","Sie beurkundet das verfassungsmäßige Zustandekommen eines Gesetzes. Das ist eine formale Prüfung, keine inhaltliche. Sie gewährt nicht die Demokratie.",[("f4",1),("rv",50)])
T("r-direkt","rp","Direkte Demokratie","Volksabstimmung, Volksbefragung und Volksbegehren. Volksbefragungen binden rechtlich nicht, auch erfolgreiche Volksbegehren müssen nicht umgesetzt werden. Bindend ist die Volksabstimmung.",[("f4",2),("f4",5),("rv",40)])
T("r-bund","rp","Bund und Länder","Art 10: Gesetzgebung und Vollziehung beim Bund. Art 11: Gesetz Bund, Vollziehung Land. Art 12: Grundsatzgesetz Bund, Ausführung und Vollziehung Land. Art 15: Auffangtatbestand, alles Übrige ist Landessache. Die Gerichtsbarkeit ist nur Bundessache.",[("rv",51),("rv",52),("f4",3)])
T("r-gesetz","rp","Wie ein Bundesgesetz entsteht","Initiative, Ausschuss und drei Lesungen im Nationalrat, Bundesrat, Beurkundung, Gegenzeichnung, Kundmachung im Bundesgesetzblatt. Einfache Gesetze brauchen 1/3 Anwesenheit und einfache Mehrheit, Verfassungsgesetze 1/2 Anwesenheit und 2/3 Mehrheit.",[("f4",4),("rv",43),("rv",44),("rv",45)])
T("r-rechtsstaat","rp","Rechtsstaat und Gewaltenteilung","Der Rechtsstaat soll Willkür verhindern: Legalitätsprinzip, bestimmte Gesetze, gesetzliche*r Richter*in, rechtliches Gehör, Rechtsmittel. Gesetzgebung und Vollziehung sind getrennt, ebenso Gerichtsbarkeit und Verwaltung in allen Instanzen.",[("f5",1),("f5",2),("rv",54),("rv",55)])
T("r-kontrolle","rp","Volksanwaltschaft und Rechnungshof","Die drei Volksanwält*innen prüfen Missstände der Verwaltung, jede*r kann sich beschweren. Der Rechnungshof kontrolliert die Finanzen nach Richtigkeit, Sparsamkeit, Wirtschaftlichkeit und Zweckmäßigkeit.",[("rv",70),("rv",71),("f5",2)])
T("r-grund","rg","Wer Grundrechte schuldet","Nur der Staat hat Grundrechte zu gewährleisten, auch wenn er privatrechtlich handelt (Fiskalgeltung). Private halten sich an Gesetze, die den Grundrechten entsprechen müssen.",[("f5",3),("f2",7)])
T("r-grenzen","rg","Grenzen der Grundrechte","Fast alle Grundrechte stehen unter Eingriffs- oder Gesetzesvorbehalt. Sie enden dort, wo die Grundrechte anderer beginnen. Eingriffe müssen verhältnismäßig sein.",[("f5",3),("f5",4),("rv",75)])
T("r-rechtsweg","ri","Der Weg durch die Instanzen","Sozialhilfe: Behörde, Landesverwaltungsgericht, dann VwGH oder VfGH, zuletzt der EGMR. Zivilsachen: Bezirksgericht oder Landesgericht mit Urteil, Berufung, Revision. Das Strafverfahren am Bezirksgericht hat zwei Instanzen.",[("f3",4),("f3",6),("f3",7)])
T("r-schnell","ri","Schnellverfahren im Verwaltungsstrafrecht","Organmandat bis in der Regel 90 Euro, Anonymverfügung bis 365 Euro, jeweils ohne Rechtsmittel; zahlt man nicht, folgt ein Verfahren. Strafverfügung bis 600 Euro, dagegen gibt es Einspruch.",[("f3",5)])
T("r-avg","rw","Das Verwaltungsverfahren","Es führt zu einem Bescheid, auf Antrag oder von Amts wegen. Die Behörde forscht selbst nach dem Sachverhalt (materielle Wahrheit) und würdigt Beweise frei. Parteien haben Akteneinsicht, Parteiengehör, Zustellung, Rechtsmittel und können die Entscheidungspflicht geltend machen.",[("r2",8),("r2",10),("r2",14),("rv",66)])
T("r-bescheid","rw","Der Bescheid","Bezeichnung als Bescheid, Behörde, Spruch, Begründung, Rechtsmittelbelehrung, Unterschrift und Datum. Nach der Rechtsmittelfrist ist er verbindlich und vollstreckbar.",[("r2",14),("r2",15),("rv",64)])
T("r-beschwerde","rw","Rechtsmittel und Säumnis","Beschwerde binnen 4 Wochen an das Verwaltungsgericht, bei der Behörde einzubringen, in der Regel mit aufschiebender Wirkung und ohne Anwaltszwang. Entscheidet die Behörde nicht rechtzeitig, gibt es die Säumnisbeschwerde. Berufung mit 2 Wochen gibt es nur noch im eigenen Wirkungsbereich der Gemeinden.",[("r2",16),("r2",17),("r2",18),("f3",4)])
T("r-wieder","rw","Wiederaufnahme und Wiedereinsetzung","Wiedereinsetzung hilft bei einer unverschuldet versäumten Frist: Antrag binnen 2 Wochen ab Wegfall des Hindernisses und die versäumte Handlung gleich nachholen. Wiederaufnahme hilft bei neuen Tatsachen oder gefälschten Beweisen.",[("r2",18)])
T("r-vstg","rw","Verwaltungsstrafe und Gerichtsstrafe","Im Verwaltungsstrafrecht gilt das Kumulationsprinzip: jede Übertretung eine eigene Strafe. Anklage und Entscheidung sind nicht getrennt. Es gibt kein kodifiziertes Gesetz wie das StGB. Verwaltungsstrafen stehen nicht im gerichtlichen Strafregister.",[("r2",19),("r2",20),("f7",2)])
T("r-gericht","rw","Gericht und Verwaltung im Vergleich","Richter*innen sind weisungsfrei, unversetzbar und unabsetzbar, Verwaltungsorgane weisungsgebunden. Vor Gericht gelten schon in erster Instanz Mündlichkeit, Unmittelbarkeit und Öffentlichkeit, und ab gewissen Größen besteht Anwaltspflicht.",[("f7",2),("rv",29)])
T("r-zpo","rz","Streitiges Verfahren","Eingeleitet nur durch Klage. Die Klägerin trägt in der Regel die Beweislast. Bezirksgericht bis 15.000 Euro, darüber Landesgericht, Familiensachen und Besitzstörung unabhängig vom Wert am Bezirksgericht. Absolute Anwaltspflicht am Bezirksgericht über 5.000 Euro.",[("r2",24),("r2",25),("r2",28),("f7",3)])
T("r-mahn","rz","Mahnklage und Zahlungsbefehl","Reine Geldforderungen bis 75.000 Euro laufen über die Mahnklage. Das Gericht prüft die Forderung nicht inhaltlich und erlässt einen Zahlungsbefehl. Einspruch binnen 4 Wochen, auch unbegründet. Ohne Einspruch wird er rechtskräftig und exekutierbar. Im Zweifel Einspruch.",[("r2",32),("f3",7),("f7",3),("f7",4)])
T("r-kosten","rz","Kosten und Prozessrisiko","Auch mit Verfahrenshilfe trägt, wer verliert, die Kosten der Gegenseite. Ein gewonnenes Urteil nützt wenig, wenn beim Gegenüber nichts pfändbar ist. Zeug*innen können Widersprüche und Vertagungen bringen.",[("f7",3),("f7",4)])
T("r-besitz","rz","Räumung und Besitzstörung","Läuft ein Mietvertrag ab und geht der Mieter nicht freiwillig, muss der Vermieter auf Räumung klagen. Hinauswerfen oder das Schloss tauschen berechtigt den Mieter zur Besitzstörungsklage.",[("f7",1),("r2",32)])
T("r-zust","rf","Zustellung","RSa (blauer Brief) nur eigenhändig, keine Ersatzzustellung. RSb (weißer Brief) gilt für Klagen, Bescheide und Zahlungsbefehle; Ersatzzustellung an Erwachsene an derselben Abgabestelle ist möglich. Hinterlegte Sendungen gelten mit dem ersten Tag der Abholfrist als zugestellt.",[("r2",41),("r2",42),("r2",43)])
T("r-maengel","rf","Zustellmängel","Falscher Name oder Adresse, RSa an Ersatzperson, Zustellung trotz bekannter Abwesenheit machen die Zustellung unwirksam. Erreicht das Dokument den Empfänger tatsächlich, ist der Mangel geheilt.",[("r2",43),("f7",4),("f7",5)])
T("r-frist","rf","Fristen","Wochenfristen enden am gleichnamigen Tag. Fällt das Ende auf Samstag, Sonn- oder Feiertag, endet die Frist am nächsten Werktag. Bei verfahrensrechtlichen Fristen reicht die Postaufgabe am letzten Tag, bei materiellen muss die Erklärung angekommen sein.",[("r2",43),("r2",44),("f7",5)])
T("r-exe","rx","Exekution","Für eine Exekution braucht es einen Titel, etwa Urteil, gerichtlichen Vergleich oder Zahlungsbefehl. Ein Gesetz kann man nicht exekutieren lassen. Möglich sind Fahrnispfändung, Lohnpfändung und Immobiliarexekution, auch gleichzeitig. Wer zuerst kommt, hat den besseren Rang.",[("r2",34),("r2",35),("f3",3)])
T("r-exmin","rx","Existenzminimum","Unpfändbar bleibt 2026 ein Grundbetrag von 1.308 Euro, bei AMS-Bezug 1.526 Euro, dazu 261 Euro je Unterhaltspflicht und Steigerungsbeträge. Beihilfen und Mindestsicherung sind nicht pfändbar. Bei Unterhaltsexekution bleiben nur 75 % des Grundbetrags.",[("r2",38),("r2",39),("r2",40)])
T("r-ins","rx","Privatinsolvenz","Einzige echte Voraussetzung ist die Zahlungsunfähigkeit. Zinsen und Exekutionen stoppen, außer Unterhaltsexekution. Zahlungsplan: maximal 7 Jahre, Gläubigermehrheit nötig. Abschöpfung: für Anträge ab 17.7.2026 fünf Jahre, auch gegen den Willen der Gläubiger*innen.",[("r2",48),("r2",49),("r2",50),("r2",51)])
T("r-eu","re","EU-Institutionen","Kommission: EU-Interessen, Hüterin der Verträge. Rat der EU: Minister*innen, Interessen der Staaten. Parlament: Unionsbürger*innen, 720 Abgeordnete. EuGH in Luxemburg. Der Europäische Rat macht politische Zielvorgaben, keine Gesetze.",[("rv",80),("rv",81),("rv",82),("rv",83),("rv",85)])
T("r-egmr","re","EGMR ist nicht EU","Der Europäische Gerichtshof für Menschenrechte in Straßburg ist keine EU-Institution. Er wacht über die EMRK, jede Einzelperson kann dort Beschwerde einlegen.",[("rv",84),("f2",6)])
T("r-sh","rl","Sozialhilfe im Stufenbau","Armenwesen ist Art 12 B-VG: Grundsatzgesetz des Bundes, Ausführungsgesetze und Vollziehung der Länder. Darum ist die Wiener Mindestsicherung Landesrecht und die MA 40 Landesbehörde. Das Sozialhilfe-Grundsatzgesetz 2019 regelt Höchstsätze statt Mindeststandards.",[("r2",61),("r2",63),("f3",4)])
T("r-prinzipien","rl","Drei Prinzipien sozialer Sicherung","Versicherungsprinzip: Beiträge und Gegenleistung. Versorgungsprinzip: Leistung ohne Vorleistung, etwa Familienbeihilfe. Sozialhilfeprinzip: Hilfsbedürftigkeit, subsidiär, heute mit Rechtsanspruch.",[("r2",61),("r2",62),("r2",63)])
T("r-alv","rl","Arbeitslosengeld","Anspruch hat, wer der Vermittlung zur Verfügung steht, die Anwartschaft erfüllt und die Bezugsdauer nicht erschöpft hat. Zur Verfügung steht, wer arbeitsfähig, arbeitswillig und arbeitslos ist. Grundbetrag: 55 % des Nettoeinkommens.",[("r3",7),("r3",8),("r3",15)])
T("r-schutz","rl","Berufs- und Entgeltschutz","Erste 100 Tage Berufsschutz, in den ersten 120 Tagen mindestens 80 % der Bemessungsgrundlage, danach 75 %. In der Notstandshilfe gibt es beides nicht mehr.",[("r3",9),("r3",17)])
T("r-nh","rl","Notstandshilfe","Nach Erschöpfung des Arbeitslosengelds auf Antrag für bis zu 52 Wochen, Folgeanträge unbegrenzt. Partner*inneneinkommen wird seit 2018 nicht mehr angerechnet. Bezieher*innen sind kranken- und pensionsversichert.",[("r3",17),("r3",18)])

# ------------------------------------------------------------ Fernlehre-Fragen
OPEN(1,"Fernlehre 2","Norma: „Jurist*innen lernen Gesetze auswendig.“ Juri: „Österreichisches Recht ist case law.“ Wie erklärst du den Zusammenhang von Gesetz und Rechtsprechung?","Gesetzesstaat: Jede Entscheidung braucht ein Gesetz, Höchstgerichte geben den Auslegungsrahmen vor.",
 [("Österreich ist ein Gesetzesstaat: Nach dem Legalitätsprinzip muss jede Entscheidung auf einer gesetzlichen Grundlage beruhen, nicht nur auf Vorentscheidungen.",[("f2",1)]),
  ("Die Rechtsinterpretation ist trotzdem wichtig, weil manche Gesetze wenig Inhalt haben und die Rechtsprechung sehr detailliert ist, etwa im Unterhaltsrecht.",[("f2",1)]),
  ("Untere Behörden und Gerichte wie MA 40 oder Bezirksgericht halten sich an OGH, VwGH und VfGH. Richtungsänderungen kommen von den Höchstgerichten.",[("f2",1)]),
  ("Erstgerichte nach der ZPO helfen den Parteien nicht beim Tatsachennachweis. Sie würdigen Beweise frei und müssen überprüfbar festhalten, wovon sie ausgehen.",[("f2",1)])],"rs")
OPEN(2,"Fernlehre 2","RIS und Jusline: Worin liegen die Vor- und Nachteile?","RIS amtlich und exakt, Jusline besser zum ersten Suchen.",
 [("Das RIS hat keine Fehlertoleranz und taugt vor allem, wenn man schon weiß, was man sucht.",[("f2",2)]),
  ("Für ein erstes Suchen ist Jusline geeigneter.",[("f2",2)]),
  ("Im RIS finden sich unter Judikatur auch die Entscheidungen der Gerichte.",[("f2",2)])],"rs")
OPEN(3,"Fernlehre 2","Inwiefern steht Verfassungsrecht über einfachen Gesetzen? Welche Rolle spielen Verordnungen? Ist die StVO eine Verordnung?","Höherrangiges Recht hat Vorrang. Verordnungen konkretisieren Gesetze. Die StVO ist ein Bundesgesetz.",
 [("Widerspricht ein Gesetz einem Verfassungsgesetz, hat das höherrangige Verfassungsgesetz Vorrang. So steht das BVG Kinderrechte über § 138 ABGB.",[("f2",3),("f2",2)]),
  ("Die sechs Grundprinzipien sind so wichtig, dass eine Änderung oder Aushöhlung nur mittels Volksabstimmung möglich wäre.",[("f2",3)]),
  ("Innerstaatliche Verordnungen gibt es vor allem in der Verwaltung zur Konkretisierung von Gesetzen. Beispiel: WMG-Verordnung zum Wiener Mindestsicherungsgesetz.",[("f2",3),("f2",2)]),
  ("Die Straßenverkehrsordnung ist trotz ihres Namens ein Bundesgesetz.",[("f2",3)])],"rs")
OPEN(4,"Fernlehre 2","Yola will als Gemeindemitarbeiterin eine Verordnung zum Fahrradverleih erlassen. Was rätst du ihr mit dem Stufenbau?","Stufe für Stufe prüfen. Und: Verordnungen erlässt der Gemeinderat.",
 [("Höherrangiges bindet: Die Verordnung darf weder Verfassung noch Bundes- oder Landesgesetzen widersprechen.",[("f2",4),("f2",5)]),
  ("Stufe für Stufe prüfen: Verfassung und Grundrechte, Bundes- und Landesgesetze, Regelungen der Gemeinde.",[("f2",6)]),
  ("Behörden können nur im Rahmen ihres sachlichen und örtlichen Wirkungsbereichs Verordnungen erlassen. Das B-VG regelt die Gemeinden in den Artikeln 115 bis 120, Details die Gemeindeordnung.",[("f2",3),("f2",4)]),
  ("Verordnungen beschließt laut Beispiellösung der Gemeinderat. Yola könnte ihr Anliegen nur einbringen, etwa als Tagesordnungspunkt.",[("f2",4)])],"rs")
OPEN(5,"Fernlehre 2","Stanislaus: „Wurde ich beraubt, klage ich meine Grundrechte ein und der Staat ersetzt den Schaden.“ Stimmt das?","Nein. Das ist ein Delikt einer Privatperson, keine Grundrechtsverletzung.",
 [("Keine Grundrechtsverletzung: Eine Privatperson muss keine Grundrechte gewähren. Es liegt ein Schadensfall und ein Delikt vor.",[("f2",7)]),
  ("Der Staat zahlt keinen Schadenersatz. Zuständig sind Straf- und Zivilgerichtsbarkeit.",[("f2",7)]),
  ("Stanislaus muss selbst auf Schadenersatz klagen. Hat der*die Schädiger*in nichts Exekutierbares, kann er leer ausgehen.",[("f2",7)]),
  ("Das Grundrecht auf Eigentum schützt vor dem Staat, etwa vor Enteignung. Über einfache Gesetze wirkt es auch zwischen Privaten.",[("f2",7)]),
  ("Er kann sich dem Strafverfahren als Privatbeteiligte*r anschließen. Schadensgutmachung ist ein wesentlicher Milderungsgrund.",[("f2",8)])],"rg")
OPEN(6,"Fernlehre 3","Welche Theorien grenzen öffentliches Recht und Privatrecht ab, und warum ist das wichtig?","Vier Theorien; die Unterscheidung entscheidet über Zuständigkeit und Amtshaftung.",
 [("Interessentheorie: öffentliche gegen private Interessen.",[("f3",1)]),
  ("Subordinationstheorie: Über- und Unterordnung gegen Gleichordnung.",[("f3",1)]),
  ("Subjektstheorie: Am öffentlichen Recht ist immer ein Rechtsträger mit Hoheitsgewalt beteiligt.",[("f3",1)]),
  ("Rechtswegtheorie: öffentlich, wenn Verwaltung entscheidet; privat, wenn Gerichte entscheiden.",[("f3",1)]),
  ("Wichtig wegen Behördenzuständigkeit, Kompetenzverteilung und Amtshaftung.",[("f3",2)])],"rn")
OPEN(7,"Fernlehre 3","S. beantragt Mindestsicherung. Wo? Wie heißt die Entscheidung? Welche Frist, wohin anfechten, bis wohin?","MA 40, Bescheid, 4 Wochen ans Landesverwaltungsgericht, dann VwGH oder VfGH, dann EGMR.",
 [("Antrag bei einer Verwaltungsbehörde, in Wien bei der MA 40. Grundlage: Armenwesen, Art 12 B-VG.",[("f3",4)]),
  ("Die Entscheidung ergeht als Bescheid. Entscheidet die Behörde nicht, gibt es die Säumnisbeschwerde. Bei der WMS beträgt die Entscheidungsfrist 3 Monate.",[("f3",4),("r2",18)]),
  ("Binnen 4 Wochen Beschwerde an das Landesverwaltungsgericht, einzubringen bei der MA 40.",[("f3",4)]),
  ("Danach binnen 6 Wochen Revision an den VwGH oder außerordentliche Beschwerde an den VfGH, mit anwaltlicher Vertretung. Verfahrenshilfe kann innerhalb der Frist beantragt werden.",[("f3",4)]),
  ("Außerhalb Österreichs: Beschwerde an den EGMR wegen Verletzung von Menschenrechten.",[("f3",4),("f3",5)])],"ri")
OPEN(8,"Fernlehre 3","C. fährt 70 km/h im Ortsgebiet. Wer ist zuständig, wie läuft es?","Verwaltungsstrafrecht: Landespolizeidirektion, Schnellverfahren oder Bescheid, 4 Wochen ans Landesverwaltungsgericht.",
 [("Schnellverfahren: Organmandat bis 90 Euro, Anonymverfügung bis 365 Euro, Strafverfügung bis 600 Euro mit Einspruch.",[("f3",5)]),
  ("Sonst Bescheid der Landespolizeidirektion.",[("f3",5)]),
  ("Binnen 4 Wochen Anfechtung beim Landesverwaltungsgericht, einzubringen bei der Behörde 1. Instanz.",[("f3",5)]),
  ("Danach binnen 6 Wochen Revision an den VwGH oder außerordentliche Beschwerde an den VfGH.",[("f3",5)])],"ri")
OPEN(9,"Fernlehre 3","A. lässt bei DM ein Parfüm mitgehen. Wer ist zuständig? Kommt es immer zu diesem Verfahren?","Gerichtliches Strafrecht: Bezirksgericht, Urteil, Berufung ans Landesgericht. Nicht immer: tätige Reue, Diversion.",
 [("Das Bezirksgericht fällt ein Urteil (§ 127 StGB).",[("f3",6)]),
  ("Nach Urteilsverkündung 3 Tage zum Anmelden des Rechtsmittels. Die 4-Wochen-Frist für die Berufung an das Landesgericht läuft ab Erhalt der schriftlichen Ausfertigung.",[("f3",6)]),
  ("Das Strafverfahren ist hier nur in 2 Instanzen angelegt.",[("f3",6)]),
  ("Nicht immer: Bei tätiger Reue, also Rückgabe und Kostenersatz, kommt es oft gar nicht zur Anzeige. Auch eine diversionelle Erledigung ist möglich.",[("f3",6)])],"ri")
OPEN(10,"Fernlehre 3","Frida macht für Frizzy Kindesunterhalt gegen Freya geltend. Wo, wie, wer kann anfechten?","Bezirksgericht, Pflegschaftsabteilung, Beschluss, 2 Wochen Rekurs.",
 [("Bezirksgericht (Pflegschaftsabteilung), die Entscheidung ist ein Beschluss.",[("f3",7)]),
  ("2 Wochen Rekurs an das Landesgericht, Revisionsrekurs an den OGH ist selten möglich.",[("f3",7)]),
  ("Anfechten können das Kind und die Geldunterhaltspflichtige, weil beide beschwert sein können. Das gebietet die Rechtsstaatlichkeit.",[("f3",7)]),
  ("Auch die Kinder- und Jugendhilfe kann das Kind vertreten oder eine Vereinbarung aufnehmen. Das ist ein exekutierbarer Vergleich.",[("f3",6)])],"ri")
OPEN(11,"Fernlehre 3","I. klagt O. auf 14.000 Euro Schadenersatz. Zuständigkeit, Anwalt, Entscheidung, Rechtsmittel?","Mahnklage am Bezirksgericht, Zahlungsbefehl, Einspruch binnen 4 Wochen.",
 [("Mahnklage am Bezirksgericht, weil der Streitwert unter 15.000 Euro liegt. Ergebnis: Zahlungsbefehl.",[("f3",7)]),
  ("Einspruch binnen 4 Wochen eröffnet das mündliche Verfahren. Ohne Einspruch wird der Zahlungsbefehl rechtskräftig und exekutierbar.",[("f3",7)]),
  ("Nach Einspruch müssen sich beide anwaltlich vertreten lassen, weil der Streitwert über 5.000 Euro liegt.",[("f3",7)]),
  ("Urteil, dann 4 Wochen ab Zustellung Berufung an das Landesgericht, Revision an den OGH sehr selten.",[("f3",7)])],"ri")
OPEN(12,"Fernlehre 3","Richtig oder falsch mit Begründung: „Ich kann jedes Gesetz sofort exekutieren lassen.“ „Urteile erlassen auch Behörden.“ „Durch die EU wurden alle Gesetze verändert.“","Alle drei falsch.",
 [("Exekution braucht zuerst ein Verfahren und einen Titel: Urteil, Beschluss, Bescheid.",[("f3",3)]),
  ("Urteile und Beschlüsse kommen von Gerichten, Bescheide von Verwaltungsbehörden.",[("f3",3)]),
  ("Viele Gesetze blieben unverändert. Neu war, dass nun auch Normen gelten, die nicht in Österreich demokratisch legitimierte Organe beschließen; daher die Volksabstimmung vor dem Beitritt.",[("f3",2)])],"rn")
OPEN(13,"Fernlehre 4","„Die Bundespräsidentin gewährt die Demokratie, prüft mit ihrer Unterschrift die Menschenrechtskonformität und bestimmt die Regierungsparteien.“ Stimmt das?","Nein. Sie beurkundet nur das verfassungsmäßige Zustandekommen.",
 [("Sie gewährt keine Grundprinzipien, sondern ist Bestandteil eines Zusammenspiels von Nationalrat, Bundesrat, VfGH, EMRK.",[("f4",1)]),
  ("Die Unterschrift beurkundet das ordnungsgemäße Zustandekommen. Das ist eine rein formale Prüfung.",[("f4",1)]),
  ("Der einzige Fall einer Verweigerung (Heinz Fischer) betraf rückwirkende Strafvorschriften und kann als inhaltlich eingeordnet werden.",[("f4",1)]),
  ("Auch der VfGH prüft nicht jedes Gesetz, sondern nur auf bestimmten Wegen, etwa durch außerordentliche Beschwerde oder Bürger*innenbeschwerde.",[("f4",1)])],"rp")
OPEN(14,"Fernlehre 4","Welche Elemente direkter Demokratie gibt es, und wie stark sind sie?","Volksbefragung, Volksabstimmung, Volksbegehren. Schwach ausgeprägt.",
 [("Volksbefragung, Volksabstimmung und Volksbegehren.",[("f4",2)]),
  ("Im Gegensatz zur Schweiz nicht sehr ausgeprägt.",[("f4",2)]),
  ("Volksbefragungen binden rechtlich nicht, auch erfolgreiche Volksbegehren müssen nicht umgesetzt werden.",[("f4",2)])],"rp")
OPEN(15,"Fernlehre 4","Was heißt „Österreich ist ein Bundesstaat“? Was bleibt beim Bund, was bekommen die Länder?","Aufteilung nach Art 10 bis 15 B-VG.",
 [("Gesetzgebung und Vollziehung sind aufgeteilt: Art 10 bis 15 B-VG.",[("f4",3)]),
  ("Zivilrecht, Strafrecht, Arbeitsrecht und Finanzrecht sind ausschließlich Bund (Art 10), damit sie überall gleich gelten.",[("f4",3)]),
  ("Art 15 ist Auffangtatbestand: Alles Übrige bleibt den Ländern.",[("f4",3)]),
  ("Jedes Bundesland hat eine eigene Landesverfassung, aber kein eigenes Staatssystem.",[("f4",3)])],"rp")
OPEN(16,"Fernlehre 4","Wie kommen Bundes- und Landesgesetze zustande? Stichworte.","Initiative, Nationalrat, Bundesrat, Beurkundung, Gegenzeichnung, Kundmachung.",
 [("Vier Initiativen: Regierungsvorlage, Initiativantrag, Bundesrat, Volksbegehren.",[("f4",4)]),
  ("Nationalrat (183 Abgeordnete): Ausschussarbeit und 3 Lesungen.",[("f4",4)]),
  ("Einfaches Gesetz: mindestens 1/3 anwesend, einfache Mehrheit. Verfassungsgesetz: mindestens 1/2 anwesend, 2/3 Mehrheit.",[("f4",4)]),
  ("Bundesrat (60 Mitglieder): meist nur suspensives Veto, absolutes bei massivem Eingriff in Länderkompetenzen.",[("f4",4)]),
  ("Beurkundung durch Bundespräsident*in, Gegenzeichnung und Kundmachung durch Bundeskanzler*in.",[("f4",4)]),
  ("Landesgesetze: Landtag; Einspruch der Bundesregierung binnen 8 Wochen bei Gefährdung der Bundesinteressen.",[("f4",4)])],"rp")
OPEN(17,"Fernlehre 4","Du möchtest König*in von Österreich werden. Was müsstest du veranlassen?","Abschaffung eines Grundprinzips: Verfassungsmehrheit und Volksabstimmung.",
 [("Monarchie betrifft die Staatsform, also das republikanische Grundprinzip.",[("f4",5)]),
  ("Eine Diktatur beträfe die Herrschaftsform, also das demokratische und weitere Prinzipien.",[("f4",5)]),
  ("Abschaffung oder Aushöhlung braucht eine verbindliche Volksabstimmung: Der Nationalrat beschließt mit Verfassungsmehrheit, vor der Unterzeichnung stimmt das Volk mit Ja oder Nein ab.",[("f4",5)])],"rp")
OPEN(18,"Fernlehre 5","Was bedeutet „Die Gesetzgebung ist von der Vollziehung getrennt“? Was ist Vollziehung?","Gewaltenteilung. Vollziehung ist Gerichtsbarkeit plus Verwaltung.",
 [("Die Staatsfunktionen werden von voneinander unabhängigen Organen ausgeübt, die nicht in andere eingreifen dürfen.",[("f5",1)]),
  ("Vollziehung erfolgt über Gerichtsbarkeit und Verwaltung, die in allen Instanzen getrennt sind und einander nicht anweisen.",[("f5",1)]),
  ("Alle Gerichte sind Bundesbehörden, auch das Landesgericht.",[("f5",1)]),
  ("Es gibt keinen Instanzenzug zwischen Gerichtsbarkeit und Verwaltung.",[("f5",1)])],"rp")
OPEN(19,"Fernlehre 5","Welche Grundsätze beinhaltet das rechtsstaatliche Prinzip?","Willkür verhindern: Gesetzgeber an die Verfassung binden, Vollziehung an die Gesetze.",
 [("Es soll Willkür verhindern und Freiheit und Würde sichern.",[("f5",2)]),
  ("Der Gesetzgeber ist an die Verfassung gebunden, Verwaltung und Gerichte an die Gesetze.",[("f5",2)]),
  ("Ausreichend bestimmte Gesetze und gesetzliche*r Richter*in.",[("f5",2)]),
  ("Verteidigung, Übersetzung, Verfahrensbeteiligung, rechtliches Gehör.",[("f5",2)]),
  ("Rechtsmittel und Legalitätsprinzip.",[("f5",2)])],"rp")
OPEN(20,"Fernlehre 5","„Das Grundrecht auf Eigentum heißt, der Staat teilt mir Eigentum zu.“ „Über meine Arbeit kann ich posten, was ich will.“ Welcher gemeinsame Fehler steckt in solchen Aussagen?","Grundrechte binden den Staat und haben Grenzen.",
 [("Nur der Staat hat Grundrechte zu gewährleisten, auch wenn er privatrechtlich handelt (Fiskalgeltung).",[("f5",3)]),
  ("Fast alle Grundrechte stehen unter Eingriffs- oder Gesetzesvorbehalt.",[("f5",3)]),
  ("Grundrechte enden dort, wo Grundrechte anderer beginnen.",[("f5",3)]),
  ("Eigentumsschutz bedeutet Schutz des vorhandenen Eigentums, keine Zuteilung; Art 10 EMRK erlaubt gesetzliche Einschränkungen.",[("f5",4)])],"rg")
OPEN(21,"Fernlehre 6","Wie erlangen EU-Rechtsakte Verbindlichkeit? Welche EU-Institutionen musst du kennen?","Nur was auf den Folien steht: Richtlinie umsetzen, Verordnung gilt direkt, vier Hauptorgane.",
 [("Zur Prüfung nur lernen, was auf den Folien steht.",[("f6",1)]),
  ("Richtlinien setzen die Staaten um, EU-Verordnungen gelten unmittelbar.",[("f2",3)]),
  ("Kommission, Rat der EU, Parlament und EuGH.",[("rv",79)]),
  ("Der EGMR ist keine EU-Institution.",[("rv",84)])],"re")
OPEN(22,"Fernlehre 7","Worin unterscheiden sich Gerichtsverfahren und Verwaltungsverfahren?","Unabhängigkeit, Entscheidungsform, Einleitung, Vertretung, Grundsätze.",
 [("Verwaltungsorgane sind weisungsgebunden, Richter*innen weisungsfrei, unversetzbar und unabsetzbar.",[("f7",2)]),
  ("Urteil gegen Bescheid.",[("f7",2)]),
  ("Verwaltungsstrafverfahren in der Regel von Amts wegen, Gerichtsverfahren durch Klage oder Anklage.",[("f7",2)]),
  ("Verwaltungsstrafrecht: Kumulationsprinzip, kein kodifiziertes Gesetz, Ankläger*innen und Richter*innen nicht getrennt.",[("f7",2)]),
  ("Anwaltspflicht bei Gericht ab gewissen Größen, im Verwaltungsverfahren kann sich die Partei selbst vertreten.",[("f7",2)]),
  ("Vor Gericht schon in 1. Instanz Mündlichkeit, Unmittelbarkeit, Öffentlichkeit.",[("f7",2)])],"rw")
OPEN(23,"Fernlehre 7","Parteienrechte, Mindestinhalt eines Bescheids, Rechtsmittel: Was sagt das Skript?","Partei hat Akteneinsicht, Gehör, Rechtsmittel. Bescheid mit Spruch, Begründung, Belehrung.",
 [("Parteien: Akteneinsicht, Parteiengehör, Zustellung, Rechtsmittel, Wiederaufnahme, Geltendmachung der Entscheidungspflicht.",[("r2",10)]),
  ("Bescheid: Bezeichnung, Behörde, Spruch, Begründung, Rechtsmittelbelehrung, Unterschrift und Datum.",[("r2",14),("r2",15)]),
  ("Beschwerde binnen 4 Wochen an das Verwaltungsgericht, in der Regel aufschiebend.",[("r2",16)]),
  ("Im Verwaltungsstrafrecht entscheidet die Behörde des Tatorts; Anhaltung bis 6 Wochen.",[("r2",20)])],"rw")
OPEN(24,"Fernlehre 7","Maya M. will 25.000 Euro einklagen, die sie L. gegeben hat. Wo, wie, mit welchem Risiko?","Landesgericht, Mahnklage, Anwaltspflicht. Beweis- und Einbringlichkeitsrisiko.",
 [("Beweislast bei Maya: Zeug*innen und Kontoauszüge. Das Gericht könnte eine Schenkung annehmen oder mangels Fälligkeit abweisen.",[("f7",3)]),
  ("Risiko Zeug*innen: Widersprüche und teure Vertagungen.",[("f7",3)]),
  ("Auch mit Verfahrenshilfe muss sie bei Verlust die Kosten der Gegenseite ersetzen. Rechtsschutzversicherung prüfen.",[("f7",3)]),
  ("Bei Einkommen und Sorgepflicht von L. ist wenig pfändbar. Sie könnte ein Urteil gewinnen und nichts einbringen.",[("f7",3)]),
  ("Landesgericht, weil über 15.000 Euro; Anwaltspflicht; Mahnklage, weil unter 75.000 Euro.",[("f7",3)]),
  ("Einspruch binnen 4 Wochen. Berufung binnen 4 Wochen an das Oberlandesgericht Wien.",[("f7",4)])],"rz")
OPEN(25,"Fernlehre 7","R. Luger hat keinen Zahlungsbefehl bekommen, weil die demente Mutter ihn übernahm. Jetzt läuft die Exekution. Was tun?","Zustellmangel prüfen, Wiedereinsetzung und Einspruch, oder zahlen, wenn die Schuld stimmt.",
 [("Ohne Einspruch ist der Zahlungsbefehl rechtskräftig, sonst gäbe es keine Exekution.",[("f7",4)]),
  ("Zustellmangel prüfen: Er könnte ab tatsächlichem Erhalt heilen (§ 7 ZustellG).",[("f7",4)]),
  ("Fehlerhafte Zustellung geltend machen und gleichzeitig Eventual-Wiedereinsetzungsantrag und Einspruch einbringen.",[("f7",4)]),
  ("Schuldet sie den Betrag, einfach zahlen, aber die Zustellung im Akt dokumentieren lassen und unnötige Kosten nicht zahlen.",[("f7",4)]),
  ("Die Demenz ist für den Zusteller nicht relevant, solange er nicht informiert ist oder es ihm auffallen musste.",[("f7",4)])],"rf")
OPEN(26,"Fernlehre 7","Schützt es, einfach nicht abzuholen oder umzuziehen? Bis wann läuft die Frist bei Hinterlegung am Montag, 19. Oktober 2026?","Nein. Fristende Dienstag, 17. November 2026.",
 [("Kurze Ortsabwesenheit kann man später nachweisen. Sonst wirkt die Hinterlegung nach den Voraussetzungen.",[("f7",5)]),
  ("Wer möglicher Schuldner ist, muss Adressänderungen melden. Gläubiger*innen dürfen an die letzte bekanntgegebene Anschrift adressieren.",[("f7",5)]),
  ("Laut Fernlehre beginnt die Frist am Tag nach der Hinterlegung: ab Dienstag 20. Oktober plus 4 Wochen ergibt Dienstag 17. November.",[("f7",5)]),
  ("Fiele das Ende auf Samstag, Sonntag oder Feiertag, wäre der nächste Werktag das Fristende.",[("f7",5)])],"rf")

# ------------------------------------------------------------ Karten: Normen, Stufenbau
MC("r-norm",[12],"Was unterscheidet Rechtsnormen von Moral oder Sitte?","Sie werden staatlich gesetzt, kundgemacht und mit Zwang durchsetzbar",["Sie gelten nur für Staatsbürger*innen","Sie sind immer gerecht","Sie entstehen durch Gewohnheit in der Gruppe"],"Recht setzt eine staatliche Autorität. Bei Nichtbefolgung kann es mit organisiertem Zwang durchgesetzt werden.",[("rv",7)])
TF("r-norm",[],"Normen der Moral und der Sitte werden vom Staat erlassen.",False,"Falsch. Sie können aber bei der Auslegung ein Anhaltspunkt sein, und manche Gesetze verweisen sogar auf die Sitte.",[("f3",2)])
MC("r-gerecht",[12],"„Recht ist die Kurzform von Gerechtigkeit“. Was stimmt?","Auch als ungerecht empfundenes Recht ist gültig, außer es ist mit Grundwerten unvereinbar",["Ungerechte Gesetze gelten nie","Nur Gerichte dürfen sagen, was gerecht ist","Recht und Gerechtigkeit sind gesetzlich gleichgestellt"],"Recht ist nicht mit Gerechtigkeit gleichzusetzen. Siehe auch die Diskussion von Kelsen bis Radbruch.",[("f3",3)])
MATCH("r-gerecht",[],"Wer vertritt was?",[["Kelsen","Reine Rechtslehre: Trennung von Recht und Moral"],["Radbruch","Unerträglich ungerechtes Gesetz muss weichen"]],"Kelsen trennt streng in Sollen und Sein. Radbruch reagiert auf die Justiz im Dritten Reich.",[("rv",10),("rv",11)])
BUCKET("r-einteil",[6],"Wohin gehört das Rechtsgebiet?",["Öffentliches Recht","Privatrecht"],[("Strafrecht",0),("Mietrecht",1),("Verwaltungsrecht",0),("Eherecht",1),("Finanzrecht",0),("Arbeitsrecht",1),("Prozessrecht",0),("Verbraucher*innenrecht",1)],"Öffentliches Recht: Person steht dem Staat gegenüber. Privatrecht: Bürger*innen untereinander, teils Sonderprivatrecht.",[("f3",1),("f3",2)])
MATCH("r-einteil",[6],"Welche Theorie sagt was?",[["Interessentheorie","Öffentliche oder private Interessen"],["Subordinationstheorie","Über- und Unterordnung"],["Subjektstheorie","Rechtsträger mit Hoheitsgewalt beteiligt"],["Rechtswegtheorie","Verwaltung oder Gericht entscheidet"]],"Keine Theorie überzeugt abschließend.",[("f3",1),("rv",25)])
MC("r-formen",[12],"Wer erlässt einen Bescheid?","Verwaltungsbehörden",["Bezirksgerichte","Der Oberste Gerichtshof","Das Parlament"],"Urteile und Beschlüsse kommen vom Gericht, Bescheide von Verwaltungsbehörden.",[("f3",3)])
TF("r-formen",[12],"Es ist am sichersten, jeden Vertrag gleich vor Gericht oder dem Justizministerium abzuschließen.",False,"Geht gar nicht: Der Brotkauf ist ein mündlicher Kaufvertrag. Ein gerichtlicher Vergleich enthält aber einen exekutierbaren Vertrag.",[("f3",3)])
MC("r-gesetzesstaat",[1],"Welcher Satz beschreibt Österreich?","Jede Entscheidung braucht eine gesetzliche Grundlage, Höchstgerichte geben den Auslegungsrahmen vor",["Vorentscheidungen ersetzen das Gesetz","Jede Behörde legt Gesetze nach eigenem Gutdünken aus","Nur Gesetzeswissen zählt, Urteile sind egal"],"Legalitätsprinzip. Untere Instanzen halten sich an OGH, VwGH und VfGH.",[("f2",1)])
TF("r-gesetzesstaat",[1],"Das Erstgericht hilft den Parteien im Zivilprozess beim Nachweis ihrer Tatsachen.",False,"Tatsachen werden nur erhoben, wenn die Parteien das rechtzeitig und richtig beantragen.",[("f2",1)])
ORD("r-stufen",[3,4],"Ordne den Stufenbau von oben nach unten.",["Baugesetze der Verfassung","Verfassungsgesetze","Einfache Gesetze","Verordnungen","Urteile, Bescheide, Verträge","Zwangsvollstreckung"],"Höherrangiges bedingt den Rahmen für das Untere.",[("rv",27)])
TF("r-stufen",[3],"Die Straßenverkehrsordnung ist eine Verordnung.",False,"Die StVO ist ein Bundesgesetz, trotz des Namens.",[("f2",3)])
MC("r-stufen",[3],"Warum steht das BVG über die Rechte von Kindern über § 138 ABGB?","Es ist Verfassungsrecht, § 138 ABGB nur einfaches Gesetz",["Es ist jünger","Es gilt nur für Kinder","Das ABGB ist Privatrecht und zählt daher nicht"],"Widerspricht ein Gesetz einem Verfassungsgesetz, hat das höherrangige Vorrang.",[("f2",2),("f2",3)])
MC("r-stufen",[3],"Was ist die WMG-Verordnung im Stufenbau?","Eine Verordnung, die das Wiener Mindestsicherungsgesetz konkretisiert",["Ein Bescheid der MA 40","Ein Bundesgesetz","Verfassungsrecht"],"Verordnungen gibt es vor allem in der Verwaltung zur Konkretisierung von Gesetzen.",[("f2",2),("f2",3)])
MC("r-stufen",[],"Zwei Gesetze widersprechen einander. Welche Auslegungsregel gibt es?","Das jüngere vor dem älteren, das speziellere vor dem allgemeinen",["Das ältere gilt immer","Das längere gilt","Die Behörde wählt frei"],"Dazu: Verfassungsrecht vor einfachem Gesetz.",[("f2",6)])
MULTI("r-eurecht",[],"Was stimmt zu EU-Recht?",["EU-Verordnungen gelten unmittelbar","EU-Richtlinien müssen die Staaten umsetzen","Die Baugesetze stehen über dem EU-Recht"],["EU-Recht steht über allem österreichischen Recht","EU-Verordnungen und österreichische Verordnungen sind dasselbe"],"Achtung Begriff: EU-Verordnung ist nicht innerstaatliche Verordnung. Einfaches Verfassungsrecht steht unter dem EU-Recht.",[("f2",3),("f3",2)])
TF("r-eurecht",[12],"Durch die EU wurden alle österreichischen Gesetze verändert.",False,"Viele blieben unverändert. Wegen der Auswirkung auf das demokratische Prinzip brauchte der Beitritt eine Volksabstimmung.",[("f3",2)])
MC("r-recherche",[2],"Du kennst nur ungefähr das Thema und willst losgoogeln. Was passt zuerst?","Jusline",["RIS, weil es fehlertolerant ist","Bundesgesetzblatt","Amtsblatt der EU"],"Das RIS hat keine Fehlertoleranz. Es ist sehr gut, wenn man schon weiß, was man sucht.",[("f2",2)])

# Prinzipien
MULTI("r-prinz",[3,17],"Welche gehören zu den sechs Grundprinzipien?",["Demokratisches Prinzip","Bundesstaatliches Prinzip","Rechtsstaatliches Prinzip","Liberales Prinzip"],["Soziales Prinzip","Neutralitätsprinzip"],"Dazu kommen das republikanische und das gewaltenteilende Prinzip. Neutralität ist eine Staatszielbestimmung.",[("rv",36),("rv",77)])
BUCKET("r-prinz",[],"Steht das Prinzip ausdrücklich im B-VG oder ergibt es sich aus dem Gesamtkontext?",["Ausdrücklich","Aus Gesamtkontext"],[("Demokratisch",0),("Republikanisch",0),("Bundesstaatlich",0),("Rechtsstaatlich",1),("Gewaltenteilend",1),("Liberal",1)],"Art 1 und Art 2 B-VG nennen die ersten drei.",[("rv",37)])
MC("r-prinz",[17],"Monarchie oder Republik: Was wäre betroffen?","Die Staatsform",["Die Herrschaftsform","Der Föderalismus","Die Gewaltenteilung allein"],"Republik ist die Staatsform, Demokratie die Herrschaftsform.",[("f4",5),("rv",49)])
MC("r-bp",[13],"Was prüft die Bundespräsidentin mit ihrer Unterschrift unter ein Gesetz?","Ob das Gesetz ordnungsgemäß zustande gekommen ist",["Ob es menschenrechtskonform ist","Ob es EU-konform ist","Ob es politisch sinnvoll ist"],"Rein formale Prüfung. Die einzige Verweigerung durch Fischer betraf aber rückwirkende Strafvorschriften.",[("f4",1)])
TF("r-bp",[13],"Der VfGH prüft jedes einzelne Gesetz, bevor es gilt.",False,"Er prüft nur auf bestimmten Wegen, etwa nach Beschwerde, Vorlage eines Gerichts oder Bürger*innenbeschwerde.",[("f4",1)])
MC("r-direkt",[14],"Welches Instrument ist verbindlich?","Volksabstimmung",["Volksbefragung","Volksbegehren","Petition"],"Volksbefragungen binden nicht, erfolgreiche Volksbegehren müssen nicht umgesetzt werden.",[("f4",2),("f4",5)])
MATCH("r-bund",[15],"Wer macht was?",[["Art 10 B-VG","Gesetz Bund, Vollziehung Bund"],["Art 11 B-VG","Gesetz Bund, Vollziehung Land"],["Art 12 B-VG","Grundsatz Bund, Ausführung und Vollziehung Land"],["Art 15 B-VG","Gesetz Land, Vollziehung Land"]],"Armenwesen fällt unter Art 12. Art 15 ist Auffangtatbestand.",[("rv",52)])
TF("r-bund",[18],"Das Landesgericht ist eine Behörde des Landes.",False,"Alle Gerichte sind Bundesbehörden, auch bei der Bezeichnung Landesgericht.",[("f5",1)])
TF("r-bund",[15],"Für ganz Österreich gibt es genau ein Verfassungsgesetz, in dem alles steht.",False,"Neben dem B-VG gibt es zersplitterte Verfassungsbestimmungen, und jedes Land hat seine Landesverfassung.",[("f4",3),("rv",34)])
ORD("r-gesetz",[16],"Bring den Weg eines Bundesgesetzes in die richtige Reihenfolge.",["Gesetzesinitiative","Ausschuss und 3 Lesungen im Nationalrat","Bundesrat","Beurkundung durch Bundespräsident*in","Gegenzeichnung durch Bundeskanzler*in","Kundmachung im Bundesgesetzblatt"],"Mit der Kundmachung gilt das Gesetz.",[("f4",4)])
MC("r-gesetz",[16],"Welche Mehrheit braucht ein Verfassungsgesetz?","Mindestens 1/2 anwesend und 2/3 Mehrheit",["1/3 anwesend und einfache Mehrheit","Alle Abgeordneten","Volksabstimmung in jedem Fall"],"Einfache Gesetze: 1/3 anwesend und einfache Mehrheit.",[("f4",4)])
MC("r-gesetz",[16],"Wie stark ist der Bundesrat in der Regel?","Nur suspensives Veto",["Absolutes Veto","Er entscheidet endgültig","Er hat keine Mitwirkung"],"Absolutes Veto nur bei massivem Eingriff in Länderkompetenzen.",[("f4",4)])
MULTI("r-rechtsstaat",[19],"Was gehört zum rechtsstaatlichen Prinzip?",["Recht auf gesetzliche*n Richter*in","Rechtliches Gehör","Überprüfbarkeit von Entscheidungen","Legalitätsprinzip"],["Wahlrecht ab 16","Oberbefehl über das Bundesheer"],"Es bindet den Gesetzgeber an die Verfassung und die Vollziehung an die Gesetze.",[("f5",2)])
TF("r-rechtsstaat",[18],"Gegen eine Entscheidung einer Verwaltungsbehörde geht man einfach zum Bezirksgericht in die nächste Instanz.",False,"Es gibt keinen Instanzenzug zwischen Gerichtsbarkeit und Verwaltung.",[("f5",1),("rv",29)])
MATCH("r-kontrolle",[],"Was kontrolliert wer?",[["Volksanwaltschaft","Missstände der Verwaltung"],["Rechnungshof","Finanzielle Gebarung"],["VwGH","Rechtswidrigkeit im Verwaltungsbereich"],["VfGH","Verfassungsmäßigkeit von Gesetzen"]],"Volksanwaltschaft: jede*r kann sich beschweren. Tirol und Vorarlberg haben Besonderheiten.",[("rv",69),("rv",70),("rv",71),("f5",2)])

# Grundrechte
TF("r-grund",[5,20],"Alle Privatpersonen haben sich gegenüber ihren Nachbar*innen an Grundrechte zu halten.",False,"Private haben keine Grundrechte zu gewähren. Sie halten sich an Gesetze, die den Grundrechten entsprechen müssen.",[("f5",3)])
MC("r-grund",[20],"Was bedeutet Fiskalgeltung der Grundrechte?","Der Staat muss sie auch wahren, wenn er privatrechtlich handelt",["Steuern müssen gerecht sein","Nur Finanzämter sind gebunden","Private zahlen für Grundrechte"],"Beispiel: Ausschreibung, PC-Ankauf, Vergaberecht.",[("f5",3),("f2",7)])
CHAIN("r-grund",[5],"Stanislaus wurde beraubt","Stanislaus verlangt das Geld vom Staat, notfalls mit Grundrechten.",[
 ("Liegt eine Grundrechtsverletzung vor?","Nein, ein Delikt einer Privatperson",["Ja, Eigentum wurde verletzt","Ja, weil die Polizei nicht da war"],"Grundrechte gewährt der Staat, nicht der*die Räuber*in.",[("f2",7)]),
 ("Wie kommt er zum Geld?","Schadenersatzklage oder Privatbeteiligung im Strafverfahren",["Antrag beim Finanzamt","Beschwerde an den EGMR"],"Der Anschluss als Privatbeteiligte*r spart oft Kosten.",[("f2",7),("f2",8)]),
 ("Was wenn der*die Täter*in nichts hat?","Dann kann er leer ausgehen",["Dann zahlt der Staat","Dann zahlt die Polizei"],"Ohne Exekutierbares hilft auch das Urteil nicht.",[("f2",7)]),
 ("Kann er die Anzeige zurücknehmen?","Nein, das ist ein Offizialdelikt",["Ja, jederzeit","Ja, mit Zustimmung des Täters"],"Der Staat muss bei hinreichend Substrat tätig werden.",[("f2",8)]),
],"Schaden, Strafrecht und Grundrechte sind drei verschiedene Ebenen.")
TF("r-grenzen",[20],"Der Gleichheitsgrundsatz besagt, dass alle vom Staat die gleichen Zuschüsse bekommen müssen.",False,"Das ist eine der falschen Aussagen aus Fernlehre 5. Grundrechte können auch sachlich gerechtfertigte Anforderungen nicht beseitigen.",[("f5",3)])
TF("r-grenzen",[20],"Die Erwerbsfreiheit erlaubt mir, morgen eine Fachhochschule zu eröffnen.",False,"Sachlich gerechtfertigte Anforderungen und Ausgestaltungen bleiben aufrecht.",[("f5",3)])
MC("r-grenzen",[20],"Was gilt für die Meinungsfreiheit nach Art 10 EMRK?","Sie kann gesetzlich eingeschränkt werden, etwa zum Schutz des guten Rufes",["Sie gilt absolut","Sie gilt nur im Privaten","Sie gilt nur für Journalist*innen"],"Abs 2 nennt Einschränkungen, die in einer demokratischen Gesellschaft unentbehrlich sind.",[("f5",4)])

# Wer entscheidet
BUCKET("r-rechtsweg",[7,8,9,10,11],"Gericht oder Verwaltungsbehörde?",["Verwaltungsbehörde","Gericht"],[("Antrag auf Mindestsicherung",0),("70 km/h im Ortsgebiet",0),("Parfüm bei DM mitgehen lassen",1),("Kindesunterhalt",1),("Schadenersatz 14.000 Euro",1),("Antrag auf Invaliditätspension",0)],"Faustregel aus Fernlehre 3 und 7. Die Exekution läuft immer über Gericht.",[("f3",4),("f3",5),("f3",6),("f3",7),("f7",1)])
CHAIN("r-rechtsweg",[7],"S. beantragt Mindestsicherung","Geh den ganzen Weg mit S.",[
 ("Wo stellt S. den Antrag?","MA 40",["Bezirksgericht","Landesgericht","AMS"],"Verwaltungsbehörde, in Wien die MA 40.",[("f3",4)]),
 ("Wie heißt die Entscheidung?","Bescheid",["Urteil","Beschluss","Zahlungsbefehl"],"Verwaltungsbehörden entscheiden mit Bescheid.",[("f3",4)]),
 ("Bis wann muss die MA 40 entscheiden?","3 Monate",["6 Wochen","4 Wochen","6 Monate"],"6 Monate ist die allgemeine Frist, bei der WMS sind es 3 Monate.",[("r2",18)]),
 ("Die Behörde bleibt untätig. Was jetzt?","Säumnisbeschwerde",["Einspruch","Rekurs","Revision"],"Bei der Behörde einzubringen, adressiert an das Landesverwaltungsgericht.",[("f3",4)]),
 ("Bescheid negativ. Frist und Ziel?","4 Wochen, Landesverwaltungsgericht",["2 Wochen, Landesgericht","4 Wochen, Bezirksgericht","6 Wochen, VwGH"],"Einzubringen bei der MA 40.",[("f3",4)]),
 ("Wie geht es danach weiter?","6 Wochen, VwGH oder VfGH mit Anwalt",["4 Wochen, OGH ohne Anwalt","Gar nicht mehr","2 Wochen, Landesgericht"],"Verfahrenshilfe kann innerhalb der Frist beantragt werden.",[("f3",4)]),
 ("Und ganz zum Schluss?","EGMR wegen Menschenrechtsverletzung",["EuGH wegen EU-Recht","Bundespräsidentin","Volksanwaltschaft als Instanz"],"Eine Klage der Privatperson vor dem EGMR ist möglich.",[("f3",4),("f3",5)]),
],"Behörde, Landesverwaltungsgericht, VwGH oder VfGH, EGMR.")
CHAIN("r-schnell",[8],"C. fährt zu schnell","C. wird mit 70 km/h im Ortsgebiet gemessen.",[
 ("Welcher Bereich ist das?","Verwaltungsstrafrecht",["Gerichtliches Strafrecht","Zivilrecht"],"Die StVO enthält selbst Strafbestimmungen.",[("rv",18),("f3",5)]),
 ("Bis wie viel geht eine Anonymverfügung?","365 Euro",["90 Euro","600 Euro","1000 Euro"],"Organmandat in der Regel bis 90 Euro, Strafverfügung bis 600 Euro.",[("f3",5)]),
 ("Wogegen gibt es Einspruch?","Strafverfügung",["Organmandat","Anonymverfügung"],"Bei den anderen zwei: nicht zahlen eröffnet das Verfahren.",[("f3",5)]),
 ("Wer erlässt den Bescheid im Normalverfahren?","Landespolizeidirektion",["Bezirksgericht","Landtag"],"Danach 4 Wochen Beschwerde an das Landesverwaltungsgericht.",[("f3",5)]),
],"Verwaltungsstrafen landen nicht bei Gericht in erster Instanz.")
CHAIN("r-rechtsweg",[9],"A. und das Parfüm","A. lässt bei DM ein Parfüm mitgehen.",[
 ("Wer ist zuständig?","Bezirksgericht",["Landespolizeidirektion","MA 40","Handelsgericht"],"§ 127 StGB, Strafdrohung unter einem Jahr.",[("f3",6)]),
 ("Wie viele Tage hat A., um das Rechtsmittel anzumelden?","3 Tage",["14 Tage","4 Wochen"],"Die 4 Wochen beginnen erst mit der schriftlichen Ausfertigung.",[("f3",6)]),
 ("Wohin geht die Berufung?","Landesgericht",["OGH","Landesverwaltungsgericht"],"Das Strafverfahren ist hier nur in 2 Instanzen angelegt.",[("f3",6)]),
 ("Kommt es immer dazu?","Nein, tätige Reue oder Diversion sind möglich",["Ja, immer","Nur bei Vorstrafen nicht"],"A. kommt eventuell mit einem blauen Auge davon.",[("f3",6)]),
],"Andere Fristen als im Verwaltungsverfahren, deshalb gern verwechselt.")
MC("r-rechtsweg",[10],"Welches Rechtsmittel gibt es gegen den Unterhaltsbeschluss?","Rekurs binnen 2 Wochen",["Berufung binnen 4 Wochen","Beschwerde binnen 4 Wochen","Einspruch binnen 14 Tagen"],"Beschluss, deshalb Rekurs. Revisionsrekurs an den OGH selten.",[("f3",7)])
MATCH("r-rechtsweg",[7,9,10,11],"Welches Rechtsmittel gehört zu welcher Entscheidung?",[["Bescheid","Beschwerde"],["Zivilurteil","Berufung"],["Beschluss","Rekurs"],["Zahlungsbefehl","Einspruch"]],"Die Begriffe sind nicht austauschbar.",[("f3",4),("f3",7),("r2",29)])
MATCH("r-rechtsweg",[7,10],"Welche Frist gilt?",[["Beschwerde gegen Bescheid","4 Wochen"],["Rekurs gegen Unterhaltsbeschluss","2 Wochen"],["Revision an den VwGH","6 Wochen"],["Anmeldung Strafberufung","3 Tage"]],"Merkkette für die Fälle. Einspruch und Berufung im Zivilprozess: ebenfalls 4 Wochen.",[("f3",4),("f3",6),("f3",7)])

# Verwaltungsverfahren
MULTI("r-avg",[23],"Welche Rechte hat eine Partei?",["Akteneinsicht","Parteiengehör","Zustellung des Bescheides","Rechtsmittel"],["Recht auf positive Entscheidung","Eigene Beweisregeln"],"Dazu: Wiederaufnahme und Geltendmachung der Entscheidungspflicht. Alle anderen sind nur Beteiligte.",[("r2",10)])
MC("r-avg",[],"Grundsatz der materiellen Wahrheit: Was heißt das?","Die Behörde muss selbst den Sachverhalt erforschen",["Die Behörde glaubt der Partei","Es zählt nur der Antrag","Drei Zeug*innen gelten als Wahrheit"],"Beispiel im Skript: Hausbesuch bei Verdacht auf Kindeswohlgefährdung. Das letzte wäre eine Beweisregel, die es nicht gibt.",[("r2",14)])
TF("r-avg",[23],"Im Verwaltungsverfahren kann mich auch meine Lebensgefährtin vertreten.",True,"Jede eigenberechtigte Person kann mit Vollmacht vertreten.",[("r2",10),("f7",2)])
MC("r-bescheid",[23],"Was muss ein Bescheid NICHT enthalten?","Eine Unterschrift der Partei",["Den Spruch","Die Begründung","Die Rechtsmittelbelehrung"],"Unterschrieben wird von der Behörde.",[("r2",14),("r2",15)])
MC("r-beschwerde",[23],"Bis wann muss die Behörde allgemein spätestens entscheiden?","Innerhalb von 6 Monaten",["Innerhalb von 4 Wochen","Innerhalb von 1 Jahr","Es gibt keine Frist"],"Bei der WMS sind es 3 Monate. Die säumige Behörde kann die Entscheidung binnen 3 Monaten nachholen.",[("r2",18)])
MC("r-beschwerde",[],"Wann gibt es heute noch die Berufung mit 2 Wochen im Verwaltungsverfahren?","Im eigenen Wirkungsbereich der Gemeinden",["Bei der Mindestsicherung","Bei jedem Bescheid","Bei Verwaltungsstrafen"],"Etwa örtliche Baupolizei. Sonst heißt das Rechtsmittel Beschwerde.",[("r2",17)])
TF("r-beschwerde",[23],"Für eine Beschwerde an das Verwaltungsgericht braucht man eine Anwältin.",False,"Kein Anwaltszwang. Erst ab VwGH und VfGH.",[("r2",16),("f3",4)])
TF("r-beschwerde",[23],"Eine rechtzeitige Beschwerde hat grundsätzlich aufschiebende Wirkung.",True,"Unter gewissen Voraussetzungen kann das ausgeschlossen werden.",[("r2",16)])
MC("r-wieder",[25],"Frau X. liegt im Krankenhaus und versäumt die Beschwerdefrist. Was hilft?","Wiedereinsetzung binnen 2 Wochen ab Wegfall des Hindernisses",["Wiederaufnahme binnen 3 Jahren","Einspruch binnen 4 Wochen","Nichts"],"Krankheit kann ein unvorhersehbares Ereignis sein. Die Beschwerde gleich mitbringen.",[("r2",18)])
BUCKET("r-vstg",[22],"Trifft es auf Verwaltungsstrafe oder Gerichtsstrafe zu?",["Verwaltungsstrafe","Gerichtsstrafe"],[("Kumulationsprinzip",0),("StGB als Kodifikation",1),("Ankläger*in und Entscheider*in nicht getrennt",0),("Eintrag im Strafregister",1),("Höchstens 6 Wochen Freiheitsstrafe",0)],"Haft über 6 Wochen dürfen nur Gerichte verhängen.",[("r2",19),("r2",20),("f7",2)])
BUCKET("r-vstg",[22],"Wo gehört der Fall hin?",["Verwaltungsverfahren","Verwaltungsstrafverfahren","Zivilverfahren","Strafverfahren"],[("Antrag auf Invaliditätspension",0),("Geschwindigkeitsübertretung",1),("Amtshaftungsklage auf Schadenersatz",2),("Verbreitung von NS-Gedankengut",3),("Mietrückstand wird eingeklagt",2)],"Aus den Korrekturen in Fernlehre 7. Auch bei Verwaltungshandeln können zivilrechtliche Ansprüche entstehen.",[("f7",1)])

# Zivil
BUCKET("r-zpo",[24],"Welches Gericht?",["Bezirksgericht","Landesgericht"],[("Klage über 14.000 Euro",0),("Klage über 25.000 Euro",1),("Scheidung",0),("Besitzstörung",0),("Arbeitsrechtsklage",1),("Amtshaftung",1)],"Eigenzuständigkeit geht vor Wertzuständigkeit. Grenze sonst 15.000 Euro.",[("r2",28),("f7",3),("f3",7)])
MC("r-zpo",[24],"Ab wann besteht am Bezirksgericht absolute Anwaltspflicht?","Streitwert über 5.000 Euro bei Wertzuständigkeit",["Immer","Streitwert über 15.000 Euro","Nie"],"Bis 5.000 Euro kann auch ein*e Nichtjurist*in vertreten.",[("r2",28),("r2",29)])
MC("r-zpo",[24],"Wer muss im Zivilprozess in der Regel beweisen?","Die klagende Partei",["Das Gericht von Amts wegen","Die beklagte Partei immer","Die Staatsanwaltschaft"],"Beklagte nur manchmal, etwa bei Schadenersatz aus Vertrag.",[("r2",25),("f7",3)])
CHAIN("r-mahn",[24,25],"Der Zahlungsbefehl","Herr T. findet einen Zahlungsbefehl über 2.000 Euro in der Post. Er glaubt, die Forderung stimmt nicht.",[
 ("Hat das Gericht die Forderung geprüft?","Nein, nur Formvorschriften und Schlüssigkeit",["Ja, genau","Ja, mit Zeug*innen"],"Keine inhaltliche Überprüfung.",[("r2",32),("f7",3)]),
 ("Welche Frist hat er?","4 Wochen Einspruch",["2 Wochen Rekurs","14 Tage Widerspruch"],"Auch ab Zustellung durch Hinterlegung.",[("r2",32)]),
 ("Muss er den Einspruch begründen?","Nein, ein leerer Einspruch genügt am Bezirksgericht",["Ja, ausführlich","Ja, durch Anwältin"],"Es muss nur ersichtlich sein, dass er Einspruch erheben will.",[("r2",32)]),
 ("Was passiert ohne Einspruch?","Rechtskräftig und vollstreckbar",["Das Gericht lädt ihn nochmal","Die Forderung verfällt"],"Damit ist es ein Exekutionstitel. Im Zweifel Einspruch.",[("r2",32)]),
],"Die wichtigste Handlungsanleitung für die Praxis: nie liegen lassen.")
TF("r-mahn",[11],"Ein Zahlungsbefehl über 14.000 Euro kommt vom Bezirksgericht.",True,"Streitwert unter 15.000 Euro.",[("f3",7)])
MC("r-kosten",[24],"Maya M. bekommt Verfahrenshilfe und verliert. Was gilt?","Sie muss die Kosten der Gegenseite trotzdem ersetzen",["Der Staat zahlt alles","Sie zahlt nichts","Die Gegenseite trägt ihre Kosten selbst"],"Darum lohnt der Blick auf eine Rechtsschutzversicherung.",[("f7",3)])
TF("r-kosten",[24],"Ein gewonnenes Urteil über 25.000 Euro heißt, dass Maya das Geld bekommt.",False,"Bei L. ist vielleicht kaum etwas pfändbar. Sie trägt dann die Prozesskosten und bringt nichts ein.",[("f7",3)])
MC("r-besitz",[],"Der Mietvertrag ist abgelaufen. Der Vermieter wechselt das Schloss. Was gilt?","Der Mieter kann auf Besitzstörung klagen",["Das ist erlaubt","Das ist eine Verwaltungsstrafe","Der Mieter hat keine Rechte mehr"],"Der Vermieter muss auf Räumung klagen.",[("f7",1)])

# Zustellung
MATCH("r-zust",[25],"Welche Zustellart?",[["RSa, blauer Brief","Nur eigenhändig"],["RSb, weißer Brief","Ersatzzustellung möglich"],["Hinterlegung","Mit erstem Tag der Abholfrist zugestellt"]],"Seit 2009 gehen Klagen und Zahlungsbefehle nur noch mit RSb. Das birgt Risiken.",[("r2",41),("r2",42),("r2",43)])
MC("r-zust",[25],"Ein Zahlungsbefehl wird an die erwachsene Mitbewohnerin übergeben. Ist das möglich?","Ja, RSb erlaubt Ersatzzustellung",["Nein, nur eigenhändig","Nur mit Vollmacht","Nur bei Bescheiden"],"Ersatzempfänger*innen sind Erwachsene an derselben Abgabestelle.",[("r2",42)])
MC("r-zust",[26],"Frau E. holt den Gerichtsbrief nicht ab. Was gilt?","Er gilt trotzdem als zugestellt, die Frist läuft",["Dann gibt es keine Frist","Das Gericht muss es nochmal versuchen","Der Fall ruht"],"Die Nichtabholung kann Rechtsfolgen auslösen. Verweigern hat oft weitreichende Folgen.",[("r2",41),("r2",43)])
TF("r-zust",[26],"Wer umzieht, ist vor rechtswirksamer Zustellung geschützt.",False,"Gläubiger*innen brauchen nur an die letzte bekanntgegebene Anschrift zu adressieren.",[("f7",5)])
MULTI("r-maengel",[25],"Was ist ein Zustellmangel?",["RSa-Brief an Ersatzempfänger*in","Falscher Name","Zustellung trotz bekannter Ortsabwesenheit"],["Empfängerin hat keine Lust abzuholen","Brief ist unangenehm"],"Der Mangel heilt, wenn das Dokument tatsächlich ankommt.",[("r2",43)])
CALC("r-frist",[26],"Hinterlegung am Montag, 19. Oktober 2026. 4 Wochen Beschwerdefrist. Der wievielte November ist das Fristende?","17","November",["Fristlauf laut Fernlehre ab dem Tag danach: Dienstag, 20. Oktober.","4 Wochen später ist Dienstag, 17. November."],"Fiele das Ende auf Samstag, Sonntag oder Feiertag, wäre es der nächste Werktag.",[("f7",5)],tol=0)
CALC("r-frist",[],"Zustellung am Freitag, 6. November 2026. 2 Wochen Frist, Wochenfristen enden am gleichnamigen Tag. Der wievielte November ist das Fristende?","20","November",["2 Wochen nach Freitag dem 6. ist Freitag der 20."],"Samstag und Sonntag behindern den Lauf nicht, nur das Ende.",[("r2",44)],tol=0)
TF("r-frist",[],"Bei verfahrensrechtlichen Fristen reicht es, die Erklärung am letzten Tag zur Post zu bringen.",True,"Der Postweg zählt nicht in die Frist. Bei materiellen Fristen, etwa einer Mietkündigung, muss sie angekommen sein.",[("r2",43)])
TF("r-frist",[],"Der Einwurf in den gerichtlichen Einlaufpostkasten zählt sofort als Eingang.",False,"Erst bei dessen Leerung, unter Umständen am nächsten Tag.",[("r2",44)])

# Exekution
MC("r-exe",[12],"Was ist kein Exekutionstitel?","Ein einfaches Gesetz",["Ein Urteil","Ein gerichtlicher Vergleich","Ein rechtskräftiger Zahlungsbefehl"],"Exekution braucht zuerst ein Verfahren. Auch Geldstrafen und Rückstandsaufträge sind Titel.",[("r2",34),("f3",3)])
TF("r-exe",[],"Der Gläubiger, der zuerst exekutiert, wird zuerst befriedigt.",True,"Prioritätsprinzip: Rang entscheidet. Nachrangige gehen oft leer aus.",[("r2",35)])
MULTI("r-exe",[],"Was ist bei der Fahrnispfändung unpfändbar?",["Bett","Kühlschrank","Waschmaschine","Für den Beruf notwendige Gegenstände"],["Zweites Auto","Luxusuhr"],"Schuldner*innen sollen weiterleben können.",[("r2",37)])
TF("r-exe",[],"Mein Name steht nicht auf der Rechnung des Fernsehers meiner Mitbewohnerin. Der Exekutor darf ihn sicher nicht mitnehmen.",False,"Im Zweifel kann trotzdem gepfändet werden. Eigentümer*innen wehren sich mit einer Exszindierungsklage. Rechnungen auf den eigenen Namen helfen.",[("r2",37)])
MC("r-exmin",[],"Wie hoch ist 2026 der allgemeine Grundbetrag bei Lohnpfändung?","1.308 Euro",["1.229,89 Euro","1.827 Euro","900 Euro"],"Bei AMS-Bezug 1.526 Euro. 1.827 Euro wäre die Armutsgefährdungsschwelle, deren Höhe Schuldenberatungen und Armutskonferenz als Grenze fordern.",[("r2",38),("r2",39)])
BUCKET("r-exmin",[],"Pfändbar oder nicht?",["Beschränkt pfändbar","Nicht pfändbar"],[("Lohn",0),("Notstandshilfe",0),("Krankengeld",0),("Mindestsicherung",1),("Familienbeihilfe",1),("Kinderbetreuungsgeld",1),("Wohnbeihilfe",1)],"Arbeitslosengeld und Notstandshilfe: erhöhter Grundbetrag, weil nur 12-mal ausbezahlt.",[("r2",40)])
MC("r-exmin",[],"Warum ist die Unterhaltsexekution so hart?","Es bleiben nur 75 % des Grundbetrags, ohne Unterhaltsbeträge",["Sie ist unbegrenzt","Sie betrifft auch Beihilfen","Sie läuft in Haft"],"Das soll zum Zahlen bewegen, führt in der Praxis aber oft zu akuter Existenzgefährdung.",[("r2",40)])
CALC("r-exmin",[],"Herr P. bezieht Notstandshilfe und ist für ein Kind unterhaltspflichtig. Wie hoch ist die Summe aus erhöhtem Grundbetrag und einem Unterhaltsgrundbetrag?","1526+261","Euro",["Erhöhter Grundbetrag bei AMS-Bezug: 1.526 Euro.","Unterhaltsgrundbetrag: 261 Euro.","Summe: 1.787 Euro, dazu kämen noch Steigerungsbeträge."],"Das System verstehen zählt, nicht das Rechnen im Detail.",[("r2",38),("r2",40)],tol=0)
TF("r-ins",[],"Für den Privatkonkurs muss vorher ein außergerichtlicher Ausgleich versucht werden.",False,"Keine Voraussetzung mehr. In wenigen Fällen ist er trotzdem sinnvoll.",[("r2",48)])
MC("r-ins",[],"Was stoppt die Insolvenzeröffnung NICHT?","Unterhaltsexekution",["Zinsenlauf","Andere Exekutionen","Weitere Kosten"],"Unterhalt läuft weiter.",[("r2",49)])
MC("r-ins",[],"Wie lange dauert ein Abschöpfungsverfahren bei Antrag ab 17.7.2026?","5 Jahre",["3 Jahre","7 Jahre","10 Jahre"],"Die 3-jährige Variante ist weggefallen. Bedenken wegen Gleichheitsgrundsatz gegenüber Unternehmer*innen werden vorgebracht.",[("r2",50),("r2",51)])
MULTI("r-ins",[],"Welche Obliegenheiten gelten in der Abschöpfung?",["Sich um zumutbaren Erwerb bemühen","Wohnungswechsel anzeigen","Erbschaften melden und herausgeben","Keine neuen Schulden"],["Keine Urlaube","Eigentumswohnung kaufen"],"Sonst Einstellung und lange Sperrfristen.",[("r2",52)])
MC("r-ins",[],"Eheleute haben gemeinsame Schulden. Was gilt?","Jede*r braucht ein eigenes Insolvenzverfahren",["Ein gemeinsames reicht","Nur der*die Hauptschuldner*in","Scheidung ist nötig"],"Bürg*innen und Mitschuldner*innen werden durch die Befreiung nicht entlastet.",[("r2",49)])

# EU
MATCH("r-eu",[21],"Wen vertritt welches Organ?",[["Kommission","Interessen der EU"],["Rat der EU","Interessen der Mitgliedstaaten"],["Europäisches Parlament","Interessen der Unionsbürger*innen"]],"Rat und Parlament sind gemeinsam für die Rechtssetzung zuständig.",[("rv",80),("rv",81),("rv",82)])
MC("r-eu",[21],"Was macht der Europäische Rat?","Politische Zielvorstellungen, kein Rechtssetzungsverfahren",["Beschließt Gesetze","Spricht Urteile","Ist dasselbe wie der Rat der EU"],"Achtung, ähnliches Wording.",[("rv",85)])
TF("r-egmr",[21],"Der EGMR ist eine Institution der EU.",False,"Er sitzt in Straßburg und wacht über die EMRK. Der EuGH sitzt in Luxemburg.",[("rv",84),("rv",83)])
MC("r-egmr",[7],"Wer kann sich an den EGMR wenden?","Jede Einzelperson, die eine EMRK-Verletzung vorbringt",["Nur Staaten","Nur EU-Bürger*innen","Nur Gerichte"],"Auch Mitgliedstaaten können das.",[("rv",84)])

# Soziale Sicherung
MC("r-sh",[7],"Unter welchen Kompetenztatbestand fällt die Sozialhilfe?","Art 12 B-VG, Armenwesen",["Art 10 B-VG","Art 11 B-VG","Art 15 B-VG"],"Grundsatzgesetz Bund, Ausführung und Vollziehung Land.",[("r2",61),("f3",4)])
ORD("r-sh",[],"Bring die Entwicklung der Sozialhilfe in die richtige Reihenfolge.",["Verschiedene Sozialhilfegesetze der Länder","15a-Vereinbarung: Bedarfsorientierte Mindestsicherung","Vereinbarung läuft Ende 2016 aus","Sozialhilfe-Grundsatzgesetz 2019"],"Vom Mindeststandard zum Höchstsatz.",[("r2",61)])
TF("r-sh",[],"Armutsbekämpfung steht als Ziel ausdrücklich im Sozialhilfe-Grundsatzgesetz.",False,"Das Ziel der 15a-Vereinbarung wird dort nicht mehr angeführt. Neu sind integrations- und fremdenpolizeiliche Ziele.",[("r2",63)])
BUCKET("r-prinzipien",[],"Welches Prinzip steckt dahinter?",["Versicherung","Versorgung","Sozialhilfe"],[("Arbeitslosengeld",0),("Familienbeihilfe",1),("Wiener Mindestsicherung",2),("Krankenversicherung",0),("Kinderbetreuungsgeld",1),("Pensionsversicherung",0)],"Das Skript zählt das Kinderbetreuungsgeld zu den Versorgungsleistungen.",[("r2",61),("r2",62),("r2",63)])
MULTI("r-alv",[],"Was muss für Arbeitslosengeld vorliegen?",["Arbeitsfähig","Arbeitswillig","Arbeitslos","Anwartschaft erfüllt"],["Österreichische Staatsbürgerschaft","Kein Vermögen"],"Die Staatsangehörigkeit spielt für die Versicherung keine Rolle.",[("r3",4),("r3",7)])
MC("r-alv",[],"Wie hoch ist der Grundbetrag des Arbeitslosengelds?","55 % des täglichen Nettoeinkommens",["80 %","92 %","100 %"],"92 bis 95 % ist die Notstandshilfe im Verhältnis zum Arbeitslosengeld.",[("r3",15),("r3",18)])
MC("r-schutz",[],"Wie lange gilt der Berufsschutz?","Die ersten 100 Tage",["Die ersten 120 Tage","Ein Jahr","Während des gesamten Bezugs"],"Entgeltschutz: erste 120 Tage 80 %, danach 75 % der Bemessungsgrundlage.",[("r3",9)])
TF("r-nh",[],"Bei Notstandshilfe gibt es weder Berufs- noch Entgeltschutz.",True,"Das Skript sagt es ausdrücklich.",[("r3",17)])
TF("r-nh",[],"Das Einkommen der Partnerin wird auf die Notstandshilfe angerechnet.",False,"Seit 1.7.2018 nicht mehr.",[("r3",17)])
MC("r-nh",[],"Für wie lange wird Notstandshilfe gewährt?","Bis zu 52 Wochen, Folgeanträge unbegrenzt",["Höchstens 20 Wochen","Ein Leben lang automatisch","6 Monate, kein Folgeantrag"],"Darum in der Präsentation der Sozialpolitik: de facto unbefristet.",[("r3",18)])

# ------------------------------------------------------------ Begriffe
for t,x,s in [
 ("Legalitätsprinzip","Art 18 B-VG: Die gesamte staatliche Verwaltung darf nur auf Grund der Gesetze ausgeübt werden.",[("rv",53)]),
 ("Offizialmaxime","Amtswegigkeit: Ist ein Antrag eingebracht, führt die Behörde das Verfahren weiter.",[("r2",14)]),
 ("Parteiengehör","Parteien müssen im Verfahren Stellung nehmen können.",[("r2",14)]),
 ("Säumnisbeschwerde","Beschwerde wegen Verletzung der Entscheidungspflicht, wenn die Behörde nicht rechtzeitig entscheidet.",[("r2",18)]),
 ("Fiskalgeltung","Der Staat muss Grundrechte auch wahren, wenn er privatrechtlich handelt.",[("f5",3)]),
 ("Titel","Rechtskräftige Grundlage für Exekution, etwa Urteil, Vergleich, Zahlungsbefehl.",[("r2",34)]),
 ("Drittschuldner*in","Meist Dienstgeber*in: muss bei Lohnpfändung Auskunft geben und den pfändbaren Betrag leiten.",[("r2",38)]),
 ("Kumulationsprinzip","Im Verwaltungsstrafrecht eine eigene Strafe für jede Übertretung.",[("r2",20)]),
 ("Prioritätsprinzip","Gläubiger*innen werden nach ihrem Rang befriedigt.",[("r2",35)]),
 ("Ordre public","Fremdes Recht wird nicht angewendet, wenn es mit Grundwertungen der österreichischen Rechtsordnung unvereinbar ist (§ 6 IPRG).",[("f3",3)]),
 ("Exszindierungsklage","Klage der Eigentümer*innen, wenn fremde Sachen gepfändet wurden.",[("r2",37)]),
 ("Offizialdelikt","Der Staat muss bei hinreichendem Substrat tätig werden, die Anzeige lässt sich nicht zurücknehmen.",[("f2",8)]),
 ("Verfahrenshilfe","Soll gleiche Chancen auf Rechtsdurchsetzung sichern. Verliert man, sind die Kosten der Gegenseite trotzdem zu ersetzen.",[("r2",24),("f7",3)]),
]: TERM(t,x,s)

# ------------------------------------------------------------ Widersprüche
TRAP("Wie viele Gesetzesinitiativen kommen von der Regierung?","Die Folien sagen bis zu 85 %, die Fernlehre 4 sagt bis zu über 90 %. Merk dir: die große Mehrheit, und frag im Zweifel nach.",[("rv",43),("f4",4)])
TRAP("Zahlungsplan: drei oder fünf Jahre?","Das Recht-Skript nennt als Mindestangebot das Einkommen der folgenden drei Jahre (vor der letzten Novelle fünf). Die MatSi-Präsentation nennt fünf Jahre. Maximallaufzeit 7 Jahre stimmt überall.",[("r2",50),("msp",72)])
TRAP("Bezirksgericht bis 15.000 oder 75.000 Euro?","Die MatSi-Präsentation schreibt „Bis 75.000 €: Verfahren am Bezirksgericht“. Skript und Fernlehre 7: Bezirksgericht bis 15.000 Euro, am Landesgericht ist die Mahnklage bis 75.000 Euro möglich. Für Recht gilt die Skript-Fassung.",[("msp",62),("r2",32),("f7",3)])
TRAP("Wann beginnt die Frist bei Hinterlegung?","Das Skript sagt, Wochenfristen beginnen am Tag der Zustellung und Hinterlegtes gilt mit dem ersten Abholtag als zugestellt. Die Fernlehre rechnet ab dem Tag nach der Hinterlegung. Das Fristende im Beispiel ist der 17. November.",[("r2",43),("r2",44),("f7",5)])
TRAP("Wie aktuell sind die Verfassungsfolien?","Auf der ersten Folie steht „nur bei Interesse, nicht im Detail aktualisiert“. Die Fernlehre 6 sagt aber zu EU: Zur Prüfung müsst ihr nur lernen, was auf den Folien steht. Einzelne Angaben, etwa zum Unabhängigen Verwaltungssenat, sind historisch.",[("rv",1),("f6",1),("rv",19)])
TRAP("Fernlehre 3, Fall Frizzy","Die Musterantwort springt bei den Namen: Frida, Freya, Feya, Friedrich und „Kindesmama“. Inhaltlich zählt: Eine Person macht für das Kind gegen die Geldunterhaltspflichtige geltend.",[("f3",6),("f3",7)])
TRAP("Fernlehre 7, R. Luger","Im Text wechseln er und sie für dieselbe Person. Das ändert am Rechtsweg nichts.",[("f7",4)])
