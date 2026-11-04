from dsl import Course
c = Course("sopol", name="Sozialpolitische und ökonomische Bezüge", short="SoPol", term="WS 2026/27", lecturer="Dominik Klaus, Maddalena Lamura",
           exams=[dict(id="p", label="Prüfung", date="2026-11-30")], accent="#8C2F39", lineTitle="Die Einheiten", stopWord="Einheit",
           openName="Kernfrage", openNamePl="Kernfragen", openLead="Die Präsentationen sind das Relevanteste. Beantworte die Fragen frei, vergleiche danach mit den Punkten von den Folien.",
           ranks=[[0,"Wohlfahrtsneuling"],[100,"Flötenrichter*in"],[300,"Esping-Andersen-Kenner*in"],[650,"Umverteiler*in"],[1100,"Marienthal-Forscher*in"],[1700,"Gini-Profi"],[2500,"Sozialstaatsarchitekt*in"]],
           modes=["chains","blitz"], source="Präsentationen der Einheiten 1 bis 6. Zusatztexte und Webseiten sind als Zusatz gekennzeichnet und kommen seltener. Vier Einheiten fehlen noch.",
           upcoming="Noch 4 Einheiten: Armut (Gastvortrag), Klima und Sozialpolitik, Gesundheit und Ungleichheit, Wiederholung.")
CH,T,MC,TF,ORD,MATCH,MULTI,BUCKET,CHAIN,CALC,OPEN,TERM,TRAP,TL,PERSON = c.CH,c.T,c.MC,c.TF,c.ORD,c.MATCH,c.MULTI,c.BUCKET,c.CHAIN,c.CALC,c.OPEN,c.TERM,c.TRAP,c.TL,c.PERSON

CH("e1","Einheit 1: Was ist Sozialpolitik?","21.09.","Sozialstaat und Soziale Arbeit",["s1"])
CH("e2","Einheit 2: Gerechtigkeit und Wohlfahrtsstaaten","23.09.","Die Flöte, Bismarck, Esping-Andersen",["s2"])
CH("e3","Einheit 3: Der österreichische Sozialstaat","05.10.","Einnahmen, Ausgaben, Umverteilung",["s3"])
CH("ea","Armut: Gastvortrag Martin Schenk","15.10., Folien fehlen","Bis dahin nur aus Zusatzquellen",["zw"])
CH("e4","Einheit 4: Arbeit und Arbeitslosigkeit","19.10.","Marienthal, Jahoda, working poor",["s4"])
CH("e5","Einheit 5: Arbeitsmarktpolitik","21.10.","Von Vollbeschäftigung zu Workfare",["s5"])
CH("e6","Einheit 6: Vermögen","28.10.","Gini, Steuern, Überreichtum",["s6"])
CH("ep","Standpunkte","Zusatzquelle","Was Parteien 2024 sagten",[])
CH("ek","Klima und Sozialpolitik","09.11., folgt noch","Folien kommen noch",[],pending=True)
CH("eg","Gesundheit und Ungleichheit","18.11., folgt noch","Folien kommen noch",[],pending=True)
CH("ew","Wiederholung und Fallbesprechung","23.11., folgt noch","Folien kommen noch",[],pending=True)

