"""Prüfungsfragestunde Recht (Mitschrift vom 16.11.2026, über other/Jakob). Die Lehrende ging Fragen aus dem Fragenpool durch.
Die Fragen und Themen stammen aus der Mitschrift (`fs`), die Antworten sind mit Skript und Folien abgeglichen und tragen deren Seiten.
Wo die Mitschrift ungenau ist oder vom Skript abweicht, steht das in TRAP. Jede Karte hat pf=<Block> und erscheint im Tab „Fragestunde“."""

BLOCKS = ["Verträge und Gewährleistung", "AMS, Notstandshilfe, KBG", "Verfahren, Zustellung, Strafen", "Exekution und Insolvenz", "Staat und Verfassung", "Mindestsicherung"]
INFO = ("Laut Prüfungsfragestunde hat die Prüfung 23 Fragen, davon 3 offene. Dazu kommen ungefähr 0 bis 2 Zahleneingaben, je 3 bis 4 Wahr/Falsch- und Single-Choice-Fragen "
        "und etwa 7 bis 10 Multiple-Choice-Fragen; die Aufteilung ist nur eine Schätzung der Lehrenden. Ihre Tipps: die offenen Fragen sicher können, die Fernlehren und das Skript "
        "mindestens einmal durchgehen, die Folien zur Mindestsicherung wiederholen und genau lesen, denn viele Antworten klingen plausibel und sind trotzdem falsch. "
        "Hier stehen die Fragen aus der Fragestunde mit Antworten aus Skript und Folien. Sie ist nicht der ganze Stoff. Die zweite Fragestunde bestätigt 30 Minuten und nennt 44 Punkte für die 3 offenen Fragen; falsche Kreuze geben Minuspunkte. Dazu kommen die Altfragen vom Vorjahr als eigener Block. Die echte Prüfung mit offenen Fragen probst du im Prüfungsmodus auf der Seite „Fernlehre-Fragen“.")


