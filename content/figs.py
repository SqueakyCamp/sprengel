"""Interaktive Grafiken fuer die Zusammenfassungen. Jede Grafik haengt an einem Kapitel; jeder antippbare Teil hat Text und Verweise.

kind:
  "lanes"   Spalten mit Stationen untereinander; "edge" beschriftet den Pfeil in die Station (Rechtsmittel, Frist).
  "pyramid" Stufen von oben nach unten, oben am wichtigsten.
  "compare" Spalten mit gleichen Zeilen (rows); ein Tipp auf die Spalte zeigt die Erklaerung.
Gebaut und geprueft von tools/build_all.py (Seiten existieren, Zahlen stehen auf den Seiten).
"""

def N(label, text, src, sub="", edge="", tag=""):
    return dict(label=label, sub=sub, edge=edge, tag=tag, text=text, src=src)

def COL(title, nodes=None, text="", src=None, cells=None, tag=""):
    return dict(title=title, nodes=nodes or [], text=text, src=src or [], cells=cells or [], tag=tag)

FIGS = {
  "recht": [
    dict(id="fig-instanz", ch="ri", title="Der Instanzenzug", lead="Drei Wege durch die Instanzen. Tippe auf eine Station.", kind="lanes", cols=[
      COL("Verwaltung", [
        N("Behörde", "Sozialhilfe wird bei einer Verwaltungsbehörde beantragt, in Wien bei der MA 40. Sie entscheidet mit Bescheid. Entscheidet sie nicht, gibt es die Säumnisbeschwerde an das Landesverwaltungsgericht.", [("f3",4)], sub="z. B. MA 40, Bescheid"),
        N("Landes\u00adverwaltungs\u00adgericht", "Innerhalb von 4 Wochen kann der Bescheid beim Landesverwaltungsgericht angefochten werden, eingebracht bei der Behörde, die entschieden hat. Seit 2014 heißt dieses Rechtsmittel Beschwerde, nicht mehr Berufung.", [("f3",4)], edge="Beschwerde, 4 Wochen"),
        N("VwGH oder VfGH", "Danach bleibt innerhalb von 6 Wochen die Revision an den VwGH und die außerordentliche Beschwerde an den VfGH. Dafür braucht es eine anwaltliche Vertretung; Verfahrenshilfe kann innerhalb der Frist beantragt werden.", [("f3",4)], edge="Revision oder Beschwerde, 6 Wochen"),
        N("EGMR", "Gegen die Entscheidung von VwGH oder VfGH ist eine Beschwerde der Privatperson an den Europäischen Gerichtshof für Menschenrechte möglich, wegen Verletzung von Menschenrechten durch die Gesetzeslage oder das Behördenverhalten.", [("f3",4),("f3",5)], edge="wegen Menschenrechten"),
      ]),
      COL("Zivilsachen", [
        N("Bezirksgericht", "Unterhalt für ein Kind entscheidet das Bezirksgericht in der Pflegschaftsabteilung mit Beschluss. Eine Schadenersatzklage unter 15.000 Euro läuft als Mahnklage am Bezirksgericht: Zahlungsbefehl, Einspruch binnen 4 Wochen, dann Urteil.", [("f3",7)], sub="Urteil oder Beschluss"),
        N("Landesgericht", "Gegen das Urteil gibt es 4 Wochen nach Zustellung der schriftlichen Ausfertigung die Berufung an das Landesgericht, gegen einen Beschluss binnen 2 Wochen den Rekurs.", [("f3",7)], edge="Berufung 4 Wochen, Rekurs 2 Wochen"),
        N("OGH", "Danach gibt es die Revision oder den Revisionsrekurs an den OGH, aber nur selten.", [("f3",7)], edge="Revision, sehr selten"),
      ]),
      COL("Strafsachen", [
        N("Bezirksgericht", "Ein Ladendiebstahl wie das Parfüm bei DM landet beim Bezirksgericht, das ein Urteil fällt. Nach der Verkündung bleiben 3 Tage, um das Rechtsmittel anzumelden.", [("f3",6)], sub="Urteil"),
        N("Landesgericht", "Die Berufung geht binnen 4 Wochen an das Landesgericht, eingebracht beim Bezirksgericht; die Frist beginnt mit der schriftlichen Urteilsausfertigung. Das Strafverfahren hat hier nur zwei Instanzen.", [("f3",6)], edge="Berufung, 4 Wochen"),
      ]),
    ]),
    dict(id="fig-schnell", ch="ri", title="Schnellverfahren im Verwaltungsstrafrecht", lead="Je höher die Strafe, desto mehr Rechtsschutz. Tippe auf eine Spalte.", kind="compare", rows=["Bis", "Rechtsmittel"], cols=[
      COL("Organ\u00admandat", text="Die Organstrafverfügung geht in der Regel bis 90 Euro. Es gibt kein Rechtsmittel; wer nicht zahlt, eröffnet aber das Verwaltungsstrafverfahren, das meist in einem Bescheid endet.", src=[("f3",5)], cells=["90 Euro", "keines, nicht zahlen öffnet das Verfahren"]),
      COL("Anonym\u00adverfügung", text="Die Anonymverfügung geht bis 365 Euro. Wie beim Organmandat gibt es kein Rechtsmittel, nur die Möglichkeit, nicht zu zahlen.", src=[("f3",5)], cells=["365 Euro", "keines, wie Organmandat"]),
      COL("Straf\u00adverfügung", text="Die Strafverfügung geht bis 600 Euro. Dagegen gibt es den Einspruch.", src=[("f3",5)], cells=["600 Euro", "Einspruch"]),
      COL("Bescheid", text="Ohne Schnellverfahren entscheidet die Landespolizeidirektion mit Bescheid. Er kann innerhalb von 4 Wochen beim Landesverwaltungsgericht angefochten werden, danach binnen 6 Wochen Revision oder Beschwerde an die Höchstgerichte.", src=[("f3",5)], cells=["Normalverfahren", "Beschwerde, 4 Wochen"], tag="hi"),
    ]),
    dict(id="fig-stufen", ch="rs", title="Stufenbau der Rechtsordnung", lead="Jede Stufe stützt sich auf die darüber. Tippe auf eine Stufe.", kind="pyramid", nodes=[
      N("Baugesetze", "Die Grundprinzipien der Bundesverfassung stehen ganz oben. Sie stehen auch über dem EU-Recht; deshalb brauchte der EU-Beitritt eine Volksabstimmung.", [("rv",27),("rv",28),("f2",3)], sub="Grundprinzipien der Bundesverfassung"),
      N("EU-Recht", "Primäres und sekundäres Gemeinschaftsrecht der EU stehen unter den Grundprinzipien, aber über dem übrigen Bundesverfassungsrecht. EU-Verordnungen gelten unmittelbar, Richtlinien müssen erst umgesetzt werden.", [("rv",28),("f2",3)], sub="Vorrang vor dem übrigen Recht", tag="eu"),
      N("Verfassungs\u00adrecht", "Das übrige Bundesverfassungsrecht. Einfache Gesetze, die ihm widersprechen, kann der VfGH aufheben.", [("rv",27),("rv",28)], sub="übriges Bundesverfassungsrecht"),
      N("Einfache Gesetze", "Einfache Bundes- und Landesgesetze. Sie brauchen eine Grundlage in der Verfassung und dürfen ihr nicht widersprechen.", [("rv",27),("rv",28)], sub="Bundes- und Landesgesetze"),
      N("Verordnungen", "Verordnungen konkretisieren Gesetze und brauchen eine gesetzliche Grundlage.", [("rv",27),("f2",5)], sub="konkretisieren Gesetze"),
      N("Einzelakte", "Urteile, Bescheide und Verträge regeln den einzelnen Fall. Ein Bescheid ohne gesetzliche Grundlage ist rechtswidrig.", [("rv",27),("f2",6)], sub="Urteile, Bescheide, Verträge"),
      N("Exekution", "Ganz unten steht die Zwangsvollstreckung, also die zwangsweise Durchsetzung der Einzelakte.", [("rv",27)], sub="Zwangsvollstreckung"),
    ]),
    dict(id="fig-kompetenz", ch="rp", title="Wer macht was? Art 10 bis 15 B-VG", lead="Bund und Länder teilen sich Gesetzgebung und Vollziehung. Tippe auf einen Artikel.", kind="compare", rows=["Gesetzgebung", "Vollziehung"], cols=[
      COL("Art 10", text="Gesetzgebung und Vollziehung liegen beim Bund.", src=[("rv",52)], cells=[["Bund", "bund"], ["Bund", "bund"]]),
      COL("Art 11", text="Der Bund macht das Gesetz, das Land vollzieht es.", src=[("rv",52)], cells=[["Bund", "bund"], ["Land", "land"]]),
      COL("Art 12", text="Der Bund macht ein Grundsatzgesetz, das Land das Ausführungsgesetz und die Vollziehung. Darunter fällt das Armenwesen und damit die Sozialhilfe.", src=[("rv",52),("f3",4)], cells=[["Grundsatz Bund, Ausführung Land", "mix"], ["Land", "land"]], tag="hi"),
      COL("Art 15", text="Was nicht ausdrücklich dem Bund übertragen ist, bleibt bei den Ländern: Gesetzgebung und Vollziehung. Die Gerichtsbarkeit ist dagegen nur Bundessache.", src=[("rv",51),("rv",52)], cells=[["Land", "land"], ["Land", "land"]]),
    ]),
    dict(id="fig-prinzip", ch="r9", title="Drei Prinzipien sozialer Sicherung", lead="Woher eine Leistung kommt, entscheidet, was man dafür braucht. Tippe auf eine Spalte.", kind="compare", rows=["Voraussetzung", "Beispiele"], cols=[
      COL("Ver\u00adsicherung", text="Versicherungsprinzip: Wer Beiträge zahlt, bekommt im Versicherungsfall eine Gegenleistung. Sozialversicherungen sind über weite Bereiche Zwangsversicherung, die Beiträge richten sich nach dem Einkommen.", src=[("r2",61),("r2",62)], cells=["Beiträge gezahlt", "Arbeitslosengeld, Pension, Krankenversicherung"]),
      COL("Versorgung", text="Versorgungsprinzip: Leistung ohne Vorleistung, wenn eine bestimmte Situation eintritt.", src=[("r2",62),("r2",63)], cells=["eine bestimmte Situation", "Familienbeihilfe, Kinderbetreuungsgeld"]),
      COL("Sozialhilfe", text="Sozialhilfeprinzip: Hilfe bei Hilfsbedürftigkeit, subsidiär, also erst wenn nichts anderes reicht. Früher oft mit Regress, heute in der WMS mit Rechtsanspruch.", src=[("r2",62),("r2",63)], cells=["Hilfsbedürftigkeit, subsidiär", "Wiener Mindestsicherung"], tag="hi"),
    ]),
  ],
  "matsi": [
    dict(id="fig-netze", ch="m1", title="Drei Sorten Leistungen", lead="Das zweite Netz greift erst, wenn alles andere nicht reicht. Tippe auf eine Spalte.", kind="compare", rows=["Hängt ab von", "Beispiele"], cols=[
      COL("Universal", text="Universalleistungen gibt es unabhängig von Einkommen und Vermögen.", src=[("msp",2)], cells=["nichts, unabhängig von Einkommen und Vermögen", "Familienbeihilfe, Pflegegeld"]),
      COL("Ver\u00adsicherung", text="Versicherungsleistungen der Sozialversicherung folgen dem Prinzip der Anwartschaft: Wer eingezahlt hat, bekommt etwas; Dauer und Höhe hängen vom bisherigen Bezug ab. Sie gelten für Erwerbstätige und ihre Angehörigen.", src=[("msp",2)], cells=["Anwartschaft, bisheriger Bezug", "Leistungen der Sozialversicherung"]),
      COL("Fürsorge", text="Fürsorge- oder Sozialhilfeleistungen sind das zweite soziale Netz. Sie setzen erst ein, wenn Arbeit, Einkommen, Vermögen, Familie und das erste Netz nicht reichen.", src=[("msp",2),("msk",29)], cells=["Bedarf, wenn alles andere nicht reicht", "WMS, Beihilfen zum Wohnen, Rezeptgebührenbefreiung"], tag="hi"),
    ]),
    dict(id="fig-konkurs", ch="m11", title="Drei Wege durch den Privatkonkurs", lead="Nach der Eröffnung gibt es drei Pläne. Tippe auf eine Spalte.", kind="compare", rows=["Quote", "Laufzeit", "Gläubiger*innen"], cols=[
      COL("Sanierungs\u00adplan", text="Fixe Quote, höchstens 5 Jahre, die Mehrheit der Gläubiger*innen muss zustimmen. In der Praxis kaum relevant, weil die Gläubiger*innen ohne Vermögensverwertung nicht zustimmen.", src=[("msp",71)], cells=["fix", "max. 5 Jahre", "Mehrheit muss zustimmen"]),
      COL("Zahlungs\u00adplan", text="Fixe Quote, höchstens 7 Jahre, Summen- und Kopfmehrheit der Gläubiger*innen. Das Mindestangebot richtet sich nach dem pfändbaren Einkommen der nächsten 5 Jahre. Meist erwünscht, weil die Person selbst zahlt und keine laufenden Pfändungen hat.", src=[("msp",71),("msp",72)], cells=["fix", "max. 7 Jahre", "Mehrheit muss zustimmen"], tag="hi"),
      COL("Abschöpfungs\u00adplan", text="Abschöpfung über 5 Jahre ohne Mindestquote. Ein Treuhänder verteilt das pfändbare Einkommen an die Gläubiger*innen; möglich auch gegen ihren Willen. Obliegenheiten: keine neuen Schulden, pfändbares Einkommen und Vermögen herausgeben.", src=[("msp",71)], cells=["keine Mindestquote", "5 Jahre", "auch gegen ihren Willen"]),
    ]),
  ],
  "sopol": [
    dict(id="fig-regime", ch="e2", title="Wohlfahrtsregime nach Esping-Andersen", lead="Nicht mehr oder weniger Staat, sondern verschiedene Varianten. Tippe auf ein Regime.", kind="compare", rows=["Leistungen", "Dekommodifizierung", "Beispiele"], cols=[
      COL("Liberal", text="Geringe, steuerfinanzierte Grundsicherung und private Zusatzversicherungen. Geringe Dekommodifizierung: Wer seine Arbeitskraft nicht verkaufen kann, ist schlecht abgesichert. Bestehende Ungleichheit verfestigt sich.", src=[("s2",18),("s2",19)], cells=["gering, steuerfinanziert, privat ergänzt", "gering", "USA, Großbritannien"]),
      COL("Konservativ", text="Statusgebundene, beitragsfinanzierte Sozialleistungen, starker Einfluss der Kirche und zentrale Rolle der Familie. Mittlere Dekommodifizierung, vorwiegend auf Statuserhalt gerichtet. Österreich gehört dazu.", src=[("s2",19)], cells=["statusgebunden, beitragsfinanziert", "mittel", "Österreich, Deutschland"], tag="hi"),
      COL("Sozial\u00addemokratisch", text="Umfassende, steuerfinanzierte Sozialleistungen, hohe Dekommodifizierung und umfassende Solidarität.", src=[("s2",19)], cells=["umfassend, steuerfinanziert", "hoch", "Schweden, Dänemark"]),
    ]),
  ],
}