T("s-rahmen","e1","Rahmenbedingungen im Modul","Das Modul hat vier Teile mit gemeinsamer Note: Materielle Sicherung, Rechtliche Grundlagen, Sozialpolitik und Fallanalyse, je 25 von 100 Punkten. Die Prüfung in Sozialpolitik steht am 30.11. im Semesterplan.",[("s1",2),("s1",8)])
T("s-def","e1","Was Sozialpolitik ist","Eng gefasst: staatliche Sozialleistungen. Weit gefasst: Interventionsform zur sozialen Absicherung und zur Gestaltung von Lebensbedingungen. Sie will Risiken vorbeugen, zur Bewältigung befähigen, Wirkungen ausgleichen und Lebenslagen sichern.",[("s1",4),("s1",5)])
T("s-staat","e1","Was der Sozialstaat ist","Staatliche Einrichtungen, Steuerung und Normen, die Lebensrisiken einer kapitalistischen Marktwirtschaft innerhalb dieser Wirtschaft politisch bearbeiten. Der Markt versorgt mit Gütern, erzeugt aber auch Risiken, die er selbst nicht regulieren kann.",[("s1",6)])
T("s-sa","e1","Soziale Arbeit und Sozialpolitik","Soziale Arbeit ist zentraler Bestandteil der Sozialpolitik, hängt stark von Staat und Politik ab und verändert sich mit dem Sozialstaat und seinen Paradigmen.",[("s1",7)])
T("s-bettinger","e1","Aktivierender Staat und Soziale Arbeit","Bettinger: Seit den 1970ern wandelt sich der Sozialstaat zum marktliberalen Modell. Der aktivierende Staat formt ökonomische und moralische Subjekte. Soziale Arbeit ist daran beteiligt und nicht bloß Opfer dieser Entwicklung.",[("zb",2),("zb",4),("zb",5)])
T("s-floete","e2","Die Flöte","Anna kann spielen, Bert ist arm, Carla hat sie gebaut. Jedes Kind steht für ein anderes Gerechtigkeitskonzept: Anna für Utilitarismus, Bert für Bedarf, Carla für Leistung und Besitz. Unterschiedliche politische Philosophien bauen auf unterschiedlichen Konzepten.",[("s2",3),("s2",4)])
T("s-gerecht","e2","Gerechtigkeitskonzepte","Bedarfsgerechtigkeit: Sozialismus, Sicherung des Existenzminimums. Leistungsgerechtigkeit: Liberalismus, aber wer bewertet Leistung? Besitzstandsgerechtigkeit: Konservativismus, Nozick. Weitere: Startchancen-, Generationen-, Verteilungs- und Umweltgerechtigkeit.",[("s2",4),("s2",5),("s2",6),("s2",7),("s2",8),("s2",9)])
T("s-bismarck","e2","Anfänge unter Bismarck","Erstes Sozialversicherungssystem um 1880: Unfälle, Krankheit, Arbeitsunfähigkeit, Altersarmut. Die Beweggründe sind umstritten: Fortbestand der Arbeiterschaft, sozialer Friede, Zugeständnisse aus Angst vor Aufständen.",[("s2",11),("s2",12)])
T("s-entw","e2","Drei Phasen","18./19. Jahrhundert: Industrialisierung und erste kollektive Organisation sozialer Risiken. 20. Jahrhundert: Institutionalisierung, Grundlage ist die Erwerbsarbeit. 20./21. Jahrhundert: neoliberal turn, Aktivierung und workfare statt welfare.",[("s2",10),("s2",13),("s2",14),("s2",15)])
T("s-regime","e2","Wohlfahrtsregime nach Esping-Andersen","Dekommodifizierung fragt: Wie unabhängig ist die Existenz vom Verkauf der Arbeitskraft? Stratifizierung fragt: Wie beeinflusst Sozialpolitik die Ungleichheit? Liberal gering, konservativ mittel, sozialdemokratisch hoch.",[("s2",18),("s2",19)])
T("s-at","e2","Österreich als konservativer Wohlfahrtsstaat","Ausgelegt auf Statuserhalt. Ansprüche über Erwerbsarbeit oder als Mitversicherte. Basis ist der männliche Alleinverdiener mit lebenslanger Vollzeit. Familie spielt eine zentrale Rolle. Deshalb anfällig für Teilzeit und Scheidungen.",[("s2",20),("s2",23)])
T("s-kritik","e2","Kritik an Esping-Andersen","Geringe Fallzahl, Fokus auf Nord- und Mitteleuropa. Postkommunistische Staaten passen nicht eindeutig. Gender-blind: Erwünschtheit weiblicher Erwerbsbeteiligung, Auszahlung von Familienleistungen an Frauen.",[("s2",21)])
T("s-krise","e2","Neuere Entwicklungen","Mehr Erwerbsbeteiligung von Frauen, prekäre Arbeit, Erosion der Normalerwerbsbiographie, Digitalisierung, mehr Scheidungen. Reaktion: Einsparungen, Aktivierung, Verschiebung der Verantwortung. Corona zeigte Lücken und ungleiche Sorgearbeit.",[("s2",22),("s2",23),("s2",24)])
T("s-talos","e2","Zusatztext: Profil des österreichischen Sozialstaats","Tálos und Obinger: Sozialversicherung an Erwerbsarbeit gebunden, Äquivalenzprinzip und Lebensstandardsicherung, berufsgruppenspezifische Fragmentierung, Subsidiarität der Sozialhilfe. Der Schutz nichterwerbstätiger Frauen hängt an der Stabilität der Ehe.",[("zt",7),("zt",8)])
T("s-nullmeier","e2","Zusatztext: Begründungen des Wohlfahrtsstaats","Nullmeier: Debatte zwischen Rechtfertigung und Kritik. Zentrale Figuren sind Modernisierung und Globalisierung, ökonomische Effizienz, Gerechtigkeit und Gleichheit, Freiheit und Eigenverantwortung, Solidarität. Neoliberale Argumente wurden von der Kritik zur Begründung des Rückbaus.",[("zn",1),("zn",9)])
T("s-umvert","e3","Wozu Umverteilung?","Ausgleich von Marktversagen, Teilhabe für niedrige Einkommen, zu große Ungleichheit ist politisch und ethisch nicht wünschenswert. Neuere Studien finden einen negativen Zusammenhang von Ungleichheit und Wachstum. Wilkinson und Pickett: In egalitären Gesellschaften geht es Armen und Reichen besser.",[("s3",7),("s3",8)])
T("s-geld","e3","Einnahmen und Ausgaben","Einnahmen: Steuern auf Konsum, Arbeit und Kapital, dazu Versicherungsbeiträge. Ausgaben: Geldleistungen wie Pensionen und Arbeitslosengeld, Sachleistungen wie Krankenhäuser und Bildungseinrichtungen. Deine Notiz: Steuern sind nicht zweckgebunden, Versicherungsbeiträge schon.",[("s3",9)])
T("s-anteile","e3","Wofür das Geld ausgegeben wird","Sozialausgaben 2024: 157 Milliarden Euro, 33,3 % des BIP. Alter 46,1 %, Gesundheit 27,3 %, Familie 9 %, Arbeitslosigkeit 4,7 %, Wohnen und soziale Ausgrenzung 2,5 %. Finanzierung: 40 % Steuern, 33 % Arbeitgeberbeiträge, 25 % Beiträge der Geschützten.",[("s4",2),("s3",11),("s3",12)])
T("s-bed","e3","Bedürftigkeitsprüfung","Nur 9,3 % der Sozialleistungen 2024 haben eine Bedürftigkeitsprüfung. Sie spielt bei Wohnen und sozialer Ausgrenzung mit 87 % eine große Rolle, bei Krankheit kaum.",[("s3",13)])
T("s-vert","e3","Verteilungswirkung","Leistungen für Arbeitslosigkeit und Sozialhilfe gehen zu 75 % an niedrige Einkommen, Wohnen zu 51 %, Familien zu 40 %. Familienleistungen sind mehrheitlich universell. Die Armutsgefährdung wäre ohne Transfers viel höher.",[("s3",16),("s3",18),("s3",19),("s3",20),("s3",22)])
T("s-armut","ea","Zahlen zur Armut","EU-SILC 2025 laut Armutskonferenz: 1.441.000 Menschen sind armutsgefährdet, das sind 15,9 %. Die Schwelle liegt bei 1.827 Euro monatlich für eine Person. Armuts- oder ausgrenzungsgefährdet sind 1.699.000 Menschen, 18,8 %.",[("@armut",0)])
T("s-messung","ea","Armut messen","Badelt und Heitzmann: Traditionelle Armutsmaße reichen in Vielfachkrisen nicht aus, es braucht breitere Indikatoren. Dilemma: Treffsicherheit gelingt erst in Einzelfallentscheidungen, wie sie die Sozialarbeit fällt. Darum wird präventive Sozialpolitik wichtiger.",[("zw",1)])
T("s-widerspruch","e4","Widersprüche der Arbeitsgesellschaft","Arbeit bleibt zentraler Modus der Vergesellschaftung, auch wenn ihr die Arbeit ausgeht. Sozialpolitik hält am Normalarbeitsverhältnis fest, obwohl es erodiert. Arbeitswilligkeit ist Bedingung auch für Versicherungsleistungen.",[("s4",6)])
T("s-vier","e4","4-in-1-Perspektive","Frigga Haug: Erwerbsarbeit, Sorgearbeit, Freiwilligenarbeit, Eigenarbeit. Der Fokus auf Erwerbsarbeit blendet aus, was für den Zusammenhalt notwendig ist.",[("s4",7),("s4",8)])
T("s-prekaer","e4","Atypisch und prekär","Atypisch ist Teilzeit, geringfügig, befristet oder Kurz- und Leiharbeit. Der Sozialstaat reagiert nur unzureichend. Arbeit sichert immer seltener die Existenz: working poor.",[("s4",9)])
T("s-alo","e4","Arbeitslosigkeit definieren","EU: In der Woche nicht erwerbstätig, aktiv suchend, binnen 2 Wochen verfügbar. AMS: am Stichtag gemeldet. Langzeitbeschäftigungslos: mindestens zwölf Monate beim AMS, Schulungen zählen mit.",[("s4",13)])
T("s-marienthal","e4","Marienthal und Jahoda","Die Studie zeigt: Arbeitslosigkeit trifft Sinnerleben, Gemeinschaft, Tagesstruktur; dazu Stigma. Jahodas latente Funktionen der Erwerbsarbeit: Zeitstruktur, regelmäßige Tätigkeit, Status und Identität, soziale Kontakte, Beitrag zu kollektiven Zielen.",[("s4",17),("s4",18)])
T("s-amp","e5","Geschichte der Arbeitsmarktpolitik","1960er: Vollbeschäftigung, Institutionalisierung. 1970er und 1980er: Ölkrisen, Austro-Keynesianismus, Bildungsexpansion. 1990er: Aktivierung, Privatisierung. 2000er: schlanker Staat, schärfere Zumutbarkeit, workfare. 2020 bis 2024: Corona-Programme, seit 2024 wieder Einsparungen.",[("s5",5),("s5",6),("s5",7)])
T("s-ams","e5","Das AMS","Ziel laut § 29 AMSG: Arbeitslosigkeit verhüten und beseitigen, Angebot und Nachfrage zusammenführen, die wirtschaftliche Existenz während der Arbeitslosigkeit sichern.",[("s5",8)])
T("s-aktiv","e5","Passiv, aktiv, aktivierend","Passiv: Leistungen zur Existenzsicherung. Aktiv: bessere Integration und Matching, mit Beschäftigung, Qualifizierung, Unterstützung. Aktivierend: Beide sollen die Aufnahme von Erwerbsarbeit fördern, auch durch Abbau struktureller Barrieren im Sinn von Flexibilisierung.",[("s5",9),("s5",10),("s5",11),("s5",13)])
T("s-alg","e5","Arbeitslosengeld und Notstandshilfe","Arbeitslosengeld: SV-pflichtige Beschäftigung, arbeitsfähig und -willig, 55 % des Nettogehalts, grundsätzlich 20 Wochen. Notstandshilfe: 92 bis 95 % des Arbeitslosengelds, de facto unbefristet, Notlage regelmäßig nachzuweisen.",[("s5",12)])
T("s-soeb","e5","Sozialökonomische Betriebe","Befristete Arbeitsplätze für Benachteiligte, etwa Langzeitbeschäftigungslose, Ältere, Personen mit Behinderung. Ziel ist die Integration in den regulären Arbeitsmarkt. Deine Notiz: Viele Fixangestellte dort sind Sozialarbeiter*innen.",[("s5",15)])
T("s-garantie","e5","Jobgarantie oder Grundeinkommen","Marienthal reversed: Jobgarantie für Langzeitarbeitslose in Gramatneusiedl mit 100 % Lohnförderung. Zur Diskussion stehen garantierte Beschäftigung und bedingungsloses Grundeinkommen von 1.000 Euro monatlich.",[("s5",16),("s5",17)])
T("s-gini","e6","Gini-Koeffizient","Maß für Ungleichheit von 0 bis 1. 0 heißt völlige Gleichverteilung, 1 heißt, eine Person besitzt alles. In Österreich ist das Einkommen vergleichsweise gleich verteilt, das Vermögen sehr ungleich.",[("s6",7),("s6",8),("s6",9)])
T("s-haeq","e6","Haushaltsäquivalenzeinkommen","Macht Armut vergleichbar, weil Haushalte Größenvorteile haben: 1,0 für die erste erwachsene Person, 0,5 für jede weitere über 14, 0,3 für jedes Kind unter 14. Problematisch bei WGs ohne gemeinsamen Haushalt.",[("s6",10)])
T("s-verm","e6","Vermögen und Steuern","Vermögen ist sehr ungleich verteilt, besonders bei Immobilien: 50,1 % der Haushalte haben keine. Arbeit und Konsum tragen am meisten bei, vermögensbezogene Steuern nur 3,1 %. Vermögensteuer bis 1993, Erbschaftssteuer bis 2008; der VfGH hob sie 2007 aus formalen Gründen auf.",[("s6",6),("s6",11),("s6",12),("s6",14)])
T("s-vorschlag","e6","Überreichtum und Reformvorschläge","Fessler und Schürz schlagen Grundsteuer, Erbschaftssteuer und Überreichtumssteuer vor. Überreichtum heißt: Vermögen wird zu politischer und wirtschaftlicher Macht. Die Debatte über Legitimität dreht sich sonst meist um Armutsbetroffene.",[("s6",16),("s6",17)])
T("s-falter","e6","Zusatztext: Falter zur Nationalbank-Studie","Die OeNB ersuchte die Autoren, sich auf den analytisch-deskriptiven Teil zu beschränken, sie sagten ihre Teilnahme ab. Immobilieneigentum beginnt erst in der oberen Hälfte der Vermögensverteilung. Empfehlung: Besteuerung leistungsloser Einkommen.",[("zf",1)])
T("s-stand","ep","Standpunkte 2024","Die Wahlkabine zur Nationalratswahl 2024 zeigt, wie Parteien sozialpolitische Fragen beantwortet haben. Das hilft, Gerechtigkeitskonzepte politisch einzuordnen, ist aber eine Selbstauskunft aus dem Wahlkampf.",[("@wk",0)])

