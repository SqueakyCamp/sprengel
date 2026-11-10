"""MATS-Pruefungsfragen (Wunsch vom 11.11.2026): Fragen aus der Sammlung „MATS Fragen“ (Mitschriften von Studierenden
aus der Pruefungseinsicht). Die Fragen stammen aus der Sammlung, die Antworten wurden gegen Praesentation und Skriptum
geprueft und tragen deren Seiten. Wo die Mitschrift etwas anderes sagt als die Unterlagen, steht das in TRAP.
Format wie in der Pruefung: Multiple Choice (auch mehrere richtig) und Ja/Nein-Fragen. Jede Karte hat pf=<Themenblock>."""

BLOCKS = ["Wohnungslosenhilfe", "Wiener Mindestsicherung", "Schuldenberatung", "Familie und Ansprüche", "Knifflige Fragen"]
INFO = "Laut Mitschrift: 40 Fragen in 30 Minuten, keine offenen Fragen, vor allem Multiple Choice (oft mehrere richtig) und einige Ja/Nein-Fragen. Themen: Schuldenberatung, WMS, Wohnungslosenhilfe und Leistungen im Familienbereich."


def add(c):
    def tag(block):
        c.cards[-1]["pf"] = block

    def MC(b, t, q, right, wrong, why, src):
        c.MC(t, [], q, right, wrong, why, src); tag(b)

    def TF(b, t, q, val, why, src):
        c.TF(t, [], q, val, why, src); tag(b)

    def MU(b, t, q, right, wrong, why, src):
        c.MULTI(t, [], q, right, wrong, why, src); tag(b)

    W, M, S, F, K = BLOCKS

    # ---------------- Wohnungslosenhilfe ----------------
    MU(W, "m-angebote", "Welche dieser Angebote zählen zur Wiener Wohnungslosenhilfe?",
       ["Mobil betreutes Wohnen", "Stationär betreutes Wohnen", "Chancenhäuser", "Mutter-Kind-Einrichtungen"], ["Frauenhäuser"],
       "Mobil und stationär betreutes Wohnen, Chancenhäuser und Mutter-Kind-Einrichtungen sind Angebote der WWH, die der FSW fördert. Frauenhäuser gehören nicht dazu, auch wenn sie Menschen ein Dach bieten: Sie sind Opferschutzeinrichtungen. Laut Mitschrift war genau das die Falle in der Prüfung.",
       [("msk", 96), ("msk", 97), ("msk", 98)])
    TF(W, "m-angebote", "Für einen Platz im Chancenhaus gibt es keine formalen Voraussetzungen.", True,
       "Stimmt. Chancenhäuser bieten akut obdachlosen Menschen eine niederschwellige und voraussetzungslose Wohnmöglichkeit. Ob jemand Anspruch auf weitere WWH-Leistungen hat, wird erst während des Aufenthalts geprüft.",
       [("msk", 97)])
    MU(W, "m-angebote", "Was bieten Chancenhäuser ihren Bewohner*innen?",
       ["Direkt zugängliche Plätze in Einzel-, Doppel- oder Paarzimmern mit Tagesaufenthalt", "Sozialarbeiterische Beratung vor Ort ab dem ersten Tag", "Erarbeitung einer Wohnperspektive"],
       ["Eine Gemeindewohnung nach drei Monaten", "Einen unbefristeten Mietvertrag"],
       "Chancenhäuser sind niederschwellig und voraussetzungslos. Die Beratung beginnt am ersten Tag und zielt auf eine Wohnperspektive, eine eigene Wohnung ist damit aber nicht garantiert.",
       [("msk", 97)])
    MC(W, "m-ethos", "Welche Menschen zählen nach der ETHOS-Typologie zu den obdachlosen Menschen?",
       "Menschen, die im öffentlichen Raum leben, und Menschen in Notschlafstellen oder Wärmestuben",
       ["Menschen in Frauenhäusern", "Menschen, die von Delogierung bedroht sind", "Menschen in überfüllten Wohnungen"],
       "Obdachlos sind nach ETHOS Menschen ohne jede Unterkunft (öffentlicher Raum) und Menschen in Notunterkünften wie Notschlafstellen und Wärmestuben. Frauenhäuser zählen zur Kategorie wohnungslos, drohende Delogierung zu ungesichertem Wohnen, Überbelag zu ungenügendem Wohnen.",
       [("msk", 83)])
    MU(W, "m-wwhrecht", "Welche Begriffe gehören zum Förderwesen der Wiener Wohnungslosenhilfe?",
       ["Anerkennung", "Objektförderung", "Subjektförderung"], ["Befürwortung", "Überschuldung"],
       "Der FSW unterscheidet Subjekt-, Objekt- und Projektförderung. In der Subjektförderung brauchen Einrichtungen eine Anerkennung, um Klient*innen mit Förderbewilligung zu betreuen. Die Befürwortung gehört zur Sozialen Wohnungsvergabe, nicht zum Förderwesen.",
       [("msk", 90), ("msk", 91), ("msk", 92)])
    MC(W, "m-wwhrecht", "Worin ist die Wiener Wohnungslosenhilfe gesetzlich geregelt?", "Im Wiener Sozialhilfegesetz",
       ["Im Wiener Mindestsicherungsgesetz", "Im Mietrechtsgesetz", "Im Wiener Wohnbauförderungsgesetz"],
       "Gesetzliche Grundlage der WWH ist das Wiener Sozialhilfegesetz: Unterkunft gehört dort zu den Hilfen zur Sicherung des Lebensbedarfes. Die Mindestsicherung hat ein eigenes Gesetz, das ist eine häufige Verwechslung.",
       [("msk", 89)])
    MC(W, "m-swv", "Wer erstellt ein Ansuchen auf eine Gemeindewohnung im Rahmen der Sozialen Wohnungsvergabe?",
       "Die soziale Einrichtung, die die Person betreut, in Form einer Befürwortung",
       ["Die Schuldenberatung", "Die Person selbst online bei Wiener Wohnen", "Das Sozialzentrum der MA 40"],
       "Bei betreuten Personen läuft der Antrag über die betreuende Einrichtung, etwa aus der WWH, der Kinder- und Jugendhilfe oder Neustart. Sie legt einen Sozialbericht bei, wenn sie meint, dass die Person dauerhaft wohnen kann. Die Schuldenberatung macht das laut Mitschrift ausdrücklich nicht.",
       [("msk", 76)])
    MU(W, "m-swv", "Welche Grundvoraussetzungen gelten für eine Gemeindewohnung über die Soziale Wohnungsvergabe?",
       ["Durchgehende Hauptwohnsitzmeldung in Wien in den letzten 24 Monaten", "Österreichische oder gleichgestellte Staatsbürgerschaft, Flüchtlingsstatus oder Daueraufenthalt EU", "Keine offenen Forderungen bei Wiener Wohnen"],
       ["Ein Mindesteinkommen in Höhe des doppelten Mindeststandards", "Eine Bestätigung der Schuldenberatung"],
       "Dazu kommen Volljährigkeit, niedrige Einkommensgrenzen, keine Wohnimmobilie und kein Negativeintrag in der Mieter*innenhistorie. Das Einkommen muss also unter einer Grenze liegen, nicht darüber.",
       [("msk", 76)])
    TF(W, "m-wohnticket", "Alle in Wien hauptwohnsitzgemeldeten Personen bekommen eine Gemeindewohnung.", False,
       "Falsch. Man muss die Grundvoraussetzungen erfüllen, etwa die Wohnsitzdauer, die Staatsbürgerschaft oder Gleichstellung und die Einkommensgrenze. Seit der Wohnungsvergabe NEU entscheiden dann Bonuspunkte über die Reihung.",
       [("msk", 72), ("msk", 73)])
    MC(W, "m-wohnkomm", "Für wen sind die wohnpartner zuständig?", "Ausschließlich für Mieter*innen im Wiener Gemeindebau",
       ["Für alle Mieter*innen in Wien", "Für Mieter*innen von Genossenschaftswohnungen", "Für wohnungslose Menschen ohne Anspruch auf WWH"],
       "Die wohnpartner gehören zum Wohnservice Wien und arbeiten nur im Gemeindebau: mit Gemeinwesenarbeit, Konfliktarbeit, Mediation und Vernetzung. Ziel ist ein gutes Zusammenleben in der Nachbarschaft.",
       [("msk", 72)])
    MU(W, "m-nichtanspr", "Welche Aufgaben hat die Sozial- und Rückkehrberatung der Caritas?",
       ["Kostenlose, mehrsprachige Beratung für wohnungslose EU-Bürger*innen", "Vergabe der Notquartiersplätze im Winterpaket gemeinsam mit dem P7"],
       ["Ausstellen von Förderbewilligungen für betreutes Wohnen", "Delogierungsprävention im Gemeindebau"],
       "Die Sozial- und Rückkehrberatung ist für Menschen da, die keinen Anspruch auf WWH-Leistungen haben, oft EU-Bürger*innen. Förderbewilligungen vergibt das bzWO, Delogierungsprävention machen andere Stellen.",
       [("msk", 92), ("msk", 93)])
    MU(W, "m-nichtanspr", "Welche Angebote gibt es für wohnungslose Menschen ohne Anspruch auf WWH-Leistungen?",
       ["Die Sozial- und Rückkehrberatung", "Notquartiere im Winterpaket", "Chancenhäuser"],
       ["Mobil betreutes Wohnen", "Stationär betreutes Wohnen"],
       "Wer die Förderkriterien nicht erfüllt, kann die voraussetzungslosen Angebote nutzen: Winterpaket, Chancenhäuser, Tageszentren und die Sozial- und Rückkehrberatung. Betreutes Wohnen setzt dagegen eine Förderbewilligung voraus.",
       [("msk", 92), ("msk", 93), ("msk", 97)])
    MU(W, "m-angebote", "Was zählt zu den niederschwelligen Angeboten der Wiener Wohnungslosenhilfe?",
       ["Tageszentren", "Straßensozialarbeit", "Das Winterpaket"], ["Mutter-Kind-Einrichtungen", "Stationär betreutes Wohnen"],
       "Niederschwellig heißt: Akutberatung, Erst- und Basisversorgung, leicht und unbürokratisch zugänglich. Dazu zählen Tageszentren wie Gruft oder Obdach Josi, Straßensozialarbeit, das Internetcafé Zwischenschritt und das Winterpaket.",
       [("msk", 96), ("msk", 97)])
    MU(W, "m-ursachen", "Was zählt zu den häufigsten Ursachen von Wohnungslosigkeit?",
       ["Einkommensarmut", "Mangel an leistbarem Wohnraum", "Psychische Erkrankungen und Sucht"], ["Ein zu großes Wohnungsangebot", "Ein hoher Bildungsabschluss"],
       "Wohnungslosigkeit ist kumulierte Armut: Einkommensarmut und Mangel an leistbarem Wohnraum treffen mit Arbeitslosigkeit, Krankheit, Sucht oder Lebenskrisen zusammen. Meist kommen mehrere Gründe zusammen.",
       [("msk", 85), ("msk", 86)])
    MU(W, "m-sicher", "Welche Stellen sind in Wien für Delogierungsprävention zuständig?",
       ["FAWOS (Volkshilfe Wien)", "Das Zielgruppenzentrum Wohnungssicherung der MA 40", "Die MA 11 bei Gemeindebau-Haushalten mit minderjährigen Kindern"],
       ["Das bzWO", "Die Schuldenberatung Wien"],
       "Zuständig ist je nach Wohnung: FAWOS für Privat- und Genossenschaftswohnungen, die MA 11 für Gemeindebau-Haushalte mit Kindern, die MA 40 für Gemeindebau-Haushalte ohne Kinder. Das bzWO kommt erst ins Spiel, wenn die Wohnung schon verloren ist.",
       [("msp", 28)])
    TF(W, "m-ksow", "Bewilligungen für mobil betreutes Wohnen vergibt das Zielgruppenzentrum Wohnen der MA 40.", False,
       "Falsch. Förderbewilligungen für alle betreuten Wohnplätze der WWH vergibt das bzWO (Beratungszentrum Wohnungslosenhilfe) des FSW. Die MA 40 ist für Mindestsicherung und Wohnungssicherung zuständig.",
       [("msp", 45), ("msk", 95)])
    TF(W, "m-ksow", "Die Leistung mobil betreutes Wohnen bewilligt das Tageszentrum P7 der Caritas.", False,
       "Falsch. Das P7 ist eine Beratungsstelle, die vermittelt und abklärt. Bewilligen kann nur das bzWO des FSW nach Prüfung der Fördervoraussetzungen.",
       [("msk", 95), ("msk", 96)])
    TF(W, "m-sicher", "Das bzWO ist für Delogierungsprävention zuständig.", False,
       "Falsch. Delogierungsprävention machen FAWOS, MA 11 und MA 40. Das bzWO prüft die Förderung von Wohnplätzen für Menschen, die schon wohnungslos sind; die Strategie 2022 will aber eine Nahtstelle zwischen beiden schaffen.",
       [("msp", 28), ("msp", 40)])
    MC(W, "m-sicher", "Wer ist für Gemeindewohnungsmieter*innen mit minderjährigen Kindern bei drohender Delogierung zuständig?",
       "Die MA 11", ["Die FAWOS", "Das U25", "Das bzWO"],
       "Bei Kindern im Gemeindebau ist die Kinder- und Jugendhilfe (MA 11) zuständig. Die finanziellen Hilfen dafür werden aber als HibL bei der MA 40 beantragt.",
       [("msp", 28)])

    # ---------------- Wiener Mindestsicherung ----------------
    MC(M, "m-ablauf", "Wer vollzieht in Wien das Wiener Mindestsicherungsgesetz?", "Die MA 40",
       ["Die MA 11", "Der Fonds Soziales Wien", "Das AMS Wien"],
       "Die Magistratsabteilung 40 (Soziales, Sozial- und Gesundheitsrecht) setzt das Gesetz um. Den Antrag stellt man pro Bedarfsgemeinschaft dort.",
       [("msk", 32)])
    MC(M, "m-ablauf", "Womit entscheidet die MA 40 über einen Antrag auf Wiener Mindestsicherung?", "Mit einem Bescheid",
       ["Mit einer formlosen Benachrichtigung", "Mit einem Urteil", "Mit einem Vertrag"],
       "Über den WMS-Antrag ergeht ein Bescheid, spätestens 3 Monate nach dem vollständigen Antrag. Gegen ihn gibt es die Beschwerde an das Verwaltungsgericht Wien. Bei der HibL gibt es keinen Rechtsanspruch.",
       [("msp", 7), ("msk", 33)])
    MC(M, "m-ablauf", "Wie heißt das Rechtsmittel gegen einen Bescheid der MA 40 über einen Mindestsicherungsantrag?", "Beschwerde",
       ["Einspruch", "Berufung", "Revision"],
       "Gegen den Bescheid kann man binnen 4 Wochen Beschwerde einbringen, bei der MA 40; entscheiden wird im Verwaltungsgericht Wien. Einspruch heißt das Mittel gegen einen Zahlungsbefehl, nicht gegen einen Bescheid.",
       [("msp", 7), ("msp", 36)])
    MU(M, "m-vor", "Was gehört zu den Anspruchsvoraussetzungen für die WMS?",
       ["Ein Antrag", "Lebensmittelpunkt in Wien", "Zugehörigkeit zum anspruchsberechtigten Personenkreis", "Mitwirkung"],
       ["Mindestens fünf Jahre Hauptwohnsitz in Wien", "Österreichische Staatsbürgerschaft"],
       "Dazu kommt ein Bedarf, der nicht durch Arbeitskraft, eigenes Vermögen oder Leistungen Dritter gedeckt werden kann (Subsidiarität). Die Staatsbürgerschaft allein ist kein Muss, auch Gleichgestellte haben Anspruch.",
       [("msp", 8)])
    MU(M, "m-person", "Wer bekommt Wiener Mindestsicherung?",
       ["Österreichische Staatsbürger*innen", "Asylberechtigte", "Menschen mit Daueraufenthalt EU"],
       ["Asylwerber*innen", "Subsidiär Schutzberechtigte"],
       "Seit der Novelle 2026 sind subsidiär Schutzberechtigte ausgeschlossen, ebenso Asylwerbende, Ausreisepflichtige und Geduldete. Die Mitschrift nennt subsidiär Schutzberechtigte noch als anspruchsberechtigt, das ist überholt.",
       [("msp", 10), ("msp", 11)])
    MC(M, "m-eu", "Unter welcher Bedingung haben EU/EWR-Bürger*innen (inklusive Schweiz) Anspruch auf WMS?",
       "Wenn sie erwerbstätig sind, die Erwerbstätigeneigenschaft behalten haben oder das Daueraufenthaltsrecht erworben haben",
       ["Sobald sie in Wien gemeldet sind", "Nur wenn sie mit Österreicher*innen verheiratet sind", "Erst nach zehn Jahren in Österreich"],
       "EU-Bürger*innen sind gleichgestellt, solange sie arbeiten, die Erwerbstätigeneigenschaft erhalten bleibt (etwa bei unfreiwilliger Arbeitslosigkeit mit AMS-Meldung) oder sie nach 5 Jahren Daueraufenthalt haben. Eine Meldeadresse allein reicht nicht.",
       [("msp", 10), ("msk", 36)])
    TF(M, "m-bg", "Ein volljähriges, erwerbstätiges Kind über 21 bildet eine eigene Bedarfsgemeinschaft, auch wenn es bei den Eltern wohnt.", True,
       "Stimmt. Zur BG der Eltern gehören minderjährige Kinder und Schüler*innen bis 21, wenn die Schule vor 18 begann. Ein älteres Kind bildet eine eigene BG, in einer Wohnung können mehrere BGs leben.",
       [("msp", 9), ("msk", 34)])
    TF(M, "m-bg", "Geschwister und Mitbewohner*innen gehören zur eigenen Bedarfsgemeinschaft.", False,
       "Falsch. Eine BG bilden Menschen im gemeinsamen Haushalt, zwischen denen Unterhaltsansprüche bestehen, dazu Lebensgefährt*innen. Zwischen Geschwistern und Mitbewohner*innen gibt es keine Unterhaltspflicht.",
       [("msp", 9), ("msk", 33)])
    MU(M, "m-bg", "Wer gehört zu einer Bedarfsgemeinschaft?",
       ["Ehepartner*innen und eingetragene Partner*innen", "Lebensgefährt*innen", "Unterhaltsberechtigte minderjährige Kinder"],
       ["Geschwister", "Mitbewohner*innen einer WG"],
       "Die Bedarfsgemeinschaft folgt den Unterhaltsbeziehungen im Haushalt, Lebensgefährt*innen kommen dazu. Volljährige Schüler*innen bis 21 gehören dazu, wenn sie die Schule vor 18 begonnen haben.",
       [("msp", 9)])
    MU(M, "m-leist", "Welche Leistungen der WMS gibt es ohne Rechtsanspruch?",
       ["Hilfe in besonderen Lebenslagen", "Wiener Energieunterstützung"], ["Mietbeihilfe", "Mindeststandards", "Behindertenzuschlag"],
       "Mit Rechtsanspruch gibt es Mindeststandards, Mietbeihilfe, Behindertenzuschlag und Krankenhilfe. HibL und Energieunterstützung sind Kann-Leistungen, die man gesondert beantragt.",
       [("msp", 12)])
    TF(M, "m-hibl", "Auf die Hilfe in besonderen Lebenslagen (HibL) gibt es einen Rechtsanspruch.", False,
       "Falsch. Die HibL ist eine Förderung ohne Rechtsanspruch, meist einmalig und zweckgebunden. Die Zusage kann an Bedingungen geknüpft werden, etwa eine Eigenleistung oder eine teilweise Rückzahlung.",
       [("msp", 27)])
    MU(M, "m-hibl", "Wofür kann eine Hilfe in besonderen Lebenslagen beantragt werden?",
       ["Mietrückstände zur Abwendung einer Delogierung", "Kosten rund um die Energieversorgung", "Übernahme der Miete während einer Haft"],
       ["Einen Urlaub", "Laufende Ratenzahlungen für einen Kredit"],
       "Die HibL hilft in Notlagen, etwa bei Mietrückständen, Energiekosten, Haushaltsgeräten oder der Miete während einer Haft. Kreditraten gehören nicht dazu.",
       [("msp", 25), ("msp", 27), ("msk", 51)])
    MU(M, "m-sz", "Was gehört zu den Aufgaben der Sozialarbeiter*innen in den Sozialzentren der MA 40?",
       ["Beratung und Betreuung", "Journaldienst und Abklärung"], ["Bearbeitung der Mindestsicherungsanträge", "Vergabe von Gemeindewohnungen"],
       "Sozialarbeiter*innen beraten, machen Journaldienst und Erstabklärung in Krisen. Die Anträge bearbeiten und Bescheide erstellen die Referent*innen. Gemeindewohnungen vergibt die MA 40 nicht.",
       [("msk", 56), ("msk", 57)])
    MU(M, "m-ruhen", "Welche Änderungen müssen WMS-Beziehende der MA 40 melden?",
       ["Änderungen bei den Wohnverhältnissen", "Änderungen beim Aufenthaltsstatus", "Änderungen bei Einkommen und Vermögen", "Abwesenheiten von mehr als zwei Wochen"],
       ["Einen Wechsel der Hausärztin", "Den Kauf eines neuen Handys auf Raten"],
       "Jede Änderung, die für die Bemessung wichtig ist, muss sofort gemeldet werden: Familie, Einkommen, Vermögen, Wohnen, Aufenthalt, Spitals- und Kuraufenthalte, Abwesenheiten über zwei Wochen. Sonst droht eine Rückforderung.",
       [("msp", 25), ("msp", 26), ("msk", 32), ("msk", 33)])
    MU(M, "m-kuerz", "Wann kann die WMS gekürzt werden?",
       ["Wenn die Arbeitskraft nicht eingesetzt wird, etwa bei Verweigerung einer AMS-Maßnahme", "Wenn die Integrationserklärung fehlt", "Bei selbst verursachter Mittellosigkeit"],
       ["Wenn das Kind krank ist", "Wenn man eine Beschwerde gegen den Bescheid einbringt"],
       "Gekürzt wird stufenweise die Leistung für den Lebensunterhalt. Seit Mai 2025 fällt nach zwei Monaten voller Kürzung auch der Wohnanteil weg, bei weiterer Verweigerung wird alles eingestellt.",
       [("msp", 22), ("msp", 23)])
    MU(M, "m-arbeit", "Wer ist von der Pflicht zur Arbeitssuche befreit?",
       ["Personen im Regelpensionsalter", "Werdende Mütter", "Personen, die ein Kind unter drei Jahren betreuen, wenn keine Betreuung möglich ist", "Personen, die Angehörige ab Pflegegeldstufe 3 überwiegend pflegen"],
       ["Alle Alleinerziehenden", "Studierende"],
       "Die Befreiungsgründe sind eng gefasst. Dazu gehören auch Erwerbsunfähige für die Dauer des Gutachtens und Teilnehmende an Alphabetisierungs- oder Deutschkursen bis A2.",
       [("msp", 24)])
    TF(M, "m-arbeit", "Wer WMS bezieht und arbeitsfähig ist, muss jede Arbeit annehmen.", False,
       "Falsch. Es geht um zumutbare Beschäftigung. Wer eine zumutbare Arbeit oder Maßnahme ablehnt, riskiert aber Kürzungen.",
       [("msk", 47), ("msk", 48)])
    TF(M, "m-verm", "Gebrauchsgegenstände wie Waschmaschine oder Geschirrspüler zählen in der WMS zum nicht verwertbaren Vermögen.", True,
       "Stimmt. Nicht verwertbar sind etwa Vermögen unter dem Freibetrag, Gebrauchsgegenstände und ein berufsbedingt nötiges Auto. Sparguthaben über dem Freibetrag muss man dagegen sofort einsetzen.",
       [("msk", 47)])
    MU(M, "m-eink", "Welche Arten von Einkommen unterscheidet die WMS?",
       ["Anrechenbares Einkommen", "Anrechenfreies Einkommen", "Fiktiv anrechenbares Einkommen"], ["Pfändbares Einkommen", "Versteuertes Einkommen"],
       "Anrechenbar sind etwa Lohn, AMS und Kinderbetreuungsgeld, anrechenfrei Pflegegeld, Familienbeihilfe und Sonderzahlungen. Fiktiv angerechnet wird ein Anspruch, den man nicht geltend macht, etwa Unterhalt.",
       [("msp", 20)])
    MC(M, "m-person", "Wer bekommt die Wiener Mindestsicherung jedenfalls nicht?", "Asylwerber*innen bis zum Abschluss ihres Verfahrens",
       ["Asylberechtigte", "Menschen mit Daueraufenthalt EU", "Österreicher*innen mit geringem Einkommen"],
       "Asylwerbende sind ausgeschlossen, sie werden über die Grundversorgung versorgt. Asylberechtigte haben dagegen Anspruch.",
       [("msp", 11)])
    MC(M, "m-dauer", "Welche Personen bekommen eine Dauerleistung der Wiener Mindestsicherung?", "Personen im Regelpensionsalter und dauerhaft arbeitsunfähige Volljährige",
       ["Alle Alleinerziehenden", "Alle Menschen unter 25", "Alle Menschen mit Kindern"],
       "Dauerleistung bekommen Menschen, von denen keine Arbeit erwartet wird: im Regelpensionsalter oder dauerhaft arbeitsunfähig. Sie hat zwei halbe Sonderzahlungen im Jahr.",
       [("msk", 42)])
    MU(M, "m-mobil", "Wer kann einen Mobilpass der Stadt Wien bekommen?",
       ["WMS-Beziehende", "Bezieher*innen einer Pension mit Ausgleichszulage"], ["Asylwerber*innen in der Grundversorgung", "Alle Studierenden"],
       "WMS-Beziehende bekommen den Mobilpass automatisch, Pensionist*innen mit Ausgleichszulage auf Ansuchen. Er bringt etwa das ermäßigte Monatsticket und Einkauf in Sozialmärkten.",
       [("msk", 23)])
    MC(M, "m-wbh", "Wer kann seit 1.3.2024 keine Wohnbeihilfe mehr bekommen?", "WMS-Beziehende, sie bekommen stattdessen die Mietbeihilfe",
       ["Pensionist*innen mit Ausgleichszulage", "Alle Gemeindebaumieter*innen", "Alle Menschen unter 25"],
       "WMS und Wohnbeihilfe schließen sich aus, die Mietbeihilfe übernimmt diese Aufgabe. Pensionist*innen mit Ausgleichszulage bekommen Wohnbeihilfe weiterhin.",
       [("msp", 19)])

    # ---------------- Schuldenberatung ----------------
    TF(S, "m-straf", "Wer die Forderung eines Inkassobüros nicht bezahlt, muss eine Strafe im Gefängnis absitzen.", False,
       "Falsch. Niemand kann in Österreich allein wegen Schulden verurteilt werden. Ein Inkassobüro hat außerdem keine hoheitliche Macht, es kann nur mahnen und Kosten verrechnen.",
       [("msk", 114), ("msk", 116)])
    TF(S, "m-straf", "Wer Kreditschulden nicht bezahlt, macht sich strafbar und muss mit Gefängnis rechnen.", False,
       "Falsch. Schulden allein sind nicht strafbar. Strafbar wird es erst bei eigenen Delikten, etwa Betrug durch neue Schulden trotz Zahlungsunfähigkeit oder Verletzung der Unterhaltspflicht.",
       [("msk", 114)])
    MU(S, "m-straf", "Bei welchen Schulden oder Taten kann es tatsächlich zu einer Freiheitsstrafe kommen?",
       ["Nicht bezahlte Geldstrafen (Ersatzfreiheitsstrafe)", "Verletzung der Unterhaltspflicht", "Betrug durch neue Schulden trotz Zahlungsunfähigkeit"],
       ["Ein offener Kredit", "Eine offene Handyrechnung"],
       "Strafen müssen bezahlt oder als Ersatzfreiheitsstrafe abgesessen werden. Wer schuldhaft keinen Unterhalt zahlt, kann nach § 198 StGB bestraft werden, und neue Schulden mit Bereicherungsvorsatz sind Betrug.",
       [("msk", 107), ("msk", 114)])
    MC(S, "m-inkasso", "Wie viele Mahnungen müssen Gläubiger*innen schreiben, bevor sie die Forderung fällig stellen und etwa ein Inkassobüro beauftragen dürfen?",
       "Keine bestimmte Anzahl; eine Mahnung ist nicht zwingend nötig", ["Drei", "Zwei", "Eine eingeschriebene Mahnung"],
       "Entgegen der verbreiteten Meinung gibt es kein Recht auf drei Mahnungen. Fällig gestellt werden kann schon bei der ersten Mahnung oder ganz ohne, bei Krediten und Konten braucht es laut Präsentation eine Mahnung mit Nachfrist.",
       [("msp", 60), ("msk", 115)])
    MU(S, "m-inkasso", "Was dürfen Inkassobüros?",
       ["Mitarbeiter*innen zur Wohnung schicken", "Angemessene Kosten für ihr Einschreiten verrechnen", "Ratenvereinbarungen mit den Schuldner*innen treffen"],
       ["Gegen den Willen der Schuldner*innen die Wohnung betreten", "Gegenstände pfänden"],
       "Inkassobüros dürfen hinschicken, mahnen und notwendige, angemessene Kosten verrechnen. Den Zutritt zur Wohnung kann man ihnen aber verweigern, pfänden darf nur der*die Gerichtsvollzieher*in.",
       [("msp", 61), ("msk", 116), ("msk", 118)])
    MU(S, "m-gericht", "Was dürfen Gerichtsvollzieher*innen?",
       ["Mit Ausweis die Wohnung betreten", "Pfändbare Gegenstände ins Pfändungsprotokoll aufnehmen"], ["Unpfändbare Gebrauchsgegenstände wegnehmen", "Eine Forderung inhaltlich prüfen"],
       "Bei der Fahrnisexekution dürfen Gerichtsvollzieher*innen die Wohnung betreten und pfändbare Dinge aufnehmen, notfalls nach einem zweiten Termin gewaltsam öffnen. Was für eine einfache Lebensführung nötig ist, bleibt unpfändbar.",
       [("msk", 118)])
    TF(S, "m-gericht", "Beim bedingten Zahlungsbefehl prüft das Gericht, ob die Forderung rechtmäßig zustande gekommen ist.", False,
       "Falsch. Das Gericht prüft nur die Form, nicht ob der Betrag zusteht. Erst bei einem Einspruch binnen 4 Wochen kommt es zum ordentlichen Verfahren mit Prüfung.",
       [("msp", 62), ("msk", 117)])
    MC(S, "m-gericht", "Was passiert, wenn gegen einen bedingten Zahlungsbefehl binnen 4 Wochen kein Einspruch erhoben wird?",
       "Er wird rechtskräftig und die Gläubiger*innen erhalten einen Exekutionstitel", ["Das Verfahren wird eingestellt", "Es kommt automatisch zu einer Tagsatzung", "Die Schuld verjährt"],
       "Ohne Einspruch wird der Zahlungsbefehl zum Exekutionstitel, mit dem 30 Jahre lang Exekution geführt werden kann. Darum muss Gerichtspost sofort gelesen werden.",
       [("msp", 62), ("msk", 117)])
    MU(S, "m-strafe", "Wer darf eine Geldstrafe verhängen?",
       ["Ein Gericht", "Verwaltungsbehörden wie die Polizei", "Finanz- und Zollbehörden"], ["Die Wiener Linien", "Ein Inkassobüro"],
       "Strafen dürfen nur Behörden verhängen. Die erhöhte Fahrscheingebühr der Wiener Linien ist darum keine Strafe, sondern eine normale Forderung.",
       [("msk", 107)])
    MC(S, "m-anam", "Was ist das Ziel der Erstberatung in der Schuldenberatung?",
       "Einen Überblick über Einkommen, Ausgaben, Vermögen und Schulden gewinnen und gefährliche Schulden abklären",
       ["Sofort mit allen Gläubiger*innen verhandeln", "Den Privatkonkurs bei Gericht einbringen", "Die Schulden der Person vollständig übernehmen"],
       "Die Erstberatung ist eine Anamnese der Ist-Situation. Priorität haben gefährliche Schulden und existenzsichernde Schritte; Verhandlungen mit Gläubiger*innen kommen erst in der laufenden Beratung.",
       [("msk", 106)])
    MC(S, "m-gef", "Als gefährlich werden Schulden bezeichnet, die …", "… die Existenz bedrohen, weil sie besonders unangenehme Folgen haben",
       ["… besonders hoch sind", "… bei einer Bank bestehen", "… älter als drei Jahre sind"],
       "Gefährlich sind Schulden, deren Folgen die Existenz bedrohen: Delogierung, Abschaltung der Energie, Ersatzfreiheitsstrafe. Auf die Höhe kommt es nicht an.",
       [("msp", 67), ("msk", 106)])
    MU(S, "m-gef", "Was zählt zu den gefährlichen Schulden?",
       ["Mietschulden", "Energieschulden", "Geldstrafen", "Unterhaltsschulden (Alimente)", "Ein überzogenes Girokonto"],
       ["Ein Konsumkredit", "Offene Rechnungen beim Versandhandel"],
       "Miete, Energie, Strafen, Alimente und Kontoüberzug können existenzielle Folgen haben. Kredite und offene Rechnungen sind normale Schulden, die im Gesamtplan geregelt werden.",
       [("msp", 67)])
    MU(S, "m-gruende", "Was sind häufige Gründe für Überschuldung?",
       ["Arbeitslosigkeit oder Einkommensverschlechterung", "Umgang mit Geld", "Gescheiterte Selbständigkeit", "Persönliche Härtefälle wie Krankheit"],
       ["Ein zu hohes Einkommen", "Zu viele Mahnungen"],
       "Arbeitslosigkeit und Einkommensverlust sind der häufigste Grund, dann Umgang mit Geld, gescheiterte Selbständigkeit, Härtefälle und Trennung. Oft wirken mehrere Gründe zusammen.",
       [("msp", 58), ("msk", 102)])
    MC(S, "m-buerg", "Wer gibt Bürgschaften und Mithaftungen typischerweise ab?", "Familienmitglieder und Lebensgefährt*innen",
       ["Banken", "Arbeitgeber*innen", "Vermieter*innen"],
       "Mithaftungen entstehen meist innerhalb von Familie und Lebensgemeinschaft. Nach Trennungen werden sie oft schlagend, weil Schulden nicht geschieden werden können.",
       [("msk", 103), ("msk", 110)])
    MC(S, "m-konkurs", "Wie lange dauert ein Abschöpfungsplan im Privatkonkurs?", "5 Jahre",
       ["3 Jahre", "10 Jahre", "So lange, bis alles bezahlt ist"],
       "Der Abschöpfungsplan dauert 5 Jahre und ist auch gegen den Willen der Gläubiger*innen möglich. Den 3-jährigen Tilgungsplan gibt es für Privatpersonen seit Juli 2026 nicht mehr.",
       [("msp", 71), ("msp", 73), ("msk", 129)])
    MU(S, "m-konkurs", "Welche Voraussetzungen braucht ein gerichtliches Schuldenregulierungsverfahren (Privatkonkurs)?",
       ["Zahlungsunfähigkeit", "Zahlungswilligkeit"], ["Manifeste Armut", "Zustimmung aller Gläubiger*innen"],
       "Der Privatkonkurs steht zahlungsunfähigen, aber zahlungswilligen Schuldner*innen offen, dazu kommt Redlichkeit. Man muss nicht arm sein, und beim Abschöpfungsplan braucht es keine Zustimmung der Gläubiger*innen.",
       [("msp", 70), ("msk", 111)])
    MU(S, "m-sbstaat", "Für wen ist die Arbeit der Schuldenberatung von Nutzen?",
       ["Schuldner*innen", "Gläubiger*innen", "Arbeitgeber*innen und die Volkswirtschaft"], ["Inkassobüros, weil mehr Kosten anfallen"],
       "Gläubiger*innen erhalten eine realistische Quote und Transparenz über die Lage. Gepfändete Menschen finden schwer Arbeit, mit einer Regulierung kommen sie zurück in den Wirtschaftskreislauf.",
       [("msk", 104)])
    TF(S, "m-sbstaat", "In staatlich bevorrechteten Schuldenberatungen müssen Klient*innen für die Beratung bezahlen.", False,
       "Falsch. Die staatlich anerkannten Schuldenberatungen sind für Privatpersonen kostenlos und werden öffentlich finanziert. Kostenpflichtig sind private, gewerbliche Schuldenregulierer*innen.",
       [("msk", 104)])
    TF(S, "m-sbstaat", "In staatlich bevorrechteten Schuldenberatungen dürfen ausschließlich Jurist*innen beraten.", False,
       "Falsch. Die Berater*innen haben meistens Soziale Arbeit oder Jus als Basisberuf und sind speziell ausgebildet.",
       [("msk", 104)])
    TF(S, "m-sbstaat", "Berater*innen staatlich anerkannter Schuldenberatungen dürfen ihre Klient*innen im Privatkonkurs bei Gericht nur begleiten, aber nicht rechtlich vertreten.", False,
       "Falsch laut Skriptum: Sie sind berechtigt, Schuldner*innen im Privatinsolvenzverfahren zu begleiten und auch rechtlich zu vertreten. In Wien übernimmt die Schuldenberatung in der Regel aber keine Vertretung, das steht ebenfalls im Skriptum.",
       [("msk", 104), ("msk", 109)])
    TF(S, "m-anam", "Die Anmeldung bei der Schuldenberatung Wien ist auch online möglich.", True,
       "Stimmt. Man meldet sich telefonisch oder über das Internet an, danach folgt die telefonische Terminvereinbarung.",
       [("msp", 74), ("msk", 106)])
    MU(S, "m-anam", "Worüber sollte im Beratungsverlauf der Schuldenberatung gesprochen werden?",
       ["Überblick über die aktuellen Einnahmen und Ausgaben", "Möglichkeiten der Einkommenserhöhung", "Mögliche Einsparungspotentiale"],
       ["Ratschläge wie „Hören Sie mit dem Rauchen auf“", "Eine ausführliche Suchtbehandlung"],
       "Ein Haushaltsplan macht Ausgaben sichtbar, entscheiden müssen aber die Klient*innen selbst. Vorhaltungen sind laut Skriptum kontraproduktiv.",
       [("msk", 112)])
    MU(S, "m-anam", "Was zählt zu den psychosozialen Auswirkungen ungeregelter Schulden?",
       ["Nervliche Anspannung durch laufende Exekutionen und Besuche von Gerichtsvollzieher*innen", "Soziale Exklusion durch das Leben am Existenzminimum"],
       ["Mehr Freizeit", "Bessere Chancen bei der Arbeitssuche"],
       "Überschuldung ist schambesetzt und belastend; viele schotten sich ab. Wer am Existenzminimum lebt, kann am gesellschaftlichen Leben kaum teilnehmen, und laufende Exekutionen erschweren die Arbeitssuche.",
       [("msk", 112)])
    TF(S, "m-unterhalt", "Die Höhe der Unterhaltszahlung richtet sich ausschließlich nach dem tatsächlich erzielten Einkommen.", False,
       "Falsch. Es gilt der Anspannungsgrundsatz: Wer weniger verdient, als er*sie könnte, zahlt Unterhalt nach dem Betrag, der nach Ausbildung und Arbeitsmarkt erreichbar wäre.",
       [("msk", 107)])
    TF(S, "m-unterhalt", "Zahlt der Staat einen Unterhaltsvorschuss, bleibt die unterhaltspflichtige Person trotzdem zur Zahlung verpflichtet.", True,
       "Stimmt. Der Unterhaltsvorschuss springt für das Kind ein, entbindet aber nicht von der Pflicht. Für Rückstände kann bis auf das Unterhaltsexistenzminimum gepfändet werden.",
       [("msk", 106), ("msk", 107)])
    TF(S, "m-straf", "Wer seine Unterhaltspflicht schuldhaft verletzt, kann mit einer Freiheitsstrafe bestraft werden.", True,
       "Stimmt. Das ist § 198 StGB. Strafbar ist auch, wer keine zumutbare Arbeit annimmt und deshalb nicht zahlen kann.",
       [("msk", 107), ("msk", 114)])
    MU(S, "m-aufr", "Welche Aussagen zu einem Gehaltsvorschuss beim eigenen Arbeitgeber stimmen?",
       ["Der Arbeitgeber kann ihn gegen das Gehalt aufrechnen", "Die Aufrechnung ist nicht durch das normale Existenzminimum begrenzt", "Er ist keine gute Lösung, um Schulden abzuzahlen"],
       ["Er wird wie eine Lohnpfändung nur über dem Existenzminimum abgezogen"],
       "Schulden beim Dienstgeber können aufgerechnet werden, bis zur Hälfte des unpfändbaren Grundbetrags. Danach reicht das restliche Gehalt meist nicht mehr zum Leben.",
       [("msp", 69), ("msk", 110), ("msk", 111)])
    TF(S, "m-aufr", "Auch Sozialversicherungsträger können Forderungen mit laufenden Leistungen aufrechnen.", True,
       "Stimmt. Ein Träger kann bis zu 50 % der Leistung, höchstens bis 90 % des Ausgleichszulagenrichtsatzes einbehalten, auch trägerübergreifend: Die PVA kann etwa Schulden bei der Gesundheitskasse abziehen.",
       [("msp", 69), ("msk", 110)])

    # ---------------- Familie und Ansprüche ----------------
    MC(F, "m-fbaus", "Für welche Kinder wird der Erhöhungsbetrag zur Familienbeihilfe (erhöhte Familienbeihilfe) gewährt?",
       "Für erheblich behinderte Kinder", ["Für alle Kinder ab dem dritten Kind", "Für Kinder von Alleinerziehenden", "Für Kinder in Ausbildung über 18"],
       "Erheblich behindert heißt: Grad der Behinderung mindestens 50 % oder voraussichtlich dauernd außerstande, sich selbst zu erhalten. Das Sozialministeriumservice bescheinigt das.",
       [("msk", 13), ("msk", 14)])
    MU(F, "m-familie", "Unter welchen Bedingungen gibt es Familienbeihilfe für ein volljähriges Kind bis zum 24. Geburtstag oder darüber hinaus?",
       ["Wenn es sich in Berufsausbildung befindet", "Für die Zeit zwischen Schulabschluss und dem frühestmöglichen Beginn einer weiteren Ausbildung", "Bei erheblicher Behinderung, wenn es sich nicht selbst erhalten kann"],
       ["Wenn es beim AMS arbeitslos gemeldet ist", "Wenn es zu Studienzwecken nach Österreich gekommen ist"],
       "Nach 18 braucht es eine Berufsausbildung. Wer dauernd erwerbsunfähig ist, hat keine Altersgrenze. Arbeitslos gemeldet ohne Ausbildung heißt: kein Anspruch.",
       [("msk", 11), ("msk", 12)])
    MC(F, "m-familie", "Wer ist bei der Familienbeihilfe vorrangig anspruchsberechtigt, wenn das Kind im gemeinsamen Haushalt der Eltern lebt?",
       "Die Mutter", ["Der Vater", "Das Kind selbst", "Der Elternteil mit dem höheren Einkommen"],
       "Die Mutter ist vorrangig berechtigt, kann aber zugunsten des Vaters verzichten. Ausgezahlt wird an den haushaltsführenden Elternteil.",
       [("msk", 11), ("msk", 14)])
    TF(F, "m-fbaus", "Soll die Familienbeihilfe ab 18 direkt auf das Konto des Kindes gehen, braucht es die Zustimmung der Eltern.", True,
       "Stimmt. Die Direktauszahlung an volljährige Kinder beantragt man beim Finanzamt, es bedarf aber der Zustimmung der Eltern. Sie kann auch widerrufen werden.",
       [("msk", 14)])
    MC(F, "m-fbaus", "Wovon hängt die Höhe der Familienbeihilfe ab?", "Vom Alter und von der Anzahl der Kinder",
       ["Vom Einkommen der Eltern", "Vom Vermögen der Familie", "Von der Wohnungsgröße"],
       "Die Familienbeihilfe ist eine Universalleistung und steigt mit dem Alter des Kindes; für mehrere Kinder gibt es einen Zusatzbetrag. Einkommen und Vermögen spielen keine Rolle.",
       [("msk", 13), ("msp", 2)])
    MC(F, "m-kbg", "Wann gibt es beim Kinderbetreuungsgeld einen Partnerschaftsbonus?", "Wenn beide Eltern etwa gleich lang Kinderbetreuungsgeld beziehen",
       ["Wenn beide Eltern gleichzeitig in Karenz sind", "Wenn das Kind in eine Krippe geht", "Wenn die Eltern verheiratet sind"],
       "Der Bonus steht zu, wenn die Betreuung etwa 50:50 oder 40:60 geteilt wird und jeder Elternteil eine Mindestdauer KBG bezieht. Er wird einmalig an jeden Elternteil ausbezahlt und muss beantragt werden.",
       [("msk", 16)])
    MU(F, "m-kbgvar", "Zwischen welchen Modellen können Eltern beim Kinderbetreuungsgeld wählen?",
       ["Einkommensabhängiges Kinderbetreuungsgeld", "Pauschales Kinderbetreuungsgeld (Kinderbetreuungsgeld-Konto)"], ["Familienbeihilfe-Konto", "Wochengeld-Variante"],
       "Das einkommensabhängige KBG ersetzt das Einkommen, das Konto ist pauschal und flexibel in der Dauer. Wochengeld ist eine eigene Leistung rund um die Geburt.",
       [("msk", 16), ("msk", 17)])
    MU(F, "m-rez", "Was gilt für die Rezeptgebührenbefreiung auf Antrag?",
       ["Das Nettoeinkommen muss unter dem Ausgleichszulagenrichtsatz liegen", "Bei hohen Medikamentenkosten gibt es eine Obergrenze von 2 % des Jahresnettoeinkommens"],
       ["Man braucht ein ärztliches Attest über eine chronische Krankheit", "Die Anzahl der Rezepte allein reicht immer für eine Befreiung"],
       "Automatisch befreit sind etwa Ausgleichszulagen- und Mindestsicherungsbeziehende. Wer mehr verdient, kann über die Obergrenze befreit werden, wenn die Rezeptgebühren 2 % des Jahresnettoeinkommens erreichen.",
       [("msk", 21), ("msk", 22)])
    TF(F, "m-gvwien", "Asylwerber*innen in einer betreuten Unterkunft bekommen zusätzlich zur Verpflegung Taschengeld und Freizeitgeld.", True,
       "Stimmt. In betreuten Unterkünften gibt es Verpflegung oder Verpflegungsgeld, dazu ein monatliches Taschengeld und ein Freizeitgeld.",
       [("msk", 63)])
    MU(F, "m-gvwien", "Welche Grundversorgungsleistungen bekommen privat wohnende Personen?",
       ["Verpflegungsgeld für Erwachsene", "Verpflegungsgeld für Kinder", "Mietzuschuss"], ["Mindeststandard der WMS", "Wohnbeihilfe"],
       "Wer privat wohnt, bekommt Verpflegungsgeld und einen Mietzuschuss, unabhängig von der Wohnform dazu Bekleidungshilfe, Schulbedarf und Krankenversicherung. Die WMS gibt es in der Grundversorgung nicht.",
       [("msk", 63)])

    # ---------------- Knifflige Fragen (gemischt) ----------------
    TF(K, "m-sbstaat", "Die Schuldenberatung behandelt Suchtmittelkonsum der Klient*innen intensiv mit.", False,
       "Falsch. Die Schuldenberatung berät zu Schulden, Budget und Regulierung. Für andere Themen wird weitervermittelt, und die Entscheidung über Ausgaben bleibt bei den Klient*innen.",
       [("msk", 104), ("msk", 112)])
    TF(K, "m-gef", "Ein Kredit ist ein allgemeiner Grund für Überschuldung.", False,
       "Falsch. Schulden müssen keine Schuldenprobleme werden, Kredite können bei guter Planung sinnvoll sein. Überschuldung entsteht durch Einkommensverlust, Umgang mit Geld, gescheiterte Selbständigkeit oder Härtefälle.",
       [("msk", 101), ("msk", 102)])
    TF(K, "m-strafe", "Die erhöhte Fahrscheingebühr der Wiener Linien ist eine Strafe.", False,
       "Falsch. Strafen verhängen nur Behörden, die Wiener Linien sind keine. Die erhöhte Fahrscheingebühr ist eine normale Forderung und darum keine gefährliche Schuld.",
       [("msk", 107)])
    MC(K, "m-hibl", "Wo wird eine Hilfe in besonderen Lebenslagen beantragt?", "Bei der MA 40",
       ["Beim FSW", "Bei der Schuldenberatung", "Beim AMS"],
       "Die HibL ist eine Leistung der MA 40 und wird dort gesondert beantragt. Auch Familien mit Kindern im Gemeindebau, die von der MA 11 betreut werden, beantragen die finanzielle Hilfe bei der MA 40.",
       [("msp", 28), ("msk", 51)])
    MU(K, "m-hibl", "Welche Voraussetzungen gelten für eine Hilfe in besonderen Lebenslagen?",
       ["Rechtmäßiger Aufenthalt seit mindestens drei Monaten", "Aktueller Hauptwohnsitz in Wien"], ["Laufender WMS-Bezug", "Österreichische Staatsbürgerschaft"],
       "Die HibL setzt eine Notlage voraus, die man trotz eigener Mittel nicht überwinden kann, und die Aussicht auf eine nachhaltige Lösung. Einen Rechtsanspruch gibt es nicht.",
       [("msk", 51)])