def add(c):
    T, TRAP = c.T, c.TRAP
    A, E, I = ("@abgb", 0), ("@eheg", 0), ("@io", 0)

    def tag(block):
        c.cards[-1]["pf"] = block

    def MC(b, t, q, right, wrong, why, src):
        c.MC(t, [], q, right, wrong, why, src); b and tag(b)

    def TF(b, t, q, val, why, src):
        c.TF(t, [], q, val, why, src); b and tag(b)

    def MU(b, t, q, right, wrong, why, src):
        c.MULTI(t, [], q, right, wrong, why, src); b and tag(b)

    def BU(b, t, q, buckets, items, why, src):
        c.BUCKET(t, [], q, buckets, items, why, src); b and tag(b)

    def MA(b, t, q, pairs, why, src):
        c.MATCH(t, [], q, pairs, why, src); b and tag(b)

    V, AL, Z, X, S, M = BLOCKS

    # ---------------- Themen, die es noch nicht gab ----------------
    T("r-form", "r8", "Formvorschriften",
      "Verträge sind grundsätzlich formfrei: Ob ein Vertrag schriftlich, mündlich oder stillschweigend geschlossen wurde, ist für seine Gültigkeit meist ohne Bedeutung, und für zehn Euro für eine Jause braucht niemand einen schriftlichen Vertrag. "
      "Nur in Ausnahmefällen schreibt das Gesetz eine Form vor, und das hat jeweils einen Schutzgrund. Der Erbverzicht oder ein Kaufvertrag unter Ehegatt*innen brauchen einen Notariatsakt oder ein gerichtliches Protokoll. "
      "Ein Autokauf muss schriftlich erfolgen, damit man das Auto anmelden kann, und beim Kauf einer Liegenschaft müssen die Unterschriften notariell beglaubigt sein, damit der Kauf ins Grundbuch kommt. "
      "Eine Schenkung verlangt laut Prüfungsfragestunde grundsätzlich die Übergabe, damit niemand aus spontaner Großzügigkeit etwas verspricht und es dann bereut. Auch eine Entlassung muss nicht schriftlich ausgesprochen werden: Es reicht, dass sie der betroffenen Person nachweislich zur Kenntnis gelangt.",
      [("r2", 54), ("fs", 1), ("fs", 7)])
    T("r-gutschein", "r8", "Gutscheine und Kostenvoranschläge",
      "Wer einen Gutschein bekommt, erhält ein Auswahlrecht, aber keinen Anspruch auf Barauszahlung. Wählt man eine Ware mit geringerem Wert, wird für die Differenz wieder ein Gutschein ausgestellt. "
      "Wurde nichts anderes vereinbart, gilt ein Gutschein 30 Jahre; kürzere Befristungen sind laut Prüfungsfragestunde nicht automatisch zulässig und müssen genau geprüft werden. "
      "Ein Kostenvoranschlag ist für Konsument*innen im Zweifel kostenlos, außer sie wurden vorher auf ein Entgelt hingewiesen, und er ist grundsätzlich verbindlich (§ 5 KSchG).",
      [("r2", 59), ("fs", 11), ("fs", 12)])
    T("r-alvweg", "rl", "Rechtsweg bei AMS und PVA",
      "Gegen Bescheide der regionalen Geschäftsstelle des AMS gibt es die Beschwerde an das Bundesverwaltungsgericht, das unter Beteiligung fachkundiger Laienrichter*innen entscheidet. "
      "Bei der Pension ist es anders: Gegen einen negativen Bescheid der PVA bringt man eine Klage beim Arbeits- und Sozialgericht ein, laut Prüfungsfragestunde genauso beim Pflegegeld. "
      "Die Lehrende betonte, dass man nicht alle sozialrechtlichen Bescheide gleich behandeln darf: AMS heißt Beschwerde ans BVwG, Pension und Pflegegeld heißen Klage beim ASG.",
      [("r3", 24), ("r3", 19), ("fs", 5)])
    T("r-beweis", "rw", "Beweismittel und Verbesserungsauftrag",
      "Als Beweis kommt im Verwaltungsverfahren alles in Frage, was den Sachverhalt klären kann. Das AVG nennt insbesondere Urkunden, Zeug*innen, die Vernehmung von Parteien und Beteiligten, Sachverständige und den Augenschein, bei dem sich die Behörde selbst vor Ort ein Bild macht. "
      "Die Behörde würdigt die Beweise frei. Fristgebundene Eingaben können nur schriftlich eingebracht werden. Formfehler wie eine fehlende Beilage, eine fehlende Vollmacht oder ein nicht verwendetes Formular berechtigen die Behörde aber nicht zur Zurückweisung: "
      "Sie muss eine Frist zur Behebung setzen, den Verbesserungsauftrag. Darum ist laut Prüfungsfragestunde bei einer Beschwerde zuerst die Frist zu wahren, die perfekte Begründung kommt danach.",
      [("r2", 11), ("r2", 13), ("rv", 63), ("fs", 16), ("fs", 18)])
    T("r-mandat", "rp", "Parteien, freies Mandat und Klubzwang",
      "Österreich ist eine mittelbare, parlamentarisch-repräsentative Demokratie: Die Bürger*innen wählen Vertreter*innen, die dann entscheiden. Die gewählten Abgeordneten haben ein freies Mandat, sie entscheiden nach eigenem Ermessen ohne rechtlich bindende Vorgaben. "
      "In der Realität gibt es häufig Klubzwang, also die Absprache, geschlossen abzustimmen; rechtlich bindend ist er nicht. Ein*e freie*r Abgeordnete*r ist dagegen jemand, der keinem Parlamentsklub angehört, etwa nach einem Parteiaustritt. "
      "Eine gesetzliche Mindestanzahl an Parteien gibt es nicht, für einen demokratischen Rechtsstaat ist aber wichtig, dass verschiedene Positionen vertreten sein können. Der Nationalrat hat 183 Abgeordnete.",
      [("rv", 39), ("rv", 42), ("fs", 13), ("fs", 14)])
    T("r-ngo", "rp", "Öffentliche Hand oder NGO",
      "Öffentliche Aufgaben werden vorwiegend aus Steuern finanziert. Sozialversicherungsbeiträge haben einen eigenen Zweck, und Spenden sind keine zentrale Finanzierungsquelle der Verwaltung. "
      "Volksanwaltschaft, Rechnungshof und Kinder- und Jugendhilfe sind staatliche Einrichtungen; Caritas, Volkshilfe und Rotes Kreuz sind NGOs, also Nichtregierungsorganisationen, die trotzdem Unternehmer im Sinne des Konsumentenschutzrechts sein können. "
      "Das Gesetz spricht von Kinder- und Jugendhilfe, nicht vom Jugendamt. Das Bundesrechenzentrum (BRZ) nannte die Lehrende als Beispiel: keine private Firma, sondern laut Mitschrift ein Dienstleistungsunternehmen des öffentlichen Rechts mit eigener Rechtspersönlichkeit.",
      [("fs", 15), ("fs", 16), ("fs", 2), ("fs", 7)])
    T("r-wmg", "r9", "Die Wiener Mindestsicherung im Skript",
      "Wien hat das Sozialhilfe-Grundsatzgesetz nur teilweise umgesetzt, darum gilt hier weiter das Wiener Mindestsicherungsgesetz (WMG). Es soll Armut und soziale Ausschließung bekämpfen und die Eingliederung ins Erwerbsleben fördern. "
      "Gegliedert ist die WMS in Leistungen mit Rechtsanspruch, nämlich zur Sicherung von Lebensunterhalt und Wohnbedarf (bei höherer Miete mit Mietbeihilfe) sowie bei Krankheit, Schwangerschaft und Entbindung, "
      "und in die Hilfe in besonderen Lebenslagen (HibL) als vertragliche Leistung ohne Rechtsanspruch; dazu kommen soziale Dienste wie Heimhilfe oder Essen auf Rädern. Die Leistungen sind subsidiär, setzen rechtzeitig ein und gibt es nicht für die Vergangenheit. "
      "Anspruch hat, wer Lebensmittelpunkt und tatsächlichen Aufenthalt in Wien hat, den Bedarf nicht selbst decken kann, einen Antrag stellt und mitwirkt, und zu den Berechtigten gehört: Österreicher*innen sowie Gleichgestellte wie Asylberechtigte, erwerbstätige EU-Bürger*innen oder Personen mit Daueraufenthalt. "
      "Asylwerbende haben bis zum Abschluss des Verfahrens keinen Anspruch, subsidiär Schutzberechtigte seit 1.1.2026 auch nicht mehr.",
      [("r2", 69), ("r2", 70), ("r2", 71), ("r2", 72), ("r2", 75)])

    # ---------------- Verträge und Gewährleistung ----------------
    TF(V, "r-form", "Ein mündlich abgeschlossener Vertrag ist genauso gültig wie ein schriftlicher.", True,
       "Stimmt. Ob ein Vertrag schriftlich, mündlich oder stillschweigend geschlossen wurde, ist für seine Gültigkeit meist ohne Bedeutung. Nur in Ausnahmefällen verlangt das Gesetz eine bestimmte Form.",
       [("r2", 54), ("fs", 1)])
    MU(V, "r-form", "Für welche dieser Geschäfte verlangt das Gesetz laut Skript eine bestimmte Form?",
       ["Erbverzicht", "Kaufvertrag unter Ehegatt*innen", "Kauf einer Liegenschaft, damit er ins Grundbuch kommt", "Autokauf, damit man das Auto anmelden kann"],
       ["Einkauf im Supermarkt", "Zehn Euro für eine Jause ausborgen"],
       "Erbverzicht und Kaufvertrag unter Ehegatt*innen brauchen einen Notariatsakt oder ein gerichtliches Protokoll, der Liegenschaftskauf Schriftform und beglaubigte Unterschriften, der Autokauf Schriftform. Alltagsgeschäfte sind formfrei.",
       [("r2", 54), ("fs", 1)])
    TF(V, "r-form", "Eine Entlassung durch den Arbeitgeber oder die Arbeitgeberin ist nur gültig, wenn sie schriftlich ausgesprochen wird.", False,
       "Falsch. Laut Prüfungsfragestunde muss eine Entlassung nicht schriftlich erfolgen. Entscheidend ist, dass sie der betroffenen Person nachweislich zur Kenntnis gelangt.",
       [("fs", 7)])
    TF(V, "r-vertrag", "Ein gemeinnütziger Verein wie die Caritas kann Unternehmer im Sinne des Konsumentenschutzgesetzes sein.", True,
       "Stimmt. Unternehmer*in ist jede auf Dauer angelegte Organisation selbständiger wirtschaftlicher Tätigkeit, auch ohne Gewinnabsicht. Laut Fragestunde sind daher auch NGOs wie Caritas, Volkshilfe oder Rotes Kreuz Unternehmer*innen, wenn sie solche Verträge schließen.",
       [("r2", 53), ("fs", 1), ("fs", 2)])
    MC(V, "r-gewaehr", "Wem gegenüber macht man Gewährleistung geltend?", "Gegenüber der Vertragspartnerin, meist der Verkäuferin",
       ["Immer gegenüber der Herstellerin", "Gegenüber der Arbeiterkammer", "Gegenüber dem Gericht, das den Kauf genehmigt hat"],
       "Gewährleistung ist gesetzlich und besteht gegenüber der Vertragspartnerin. Die Verkäuferin muss sich ihrerseits bei der Herstellerin schadlos halten. Garantie ist dagegen eine freiwillige Zusage, meist der Herstellerin, und reicht so weit, wie sie zugesagt wurde.",
       [("r2", 57), ("fs", 10)])
    TF(V, "r-gewaehr", "Gewährleistung ist bloß das österreichische Wort für Garantie.", False,
       "Falsch, das sind zwei verschiedene Dinge. Gewährleistung ist der gesetzliche Anspruch gegenüber der Vertragspartnerin für Mängel bei der Übergabe. Garantie ist eine zusätzliche freiwillige Zusage, deren Umfang sich aus den Garantiebedingungen ergibt.",
       [("r2", 57), ("fs", 10)])
    MU(V, "r-gewaehr", "Welche Möglichkeiten gibt es bei der Gewährleistung?",
       ["Verbesserung", "Austausch", "Preisminderung", "Wandlung"], ["Schadenersatz in doppelter Höhe", "Gutschein statt Geld nach Wahl der Händlerin"],
       "Die vier Gewährleistungsbehelfe sind Verbesserung (Reparatur), Austausch, Preisminderung und Wandlung, also Rückabwicklung des Vertrags. Verbesserung und Austausch kommen zuerst.",
       [("r2", 58), ("fs", 10), ("fs", 11)])
    MC(V, "r-gewaehr", "Ein Tischler liefert einen Tisch mit einem Schnitt in der Platte. Was kann die Käuferin grundsätzlich zuerst verlangen?", "Verbesserung oder Austausch",
       ["Sofort die Wandlung, also Geld zurück", "Sofort eine Preisminderung", "Nichts, bei Möbeln gibt es keine Gewährleistung"],
       "Zuerst gibt es Verbesserung oder Austausch. Erst wenn das unmöglich ist, unverhältnismäßig wäre, zu lange dauert oder aus Gründen in der Person der Händler*in unzumutbar ist, kommen Preisminderung oder Wandlung. Laut Fragestunde kann das zum Beispiel sein, wenn das Vertrauen in den Tischler völlig zerstört ist.",
       [("r2", 58), ("fs", 11)])
    MC(V, "r-gewaehr", "Ein Handy, vor acht Monaten gekauft, funktioniert nicht mehr. Was gilt für den Beweis, dass der Mangel schon bei der Übergabe da war?",
       "Im ersten Jahr wird das vermutet, die Händlerin müsste das Gegenteil beweisen",
       ["Die Käuferin muss es immer beweisen", "Das muss die Herstellerin beweisen", "Ohne Gutachten gibt es keinen Anspruch"],
       "Tritt der Mangel bei einer Ware innerhalb eines Jahres auf, wird vermutet, dass er schon bei der Übergabe vorhanden war; bei einem Werk gilt das für 6 Monate. Danach trägt die Konsumentin die Beweislast, etwa dass das Handy nicht durch Wasser kaputt wurde.",
       [("r2", 57), ("fs", 11)])
    MA(V, "r-gewaehr", "Welche Frist gehört zu welcher Regel der Gewährleistung?",
       [["Geltendmachung bei beweglichen Sachen", "2 Jahre"], ["Geltendmachung bei unbeweglichen Sachen", "3 Jahre"], ["Vermutung des Mangels bei einer Ware", "1 Jahr"], ["Vermutung des Mangels bei einem Werk", "6 Monate"]],
       "Gerichtlich geltend machen muss man die Gewährleistung bei beweglichen Sachen wie Handy oder Auto binnen 2 Jahren, bei unbeweglichen wie einem Haus binnen 3 Jahren. Die Vermutung, dass der Mangel schon bei Übergabe da war, gilt bei Waren 1 Jahr, bei Werken 6 Monate.",
       [("r2", 57), ("r2", 58)])
    MC(V, "r-gutschein", "Wie lange gilt ein Gutschein, wenn nichts anderes vereinbart wurde?", "30 Jahre",
       ["1 Jahr", "3 Jahre", "Bis zum Ende des Kalenderjahres"],
       "Laut Skript gilt ein Gutschein 30 Jahre, wenn nichts anderes vereinbart wurde. Kürzere Fristen sind laut Fragestunde nicht automatisch zulässig und müssen geprüft werden, etwa wenn der Gutschein für eine zeitlich begrenzte Leistung ausgestellt wurde.",
       [("r2", 59), ("fs", 11), ("fs", 12)])
    TF(V, "r-gutschein", "Wer einen Gutschein besitzt, kann statt der Ware auch das Geld ausbezahlt verlangen.", False,
       "Falsch. Ein Gutschein gibt ein Auswahlrecht, aber keinen Anspruch auf Barauszahlung. Wählt man eine Ware mit geringerem Wert, bekommt man für die Differenz wieder einen Gutschein.",
       [("r2", 59)])
    TF(None, "r-gutschein", "Ein Kostenvoranschlag ist für Konsument*innen im Zweifel kostenlos.", True,
       "Stimmt. Nach § 5 KSchG muss man für einen Kostenvoranschlag nur zahlen, wenn man vorher darauf hingewiesen wurde. Für Nicht-Konsument*innen ist es genau umgekehrt.",
       [("r2", 59)])

    # ---------------- AMS, Notstandshilfe, KBG ----------------
    MC(AL, "r-kbgbeginn", "Wo stellt man den Antrag auf Kinderbetreuungsgeld?", "Bei der Krankenkasse, meist der Österreichischen Gesundheitskasse (ÖGK)",
       ["Beim Finanzamt", "Beim AMS", "Beim Familienministerium"],
       "Beantragt wird bei der Krankenkasse, bei der vorher Wochengeld bezogen wurde oder die letzte Versicherung bestand, für die meisten die ÖGK. Finanzamt, AMS und Familienministerium nannte die Lehrende in der Fragestunde ausdrücklich als falsche Antworten.",
       [("r3", 26), ("fs", 3)])
    TF(AL, "r-kbgr", "Werden die Eltern-Kind-Pass-Untersuchungen nicht oder nicht rechtzeitig nachgewiesen, wird das Kinderbetreuungsgeld gekürzt.", True,
       "Stimmt. Die Untersuchungen, zu denen auch eine Beratungsstunde mit einer Hebamme gehört, sind Voraussetzung für alle Varianten des KBG. Fehlen sie oder kommt der Nachweis nicht rechtzeitig und im Original, wird die Leistung reduziert.",
       [("r3", 26), ("fs", 3)])
    TF(AL, "r-bezug", "Je höher das frühere Einkommen war, desto länger bekommt man Arbeitslosengeld.", False,
       "Falsch. Das frühere Einkommen bestimmt die Höhe des Arbeitslosengelds, nicht die Dauer. Die Bezugsdauer hängt vom Alter und von den Beschäftigungs- und Versicherungszeiten ab, vom Grundanspruch mit 20 Wochen bis zu 52 Wochen ab 50.",
       [("r3", 13), ("r3", 14), ("fs", 3), ("fs", 4)])
    TF(AL, "r-alv", "Für Arbeitslosengeld braucht man mindestens einen Pflichtschulabschluss.", False,
       "Falsch. Anspruch hat, wer der Arbeitsvermittlung zur Verfügung steht, die Anwartschaft erfüllt und die Bezugsdauer nicht erschöpft hat. Ein Schulabschluss gehört nicht dazu; eine Ausbildung kann laut Fragestunde höchstens für den Berufsschutz eine Rolle spielen.",
       [("r3", 7), ("fs", 5)])
    MC(AL, "r-nh", "Wie oft kann man einen Folgeantrag auf Notstandshilfe stellen?", "Unbegrenzt oft, jeweils rechtzeitig vor Ablauf des Zeitraums",
       ["Höchstens zweimal", "Höchstens fünfmal, dann folgt die Mindestsicherung", "Gar nicht, Notstandshilfe gibt es nur einmal"],
       "Notstandshilfe wird jeweils für bis zu 52 Wochen gewährt, danach sind Folgeanträge unbegrenzt möglich. Laut Fragestunde muss man den Ablauf des Zeitraums im Blick haben und rechtzeitig neu beantragen.",
       [("r3", 17), ("r3", 18), ("fs", 4)])
    TF(AL, "r-nh", "Wer Notstandshilfe bezieht, ist kranken- und pensionsversichert.", True,
       "Stimmt. Wie beim Arbeitslosengeld ist man auch in der Notstandshilfe kranken- und pensionsversichert. Die Mitschrift der Fragestunde ist hier unklar, das Skript ist eindeutig.",
       [("r3", 17), ("r3", 18), ("fs", 4), ("fs", 5)])
    MA(AL, "r-schutz", "Berufsschutz, Entgeltschutz, Notstandshilfe: Was gilt?",
       [["Berufsschutz", "In den ersten 100 Tagen"], ["Entgeltschutz", "In den ersten 120 Tagen"], ["Mindestentgelt im Entgeltschutz", "80 % der Bemessungsgrundlage"], ["Notstandshilfe", "Weder Berufs- noch Entgeltschutz"]],
       "Die Lehrende nannte diese Zahlen als besonders wichtig, die genauen Fachbegriffe weniger. Berufsschutz: 100 Tage keine Vermittlung in einen anderen Beruf, wenn das die künftige Arbeit im eigenen Beruf wesentlich erschwert. Entgeltschutz: 120 Tage mindestens 80 %, danach 75 %.",
       [("r3", 9), ("r3", 17), ("fs", 4)])
    MC(AL, "r-alvweg", "Das AMS sperrt Herrn K. das Arbeitslosengeld per Bescheid. Wohin richtet sich sein Rechtsmittel?", "Beschwerde an das Bundesverwaltungsgericht",
       ["Klage beim Arbeits- und Sozialgericht", "Beschwerde an das Landesverwaltungsgericht", "Berufung an den Obersten Gerichtshof"],
       "Gegen Bescheide der regionalen Geschäftsstelle des AMS gibt es die Beschwerde an das Bundesverwaltungsgericht, das mit fachkundigen Laienrichter*innen entscheidet. Das Arbeits- und Sozialgericht ist dafür laut Fragestunde ausdrücklich nicht zuständig.",
       [("r3", 24), ("fs", 5)])
    MC(AL, "r-alvweg", "Die PVA lehnt den Pensionsantrag von Frau D. ab. Wie wehrt sie sich?", "Mit einer Klage beim Arbeits- und Sozialgericht",
       ["Mit einer Beschwerde an das Bundesverwaltungsgericht", "Mit einer Säumnisbeschwerde beim AMS", "Mit einem Einspruch beim Bezirksgericht"],
       "Gegen den negativen Bescheid der PVA bringt man eine Klage ein, zuständig ist das Arbeits- und Sozialgericht. Laut Fragestunde gilt das auch beim Pflegegeld, im Unterschied zum AMS-Bescheid.",
       [("r3", 19), ("fs", 5)])
    MC(AL, "r-sperre", "Frau L. kündigt ihre Stelle selbst. Was gilt für ihr Arbeitslosengeld?", "4 Wochen Sperrfrist ab Ende des Dienstverhältnisses, die Bezugsdauer wird dadurch nicht kürzer",
       ["6 Wochen Sperre und eine kürzere Bezugsdauer", "Kein Arbeitslosengeld, bis sie eine neue Stelle hatte", "Keine Folgen, das gilt wie eine Kündigung durch den Betrieb"],
       "Wer das Dienstverhältnis selbst oder durch eigenes Verschulden beendet, bekommt 4 Wochen lang kein Arbeitslosengeld (§ 11 AlVG). Anders als die Sperre nach § 10 AlVG wegen fehlender Arbeitswilligkeit, die mindestens 6 Wochen dauert, verkürzt diese Sperrfrist die Anspruchsdauer nicht.",
       [("r3", 10)])

    # ---------------- Verfahren, Zustellung, Strafen ----------------
    MC(Z, "r-beschwerde", "Welche Frist gilt grundsätzlich für eine Beschwerde gegen einen Bescheid?", "4 Wochen",
       ["2 Wochen", "3 Monate", "6 Monate"],
       "Die Beschwerde an das Verwaltungsgericht ist binnen 4 Wochen bei der Behörde einzubringen, die den Bescheid erlassen hat. Die 2 Wochen gibt es nur noch bei der Berufung im eigenen Wirkungsbereich der Gemeinden.",
       [("r2", 16), ("r2", 17), ("fs", 6)])
    TF(Z, "r-beweis", "Bei einer Beschwerde gegen einen Bescheid ist es wichtiger, die Frist zu wahren, als sofort eine perfekte Begründung zu liefern.", True,
       "Stimmt, das betonte die Lehrende in der Fragestunde. Formfehler kann man nach einem Verbesserungsauftrag beheben, eine verspätete Beschwerde ist verloren. Im Zivilverfahren dagegen kann man eine unvollständige Berufung nicht einfach später beliebig ergänzen.",
       [("fs", 18), ("fs", 19), ("r2", 11)])
    TF(Z, "r-beweis", "Fehlt einer fristgebundenen Eingabe an die Behörde eine Beilage, muss die Behörde sie sofort zurückweisen.", False,
       "Falsch. Formfehler wie eine fehlende Beilage, eine fehlende Vollmacht oder ein nicht verwendetes Formular berechtigen die Behörde nicht zur Zurückweisung. Sie muss mit einem Verbesserungsauftrag eine Frist zur Behebung setzen. Inhaltliche Mängel können dagegen zur Abweisung führen.",
       [("r2", 11)])
    MU(Z, "r-beweis", "Welche Beweismittel kennt das AVG?",
       ["Urkunden", "Zeug*innen", "Sachverständige", "Augenschein", "Vernehmung der Parteien"], ["Geschworenenurteil", "Volksbefragung"],
       "Das AVG nennt insbesondere Urkunden, Zeug*innen, die Vernehmung von Parteien und Beteiligten, Sachverständige und den Augenschein. Grundsätzlich kommt alles in Frage, was den Sachverhalt klären kann, und die Behörde würdigt die Beweise frei.",
       [("r2", 13), ("rv", 63), ("fs", 16)])
    MC(Z, "r-beweis", "Die Behörde sieht sich eine Wohnung vor Ort an, um sich ein eigenes Bild zu machen. Welches Beweismittel ist das?", "Augenschein",
       ["Urkundenbeweis", "Sachverständigenbeweis", "Parteiengehör"],
       "Beim Augenschein verschafft sich die Behörde selbst einen Eindruck von einem Ort oder Gegenstand. Sachverständige beurteilen etwas aufgrund ihres Fachwissens, Urkunden sind schriftliche Unterlagen.",
       [("r2", 13), ("fs", 16)])
    BU(Z, "r-zust", "RSa oder RSb: Wie wird das laut Skript zugestellt?", ["RSa, nur eigenhändig", "RSb, Ersatzzustellung möglich"],
       [("Ladung eines Verwaltungsgerichts", 0), ("Einberufungsbefehl des Bundesheeres", 0), ("Urteil in Strafsachen", 0), ("Aufforderung zum Geschworenendienst", 0), ("Zahlungsbefehl", 1), ("Klage im Zivilverfahren", 1), ("Strafverfügung", 1)],
       "Seit 2009 gehen Klagen, Urteile und Zahlungsbefehle im Zivilverfahren nicht mehr RSa, sondern RSb, Strafverfügungen seit 2013 ebenfalls nicht mehr zu eigenen Handen. RSa bleibt für besonders wichtige Schriftstücke wie Ladungen der Verwaltungsgerichte, Einberufungsbefehle, Strafurteile und die Aufforderung zum Geschworenendienst.",
       [("r2", 41), ("r2", 42), ("r2", 21)])
    MC(Z, "r-zust", "Was unterscheidet einen RSb-Brief von einem RSa-Brief?", "Den RSb-Brief darf auch eine andere erwachsene Person an der Abgabestelle übernehmen, den RSa-Brief nur die Empfänger*in selbst oder eine Postbevollmächtigte",
       ["RSb ist ein einfacher Brief ohne Rechtsfolgen", "Den RSa-Brief dürfen alle Mitbewohner*innen übernehmen", "RSb verwenden nur Behörden, RSa nur Gerichte"],
       "RSa, der blaue Brief, wird nur eigenhändig zugestellt, Ausnahmen gibt es für Postbevollmächtigte und Anwält*innen. Beim RSb, dem weißen Brief, ist die Ersatzzustellung an eine erwachsene Person an derselben Abgabestelle möglich, auch am Arbeitsplatz.",
       [("r2", 41), ("r2", 42), ("fs", 6)])
    BU(Z, "r-vstg", "Verwaltungsstrafverfahren oder gerichtliches Strafverfahren?", ["Verwaltungsstrafverfahren", "Gerichtliches Strafverfahren"],
       [("Jede Übertretung wird gesondert bestraft", 0), ("Mehrere Taten werden gemeinsam verhandelt, es gibt eine Gesamtstrafe", 1), ("Anklage und Entscheidung liegen bei derselben Behörde", 0),
        ("Anklage durch die Staatsanwaltschaft, getrennt vom Gericht", 1), ("In erster Instanz grundsätzlich nicht öffentlich", 0), ("Öffentliche und mündliche Verhandlung", 1)],
       "Im Verwaltungsstrafrecht gilt das Kumulationsprinzip: Falschparken, zu schnell fahren und eine rote Ampel ergeben drei Strafen. Im gerichtlichen Strafverfahren werden mehrere Taten gemeinsam verhandelt, es gibt eine Gesamtstrafe innerhalb des gesetzlichen Höchstmaßes. Gerichte verhandeln öffentlich und im Anklageprozess, die Verwaltungsstrafbehörde ist dagegen Anklägerin und Entscheiderin zugleich.",
       [("r2", 19), ("rv", 68), ("rv", 73), ("fs", 17), ("fs", 18)])
    MC(Z, "r-vstg", "Welche Freiheitsstrafe darf eine Verwaltungsstrafbehörde höchstens verhängen?", "6 Wochen",
       ["6 Monate", "1 Jahr", "Unbegrenzt, wenn viele Übertretungen zusammenkommen"],
       "Freiheitsstrafen über 6 Wochen dürfen nur Gerichte verhängen. Im gerichtlichen Strafverfahren sind deutlich höhere Freiheitsstrafen möglich.",
       [("r2", 19), ("r2", 20), ("fs", 18)])

    # ---------------- Exekution und Insolvenz ----------------
    MC(X, "r-ausfall", "Was unterscheidet eine Ausfallsbürgschaft von einer normalen Bürgschaft?", "Die Ausfallsbürg*in haftet nur für das, was beim Hauptschuldner trotz Exekution nicht hereinzubringen ist",
       ["Die Ausfallsbürg*in haftet nie, sie bestätigt nur den Vertrag", "Bei der Ausfallsbürgschaft zahlen beide immer je die Hälfte", "Banken verlangen bei jedem Kredit eine Ausfallsbürgschaft"],
       "Eine normale Bürg*in kann belangt werden, sobald der Hauptschuldner trotz Mahnung nicht zahlt. Die Ausfallsbürg*in haftet erst für den Ausfall nach Lohnpfändung, Fahrnis- oder Immobiliarexekution, sofort aber, wenn über den Hauptschuldner das Insolvenzverfahren eröffnet wird. Laut Fragestunde verlangen Banken normalerweise eine normale Bürgschaft; die Ausfallsbürgschaft kommt aus dem Eherecht.",
       [A, E, ("r2", 49), ("fs", 2), ("fs", 3)])
    TF(X, "r-ausfall", "Nach einer Scheidung kann das Gericht aussprechen, dass die Person, die den Wohnungskredit übernimmt, Hauptschuldner*in ist und die andere nur noch Ausfallsbürg*in.", True,
       "Stimmt. So muss bei einer Trennung nicht automatisch die gemeinsam finanzierte Wohnung verkauft werden. Wer übernimmt, zahlt den Kredit allein weiter, die andere Person haftet erst, wenn beim Hauptschuldner nichts mehr hereinzubringen ist.",
       [E, ("fs", 2), ("fs", 3)])
    MC(X, "r-anfecht", "Eine verschuldete Frau verschenkt ihr Auto an den Sohn, um es vor den Gläubiger*innen zu retten, und wird später insolvent. Wie weit kann eine Anfechtung zurückreichen, wenn der Sohn die Absicht kannte?", "Bis zu 10 Jahre",
       ["1 Jahr", "2 Jahre, nie länger", "Gar nicht, Schenkungen in der Familie sind geschützt"],
       "Schenkungen sind ohne Weiteres anfechtbar, wenn sie in den letzten zwei Jahren vor der Eröffnung stattfanden. Kannte der Beschenkte die Absicht, die Gläubiger*innen zu benachteiligen, reicht die Anfechtung bis zu zehn Jahre zurück. Die Lehrende nannte die 10 Jahre als Prüfungszahl.",
       [I, ("r2", 49), ("fs", 8)])
    MC(X, "r-ins", "Bis wann muss nach der Insolvenzordnung spätestens ein Insolvenzantrag gestellt werden?", "Ohne schuldhaftes Zögern, spätestens 60 Tage nach Eintritt der Zahlungsunfähigkeit",
       ["Spätestens 14 Tage danach", "Spätestens 6 Monate danach", "Es gibt keine Frist"],
       "§ 69 IO verlangt den Antrag ohne schuldhaftes Zögern, spätestens 60 Tage nach Zahlungsunfähigkeit, beim örtlich zuständigen Bezirksgericht. Bei Privatpersonen sieht die Gerichtspraxis laut Skript aber in der Regel von dieser Pflicht und Frist ab.",
       [("r2", 48), ("fs", 8)])
    MC(X, "r-abschoepf", "Ein Abschöpfungsverfahren wird vorzeitig eingestellt, weil der Schuldner seine Pflichten verletzt. Wie lange ist ein neues Abschöpfungsverfahren gesperrt?", "20 Jahre",
       ["3 Jahre", "5 Jahre", "10 Jahre"],
       "Wer den Verpflichtungen nicht nachkommt, dessen Verfahren wird vorzeitig eingestellt, und es gelten lange Sperrfristen für neue Entschuldungsanträge: 10 Jahre nach einem Zahlungsplan, 20 Jahre nach einem Abschöpfungsverfahren.",
       [("r2", 51), ("r2", 52), ("fs", 9)])
    TF(X, "r-abschoepf", "Die dreijährige Variante des Abschöpfungsverfahrens mit Tilgungsplan gibt es für Anträge ab dem 17.7.2026 nicht mehr.", True,
       "Stimmt. Die drei Jahre galten nur für Anträge bis zum 16.7.2026, seither dauert die Abschöpfung wieder fünf Jahre. Laut Fragestunde ist eine Wiedereinführung vielleicht geplant, beschlossen ist sie nicht.",
       [("r2", 50), ("r2", 51), ("fs", 9)])
    MC(X, "r-abschoepf", "Was verlangt das Abschöpfungsverfahren anders als der Zahlungsplan?", "Eine angemessene Erwerbstätigkeit oder nachweisliches Bemühen darum, was die Gläubiger*innen bei Gericht in Frage stellen können",
       ["Die Zustimmung aller Gläubiger*innen", "Dass der Staat die restlichen Schulden zahlt", "Dass das ganze Einkommen gepfändet wird"],
       "Beim Zahlungsplan hält man sich an die vereinbarten Raten. Im Abschöpfungsverfahren geht der pfändbare Teil des Einkommens fünf Jahre an eine Treuhänder*in, und man muss einer angemessenen Erwerbstätigkeit nachgehen oder sich nachweislich darum bemühen. Laut Fragestunde können Gläubiger*innen beantragen zu prüfen, ob diese Bemühungspflicht erfüllt ist.",
       [("r2", 51), ("fs", 9)])
    TF(X, "r-ins", "Ein Ehepaar mit gemeinsamen Schulden kann ein gemeinsames Insolvenzverfahren beantragen.", False,
       "Falsch. Ehegatt*innen mit gemeinsamen Schulden müssen jeweils ein eigenes Insolvenzverfahren beantragen, weil jede Person rechtlich eigenständig ist. Wem was gehört, wird erst bei einer Scheidung aufgeteilt.",
       [("r2", 49), ("fs", 9), ("fs", 10)])
    MC(X, "r-exmin", "Was regelt die Existenzminimumverordnung?", "Wie viel vom Einkommen bei einer Exekution unpfändbar bleibt, abhängig von Einkommen und Unterhaltspflichten",
       ["Wie hoch die Mindestsicherung ist", "Welche Möbel der Exekutor mitnehmen darf", "Wie lange ein Insolvenzverfahren dauert"],
       "Das Justizministerium setzt die unpfändbaren Beträge jährlich in der Existenzminimumverordnung fest: Grundbetrag, Unterhaltsgrundbeträge je Sorgepflicht und Steigerungsbeträge. Einen fixen unpfändbaren Betrag gibt es daher nicht, und das Existenzminimum gilt bei jeder Lohnpfändung, nicht nur in der Insolvenz.",
       [("r2", 38), ("r2", 39), ("fs", 12)])
    MU(X, "r-exe", "Welche Arten der Exekution gibt es zur Hereinbringung von Geld?",
       ["Forderungsexekution, etwa Lohnpfändung", "Fahrnisexekution auf bewegliche Sachen", "Immobiliarexekution auf Wohnung oder Haus"], ["Exekution direkt aus einem Gesetz, ohne Titel", "Pfändung des Existenzminimums"],
       "Die Lehrende nannte drei Arten: Forderungs- oder Einkommensexekution, typisch die Lohnpfändung beim Dienstgeber als Drittschuldner; Fahrnisexekution auf Möbel, Handy und andere bewegliche Sachen; Immobiliarexekution auf Wohnung oder Haus. Sie sind auch gleichzeitig möglich und brauchen immer einen Exekutionstitel.",
       [("r2", 34), ("r2", 35), ("fs", 12), ("fs", 13)])
    TF(X, "r-exe", "Ein iPhone kann grundsätzlich gepfändet werden.", True,
       "Stimmt. Unpfändbar ist nur, was man zum Weiterleben oder für den Beruf braucht, etwa Bett, Kühlschrank, Waschmaschine, einfache Kleidung oder für die Berufsausübung notwendige Gegenstände. Laut Fragestunde kann ein notwendiger Gegenstand unter Umständen gegen einen günstigeren ausgetauscht werden.",
       [("r2", 37), ("fs", 13)])
    MC(X, "r-exe", "Was meint man umgangssprachlich mit dem „Kuckuck“?", "Das Pfändungszeichen, das an gepfändeten Gegenständen angebracht wird",
       ["Den Zahlungsbefehl", "Die Gerichtsvollzieherin selbst", "Eine Mahnung des Inkassobüros"],
       "Bei einer Fahrnispfändung kennzeichnet der*die Gerichtsvollzieher*in gepfändete Sachen mit einem Pfändungszeichen, umgangssprachlich Kuckuck. Die Lehrende fragte in der Fragestunde ausdrücklich nach dem Begriff.",
       [("fs", 13)])

    # ---------------- Staat und Verfassung ----------------
    TF(S, "r-grund", "Die Menschenwürde steht nur Staatsbürger*innen ab 18 Jahren zu.", False,
       "Falsch. Die Menschenwürde kommt jedem Menschen zu, sie hängt weder von der Staatsbürgerschaft noch von der Volljährigkeit ab.",
       [("fs", 13)])
    TF(S, "r-grund", "Die Europäische Menschenrechtskonvention hat in Österreich Verfassungsrang.", True,
       "Stimmt. Die EMRK wurde 1964 in die Verfassung übernommen und gehört neben dem B-VG und dem Staatsgrundgesetz zu den zentralen Teilen der Bundesverfassung. Über sie wacht der EGMR in Straßburg, der nicht zur EU gehört.",
       [("rv", 35), ("rv", 84), ("fs", 15)])
    TF(S, "r-grund", "Alle Grundrechte sind im B-VG taxativ, also abschließend, aufgezählt.", False,
       "Falsch. Die Grundrechte stehen in mehreren Quellen, etwa im Staatsgrundgesetz von 1867, in der EMRK und in der Grundrechtecharta der EU. Taxativ heißt ausschließlich oder abschließend aufgezählt.",
       [("rv", 75), ("r3", 6), ("fs", 15)])
    TF(S, "r-mandat", "Ein Rechtsstaat braucht eine gesetzlich festgelegte Mindestanzahl an Parteien.", False,
       "Falsch, eine feste Mindestanzahl gibt es nicht. Für einen demokratischen Rechtsstaat ist laut Fragestunde aber wichtig, dass verschiedene politische Positionen vertreten sein können und nicht nur eine Partei existiert.",
       [("fs", 13), ("fs", 14)])
    MC(S, "r-mandat", "Wie viele Abgeordnete hat der Nationalrat?", "183",
       ["165", "60", "100"],
       "Der Nationalrat hat 183 Abgeordnete, eine Reduzierung auf 165 war nur angedacht. Der Bundesrat hat derzeit 60 Mitglieder, die von den Landtagen entsandt werden.",
       [("rv", 42), ("fs", 14)])
    MC(S, "r-mandat", "Was unterscheidet das freie Mandat von einer freien Abgeordneten?", "Freies Mandat: Alle Abgeordneten entscheiden rechtlich nach eigener Überzeugung. Freie Abgeordnete: Sie gehört keinem Parlamentsklub an.",
       ["Beides bedeutet dasselbe", "Freies Mandat: Abgeordnete ohne Partei. Freie Abgeordnete: Abgeordnete mit Klubzwang", "Freie Abgeordnete werden direkt gewählt, alle anderen von den Parteien bestimmt"],
       "Das freie Mandat haben alle Abgeordneten: keine rechtlich bindenden Vorgaben, auch nicht von der eigenen Partei. Freie Abgeordnete sind Mandatar*innen ohne Klub, zum Beispiel nach einem Parteiaustritt mit behaltenem Mandat. Die Lehrende nannte genau diese Verwechslung als Prüfungsfalle.",
       [("rv", 39), ("fs", 14)])
    TF(S, "r-mandat", "Der Klubzwang verpflichtet Abgeordnete rechtlich dazu, mit ihrer Partei zu stimmen.", False,
       "Falsch. Abgeordnete haben ein freies Mandat. Klubzwang ist in der Realität häufig, er ist aber nur eine Absprache und rechtlich nicht bindend.",
       [("rv", 39), ("fs", 14)])
    MC(S, "r-direkt", "Was bedeutet indirekte Demokratie?", "Die Bürger*innen wählen Vertreter*innen, die dann die politischen Entscheidungen treffen",
       ["Die Bürger*innen stimmen über jedes Gesetz selbst ab", "Die Regierung entscheidet ohne Wahl", "Nur die Länder entscheiden, nicht der Bund"],
       "Österreich ist eine mittelbare, parlamentarisch-repräsentative Demokratie: Gewählte Vertreter*innen in Nationalrat und Landtagen entscheiden. Bei der direkten Demokratie entscheiden die Bürger*innen selbst, etwa in einer Volksabstimmung.",
       [("rv", 39), ("fs", 15)])
    TF(S, "r-direkt", "Die Volksabstimmung ist ein Instrument der direkten Demokratie.", True,
       "Stimmt. Bei der Volksabstimmung entscheiden die Bürger*innen selbst, und sie ist verbindlich. Bei einer Gesamtänderung der Bundesverfassung ist sie sogar Pflicht.",
       [("fs", 15), ("fs", 16), ("f2", 3)])
    MC(S, "r-stufen", "Wo steht der Oberste Gerichtshof im Verhältnis zu den Gesetzen?", "Nicht über ihnen: Gerichte wenden die Gesetze an und sind an sie gebunden",
       ["Über der Verfassung, weil er das letzte Wort hat", "Zwischen Verfassung und einfachen Gesetzen", "Ganz oben, gleichrangig mit den Baugesetzen"],
       "Urteile stehen im Stufenbau wie Bescheide und Verträge unter Verordnungen und Gesetzen. Auch der OGH ist kein Rechtsetzungsorgan über den Gesetzen, er wendet sie an; die Höchstgerichte geben aber den Interpretationsrahmen vor, an den sich untere Gerichte halten.",
       [("rv", 27), ("f2", 1), ("fs", 14)])
    MC(S, "r-prinz", "Welches davon ist kein Baugesetz der Bundesverfassung?", "Das Gerechtigkeitsprinzip",
       ["Das republikanische Prinzip", "Das liberale Prinzip", "Das bundesstaatliche Prinzip"],
       "Die sechs Baugesetze sind das demokratische, republikanische, bundesstaatliche, rechtsstaatliche, gewaltenteilende und liberale Prinzip. Ein Gerechtigkeitsprinzip wurde in der Fragestunde als Antwort genannt und von der Lehrenden nicht bestätigt.",
       [("rv", 36), ("fs", 17)])
    MC(S, "r-rechtsstaat", "Wozu dient die Gewaltenteilung?", "Sie teilt die staatliche Macht auf, damit sich die Gewalten gegenseitig kontrollieren und begrenzen",
       ["Damit alle Parteien gleich viele Posten bekommen", "Damit Bund und Länder gleich viel Geld bekommen", "Damit Gerichte selbst Gesetze beschließen können"],
       "Gesetzgebung und Vollziehung sind getrennt, ebenso Gerichtsbarkeit und Verwaltung. So soll keine Stelle zu viel Macht haben. Die Fragestunde nannte die gleich vielen Posten für alle Parteien als falsche Antwort.",
       [("f5", 1), ("fs", 17)])
    MC(S, "r-ngo", "Wie werden öffentliche Aufgaben vorwiegend finanziert?", "Durch Steuern",
       ["Durch Spenden", "Durch Krankenversicherungsbeiträge", "Durch Sozialversicherungsbeiträge"],
       "Öffentliche Aufgaben werden vorwiegend durch Steuern finanziert. Kranken- und Sozialversicherungsbeiträge haben einen eigenen Zweck, und Spenden sind keine zentrale Finanzierungsquelle der Verwaltung.",
       [("fs", 15)])
    BU(S, "r-ngo", "Staatliche Einrichtung oder NGO?", ["Staatlich", "NGO"],
       [("Volksanwaltschaft", 0), ("Rechnungshof", 0), ("Kinder- und Jugendhilfe", 0), ("Caritas", 1), ("Rotes Kreuz", 1), ("Volkshilfe", 1)],
       "Volksanwaltschaft, Rechnungshof und Kinder- und Jugendhilfe sind staatliche Einrichtungen, Caritas, Rotes Kreuz und Volkshilfe sind NGOs. Achtung: Im Gesetz heißt es Kinder- und Jugendhilfe, nicht Jugendamt.",
       [("fs", 16), ("fs", 2)])
    MC(S, "r-ngo", "Was ist laut Prüfungsfragestunde das Bundesrechenzentrum (BRZ)?", "Ein Dienstleistungsunternehmen des öffentlichen Rechts mit eigener Rechtspersönlichkeit",
       ["Eine private GmbH", "Eine Abteilung des Rechnungshofs", "Eine NGO für Datenschutz"],
       "So stellte es die Lehrende in der Fragestunde dar: keine private Firma, sondern ein Unternehmen der öffentlichen Hand mit eigener Rechtspersönlichkeit. In Skript und Folien kommt das BRZ nicht vor.",
       [("fs", 7)])
    MC(S, "r-eu", "Welches Amt hat Ursula von der Leyen?", "Präsidentin der Europäischen Kommission",
       ["Präsidentin des Europäischen Parlaments", "Präsidentin des Europäischen Rates", "Präsidentin des EuGH"],
       "Die Kommission vertritt die Interessen der EU und ist Hüterin der Verträge, ihre Präsidentin sitzt auch im Europäischen Rat. Laut Fragestunde muss man nicht alle EU-Politiker*innen kennen, aber die Ämter.",
       [("rv", 80), ("rv", 85), ("fs", 7)])

    # ---------------- Mindestsicherung ----------------
    MU(M, "r-wmg", "Für welche Bereiche besteht in der Wiener Mindestsicherung ein Rechtsanspruch?",
       ["Lebensunterhalt", "Wohnbedarf", "Krankheit", "Schwangerschaft und Entbindung"], ["Hilfe in besonderen Lebenslagen", "Schuldentilgung"],
       "§ 3 WMG deckt den Mindeststandard bei Lebensunterhalt, Wohnen, Krankheit sowie Schwangerschaft und Entbindung, darauf besteht ein Rechtsanspruch. Die Hilfe in besonderen Lebenslagen ist eine vertragliche Leistung ohne Rechtsanspruch.",
       [("r2", 69), ("r2", 70)])
    MC(M, "r-wmg", "Welche Leistung der Wiener Mindestsicherung ist eine vertragliche Leistung ohne Rechtsanspruch?", "Die Hilfe in besonderen Lebenslagen (HibL)",
       ["Die Mietbeihilfe", "Die Leistung zur Sicherung des Lebensunterhalts", "Die Leistungen bei Krankheit"],
       "Die HibL (§ 39 WMG) geht über den Lebensbedarf hinaus und kann auch bei höherem Einkommen gewährt werden, etwa bei einmaligen, unvorhergesehenen Aufwendungen oder Mietrückständen vor der Delogierung. Sie setzt voraus, dass die Notlage nachhaltig überwunden werden kann.",
       [("r2", 70), ("r2", 75)])
    MU(M, "r-wmg", "Wer kann in Wien Mindestsicherung bekommen, wenn die übrigen Voraussetzungen erfüllt sind?",
       ["Österreichische Staatsbürger*innen", "Asylberechtigte", "Erwerbstätige EU-Bürger*innen", "Personen mit Daueraufenthalt – EG"], ["Asylwerbende während des laufenden Verfahrens", "Subsidiär Schutzberechtigte, seit 2026"],
       "Neben Österreicher*innen sind Gleichgestellte anspruchsberechtigt, wenn sie sich rechtmäßig aufhalten und nicht zum Sozialhilfebezug eingereist sind. Asylwerbende haben bis zum Abschluss des Verfahrens keinen Anspruch, subsidiär Schutzberechtigte haben ihn mit 1.1.2026 verloren und sind auf die Grundversorgung angewiesen.",
       [("r2", 71), ("r2", 72)])
    MU(M, "r-wmg", "Welche Voraussetzungen nennt das Skript für den Anspruch auf Wiener Mindestsicherung?",
       ["Lebensmittelpunkt und tatsächlicher Aufenthalt in Wien", "Der Bedarf ist nicht mit Arbeitskraft, eigenen Mitteln oder Leistungen Dritter zu decken", "Antrag und Mitwirkung im Verfahren"],
       ["Österreichische Staatsbürgerschaft in jedem Fall", "Mindestens ein Jahr Hauptwohnsitz in Wien"],
       "Anspruch setzt Lebensmittelpunkt und Aufenthalt in Wien, Bedürftigkeit trotz Einsatz eigener Kräfte und Mittel sowie Antrag und Mitwirkung voraus. Die Staatsbürgerschaft ist keine Bedingung, auch Gleichgestellte wie Asylberechtigte haben Anspruch.",
       [("r2", 70), ("r2", 71)])
    TF(M, "r-wmg", "Mindestsicherung kann auch rückwirkend für vergangene Monate zuerkannt werden.", False,
       "Falsch. Die Mindestsicherung hat rechtzeitig einzusetzen, eine Zuerkennung für die Vergangenheit ist nicht möglich. Sie kann aber vorbeugend einsetzen, um eine drohende Notlage abzuwenden.",
       [("r2", 69)])

    # ---------------- Stolperfallen aus der Mitschrift ----------------
    TRAP("Ausfallsbürg*in: erst nach allen Exekutionen?",
         "Die Mitschrift sagt, die Ausfallsbürg*in hafte erst, wenn Lohnpfändung, Fahrnis- und Immobiliarexekution ausgeschöpft sind. Das stimmt als Regel. Wird über den Hauptschuldner aber das Insolvenzverfahren eröffnet, kann auch die Ausfallsbürg*in sofort herangezogen werden.",
         [("fs", 2), ("r2", 49), ("msk", 110)])
    TRAP("Gewährleistung: früher ein halbes Jahr?",
         "Laut Mitschrift wurde die Vermutungsfrist von einem halben Jahr auf ein Jahr verlängert. Das Skript unterscheidet: Bei einer Ware gilt die Vermutung ein Jahr, bei einem Werk weiterhin 6 Monate.",
         [("fs", 11), ("r2", 57)])
    TRAP("60 Tage für den Insolvenzantrag",
         "Die 60 Tage stehen so im Gesetz und wurden in der Fragestunde ausdrücklich genannt. Das Skript ergänzt, dass die Gerichtspraxis bei Privatpersonen meist von der Antragspflicht und der Frist absieht.",
         [("fs", 8), ("r2", 48)])
    TRAP("RSa-Beispiele der Mitschrift",
         "Die Mitschrift nennt Finanzamt-Sachen und das Vaterschaftsanerkenntnis als RSa-Beispiele und markiert sie selbst als unsicher; im Skript stehen sie nicht. Laut Skript gehen Strafverfügungen seit 2013 nicht mehr RSa, nur gewisse Erledigungen in Verwaltungsstrafsachen. Zahlungsbefehle gehen RSb, darin stimmen beide überein.",
         [("fs", 7), ("r2", 21), ("r2", 41)])
    TRAP("Taxativ und „fakultativ“",
         "Die Mitschrift erklärt fakultativ als Gegenteil von taxativ. Fakultativ heißt aber wahlweise; eine nicht abschließende, beispielhafte Aufzählung heißt in der Rechtssprache demonstrativ. Für die Prüfung zählt: taxativ heißt ausschließlich oder abschließend aufgezählt.",
         [("fs", 15), ("r3", 6)])
    TRAP("„Hebel“ bei der Mindestsicherung",
         "In der Mitschrift steht bei den Mindestsicherungsthemen der Begriff „Hebel“ ohne Erklärung. Gemeint ist sehr wahrscheinlich die HibL, die Hilfe in besonderen Lebenslagen: eine vertragliche Leistung der WMS ohne Rechtsanspruch.",
         [("fs", 19), ("r2", 75)])