OPEN(1,"Einheit 1","Was ist Sozialpolitik, was der Sozialstaat, und wie stehen Soziale Arbeit und Sozialpolitik zueinander?","Absicherung und Gestaltung; politische Bearbeitung von Marktrisiken; Soziale Arbeit als Teil davon.",
 [("Eng: staatliche Sozialleistungen. Weit: Interventionsform zur Absicherung und Gestaltung von Lebensbedingungen und Partizipationschancen.",[("s1",4)]),
  ("Vier Ziele: vorbeugen, befähigen, ausgleichen, Lebenslagen sichern.",[("s1",5)]),
  ("Sozialstaat: bearbeitet Lebensrisiken und Folgen einer kapitalistischen Marktwirtschaft politisch.",[("s1",6)]),
  ("Soziale Arbeit ist zentraler Bestandteil, in hohem Maß politikabhängig und verändert sich mit dem Sozialstaat.",[("s1",7)])],"e1")
OPEN(2,"Einheit 2","Welche Gerechtigkeitskonzepte kennst du? Ordne sie der Flötengeschichte und politischen Strömungen zu.","Bedarf, Leistung, Besitzstand, dazu Startchancen und mehr.",
 [("Bert steht für Bedarf: Sozialismus, Sicherung des Existenzminimums, oft auf Haushalte bezogen.",[("s2",3),("s2",4),("s2",5)]),
  ("Liberalismus steht für Leistungsgerechtigkeit: Wer definiert Leistung? Unbezahlte Arbeit fällt heraus, Erbschaften sind umstritten.",[("s2",4),("s2",6)]),
  ("Konservativismus steht für Besitzstandsgerechtigkeit: Nozicks Anspruchstheorie.",[("s2",4),("s2",7)]),
  ("Anna steht genauer betrachtet für Utilitarismus, die Maximierung des Gesamtnutzens.",[("s2",4)]),
  ("Startchancengerechtigkeit: gleiche Chancen für selbstbestimmte Lebensführung. Dazu Generationen-, Verteilungs- und Umweltgerechtigkeit.",[("s2",8),("s2",9)])],"e2")
OPEN(3,"Einheit 2","Beschreibe die drei Wohlfahrtsregime nach Esping-Andersen und die Kritik daran.","Liberal, konservativ, sozialdemokratisch nach Dekommodifizierung und Stratifizierung.",
 [("Dekommodifizierung und Stratifizierung sind die beiden Maßstäbe.",[("s2",18)]),
  ("Liberal: geringe steuerfinanzierte Grundsicherung, private Zusatzversicherung, gering dekommodifiziert. USA, Großbritannien.",[("s2",19)]),
  ("Konservativ: statusgebunden, beitragsfinanziert, Kirche und Familie, mittlere Dekommodifizierung. Österreich, Deutschland.",[("s2",19)]),
  ("Sozialdemokratisch: umfassend, steuerfinanziert, hoch dekommodifiziert. Schweden, Dänemark.",[("s2",19)]),
  ("Kritik: geringe Fallzahl, Nord- und Mitteleuropa, Osteuropa unklar, gender-blind.",[("s2",21)])],"e2")
OPEN(4,"Einheit 2","Warum ist der österreichische Sozialstaat konservativ und welche Probleme bringt das?","Statuserhalt über Erwerbsarbeit und Familie, anfällig für Teilzeit und Scheidung.",
 [("Ausgelegt auf Statuserhalt.",[("s2",20)]),
  ("Ansprüche durch Erwerbsarbeit oder als Mitversicherte.",[("s2",20)]),
  ("Basis ist männlicher Alleinverdiener mit lebenslanger Vollzeit, das Normalarbeitsverhältnis.",[("s2",20)]),
  ("Familie spielt in der Wohlfahrtserbringung eine zentrale Rolle.",[("s2",20)]),
  ("Anfällig gegenüber hohen Teilzeitquoten und Scheidungsraten.",[("s2",23)])],"e2",
 deep=[("Tálos und Obinger: Der Schutz nichterwerbstätiger Frauen hängt von der Stabilität der Ehe ab.",[("zt",7)])])
OPEN(5,"Einheit 3","Wie finanziert sich der Sozialstaat, wofür gibt er Geld aus, und wer profitiert?","40 % Steuern; Alter und Gesundheit dominieren; Arbeitslosigkeit und Sozialhilfe wirken am stärksten umverteilend.",
 [("Einnahmen: Steuern auf Konsum, Arbeit und Kapital sowie Versicherungsbeiträge.",[("s3",9)]),
  ("Finanzierung 2024: 40 % Steuermittel, 33 % Arbeitgeber, 25 % geschützte Personen.",[("s3",11)]),
  ("Ausgaben: Alter 46 %, Krankheit 27,6 %, Arbeitslosigkeit 4,7 %, Wohnen und Ausgrenzung 2,5 %.",[("s3",12)]),
  ("Verteilung: Arbeitslosigkeit und Sozialhilfe zu 75 % an niedrige Einkommen, Familien zu 40 %.",[("s3",16),("s3",20)]),
  ("Nur 9,3 % aller Leistungen sind bedürftigkeitsgeprüft.",[("s3",13)])],"e3")
OPEN(6,"Einheit 4","Welche Funktionen hat Arbeit, und was folgt aus Arbeitslosigkeit?","Jahoda: manifest Gelderwerb, dazu fünf latente Funktionen.",
 [("Marienthal: Sinnerleben, Gemeinschaft, Tagesstruktur leiden.",[("s4",17)]),
  ("Latent nach Jahoda: Zeitstruktur, regelmäßige Tätigkeit, Status und Identität, soziale Kontakte, Beitrag zu kollektiven Zielen.",[("s4",18)]),
  ("Soziales Stigma der „faulen Arbeitslosen“.",[("s4",17)]),
  ("Aktive Arbeitsmarktpolitik sollte auch die Qualität der Arbeit berücksichtigen.",[("s4",17)])],"e4")
OPEN(7,"Einheit 4","Wie unterscheiden sich die Definitionen von Arbeitslosigkeit?","EU fragt, AMS zählt, Langzeitbeschäftigungslosigkeit fasst weiter.",
 [("EU: In der abgefragten Woche nicht erwerbstätig, aktiv suchend, binnen 2 Wochen verfügbar.",[("s4",13)]),
  ("AMS: am Stichtag letzter Werktag im Monat als arbeitslos vorgemerkt.",[("s4",13)]),
  ("Langzeitbeschäftigungslos: mindestens zwölf Monate beim AMS, Schulungen und Lehrstellensuche zählen gleich.",[("s4",13)])],"e4")
OPEN(8,"Einheit 5","Wie hat sich die österreichische Arbeitsmarktpolitik verändert? Welche Umstände führten zu Verschärfungen?","Von Vollbeschäftigung über Aktivierung zu workfare.",
 [("1960er: Vollbeschäftigung, Institutionalisierung der Arbeitsmarktverwaltung.",[("s5",5)]),
  ("1970er und 1980er: Ölkrisen, aktive Arbeitsmarktpolitik, Austro-Keynesianismus, Rolle der Sozialpartnerschaft.",[("s5",5)]),
  ("1990er: strukturelle Arbeitslosigkeit und Flexibilisierung, hohe Kosten, Einsparungen in der sozialen Sicherung.",[("s5",6)]),
  ("2000er: schlanker Staat, Nulldefizit, schärfere Zumutbarkeit, Individualisierung der Verantwortung.",[("s5",6)]),
  ("Nach 2008: Prekarisierung, Corona-Programme, seit 2024 wieder Einsparungen.",[("s5",7)])],"e5")
OPEN(9,"Einheit 5","Was ist passive, aktive und aktivierende Arbeitsmarktpolitik?","Geld, Integration, und der Druck zur Aufnahme von Erwerbsarbeit.",
 [("Passiv: Leistungen zur Existenzsicherung wie Arbeitslosengeld und Notstandshilfe.",[("s5",9),("s5",12)]),
  ("Aktiv: Beschäftigung, Qualifizierung, Unterstützung, etwa Lohnbeihilfen oder Kurse.",[("s5",9),("s5",13)]),
  ("Aktivierend: Beide sollen die Aufnahme von Erwerbsarbeit fördern, auch durch Abbau von Barrieren im Sinn von Flexibilisierung.",[("s5",11)])],"e5")
OPEN(10,"Einheit 6","Was zeigt die Verteilung von Vermögen in Österreich, und welche Steuern werden vorgeschlagen?","Vermögen sehr ungleich, Steuern gering; Grund-, Erbschafts-, Überreichtumssteuer.",
 [("Gini: 0 Gleichverteilung, 1 eine Person besitzt alles.",[("s6",7)]),
  ("Einkommen vergleichsweise gleich verteilt, Vermögen sehr ungleich, besonders Immobilien.",[("s6",6),("s6",9),("s6",11)]),
  ("Arbeit und Konsum werden am stärksten besteuert, die Mehrheit wünscht Steuern auf Vermögen und klimaschädliches Verhalten.",[("s6",6)]),
  ("Vorschläge: Grundsteuer, Erbschaftssteuer, Überreichtumssteuer.",[("s6",16)]),
  ("Überreichtum: Vermögen wird zu politischer und wirtschaftlicher Macht.",[("s6",17)])],"e6")

# Karten
MC("s-def",[1],"Welche Ziele nennen Bäcker et al. für Sozialpolitik?","Vorbeugen, befähigen, ausgleichen, Lebenslagen sichern",["Nur Geldleistungen auszahlen","Marktpreise festlegen","Arbeitslosigkeit verbieten"],"Vier Teile: Risiken vorbeugen, zur Bewältigung befähigen, Wirkungen ausgleichen, Lebenslage sichern.",[("s1",5)])
TF("s-staat",[1],"Der Markt kann alle sozialen Risiken selbst regulieren, die er erzeugt.",False,"Genau deshalb gibt es den Sozialstaat.",[("s1",6)])
MULTI("s-sa",[1],"Was gilt laut Bettinger für Soziale Arbeit?",["Zentraler Bestandteil von Sozialpolitik","In hohem Maß staatsabhängig","Verändert sich mit sozialpolitischen Paradigmen"],["Völlig unabhängig von Politik","Ersetzt den Sozialstaat"],"Darum lohnt der Blick auf Politik auch für die Fallarbeit.",[("s1",7)])
TF("s-bettinger",[],"Laut Bettinger ist Soziale Arbeit nur Opfer einer Instrumentalisierung durch die Sozialpolitik.",False,"Das würde zu kurz greifen, Soziale Arbeit ist daran beteiligt.",[("zb",5)])
MATCH("s-floete",[2],"Wer steht für was?",[["Anna: kann spielen","Utilitarismus"],["Bert: ist arm","Bedarfsgerechtigkeit"],["Carla: hat sie gebaut","Leistung und Besitz"]],"Nach Sen. Die Folie ordnet Anna genauer dem Utilitarismus zu.",[("s2",3),("s2",4)])
BUCKET("s-gerecht",[2],"Welches Konzept steckt dahinter?",["Bedarf","Leistung","Besitzstand","Startchancen"],[("Absicherung des Existenzminimums",0),("Der Markt bestimmt den Wert",1),("Nozicks Anspruchstheorie",2),("Gleiche Bildungswege",3),("Ungleiches Vermögen ist gerecht, weil gerecht erworben",2),("Steuernachlässe für Haushalte",0)],"Unterschiedliche Annahmen führen zu unterschiedlichen Geltungsansprüchen.",[("s2",5),("s2",6),("s2",7),("s2",8)])
MATCH("s-gerecht",[2],"Welche Strömung setzt worauf?",[["Sozialismus","Bedarfsgerechtigkeit"],["Liberalismus","Leistungsgerechtigkeit"],["Konservativismus","Besitzstandsgerechtigkeit"]],"Die Folie 4 der Einheit 2 stellt das so zusammen.",[("s2",4)])
MC("s-gerecht",[2],"Was ist das Problem an Leistungsgerechtigkeit?","Viele Leistungen laufen nicht über den Markt, etwa Sorgearbeit",["Sie ist verboten","Sie gilt nur für Reiche","Sie kommt nur in Schweden vor"],"Auch der Zusammenhang von Leistung und Vermögen ist umstritten, etwa bei Erbschaften.",[("s2",6)])
MC("s-bismarck",[],"Worauf konzentrierte sich die Versicherung unter Bismarck?","Unfälle, Krankheit, Arbeitsunfähigkeit, Altersarmut",["Wohnen und Bildung","Kinderbetreuung","Klima und Mobilität"],"Das Zitat zeigt ein Motiv: die arbeitenden Klassen für den Staat gewinnen.",[("s2",11),("s2",12)])
ORD("s-entw",[],"Bring die Phasen in die richtige Reihenfolge.",["Industrialisierung, erste Unfallversicherung","Institutionalisierung sozialer Sicherung","Neoliberal turn: workfare statt welfare"],"18./19., 20., 20./21. Jahrhundert.",[("s2",15)])
BUCKET("s-regime",[3],"Welches Regime?",["Liberal","Konservativ","Sozialdemokratisch"],[("USA",0),("Großbritannien",0),("Österreich",1),("Deutschland",1),("Schweden",2),("Dänemark",2),("Private Zusatzversicherungen",0),("Statusgebunden, beitragsfinanziert",1),("Umfassend, steuerfinanziert",2)],"Es gibt nicht nur mehr oder weniger Staat, sondern verschiedene Varianten.",[("s2",19)])
BUCKET("s-regime",[3],"Was ist in welchem Regime zentral für die Wohlfahrtsproduktion?",["Markt","Familie","Staat"],[("Liberales Regime",0),("Konservatives Regime",1),("Sozialdemokratisches Regime",2)],"So fasst Valina die Kategorien zusammen. Die Präsentation von MatSi zeigt dieselbe Einteilung wie SoPol.",[("msp",3)])
MC("s-regime",[3],"Was bedeutet Dekommodifizierung?","Existenz und Teilhabe werden unabhängiger vom Verkauf der Arbeitskraft",["Waren werden billiger","Der Staat verkauft Betriebe","Menschen arbeiten mehr"],"Stratifizierung fragt dagegen, wie Sozialpolitik die Gesellschaftsstruktur beeinflusst.",[("s2",18)])
MC("s-at",[4],"Worauf baut der österreichische Sozialstaat auf?","Männlicher Alleinverdiener, lebenslange Vollzeit",["Bedingungsloses Einkommen","Private Vorsorge für alle","Umfassende steuerfinanzierte Leistungen"],"Das Normalarbeitsverhältnis erodiert aber.",[("s2",20)])
TF("s-at",[4],"Der österreichische Sozialstaat ist anfällig für hohe Teilzeitquoten und Scheidungsraten.",True,"Basis sind Vollzeiterwerbsarbeit und stabile heteronormative familiäre Verhältnisse.",[("s2",23)])
MULTI("s-kritik",[3],"Was wird an Esping-Andersen kritisiert?",["Geringe Fallzahl","Fokus auf Nord- und Mitteleuropa","Gender-blind"],["Zu viele Länder","Zu wenige Regime in Afrika untersucht, sonst perfekt"],"Postkommunistische Sozialstaaten lassen sich keinem Typ eindeutig zuordnen.",[("s2",21)])
MULTI("s-krise",[],"Was erodiert die Normalerwerbsbiographie?",["Prekäre Beschäftigung","Niedriglohnsegment","Digitalisierung"],["Mehr Kollektivverträge","Weniger Teilzeit"],"Dazu höhere Scheidungsraten und geringere Fertilität.",[("s2",22)])
MC("s-talos",[4],"Was bedeutet Äquivalenzprinzip?","Beitragshöhe und -dauer bestimmen die Höhe der Leistung",["Alle bekommen gleich viel","Nur Bedürftige bekommen Geld","Leistungen werden verlost"],"Es reproduziert Einkommensungleichheit, auch zwischen den Geschlechtern.",[("zt",7)])
MC("s-nullmeier",[],"Was versprach das neoliberale Argument laut Nullmeier?","Trickle-down: Marktpolitik verbessert am Ende auch die Lage der Schlechtergestellten",["Vollbeschäftigung durch Staatsbetriebe","Mehr Gewerkschaften","Höhere Sozialquote"],"Seit der Weltfinanzkrise häufen sich die Stimmen dagegen.",[("zn",9)])
MULTI("s-umvert",[5],"Welche Gründe für Umverteilung nennen die Folien?",["Ausgleich von Marktversagen","Teilhabe niedriger Einkommen","Große Ungleichheit ist nicht wünschenswert"],["Staat braucht mehr Beamte","Reiche wünschen es"],"Neuere Studien finden zudem einen negativen Zusammenhang von Ungleichheit und Wachstum.",[("s3",7)])
TF("s-umvert",[],"Wilkinson und Pickett fanden: In egalitären Gesellschaften geht es Armen und Reichen besser.",True,"Mögliche Erklärung: Statuskonkurrenz.",[("s3",8)])
BUCKET("s-geld",[5],"Geld- oder Sachleistung?",["Geldleistung","Sachleistung"],[("Pensionen",0),("Arbeitslosengeld",0),("Krankenhäuser",1),("Bildungseinrichtungen",1)],"Deine Notiz: Hohe Sachleistungen bei Gesundheit, weil Krankheit eher als unverschuldet gilt.",[("s3",9),("s3",10)])
TF("s-geld",[5],"Versicherungsbeiträge sind zweckgebunden, Steuern nicht.",True,"Deine Notiz aus der Einheit.",[("s3",9)])
MC("s-anteile",[5],"Wie groß ist der Anteil von Alter an den Sozialausgaben?","Rund 46 %",["Rund 5 %","Rund 27 %","Rund 80 %"],"Gesundheit rund 27 %.",[("s3",12),("s4",2)])
MC("s-anteile",[5],"Wie viel machen Wohnen und soziale Ausgrenzung aus?","2,5 %",["25 %","10 %","46 %"],"Ein sehr kleiner Teil, über den aber viel diskutiert wird.",[("s3",12),("s4",2)])
MC("s-anteile",[5],"Woher kommt der größte Anteil der Finanzierung?","Allgemeine Steuermittel, 40 %",["Arbeitgeber, 60 %","Vermögensteuern, 40 %","Spenden, 10 %"],"Dazu 33 % Arbeitgeber und 25 % geschützte Personen.",[("s3",11)])
TF("s-bed",[5],"Die meisten Sozialleistungen sind bedürftigkeitsgeprüft.",False,"Nur 9,3 %. Deine Notiz: spielt gesamt eine geringe Rolle.",[("s3",13)])
MATCH("s-vert",[5],"Welcher Anteil geht an niedrige Einkommen?",[["Arbeitslosigkeit und Sozialhilfe","75 %"],["Wohnen","51 %"],["Familien","40 %"]],"Hier erkennt man die stärkste Umverteilung.",[("s3",16),("s3",18),("s3",20)])
TF("s-vert",[],"Die Mehrheit der Familienleistungen ist universell.",True,"Dafür ist der Anteil der Sachleistungen, also Kinderbetreuung, EU-weit niedrig.",[("s3",19)])
MC("s-armut",[],"Wie viele Menschen sind laut Armutskonferenz (EU-SILC 2025) armutsgefährdet?","1.441.000, also 15,9 %",["144.000, also 1,6 %","3.000.000, also 33 %","800.000, also 9 %"],"Zusatzquelle. Die Schwelle: 1.827 Euro monatlich.",[("@armut",0)])
MC("s-armut",[],"Wie hoch ist die Armutsgefährdungsschwelle für eine Person?","1.827 Euro",["1.229,89 Euro","1.308 Euro","2.630 Euro"],"Die anderen Zahlen sind WMS und Existenzminimum: darunter liegt das, was Menschen tatsächlich bekommen.",[("@armut",0),("r2",39)])
TF("s-messung",[],"Badelt und Heitzmann halten traditionelle Armutsmaße in Krisen für ausreichend.",False,"Sie plädieren für breitere Indikatoren und präventive Sozialpolitik.",[("zw",1)])
MC("s-messung",[],"Welche drei Grundanliegen nennt der Text für Sozialpolitik?","Sicherheitsziel, Gerechtigkeitsziel, soziale Integration",["Wachstum, Export, Steuersenkung","Kontrolle, Strafe, Abschreckung","Nur Armutsverhinderung"],"Armut findet sich in allen drei wieder.",[("zw",3)])
MC("s-widerspruch",[],"Welcher Widerspruch stimmt?","Arbeitswilligkeit ist Voraussetzung, obwohl manche Bezüge mit Beiträgen bezahlt wurden",["Arbeit ist heute unwichtig","Es gibt kein Normalarbeitsverhältnis mehr in der Politik","Alle Bezüge sind unabhängig von Arbeit"],"Vier Widersprüche der Arbeitsgesellschaft.",[("s4",6)])
MULTI("s-vier",[],"Was gehört zur 4-in-1-Perspektive?",["Erwerbsarbeit","Sorgearbeit","Freiwilligenarbeit","Eigenarbeit"],["Schwarzarbeit","Leiharbeit"],"Frigga Haug.",[("s4",8)])
BUCKET("s-prekaer",[],"Atypisch?",["Atypisch","Normalarbeitsverhältnis"],[("Teilzeit",0),("Geringfügig",0),("Befristet",0),("Leiharbeit",0),("Unbefristete Vollzeit",1)],"Mindestens eines der vier Kriterien.",[("s4",9),("s2",20)])
BUCKET("s-alo",[7],"Welche Definition passt?",["EU","AMS","Langzeitbeschäftigungslos"],[("Befragung über eine bestimmte Woche",0),("Binnen 2 Wochen verfügbar",0),("Stichtag letzter Werktag des Monats",1),("Vorgemerkt bei der Geschäftsstelle",1),("Schulung zählt mit",2),("Mindestens zwölf Monate",2)],"Deine Notiz aus Einheit 5: Viele in Schulungen gelten nicht als arbeitslos, daher der Vorwurf der Schönung.",[("s4",13),("s5",13)])
MULTI("s-marienthal",[6],"Welche latenten Funktionen nennt Jahoda?",["Zeitstruktur","Status und Identität","Soziale Kontakte","Beitrag zu kollektiven Zielen"],["Gelderwerb","Urlaubsanspruch"],"Gelderwerb ist die manifeste Funktion.",[("s4",18),("s4",19)])
MC("s-marienthal",[6],"Laut Schönherr: Wie viele Langzeitarbeitslose haben oft nichts zu tun?","40 %",["5 %","84 %","100 %"],"Beschäftigte 5 %, Arbeitslose 37 %. Quelle: Schönherr 2021.",[("s4",19)])
ORD("s-amp",[8],"Bring die Phasen in die richtige Reihenfolge.",["Vollbeschäftigung, Institutionalisierung","Ölkrisen, Austro-Keynesianismus","Aktivierung, Privatisierung","Schlanker Staat, workfare","Corona-Sonderprogramme"],"Seit 2024 wieder Einsparungen.",[("s5",5),("s5",6),("s5",7)])
MC("s-amp",[8],"Wofür steht Austro-Keynesianismus?","Antizyklische Politik unter Kreisky, Staat stützt in der Krise",["Sparen in der Krise","Privatisierung aller Betriebe","Abschaffung der Sozialpartnerschaft"],"Deine Notiz: In schlechten Zeiten erhöhen, in guten zurückfahren; oft passierte nur das Erste.",[("s5",5)])
MULTI("s-amp",[8],"Was gehört zu den 2000er-Jahren?",["Nulldefizit","Schärfere Zumutbarkeit","Individualisierung der Verantwortung"],["Bildungsexpansion","Kurzarbeit wegen Corona"],"Auch die Hartz-Reformen in Deutschland.",[("s5",6)])
TF("s-ams",[],"Zum Ziel des AMS gehört auch die Existenzsicherung während der Arbeitslosigkeit.",True,"§ 29 AMSG.",[("s5",8)])
BUCKET("s-aktiv",[9],"Passiv oder aktiv?",["Passiv","Aktiv"],[("Arbeitslosengeld",0),("Notstandshilfe",0),("Kurzarbeit",1),("Eingliederungsbeihilfe",1),("Sozioökonomischer Betrieb",1),("AMS-Kurs",1)],"Deine Notiz: Aktive Ausgaben sind stark gestiegen.",[("s5",9),("s5",13)])
MATCH("s-aktiv",[9],"Welcher Bereich aktiver Politik?",[["Beschäftigung","Lohnbeihilfen, SÖB"],["Qualifizierung","Aus- und Weiterbildung"],["Unterstützung","Beratung, Kinderbetreuung"]],"Drei Bereiche auf der Folie.",[("s5",13)])
MC("s-alg",[],"Wie hoch ist der Grundbetrag des Arbeitslosengelds?","55 % des letzten Nettogehalts",["80 %","100 %","30 %"],"Das Skript Recht und MatSi nennen denselben Wert.",[("s5",12),("r3",15)])
MC("s-alg",[],"Wie hoch ist die Notstandshilfe?","92 bis 95 % des Arbeitslosengelds",["50 %","100 %","55 % des Lohns"],"De facto unbefristet, Notlage regelmäßig nachzuweisen.",[("s5",12)])
MC("s-soeb",[],"Was ist das Ziel eines SÖB?","Integration in den regulären Arbeitsmarkt",["Dauerbeschäftigung im Betrieb","Gewinn für Eigentümer*innen","Ersatz der Mindestsicherung"],"Befristete Plätze für besonders Benachteiligte.",[("s5",15)])
MC("s-garantie",[],"Was war „Marienthal reversed“?","Eine Jobgarantie für Langzeitarbeitslose in Gramatneusiedl",["Ein Grundeinkommen in Wien","Eine Kürzung beim AMS","Ein Filmprojekt ohne Politik"],"Betriebe erhielten 100 % Lohnförderung.",[("s5",16)])
MC("s-gini",[10],"Was bedeutet Gini 1?","Eine Person besitzt alles",["Völlige Gleichverteilung","Alle sind arm","Die Hälfte besitzt alles"],"0 wäre völlige Gleichverteilung.",[("s6",7)])
TF("s-gini",[10],"Beim Vermögen ist Österreich vergleichsweise gleich, beim Einkommen sehr ungleich.",False,"Genau umgekehrt: Einkommen vergleichsweise gleich, Vermögen sehr ungleich.",[("s6",6),("s6",8),("s6",9)])
CALC("s-haeq",[],"Paar mit einem Kind unter 14 Jahren. Wie hoch ist die Summe der Gewichte?","1+0.5+0.3","Gewichte",["Erste erwachsene Person 1,0.","Zweite erwachsene Person 0,5.","Kind unter 14: 0,3. Summe 1,8."],"Haushaltseinkommen durch 1,8 ergibt das Äquivalenzeinkommen.",[("s6",10)],tol=0.01)
CALC("s-haeq",[],"Haushalt mit 3.600 Euro, zwei Erwachsene und ein Kind unter 14. Wie hoch ist das Äquivalenzeinkommen?","3600/1.8","Euro",["Gewichte 1,0 + 0,5 + 0,3 = 1,8.","3.600 / 1,8 = 2.000 Euro."],"Das zeigt: Mehrpersonenhaushalte brauchen nicht doppelt so viel.",[("s6",10)])
MC("s-verm",[10],"Wie viele Haushalte haben laut HFCS gar keine Immobilie?","50,1 %",["5 %","25 %","90 %"],"40,5 % nur den Hauptwohnsitz. Nur 0,4 % haben 3+ weitere.",[("s6",11)])
MC("s-verm",[10],"Wie hoch ist der Anteil vermögensbezogener Steuern?","3,1 %",["20,7 %","35,6 %","17,7 %"],"Zahlen 2019, Momentum Institut.",[("s6",12)])
ORD("s-verm",[10],"Was fiel wann weg?",["Vermögensteuer auf Nettovermögen","VfGH hebt Erbschaftssteuer auf","Erbschafts- und Schenkungssteuer endet"],"1993, 2007, 2008.",[("s6",14)])
BUCKET("s-vorschlag",[10],"Welche Begründung passt?",["Grundsteuer","Erbschaftssteuer","Überreichtumssteuer"],[("Bodenrente, nachhaltigere Landnutzung",0),("Leistungslose Zuwächse besteuern",1),("Stärkt Chancengleichheit",1),("Macht- und Vermögenskonzentration verhindern",2)],"Fessler und Schürz 2024.",[("s6",16)])
TF("s-vorschlag",[],"Überreichtum beginnt dort, wo Vermögen politische und wirtschaftliche Macht verleiht.",True,"Der Begriff stellt die Legitimität von Vermögen und Erbschaften infrage.",[("s6",17)])
TF("s-falter",[],"Laut Falter sagten Fessler und Schürz ihre Teilnahme ab, nachdem die OeNB sie ersucht hatte, Empfehlungen wegzulassen.",True,"Der Standard nannte das Maulkorb für Notenbanker.",[("zf",1)])

# Standpunkte
MULTI("s-stand",[],"Wer stimmte 2024 mit Ja für ein bedingungsloses Grundeinkommen statt Mindestsicherung?",["KPÖ","KEINE"],["ÖVP","SPÖ","FPÖ","GRÜNE","NEOS"],"Quelle: Wahlkabine, Frage 20.",[("@wk",0)])
MULTI("s-stand",[],"Wer wollte 2024 eine Kindergrundsicherung?",["SPÖ","GRÜNE","NEOS","KPÖ"],["ÖVP","FPÖ"],"Quelle: Wahlkabine, Frage 23.",[("@wk",0)])
MULTI("s-stand",[],"Wer wollte, dass Erbschaften über 1,5 Millionen Euro steuerfrei bleiben?",["ÖVP","FPÖ","NEOS"],["SPÖ","GRÜNE","KPÖ"],"Quelle: Wahlkabine, Frage 16. Passt zur Debatte um Besitzstand.",[("@wk",0)])
MULTI("s-stand",[],"Wer wollte bindende Mietobergrenzen auch für Neubauten?",["SPÖ","GRÜNE","KPÖ"],["ÖVP","FPÖ","NEOS"],"Quelle: Wahlkabine, Frage 18.",[("@wk",0)])
MULTI("s-stand",[],"Wer wollte Arbeitszeit auf 30 Stunden bei vollem Lohnausgleich kürzen?",["SPÖ","GRÜNE","KPÖ"],["ÖVP","FPÖ","NEOS"],"Quelle: Wahlkabine, Frage 1.",[("@wk",0)])
MC("s-stand",[],"Welche Partei antwortete als einzige der Parlamentsparteien mit Ja auf ein höheres Pensionsantrittsalter?","NEOS",["ÖVP","SPÖ","GRÜNE"],"Quelle: Wahlkabine, Frage 13.",[("@wk",0)])

for t,x,s in [
 ("Dekommodifizierung","Wie unabhängig Existenz und Teilhabe vom Verkauf der Arbeitskraft sind.",[("s2",18)]),
 ("Stratifizierung","Wie Sozialpolitik die Gesellschaftsstruktur und Ungleichheit beeinflusst.",[("s2",18)]),
 ("Normalarbeitsverhältnis","Lebenslange Vollzeit, oft männlicher Alleinverdiener; Grundlage des österreichischen Sozialstaats.",[("s2",20)]),
 ("Workfare","Aktivierung statt Versorgung: Hilfe hängt an Arbeitswilligkeit.",[("s2",15),("s5",6)]),
 ("Working poor","Menschen, deren Arbeit die Existenz nicht sichert.",[("s4",9)]),
 ("Langzeitbeschäftigungslosigkeit","Mindestens zwölf Monate beim AMS, Schulungen eingeschlossen.",[("s4",13)]),
 ("Gini-Koeffizient","Maß für Ungleichheit zwischen 0 und 1.",[("s6",7)]),
 ("Haushaltsäquivalenzeinkommen","Einkommen, gewichtet nach Erwachsenenäquivalenten.",[("s6",10)]),
 ("Überreichtum","Vermögen, das zu politischer und wirtschaftlicher Macht wird.",[("s6",17)]),
 ("Austro-Keynesianismus","Antizyklische Wirtschaftspolitik unter Kreisky mit Bildungsexpansion und Sozialpartnerschaft.",[("s5",5)]),
 ("Äquivalenzprinzip","Leistungshöhe entspricht Beitragshöhe und -dauer.",[("zt",7)]),
 ("Sozialpartnerschaft","Spielte in der Arbeitsmarktpolitik der 1970er und 1980er eine zentrale Rolle.",[("s5",5)]),
]: TERM(t,x,s)
for n,d,x,s in [
 ("Otto von Bismarck","um 1880","Erstes Sozialversicherungssystem. Sein Zitat: die arbeitenden Klassen gewinnen oder bestechen.",[("s2",12)]),
 ("Gøsta Esping-Andersen","1990","Drei Wohlfahrtsregime.",[("s2",18)]),
 ("Robert Nozick","","Anspruchstheorie, Besitzstandsgerechtigkeit.",[("s2",7)]),
 ("Amartya Sen","","Die Idee der Gerechtigkeit, Flötenbeispiel.",[("s2",3)]),
 ("Marie Jahoda","","Latente Funktionen der Erwerbsarbeit, Marienthal.",[("s4",18)]),
 ("Frigga Haug","2008","4-in-1-Perspektive.",[("s4",8)]),
 ("Wilkinson und Pickett","2010","Gleichheit erhöht die Lebensqualität für alle.",[("s3",8)]),
 ("Fessler und Schürz","2024","Reformvorschläge zu Vermögen, Überreichtum.",[("s6",16),("zf",1)]),
 ("Bruno Kreisky","","Steht für den Austro-Keynesianismus.",[("s5",5)]),
]: PERSON(n,d,x,s)
for y,t,s in [("1880","Bismarck: erstes Sozialversicherungssystem",[("s2",11)]),("1960","Vollbeschäftigung, Institutionalisierung",[("s5",5)]),("1970","Ölkrisen, Austro-Keynesianismus",[("s5",5)]),("1990","Aktivierung, Esping-Andersen",[("s5",6),("s2",18)]),("1993","Ende der Vermögensteuer",[("s6",14)]),("2008","Ende der Erbschaftssteuer",[("s6",14)]),("2020","Corona: Kurzarbeit, Aktion Sprungbrett",[("s5",7)]),("2024","Wieder Einsparungen",[("s5",7)])]:
    TL(y,t,s)

TRAP("Ausgaben 2024: Zahlen weichen ab","Einheit 3 nennt Krankheit 27,6 % und Alter 46 %, Einheit 4 Gesundheit 27,3 % und Alter 46,1 %. MatSi nennt 163 Milliarden Sozialausgaben, SoPol 157 Milliarden. Merk dir die Größenordnung.",[("s3",12),("s4",2),("msp",6)])
TRAP("Wohnen: 0,4 % oder 2,5 %?","Einheit 3 nennt für Leistungen für Wohnen ca. 0,4 % (2015) und für Wohnen und soziale Ausgrenzung zusammen 2,5 % (2024). Verschiedene Abgrenzung und verschiedene Jahre.",[("s3",17),("s3",12)])
TRAP("Carla in der Flöte","In Einheit 1 sagt sie, sie habe die Flöte gebaut. In Einheit 2 klingt es stärker nach Leistung und Wegnahme. Darum passt Carla zu Leistung wie zu Besitz.",[("s1",9),("s2",3)])
TRAP("Falscher Termin auf der Folie","Einheit 2 nennt als nächsten Termin 25.9.2025, das ist offenbar ein Rest vom Vorjahr. Der Semesterplan zeigt 2026.",[("s2",25),("s2",2)])
TRAP("Deine Mitschrift zur Ölkrise","In deiner Notiz steht 1971. Auf der Folie steht keine Jahreszahl, nur Ölkrisen in den 1970er und 1980er Jahren. Prüf das bei Bedarf nach, die App fragt das Jahr nicht ab.",[("s5",5)])
