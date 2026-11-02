# Lerninhalte "Geschichte der Sozialen Arbeit". Alles stammt aus den LV-Unterlagen; jede Karte verweist auf Folien.
# tools/build_content.py macht daraus site/data/geschichte.json und prueft die Verweise gegen den Folientext.
# Dokumente: j Zusatztext 100 Jahre Jugendamt, e Einfuehrung, a1/a2 Armenfuersorge, eb Ehrenamt, rw Rotes Wien, t Totalitaere Regime,
#            n Nachkrieg, zs Von der Fuersorge zur Sozialarbeit, z Zeittafel

CHAPTERS = [
    # id, Stationsname, Zeitraum, Einzeiler, Dokumente, nuechtern (keine Spiel-Effekte)
    ("gr",   "Grundlagen", "Überblick", "Hilfe und Kontrolle, Begriffe, Quellen", ["e"], False),
    ("mon",  "Habsburgermonarchie", "1861–1918", "Armenfürsorge, Heimatrecht, Subsidiarität", ["a1"], False),
    ("ref",  "Reformen und Vorbilder", "ab 1853", "Elberfeld, Toynbee Hall, Hull House, Richmond, Salomon", ["a2"], False),
    ("ber",  "Vom Ehrenamt zum Beruf", "1912–1919", "Berufsvormundschaft, Ilse Arlt, Erster Weltkrieg", ["eb"], False),
    ("rot",  "Rotes Wien", "1919–1934", "Tandler, Aichhorn, Eugenik, KÜST", ["rw"], False),
    ("aut",  "Austrofaschismus", "1934–1938", "Katholische Familienpolitik, alte Wohltäterei", ["t"], False),
    ("ns",   "Nationalsozialismus", "1938–1945", "Selektion, Erfassung, Spiegelgrund", ["t"], True),
    ("nach", "Nachkrieg und Wirtschaftswunder", "1945–1968", "Kontinuitäten, Amtskapperl, Case Work", ["n"], False),
    ("sa",   "Von der Fürsorge zur Sozialarbeit", "1968–2000", "Öffnet die Heime, doppeltes Mandat, Heim 2000", ["zs"], False),
    ("heute","Aufarbeitung und Gegenwart", "seit 2000", "Heimkinder, Kommissionen, Kinderschutz heute", ["j"], True),
]

TOPICS = []
CARDS = []
LFS = []
PEOPLE = []
TERMS = []
TIMELINE = []
TRAPS = []

def T(id, ch, title, text, src):
    TOPICS.append(dict(id=id, ch=ch, title=title, text=text, src=src))

def _add(type, topic, lf, why, src, **kw):
    CARDS.append(dict(type=type, topic=topic, lf=lf, why=why, src=src or [], **kw))

def MC(topic, lf, q, right, wrong, why, src=None):
    _add("mc", topic, lf, why, src, q=q, right=right, wrong=wrong)

def TF(topic, lf, stmt, val, why, src=None):
    _add("tf", topic, lf, why, src, q=stmt, val=val)

def ORD(topic, lf, q, items, why, src=None):
    _add("ord", topic, lf, why, src, q=q, items=items)

def MATCH(topic, lf, q, pairs, why, src=None):
    _add("match", topic, lf, why, src, q=q, pairs=pairs)

def MULTI(topic, lf, q, right, wrong, why, src=None):
    _add("multi", topic, lf, why, src, q=q, right=right, wrong=wrong)

def LF(n, q, gist, points, ch, note=None):
    LFS.append(dict(n=n, q=q, gist=gist, points=[dict(t=t, src=s) for t, s in points], ch=ch, note=note))

# ---------------------------------------------------------------- Leitfragen (Musterantworten)

LF(1, "Was versteht man unter „Subsidiaritätsprinzip“?",
   "Zuerst hilft das nähere Umfeld, die öffentliche Hand springt erst zuletzt ein.",
   [("Die Gemeinde musste nur dann versorgen, wenn keine gesetzlich verpflichteten Personen da waren (Verwandte, Ehegatten, Vormünder).", [("a1",7)]),
    ("Private Vereine und Stiftungen übernahmen die Armenversorgung; erst wenn sie finanziell überfordert waren, trat die Gemeinde ein.", [("a1",7)]),
    ("Beispiel Armenkinderpflege: Zuerst waren Familie oder Verwandte zuständig, erst nach Überprüfung gab es Erziehungs-, Waisen- oder Kostgelder.", [("a1",27)]),
    ("Es bildet die dritte Ebene sozialer Absicherung neben staatlichen Sozialleistungen und Leistungen von Ländern und Gemeinden: Familie und Ehrenamt.", [("e",9)])], "mon")

LF(2, "In welchem historischen Zeitrahmen war dieses leitend für die Ausgestaltung der Fürsorge?",
   "In der Habsburgermonarchie, von der liberalen Ära ab 1861 bis 1918.",
   [("Liberale Ära 1861–1895: kein einheitlicher gesamtstaatlicher Anspruch, stattdessen private ehrenamtliche Versorgung und Familien.", [("a1",3)]),
    ("Christlichsoziale Ära 1895–1918: weiterhin dieselbe Kompensation durch Private und Familien.", [("a1",4)]),
    ("Rechtliche Basis war das Heimatrechtsgesetz von 1863, das Subsidiaritätsprinzip ist dort verankert.", [("a1",7)]),
    ("Das Rote Wien bricht ab 1919 damit: allgemeines Anrecht auf Fürsorge statt individueller Wohltat.", [("rw",2),("rw",9)]),
    ("Der Austrofaschismus nimmt dieses Anrecht ab 1934 wieder zurück und setzt erneut auf Ehrenamt und „alte Wohltäterei“.", [("t",2),("t",5)])], "mon")

LF(3, "Beschreiben Sie bitte kurz die Grundzüge der Armenfürsorge in der Habsburgermonarchie.",
   "Kein Rechtsanspruch, möglichst billig, moralisch abgewertet und stark kontrollierend.",
   [("Kein einheitlicher gesamtstaatlicher Anspruch; Kompensation durch private ehrenamtliche Versorgung und Familien.", [("a1",3),("a1",4)]),
    ("Basis: Heimatrechtsgesetz 1863 und Subsidiaritätsprinzip; es galt das Ziel, die Gemeindekosten gering zu halten.", [("a1",7),("a1",9)]),
    ("Armut galt im katholischen und liberalen Lager als selbstverschuldet („Charakterschwäche“, „Arbeitsscheu“); die Sozialdemokratie sah darin eine politische Frage.", [("a1",6)]),
    ("Offene Fürsorge: nur vorübergehende Geldaushilfen. Geschlossene Fürsorge: Armenanstalten mit Arbeitspflicht, Unterstützung nur für das „Notdürftigste“.", [("a1",19),("a1",20)]),
    ("Kriminalisierung von Armut: Zwangsarbeitergesetze von 1885, Anhaltung wegen Bettelei oder „Arbeitsscheu“.", [("a1",11)]),
    ("Interesse an öffentlicher Ordnung und „Unsichtbarmachung des Elends“: Anstaltsbau, Verlegung in die Peripherie.", [("a1",5),("a1",21)])], "mon")

LF(4, "Erläutern Sie bitte das Prinzip des Heimatrechtsgesetzes von 1863 (Bedeutung und Konsequenzen für KlientInnen der Fürsorge).",
   "Nur wer heimatberechtigt war, hatte in der Gemeinde Aufenthaltsrecht und Anspruch auf Armenversorgung.",
   [("Heimatberechtigten wurde das Recht auf ungestörten Aufenthalt und Anspruch auf Armenversorgung gewährt.", [("a1",7)]),
    ("Das Gesetz war die Basis des Armenwesens und diente der präventiven Abschottung vor Versorgungsansprüchen.", [("a1",7),("a1",8)]),
    ("Konsequenz: Der Großteil der Armen fiel aus den Regelungen heraus und blieb auf Selbsthilfe, Vereine und Familie angewiesen.", [("a1",8)]),
    ("Novelle 1896, „Ersitzungsprinzip“: Heimatrecht nach zehn Jahren ununterbrochenem Aufenthalt, nicht mehr nur durch Geburt.", [("a1",9)]),
    ("Problem Nachweis: Bettgeher*innen, Saisonarbeiter*innen, Tagelöhner*innen und Dienstbot*innen konnten den Aufenthalt kaum belegen; sie blieben ausgegrenzt.", [("a1",9)]),
    ("Fazit: Gesetz und Reform dienten der Geringhaltung der Gemeindekosten.", [("a1",9)])], "mon")

LF(5, "Welche Idee verfolgte Ilse Arlt mit der Gründung der „Vereinigten Fachkurse für Volkspflege“? (inkl. ungefähre zeitliche Zuordnung)",
   "1912: erste österreichische Ausbildung, um einen qualifizierten neuen Frauenberuf zu schaffen.",
   [("1912 in Wien gegründet: erste österreichische Ausbildungseinrichtung für soziale Arbeit, Vorbild war Alice Salomons Soziale Frauenschule.", [("eb",11)]),
    ("Ziel: ein neues weibliches Berufsfeld schaffen und öffentliche wie private Fürsorge professionalisieren.", [("eb",11)]),
    ("Normen für Wissen und Können der sozialen Helferin festlegen, die freie Liebestätigkeit nicht verdrängen, sondern stützen.", [("eb",11)]),
    ("Gleiche gründliche Ausbildung für bezahlte Berufsarbeit und unbesoldeten Hilfsdienst.", [("eb",12)]),
    ("Breiter Lehrplan (Gesundheit, Psychologie, Volkswirtschaft) und offene Aufnahme: 17 bis 35 Jahre, unterschiedliche Vorbildung.", [("eb",13),("eb",14)]),
    ("Verbindung von Wissenschaft und Forschung mit der Praxis: Grundstein der Fürsorgewissenschaft.", [("eb",8)])], "ber")

LF(6, "Was versteht Ilse Arlt unter Bedürfnishemmschwelle?",
   "Das Wort steht nicht auf den Folien. Am nächsten kommt: die Spannung zwischen einfachster ausreichender Bedürfnisbefriedigung und Unterbefriedigung.",
   [("Fürsorge müsse einschreiten, wenn „eine Spannung zwischen der einfachsten noch ausreichenden Bedürfnisbefriedigung und der jeweils vorliegenden Unterbefriedigung“ festgestellt werden kann.", [("eb",20)]),
    ("Hilfe soll nicht erst bei offensichtlicher Notlage einsetzen, sondern als Prophylaxe wirken.", [("eb",20)]),
    ("Maßstab ist der Katalog der dreizehn Bedürfnisklassen, die allen Menschen gemeinsam sind und je nach Alter, Schicht usw. variieren.", [("eb",18)]),
    ("Die genaue Kenntnis der Bedürfnisse widerlegt Annahmen über selbstverschuldete Armut und Vorurteile über „die Armen“ als homogene Gruppe.", [("eb",18)])], "ber",
   note="Der Begriff „Bedürfnishemmschwelle“ selbst kommt in den Unterlagen nur in der Leitfrage vor, auch nicht im Zusatztext. Die Punkte hier sind das, was die Folien zum Thema hergeben. Schau bitte zusätzlich in deine Mitschrift oder den Reader, ob es eine genaue Definition gibt.")

LF(7, "Nennen Sie bitte erste methodische Grundlagen der Fürsorge (internationale Vorbilder).",
   "Elberfelder System, Settlements und die Einzelfallhilfe von Mary Richmond.",
   [("Elberfelder System (1853): Dezentralisierung, Ehrenamt, Hilfe zur Selbsthilfe, Quartierprinzip, geistige Mütterlichkeit, Friendly Visiting (Hausbesuch).", [("a2",9)]),
    ("Zwei Modelle aus England und den USA: Einzelfallhilfe (Social Case Work) und Settlement (Nachbarschaftshilfe, Vorläufer der Gemeinwesenarbeit).", [("a2",14)]),
    ("Toynbee Hall in London (Henrietta und Samuel Barnett): gemeinsames Leben mit den Armen, Bildung statt Sozialdisziplinierung.", [("a2",16),("a2",17),("a2",18)]),
    ("Hull House in Chicago 1889 (Jane Addams): Nachbarschaftszentrum, Verbindung von Wissenschaft und Hilfe.", [("a2",25),("a2",26),("a2",27)]),
    ("Mary Richmond, „Social Diagnosis“ (1917): wissenschaftlich fundierte soziale Diagnose, Vorbild für Salomon und Arlt.", [("a2",37),("a2",39)])], "ref")

LF(8, "Was versteht man unter „Berufsvormundschaft“ in der Jugendwohlfahrt? Warum wurde diese eingeführt?",
   "Die Gemeinde übernimmt mit bezahltem Personal die Vormundschaft über uneheliche Kinder, weil Mütter keine Obsorge haben durften.",
   [("Im Zentrum: rechtliche Vertretung und Versorgung unehelich geborener Kinder.", [("eb",3)]),
    ("Grund: Mütter durften die rechtliche Obsorge nicht übernehmen; „Listenvormünder“ aus den Wählerlisten waren nur pro forma da und kümmerten sich nicht um die Kinder.", [("eb",3)]),
    ("Gemeinderatsbeschluss 1912, Übergangslösung in Ottakring 1913 und Penzing 1914, Fürsorgestellen als Vorläufer der Bezirksjugendämter.", [("eb",4)]),
    ("Inhalt: Unterhalts-, Gesundheits- und Familienfürsorge; Väter ausforschen, Unterhalt einholen, ärztliche Kontrollen, Hausbesuche, Verbindungsdienst.", [("eb",4),("eb",6)]),
    ("Teamarbeit aus Arzt, Berufsvormund und Pflegerinnen; 1913 die ersten 10 bezahlten Stellen: erster Schritt zur entlohnten Sozialarbeit.", [("eb",5)])], "ber")

LF(9, "Erläutern Sie bitte Prinzip und Rolle des Ehrenamtes im Rahmen der Fürsorge.",
   "Unbezahlt, ohne Ausbildung, ohne Rechtsanspruch: Es kompensierte die fehlende staatliche Versorgung.",
   [("Kompensation fehlender staatlicher Versorgung; Prinzipien: individuelle Bedürftigkeit, kein gesetzlicher Anspruch notwendig, Vorbild Elberfelder System.", [("a2",8)]),
    ("Armen- und Waisenrät*innen: unbezahlt, ohne Ausbildung, Geschlechterarbeitsteilung (Frauen vor allem bei Kostkindern).", [("a2",7)]),
    ("Geistige Mütterlichkeit: gesellschaftliche Integration bürgerlicher Frauen über das soziale Ehrenamt.", [("a2",11)]),
    ("Kritik: „Wohltäterei“, der Beschenkte schuldet Dankbarkeit und Wohlverhalten; kein neutrales Hilfskonzept.", [("a2",13)]),
    ("Das Rote Wien grenzt sich von der ehrenamtlichen Wohltätigkeit ab, der Austrofaschismus kehrt zu ihr zurück.", [("rw",9),("t",5)]),
    ("Im Ersten Weltkrieg massiver Mangel an Ehrenamtlichen, das treibt die Verberuflichung voran.", [("eb",5),("eb",25)])], "ref")

LF(10, "Skizzieren Sie bitte kurz die Positionierung der Fürsorge und ihres Selbstverständnisses im Roten Wien.",
   "Vom Almosen zum Anrecht: Die Gesellschaft ist zur Hilfe verpflichtet, zugleich erfasst und kontrolliert sie.",
   [("Allgemeines Anrecht auf Fürsorge: Abkehr von individualistischer Wohltat zum kollektiven Hilfeanspruch, ein zentraler Wendepunkt.", [("rw",9)]),
    ("Tandler: „Die Kinder haben ein Anrecht auf Fürsorge und die Gesellschaft ist ihr Sachwalter.“", [("rw",9)]),
    ("1921 Wohlfahrtsamt: straffe Organisation, engmaschiges Netz, Finanzierung durch die Breitner-Steuern.", [("rw",6),("rw",8)]),
    ("Prophylaxe und bevölkerungspolitische Ausrichtung: Maßnahmen vor dem Eintreten der Not.", [("rw",10)]),
    ("Die geschulte Fürsorgerin als Beauftragte der Gesellschaft: beraten, aber auch „erfassen“, „erheben“ und „Nachschau“ halten.", [("rw",15),("rw",16)])], "rot")

LF(11, "Inwiefern kann die Fürsorge des Roten Wien als richtungsweisend für die folgenden Jahrzehnte angesehen werden?",
   "Anrecht, Prophylaxe, moderne Heime und Beratung wirkten nach, ebenso aber Kontrolle und Testverfahren.",
   [("Das Anrecht auf Fürsorge als Wendepunkt im Selbstverständnis.", [("rw",9)]),
    ("Sieben Neuerungen für die Praxis, z.B. Jugendfürsorge bis zum 18. Lebensjahr, Vereinheitlichung im Jugendamt, Ziehkindergesetz, mehr Berufsfürsorgerinnen.", [("rw",40)]),
    ("Heime statt Anstalten: Umgestaltung der Fremdunterbringung als zentrale Leistung.", [("rw",30),("rw",31)]),
    ("Aichhorn: Beraten und erziehen statt strafen. Fallbesprechungen der Kinderstube nehmen das Case Work der 1960er vorweg.", [("rw",18),("rw",24)]),
    ("Kehrseite mit Langzeitwirkung: distanzlose Hausbesuche als jahrzehntelange Praxis und jahrzehntelange Begutachtung auf Basis der KÜST-Tests.", [("rw",16),("rw",34)]),
    ("Das Säuglingswäschepaket von 1927 blieb bis zum Wickelrucksack im Jahr 2000 ein Symbol.", [("rw",14),("zs",25)])], "rot")

LF(12, "Welche Rolle kam der Fürsorgerin in der Vermittlung eugenischer Ideale im Roten Wien zu?",
   "Sie trug die Bevölkerungspolitik in die Familien: beraten, erfassen, kontrollieren.",
   [("Tandlers Fürsorge war bevölkerungspolitisch geleitet: „positive“ Eugenik, Hebung der Geburten, bessere „Aufzuchtsbedingungen“.", [("rw",10)]),
    ("Beratungsstellen verbreiteten das eugenische Gedankengut; Menschen mit erblichen oder psychiatrischen Krankheiten und Sucht wurde der Verzicht auf Kinder nahegelegt.", [("rw",11)]),
    ("Die Fürsorgerin erfasste von Geburt an: Verbindungsdienst in Geburtsabteilungen, Säuglingswäschepaket beim Hausbesuch, Schulfürsorge.", [("rw",14)]),
    ("Sie erzog Mütter zur „besseren“ Erfüllung ihrer Aufgaben, Hausbesuche dienten auch der Disziplinierung bis zur Androhung der Kindesabnahme.", [("rw",16)]),
    ("Sie trennte „gute“ von „schlechten“ Hilfsbedürftigen; Maßstab war die normierte kleinbürgerliche Familie.", [("rw",13),("rw",15)])], "rot")

LF(13, "Welche Bedeutung lässt sich August Aichhorn für die Fürsorge, insbesondere die Jugendfürsorge beimessen?",
   "Er machte aus dem „Störenfried“ eine hilfsbedürftige Person: Verstehen und Gespräch statt Strafe.",
   [("Neuer Verwahrlosungsbegriff: weder erblich noch Charakterschwäche, sondern individuelle Reaktion auf soziale und psychische Erfahrungen.", [("rw",18)]),
    ("Pionier der psychoanalytischen Sozialarbeit: vernetzte Psychoanalyse und Fürsorge, vermittelte Fürsorgerinnen die Grundlagen.", [("rw",20),("rw",22)]),
    ("Oberhollabrunn: Prügelstrafe abgeschafft, keine verschlossenen Türen; Vorbild für die Umgestaltung von Besserungsanstalten (Eggenburg, Weinzierl).", [("rw",38),("rw",39)]),
    ("Ausbau der Erziehungsberatung: Berater als „verständnisvoller Verbündeter“.", [("rw",20),("rw",23)]),
    ("Kinderstube 1926 mit ersten Fallbesprechungen; 1949 Mitinitiator der Child Guidance Klinik mit Rosa Dworschak.", [("rw",24),("n",39)])], "rot")

LF(14, "Wie gestaltete sich die Fürsorge im Ständestaat?",
   "Kein Ausbau, Privatisierung und Rückkehr zur katholischen Wohltätigkeit.",
   [("Keine strukturellen Neuerungen, kein weiterer Ausbau; mehr Geld für private konfessionelle Einrichtungen, Privatisierung (Schloss Wilhelminenberg geht an die Sängerknaben).", [("t",2)]),
    ("Grundlage katholische Soziallehre: Rücknahme des allgemeinen Anrechts, Konzentration auf die „alte Wohltäterei“ des Ehrenamtes.", [("t",5)]),
    ("Familienschutz: Bevölkerungspolitik des Roten Wien wird mit sittlich-katholischen Werten verknüpft, 800 Familienasyle für „geordnete Familien“.", [("t",7),("t",8)]),
    ("Viel Not bei zu wenig Mitteln; Fürsorgebuch zur Einsparung und Überprüfung.", [("t",9)]),
    ("Fremdunterbringung in katholischen Privatanstalten, „Anstalt“ statt „Heim“, katholisches Bekenntnis als Voraussetzung für Pflegekinder, politische Personalveränderungen.", [("t",11)])], "aut")

LF(15, "Erläutern Sie bitte den Zusammenhang zwischen Fürsorge und NS-Regime. (Auswirkungen auf das Fürsorgesystem? Auswirkungen auf die Soziale Arbeit im Speziellen?)",
   "Strukturen blieben, die Ideologie drehte sich um: Dienst am Staat statt an Hilfsbedürftigen.",
   [("Strukturelle Weiterführung: Das Jugendamt wird Gaujugendamt Niederdonau, das Sprengelsystem wird ausgebaut.", [("t",12)]),
    ("Ideologische Umkehr: bestehende Fürsorgerechte außer Kraft, Zwangsmaßnahmen, der Dienst am Staat steht im Zentrum.", [("t",13)]),
    ("Private Einrichtungen zwangsweise aufgelöst oder eingegliedert, alle Ausbildungsstätten geschlossen; enge Zusammenarbeit mit Polizei und Gestapo.", [("t",14),("t",15)]),
    ("Neue Soziale Frauenschule: Erb- und Rassenpflege, SS-Ärzte als Vortragende, niedrigeres Niveau als im Roten Wien.", [("t",24)]),
    ("Personal: jüdische und oppositionelle Bedienstete entfernt, Diensteid, politische Schulungen, Klima der Angst.", [("t",26),("t",27),("t",29),("t",30)]),
    ("Handlungsspielräume waren unterschiedlich: Anpassung und Opportunismus, aber auch Sabotage etwa bei den Sippenbögen.", [("t",28),("t",36),("t",37)])], "ns")

LF(16, "Erläutern Sie bitte den Zusammenhang zwischen Fürsorge und NS-Regime. (Auswirkungen auf die KlientInnen?)",
   "Hilfe nur für die „Volksgemeinschaft“, für alle anderen wurde Fürsorge lebensgefährlich.",
   [("Juden und Jüdinnen wurden aus der öffentlichen Wohlfahrt ausgeschlossen; die Berufsvormundschaft galt nur noch für Kinder, „die keine Juden (…) und keine Zigeuner sind“.", [("t",14)]),
    ("Gespaltene Fürsorge: großzügige Hilfe für die als würdig Geltenden und kinderreiche „erbgesunde“ Familien, Mitwirkung an „Selektion und Auslese“ für andere.", [("t",32),("t",33)]),
    ("„Verwahrlosung“ wird zu „Asozialität“; Drill, Zucht und Zwangseingliederung in HJ und BDM.", [("t",18),("t",19)]),
    ("An die Stelle der Erziehung tritt der Ausschluss, in letzter Konsequenz mit tödlichen Folgen.", [("t",22)]),
    ("Totale Erfassung: Hausbesuch und Verbindungsdienst dienten der Erhebung von Erbkrankheiten; Erbkartei von 7.868 auf 406.537 Personen. Kontakt mit der Fürsorge konnte gefährlich werden.", [("t",35),("t",36)]),
    ("Am Spiegelgrund: 789 dokumentierte Todesopfer unter Kindern und Jugendlichen. Für Überlebende folgten oft jahrelange Heimaufenthalte.", [("t",38),("t",40)])], "ns")

LF(17, "Skizzieren Sie bitte kurz Traditionen und Brüche im Rahmen der Fürsorge nach 1945.",
   "Formal ein Neubeginn, in Personal, Gesetzen, Ausbildung und Haltung aber viel Kontinuität.",
   [("Brüche: Trennung von Gesundheitsfürsorge und Jugendwohlfahrt, wieder Wiener städtisches Jugendamt; NS-Fächer entfallen.", [("n",2),("n",10)]),
    ("Tradition Gesetz: Die Jugendwohlfahrtsverordnung von 1940 blieb Grundlage bis zum neuen Gesetz von 1954.", [("n",2),("n",27)]),
    ("Tradition Personal: meist kurze Berufsverbote; nach der Amnestie 1947 wurden etwa 90 Prozent der NationalsozialistInnen wieder eingestellt.", [("n",6)]),
    ("Tradition Ausbildung: Inhalte von vor 1938, medizinisch ausgerichtet, praxisfern; Methodenrezeption durch den NS unterbrochen.", [("n",10),("n",11)]),
    ("Tradition Kontrolle: Der in der NS-Zeit verstärkte Kontrollcharakter wird fortgesetzt, Hausbesuche als Eingriffe ins Private, „Amts-Kapperl“.", [("n",25)]),
    ("Neu ab den 1950ern: Case Work, Familienförderung, Einbezug der Väter, Stärkung mütterlicher Rechte 1954.", [("n",27),("n",28),("n",45)])], "nach")

LF(18, "In welcher Weise wurden Konzepte sozialer Disziplinierung im Kontext der Jugendwohlfahrt nach 1945 weitergeführt?",
   "„Sozialanpassung“ ersetzt „Asozialität“, Heime und Abnahmen disziplinieren weiter.",
   [("„Sozialanpassung“ wird anstelle der NS-„Asozialität“ zum Gradmesser für Kinder und Jugendliche.", [("n",36)]),
    ("Moralische und sittliche Verwahrlosung wird zentrales Thema, Mütter und ihre Berufstätigkeit gelten als Ursache.", [("n",20),("n",34),("n",36)]),
    ("Kindesabnahmen gehen weiter, nun stark wegen „Erziehungsschwierigkeiten“; kaum Änderung der Praxis bis Ende der 1960er.", [("n",34)]),
    ("Gutachten mit Weiterwirken von NS-Gedankengut, z.B. das Gutachten von 1953.", [("n",52)]),
    ("Heim als „totale Institution“: Gewalt bis in die 1970er; Ausbeutung auf ländlichen Pflegestellen.", [("n",53)]),
    ("Kampf gegen „Schmutz und Schund“ und Geschlechtererziehung wie die Puppenadoption ab 1954.", [("n",30),("n",38)])], "nach")

LF(19, "Was versteht man unter dem „doppelten Mandat“ der Fürsorge?",
   "Soziale Arbeit steht immer zwischen Hilfe und Kontrolle.",
   [("Soziale Arbeit entstand als Reaktion auf problematische Lebenslagen: Hilfestellung, Disziplinierung und Kontrolle, also das „doppelte Mandat“.", [("e",19)]),
    ("Geschichte der Sozialarbeit und Jugendwohlfahrt als Pendeln zwischen Hilfe und Kontrolle, das immanenter Teil der Jugendwohlfahrt ist.", [("zs",31)]),
    ("Das zeigt sich früh: „Verknüpfung von Hilfe, Schutz und Kontrolle“ schon in der Armenfürsorge, später etwa beim Hausbesuch.", [("a1",14),("eb",6)])], "sa")

LF(20, "Worin liegen Ihrer Meinung nach die Unterschiede zwischen „alter Fürsorge“ und „moderner Sozialarbeit“?",
   "Von Zwang, Kontrolle und Autorität zu Beratung, Freiwilligkeit und Partnerschaftlichkeit.",
   [("Haltung: statt autoritärer Bevormundung Partnerschaftlichkeit, Klient*in im Mittelpunkt, Hilfe zur Selbsthilfe.", [("zs",6),("zs",7),("zs",20)]),
    ("Methode: statt „Amtskapperl“ Beratung, vertiefte Einzelfallhilfe, Gesprächsführung, Systemik, Supervision.", [("zs",6),("n",46)]),
    ("Eingriff: statt obligatorischer, unangemeldeter Kontrollbesuche anlassbezogene Erhebungen nach dem Vieraugenprinzip.", [("zs",29),("n",21)]),
    ("Unterbringung: von „so lange wie möglich“ im Großheim zu „so kurz wie notwendig“, ambulant vor stationär.", [("zs",27),("zs",29)]),
    ("Zweck: Keine Verbindung mehr mit bevölkerungspolitischen Interessen; Kinderschutz und Familienförderung sind von staatlichen Interessen abgekoppelt.", [("zs",25)]),
    ("Selbst einschätzen: Die Frage fragt nach deiner Meinung. Beachte auch die Grenzen, denn Kontrolle bleibt Teil der Arbeit, und noch die „Stadt des Kindes“ blieb autoritär.", [("zs",11),("zs",31)])], "sa")

LF(21, "Wie positioniert sich die Sozialarbeit im Unterschied zur Fürsorge zum „doppelten Mandat“?",
   "Sie erkennt die Spannung an, stärkt die Freiwilligkeit und rechtfertigt Kontrolle über den Kinderschutz.",
   [("Die 1968er Bewegung kämpft gegen den Kontrollcharakter, die Freiwilligkeit der Angebote wird gestärkt.", [("zs",31)]),
    ("Das Pendeln zwischen Hilfe und Kontrolle wird als immanenter Teil anerkannt, nicht verleugnet.", [("zs",31)]),
    ("Theoretische und praktische Abkehr von primärer Kontrolle bei gleichzeitigem Festhalten am „umfassenden Kinderschutz“.", [("zs",31)]),
    ("„Kontrolle ja, reduziert aber auf die schwierigsten Fälle“; heute anlassbezogen, Zwang nur bei „Gefahr im Verzug“.", [("zs",7),("zs",29)]),
    ("Kinderschutz wird offen als Hauptaufgabe benannt, statt die Kompetenz der KlientInnen zu untergraben.", [("zs",32)])], "sa")

LF(22, "Was versteht man unter Verbindungsdienst der Jugendfürsorge? (Praxis und Ziele)",
   "Fürsorgerinnen sind direkt an Geburtsstationen und Schulen, um Bedürftige früh zu erfassen.",
   [("Praxis: Verbindungsdienst an Geburtskliniken, zum „Ausforschen“ bedürftiger Mütter und Kinder.", [("eb",6)]),
    ("Im Ersten Weltkrieg ausgebaut: Unterstützung bedürftiger Mütter mit Geld, Lebensmitteln und Säuglingswäsche.", [("eb",24)]),
    ("Rotes Wien: Ein Großteil der Neugeborenen samt Müttern wird „erfasst“, Meldepflicht unehelicher Geburten, dazu Schulfürsorge.", [("rw",14)]),
    ("Ziel zugleich Hilfe und Kontrolle: frühe Unterstützung und vollständige Erfassung; die Erhebungen fließen in den Kinder-Evidenzkataster.", [("rw",16)]),
    ("NS-Zeit: Das Wäschepaket dient auch der Erhebung von Erbkrankheiten; Verbindungsdienst zu HJ und NSV zur restlosen Erfassung.", [("t",22),("t",35)])], "ber")

LF(23, "Nennen Sie bitte ein paar Aspekte für die historische Herausbildung der Sozialen Arbeit als spezifischer Frauenberuf.",
   "Geistige Mütterlichkeit, Frauenbewegung und der Wunsch nach Erwerbsarbeit machten Fürsorge weiblich.",
   [("Geistige Mütterlichkeit: Fürsorge als öffentliche Reproduktionsarbeit, Pendant zur privaten, weiblich definierten Familienarbeit.", [("a2",11)]),
    ("Frauenbewegung als Motor: Berufisierung eng verbunden mit der österreichischen Frauenbewegung; Vorbilder Salomon und Arlt.", [("eb",2),("a2",43)]),
    ("Bürgerliche Mädchen hatten kaum Bildungs- und Berufschancen, der Beruf bot Arbeit und Sinn.", [("a2",43),("eb",12)]),
    ("Arlts Ziel war ausdrücklich ein neues weibliches Berufsfeld.", [("eb",11)]),
    ("1917 bis 1919 Ehe- und Kinderlosigkeit als Voraussetzung: Lebensentwurf jenseits von Mutterschaft.", [("eb",25)]),
    ("Weiblich codiert bis in die 1950er („fraulich-mütterliches Wesen“); Männer erst ab 1948/49 zugelassen, Leitung oft männlich; niedriges Sozialprestige.", [("n",9),("n",41),("n",43),("n",49)])], "ber")

LF(24, "Was ist unter Berufisierung und Professionalisierung im Hinblick auf die Entwicklung des Fürsorgeberufes zu verstehen? (inkl. ungefähre zeitliche Zuordnung)",
   "Berufisierung: bezahlte Stellen ab etwa 1913. Professionalisierung: Ausbildung, Methoden, Wissenschaft, mit Schub ab den 1950er bis 1970er Jahren.",
   [("Berufisierung: vom Ehrenamt zur entlohnten Arbeit. 1913 erstmals 10 Stellen für Berufspflegerinnen, noch ohne Ausbildung als Voraussetzung.", [("eb",5)]),
    ("Professionalisierung: qualifizierte Ausbildung, wissenschaftliche Fundierung, eigene Methoden. Impuls durch Arlt ab 1912.", [("eb",8),("eb",11)]),
    ("1917 Gründung des Jugendamtes, zweijährige städtische Fachkurse und Berufstitel „Fürsorgerin“; 1918 Akademie für soziale Verwaltung.", [("eb",26),("eb",27)]),
    ("Bruch im NS, danach praxisferne Ausbildung; Methoden kommen über Case Work ab den 1950ern.", [("n",11),("n",41),("n",47)]),
    ("„Professionalisierungs- und Modernisierungsschub“ um 1968; 1976 Akademien für Sozialarbeit, 1987 sechs Semester.", [("zs",6),("zs",14)]),
    ("2002 vierjährige FH-Studiengänge, 2017 berufsbegleitender Master.", [("z",4),("z",5)])], "ber")

LF(25, "Welche Bedeutung lässt sich der Kritik der 1968er Bewegung im Hinblick auf eine Neugestaltung der Fürsorge, insbesondere die Jugendfürsorge beimessen? (Inhalt der Kritik und Konsequenzen)",
   "Massive Institutionskritik, „Öffnet die Heime“, und daraus Heimreform, Beratung und neue Projekte.",
   [("Inhalt: autoritärer und kontrollierender Charakter von Sozialarbeit und Sozialpädagogik, weibliche Rollenzuschreibung, patriarchale Strukturen.", [("zs",2),("zs",3)]),
    ("Protest „Öffnet die Heime“: Demonstration am 29.1.1970, Kritik an „scheindemokratischer“, autoritärer Führung.", [("zs",10)]),
    ("Konsequenz Heime: Enquete 1971, Wiener Heimkommission, Liberalisierung, Stadt des Kindes 1974.", [("zs",10),("zs",11)]),
    ("Konsequenz Praxis: von Zwang zu Freiwilligkeit und Beratung, niederschwellige ambulante Angebote, mehr Pflegefamilien.", [("zs",3)]),
    ("Konsequenz Beruf: Professionalisierungsschub, neue Projekte wie Frauenhäuser, Streetwork, „Augustin“; Sozialarbeit wird attraktiv.", [("zs",6),("zs",18)]),
    ("Generationskonflikt im Amt zwischen alten Fürsorgerinnen und jungen Sozialarbeiterinnen.", [("zs",20)])], "sa")

LF(26, "Welche Bedeutung hatte die Einführung des Case-Work auf das Feld sozialer Arbeit (sowohl für Klientinnen als auch ProfessionistInnen)?",
   "Für Klient*innen: Anerkennung statt Kontrolle. Für Professionist*innen: Methode, Fortbildung und Supervision.",
   [("Herkunft: Mary Richmonds Einzelfallhilfe, in Wien vermittelt durch Rosa Dworschak in der Tradition Aichhorns.", [("a2",37),("rw",28)]),
    ("Für Klient*innen: Absage an den Kontrollcharakter, Anerkennung der individuellen Persönlichkeit, umfassende psychosoziale Anamnese, Anleitung zur Selbsthilfe.", [("n",45)]),
    ("Für Professionist*innen: Fortbildung ab 1954 mit Supervision, klientenzentrierte Gesprächsführung, professionelles und menschliches Verhältnis statt Amtsmacht.", [("n",45),("n",47)]),
    ("Einführung langsam: Modellversuch 1957 in Hernals; daneben lief die „Amts-Kapperl-Fürsorge“ weiter.", [("n",45),("n",46)]),
    ("Spätere Folge: vertiefte Einzelfallhilfe als Teil des Professionalisierungsschubs um 1968.", [("zs",6)])], "nach")

# ---------------------------------------------------------------- Grundlagen

T("gr-mandat","gr","Hilfe und Kontrolle",
  "Soziale Arbeit entstand als Reaktion auf problematische Lebenslagen. Sie war von Anfang an Hilfestellung, aber auch Disziplinierung und Kontrolle. Diese Spannung nennt die LV „doppeltes Mandat“, sie zieht sich durch alle Epochen.",
  [("e",9),("e",19)])
T("gr-netze","gr","Wer ist zuständig?",
  "Soziale Arbeit hängt immer an der Frage des rechtlichen Anspruchs. Die LV unterscheidet drei Ebenen: staatliche Sozialleistungen, Leistungen von Ländern und Gemeinden sowie Familie und Ehrenamt. Soziale Netze sind relativ junge Errungenschaften.",
  [("e",8),("e",9)])
T("gr-begriffe","gr","Sozialarbeit und Sozialpädagogik",
  "Sozialarbeit hat grob vereinfacht erzieherisch zu helfen, Sozialpädagogik helfend zu erziehen. Die Begriffe und Felder sind historisch nicht konstant. Die LV verfolgt einen Konvergenz- statt einen Differenzansatz.",
  [("e",5),("e",13),("e",14)])
T("gr-quellen","gr","Wie Geschichte rekonstruiert wird",
  "Es gibt schriftliche Quellen wie Akten und Gesetze, mündliche wie Zeitzeug*innenberichte und zusätzliche wie Film und Fotos. Quellen sind immer auch Deutungen, deshalb ist die Kontextualisierung besonders wichtig. Gesetzestexte sagen wenig über die Praxis.",
  [("e",16),("e",17),("e",18)])
T("gr-pruefung","gr","Die Prüfung",
  "Die schriftliche Prüfung besteht aus 7 Überblicksfragen in 90 Minuten. Dazu kommt eine schriftliche Reflexion mit mindestens 3500 Zeichen. Basis sind Präsentationen, Zeittafel und Zusatztexte.",
  [("e",2),("e",3)])

MC("gr-netze",[1],"Welche Ebene sozialer Absicherung verbindet die Einführung ausdrücklich mit dem Subsidiaritätsprinzip?","Familie und Ehrenamt",["Staatliche Sozialleistungen","Leistungen der Länder","Leistungen der Gemeinden"],"Die Folie nennt drei Ebenen und ordnet das Subsidiaritätsprinzip der Ebene Familie und Ehrenamt zu.")
MC("gr-begriffe",[],"Wie lautet die grob vereinfachte Unterscheidung?","Sozialarbeit hilft erzieherisch, Sozialpädagogik erzieht helfend",["Sozialarbeit erzieht strafend, Sozialpädagogik berät freiwillig","Sozialarbeit betreut Erwachsene, Sozialpädagogik nur Kinder","Sozialarbeit ist ehrenamtlich, Sozialpädagogik ist bezahlt"],"So steht es in der Einführung: erzieherisch helfen gegenüber helfend erziehen, fürsorgerisch-sozialpolitisch gegenüber pädagogisch-sozialerzieherisch.")
TF("gr-begriffe",[],"Die Vorlesung arbeitet mit einem Differenzansatz zwischen Sozialarbeit und Sozialpädagogik.",False,"Die Folie sagt das Gegenteil: Konvergenzansatz statt Differenzansatz.")
MC("gr-quellen",[],"Warum müssen historische Quellen laut LV kontextualisiert werden?","Quellen sind immer auch Deutungen",["Quellen sind meist gefälscht","Es gibt erst ab 1945 Quellen","Nur Gesetze gelten als Quelle"],"Es ist immer zu fragen, von wem, wann und zu welchem Zweck eine Quelle verfasst wurde.")
TF("gr-quellen",[],"Gesetzestexte zeigen zuverlässig, wie die Fürsorge in der Praxis ablief.",False,"Sie geben wenig Information über die Praxis und spiegeln die Intentionen von Behörden.",[("e",16)])
MULTI("gr-mandat",[19],"Welche Begriffe verwendet die Einführung, um den Ausgangspunkt Sozialer Arbeit zu beschreiben?",["Hilfestellung","Disziplinierung","Kontrolle"],["Gewinnorientierung","Selbstverwaltung"],"Soziale Arbeit als Reaktion auf problematische Lebenslagen: Hilfestellung, Disziplinierung, Kontrolle, „doppeltes Mandat“.",[("e",19)])
MULTI("gr-mandat",[],"Welche Bewegungen haben laut Einführung die Soziale Arbeit historisch geprägt?",["Arbeiter*innenbewegung","Frauenrechtsbewegung","Jugendbewegung","1968er Bewegung"],["Friedensbewegung der 1920er"],"Die Einführung nennt dazu noch die Frauenbewegung der 1970er/80er Jahre.",[("e",20)])
MC("gr-pruefung",[],"Wie viele Überblicksfragen enthält die schriftliche Prüfung?","7",["5","10","26"],"7 Überblicksfragen in 90 Minuten. Die 26 Leitfragen sind der Fragenkatalog zur Vorbereitung.")
MC("gr-netze",[],"Seit wann gibt es laut Einführung soziale staatliche Absicherung und soziale Netze?","Erst seit Mitte des 19. Jahrhunderts",["Seit dem Mittelalter","Erst seit 1945","Seit der Römerzeit"],"Sie sind relativ junge Errungenschaften und haben sich erst Mitte des 19. Jahrhunderts entwickelt.",[("e",8)])

# ---------------------------------------------------------------- Habsburgermonarchie

T("mon-epochen","mon","Zwei Ären der Gemeindeverwaltung",
  "In der liberalen Ära (1861–1895) galt „Jeder muss sich selbst helfen“, eine kommunale Versorgung war kaum ausgebaut. In der christlichsozialen Ära (1895–1918) gab es Neuerungen vor allem im Gesundheitswesen. In beiden fehlte ein einheitlicher gesamtstaatlicher Anspruch.",
  [("a1",3),("a1",4)])
T("mon-heimat","mon","Heimatrecht",
  "Das Heimatrechtsgesetz von 1863 war die Basis des Armenwesens. Nur Heimatberechtigte hatten Recht auf ungestörten Aufenthalt und Anspruch auf Armenversorgung. Das Gesetz schottete die Gemeinden präventiv ab, und auch die Novelle von 1896 half vielen Armen nicht.",
  [("a1",7),("a1",8),("a1",9)])
T("mon-subs","mon","Subsidiaritätsprinzip",
  "Die Gemeinde sprang erst ein, wenn niemand sonst zuständig war. Vorher waren gesetzlich verpflichtete Personen sowie private Vereine und Stiftungen gefragt. Das Prinzip hielt die öffentlichen Kosten niedrig und prägte die ganze Armenfürsorge.",
  [("a1",7),("a1",27)])
T("mon-armut","mon","Wie Armut gedeutet wurde",
  "Katholisches und liberales Lager sahen Armut als selbstverschuldet, als „Charakterschwäche“. Die Sozialdemokratie sah in der sozialen Frage eine politische Frage. Trotz Massenarbeitslosigkeit nach 1873 wurden Arme als „arbeitsscheu“ definiert und ab 1885 kriminalisiert.",
  [("a1",6),("a1",11)])
T("mon-formen","mon","Offene und geschlossene Armenfürsorge",
  "Offene Fürsorge bedeutete vorübergehende Geldaushilfen, oft erst nach Verkauf der letzten Wertgegenstände. Geschlossene Fürsorge fand in Armenanstalten mit Arbeitspflicht statt. Beides sollte nur das „Notdürftigste“ abdecken und war sozialdisziplinierend.",
  [("a1",19),("a1",20)])
T("mon-unsicht","mon","Unsichtbarmachung des Elends",
  "Aus Angst vor der Berührung mit Armut setzte man auf Wegsperren und Verstecken. Anstalten wurden ausgebaut, etwa das Lainzer Versorgungshaus 1904, und in die Peripherie verlegt. Sie blieben bis zum Ersten Weltkrieg überfüllt.",
  [("a1",21)])
T("mon-obdach","mon","Obdachlosenfürsorge statt Wohnungspolitik",
  "Hohe Mieten führten zu Obdachlosigkeit und zum Bettgeher*innentum, bei dem sich mehrere Personen ein Bett teilten. Massenquartiere waren bewusst abschreckend. Die Mehrheit der Obdachlosen war nicht in Wien heimatberechtigt.",
  [("a1",15),("a1",16)])
T("mon-vers","mon","Sozialversicherung und Armenfürsorge",
  "In den 1880er Jahren trennten sich Armen- und Arbeiter*innenpolitik. Die Sozialversicherung war bescheiden und galt nur für Lohnarbeiter*innen, war aber weniger diskriminierend als die Armenhilfe. Eine Alters-, Invaliditäts- oder Arbeitslosenversicherung fehlte.",
  [("a1",12),("a1",13),("a1",14)])
T("mon-kinder","mon","Armenkinder",
  "Kinder- und Jugendfürsorge war Teil der Armenfürsorge. Es ging darum, unversorgte, verwaiste und verwahrloste Kinder zu kontrollieren und möglichst billig zu verwahren. Die Idee von Erziehung und Prävention kam um die Jahrhundertwende auf, wurde praktisch aber kaum umgesetzt.",
  [("a1",25),("a1",26)])
T("mon-kost","mon","Kostkinderwesen",
  "Fremdunterbringung bei Pflegefamilien gegen Kostgeld war bis 1914 ein Dauerproblem, oft ungeregelt und unkontrolliert. Am Land war sie billiger, Pflegefamilien sahen auch Arbeitskräfte und Pflegegeld. Diese Kontinuität reicht bis in die 1960er Jahre.",
  [("a1",28)])
T("mon-verw","mon","„Verwahrlosung“",
  "„Verwahrlosung“ war das zentrale Schlagwort mit moralischer Komponente: Es ging nicht um Schutz, sondern um Ausgrenzung, weil „Ansteckungsgefahr“ unterstellt wurde. Nach der Jahrhundertwende setzte mit der Erziehungsfürsorge ein Paradigmenwechsel ein.",
  [("a1",30)])
T("mon-poli","mon","Politische Anstöße",
  "Das sozialdemokratische Kommunalprogramm von 1896 war ein erstes Modell für Familien-, Bevölkerungs- und Gesundheitspolitik. Neu war die Konzentration auf Bedürftige, die nicht Lohnarbeiter waren, etwa Säuglinge und Schwangere. Darauf baute später das Rote Wien auf.",
  [("a1",24)])

MC("mon-heimat",[4],"Was gewährte das Heimatrechtsgesetz von 1863 den Heimatberechtigten?","Ungestörten Aufenthalt und Anspruch auf Armenversorgung",["Eine staatliche Pension und freie Wohnungswahl","Das Wahlrecht und einen fixen Unterhaltsbetrag","Eine Ausbildung und freie Arbeitsplatzwahl"],"Heimatberechtigten wurde das Recht auf ungestörten Aufenthalt und Anspruch auf Armenversorgung gewährt.")
MC("mon-heimat",[4],"Welchem Zweck diente das Heimatgesetz laut Folie vor allem?","Präventive Abschottung vor Armenversorgungsansprüchen",["Förderung der Zuwanderung nach Wien","Schaffung eines Rechtsanspruchs für alle Armen","Aufbau einer staatlichen Sozialversicherung"],"Ein Großteil der Armen fiel aus den Regelungen heraus, und die Gemeinden hielten so ihre Kosten gering.",[("a1",8)])
MC("mon-heimat",[4],"Was änderte die Novelle des Heimatrechts von 1896?","Heimatrecht nach zehn Jahren ununterbrochenem Aufenthalt",["Heimatrecht für alle in Wien Arbeitenden ab dem ersten Tag","Abschaffung des Heimatrechts in allen Gemeinden","Heimatrecht nur noch durch Geburt in der Gemeinde"],"Das ist das „Ersitzungsprinzip“: Nicht mehr nur die Geburt, sondern auch der Aufenthalt war maßgeblich.",[("a1",9)])
MULTI("mon-heimat",[4],"Für wen war der Aufenthaltsnachweis nach dem Ersitzungsprinzip besonders schwierig?",["Bettgeher*innen","Saisonarbeiter*innen","Tagelöhner*innen","Dienstbot*innen"],["Facharbeiter in stabiler Anstellung"],"Sozial stabilere Facharbeiterkreise waren die Ausnahme, die anderen blieben häufig rechtlich und sozial ausgegrenzt.",[("a1",9)])
TF("mon-heimat",[4],"Auf die Armenversorgung nach dem Heimatrechtsgesetz bestand ein Rechtsanspruch.",False,"Die Folie hält fest: Ein Rechtsanspruch bestand nicht darauf.",[("a1",7)])
TF("mon-heimat",[4,3],"Laut Resümee der Folie dienten Gesetz und Reform der Geringhaltung der Gemeindekosten.",True,"Genau so das Resümee zur Novelle von 1896.",[("a1",9)])
MC("mon-subs",[1],"Wann bestand nach dem Subsidiaritätsprinzip eine Versorgungspflicht der Gemeinde?","Wenn keine gesetzlich verpflichteten Personen zur Verfügung standen",["Sobald eine Person in der Gemeinde wohnte","Wenn eine Person dies schriftlich beantragte","Immer dann, wenn der Staat es anordnete"],"Vorrangig zuständig waren Verwandte, Ehegatten und Vormünder.",[("a1",7)])
MC("mon-subs",[1],"Wer übernahm die Armenversorgung, bevor die Gemeinde eintrat?","Private Vereine und Stiftungen",["Das Ministerium für Soziale Fürsorge","Die staatliche Arbeitslosenversicherung","Die Bezirksjugendämter"],"Erst bei finanzieller Überforderung dieser privaten Träger trat die Gemeinde ein.",[("a1",7)])
TF("mon-subs",[1],"In der offenen Armenkinderpflege waren zuerst Familie oder Verwandte zuständig.",True,"Erst nach Überprüfung gab es Erziehungs-, Waisen- und Kostgelder.",[("a1",27)])
TF("mon-epochen",[2],"In der christlichsozialen Ära gab es erstmals einen einheitlichen gesamtstaatlichen Versorgungsanspruch.",False,"Auch 1895–1918 gab es „weiterhin keinen“ einheitlichen Anspruch, sondern Kompensation durch Private und Familien.",[("a1",4)])
MATCH("mon-epochen",[2,3],"Ordne die Merkmale den Ären zu.",[("Liberale Ära","„Jeder muss sich selbst helfen“"),("Christlichsoziale Ära","Neuerungen im Gesundheitswesen"),("Rotes Wien","Allgemeines Anrecht auf Fürsorge"),("Austrofaschismus","Rücknahme des Anrechts auf Fürsorge")],"Das Subsidiaritätsprinzip prägt die Monarchie; das Rote Wien bricht damit, der Austrofaschismus nimmt den Bruch zurück.",[("a1",3),("a1",4),("rw",9),("t",5)])
MC("mon-epochen",[3],"Welcher Grundsatz galt laut Folie insbesondere in den Städten?","„Überleben kann nur, wer arbeitet.“",["„Arbeit ist Privatsache.“","„Die Gemeinde sorgt für alle.“","„Jedem nach seinen Bedürfnissen.“"],"Hinzu kam das Interesse an der Aufrechterhaltung der öffentlichen Ordnung.",[("a1",5)])
MC("mon-armut",[3],"Wie deuteten das katholische und das liberale Lager Armut?","Als selbstverschuldet, als „Charakterschwäche“",["Als politische Frage der Verteilung","Als unvermeidliche Folge von Krankheit","Als staatliches Versagen"],"Der Diskurs folgte sittlich-moralischen Kriterien. Ausnahme waren krankheitsbedingte Ursachen.",[("a1",6)])
MC("mon-armut",[3],"Was sahen die Zwangsarbeitergesetze von 1885 vor?","Anhaltung in Zwangsarbeits- und Besserungsanstalten",["Einen Arbeitsplatz für jede arbeitslose Person","Eine Versicherung gegen Arbeitsunfälle","Verpflichtende Lehrstellen für Waisen"],"Grund konnten eine Verurteilung wegen Landstreicherei, Bettelei oder „Arbeitsscheu“ sein: die Kriminalisierung von Armut.",[("a1",11)])
TF("mon-armut",[3],"Die Sozialdemokratie sah in der sozialen Frage eine politische Frage und forderte Sozialreformen.",True,"Damit grenzte sie sich vom katholischen und liberalen Lager ab.",[("a1",6)])
MC("mon-armut",[],"Welcher Widerspruch prägte die große Depression ab 1873?","Arbeitslosigkeit stieg stark an und wurde zugleich als „arbeitsscheu“ gedeutet",["Löhne stiegen stark, doch niemand wollte arbeiten","Die Gemeinden hatten viel Geld, aber keine Armen","Die Armen wanderten ab, die Anstalten blieben voll"],"Depression 1873–1896: Der Börsenkrach verstärkte die Mobilität, die Folge wurde moralisch bewertet und bestraft.",[("a1",10),("a1",11)])
MATCH("mon-formen",[3],"Offen oder geschlossen?",[("Armenanstalten mit Arbeitspflicht","geschlossene Fürsorge"),("Vorübergehende Geldaushilfen","offene Fürsorge"),("Lainzer Versorgungshaus","geschlossene Fürsorge"),("Mietzinsbeihilfen","offene Fürsorge")],"Geschlossen heißt in einer Anstalt, offen heißt Unterstützung außerhalb.",[("a1",19),("a1",20),("a1",21)])
MC("mon-formen",[3],"Was war Voraussetzung für Hilfen in der offenen Armenfürsorge?","Verkauf der letzten eigenen Wertgegenstände",["Ein Jahr Mitgliedschaft in einer Gewerkschaft","Bestätigung des Pfarrers über gute Sitten","Eintritt in eine Armenanstalt"],"Die Maßnahme sollte dazu beitragen, dass die Betroffenen ohne Unterstützung der Gemeinde überleben.",[("a1",20)])
MC("mon-formen",[3],"Welcher Satz fasst die Haltung der geschlossenen Armenpflege zusammen?","„Wer nicht arbeitet, soll auch nicht essen“",["„Wer Kindern Paläste baut, reißt Kerkermauern nieder“","„Die Gesellschaft ist ihr Sachwalter“","„So kurz wie notwendig“"],"Unterstützung sollte nur das „Notdürftigste“ umfassen. Die anderen Sätze stammen aus späteren Epochen.",[("a1",19)])
MC("mon-unsicht",[3],"Was war das Ziel der Verlegung Armer in Anstalten an der Peripherie?","Armut aus dem Blickfeld zu bringen",["Bessere Luft zur Heilung aller Kranken","Billiger Boden für neue Gemeindebauten","Nähe zu Arbeitsplätzen in der Industrie"],"Das Stichwort ist Unsichtbarmachung des Elends: Wegsperren und Verstecken.")
MC("mon-unsicht",[],"Welche Funktion hatte das Lainzer Versorgungshaus von 1904?","Zentralstelle der geschlossenen Armenpflege für Personen über 14",["Erste Schule für Fürsorgerinnen in Wien","Heim für verlassene Säuglinge","Sitz der städtischen Berufsvormundschaft"],"Ein großer Armenhauskomplex mit „Drehscheibenfunktion“.")
MC("mon-obdach",[],"Was bedeutet „Bettgeher*innentum“?","Mehrere Personen nutzen dasselbe Bett, ohne Mietvertrag",["Kranke werden zu Hause von Ärzten besucht","Arme schlafen in städtischen Notspitälern","Kinder werden zu Pflegefamilien verschickt"],"Es ist die serielle Nutzung eines Bettes als Folge der „Wucherzinse“.",[("a1",15)])
TF("mon-obdach",[4],"Die Mehrheit der Obdachlosen in Wien war dort heimatberechtigt.",False,"Die Mehrheit war nicht in Wien heimatberechtigt, meist jung, ledig und vorwiegend männlich.",[("a1",15)])
TF("mon-vers",[],"Die Sozialversicherung der Zeit galt nur für Lohnarbeiter*innen, sie sparte damit einen großen Teil der Armen aus.",True,"Kranken- und Unfallversicherung wurde von Arbeiter- und Unternehmerseite finanziert, nur für LohnarbeiterInnen.",[("a1",13)])
MULTI("mon-vers",[],"Was kam vor 1918 trotz Debatten nicht zustande oder fehlte?",["Staatliche Arbeitslosenversicherung","Witwen- und Waisenversicherung","Alters- und Invaliditätssicherung"],["Kranken- und Unfallversicherung"],"Nur Kranken- und Unfallversicherung existierten, finanziert aus Beiträgen.",[("a1",13)])
MC("mon-vers",[],"Mit welchen Methoden sollte die soziale Frage laut Folie bearbeitet werden?","Individualisierung, Pädagogisierung, Medikalisierung",["Verstaatlichung, Enteignung, Umverteilung","Mitbestimmung, Selbstverwaltung, Streik","Digitalisierung, Automatisierung, Auslagerung"],"Daraus ergibt sich eine Kontinuität der Fürsorge: die Verknüpfung von Hilfe, Schutz und Kontrolle.",[("a1",14)])
MC("mon-kinder",[],"Welches Interesse stand in der Kinder- und Jugendfürsorge vor 1900 im Vordergrund?","Kontrollieren und möglichst billig verwahren",["Individuelle Förderung aller Begabungen","Psychoanalytische Beratung der Eltern","Rückführung in die Herkunftsfamilie"],"Die Folie spricht vom Disziplinierungscharakter der Fürsorge.",[("a1",26)])
MC("mon-kinder",[],"Was brachte die Reform der Armenkinderpflege von 1901 für Frauen?","Erstmals auch Frauen als Bezirksarmenrät*innen",["Das aktive Wahlrecht auf Bezirksebene","Bezahlte Stellen in allen Waisenhäusern","Die rechtliche Obsorge für ihre Kinder"],"Betreuung und Organisation oblagen den Bezirksarmenrät*innen, nun auch erstmals Frauen.",[("a1",26)])
TF("mon-kost",[],"Das Kostkinderwesen war bis 1914 vielfach ungeregelt und unkontrolliert.",True,"Es gab erwiesene Missstände in Pflegefamilien. Die Kontinuität reicht bis in die 1960er Jahre.")
MC("mon-kost",[],"Welche Motive hatten ländliche Pflegefamilien laut Folie oft?","Pflegegeld und potentielle Arbeitskräfte",["Religiöser Auftrag und Schulpflicht","Prestige und politische Ämter","Adoption und Erbschaft"],"Die Folie nennt egoistische Motive: Interesse am Pflegegeld.")
MC("mon-verw",[],"Womit wurde ein „verwahrlostes“ Kind in einem Zitat gleichgestellt?","Mit einem an einem epidemischen Leiden Erkrankten",["Mit einem Opfer eines Verbrechens","Mit einem begabten, aber armen Kind","Mit einem Waisenkind in Not"],"Das zeigt die moralische Komponente: Separation wegen „Ansteckungsgefahr“ statt Schutz.")
TF("mon-verw",[],"Der Bezirksschulrat agierte als „pädagogische Polizei“ und gab nicht angepasste Kinder in Besserungsanstalten ab.",True,"So die Folie. Noch 1906 legitimierte das Vagabundengesetz solche Einweisungen.")
MC("mon-poli",[11],"Was war am sozialdemokratischen Kommunalprogramm von 1896 neu?","Konzentration auf Bedürftige, die nicht Lohnarbeiter sind",["Abschaffung aller privaten Wohltätigkeit","Die Einführung der Generalvormundschaft","Das Ende des Heimatrechts"],"Säuglinge, Schwangere, Wöchnerinnen und bestimmte Krankheiten rücken ins Zentrum: Die Folie verweist hier auf das Rote Wien ab 1919.")
ORD("mon-epochen",[2,3],"Bringe die Ereignisse der Monarchie in die richtige Reihenfolge.",[("1863","Heimatrechtsgesetz"),("1885","Zwangsarbeitergesetze"),("1896","Novelle mit Ersitzungsprinzip"),("1901","Reform der Armenfürsorge")],"Vom Heimatrecht über die Kriminalisierung der Armut zu den ersten Reformen.",[("a1",7),("a1",11),("a1",9),("a2",3)])

# ---------------------------------------------------------------- Reformen und Vorbilder

T("ref-1901","ref","Reform von 1901",
  "Die christlich-soziale Reform differenzierte die Fürsorge nach Alter und Bedarf und baute die Versorgung von Kindern aus. Ziel war eine bessere Zusammenarbeit von privater und öffentlicher Armenpflege, zugleich aber auch verstärkte Kontrolle der Armen, das „Erfassen“.",
  [("a2",2),("a2",3)])
T("ref-ehren","ref","Ehrenamt und freiwillige Fürsorge",
  "Ehrenamtliche Armenrät*innen und private Wohltätigkeit glichen die fehlende staatliche Versorgung aus. Das Amt war unbezahlt und setzte keine Ausbildung voraus. Später prangerte die Sozialdemokratie das als „Wohltäterei“ an, weil Beschenkte Dankbarkeit und Wohlverhalten schuldeten.",
  [("a2",7),("a2",8),("a2",13)])
T("ref-elb","ref","Elberfelder System",
  "1853 entwickelt, als Antwort auf Zuwanderung und wachsende Armut in Textilstädten. Kennzeichen sind Dezentralisierung, Ehrenamt, Hilfe zur Selbsthilfe, Quartierprinzip, geistige Mütterlichkeit und der Hausbesuch als Friendly Visiting. Es wurde Vorbild für die freiwillige Fürsorge.",
  [("a2",8),("a2",9)])
T("ref-selbst","ref","Hilfe zur Selbsthilfe",
  "Einmalige Gaben helfen nicht, Hilfe soll temporär und gezielt sein, damit Menschen danach ohne Fürsorge auskommen. Die Folie nennt das auch Selbstermächtigung. Daneben gab es ökonomische Interessen, weil soziale Ausgaben nicht zu hoch werden sollten.",
  [("a2",10)])
T("ref-mutter","ref","Geistige Mütterlichkeit",
  "Das Ideal der bürgerlichen Frauenbewegung stellte der biologischen Mutterschaft eine soziale Mütterlichkeit zur Seite. So konnten Frauen sich über das soziale Ehrenamt gesellschaftlich integrieren. Zugleich setzte es das bürgerliche Rollenmodell fort: Fürsorge als öffentliche Reproduktionsarbeit.",
  [("a2",11)])
T("ref-modelle","ref","Zwei Modelle aus England und den USA",
  "Aus der Verelendung im Zuge der Industrialisierung entstanden neue private Einrichtungen mit Vorbildcharakter. Das eine Modell ist die Einzelfallhilfe, Social Case Work. Das andere ist das Settlement, die Nachbarschaftshilfe als Vorläuferin der Gemeinwesenarbeit.",
  [("a2",14)])
T("ref-toynbee","ref","Toynbee Hall",
  "Henrietta und Samuel Barnett kritisierten das ungleiche Verhältnis von Geber und Empfänger, das die Selbstachtung der Armen zerstört. Akademiker lebten als „Settler“ im Armenviertel, um zu lehren und zu lernen. Bildung und Kultur sollten die Sozialdisziplinierung ersetzen.",
  [("a2",16),("a2",17),("a2",18),("a2",20)])
T("ref-hull","ref","Hull House",
  "Jane Addams gründete Hull House 1889 in Chicago nach dem Vorbild von Toynbee Hall, das sie 1888 kennengelernt hatte. Das Nachbarschaftszentrum bot Kindergarten, Volksküche und Bildung, vor allem für mittellose Frauen und Kinder. Addams engagierte sich auch sozialpolitisch und untersuchte die Lebensbedingungen im Viertel.",
  [("a2",25),("a2",26),("a2",27),("a2",28),("a2",33)])
T("ref-richmond","ref","Mary Richmond und die soziale Diagnose",
  "Mary Richmond konzentrierte sich im Altamont Hotel in Baltimore auf Einzelfallhilfe. In Anlehnung an die ärztliche Diagnose suchte sie die individuellen Ursachen sozialer Not. Ihr Werk „Social Diagnosis“ von 1917 gilt als zentrales Werk, und sie forderte eine professionelle Ausbildung.",
  [("a2",34),("a2",37),("a2",38),("a2",39)])
T("ref-salomon","ref","Alice Salomon",
  "Alice Salomon gründete 1908 in Berlin die erste interkonfessionelle Soziale Frauenschule und 1925 eine Akademie für Führungskräfte. Sie verband Frauenbewegung, Ausbildung und Wissenschaft. Die Nationalsozialisten entzogen ihr die Ämter, 1937 wurde sie ausgewiesen.",
  [("a2",46),("a2",47),("a2",50),("a2",52)])
T("ref-ott","ref","Ottakringer Settlement",
  "Nach dem Vorbild von Toynbee Hall entstand 1901 das Ottakringer Settlement in Wien, gegründet von Marie Lang. Es kümmerte sich um Kinder ärmerer Schichten und um die Weiterbildung der Mütter, unter Ausschluss jeder politischen Tätigkeit. 1938 wurde der Verein enteignet und aufgelöst.",
  [("a2",54),("a2",55),("a2",60)])
T("ref-key","ref","Das Jahrhundert des Kindes",
  "Das Buch der schwedischen Reformpädagogin Ellen Key von 1902 (auf den Folien auch „Kay“) war ein zeitgenössisches Standardwerk. Es kritisierte Erziehungspraktiken von Zucht und Drill.",
  [("a2",5)])

MC("ref-1901",[],"Was war das Ziel der Reform der Armenfürsorge von 1901?","Bessere Zusammenarbeit privater und öffentlicher Armenpflege und mehr Kontrolle",["Abschaffung der privaten Armenpflege zugunsten der Gemeinde","Einführung eines allgemeinen Anrechts auf Fürsorge","Trennung von Gesundheitsfürsorge und Jugendwohlfahrt"],"„Erfassen“ steht auf der Folie als Stichwort für die verstärkte Kontrolle.")
MC("ref-ehren",[9],"Welche zwei Merkmale kennzeichnen das Amt der Armenrät*innen?","Unbezahlt und keine Ausbildung",["Bezahlt und mit Matura","Unbezahlt und zweijährige Ausbildung","Bezahlt und ohne Ausbildung"],"Das Amt setzte zudem männliche Gemeindemitglieder voraus, eine Ausnahme waren die Kostkinder.",[("a2",7)])
TF("ref-ehren",[9,23],"Frauen wurden als Armenrätinnen vor allem bei den Kostkindern und Waisenkindern eingesetzt.",True,"Die Folie vermerkt dazu „Geschlechterrollen!!“ und geschlechtsspezifische Arbeitsteilung.",[("a2",7)])
MC("ref-ehren",[9],"Was warf die Sozialdemokratie der privaten „Wohltäterei“ vor?","Beschenkte stehen in Schuld und müssen sich dankbar verhalten",["Die Hilfe war zu großzügig und zu teuer","Wohltäter arbeiteten ohne jede Religion","Sie finanzierte die Gewerkschaften"],"Privatwohltätigkeit operierte somit keineswegs als neutrales Hilfskonzept.",[("a2",13)])
MULTI("ref-ehren",[9],"Welche Prinzipien der freiwilligen Fürsorge nennt die Folie?",["Individuelle Bedürftigkeit","Gesetzlicher Anspruch nicht notwendig","Ehrenamt"],["Allgemeines Anrecht auf Fürsorge","Berufsausbildung als Pflicht"],"Vorbild war das Elberfelder System.",[("a2",8)])
TF("ref-ehren",[9],"In Österreich spielte private Wohltätigkeit eine größere Rolle als in den USA und Deutschland.",False,"Sie spielte eine vergleichsweise geringe Rolle, blieb aber wegen der schwachen Sozialgesetzgebung relevant.",[("a2",12)])
MULTI("ref-elb",[7],"Was gehört zu den Charakteristika des Elberfelder Systems?",["Quartierprinzip","Ehrenamtlichkeit","Friendly Visiting","Dezentralisierung"],["Zentrale staatliche Verwaltung","Rechtsanspruch auf Hilfe"],"Dazu kommen Hilfe zur Selbsthilfe und geistige Mütterlichkeit.")
MC("ref-elb",[7],"Was ist mit „Friendly Visiting“ gemeint?","Der Hausbesuch",["Der Besuch in einer Klinik","Eine Spendengala","Ein Kurs für Eltern"],"Das Hausbesuchsprinzip wurde über Jahrzehnte zentral, später auch als Kontrollinstrument.",[("a2",9)])
MC("ref-elb",[7],"Wann wurde das Elberfelder System entwickelt?","1853",["1889","1901","1917"],"Ausgangspunkt waren Zuwanderung, dichte Besiedelung und mehr Arme in den Textilstädten.",[("a2",9)])
MC("ref-selbst",[7],"Was meint „Hilfe zur Selbsthilfe“?","Temporäre, gezielte Hilfe, damit Menschen danach ohne Fürsorge auskommen",["Dauerhafte finanzielle Absicherung aller Armen","Armen wird das Betteln grundsätzlich erlaubt","Familien müssen Angehörige selbst pflegen"],"Die Folie spricht von Selbstermächtigung und Empowerment, merkt aber auch ökonomische Interessen an.")
TF("ref-selbst",[],"Hinter „Hilfe zur Selbsthilfe“ standen neben dem Hilfsaspekt auch ökonomische Interessen.",True,"Soziale Ausgaben sollten nicht zu hoch werden.")
MC("ref-mutter",[23],"Was ist „geistige Mütterlichkeit“?","Ideal der bürgerlichen Frauenbewegung: weiblicher Beitrag über soziales Ehrenamt",["Eine Ausbildung für Mütter in Geburtskliniken","Ein Gesetz über die Obsorge unverheirateter Mütter","Das Mutterkreuz als öffentliche Auszeichnung"],"Soziale Arbeit wird damit als öffentliche Reproduktionsarbeit weiblich definiert.")
TF("ref-mutter",[23],"Die geistige Mütterlichkeit brach mit dem bürgerlichen Geschlechterrollenmodell.",False,"Die Folie nennt sie eine Fortsetzung des bürgerlichen Geschlechterrollenmodells.")
MC("ref-modelle",[7],"Welches Modell gilt als Vorläufer der Gemeinwesenarbeit?","Das Settlement",["Das Social Case Work","Das Elberfelder Quartier","Die Berufsvormundschaft"],"Case Work ist dagegen Vorläufer der vertieften Einzelfallhilfe.")
MATCH("ref-modelle",[7],"Verbinde Person und Einrichtung.",[("Barnett","Toynbee Hall, London"),("Jane Addams","Hull House, Chicago"),("Mary Richmond","Altamont Hotel, Baltimore"),("Marie Lang","Ottakringer Settlement, Wien")],"Die ersten beiden und Lang stehen für das Settlement, Richmond für die Einzelfallhilfe.",[("a2",16),("a2",26),("a2",34),("a2",55)])
MC("ref-toynbee",[7],"Was war die Kernidee von Toynbee Hall?","Gemeinsames Leben mit den Armen, um zu lehren und von ihnen zu lernen",["Arme in Anstalten am Stadtrand unterbringen","Spenden reicher Familien zentral verteilen","Kinder in Pflegefamilien am Land vermitteln"],"Die persönliche Beziehung zwischen „Settlern“ und Bewohner*innen stand im Zentrum.",[("a2",18)])
MC("ref-toynbee",[7],"Was kritisierte Toynbee Hall an der karitativen Armenfürsorge?","Ungleiches Verhältnis von Geber und Empfänger zerstört die Selbstachtung",["Sie gab den Armen zu viel Geld","Sie war zu stark wissenschaftlich fundiert","Sie schloss Akademiker von der Arbeit aus"],"Praktische Tätigkeit und Hilfe statt Mitleid und Erleichterung des Gewissens durch Spenden.",[("a2",17)])
TF("ref-toynbee",[7],"Die Tätigkeit der „Settler“ in Toynbee Hall wurde bezahlt.",True,"Die Settler waren junge Männer, in der Regel aus der sozialen Oberschicht.",[("a2",18)])
MC("ref-toynbee",[26],"Woran erinnern die wöchentlichen Vieraugengespräche zwischen Barnett und den Bewohnern laut Folie?","An Supervision",["An ein Verhör","An eine Bilanzprüfung","An eine Beichte"],"Es ging um Austausch und Beratung. Die Folie verweist selbst auf Supervision.",[("a2",20)])
MC("ref-hull",[7],"Worin ähnelte Hull House Toynbee Hall?","Unter den Armen leben und von ihnen lernen",["Als rein männliche Einrichtung von Akademikern","Als behördliche Kontrollstelle der Stadt","Als Heim für Waisen unter 6 Jahren"],"Hull House war aber auf Frauen und Kinder konzentriert, die Mitarbeiterinnen waren in der Regel ehrenamtliche Frauen.",[("a2",27),("a2",28)])
MC("ref-hull",[7],"Was sah Addams in der Großstadt?","Einen Sozialisierungsraum mit eigener positiver Bedeutung",["Die Hauptursache allen sozialen Übels","Einen Ort, den Arme verlassen sollten","Einen Markt für billige Arbeitskräfte"],"Die Folie betont: nicht Kritik an der Großstadt.",[("a2",33)])
MULTI("ref-hull",[7],"Welche Forderungen stellte Hull House sozialpolitisch?",["Arbeitslosenhilfe","Arbeitszeitverkürzung","Mindestlöhne"],["Abschaffung der Schulpflicht","Einführung von Zwangsarbeit"],"Auch die Verbesserung des Arbeitsschutzes gehörte dazu.",[("a2",33)])
MC("ref-richmond",[7,26],"Worauf gründete Mary Richmonds Hilfskonzept?","Auf einer wissenschaftlich fundierten „sozialen Diagnose“",["Auf Nachbarschaftsabenden und Musik","Auf gesetzlichen Zwangsmaßnahmen","Auf religiöser Unterweisung"],"Vorbild war die ärztliche Diagnose, es ging um individuelle körperliche und psychische Ursachen.",[("a2",37)])
MC("ref-richmond",[7],"Wann erschien „Social Diagnosis“?","1917",["1889","1902","1929"],"Es gilt als zentrales Werk sozialer Einzelfallhilfe.",[("a2",39)])
TF("ref-richmond",[5],"Richmond war Vorbild sowohl für Alice Salomon als auch für Ilse Arlt.",True,"So steht es auf der Folie zur Einzelfallhilfe.",[("a2",37)])
MC("ref-richmond",[24],"Warum forderte Richmond Fortbildungskurse im Friendly Visiting?","Soziale Arbeit soll organisiert statt punktuell sein",["Ehrenamtliche sollten Spenden sammeln lernen","Frauen sollten vom Beruf ferngehalten werden","Der Staat sollte die Kurse kontrollieren"],"Geschäftsmäßig organisiert, zur Optimierung der vorhandenen Ressourcen.",[("a2",38)])
MC("ref-salomon",[5],"Was gründete Alice Salomon 1908 in Berlin?","Die erste interkonfessionelle Soziale Frauenschule",["Die Akademie für soziale Verwaltung","Das erste Jugendamt Deutschlands","Das Settlement in Ottakring"],"Dauer 2 Jahre, Wissen und Haltung: „Pflanzstätte sozialer Gesinnung“. Sie war Vorbild für Arlt.",[("a2",47),("eb",11)])
MATCH("ref-salomon",[],"Ordne Salomons Lebensdaten zu.",[("1899","erster Jahreskurs zur Wohlfahrtspflege"),("1908","Soziale Frauenschule"),("1925","Deutsche Akademie"),("1937","Ausweisung, Emigration in die USA")],"Ein Leben zwischen Frauenbewegung, Ausbildung und Vertreibung.",[("a2",46),("a2",47),("a2",50),("a2",52)])
TF("ref-salomon",[],"Salomon promovierte 1906 über die Ursachen der ungleichen Entlohnung von Männer- und Frauenarbeit.",True,"Ein in der Frauenbewegung kontrovers diskutiertes Thema.",[("a2",46)])
MC("ref-ott",[7],"Nach welchem Vorbild entstand das Ottakringer Settlement?","Toynbee Hall in London",["Hull House in Chicago","Altamont Hotel in Baltimore","Elberfeld in Deutschland"],"Es wurde 1901 vom Verein Wiener Settlement gegründet.")
TF("ref-ott",[],"Das Ottakringer Settlement schloss laut Statuten jede politische Tätigkeit aus.",True,"Ziel war die Hebung des „geistigen, körperlichen und sittlichen Niveaus“, „unter Ausschluss jeder politischen Thätigkeit“.",[("a2",54)])
TF("ref-ott",[15],"Nach 1945 kehrten die jüdischen Mitarbeiterinnen ins Ottakringer Settlement zurück.",False,"Sie fehlten: Sie mussten emigrieren oder wurden ermordet. Der Verein wurde 1938 enteignet, erst 1950 kam er in das leere Haus zurück.",[("a2",60)])
MC("ref-key",[],"Was kritisierte Ellen Key in „Das Jahrhundert des Kindes“?","Erziehungspraktiken von Zucht und Drill",["Die Ausbildung von Fürsorgerinnen","Die Schließung der Waisenhäuser","Den Bau neuer Kindergärten"],"Ein zeitgenössisches Standardwerk von 1902.")

# ---------------------------------------------------------------- Vom Ehrenamt zum Beruf

T("ber-bv","ber","Berufsvormundschaft",
  "Uneheliche Kinder brauchten einen rechtlichen Vertreter, weil Mütter die Obsorge nicht übernehmen durften. „Listenvormünder“ aus den Wählerlisten kümmerten sich aber nicht. Ab 1913 entstand in Ottakring eine Lösung mit Team und Fürsorgestellen, die Vorläufer der Bezirksjugendämter.",
  [("eb",3),("eb",4),("eb",5)])
T("ber-aufgaben","ber","Was die Berufsvormundschaft tat",
  "Sie forschte Väter aus, holte Unterhalt ein und ließ die „Mündel“ ärztlich kontrollieren. Hausbesuche dienten der Belehrung lediger Mütter, also Hilfe und Kontrolle zugleich. Der Verbindungsdienst mit Geburtskliniken erfasste bedürftige Mütter und Kinder.",
  [("eb",6)])
T("ber-arlt","ber","Ilse Arlt und die Fachkurse",
  "Ilse Arlt gründete 1912 die Vereinigten Fachkurse für Volkspflege, die erste österreichische Ausbildung für soziale Arbeit. Sie wollte ein neues weibliches Berufsfeld und die Professionalisierung der Fürsorge. Bezahlte und unbezahlte Arbeit sollten dieselbe gründliche Vorbereitung bekommen.",
  [("eb",8),("eb",11),("eb",12)])
T("ber-beduerf","ber","Arlts Bedürfnislehre",
  "Aus Einzelfällen entwickelte Arlt dreizehn Bedürfnisklassen als Maßstab für Forschung und Hilfe. Fürsorge soll schon vorbeugend einschreiten, sobald eine Spannung zwischen einfachster ausreichender Bedürfnisbefriedigung und Unterbefriedigung vorliegt. Das widerlegt Vorurteile über selbstverschuldete Armut.",
  [("eb",18),("eb",19),("eb",20)])
T("ber-wk","ber","Erster Weltkrieg",
  "Im Krieg stiegen Säuglingssterblichkeit und Not. 1916 entstand ein Ministerium für soziale Fürsorge. Die Jugendfürsorge erweiterte sich auf „erzieherische Gefährdung“ und die Versorgung von Kriegerwitwen und Waisen, der Verbindungsdienst an Gebäranstalten wurde ausgebaut.",
  [("eb",22),("eb",23),("eb",24)])
T("ber-ehe","ber","Ehe- und Kinderlosigkeit",
  "Wegen des Mangels an Ehrenamtlichen beschloss Wien 1917 Ehe- und Kinderlosigkeit als Voraussetzung für das Fürsorgerinnenamt. 1919 wurde das wieder aufgehoben. Der Beruf lässt sich so auch als weiblicher Lebensentwurf jenseits von Familie und Mutterschaft lesen.",
  [("eb",25)])
T("ber-ja","ber","Geburt des Jugendamtes 1917",
  "1917 wurde die Berufsvormundschaft für uneheliche Kinder auf alle Wiener Bezirke ausgedehnt und das Jugendamt gegründet. Der umfassende Ausbau folgte erst im Roten Wien. Parallel entstanden städtische Fachkurse mit dem Berufstitel „Fürsorgerin“ und weitere Ausbildungsstätten.",
  [("eb",26),("eb",27),("z",1)])

MC("ber-bv",[8],"Warum brauchte es überhaupt eine Vormundschaft für uneheliche Kinder?","Mütter durften die rechtliche Obsorge nicht übernehmen",["Väter hatten kein Interesse an Geld","Die Kirche untersagte jede Pflege durch Mütter","Kinder hatten sonst keinen Schulplatz"],"Die Frage der rechtlichen Vertretung war der Kern des Problems.")
MC("ber-bv",[8],"Was waren „Listenvormünder“?","Aus Wählerlisten bestimmte Männer, die nur pro forma Vormund waren",["Ausgebildete Fürsorgerinnen der Gemeinde","Ärzte aus den städtischen Geburtskliniken","Väter unehelicher Kinder auf einer Meldeliste"],"Sie übernahmen die Vertretung, wenn kein männlicher Verwandter da war, kümmerten sich aber nicht um das Wohl der Kinder.",[("eb",3)])
MULTI("ber-aufgaben",[8],"Welche Aufgaben hatte die Berufsvormundschaft?",["Väter unehelicher Kinder ausforschen","Unterhaltszahlungen einholen","Ärztliche Kontrolle der Mündel","Hausbesuche bei ledigen Müttern"],["Schulen für Fürsorgerinnen leiten"],"Dazu kam der Verbindungsdienst mit Geburtskliniken.")
MC("ber-aufgaben",[22],"Was geschah im „Verbindungsdienst“ mit Geburtskliniken?","Ausforschen bedürftiger Mütter und Kinder",["Finanzierung neuer Krankenhäuser","Ausbildung von Hebammen","Verteilung von Spenden aus dem Ausland"],"Ein Instrument von Hilfe und Erfassung, das in späteren Epochen erweitert wurde.")
MC("ber-bv",[8,24],"Was geschah 1913 in der Berufsvormundschaft erstmals?","10 Dienststellen für bezahlte Berufspflegerinnen",["Einführung der Generalvormundschaft für ganz Wien","Akademische Ausbildung für alle Pflegerinnen","Abschaffung des Ehrenamts in der Jugendwohlfahrt"],"Der Grund war ein Mangel an ehrenamtlichem Personal: der erste Schritt zu entlohnter Berufsarbeit, noch ohne Ausbildung.",[("eb",5)])
TF("ber-bv",[24],"Die ersten bezahlten Berufspflegerinnen 1913 mussten eine abgeschlossene Ausbildung nachweisen.",False,"Die Folie betont: entlohnte soziale Berufsarbeit „ohne Ausbildung als Voraussetzung“.",[("eb",5)])
MULTI("ber-bv",[8],"Wer arbeitete im Team der Berufsvormundschaft?",["Arzt","Rechtskundiger Berufsvormund","Pflegerinnen","Juristen"],["Psychoanalytiker"],"Das Team wurde von ehrenamtlichen Mitarbeiter*innen ergänzt.",[("eb",5)])
MC("ber-arlt",[5],"Wann gründete Ilse Arlt die Vereinigten Fachkurse für Volkspflege?","1912",["1899","1917","1921"],"Erste österreichische Ausbildungseinrichtung für soziale Arbeit.")
MC("ber-arlt",[5],"Was war das Ziel von Arlts Schule?","Neues weibliches Berufsfeld und Professionalisierung der Fürsorge",["Abschaffung der freien Liebestätigkeit","Ausbildung von Beamten für das Ministerium","Vorbereitung von Frauen auf die Ehe"],"Sie wollte die freie Liebestätigkeit nicht verdrängen, sondern stützen.")
TF("ber-arlt",[5],"Arlt wollte die Ausbildung für unbesoldete Hilfstätigkeit einfacher halten als für bezahlte Berufsarbeit.",False,"Sie machte keinen Unterschied, denn unbesoldete Arbeit soll genauso gründlich getan werden.",[("eb",12)])
MC("ber-arlt",[5],"Wie waren die Aufnahmekriterien an Arlts Schule?","Offen: 17 bis 35 Jahre, unterschiedliche Vorbildung",["Nur Maturantinnen ab 21 Jahren","Nur Kinderlose mit zwei Jahren Praxis","Nur Frauen mit Kindergartenprüfung"],"Es sollten möglichst viele Frauen gewonnen werden, die Persönlichkeit war wesentlich.",[("eb",13)])
MULTI("ber-arlt",[5],"Welche Inhalte gehörten zu Arlts Lehrplan?",["Gesundheitsfürsorgerische Inhalte","Psychologische Inhalte","Volkswirtschaftslehre"],["Rassenkunde","Kirchenrecht als Hauptfach"],"Ein umfassender und vielseitiger Lehrplan, auch mit Gastlehrenden von der Universität.",[("eb",14)])
MC("ber-arlt",[5],"Welches Vorbild nennt die Folie für Arlts Schule?","Alice Salomons Soziale Frauenschule",["Jane Addams’ Hull House","Tandlers Wohlfahrtsamt","Ellen Keys Reformschule"],"Für die Methode beziehen sich die Folien außerdem auf Mary Richmond.",[("eb",2),("eb",11)])
MATCH("ber-arlt",[],"Welches Werk erschien wann?",[("1921","Die Grundlagen der Fürsorge"),("1923","Die Gestaltung der Hilfe"),("1958","Wege zu einer Fürsorgewissenschaft")],"Arlts Überzeugung: Soziale Arbeit als Wissenschaft und Praxis.",[("eb",17)])
MC("ber-beduerf",[6],"Wie viele Bedürfnisklassen unterscheidet Ilse Arlt?","Dreizehn",["Sieben","Sechsundzwanzig","Drei"],"Sie reichen von Luft, Licht und Wärme bis zur Geistespflege.")
MULTI("ber-beduerf",[6],"Welche gehören zu Arlts Bedürfnisklassen?",["Luft, Licht, Wärme","Rechtsschutz","Erholung","Familienleben"],["Besitz und Vermögen"],"Allen Menschen gemeinsam, aber variierend je nach Alter, Schicht, Religion und Behinderung.",[("eb",18)])
MC("ber-beduerf",[6],"Wann muss Fürsorge laut Arlt einschreiten?","Bei Spannung zwischen einfachster ausreichender Befriedigung und Unterbefriedigung",["Erst bei offensichtlicher, akuter Notlage","Wenn eine Behörde sie ausdrücklich anfordert","Wenn die betroffene Person arbeitslos gemeldet ist"],"Hilfe soll als Prophylaxe wirken, nicht erst im Notfall.",[("eb",20)])
TF("ber-beduerf",[6],"Arlts Kenntnis der Bedürfnisse sollte die Annahme stützen, dass Armut selbstverschuldet ist.",False,"Sie sollte solche Annahmen und das Vorurteil einer homogenen Gruppe von Armen widerlegen.",[("eb",18)])
MC("ber-wk",[],"Was entstand 1916 auf staatlicher Ebene?","Ein Ministerium für soziale Fürsorge",["Die Akademie für soziale Verwaltung","Das Rote Wien","Die Generalvormundschaft"],"Die Jugendfürsorge bekam im selben Jahr auch ein eigenes Referat der Gemeinde Wien.")
MC("ber-wk",[22],"Was bekamen bedürftige Mütter im Ersten Weltkrieg über den Verbindungsdienst?","Beihilfen in Geld, Lebensmitteln und Säuglingswäsche",["Eine bezahlte Ausbildung als Pflegerin","Das Recht auf Obsorge über ihr Kind","Einen freien Platz im Gemeindebau"],"Die Wäsche nähten Arbeitslose in einer Nähstube.",[("eb",24)])
TF("ber-wk",[],"NEU im Ersten Weltkrieg war die Konzentration auf Fälle „erzieherischer Gefährdung“.",True,"Begründet wurde das mit der außerhäuslichen Berufsarbeit der Mütter.",[("eb",22)])
MC("ber-ehe",[23],"Was verlangte der Gemeinderatsbeschluss vom 27.4.1917?","Ehe- und Kinderlosigkeit für das Fürsorgerinnenamt",["Matura für alle Pflegerinnen","Männliche Vormünder für jedes Kind","Unbezahlte Probezeit von zwei Jahren"],"1919 wurde die Regel aufgehoben, wegen verstärkter Nachfrage nach weiblichem Personal.")
TF("ber-ehe",[23],"Die Ehe- und Kinderlosigkeit galt für Fürsorgerinnen über mehrere Jahrzehnte.",False,"Sie galt von 1917 bis 1919.")
MC("ber-ja",[24],"Welchen Berufstitel führten die Absolventinnen der städtischen Fachkurse von 1917?","Fürsorgerin",["Sozialarbeiterin","Wohlfahrtspflegerin","Volkspflegerin"],"Die Fachkurse dauerten 2 Jahre, 1918 wurden sie in eine Akademie für soziale Verwaltung umgewandelt.",[("eb",27)])
TF("ber-ja",[24],"Die Akademie für soziale Verwaltung setzte ab 1919 einen Schulabschluss mit Matura voraus.",True,"Ganz im Unterschied zu vorher.",[("eb",27)])
ORD("ber-ja",[24,5],"Von den ersten Kursen zum Jugendamt: Was kam wann?",[("1912","Arlts Vereinigte Fachkurse"),("1913","10 Stellen für Berufspflegerinnen"),("1917","Gründung des Wiener Jugendamtes"),("1918","Akademie für soziale Verwaltung")],"In wenigen Jahren wird aus dem Ehrenamt ein Beruf.",[("eb",11),("eb",5),("z",1)])

# ---------------------------------------------------------------- Rotes Wien

T("rot-kontext","rot","Das Rote Wien",
  "Nach dem Wahlsieg 1919 war Wien die einzige Millionenstadt unter rein sozialdemokratischer Verwaltung und wurde bald ein eigenes Bundesland. Nach dem Krieg herrschten Hunger, Inflation und Wohnungsnot. Die Breitner-Steuern finanzierten Wohnbau und Fürsorge.",
  [("rw",2),("rw",3),("rw",6)])
T("rot-anrecht","rot","Anrecht statt Almosen",
  "Das Wohlfahrtsamt von Julius Tandler verband alle Einrichtungen zu einem engen Netz. Das allgemeine Anrecht auf Fürsorge war ein zentraler Wendepunkt: weg von individueller Wohltat, hin zur kollektiven Hilfeleistung. Die Kinder haben Anrecht, die Gesellschaft ist ihr Sachwalter.",
  [("rw",8),("rw",9)])
T("rot-eugenik","rot","Fürsorge und Eugenik",
  "Tandlers Konzeption war bevölkerungspolitisch geleitet. „Positive“ Eugenik sollte die Geburten heben und die Säuglingssterblichkeit senken. Beratungsstellen verbreiteten eugenisches Gedankengut, „unproduktive“ Ausgaben für Alte und Kranke sollten gering bleiben.",
  [("rw",10),("rw",11)])
T("rot-erfassen","rot","Erfassen und Erheben",
  "Die Fürsorgerin war Beauftragte der Gesellschaft. Über Verbindungsdienst, Wäschepaket, Schulfürsorge und Hausbesuch kam sie an alle Familien heran. Hilfe verband sich mit Kontrolle, Maßstab war die normierte kleinbürgerliche Familie.",
  [("rw",13),("rw",14),("rw",15),("rw",16)])
T("rot-jugendamt","rot","Generalvormundschaft",
  "Die Gemeinde Wien übernahm die Vormundschaft über alle ledig geborenen Kinder, die „Mündel“. Mütter konnten die rechtliche Obsorge nicht übernehmen, das galt noch bis 1989. Das Jugendamt registrierte, überwachte, beriet und leitete familienersetzende Maßnahmen ein.",
  [("rw",12)])
T("rot-verw","rot","Kampfbegriff „Verwahrlosung“",
  "„Verwahrlosung“ diente als Sammelbegriff für alle festgestellten „Mängel“ und legitimierte das Eingreifen. Auch uneheliche Kinder und Kinder von Alleinerziehenden galten als gefährdet. Viele Arbeiterfamilien konnten die bürgerlichen Ideale aus sozialen Gründen gar nicht erfüllen.",
  [("rw",17)])
T("rot-aichhorn","rot","August Aichhorn",
  "Der Pädagoge und Psychoanalytiker sah Verwahrlosung als individuelle Reaktion auf Erfahrungen, nicht als Erbe oder Charakterschwäche. In Oberhollabrunn schaffte er die Prügelstrafe ab und setzte das Gespräch an die Stelle von Strafen. Als Erziehungsberater verstand er sich als „verständnisvoller Verbündeter“.",
  [("rw",18),("rw",20),("rw",23),("rw",38)])
T("rot-kinderstube","rot","Erziehungsberatung und Kinderstube",
  "Erziehungsberatung begann 1919 und wurde 1926 ausgebaut. Die Kinderstube von 1926 ergänzte sie mit Spiel und Lernhilfe. Im Team gab es erstmals Fallbesprechungen, was das spätere Case Work vorwegnimmt.",
  [("rw",18),("rw",21),("rw",24)])
T("rot-dwor","rot","Rosa Dworschak",
  "Die Absolventin von Arlts Fachkursen arbeitete als Sprengelfürsorgerin und ab 1923 mit Aichhorn in der Erziehungsberatung. Ihre „Dorfgeschichten aus der Großstadt“ erzählen vom Barackenlager in Ottakring. 1949 baute sie das Institut für Erziehungshilfe auf und wurde entscheidende Vermittlerin des Case Work.",
  [("rw",25),("rw",27),("rw",28)])
T("rot-heime","rot","Heime statt Anstalten",
  "Als zentrale Leistung gilt die Umgestaltung der Fremdunterbringung: mehr Licht, mehr Platz, Unterscheidung nach heilpädagogischen Gesichtspunkten. Tandlers Motto lautete „Wer Kindern Paläste baut, reißt Kerkermauern nieder!“. Trotzdem blieb der Mangel an Plätzen groß.",
  [("rw",19),("rw",30),("rw",31)])
T("rot-kuest","rot","Die KÜST",
  "Die Kinderübernahmestelle von 1925 war das „Juwel der modernen Kinderfürsorge“ und Drehscheibe für abgenommene Kinder. Nach einigen Wochen Beobachtung und Tests wurde über Pflegefamilie oder Heim entschieden. Die Folie nennt sie eine „panoptische Anlage“, das Kind wurde zum Objekt.",
  [("rw",33),("rw",34),("rw",35)])
T("rot-neu","rot","Was vom Roten Wien bleibt",
  "Die letzte Folie listet die Neuerungen für die Praxis auf: Heimbauten, Jugendfürsorge bis 18, Familienfürsorge, Zusammenarbeit der Stellen, Vereinheitlichung im Jugendamt, Ziehkindergesetz und mehr Berufsfürsorgerinnen. Einiges davon wirkte über Jahrzehnte.",
  [("rw",40)])

MC("rot-kontext",[10],"Womit finanzierte das Rote Wien Wohnbau und Fürsorge?","Mit den „Breitner-Steuern“ auf Besitz, Verkehr und Boden",["Mit einer Kopfsteuer auf alle Arbeiter","Mit Krediten der Habsburger","Mit Zöllen auf Lebensmittel"],"Luxussteuern, also Verteilung von oben nach unten. Hugo Breitner war Finanzstadtrat.",[("rw",6)])
MC("rot-kontext",[],"Wie viele kommunale Wohnungen brachten die drei Wohnbauprogramme von 1923–1927 ungefähr?","Etwa 60.000",["Etwa 6.000","Etwa 600.000","Etwa 250"],"Sie hatten eigenen Wasseranschluss und Toiletten, deckten den Bedarf aber nicht.",[("rw",7)])
TF("rot-kontext",[10],"Wien war ab 1919 die einzige Millionenstadt unter rein sozialdemokratischer Verwaltung.",True,"Nach den ersten allgemeinen Wahlen am 4.5.1919.",[("rw",2)])
MC("rot-kontext",[],"Worauf zielte die Sozialpolitik im Wohnbau familienpolitisch ab?","Die normative Arbeiter-Kleinfamilie nach kleinbürgerlichem Vorbild",["Die Großfamilie nach bäuerlichem Vorbild","Die Auflösung der Familie zugunsten von Kollektiven","Das Einzelwohnen junger Erwachsener"],"Wohnungswesen und Fürsorge hingen eng zusammen.",[("rw",6)])
MC("rot-anrecht",[10],"Was war der zentrale Wendepunkt des Roten Wien im fürsorgerischen Selbstverständnis?","Die Formulierung eines allgemeinen Anrechts auf Fürsorge",["Die Einführung des Heimatrechts","Die Rückkehr zum Ehrenamt","Der Ausschluss der Unehelichen"],"Abkehr von individualistischer Wohltat zum kollektiven Hilfeanspruch.")
MC("rot-anrecht",[10],"Wie lautet Tandlers Grundsatz der Jugendfürsorge?","„Die Kinder haben ein Anrecht auf Fürsorge und die Gesellschaft ist ihr Sachwalter.“",["„Wer nicht arbeitet, soll auch nicht essen.“","„Jedes Kind gehört der Familie allein.“","„Die Armen tragen selbst die Schuld.“"],"Der Satz markiert den kollektiven Hilfeanspruch.")
TF("rot-anrecht",[10,9],"Die sozialdemokratische Wohlfahrt setzte die ehrenamtliche Wohltätigkeit bewusst fort.",False,"Sie grenzte sich deutlich davon ab und verstand sich als „kollektivistische Hilfeleistung“.",[("rw",9)])
MC("rot-anrecht",[],"Was bedeutet die Errichtung von Fürsorgesprengeln?","Dezentralisierung des Jugendamtes durch Einteilung in Bezirke",["Einsparung aller Hausbesuche","Privatisierung der Kindergärten","Verlegung von Heimen aufs Land"],"Teil von Tandlers straffer Organisation und engmaschigem Netz.",[("rw",8)])
MC("rot-eugenik",[12],"Was meint „positive Eugenik“ bei Tandler?","Qualitative Bevölkerungspolitik zur Hebung der Geburten und besseren „Aufzucht“",["Verbot jeder Heirat durch den Staat","Völlige Trennung von Fürsorge und Medizin","Förderung der Alten vor den Kindern"],"Geburtenfördernd, gegen Säuglingssterblichkeit. Die Familie gilt als „Keimzelle aller sozialen Organisation“.")
MC("rot-eugenik",[12],"Wem wurde in den Beratungsstellen nahegelegt, auf Kinder zu verzichten?","Personen mit erblichen, psychiatrischen oder Suchterkrankungen",["Allen Arbeiterfrauen unter 25 Jahren","Allen Unverheirateten","Allen Personen ohne Heimatrecht"],"Stichwort „vernünftige Zuchtwahl“, vgl. den Film „Hygiene der Ehe“.",[("rw",11)])
MC("rot-eugenik",[12],"Welche Ausgaben galten als „bevölkerungspolitisch unproduktiv“?","Leistungen für „Gebrechliche, Alte und Irre“",["Leistungen für Kindergärten und Horte","Ausgaben für die Jugendfürsorge","Ausgaben für die Säuglingsfürsorge"],"Sie sollten möglichst gering gehalten werden, um nicht auf Kosten der „produktiven“ zu gehen.",[("rw",11)])
TF("rot-eugenik",[12],"Eugenik spielte in der Fürsorge des Roten Wien keine Rolle, sie kam erst mit dem NS-Regime.",False,"Tandlers Konzept war maßgeblich bevölkerungspolitisch geleitet. Das Thema ist auch deshalb Prüfungsstoff.",[("rw",10)])
MC("rot-erfassen",[12,22],"Was geschah mit dem Säuglingswäschepaket von 1927?","Alle Mütter bekamen es unentgeltlich beim Hausbesuch",["Nur bedürftige Mütter konnten es kaufen","Es wurde an Schulen an Väter ausgeteilt","Es war eine Prämie für die Eheschließung"],"Unabhängig von der Bedürftigkeit. So kam die Fürsorgerin zugleich in jede Wohnung.",[("rw",14)])
MULTI("rot-erfassen",[12,22],"Mit welchen Instrumenten wurde Bedürftigkeit „erfasst“?",["Verbindungsdienst in Geburtsabteilungen","Säuglingswäschepaket","Obligatorische Schulfürsorge","Hausbesuch"],["Freiwillige Online-Beratung"],"Vier Wege zu den Familien, die jeweils Hilfe und Kontrolle verbanden.",[("rw",14)])
MC("rot-erfassen",[12],"Was überprüfte die Fürsorgerin beim Hausbesuch vor allem?","Sauberkeit, Ordnung und Hygiene",["Einkommen und Parteizugehörigkeit","Schulnoten und Religion","Mietvertrag und Heimatrecht"],"Bis hin zum „distanzlosen Öffnen der Kästen“, laut Folie jahrzehntelang gängige Praxis.",[("rw",14),("rw",16)])
MATCH("rot-erfassen",[10],"Was bedeutet was im Amt des Roten Wien?",[("Hilfsfürsorgerin","stammt aus dem Arbeitermilieu, schlechter gestellt"),("Kinder-Evidenzkataster","fasst alle betreuten Kinder einheitlich zusammen"),("Nachschau","zentrale Kontrollaufgabe der Fürsorgerin")],"Der Einsatz von Hilfsfürsorgerinnen ab 1926 sollte den schwierigen Kontakt zu Müttern erleichtern.",[("rw",15),("rw",16)])
TF("rot-erfassen",[12],"Hausbesuche dienten im Roten Wien auch der Disziplinierung der Mütter.",True,"Bis zur Androhung, ihre Kinder wegzunehmen.",[("rw",16)])
MC("rot-jugendamt",[8],"Was übernahm die Gemeinde Wien mit der Generalvormundschaft?","Die Vormundschaft über alle in Wien ledig geborenen Kinder",["Das Vermögen aller Waisenkinder","Die Aufsicht über alle Volksschulen","Die Pflege aller Kranken"],"Ausnahme waren männliche Verwandte. Mütter konnten die rechtliche Obsorge nicht übernehmen.")
MC("rot-jugendamt",[],"Bis wann konnten Mütter unehelicher Kinder laut Folie keine rechtliche Obsorge übernehmen?","1989",["1934","1954","2000"],"Die Folie setzt „SIC!“ dazu. 1954 kam zwar eine erste Lockerung, die generelle Übertragung erst 1989.",[("rw",12),("n",27),("zs",9)])
TF("rot-jugendamt",[],"Uneheliche Kinder standen bis zur Volljährigkeit mit 21 Jahren unter der Vormundschaft der Gemeinde Wien.",True,"Die allgemeine Zuständigkeit des Jugendamts reichte bis 18.",[("rw",12)])
MC("rot-verw",[12],"Wen stufte man im Roten Wien als „verwahrlosungsgefährdet“ ein?","Uneheliche Kinder oder Kinder, die nur mit der Mutter aufwuchsen",["Kinder, deren Eltern im Gemeindebau wohnten","Kinder, die einen Kindergarten besuchten","Kinder von Fürsorgerinnen"],"Maßstab war das Vater-Mutter-Kind-Familienmodell.")
TF("rot-verw",[12],"Der Begriff „Verwahrlosung“ war eng und klar definiert.",False,"Er war weit gefasst, ein Kampfbegriff für alle festgestellten „Mängel“ und zur Legitimation des Eingreifens.")
MC("rot-aichhorn",[13],"Wie sah Aichhorn „Verwahrlosung“?","Als individuelle Reaktion auf soziale und psychische Erfahrungen",["Als vererbte Eigenschaft","Als Charakterschwäche","Als Folge fehlender Religion"],"Der Verwahrloste ist nicht Störenfried, sondern „hilfsbedürftige Person“.",[("rw",18)])
MC("rot-aichhorn",[13],"Was änderte Aichhorn in Oberhollabrunn?","Prügelstrafe abgeschafft, keine verschlossenen Türen",["Einführung von Drill und Zucht","Reine Beschäftigung in der Fabrik","Verlegung aller Kinder in Pflegefamilien"],"Bruch mit den Methoden von Straferziehungsanstalten. 1921 wurde es aus Kostengründen aufgelöst.",[("rw",38)])
MC("rot-aichhorn",[13],"Als was verstand Aichhorn die Rolle des Erziehungsberaters?","„Verständnisvoller Verbündeter“ der Verwahrlosten",["Strenger Vertreter der Behörde","Beobachter ohne jeden Kontakt","Polizeilicher Ermittler"],"Hinter dem Konzept stehen Psychoanalyse und das Ziel, Familien zu unterstützen.",[("rw",23)])
MC("rot-aichhorn",[13],"Auf welcher theoretischen Grundlage arbeitete Aichhorn?","Psychoanalyse",["Rassenhygiene","Katholische Soziallehre","Betriebswirtschaft"],"Er machte Psychoanalyse bei Sigmund Freud und vermittelte sie auch Fürsorgerinnen.",[("rw",20),("rw",22)])
TF("rot-aichhorn",[13],"Oberhollabrunn wurde Vorbild für die Umgestaltung der Anstalten Eggenburg und Weinzierl.",True,"Besserungsanstalten wurden zu Erziehungsfürsorgeanstalten.",[("rw",39)])
MC("rot-aichhorn",[13],"Was gilt als Zitat Aichhorns zur Anstaltserziehung?","„Das dissoziale Kind braucht ein Milieu, das ihm Bewegungsfreiheit gibt.“",["„Ein verwahrlostes Kind ist ein Krankheitsherd.“","„Es soll nur der befürsorgt werden, welcher der Fürsorge bedarf.“","„Überleben kann nur, wer arbeitet.“"],"Aus „Über die Erziehung in Besserungsanstalten“ von 1923.",[("rw",37)])
MC("rot-kinderstube",[13,26],"Was nimmt die Kinderstube von 1926 laut Folie vorweg?","Case Work",["Das Säuglingswäschepaket","Den Verbindungsdienst","Die Heimkommission"],"Dort gab es erstmals Fallbesprechungen im Team.",[("rw",24)])
TF("rot-kinderstube",[],"Die Erziehungsberatung im Wiener Jugendamt begann 1919 mit Franz Winkelmayer.",True,"Dessen spätere Rolle zeigt die Brüche: 1943 leitete er kommissarisch das Erziehungsheim Am Spiegelgrund.",[("rw",18),("z",2)])
MC("rot-dwor",[26],"Welche Rolle spielte Rosa Dworschak für das Case Work?","Entscheidende Vermittlerin unter ihren Kolleginnen",["Gründerin des Elberfelder Systems","Erfinderin der KÜST-Intelligenztests","Autorin von „Social Diagnosis“"],"Sie stand in der Tradition Aichhorns, zu einem Zeitpunkt, als die Methode noch nicht etabliert war.",[("rw",28)])
MC("rot-dwor",[],"Wo erwarb Rosa Dworschak ihre Fürsorgeausbildung?","Bei Ilse Arlts Vereinigten Fachkursen",["An Salomons Akademie in Berlin","Bei Mary Richmond in Baltimore","An der Akademie für Sozialarbeit"],"Abschluss 1918, danach Anstellung im Wiener Jugendamt.",[("rw",25)])
TF("rot-dwor",[],"Der historische Name des Barackenlagers in Ottakring ist laut Folie Ausdruck rassistisch-eugenischer Ideologie.",True,"Die Folie kürzt ihn deshalb ab und nennt ihn problematisch. Das Lager wurde 1952 abgerissen.",[("rw",25),("rw",26)])
MC("rot-heime",[11],"Was gilt als zentrale Leistung des Roten Wien in der Fremdunterbringung?","Schrittweise Umgestaltung von Anstalten zu Heimen",["Völlige Abschaffung der Kindesabnahme","Unterbringung aller Kinder bei Verwandten","Schließung aller Pflegefamilien"],"Bisher wurden abgenommene Kinder primär in Anstalten verwahrt.",[("rw",30)])
MC("rot-heime",[11],"Wo stand „Wer Kindern Paläste baut, reißt Kerkermauern nieder!“?","Beim Eingang der Kinderübernahmestelle",["Auf dem Rathaus","Am Karl-Marx-Hof","Im Jugendamt Ottakring"],"Das ist Tandlers Motto, am Eingang der KÜST.",[("rw",30)])
MC("rot-kuest",[11],"Wofür diente die KÜST als „Drehscheibe“?","Abklärung über die weitere Unterbringung in Pflegefamilie oder Heim",["Vermittlung von Lehrstellen für Jugendliche","Aufnahme von Müttern zur Entbindung","Ausbildung von Hilfsfürsorgerinnen"],"Basis waren psychologische Testungen. Das überstellte Kind wurde Objekt der Beobachtung.")
TF("rot-kuest",[11],"Die Begutachtung auf Basis der KÜST-Tests blieb jahrzehntelang üblich.",True,"Die Folie vermerkt eine jahrzehntelange Begutachtung, etwa mit Kleinkindertests von Bühler und Hetzer.",[("rw",34)])
MC("rot-kuest",[],"Wie beschreibt eine ehemalige Verbindungsfürsorgerin den Aufenthalt in der KÜST?","Körperlich gut behandelt, aber wie „in einer Glasbox“",["Hart, doch sehr kindgerecht","Liebevoll, aber gesundheitlich gefährlich","Völlig frei von jeder Beobachtung"],"Das Zitat zeigt die Spannung: Die Betreuung konzentrierte sich primär auf das gesundheitliche Wohl.",[("rw",35)])
MC("rot-kuest",[11],"Welche Funktion hatte das Kinderheim Schloss Wilhelminenberg ab 1927?","Heilpädagogische Beobachtungsstelle für „auffällige“ Kinder",["Ausbildungsstätte für Fürsorgerinnen","Sitz der Wiener Sängerknaben","Mutter-Kind-Heim für 25 Mütter"],"Klassifizierung mit defizitorientierten Testverfahren. Erst 1934 kam es an die Sängerknaben.",[("rw",36),("t",2)])
MULTI("rot-neu",[11],"Was nennt die Folie als relevante Neuerungen des Roten Wien?",["Erweiterung der Jugendfürsorge bis zum 18. Lebensjahr","Vereinheitlichung im städtischen Jugendamt","Ziehkindergesetz","Mehr Berufsfürsorgerinnenposten"],["Abschaffung des Hausbesuchs"],"Dazu kommen bauliche Tätigkeit, Verankerung in der Familienfürsorge und Zusammenarbeit öffentlicher und privater Stellen.")
MATCH("rot-aichhorn",[11],"Wer steht wofür im Roten Wien?",[("Julius Tandler","Wohlfahrtsamt, Stadtrat"),("Hugo Breitner","Steuern, Finanzstadtrat"),("August Aichhorn","Erziehungsberatung, Oberhollabrunn"),("Rosa Dworschak","Sprengelfürsorge, Case Work")],"Vier Namen, die in einer Überblicksfrage zum Roten Wien vorkommen können.",[("rw",6),("rw",8),("rw",20),("rw",28)])
ORD("rot-kuest",[11],"Reihe die Eckdaten des Roten Wien.",[("1919","Beginn der Erziehungsberatung"),("1921","Wohlfahrtsamt"),("1925","Eröffnung der KÜST"),("1927","Säuglingswäschepaket")],"Vom Beginn der Beratung bis zum Paket für alle Mütter.",[("z",2),("rw",8),("rw",14)])

# ---------------------------------------------------------------- Austrofaschismus

T("aut-grund","aut","Fürsorge im Ständestaat",
  "Ab 1934 gab es keine strukturellen Neuerungen und keinen weiteren Ausbau. Stattdessen flossen mehr Mittel an konfessionelle Einrichtungen, öffentliche wurden privatisiert. Grundlage war die katholische Soziallehre, das allgemeine Anrecht auf Fürsorge wurde zurückgenommen.",
  [("t",2),("t",5)])
T("aut-familie","aut","Einheit der Familie",
  "Der Familienschutz stand im Zentrum. Eugenische Prinzipien des Roten Wien wurden mit sittlich-katholischen Werten verknüpft. Wohnungen in den Familienasylen gab es nur für „geordnete Familien“ mit mehreren Kindern.",
  [("t",7),("t",8)])
T("aut-not","aut","Not im Parteienverkehr",
  "Die Not stieg, die Fürsorgerinnen hatten aber zu wenig Mittel. Das Fürsorgebuch sollte Verwaltungskosten sparen und Klient*innen überprüfbar machen. Eine Fürsorgerin erinnert sich an 20 oder 30 Brotmarken für 50 bis 70 Wartende.",
  [("t",9),("t",10)])
T("aut-erz","aut","Religiöse Erziehung",
  "Fürsorgerinnen überwachten neben Sauberkeit und Hygiene auch die „sittlich-religiöse Erziehung“. Kinder kamen in katholische Privatanstalten, und der Begriff „Anstalt“ kehrte zurück. Das Verbot der Sozialdemokratie führte zu politisch motivierten Personalveränderungen.",
  [("t",11)])

MC("aut-grund",[14,9],"Was geschah mit dem Anrecht auf Fürsorge im Austrofaschismus?","Es wurde zurückgenommen, zugunsten der „alten Wohltäterei“",["Es wurde gesetzlich auf alle ausgeweitet","Es wurde erstmals formuliert","Es galt nur noch für die Sozialdemokratie"],"Der Begriff „alte Wohltäterei“ stammt von Tandler. Grundlage war die katholische Soziallehre.")
MC("aut-grund",[14],"Was passierte mit dem Kinderheim Schloss Wilhelminenberg 1934?","Es wurde aufgelassen und den Sängerknaben übergeben",["Es wurde zum Gaujugendamt umgebaut","Es wurde vergrößert und saniert","Es wurde zur Ausbildungsstätte"],"Ein Beispiel für die Privatisierung öffentlicher Einrichtungen. Die Arbeiterzeitung schrieb: „Statt armer Kinder eine klerikale Institution!“",[("t",2),("t",4)])
TF("aut-grund",[14],"Der Ständestaat baute die Fürsorgeangebote strukturell massiv aus.",False,"Keine strukturell-organisatorischen Neuerungen und kein weiterer Ausbau.",[("t",2)])
MC("aut-grund",[14],"Was war die Vaterländische Front?","Monopolorganisation, die als Einheitspartei fungierte",["Ein Verein für Kinderschutz","Der Berufsverband der Fürsorgerinnen","Eine Abteilung des Jugendamtes"],"Gegründet im Mai 1933 unter Dollfuß, nach Ausschaltung von Parlament und Opposition als Einheitspartei.",[("t",6)])
MC("aut-familie",[14],"Wer bekam eine Wohnung in den Familienasylen von 1934?","Nur „geordnete Familien“ mit zwei oder mehr Kindern",["Alle Obdachlosen ohne Heimatrecht","Ledige Mütter mit Säuglingen","Mitglieder der Sozialdemokratie"],"Dazu Einsatz von Fürsorgerinnen, Arzt und Seelsorger zur „Erziehung zur gesunden Familie“.")
TF("aut-familie",[14,12],"Die Bevölkerungspolitik des Roten Wien wurde im Austrofaschismus mit sittlich-katholischen Werten verknüpft.",True,"Christliche Familie gleich „erbgesunde Familie“ steht auf der Folie.",[("t",7)])
MC("aut-familie",[14],"Wo wurden Fürsorgerinnen im Austrofaschismus ausgebildet?","An der katholischen „Pichlschule“",["An der Sozialen Frauenschule der Stadt Wien","An Arlts Sozialakademie","An der Lehranstalt für gehobene Sozialberufe"],"Inhalte: religiöse, pronatalistische Themen, Gesundheitsfürsorge, Mutterschutz und Wochenbettpflege.",[("t",8)])
MC("aut-not",[14],"Wozu diente das Fürsorgebuch?","Einsparung von Verwaltungskosten und Überprüfbarkeit der Klient*innen",["Vermerk von Schulnoten der Kinder","Abrechnung der Breitner-Steuern","Nachweis der Parteimitgliedschaft"],"Unterstützung gab es vor allem für kinderreiche Familien.")
TF("aut-erz",[14],"Für die Übernahme eines Pflegekindes war ein katholisches Religionsbekenntnis Voraussetzung.",True,"Die Fremdunterbringung erfolgte zudem in katholischen Privatanstalten.")
MC("aut-erz",[14],"Welcher Begriff kehrte im Austrofaschismus zurück?","„Anstalt“ anstelle von „Heim“",["„Heim“ anstelle von „Anstalt“","„Klient“ anstelle von „Partei“","„Sozialarbeiterin“ anstelle von „Fürsorgerin“"],"Das ist ein sprachlicher Rückschritt gegenüber dem Roten Wien.")

# ---------------------------------------------------------------- Nationalsozialismus (ohne Spieleffekte)

T("ns-system","ns","Struktur und Ideologie",
  "Einrichtungen liefen strukturell weiter, das Wiener Jugendamt wurde zum „Gaujugendamt Niederdonau“. Entscheidend war die ideologische Umkehr: Nicht mehr der Dienst an Hilfsbedürftigen, sondern am Staat stand im Zentrum. Personen außerhalb der „Volksgemeinschaft“ waren Zwangsmaßnahmen ausgesetzt.",
  [("t",12),("t",13)])
T("ns-ausschluss","ns","Ausschluss und Liquidierung",
  "Juden und Jüdinnen wurden aus der Wohlfahrt ausgeschlossen, die Berufsvormundschaft wurde eingeschränkt. Private Einrichtungen wurden aufgelöst oder eingegliedert, Ausbildungsstätten sofort geschlossen. Polizei und Gestapo arbeiteten eng mit der Fürsorge zusammen.",
  [("t",14),("t",15)])
T("ns-asozial","ns","Von „Verwahrlosung“ zu „Asozialität“",
  "„Verwahrlosung“ wurde zu „Asozialität“ umgedeutet, also „gemeinschaftswidrigem Verhalten“. Disziplin und Ordnung ersetzten die pädagogischen Konzepte des Roten Wien. An die Stelle der Erziehung trat der Ausschluss, in letzter Konsequenz mit tödlichen Folgen.",
  [("t",18),("t",19),("t",22)])
T("ns-spalt","ns","Gespaltene Fürsorge",
  "Für die „erbgesunde“, „arische“ Familie gab es umfassende Hilfe und eigene Budgets, etwa für kinderreiche Familien. Für alle anderen wirkte die Fürsorge an „Selektion und Auslese“ mit. Die Nürnberger Rassengesetze bildeten dafür die rechtliche Basis.",
  [("t",32),("t",33),("t",34)])
T("ns-erfassen","ns","Totales Erfassen",
  "Hausbesuch, Verbindungsdienst und Schulfürsorge dienten nun auch der Erhebung von Erbkrankheiten. Die Erbkartei wuchs rasant. Der Kontakt mit der Fürsorge konnte für viele gefährlicher sein, als er half.",
  [("t",35),("t",36)])
T("ns-personal","ns","Personal, Angst, Anpassung",
  "Jüdische und politisch opponierende Beamt*innen wurden entfernt, alle anderen schworen am 16. März 1938 den Diensteid. Politische Schulungen, Denunziationsgefahr und Sanktionen prägten das Klima. Die Ausbildung vermittelte durch SS-Ärzte Erb- und Rassenpflege, auf geringerem Niveau.",
  [("t",24),("t",26),("t",27),("t",29),("t",30)])
T("ns-spiel","ns","Handlungsspielräume",
  "Nicht alle Fürsorgerinnen gingen mit dem Auftrag konform. Manche sabotierten bei den „Sippenbögen“ durch nur äußere Anpassung, andere nutzten die Situation aus Opportunismus für ihre Karriere. Ob passiver Widerstand ausgeübt wurde, war unterschiedlich.",
  [("t",28),("t",36),("t",37)])
T("ns-spiegel","ns","Am Spiegelgrund",
  "Die Kinderfachabteilung der Anstalt Am Steinhof wurde zum Ort der Vernichtung. 789 Todesopfer sind dokumentiert, die meisten in der Säuglingsabteilung. Die Jugendfürsorge, die Kinderübernahmsstelle und der Spiegelgrund waren organisatorisch eng verbunden.",
  [("t",38),("t",39),("t",40)])
T("ns-krieg","ns","Kriegsjahre",
  "Mit der Dauer des Krieges wurden Fürsorgemittel massiv reduziert und für den Krieg eingesetzt. Fürsorge diente der Stabilisierung der „Heimatfront“. Luftangriffe und Transportprobleme erschwerten den Betrieb, unqualifiziertes Personal ersetzte fehlende Männer in den Heimen.",
  [("t",42),("t",43)])

MC("ns-system",[15],"Was wurde 1938 aus dem Wiener Jugendamt?","Das „Gaujugendamt Niederdonau“",["Die Soziale Frauenschule","Die Nationalsozialistische Volkswohlfahrt","Die Kinderübernahmsstelle"],"Strukturell wurde das System weitergeführt, das Sprengelsystem sogar ausgebaut.")
MC("ns-system",[15],"Was war laut Folie die entscheidende Veränderung im NS-Fürsorgesystem?","Die ideologische Ausrichtung: Dienst am Staat statt an Hilfsbedürftigen",["Der komplette Abbau aller Fürsorgestellen","Die Rückkehr zur katholischen Wohltätigkeit","Die Einführung eines Rechtsanspruchs für alle"],"Bestehende Bestimmungen wurden außer Kraft gesetzt, Zwangsmaßnahmen gegen die als nicht „unterstützungswürdig“ Geltenden verhängt.")
TF("ns-system",[15],"Das NS-Regime führte bestehende Fürsorgeeinrichtungen strukturell weiter.",True,"Der Bruch lag in der Ideologie, nicht in den Strukturen.",[("t",12)])
MC("ns-ausschluss",[16],"Wen schloss die Entscheidung vom 21. August 1938 von der Berufsvormundschaft aus?","Jüdische Kinder und als „Zigeuner“ bezeichnete Kinder",["Alle unehelichen Kinder","Alle Kinder unter sechs Jahren","Alle Kinder ohne Heimatrecht"],"Die Folie zitiert die Formulierung und benennt sie als Rassismus und Antisemitismus.",[("t",14)])
MC("ns-ausschluss",[15],"Was geschah 1938 mit den Ausbildungsstätten für Fürsorgerinnen?","Alle wurden geschlossen, eine neue Soziale Frauenschule entstand",["Sie blieben unverändert in kirchlicher Hand","Sie wurden zu Akademien aufgewertet","Sie wurden an Universitäten angegliedert"],"Die neue Ausbildung diente der Gleichschaltung.",[("t",15),("t",23),("z",2)])
TF("ns-ausschluss",[15],"Fürsorge und Polizei arbeiteten getrennt voneinander.",False,"Eine enge Zusammenarbeit mit Polizei und Gestapo sollte Klient*innen unter die Kontrolle des Regimes zwingen.",[("t",14)])
MC("ns-asozial",[16],"In welchen Begriff wurde „Verwahrlosung“ umgedeutet?","„Asozialität“",["„Sozialanpassung“","„Erziehungsnotstand“","„Schwererziehbarkeit“"],"In der Nachkriegszeit wird dann „Sozialanpassung“ zum neuen Maßstab.",[("t",18),("n",36)])
MC("ns-asozial",[16],"Was ersetzte die pädagogischen Konzepte des Roten Wien?","Disziplin und Ordnung, Heime mit Drill und Zucht",["Psychoanalytische Beratung","Freiwillige Elternschulen","Offene Wohngemeinschaften"],"Heimkinder wurden 1938 zudem zwangsweise in HJ und BDM eingegliedert.",[("t",19)])
TF("ns-asozial",[16],"An die Stelle von Erziehung trat laut Folie der Ausschluss, in letzter Konsequenz mit tödlichen Folgen.",True,"Das ist eine zentrale Aussage zu den Auswirkungen auf Klient*innen.",[("t",22)])
MC("ns-asozial",[22],"Zu wem errichtete das Jugendamt einen Verbindungsdienst zur restlosen Erfassung?","Zu HJ und Nationalsozialistischer Volkswohlfahrt (NSV)",["Zu Kirche und Vaterländischer Front","Zu den Gewerkschaften und der Caritas","Zu Schweizer Pflegefamilien"],"Stichwort Zwangspädagogisierung. Fürsorgerinnen wurde der Beitritt zur NSV nahegelegt.",[("t",22)])
MC("ns-spalt",[16],"Worauf konzentrierte sich die NS-Wohlfahrtspflege auf der helfenden Seite?","Auf die „erbgesunde“, „arische“ Familie als „Urzelle des Volkes“",["Auf alle Armen, unabhängig von Herkunft","Auf Alte und Kranke in Anstalten","Auf Alleinerziehende und ihre Kinder"],"Geburtenförderung und Selektion waren zwei Seiten derselben Politik.",[("t",32)])
TF("ns-spalt",[16],"Für kinderreiche Familien, die als „der Hilfe würdig“ galten, gab es umfassende Unterstützung.",True,"Das meint die „gespaltene Fürsorge“: großzügige Hilfe für die einen, Auslese für die anderen.",[("t",33)])
MC("ns-spalt",[16],"Woran wirkte das Jugendamt beim „Mutterkreuz“ mit?","Auswahl der Mütter über Erhebungen und Empfehlungen",["Herstellung und Verkauf der Auszeichnung","Überweisung einer monatlichen Rente","Ausschluss aller Mütter mit Beruf"],"38.663 kinderreiche Mütter erhielten es 1939 laut Folie.",[("t",34)])
MC("ns-erfassen",[16],"Wozu diente die Übergabe des Säuglingswäschepakets in der NS-Zeit zusätzlich?","Zur Erhebung von Erbkrankheiten",["Zur Spendensammlung für den Krieg","Zur Werbung für die Ausbildung","Zur Verteilung von Lebensmittelmarken"],"Ein Beispiel dafür, wie ein Instrument aus dem Roten Wien umgenutzt wurde.",[("t",35)])
MC("ns-erfassen",[16],"Wie viele Personen erfasste die „Erbkartei“ im April 1940?","406.537",["7.868","38.663","1.235"],"Im April 1939 waren es noch 7.868.",[("t",36)])
MC("ns-personal",[15],"Wozu verpflichtete der Diensteid vom 16. März 1938?","Zu Treue und Gehorsam gegenüber Adolf Hitler",["Zum Austritt aus der Kirche","Zur Mitgliedschaft in der SS","Zum Verzicht auf das Gehalt"],"Ausgenommen waren „jüdische Beamte“, die aus dem Dienst entfernt wurden.",[("t",27)])
MC("ns-personal",[15],"Wer vermittelte Inhalte an der neuen Sozialen Frauenschule?","SS-Ärzte",["Pfarrer","Psychoanalytiker","Vertreterinnen der Frauenbewegung"],"Grundgedanken der Erbgesundheits- und Rassenpflege, bei geringerem Niveau als im Roten Wien.",[("t",24)])
MC("ns-personal",[15],"Welche zwei Funktionen wurden eingeführt und trennten kontrollierende und helfende Kompetenzen?","Organisationsfürsorgerin (ORGA) und Fachfürsorgerin für Erziehungsberatung",["Hauptfürsorgerin und Hilfsfürsorgerin","Berufsvormund und Listenvormund","Waisenmutter und Armenrätin"],"De facto hatte die ORGA deutlich mehr Macht.",[("t",25)])
MULTI("ns-personal",[15],"Welche Sanktionen drohten politisch nicht konformen Mitarbeiter*innen?",["Verbot von Hausbesuchen","Versetzung in weit entfernte Sprengel","Versetzung nach Polen","Strafeinsatz in kriegswichtigen Betrieben"],["Aufstieg zur Amtsleitung"],"Das Klima in den Bezirksjugendämtern war von Angst und Einschüchterung geprägt.",[("t",30)])
MC("ns-spiel",[15],"Wie sabotierten manche Fürsorgerinnen die „erbbiologische Bestandsaufnahme“?","Sie beantworteten Fragen in den Sippenbögen bewusst anders",["Sie verließen geschlossen das Amt","Sie veröffentlichten die Listen im Ausland","Sie verweigerten offen den Diensteid"],"„Man hat sabotiert“: eine nur äußere Anpassung.",[("t",36)])
TF("ns-spiel",[15],"Alle Fürsorgerinnen leisteten im NS-Regime passiven Widerstand.",False,"Das war durchaus unterschiedlich. Die Erinnerungen nennen auch Anpassung, Opportunismus und illegale Nationalsozialist*innen.",[("t",28),("t",37)])
TF("ns-spiegel",[16],"Am Spiegelgrund sind 789 Todesopfer dokumentiert, die überwiegende Mehrheit in der Säuglingsabteilung (Pavillon 15).",True,"Die Kinderfachabteilung wurde laut Folie zum Ort der Vernichtung.",[("t",38)])
MC("ns-spiegel",[16],"Was zeigt die Geschichte von Otto Zipser laut Folie?","Enge Verbindung von Jugendfürsorge, KÜST und Spiegelgrund",["Dass Einweisungen nur auf Elternwunsch erfolgten","Dass die Anstalt von der Fürsorge unabhängig war","Dass nur Kinder unter sechs betroffen waren"],"Einweisung 1940, vermutlich nach Denunziation durch Hausbewohner. Die Folie spricht vom Zuträger des Selektions- und Vernichtungsprogramms.",[("t",39)])
TF("ns-spiegel",[16],"Für viele Überlebende war der Spiegelgrund der Ausgangspunkt für jahrelange weitere Heimunterbringungen.",True,"Mitunter nahmen dort auch lebenslange psychiatrische Martyrien ihren Anfang.",[("t",40)])
MC("ns-krieg",[15],"Wie veränderte der Krieg die Fürsorge?","Massive Reduktion der Mittel, Stabilisierung der „Heimatfront“",["Mehr Mittel für Beratung und Therapie","Ende aller Hausbesuche ab 1939","Rückgabe der Heime an private Träger"],"Neue Aufgaben waren die Betreuung von Umsiedlern, Flüchtlingen und Ausgebombten.")

# ---------------------------------------------------------------- Nachkrieg

T("n-stunde","nach","1945: Stunde Null?",
  "Formal gab es einen Neubeginn: Das Wiener Jugendamt wurde wiederhergestellt, Gesundheitsfürsorge und Jugendwohlfahrt getrennt. Die gesetzliche Grundlage blieb aber bis 1954 die Jugendwohlfahrtsverordnung von 1940. Hunger, Zerstörung und Versorgungskrisen bestimmten den Alltag.",
  [("n",2),("n",4),("z",3)])
T("n-entnazi","nach","„Entnazifizierung“",
  "Viele Bedienstete wurden 1945 außer Dienst gestellt, meist aber nur kurz. Oft wurden nur die Amtsleiter ausgetauscht. Die Generalamnestie von 1947 war der formale Abschluss, etwa 90 Prozent wurden wieder bei der Gemeinde Wien eingestellt.",
  [("n",6),("n",7)])
T("n-ausb","nach","Ausbildung hinkt nach",
  "Die Schulen übernahmen großteils die Inhalte aus der Zeit vor 1938, medizinisch ausgerichtet und praxisfern. Die Rezeption internationaler Methoden war durch den NS unterbrochen, Arlts Arbeiten fanden kaum Beachtung. Ab 1948/49 durften auch Männer die Ausbildung machen, sie blieben aber wenige.",
  [("n",9),("n",10),("n",11),("n",41)])
T("n-alltag","nach","Verwaltung des Mangels",
  "Fürsorgerinnen kämpften gegen Hunger und Krankheit, verteilten Care-Güter und vermittelten Kinder auf Erholung. Bei den Hausbesuchen entschieden sie über Hilfen. Mütter wurden für „Jugendverwahrlosung“ verantwortlich gemacht, obwohl viele Alleinversorgerinnen waren.",
  [("n",14),("n",19),("n",20)])
T("n-kontrolle","nach","Amtskapperl und Mündel",
  "Der in der NS-Zeit verstärkte Kontrollcharakter blieb, die Hausbesuche dienten vielen als Machtdemonstration. Die Überwachung der städtischen Mündel blieb bis in die 1980er Jahre zentral. Fürsorgerinnen blieben für Klient*innen bis Ende der 1960er namenlos, der Umgang war hierarchisch.",
  [("n",21),("n",25),("n",46),("n",48)])
T("n-disz","nach","Sozialanpassung und sittliche Verwahrlosung",
  "Mitte der 1950er Jahre wurde „moralische und sittliche“ Verwahrlosung zum zentralen Thema. „Sozialanpassung“ löste die NS-„Asozialität“ als Maßstab ab. Dazu passte der Kampf gegen „Schmutz und Schund“. Abnahmen wegen „Erziehungsschwierigkeiten“ stiegen stark an.",
  [("n",34),("n",36),("n",38)])
T("n-familie","nach","Familienförderung im Wirtschaftswunder",
  "Mit dem Aufschwung verschob sich der Fokus von materieller Not zu psychosozialen Problemen. Das Jugendwohlfahrtsgesetz von 1954 stärkte erstmals mütterliche Rechte, Elternschulen sollten Familien stützen. Die Politik zielte auf Geburtenförderung, die Rollenbilder blieben traditionell.",
  [("n",26),("n",27),("n",28)])
T("n-puppe","nach","Die Puppenadoption",
  "Ab 1954 bekamen Mädchen in einem Kindergarten im Stadtpark eine Puppe in Pflege, die monatlich in der „Puppenmutterberatungsstelle“ kontrolliert wurde. Die Tradition lief bis 1976. Sie steht beispielhaft für traditionelle Geschlechterrollen, Buben waren nicht beteiligt.",
  [("n",30)])
T("n-casework","nach","Case Work",
  "Über Emigrant*innen aus den USA und die Tradition Aichhorns kam das Case Work in den 1950ern nach Wien. Es sagte dem Kontrollcharakter ab und forderte eine demokratische Grundhaltung gegenüber Klient*innen. Eingeführt wurde es langsam, der Alltag blieb oft „Amtskapperl-Fürsorge“.",
  [("n",44),("n",45),("n",46),("n",47)])
T("n-heim","nach","Heime als totale Institutionen",
  "Heime blieben stark kontrollierend, Erzieher*innen waren oft nicht ausgebildet und teils seit der NS-Zeit im Dienst. Gutachten zeigen das Weiterwirken von NS-Gedankengut. Bis in die 1970er gab es physische, sexuelle und psychische Gewalt.",
  [("n",51),("n",52),("n",53)])
T("n-pflege","nach","Ländliche Pflegefamilien",
  "Leitgedanke war, dass Aufwachsen in einer Familie günstiger ist als im Heim. Wegen des Platzmangels vermittelte man viele Kinder in Großpflegefamilien am Land. Dort wurden Wiener Kinder teils als Arbeitskräfte ausgebeutet und schlecht versorgt.",
  [("n",23),("n",35),("n",53)])

TF("n-stunde",[17],"Nach 1945 wurde sofort ein neues Jugendwohlfahrtsgesetz beschlossen.",False,"Grundlage blieb zunächst die Verordnung von 1940, ein neues Gesetz kam erst 1954.",[("n",2),("n",27)])
MC("n-stunde",[17],"Welche Verwaltungsreform gab es 1945?","Trennung von Gesundheitsfürsorge und Jugendwohlfahrt",["Eingliederung des Jugendamtes in die Polizei","Auflösung aller Fürsorgesprengel","Trennung von Sozialarbeit und Sozialpädagogik"],"Fürsorgesprengel wurden als „kleine Reiche“ der Fürsorgerinnen beschrieben.",[("n",2)])
MC("n-entnazi",[17],"Was war die Generalamnestie von 1947?","Formalrechtlicher Abschluss der „Entnazifizierung“",["Der Beginn der strengen Strafverfolgung","Eine Entschädigung für Opfer der Fürsorge","Das Verbot jeder Beschäftigung früherer Nationalsozialist*innen"],"Etwa 90 Prozent wurden wieder bei der Gemeinde Wien eingestellt.")
MC("n-entnazi",[17],"Wie viele frühere Nationalsozialist*innen wurden nach 1947 wieder eingestellt?","Etwa 90 Prozent",["Etwa 10 Prozent","Etwa 50 Prozent","Niemand"],"In der Regel gab es nur kurzfristige Berufsverbote und einen Austausch der Amtsleiter.",[("n",6)])
TF("n-entnazi",[17],"Die Erzählungen von Fürsorgerinnen nennen amtsinterne Konflikte wegen unterschiedlicher Erfahrungen in der NS-Zeit.",True,"Etwa darüber, wer wie politisch tätig war, verfolgt wurde oder emigrieren musste.",[("n",7)])
MC("n-ausb",[17],"Woran orientierte sich der Lehrplan nach 1945?","An der medizinisch-gesundheitsfürsorgerischen Ausrichtung der Vorkriegszeit",["An modernen Methoden der US-Sozialarbeit","An der Soziologie der 1968er Bewegung","An einem neuen Universitätsstudium"],"Die Fächer „Nationalpolitische Schulung“ und „Erb- und Rassenkunde“ entfielen, sonst blieb vieles.",[("n",10)])
MC("n-ausb",[23],"Ab wann war die Ausbildung auch für männliche Bewerber zugänglich?","Schuljahr 1948/49",["1912","1938","1976"],"Oktober 1949: 76 weibliche und 6 männliche Schüler*innen.",[("n",9)])
TF("n-ausb",[17],"Arlts Forderung nach interdisziplinärer Fürsorgeforschung fand in der Nachkriegszeit große Beachtung.",False,"Die Folie sagt, ihre grundlegenden Arbeiten wurden weder in Österreich noch international entsprechend beachtet.",[("n",11)])
MC("n-ausb",[23],"Womit warb eine steirische Schule in den 1950er Jahren um Schülerinnen?","„Fraulich-mütterliches Wesen“ könne sich hier entfalten",["Hohes Gehalt und schnelle Karriere","Freie Arbeitszeit und Dienstwagen","Politische Mitbestimmung im Amt"],"Der Folder zeigt, wie lange die weibliche Rollenzuschreibung wirkte.",[("n",43)])
MC("n-ausb",[],"Warum galt der Beruf in den 1950ern und 1960ern als unattraktiv?","Geringe Entlohnung und niedriges Sozialprestige",["Zu viele Stellen für Männer","Zu kurze Arbeitszeiten","Zu hohe Anforderungen an Fremdsprachen"],"Die Folge war ein „katastrophaler Nachwuchsmangel“.",[("n",41)])
MC("n-alltag",[],"Was organisierte das Jugendamt nach dem Krieg mit Hilfe des Auslands?","Erholungsaufenthalte und Pflege, etwa in der Schweiz",["Studienplätze für Fürsorgerinnen","Wohnungsbau für Mütter in den USA","Auswanderung ganzer Familien"],"1.010 Kinder wurden von Schweizer Familien in Pflege übernommen.",[("n",14)])
TF("n-alltag",[18],"Dass viele Frauen allein für die Familie sorgten, wurde bei der Klage über „Jugendverwahrlosung“ berücksichtigt.",False,"Es fand laut Folie keinerlei Berücksichtigung. Mütter wurden verantwortlich gemacht.",[("n",20)])
MC("n-alltag",[],"Was war bei der Suche nach zahlungspflichtigen Vätern ein Problem?","Akten waren vernichtet, Väter gefallen oder vermisst",["Väter zahlten aus Prinzip doppelt","Mütter durften keine Angaben machen","Die Gerichte waren nicht zuständig"],"Väter aus den Besatzungsmächten konnten nicht auf Unterhalt geklagt werden.",[("n",18)])
MC("n-kontrolle",[17,18],"Was bedeutet die „Amts-Kapperl-Methode“?","Autorität nutzen, auch gegen den Willen der Leute",["Beratung in Uniform auf freiwilliger Basis","Spezielle Form der Gruppenarbeit","Verwaltungstechnik im Hausbesuch"],"Eine Fürsorgerin erinnert sich: Kinder wurden in der Früh einfach von zu Hause weggeholt.",[("n",25)])
TF("n-kontrolle",[17],"Hausbesuche waren in den 1950er Jahren in der Regel lange, angemeldete Gespräche.",False,"Eine Fürsorgerin berichtet von unangemeldeten, zwei- bis dreiminütigen Besuchen, um ein „Stricherl“ auf die Liste zu machen.",[("n",21)])
MC("n-kontrolle",[20],"Warum hatten Fürsorgerinnen lange nur ein Taferl mit einem Buchstaben am Tisch?","Um das soziale Gefälle zu betonen und einzuschüchtern",["Damit sich Klient*innen Namen leichter merken","Wegen Papiermangels nach dem Krieg","Weil es zu viele Namensgleichheiten gab"],"Erst Mitte der 70er Jahre kamen Namen. Die Taferl schützten manche auch vor zu großer Identifikation.",[("n",48)])
MC("n-kontrolle",[],"Wer hatte bis Ende der 1960er eine prominente Machtposition im Amt?","ORGAS und die überwiegend männlichen, autoritären Amtsleiter",["Die jungen Praktikant*innen","Die Klient*innen über Beiräte","Die Erziehungsberater*innen"],"„Die Behörde bin ich!“ brüllte einer davon laut einer Erinnerung ins Telefon.",[("n",49)])
MC("n-disz",[18],"Was wurde nach 1945 anstelle der „Asozialität“ zum Gradmesser?","„Sozialanpassung“",["„Selbstermächtigung“","„Volksgemeinschaft“","„Hilfe zur Selbsthilfe“"],"Der Direktor von Eggenburg machte sie sogar am äußeren Erscheinungsbild fest.",[("n",36),("n",37)])
MC("n-disz",[18],"Womit begründete man Verwahrlosung in den 1950ern wie bisher?","Mit Berufstätigkeit und fehlender Aufsichtspflicht von Müttern",["Mit schlechter Bezahlung der Väter","Mit dem Fehlen von Kindergärten","Mit zu großzügigen Sozialleistungen"],"Das setzt die Linie der Verantwortungszuweisung an Mütter fort.",[("n",34)])
MC("n-disz",[18],"Welches Kinderbuch landete angeblich gewaltfördernd auf der schwarzen Liste?","„Tom Sawyer“",["„Pippi Langstrumpf“","„Heidi“","„Die Biene Maja“"],"Teil des Kampfs gegen „Schmutz und Schund“ im Sinne des Gesetzes von 1950.",[("n",38)])
TF("n-disz",[18],"Mit besserer wirtschaftlicher Lage sanken Abnahmen wegen Not, Unterbringungen wegen „Erziehungsschwierigkeiten“ stiegen stark.",True,"Der Grund für die Disziplinierung verschob sich, die Praxis blieb bis Ende der 1960er ähnlich.",[("n",34)])
MC("n-familie",[17],"Was änderte das Jugendwohlfahrtsgesetz von 1954 für Mütter?","Sie konnten nach Befund Vormund unehelicher Kinder werden",["Sie erhielten automatisch die volle Obsorge","Sie mussten die Berufstätigkeit aufgeben","Sie wurden zu Hausbesuchen verpflichtet"],"Erstmals eine rechtliche Stärkung, aber noch keine generelle Reduktion des Kontrollauftrags.",[("n",27)])
MC("n-familie",[17],"Was bedeutet der Wandel zu „familienfördernden“ Maßnahmen?","Familie soll Erziehung selbst leisten, auch Väter werden einbezogen",["Familien werden öfter durch Heime ersetzt","Fürsorgerinnen übernehmen die Erziehung","Der Staat bezahlt alle Mütter für die Heimarbeit"],"Zum Beispiel Elternschulen und Väterschulen am Sonntag. Die Fürsorgerin soll „beratende Freundin“ sein.",[("n",28)])
TF("n-familie",[],"Die Familienpolitik der 1950er und 1960er Jahre zielte unter anderem auf Geburtenförderung.",True,"Hintergrund war ein Geburtenrückgang von fast 50% zwischen 1947 und 1952.",[("n",28)])
MC("n-puppe",[18,23],"Wofür steht die Puppenadoption ab 1954?","Beibehaltung traditioneller geschlechtsspezifischer Arbeitsteilung",["Frühe Förderung von Buben und Mädchen","Abbau von Vorurteilen gegenüber Pflegefamilien","Beginn der Gemeinwesenarbeit"],"Mädchen wurden auf die Rolle als gute Mütter vorbereitet, Buben waren nicht beteiligt.")
TF("n-puppe",[],"Die Puppen wurden monatlich in einer „Puppenmutterberatungsstelle“ vorgestellt.",True,"Bei positivem Befund durften die Mädchen die Puppe nach einem Jahr adoptieren.")
MC("n-casework",[26],"Was gehört zu den Forderungen des Case Work?","Anerkennung der Persönlichkeit, psychosoziale Anamnese, Anleitung zur Selbsthilfe",["Unangemeldete Kontrollen und schnelle Abnahmen","Anonymität der Fürsorgerin und Gehorsam","Allein materielle Hilfe ohne jedes Gespräch"],"Absage an den Kontrollcharakter, demokratische Grundhaltung.",[("n",45)])
MC("n-casework",[26],"Wo wurde die „vertiefte Einzelfallhilfe“ 1957 modellhaft erprobt?","In einem einzigen Wiener Jugendamt in Hernals",["In allen Bezirksjugendämtern gleichzeitig","In der Stadt des Kindes","An der Wiener Universität"],"Zusammenarbeit mit den Jugendämtern von Hamburg und Berlin.",[("n",45)])
TF("n-casework",[26],"Case Work ersetzte die Amtskapperl-Fürsorge in Wien ab 1957 sofort und vollständig.",False,"Es wurde langsam eingeführt, daneben lief die „Amts-Kapperl-Fürsorge“ weiter.",[("n",46)])
MC("n-casework",[26],"Was boten die „psychiatrischen Kurse“ den Fachkräften?","Einführung in Case Work und klientenzentrierte Gesprächsführung",["Ausbildung zur Fachärztin für Psychiatrie","Schulung in Verwaltungsrecht","Kurse für Amtsleiter im Personalwesen"],"Fortbildungen in Case Work mit Supervision gab es ab 1954.",[("n",47)])
MC("n-casework",[26,13],"Was wurde 1949 gegründet?","Das Institut für Erziehungshilfe (Child Guidance Klinik)",["Die Kinderstube des Jugendamtes","Die Wiener Heimkommission","Die Sozialakademie"],"Mitinitiiert von Dworschak und Aichhorn: Therapie, Einbindung von Eltern und Kindern und multiprofessionelles Team.",[("n",39)])
TF("n-casework",[17],"In Österreich vollzog sich der Wandel zu egalitären Methoden schneller als im restlichen Westen.",False,"Er wurde laut Folie nur langsam vollzogen, auch wegen der Unterbrechung durch den „Anschluss“.",[("n",44)])
MC("n-heim",[18],"Als was bezeichnet die Folie das Heim Anfang der 1960er?","„Totale Institution“",["„Zweites Zuhause“","„Offenes Zentrum“","„Sanfte Schule“"],"Trotz psychologischer Betreuung gab es Gewalt bis in die 1970er Jahre.",[("n",53)])
TF("n-heim",[18,17],"Heimerzieher*innen verfügten in der Nachkriegszeit vielfach über keine fachspezifische Ausbildung.",True,"Es gab zudem personelle Konstanz über das NS-Regime hinaus.",[("n",51)])
MC("n-heim",[18],"Was zeigt das Gutachten von 1953 über ein 12-jähriges Mädchen laut Folie?","Das Weiterwirken von NS-Gedankengut",["Einen Fortschritt der klientenzentrierten Arbeit","Den Beginn des Kinderrechtsdenkens","Den Erfolg der Heimreform"],"Abwertende Zuschreibungen wie „primitiv“ und „triebhaft“ dienten als Basis der Fremdunterbringung.",[("n",52)])
MC("n-pflege",[18],"Welche Missstände gab es bei ländlichen Pflegestellen?","Ausbeutung als Arbeitskräfte und mangelhafte Versorgung",["Zu viel Freizeit und zu wenig Aufsicht","Zu teure Schulplätze in den Dörfern","Zu viele Besuche durch die Herkunftsfamilie"],"Eine Fürsorgerin sah Schwielen an Kinderhänden und holte die Kinder zurück, das war aber ein Ausnahmefall.",[("n",23),("n",53)])
ORD("n-casework",[17,26],"Vom Kriegsende bis zur Case-Work-Erprobung: Reihe die Ereignisse.",[("1947","Generalamnestie"),("1949","Institut für Erziehungshilfe"),("1954","Neues Jugendwohlfahrtsgesetz"),("1957","Modellversuch in Hernals")],"In zehn Jahren werden Kontinuität und Aufbruch zugleich sichtbar.",[("n",6),("n",39),("n",27),("n",45)])

# ---------------------------------------------------------------- Von der Fürsorge zur Sozialarbeit

T("sa-68","sa","1968 und seine Folgen",
  "Hochkonjunktur und Wohlfahrtsstaat schufen Raum für Kritik. Die 1968er Bewegung und die Zweite Frauenbewegung griffen autoritäre Strukturen, Kontrolle und Rollenzuschreibungen an. Der Wandel ging von Zwang und Kontrolle in Richtung Freiwilligkeit und Beratung.",
  [("zs",2),("zs",3)])
T("sa-heime","sa","Öffnet die Heime",
  "Studierende, Jugendliche und Fachkräfte protestierten gegen autoritäre Heime. Die Demonstration von 1970 führte zur Enquete und Heimkommission 1971. Die „Stadt des Kindes“ von 1974 wurde zum Symbol, blieb laut dortigen Sozialpädagog*innen aber autoritär geprägt.",
  [("zs",10),("zs",11)])
T("sa-beruf","sa","Von der Fürsorgerin zur Sozialarbeiterin",
  "Der Schwerpunkt verlagerte sich auf Beratung und Gespräch, mit neuen Methoden und Fortbildungen. Der neue Berufstitel symbolisierte den Wunsch nach weniger Kontrolle. Akademien für Sozialarbeit kamen 1976, nachdem Österreich international hinterhergehinkt war.",
  [("zs",6),("zs",14)])
T("sa-konflikt","sa","Generationenkonflikte",
  "Im Amt stießen alte Fürsorgerinnen und junge Sozialarbeiterinnen aufeinander, besonders beim Kontrollauftrag. Kritisiert wurden Bevormundung und fehlende Zeit für menschliche Gespräche. Gegen die fast ausschließlich männlichen Amtsleiter war zunächst kaum anzukommen.",
  [("zs",20),("zs",21),("zs",22)])
T("sa-projekte","sa","Neue Projekte",
  "Politisch engagierte Studierende der Sozialakademien gaben wichtige Impulse. Daraus wurden neue Handlungsfelder wie Frauenhäuser, Streetwork, das „Saftbeisl“ oder der „Augustin“. Sozialarbeit wurde attraktiv, die Schulen waren plötzlich überlaufen.",
  [("zs",18)])
T("sa-familie","sa","Sozialarbeit im Dienste der Familie",
  "Das Kindschaftsrecht 1978 brachte Gleichheit beider Elternteile. Die entscheidende Zäsur folgte 1989 mit der generellen Übertragung des Obsorgerechts an ledige und verheiratete Mütter. Mündelüberwachung und obligatorische Hausbesuche gingen zurück.",
  [("zs",8),("zs",9)])
T("sa-mandat","sa","Das doppelte Mandat",
  "Die Geschichte der Sozialarbeit ist ein Pendeln zwischen Hilfe und Kontrolle, das immanenter Teil der Jugendwohlfahrt bleibt. Die Sozialarbeit kehrte sich von primärer Kontrolle ab und stärkte Freiwilligkeit. Am Ideal des „umfassenden Kinderschutzes“ hält sie zugleich fest.",
  [("zs",31),("zs",32)])
T("sa-90","sa","Die 1990er: Abschied von der alten Fürsorge?",
  "Ende der 1980er zog sich der Staat schrittweise aus der sozialen Sicherung zurück, Bereiche wurden privatisiert. Gleichzeitig nahm Armut zu, und das Jugendamt sah sich Multiproblemlagen gegenüber. Im Jahr 2000 wurde es zur MAG ELF, mit Betonung von Service und Freiwilligkeit.",
  [("zs",23),("zs",24)])
T("sa-staerken","sa","Familien stärken, Kinder schützen",
  "Die Familie bleibt im Zentrum, neu ist aber die Abkopplung von bevölkerungspolitischen Interessen. Der Wickelrucksack ersetzte im Jahr 2000 das Säuglingswäschepaket als Symbol. Väter werden angesprochen, und „Paar- und Familienberatung“ löst das normierte Modell ab.",
  [("zs",25),("zs",26)])
T("sa-heim2000","sa","Heim 2000",
  "Die Reform schloss Großheime zugunsten kleinerer Wohneinheiten und Krisenzentren. Die Reform der 1970er kritisierte autoritäre Führung, die Reform 2000 das System Heim selbst. Das Motto wandelte sich von „so lange wie möglich“ zu „so kurz wie notwendig“.",
  [("zs",27),("zs",28),("zs",29)])
T("sa-pflege","sa","Neue Pflegefamilien",
  "Pflegefamilien gelten seit den 1980ern als eigenständige Familienform, nicht nur als Ersatz. Vorbereitungskurse, gezielte Auswahl und Kontakt zur Herkunftsfamilie heben das Niveau. Auch ältere und beeinträchtigte Kinder werden vermittelt.",
  [("zs",4),("zs",30)])

MULTI("sa-68",[25],"Was kritisierte die 1968er Bewegung an der Fürsorge?",["Autoritärer und kontrollierender Charakter","Weibliche Rollenzuschreibung sozialer Arbeit","Autoritär geführte Kinder- und Jugendheime"],["Zu wenig Kontrolle durch den Staat","Zu viel Freiwilligkeit"],"Zur Kritik kam die Forderung nach Öffnung der Heime.",[("zs",2),("zs",3)])
MC("sa-68",[25,20],"In welche Richtung bewegte sich die Praxis nach 1968?","Von Zwang und Kontrolle zu Freiwilligkeit und Beratung",["Von Beratung zu mehr Hausbesuchen und Abnahmen","Von Ambulanz zu mehr Großheimen","Von Beruf zurück zum Ehrenamt"],"Ausbau niederschwelliger, regionaler und ambulanter Angebote.",[("zs",3)])
MC("sa-heime",[25],"Welche Maßnahme folgte der Heimkritik 1971?","Enquete des Jugendamtes und Wiener Heimkommission",["Schließung aller Wiener Heime im selben Jahr","Gründung der Kinderübernahmestelle","Einführung des Fürsorgebuches"],"Danach gab es längere Ausgangszeiten, kleinere Gruppen und ab 1973 erstmals Taschengeld.",[("zs",10)])
MULTI("sa-heime",[25],"Was war neu an der „Stadt des Kindes“ von 1974?",["Kleine „Familiengruppen“","Besuch öffentlicher Schulen","Öffentliches Schwimmbad, Öffnung nach außen"],["Interne Heimschule mit Drill","Getrennte Säle für 300 Kinder"],"Sie war die bauliche Umsetzung der Richtlinien der Heimkommission.",[("zs",11)])
TF("sa-heime",[25],"Laut damals tätigen Sozialpädagog*innen war die Stadt des Kindes völlig frei von autoritärem Charakter.",False,"Der Heimbetrieb sei dennoch deutlich autoritär geprägt gewesen.",[("zs",11)])
MC("sa-heime",[],"Was geschah 2002 mit der „Stadt des Kindes“?","Sie wurde als letztes Wiener Großheim geschlossen",["Sie wurde zum Krisenzentrum für Säuglinge","Sie wurde an private Träger verkauft","Sie wurde neu eröffnet und vergrößert"],"Das Vorzeigeprojekt der 1970er wurde so selbst Teil der Reform Heim 2000.",[("zs",29)])
MC("sa-beruf",[24,25],"Welche Methoden kamen im „Professionalisierungs- und Modernisierungsschub“ hinzu?","Vertiefte Einzelfallhilfe, nicht-direktive Gesprächsführung, Systemik, Supervision",["Erb- und Rassenkunde, Fürsorgebuch","Kostkinderwesen und Waisenbureau","Nachschau und Amtskapperl"],"Der Schwerpunkt verlagerte sich auf Beratung und Gespräch.",[("zs",6)])
MC("sa-beruf",[24],"Was entstand 1976 in Österreich?","Akademien für Sozialarbeit",["Das Institut für Heimerziehung","Das erste Jugendamt","Die FH-Studiengänge"],"Die viersemestrige Ausbildung wurde erst 1987 auf sechs Semester verlängert.",[("zs",14)])
TF("sa-beruf",[24],"Österreich lag mit den Lehranstalten für gehobene Sozialberufe deutlich hinter dem internationalen Ausbildungsniveau zurück.",True,"Ab 1968 wurde fast in ganz Europa das Niveau angehoben, in Österreich dauerte das bis 1976.",[("zs",14)])
MC("sa-beruf",[21,20],"Wofür steht der neue Berufstitel „Sozialarbeiterin“ symbolisch?","Wunsch nach weniger Kontrolle, mehr Partnerschaftlichkeit und Freiwilligkeit",["Vollständigen Verzicht auf Kinderschutz","Rückkehr zum sozialen Ehrenamt","Unterordnung unter das Amt"],"Zumindest eine theoretische Verschiebung, schreibt die Folie.",[("zs",6)])
MC("sa-konflikt",[25],"Worum drehte sich der Generationskonflikt im Amt vor allem?","Um Fragen des Kontrollauftrags",["Um Pensionsansprüche","Um die Wahl der Amtsleiter","Um die Verlegung der Ämter"],"Dazu Kritik an Bevormundung und fehlender Zeit für Gespräche.")
MC("sa-konflikt",[23],"Wie arbeiteten Männer, die in den 1950er/60er Jahren die Ausbildung machten, meistens?","Mehrheitlich nicht in der Jugendwohlfahrt",["Fast alle als Sprengelfürsorger im Außendienst","Hauptsächlich in Mutterberatungsstellen","Als Heimmütter in Kinderheimen"],"Viele strebten Karrieren mit höherem Sozialprestige an.",[("zs",22)])
MC("sa-projekte",[25],"Welche Projekte gingen aus Impulsen der Studierenden der Sozialakademien hervor?","Frauenhäuser, Streetwork, Obdachlosenzeitung „Augustin“",["KÜST, Kinderstube und Wäschepaket","Waisenbureau, Armenanstalten, Kostkinderwesen","Mutterkreuz, Familienasyle, Fürsorgebuch"],"Dazu Saftbeisl, Ausstiegshilfen für Prostituierte und Betreuung von „Gastarbeiterkindern“.")
TF("sa-projekte",[25],"Nach 1968 wurde Sozialarbeit attraktiv, Ausbildungsstätten waren plötzlich überlaufen.",True,"Das ist ein deutlicher Wandel gegenüber dem Nachwuchsmangel der 1950er und 1960er.",[("zs",14),("zs",18)])
MC("sa-familie",[8],"Was brachte das Jahr 1989?","Generelle gesetzliche Übertragung des Obsorgerechts an Mütter",["Die Einführung der Generalvormundschaft","Die Gründung des Jugendamtes","Die Schließung aller Pflegestellen"],"Damit endete eine lange Tradition: Die zu überwachenden „Mündel“ und die obligatorischen Hausbesuche nahmen ab.",[("zs",9)])
MC("sa-familie",[],"Was bewirkte das neue Kindschaftsrecht von 1978?","Gleichheitsgrundsatz beider Elternteile gegenüber dem Kind",["Alleinige Obsorge des Vaters bei Scheidung","Verpflichtung beider Eltern zu Hausbesuchen","Abschaffung von Unterhaltszahlungen"],"Verpflichtung zu einvernehmlicher Obsorge.",[("zs",8)])
TF("sa-pflege",[],"Ab den 1980er Jahren wurden Pflegefamilien erstmals als eigenständige Familienform mit spezifischen Problemen gesehen.",True,"Beratungsstelle ab 1983 und Vorbereitungskurse ab 1985 zeugen davon.",[("zs",4)])
MC("sa-mandat",[19],"Was meint das „doppelte Mandat“?","Soziale Arbeit steht zwischen Hilfe und Kontrolle",["Eine Fürsorgerin hat zwei Sprengel","Bund und Land finanzieren gemeinsam","Zwei Personen müssen jeden Akt unterschreiben"],"Dieses Pendeln ist laut Folie immanenter Teil der Jugendwohlfahrt.")
MC("sa-mandat",[21],"Wie geht moderne Sozialarbeit laut Folie mit dem doppelten Mandat um?","Abkehr von primärer Kontrolle bei Festhalten am umfassenden Kinderschutz",["Völliger Verzicht auf jede Kontrolle","Rückkehr zur Kontrolle durch Hausbesuche","Abgabe des Kinderschutzes an die Polizei"],"Es gilt theoretisch und praktisch. Kontrolle wird nicht geleugnet.")
TF("sa-mandat",[21,19],"Das Pendeln zwischen Hilfe und Kontrolle wurde mit der modernen Sozialarbeit endgültig aufgehoben.",False,"Es ist laut Folie immanenter Teil der Jugendwohlfahrt. Verändert hat sich die Gewichtung.")
MC("sa-mandat",[21],"Wie fasst eine Sozialarbeiterin die Haltung der 1970er zusammen?","„Kontrolle ja, reduziert aber auf die schwierigsten Fälle“",["„Kontrolle ist immer die beste Hilfe“","„Hilfe nur für die Arbeitswilligen“","„Die Behörde bin ich“"],"„Die Behörde bin ich!“ stammt dagegen von einem autoritären Amtsleiter früherer Jahre.",[("zs",7)])
MC("sa-90",[],"Was kennzeichnet die Sozialpolitik ab Ende der 1980er Jahre?","Schrittweiser Rückzug des Staates und Privatisierungen",["Starker Ausbau aller Leistungen","Wiedereinführung des Heimatrechts","Abschaffung der Sozialversicherung"],"Zugleich gab es mehr armutsgefährdete Menschen und Multiproblemlagen.",[("zs",23)])
MC("sa-90",[],"Was geschah im Jahr 2000 mit dem Jugendamt?","Umbenennung in MAG ELF, Amt für Jugend und Familie",["Auflösung und Verlagerung an Vereine","Eingliederung in das Bundesministerium","Rückbenennung in Wohlfahrtsamt"],"Bekenntnis zu umfassendem präventivem Kinder- und Jugendschutz.",[("zs",24)])
MC("sa-staerken",[20],"Wofür steht der Wickelrucksack?","Symbol für die Neuorientierung der Jugendwohlfahrt",["Symbol für die Rückkehr zur Erfassung","Prämie für kinderreiche Familien","Ausrüstung der Fürsorgerinnen"],"Er ersetzte 2000 das Säuglingswäschepaket und spricht auch Väter an.")
TF("sa-staerken",[20],"Kinderschutz und Familienförderung sind heute laut Folie von bevölkerungspolitischen Interessen abgekoppelt.",True,"Das ist ein großer Unterschied zur bevölkerungspolitischen Linie seit Tandler.")
MC("sa-staerken",[],"Was drückt die Umbenennung in „Paar- und Familienberatungsstellen“ aus?","Absage an das normierte Vater-Mutter-Kind-Modell",["Pflicht zur Eheschließung","Trennung von Eltern und Kindern","Ende aller Beratung"],"Patchwork-Familien werden zunehmend berücksichtigt.")
MC("sa-heim2000",[20],"Wie lautet das neue Motto der Fremdunterbringung?","„So kurz wie möglich“ bzw. „so kurz wie notwendig“",["„So lange wie möglich“","„Wer nicht arbeitet, soll auch nicht essen“","„Erst Heim, dann Familie“"],"Dazu kommen regionale Krisenzentren, damit das gewohnte Umfeld bleibt.",[("zs",29)])
MC("sa-heim2000",[20,25],"Was ist der Unterschied zwischen den Heimreformen der 1970er und von 2000?","Früher Kritik am Führungsstil, 2000 Kritik am System Heim selbst",["Früher Kritik an den Kosten, 2000 an der Lage","Früher Schließung aller Heime, 2000 neue Großheime","Früher nur in Wien, 2000 nur in Niederösterreich"],"Ein starkes Beispiel, um im Vergleich zu argumentieren: „Heim als Kindergefängnis“.",[("zs",27)])
MC("sa-heim2000",[21],"Wie laufen Erhebungen heute laut Folie ab?","Anlassbezogen nach dem Vieraugenprinzip",["Monatlich und unangemeldet durch eine Person","Telefonisch über die Schule","Durch die Polizei in Uniform"],"Zwangsmaßnahmen werden nur bei „Gefahr im Verzug“ angedroht.",[("zs",29)])
MC("sa-heim2000",[],"Was war FIDUZ 1990?","Die erste Wohngemeinschaft als Krisenzentrum",["Eine Beratungsstelle für Pflegeeltern","Ein Großheim in Niederösterreich","Ein Verein für Streetwork"],"Säuglinge und Kleinkinder kamen ab 2001 temporär in Krisenpflegefamilien.",[("zs",28)])
ORD("sa-heim2000",[25,20],"Vom Protest zur Schließung: Bringe die Heimgeschichte in Reihenfolge.",[("1970","Demonstration von Lehrlingen und Jugendlichen"),("1974","Stadt des Kindes"),("1995","Beginn der Reform Heim 2000"),("2013","Schließung des Lindenhofs")],"Von der Kritik an Heimleitungen zur Kritik am System.",[("zs",10),("zs",11),("z",4),("zs",29)])

# ---------------------------------------------------------------- Epochenuebergreifend

T("x-verw","nach","Der Wandel von „Verwahrlosung“",
  "Der Begriff zieht sich durch alle Epochen und zeigt, wie Fürsorge ihre Klient*innen sah: als Ansteckungsgefahr in der Monarchie, als Kampfbegriff und bei Aichhorn als Reaktion im Roten Wien, als „Asozialität“ im NS, als „Sozialanpassung“ in der Nachkriegszeit. Das ist gutes Material für Überblicksfragen.",
  [("a1",30),("rw",17),("rw",18),("t",18),("n",36)])
T("x-paket","sa","Vom Wäschepaket zum Wickelrucksack",
  "Ein Objekt, das die Geschichte erzählt: 1927 im Roten Wien für alle Mütter, im NS auch zur Erhebung von Erbkrankheiten, nach dem Krieg zunächst nur für Bedürftige, im Jahr 2000 durch den Wickelrucksack ersetzt.",
  [("rw",14),("t",35),("n",19),("zs",25)])
T("x-haus","nach","Der Hausbesuch durch die Zeit",
  "Vom Friendly Visiting bis zur Erhebung nach dem Vieraugenprinzip wandelte sich der Hausbesuch stark. Er war Belehrung und Kontrolle unehelicher Mütter, Erfassung im NS und bis in die 1980er Jahre Pflicht bei den Mündeln. Heute geschieht er anlassbezogen.",
  [("a2",9),("eb",6),("rw",16),("t",35),("n",21),("zs",9),("zs",29)])

MATCH("x-verw",[11,16,18],"Wie deutet welche Epoche „Verwahrlosung“?",[("Monarchie","Moralisch, wie eine „Ansteckungsgefahr“"),("Aichhorn","Reaktion auf psychische und soziale Erfahrung"),("NS-Regime","„Asozialität“, gemeinschaftswidriges Verhalten"),("1950er","Mangelnde „Sozialanpassung“")],"Die Deutung bestimmt jeweils, wie eingegriffen wird.")
MATCH("x-paket",[22,20],"Was war das Säuglingspaket wann?",[("1927","Für alle Mütter, Übergabe beim Hausbesuch"),("NS-Zeit","Zugleich Erhebung von Erbkrankheiten"),("Nachkriegszeit","Vorerst nur für bedürftige Mütter"),("2000","Ersetzt durch den Wickelrucksack")],"Hilfe und Kontrolle in einem Paket, ein gutes Beispiel für das doppelte Mandat.")
MC("x-haus",[19,20],"Wie veränderte sich die Mündelbetreuung 1989?","Die obligatorischen Hausbesuche nahmen ab, Tätigkeiten verlagerten sich ins Amt",["Jede Familie bekam nun wöchentlich Besuch","Hausbesuche wurden auf das Land beschränkt","Hausbesuche gingen an die Polizei"],"Das ist eine Folge der Obsorge-Übertragung an die Mütter.",[("zs",9)])
ORD("x-haus",[24],"Reihe die Stationen des Berufs.",[("1912","Vereinigte Fachkurse für Volkspflege"),("1948/49","Ausbildung auch für Männer"),("1976","Akademien für Sozialarbeit"),("2002","Vierjährige FH-Studiengänge")],"Von den ersten Kursen zum Hochschulstudium.",[("eb",11),("n",9),("zs",14),("z",4)])
ORD("x-verw",[2,11],"Bringe die großen Epochen in Reihenfolge.",[("1861","Liberale Ära der Gemeindeverwaltung"),("1919","Rotes Wien"),("1934","Austrofaschismus"),("1938","Nationalsozialismus")],"Die zeitliche Gliederung ist die Basis jeder Überblicksantwort.",[("a1",3),("rw",2),("t",2),("t",12)])
ORD("x-paket",[11],"Von der Vormundschaft zur Obsorge: Was kam wann?",[("1912","Gemeinderatsbeschluss zur Vormundschaft"),("1954","Mütter können nach Befund Vormund werden"),("1978","Neues Kindschaftsrecht"),("1989","Obsorgerecht generell an Mütter")],"Über 70 Jahre vergehen, bis Mütter unehelicher Kinder selbstverständlich Obsorge haben.",[("eb",4),("n",27),("zs",8),("zs",9)])

# ---------------------------------------------------------------- Nachschlagen

for p in [
    ("Ilse Arlt","1876–1960","Gründet 1912 die Vereinigten Fachkurse für Volkspflege, 13 Bedürfnisklassen, Fürsorgewissenschaft.",[("eb",8),("eb",11),("eb",18)]),
    ("Alice Salomon","1872–1948","Soziale Frauenschule Berlin 1908, Akademie 1925, 1937 ausgewiesen.",[("a2",47),("a2",50),("a2",52)]),
    ("Mary Richmond","1861–1928","Altamont Hotel, Einzelfallhilfe, „Social Diagnosis“ 1917.",[("a2",34),("a2",37),("a2",39)]),
    ("Jane Addams","1860–1935","Hull House in Chicago 1889, soziale Mütterlichkeit, sozialpolitisches Engagement.",[("a2",26),("a2",33)]),
    ("Henrietta und Samuel Barnett","","Toynbee Hall in London: gemeinsames Leben mit den Armen, Bildung statt Disziplinierung.",[("a2",16),("a2",17)]),
    ("Marie Lang","1858–1934","Gründerin des Ottakringer Settlements, Frauenrechtlerin.",[("a2",55)]),
    ("Ellen Key","1849–1926","„Das Jahrhundert des Kindes“ (1902), auf den Folien „Kay“.",[("a2",5)]),
    ("Julius Tandler","Stadtrat 1920–1934","Wohlfahrtsamt 1921, Anrecht auf Fürsorge, bevölkerungspolitische Fürsorge.",[("rw",8),("rw",9),("rw",10)]),
    ("Hugo Breitner","Stadtrat 1919–1932","Sozialdemokratischer Finanzpolitiker, „Breitner-Steuern“.",[("rw",6)]),
    ("August Aichhorn","gest. 1949","Psychoanalytische Sozialarbeit, Oberhollabrunn, Erziehungsberatung, Kinderstube.",[("rw",18),("rw",20),("rw",24),("rw",38)]),
    ("Rosa Dworschak","1896–1990","Sprengelfürsorgerin, Dorfgeschichten, Child Guidance Klinik, Vermittlerin des Case Work.",[("rw",25),("rw",28),("n",39)]),
    ("Franz Winkelmayer","","Erste Erziehungsberatung 1919, 1943 kommissarische Leitung am Spiegelgrund.",[("rw",18)]),
    ("Max Winter","1870–1937","Sozialreporter, 1919 Vizebürgermeister, prangerte die alte Kinderübernahmsstelle an.",[("j",14)]),
    ("Charlotte Bühler und Hildegard Hetzer","","Entwickelten auf Basis der Kinderbeobachtung an der KÜST psychologische Testverfahren.",[("j",25)]),
    ("Otto Zipser","geb. 1928","Zeitzeuge, 1940 zur „Beobachtung“ in die Anstalt Am Steinhof eingewiesen.",[("t",39),("t",40)]),
]:
    PEOPLE.append(dict(name=p[0], dates=p[1], text=p[2], src=p[3]))

for t in [
    ("Subsidiaritätsprinzip","Die Gemeinde ist erst zuständig, wenn Verwandte, Vereine und Stiftungen nicht helfen können.",[("a1",7)]),
    ("Heimatrecht","Aufenthaltsrecht und Anspruch auf Armenversorgung in der Heimatgemeinde, Gesetz von 1863.",[("a1",7)]),
    ("Ersitzungsprinzip","Novelle 1896: Heimatrecht nach zehn Jahren ununterbrochenem Aufenthalt.",[("a1",9)]),
    ("Offene und geschlossene Fürsorge","Offen ist Unterstützung außerhalb, etwa Geldaushilfen, geschlossen ist die Unterbringung in Anstalten.",[("a1",19),("a1",20)]),
    ("Kostkinder","Fremd untergebrachte Kinder in Pflegefamilien gegen Kostgeld.",[("a1",28),("a2",7)]),
    ("Elberfelder System","Ehrenamtliche Armenpflege nach dem Quartierprinzip, von 1853.",[("a2",9)]),
    ("Friendly Visiting","Hausbesuch, zentrales Element von Elberfeld und bei Richmond.",[("a2",9),("a2",37)]),
    ("Geistige Mütterlichkeit","Ideal der bürgerlichen Frauenbewegung: Fürsorge als weiblicher Beitrag.",[("a2",11)]),
    ("Settlement","Akademiker*innen leben im Armenviertel, lehren und lernen dort. Vorläufer der Gemeinwesenarbeit.",[("a2",14),("a2",18)]),
    ("Case Work","Vertiefte Einzelfallhilfe auf Basis einer sozialen Diagnose.",[("a2",37),("n",45)]),
    ("Listenvormund","Aus Wählerlisten bestimmter Mann, Vormund meist nur pro forma.",[("eb",3)]),
    ("Berufsvormundschaft","Bezahlte, organisierte Vormundschaft für uneheliche Kinder.",[("eb",3),("eb",4)]),
    ("Generalvormundschaft","Vormundschaft der Gemeinde Wien über alle dort ledig geborenen Kinder.",[("rw",12)]),
    ("Mündel","Uneheliche oder verwaiste Kinder unter Vormundschaft.",[("eb",6),("rw",12)]),
    ("Verbindungsdienst","Fürsorgerinnen in Geburtskliniken und Schulen zur Erfassung Bedürftiger.",[("eb",6),("rw",14)]),
    ("Volkspflege","Arlts Hilfsweise: Hilfe nach genauer Erfassung der Not unter Berücksichtigung aller Grundbedürfnisse.",[("eb",19)]),
    ("Einheitsfürsorge","Familienfürsorge mit bevölkerungspolitischer Ausrichtung auf die Reproduktion der Familie.",[("eb",29)]),
    ("Erfassen, Erheben, Nachschau","Umschreibung für die Kontrollpraktiken der Fürsorgerin.",[("rw",15)]),
    ("Fürsorgesprengel","Bezirk einer Fürsorgerin, Dezentralisierung des Jugendamtes.",[("rw",8),("n",2)]),
    ("Doppeltes Mandat","Soziale Arbeit zwischen Hilfe und Kontrolle.",[("e",19),("zs",31)]),
    ("Sozialanpassung","Maßstab der Nachkriegszeit für Jugendliche, an Stelle der NS-„Asozialität“.",[("n",36)]),
    ("Amtskapperl","Fürsorge, die ihre Macht ausschöpft, in den Worten von Fürsorgerinnen.",[("n",25),("n",46)]),
    ("Totale Institution","Bezeichnung für das Heim mit Gewalt und Kontrolle.",[("n",53)]),
    ("Vieraugenprinzip","Zwei Sozialarbeiter*innen besuchen Familien anlassbezogen.",[("zs",29),("j",76)]),
    ("Clearing","Abklärung und Aufgabenteilung in den Regionalstellen, löste das alte Sprengelmodell ab.",[("j",70)]),
    ("Fürsorgeassistentin","1968 eingestellte Kräfte, die die Ausbildung berufsbegleitend nachholen mussten.",[("j",64)]),
]:
    TERMS.append(dict(term=t[0], text=t[1], src=t[2]))

for y, txt, s, ch in [
    ("1853","Elberfelder System",[("a2",9)],"ref"),
    ("1861","Beginn der liberalen Ära der Gemeindeverwaltung",[("a1",3)],"mon"),
    ("1863","Heimatrechtsgesetz",[("a1",7)],"mon"),
    ("1885","Zwangsarbeitergesetze",[("a1",11)],"mon"),
    ("1889","Hull House in Chicago, Altamont Hotel in Baltimore",[("a2",25),("a2",34)],"ref"),
    ("1895","Beginn der christlichsozialen Ära",[("a1",4)],"mon"),
    ("1896","Novelle des Heimatrechts: Ersitzungsprinzip",[("a1",9)],"mon"),
    ("1901","Reform der Armenfürsorge, Ottakringer Settlement",[("a2",3),("a2",54)],"ref"),
    ("1908","Salomons Soziale Frauenschule in Berlin",[("a2",47)],"ref"),
    ("1912","Arlts Vereinigte Fachkurse für Volkspflege",[("eb",11)],"ber"),
    ("1913","Berufsvormundschaft Ottakring, 10 bezahlte Stellen",[("eb",4),("eb",5)],"ber"),
    ("1916","Ministerium für soziale Fürsorge",[("eb",22)],"ber"),
    ("1917","Wiener Jugendamt, Ehe- und Kinderlosigkeit als Bedingung, „Social Diagnosis“",[("z",1),("eb",25),("a2",39)],"ber"),
    ("1918","Akademie für soziale Verwaltung, Oberhollabrunn",[("eb",27),("rw",38)],"ber"),
    ("1919","Sozialdemokratische Mehrheit in Wien, erste Erziehungsberatung",[("rw",2),("rw",18)],"rot"),
    ("1921","Wiener Wohlfahrtsamt",[("rw",8)],"rot"),
    ("1925","Kinderübernahmestelle (KÜST)",[("rw",33)],"rot"),
    ("1926","Kinderstube, Hilfsfürsorgerinnen",[("rw",16),("rw",24)],"rot"),
    ("1927","Säuglingswäschepaket, Schloss Wilhelminenberg",[("rw",14),("rw",36)],"rot"),
    ("1934","Ständestaat, Familienasyle",[("t",2),("t",8)],"aut"),
    ("1938","„Anschluss“, Diensteid, Gaujugendamt",[("t",12),("t",27)],"ns"),
    ("1940","Jugendwohlfahrtsverordnung für die Ostmark",[("t",17)],"ns"),
    ("1941","Heilpädagogische Klinik Am Spiegelgrund",[("t",38)],"ns"),
    ("1945","Ende der Kampfhandlungen, Wiener Jugendamt wiederhergestellt",[("n",2)],"nach"),
    ("1947","Generalamnestie",[("n",6)],"nach"),
    ("1948/49","Ausbildung auch für Männer",[("n",9)],"nach"),
    ("1949","Institut für Erziehungshilfe",[("n",39)],"nach"),
    ("1928","Jugendstrafrecht",[("j",27)],"rot"),
    ("1950","Schutz der Jugend gegen sittliche Gefährdung",[("n",38)],"nach"),
    ("1954","Neues Jugendwohlfahrtsgesetz, Puppenadoption",[("n",27),("n",30)],"nach"),
    ("1957","Modellversuch Case Work in Hernals",[("n",45)],"nach"),
    ("1962","Lehranstalt für gehobene Sozialberufe, Institut für Heimerziehung",[("n",41),("n",51)],"nach"),
    ("1970","Demonstration gegen autoritäre Heime",[("zs",10)],"sa"),
    ("1971","Enquete und Wiener Heimkommission",[("zs",10)],"sa"),
    ("1974","Stadt des Kindes",[("zs",11)],"sa"),
    ("1976","Akademien für Sozialarbeit",[("zs",14)],"sa"),
    ("1978","Neues Kindschaftsrecht",[("zs",8)],"sa"),
    ("1989","Obsorgerecht generell an Mütter",[("zs",9)],"sa"),
    ("1995","Beginn der Reform Heim 2000",[("z",4)],"sa"),
    ("2000","MAG ELF, Wickelrucksack",[("zs",24),("zs",25)],"sa"),
    ("2002","Letztes Wiener Großheim schließt, FH-Studiengänge",[("zs",29),("z",4)],"sa"),
    ("2010","Heimkinder gehen an die Öffentlichkeit, Aufarbeitung beginnt",[("j",77)],"heute"),
    ("2013","Lindenhof schließt, Tag der offenen Tür für ehemalige Heim- und Pflegekinder",[("zs",29),("j",78)],"heute"),
    ("2018","Wiener Kinder- und Jugendhilfe",[("z",5)],"sa"),
]:
    TIMELINE.append(dict(y=y, t=txt, src=s, ch=ch))

for title, text, src in [
    ("Heimatrecht: 1863 oder 1865?","Leitfrage und Foliensatz nennen 1863, die Zeittafel 1865. Nimm 1863, so steht es in der Leitfrage.",[("a1",7),("z",1)]),
    ("Generalvormundschaft: 1921 oder 1922?","Folie und Zusatztext nennen 1921, der Text sogar den 10. 2. 1921, die Zeittafel 1922. Die Folie sagt zudem Vormundschaft bis zur Volljährigkeit mit 21, der Text bis zum 18. Lebensjahr. Das Jahr wird in der App nicht abgefragt.",[("rw",12),("j",21),("z",2)]),
    ("Berufstitel Sozialarbeiterin: 1968, 1976 oder 1981?","Die Folie nennt 1968, die Zeittafel 1976 zusammen mit den Akademien, der Zusatztext „offiziell“ erst 1981. Eine Karte fragt die Angabe aus dem Zusatztext ab und nennt sie als solche. Am sichersten beschreibst du es als Prozess: um 1968 an den Schulen, 1976 mit den Akademien, offiziell später.",[("zs",6),("z",3),("j",61)]),
    ("Lehranstalt: 1962 oder 1963?","Nachkriegsfolie und Zeittafel nennen 1962, der Foliensatz „Von der Fürsorge zur Sozialarbeit“ „seit 1963“.",[("n",41),("z",3),("zs",14)]),
    ("Erste Berufsvormundschaft: Penzing oder Rudolfsheim?","Folie und Zusatztext nennen Ottakring 1913 und Penzing 1914, die Zeittafel Ottakring und Rudolfsheim 1913/14 und zudem eine Einführung 1910.",[("eb",4),("j",10),("z",1)]),
    ("Jugendamt: 1916 oder 1917, und welcher April?","1916 wird das Amt ein selbständiges Referat „städtisches Jugendamt“, die Gründung datieren Zeittafel und Folie mit 1917. Beim Tag schwanken die Unterlagen: Überschrift und Vorwort des Zusatztexts nennen den 27. 4., sein Fließtext auch den 17. 4. und 24. 4., die Folie den 17. 4. Merke dir April 1917.",[("eb",22),("eb",26),("z",1),("j",5),("j",15)]),
    ("Zukunftswerkstatt: 1988 oder 1989?","Die Zeittafel nennt die Werkstatt 1988, die Folie den Bericht von 1989. Beides passt zusammen, wenn der Bericht ein Jahr später kam, klar sagen es die Folien aber nicht.",[("z",4),("zs",27)]),
    ("Tippfehler in den Unterlagen","Aichhorns Lebensdaten stehen in Folie und Zusatztext als „1978–1949“. Auf der Folie zum Altamont Hotel steht „Addams“, gemeint ist dem Zusammenhang nach Richmond. Ellen Key erscheint als „Kay“.",[("rw",20),("a2",37),("a2",5)]),
    ("Wien als Bundesland: 1921 oder 1922?","Die Folie nennt den 1. 1. 1921, der Zusatztext den 1. 1. 1922.",[("rw",2),("j",18)]),
    ("KÜST: wie lange blieben Kinder?","Die Folie nennt drei bis sechs Wochen, der Zusatztext einen dreiwöchigen Aufenthalt.",[("rw",33),("j",25)]),
    ("Arlts Schule nach dem Krieg","Der Zusatztext nennt Wiedereröffnung 1945 und Schließung 1948, die Zeittafel 1946 und 1949. Den Renner-Preis datiert der Text auf 1954, die Folie auf 1955.",[("j",12),("z",3),("eb",21)]),
    ("Amtszeiten und kleine Abweichungen","Tandler: bis 1934 auf der Folie, bis 1933 im Zusatztext. Breitner: ab 1919 auf der Folie, ab 1918 im Zusatztext. Öffentliche Heime im NS: 52 im Jahr 1942 auf der Folie, im Jahr 1941 im Zusatztext.",[("rw",6),("rw",8),("j",19),("t",15),("j",36)]),
    ("Der Reader fehlt noch","Laut Einführung gehören auch die Texte aus dem Reader zur Prüfungsbasis. Sie waren nicht in den Unterlagen, darum stammt nichts in dieser App daraus.",[("e",2)]),
    ("„Bedürfnishemmschwelle“","Der Begriff aus Leitfrage 6 steht weder auf den Folien noch im Zusatztext. Lies die Musterantwort als Annäherung und ergänze sie aus deiner Mitschrift.",[("eb",20),("j",12)]),
]:
    TRAPS.append(dict(title=title, text=text, src=src))

# ---------------------------------------------------------------- Zusatztext "100 Jahre Wiener Jugendamt" (Dokument j)
# Seitenzahlen sind PDF-Seiten und entsprechen den gedruckten Seiten. Karten nur aus dem Text gelten als Zusatz (extra)
# und zaehlen nicht gegen den Stempel.

def DEEP(n, text, src):
    next(l for l in LFS if l["n"] == n).setdefault("deep", []).append(dict(t=text, src=src))

DEEP(1, "Die Armenversorgung beruhte auf unsystematischer Zusammenarbeit öffentlicher, kirchlicher und privater Stellen, die auf „freier Liebestätigkeit“ basierten.", [("j",9)])
DEEP(2, "Bis zur Reform im Roten Wien lag die Kinder- und Jugendfürsorge mehrheitlich im Bereich der Armenpflege; das Heimatrecht blieb bis 1938 in Kraft.", [("j",9)])
DEEP(4, "Das Heimatrecht blieb in der Fassung von 1896 bis 1938 in Kraft und setzte einen zehnjährigen Aufenthalt voraus, statt an Geburt oder Verehelichung gebunden zu sein.", [("j",9)])
DEEP(5, "Anlass waren willkürlich einsetzende private Wohlfahrt, fehlendes Fachpersonal und falsche Alltagstheorien über Armut. Die Schule war zugleich als Forschungseinrichtung gedacht.", [("j",11)])
DEEP(5, "Ihre „Volkspflege“ meinte individuelle Hilfe und ist inhaltlich das Gegenteil der späteren NS-Fürsorge am „Volkskörper“, auch wenn die Begriffe ähnlich klingen.", [("j",16)])
DEEP(6, "Auch der Zusatztext verwendet das Wort nicht, bestätigt aber: Hilfe soll prophylaktisch wirken und erst nach genauer Abklärung, der „sozialen Diagnose“, ansetzen.", [("j",12)])
DEEP(8, "Mütter waren Männern rechtlich nicht gleichgestellt und hatten bis 1918 kein Wahlrecht. Schon die ersten Ansätze standen im Spannungsfeld von Hilfe und Kontrolle.", [("j",9),("j",10)])
DEEP(9, "Auf die ehrenamtliche Armenpflege bestand kein Rechtsanspruch, dafür war sie nicht an das Heimatrecht gebunden. Waisenmütter hatten keine berufliche Ausbildung.", [("j",9)])
DEEP(10, "Die Reform sollte auch die sozialistische Idee des „Neuen Menschen“ voranbringen. Investitionen galten als „produktiv“, weil sie laut Tandler das Volk arbeitsfähig machen.", [("j",18),("j",20)])
DEEP(11, "Das Wiener Modell erlangte in Österreich und Europa Vorbildcharakter und prägte Theorie und Praxis für mehrere Jahrzehnte. Der Aufbau der Fürsorgeerziehung war entscheidend für das Jugendstrafrecht von 1928.", [("j",27)])
DEEP(11, "Auch Hierarchie und geschlechtsspezifische Arbeitsteilung im Amt blieben jahrzehntelang kaum hinterfragt: Männer im Innendienst, Fürsorgerinnen im Außendienst.", [("j",21)])
DEEP(12, "Tandler nahm widersprüchliche Positionen ein, etwa zur Sterilisation. Die Fürsorge des Roten Wien soll aber nicht mit der „negativen Eugenik“ der NS-Vernichtungspolitik gleichgesetzt werden.", [("j",20)])
DEEP(12, "Eugenische Bewegungen gab es seit Ende des 19. Jahrhunderts in vielen Ländern und in allen politischen Lagern.", [("j",20)])
DEEP(13, "Zunächst war er der einzige Erziehungsberater. Anliegen war es, Familien zu unterstützen und Heimunterbringungen zu umgehen.", [("j",22),("j",23)])
DEEP(14, "Das Säuglingswäschepaket ging nur noch an „bedürftige“ Mütter, das Josefswerk führte „Ehetauglichkeitsprüfungen“ durch, das Fürsorgebuch sollte den Fürsorgekataster ablösen.", [("j",31),("j",32)])
DEEP(15, "Das Jugendamt wurde dem Gesundheitsamt unterstellt, um rassenhygienische Ideale wirksam umzusetzen. Am Ende war es „durchaus mitverantwortlich“ an der Rassenpolitik.", [("j",35),("j",41)])
DEEP(15, "Die Ausbildung führte zum Titel „Volkspflegerin“, Aufnahmekriterien waren „deutschblütige Abstammung“ und gute Gesundheit. Die Aufnahmeprüfung prüfte vor allem die politische Haltung.", [("j",37),("j",38)])
DEEP(16, "Das immanente Pendeln zwischen Kontrolle und Hilfe schlug eindeutig in Richtung totalitärer Kontrolle aus. Das Jugendamt musste Eltern verständigen, „wenn ihre Kinder an Lungenentzündung verstorben sind“, was eine Fürsorgerin makaber nennt.", [("j",41)])
DEEP(16, "Der Erziehungsberater begutachtete alle neu überstellten Kinder. Diese Machtbefugnis prägte Heimeinweisungen bis in die 1970er Jahre.", [("j",36)])
DEEP(17, "Aus der Verordnung von 1940 wurden nur offensichtliche NS-Bezüge gestrichen. Die in der NS-Zeit eingeführte Teilung in ORGA und Fachfürsorgerin blieb bis 1971 bestehen.", [("j",45),("j",57)])
DEEP(18, "Gutachten als Grundlage der Fremdunterbringung unterschieden sich in der Bewertung der Kinder kaum von jenen der NS-Zeit.", [("j",58)])
DEEP(19, "Der Text nennt schon für die Anfänge das „Spannungsfeld von Hilfe und Kontrolle“, das die Praxis jahrzehntelang prägte, und das Pendeln einen seit jeher immanenten Teil der Jugendwohlfahrt.", [("j",10),("j",79)])
DEEP(20, "Heute stehen laut Vorwort Kinderrechte, Beteiligung von Kindern und Eltern und Transparenz im Mittelpunkt: „Kinder schützen, Eltern unterstützen“.", [("j",5)])
DEEP(21, "Die Hauptaufgabe Kinderschutz wird offen benannt, die Entwicklung hat sich auch praktisch weit von primärer Kontrolle wegbewegt.", [("j",79)])
DEEP(22, "1914 besuchten ehrenamtliche Volkspflegerinnen von Arlt nun alle Wöchnerinnen, sofern nicht von vornherein keine Bedürftigkeit anzunehmen war. Im NS diente der Dienst auch der Vorauswahl für die HJ.", [("j",13),("j",40)])
DEEP(23, "Die „Berufspflegerin“ gilt als „Erfindung der kommunalen Verwaltung“; zugleich leitet sich der Beruf aus dem bürgerlichen weiblichen Ehrenamt ab. Bis in die 1970er blieb er fast ausschließlich weiblich.", [("j",11),("j",67)])
DEEP(24, "Offiziell ersetzte der Titel „Sozialarbeiter“ die „Fürsorgerin“ erst 1981. Leitende Stellen gingen erst ab Mitte der 1980er an Sozialarbeiter*innen statt an Berufsfremde.", [("j",61),("j",67)])
DEEP(25, "Zugleich ein „Entidealisierungsschock“: Junge Sozialarbeiter*innen erlebten die Realität im Amt noch Anfang der 1980er als schockierend, und viele alte Großheime blieben bis Mitte der 1970er autoritär.", [("j",60),("j",66)])
DEEP(26, "Die Idee, aus „Parteien“ mögen „Klienten“ werden, ließ in der Praxis lange auf sich warten. Das Institut für Erziehungshilfe hatte für viele Fürsorgerinnen Modellcharakter.", [("j",55),("j",56)])

T("j-kost","mon","Kostkinder im Ersten Weltkrieg",
  "Der Zusatztext zeigt, wie stark die Fremdunterbringung im Krieg zunahm: von 4.732 Pflegekindern im Jahr 1914 auf 8.325 im Jahr 1918, die Mehrheit am Land. Die alte Kinderübernahmsstelle war stark überfüllt. Der Sozialreporter Max Winter nannte sie eine Schande für Wien.",
  [("j",14)])
T("j-anfang","ber","Die Anfänge: 1907 bis 1917",
  "Vor der Berufsvormundschaft fehlte jede gesetzliche Jugendfürsorge über Vormundschaftsfragen hinaus. Auf die Zentralstelle für Kinderschutz von 1907 folgte 1912 der Beschluss zur Berufsvormundschaft. Der Ausbaubeschluss von 1917 gilt als Geburtstag des Wiener Jugendamtes, die Umsetzung folgte aber erst im Roten Wien.",
  [("j",9),("j",10),("j",15)])
T("j-beruf","ber","Wie der Frauenberuf entstand",
  "Der Beruf hat zwei Wurzeln: die Stellen der Gemeinde ab 1913 und das bürgerliche weibliche Ehrenamt. Die bürgerliche Frauenbewegung war der wesentliche Motor. Geistige Mütterlichkeit und Hilfe zur Selbsthilfe gelten als erste methodisch-theoretische Leitlinien.",
  [("j",11)])
T("j-arlt","ber","Arlts weiterer Weg",
  "Ilse Arlt studierte ohne Matura Nationalökonomie und Sozialwissenschaften. Wegen der jüdischen Herkunft ihrer Mutter erhielt sie 1938 Schreib- und Berufsverbot, die Schule wurde geschlossen. Ihre „Volkspflege“ meinte individuelle Hilfe und hat inhaltlich nichts mit dem späteren NS-Begriff gemein.",
  [("j",11),("j",12),("j",16)])
T("j-paket","rot","Das Wäschepaket als Politik",
  "Das Paket von 1927 wurde über die Pferderennsteuer finanziert und ging an alle Wiener Mütter. Die Fürsorgerin überbrachte als Beauftragte des Bürgermeisters die Glückwünsche der Stadt. In zwei Jahren wurden 54.739 Pakete übergeben.",
  [("j",19)])
T("j-amt","rot","Hierarchie im Bezirksjugendamt",
  "An der Spitze stand ein Jurist oder Rechtsfürsorger, Männer arbeiteten überwiegend im Innendienst. Die ausschließlich weiblichen Fürsorgerinnen waren vor allem im Außendienst. Diese Aufteilung blieb jahrzehntelang kaum hinterfragt, und die Hilfsfürsorgerinnen sollten den Kontakt zu den Müttern verbessern.",
  [("j",21),("j",22)])
T("j-eugenik","rot","Eugenik einordnen",
  "Eugenische Bewegungen gab es seit Ende des 19. Jahrhunderts in vielen Ländern und allen politischen Lagern. Im Roten Wien ging es vor allem um Geburtenförderung und um weniger Säuglingssterblichkeit. Tandler vertrat auch widersprüchliche Positionen, das soll aber nicht mit der NS-Vernichtungspolitik gleichgesetzt werden.",
  [("j",20)])
T("j-kuest","rot","Die KÜST aus Sicht der Kinder",
  "Frau Jindra kam als Kind dreimal in die KÜST, weil ihre Familie an Tuberkulose erkrankt war. Sie erinnert sich an einen „furchtbaren Glaspalast“, an Isolation und Einsamkeit. Auch die uniformierte Kleidung vom Jugendamt machte sie später als Pflegekind erkennbar und stigmatisierte sie.",
  [("j",25),("j",26)])
T("j-straf","rot","Jugendstrafrecht und Fürsorgeerziehung",
  "Bis 1928 fielen Jugendliche ab dem 14. Lebensjahr unter das Erwachsenenstrafrecht. Der Aufbau der Fürsorgeerziehung war entscheidend dafür, dass die Gefängnisstrafen für Jugendliche abgeschafft wurden. Das Wiener Modell erlangte in Österreich und Europa Vorbildcharakter.",
  [("j",27)])
T("j-aut","aut","Weniger Mittel, mehr Kirche",
  "Der enorme Anstieg der Not traf auf eine drastische Kürzung öffentlicher Mittel. Das Wäschepaket ging nur noch an „bedürftige“ Mütter. Das katholische Josefswerk beriet zu christlicher Ehe und führte gesundheitliche „Ehetauglichkeitsprüfungen“ durch, auch Absolventinnen der Ausbildung fanden kaum Stellen.",
  [("j",30),("j",31),("j",32)])
T("j-ns-struktur","ns","Dem Gesundheitsamt unterstellt",
  "Der Regimewechsel brachte keinen grundsätzlichen Bruch im Fürsorgesystem. Das Jugendamt wurde dem Gesundheitsamt unterstellt, um rassenhygienische Ideale wirksam umzusetzen. Der Erziehungsberater bekam große Macht über Heimeinweisungen, die bis in die 1970er nachwirkte.",
  [("j",35),("j",36)])
T("j-volkspfl","ns","Die „Volkspflegerin“",
  "Die neue Soziale Frauenschule diente der ideologischen Gleichschaltung einer neuen Generation. Die schulischen Voraussetzungen lagen deutlich unter jenen vor 1938, wichtig waren gute Gesundheit und „deutschblütige Abstammung“. Die Aufnahmeprüfung prüfte vor allem die politische Haltung.",
  [("j",37),("j",38)])
T("j-verantw","ns","Mitverantwortung",
  "Viele verstanden ihre Arbeit als Pflichterfüllung, und nicht alle identifizierten sich mit der Ideologie. Trotzdem war das Jugendamt laut Text letztlich mitverantwortlich an der Rassenpolitik. Die Fürsorgerinnen dürften mehrheitlich von Deportation und Vernichtung erfahren haben.",
  [("j",41)])
T("j-nach","nach","Neuanfang mit alten Mustern",
  "Aus der Verordnung von 1940 wurden nach 1945 nur offensichtliche NS-Bezüge gestrichen. Chancen auf einen Posten hingen laut Erzählungen auch von Beziehungen und politischer Protektion ab. Die Aufnahmebedingungen der Schulen wurden erhöht, weil das NS-Ausbildungsniveau gering gewesen war.",
  [("j",45),("j",46)])
T("j-taschengeld","nach","Das Taschengeld",
  "Um Nachwuchs zu gewinnen, gab das Jugendamt finanziell schwachen Schüler*innen Stipendien und ein Taschengeld. Daran hing die Pflicht, danach fünf Jahre im Amt zu arbeiten. Die Maßnahme erwies sich als kontraproduktiv und wurde erst mit dem Ansturm auf die Sozialakademien abgeschafft.",
  [("j",56),("j",65)])
T("j-parteien","nach","Aus Parteien sollen Klienten werden",
  "Case Work sollte bis 1960 zumindest theoretisch alle Bezirksjugendämter erreichen, die praktische Umsetzung dauerte aber lange. Die in der NS-Zeit eingeführte Aufteilung in Organisations- und Erziehungsfachfürsorgerin blieb bis 1971 bestehen. Erst dann wurde sie zur Leitenden Sozialarbeiterin zusammengelegt.",
  [("j",56),("j",57)])
T("j-wilhelm","nach","Spiegelgrund nach dem Krieg",
  "Ein Schreiben von 1950 zeigt die Kontinuität der Einrichtungen: Für schwer erziehbare Kinder, die noch am Spiegelgrund waren, sollte das Schloss Wilhelminenberg bereitgestellt werden. Im selben Schreiben geht es um 260 schlecht versorgte Pflegekinder im Jennersdorfer Bezirk.",
  [("j",49)])
T("j-wegen","sa","Der Wiener Weg",
  "Der „Wiener Weg der Jugendwohlfahrt“ sollte von Zwang und Kontrolle zu Freiwilligkeit und Beratung führen. Außenstellen und niederschwellige Angebote sollten die Angst nehmen, Hilfe zu holen, denn das Bild des Amtes war sehr negativ. In der Praxis hielten manche weiter an Kontrolle fest.",
  [("j",60)])
T("j-schock","sa","Zwischen Ideal und Wirklichkeit",
  "Viele junge Sozialarbeiter*innen erlebten beim Eintritt ins Amt einen „Entidealisierungsschock“. Konflikte gab es auch mit Sozialpädagog*innen und um die Einschätzung von Gefahr bei häuslicher Gewalt. Erst im Krisenzentrum FIDUZ wurde die lange Konkurrenz der Berufsgruppen überwunden.",
  [("j",66),("j",67),("j",74)])
T("j-titel","sa","Der lange Weg zum Berufstitel",
  "An den Schulen wurde schon „Sozialarbeit“ gelehrt, offiziell ersetzte der neue Titel die „Fürsorgerin“ laut Text aber erst 1981. Um den Mangel auszugleichen, stellte das Jugendamt 1968 zwanzig „Fürsorgeassistentinnen“ ein, die die Ausbildung nachholen mussten.",
  [("j",61),("j",64)])
T("j-clearing","sa","Regionalstellen und Clearing",
  "Bezirksjugendämter wurden zu Regionalstellen für Soziale Arbeit mit Familien, die Dezernate werden seit 1998 von der eigenen Berufsgruppe geleitet. Das Clearing löste das alte Sprengelmodell ab, nicht ohne Konflikt: Eine langjährige Mitarbeiterin hielt den Begriff für Klient*innen für irreführend.",
  [("j",69),("j",70)])
T("j-heim","sa","Warum die Großheime schließen mussten",
  "Eine Studie von 1992 zeigte negative Folgen der Heimunterbringung für die gesamte Biographie. Im selben Jahr stieg die Zahl der Abnahmen auf 1.000, die alte KÜST „platzte aus allen Nähten“. Der erste Tag der Fremdunterbringung soll nun auch der Beginn der Rückführungsarbeit sein.",
  [("j",73),("j",74)])
T("h-aufarbeitung","heute","Ein Amt stellt sich seiner Geschichte",
  "2010 wandten sich ehemalige Wiener Heimkinder an die Öffentlichkeit. Der „Weiße Ring“ übernahm Prüfung und Entschädigung, die Historikerkommission unter Reinhard Sieder die Aufarbeitung. Dazu kamen die Kommission Wilhelminenberg und eine Studie zu Pflegekindern an der FH Campus Wien.",
  [("j",77)])
T("h-folgen","heute","„Damit es sich nicht wiederholt“",
  "2013 lud das Jugendamt ehemalige Heim- und Pflegekinder unter diesem Motto zu einem Tag der offenen Tür. Seit 2012 gibt es verpflichtende jährliche interne Revisionen. Der Text betont, es gehe nun darum, strukturelle Probleme aufzudecken, nicht nur Fehler Einzelner zu suchen.",
  [("j",78)])
T("h-umf","heute","Unbegleitete minderjährige Flüchtlinge",
  "Flüchtlinge beschäftigten das Jugendamt immer wieder, etwa 1956 und 1968. Seit 1969 gehört die Betreuung unbegleiteter Minderjähriger zum Auftrag. 2003 entstand die „Drehscheibe“, seit 2004 obliegen dem Amt die Rechtsvertretung im Asylverfahren sowie die Unterbringung, und 2015 kam eine Koordinierungsstelle hinzu.",
  [("j",78)])
T("h-heute","heute","Kinder schützen, Eltern unterstützen",
  "Stärkung der Kinderrechte, Beteiligung und Transparenz sind aktuelle Leitlinien. Das Vier-Augen-Prinzip, die Gefährdungsabklärung und die Krisenzentren waren Wiener Neuerungen, die überwiegend in das Bundes-Kinder- und Jugendhilfegesetz eingingen. Die Autorin hält trotz der dunklen Flecken fest, dass sehr vielen Kindern geholfen wurde.",
  [("j",5),("j",7),("j",79)])
T("h-ambulant","heute","Neue Hilfen für Familien",
  "Neue Projekte gingen nach Begleitung und Evaluierung in den Regelbetrieb über: Mobile Arbeit mit Familien 2005, FIT-Familienintensivtraining 2007 und „Frühe Förderung“ 2008. Für Kinder auf dem Weg in ein Krisenzentrum entstand 2007 die Stofffigur MAG ELFE, und Besuchscafés erleichtern den Kontakt zu getrennten Eltern.",
  [("j",71),("j",75),("j",76)])

MC("j-kost",[],"Wie entwickelte sich die Zahl der Pflegekinder im Ersten Weltkrieg?","Von 4.732 im Jahr 1914 auf 8.325 im Jahr 1918",["Von 8.325 im Jahr 1914 auf 4.732 im Jahr 1918","Sie blieb bei rund 4.700 konstant","Von 1.010 auf 2.000"],"Weil Wiener Pflegeparteien fehlten, kam die Mehrheit aufs Land.")
TF("j-kost",[],"Max Winter schrieb über die alte Kinderübernahmsstelle, Wien habe „keine größere Schande“ als dieses Haus.",True,"Ein Kommissionsbericht nannte das Haus sogar eine „Mördergrube“.")
MC("j-anfang",[8],"Was fehlte vor der Berufsvormundschaft laut Text?","Eine gesetzliche Jugendfürsorge, die über Vormundschaftsfragen hinausging",["Jede Form privater Wohltätigkeit","Jede Vormundschaft über uneheliche Kinder","Ärzte in den Wiener Gebärkliniken"],"Es ging bis dahin nur um die wirtschaftliche Absicherung.",[("j",9)])
MC("j-anfang",[24],"Welches Datum nennt die Überschrift als Geburtstag des Wiener Jugendamtes?","Der Ausbaubeschluss vom 27. April 1917",["Die Wahl vom 4. Mai 1919","Der Beschluss vom 7. August 1912","Die Gründung des Wohlfahrtsamtes 1921"],"Im Fließtext stehen auch andere Tage im April, siehe Stolperfallen. Die Umsetzung gelang bis Kriegsende nur teilweise.",[("j",15)])
MC("j-beruf",[23],"Wie nennt der Text die „Berufspflegerin“ auch?","Eine „Erfindung der kommunalen Verwaltung“",["Eine Erfindung der Kirche","Eine Idee von Mary Richmond","Eine Vorgabe des Ministeriums"],"Parallel leitet sich der Beruf aber aus dem bürgerlichen weiblichen Ehrenamt ab.")
TF("j-beruf",[23],"Die bürgerliche Frauenbewegung war laut Text die zentrale gesellschaftspolitische Kraft für den weiblichen Fürsorgeberuf.",True,"Sie verhalf Frauen zu besseren Bildungs- und Berufsmöglichkeiten.")
MC("j-arlt",[5],"Wie unterscheidet sich Arlts „Volkspflege“ von der späteren NS-Fürsorge?","Sie meint individuelle Hilfe statt der Idee des „Volkskörpers“",["Sie war eine frühere Form derselben Rassenpflege","Sie galt nur für Männer im Staatsdienst","Sie lehnte jede wissenschaftliche Forschung ab"],"Die Begriffe waren semantisch ähnlich, aber inhaltlich diametral entgegengesetzt.",[("j",16)])
MC("j-arlt",[],"Was geschah 1938 mit Ilse Arlt?","Schule geschlossen, Schreib- und Berufsverbot",["Berufung an die neue Soziale Frauenschule","Emigration nach Chicago zu Addams","Leitung des Gaujugendamtes"],"Grund war die jüdische Herkunft mütterlicherseits.",[("j",12)])
TF("j-arlt",[5],"Arlts Schule war zugleich als Forschungseinrichtung konzipiert.",True,"Forschung und praktische Anwendbarkeit prägen auch ihre beiden Lehrbücher.",[("j",11),("j",12)])
MC("j-paket",[12,22],"Wie wurde das Säuglingswäschepaket von 1927 finanziert?","Über die Pferderennsteuer",["Über Spenden aus Amerika","Über den Waisenkinderfonds","Über Beiträge der Mütter"],"Ein Beispiel für die „Breitner-Luxussteuern“: Verteilung von oben nach unten.")
TF("j-paket",[22],"Die Fürsorgerin übergab das Paket als Beauftragte des Bürgermeisters mit den Glückwünschen der Stadt.",True,"Hilfe und Zugang zur Familie zugleich: „die Glückwünsche Wiens zur Ankunft des neuen Staatsbürgers“.")
MC("j-amt",[23],"Wie war die Arbeit im Bezirksjugendamt aufgeteilt?","Männer überwiegend im Innendienst, Fürsorgerinnen vor allem im Außendienst",["Frauen leiteten alle Ämter, Männer machten Hausbesuche","Männer und Frauen wechselten wöchentlich","Hausbesuche machten ausschließlich Ärzte"],"Diese Arbeitsteilung wurde jahrzehntelang kaum hinterfragt.",[("j",21)])
MC("j-amt",[10],"Warum gab es ab 1926 Hilfsfürsorgerinnen?","Der Kontakt zwischen bürgerlichen Fürsorgerinnen und Klientinnen sollte besser werden",["Die Fürsorgerinnen sollten nur noch im Amt sitzen","Ausländische Hilfsaktionen verlangten mehr Personal","Ärzte wollten weniger Untersuchungen"],"Sie stammten aus dem Arbeitermilieu, waren aber schlechter gestellt.",[("j",21),("j",22)])
TF("j-eugenik",[12],"Laut Text kann man die theoretischen Grundlagen der Fürsorge im Roten Wien mit der „negativen Eugenik“ des NS gleichsetzen.",False,"Der Text warnt ausdrücklich vor dieser Gleichsetzung, auch wenn Tandler problematische Begriffe verwendete.")
MC("j-eugenik",[12],"Wo gab es laut Text eugenische Bewegungen?","In vielen Ländern und innerhalb aller politischen Lager",["Nur im deutschsprachigen Raum","Nur in der Sozialdemokratie","Nur in der katholischen Kirche"],"Die Programme waren vor allem „positive Eugenik“, also Geburtenförderung.")
MC("j-kuest",[11],"Wie erinnert sich Frau Jindra an die KÜST?","Als „furchtbaren Glaspalast“, mit Isolation und Einsamkeit",["Als schönste Zeit ihrer Kindheit","Als gewöhnliche Schule im Bezirk","Sie war dort als Erzieherin tätig"],"Der Text stellt das gegen das zeitgenössische Lob als „Juwel“.",[("j",26)])
TF("j-kuest",[],"Die Kinder in der KÜST standen zugleich für kinderpsychologische Studien zur Verfügung.",True,"Charlotte Bühler und Hildegard Hetzer entwickelten auf dieser Basis Testverfahren.",[("j",25)])
MC("j-straf",[11,13],"Was änderte sich 1928 für Jugendliche?","Ein Jugendstrafrecht wurde verabschiedet",["Sie wurden ab 12 Jahren strafmündig","Alle Besserungsanstalten wurden erweitert","Sie erhielten das Wahlrecht"],"Bis dahin fielen sie ab dem 14. Lebensjahr unter das Erwachsenenstrafrecht.")
MC("j-aut",[14],"An wen ging das Säuglingswäschepaket im Austrofaschismus?","Nur noch an „bedürftige“ Mütter",["An alle Wiener Mütter","Nur an kinderreiche Väter","Nur an Mitglieder der Vaterländischen Front"],"Ein Beispiel für die Rücknahme des allgemeinen Anrechts.",[("j",31)])
MC("j-aut",[14],"Welche Prüfungen fanden im Rahmen der katholischen Eheberatung statt?","Gesundheitliche „Ehetauglichkeitsprüfungen“",["Kostenlose Führerscheinprüfungen","Prüfungen im Fach Volkswirtschaft","Aufnahmeprüfungen für die Pichlschule"],"Das Josefswerk beriet in rechtlichen und seelsorgerischen Fragen zur christlichen Ehe.",[("j",31)])
TF("j-aut",[14],"Auch Absolventinnen der Fürsorgeausbildung waren in der Krise von Arbeitslosigkeit betroffen.",True,"Im öffentlichen Dienst gab es keine freien Stellen für Fürsorgerinnen.",[("j",32)])
MC("j-ns-struktur",[15],"Warum wurde das Jugendamt dem Gesundheitsamt unterstellt?","Primär zur wirksamen Umsetzung rassenhygienischer Ideale",["Weil es zu wenige Ärzte gab","Um Geld für Kindergärten zu sparen","Auf Wunsch der Fürsorgerinnen"],"Fürsorgerinnen arbeiteten dadurch zugleich in der Gesundheitsfürsorge.",[("j",35)])
TF("j-ns-struktur",[15],"Der Regimewechsel 1938 bewirkte laut Text grundsätzlich einen Bruch mit dem bisherigen Fürsorgesystem.",False,"Einrichtungen bestanden mehr oder weniger weiter. Entscheidend war die neue ideologische Ausrichtung.",[("j",35)])
MC("j-ns-struktur",[16,18],"Welche Macht bekam der Erziehungsberater im NS?","Seine Gutachten entschieden mit über die Unterbringung",["Er durfte Gesetze erlassen","Er leitete die Polizei","Er hatte keinerlei Einfluss"],"Das bestimmte die Praxis der Heimeinweisungen bis in die 1970er Jahre mit.",[("j",36)])
MC("j-volkspfl",[15],"Worauf zielte die Aufnahmeprüfung der Sozialen Frauenschule im NS?","Primär auf die politisch-ideologische Haltung",["Vor allem auf Fremdsprachen","Auf die Kenntnis von Arlts Schriften","Auf Erfahrung in Psychoanalyse"],"Die schulischen Voraussetzungen lagen deutlich unter jenen vor 1938.",[("j",38)])
MC("j-volkspfl",[15],"Was geschah 1943 mit dem Begriff „Heim“?","Er wurde neuerlich festgesetzt, was der Text zynisch nennt",["Er wurde durch „Akademie“ ersetzt","Er wurde erstmals überhaupt verwendet","Er wurde für alle Schulen vorgeschrieben"],"Rotes Wien: „Heim“. Ständestaat: wieder „Anstalt“. Ab 1. April 1943 wieder „Heim“.",[("j",37)])
TF("j-volkspfl",[15],"Die Einführung der Hilfsfürsorgerinnen erwies sich im NS als verhängnisvoll, weil Hauptfürsorgerinnen auf diesen Status herabgesetzt wurden.",True,"Beide Kategorien wurden vereinheitlicht.",[("j",38)])
TF("j-verantw",[15],"Laut Text war das Wiener Jugendamt an der Umsetzung der NS-Rassenpolitik letztlich durchaus mitverantwortlich.",True,"Das gilt auch, wenn nicht alle sich mit der Ideologie identifizierten und viele die Arbeit als Pflichterfüllung sahen.")
MC("j-verantw",[16],"Woran erfuhren Fürsorgerinnen spätestens von der Vernichtung?","Wenn dem Jugendamt der Tod eines Mündels übermittelt wurde",["Durch offizielle Rundschreiben an alle Bürger","Durch Berichte in der Arbeiterzeitung","Erst durch Prozesse nach 1945"],"Das Jugendamt musste dann die Eltern verständigen, was eine Fürsorgerin im Rückblick makaber nennt.")
MC("j-nach",[17],"Was änderte sich 1945 an der Jugendwohlfahrtsverordnung von 1940?","Gestrichen wurden nur offensichtliche ideologische NS-Bezüge",["Sie wurde vollständig aufgehoben","Sie wurde durch das Heimatrecht ersetzt","Sie galt nur noch für Pflegekinder"],"Sie blieb gesetzliche Grundlage der öffentlichen Jugendwohlfahrt.",[("j",45)])
TF("j-nach",[17],"Nach 1945 wurden die Aufnahmebedingungen der Fürsorgeschulen erhöht, unter anderem wegen des geringen Niveaus der NS-Ausbildung.",True,"Verlangt wurden etwa die Vollendung des 18. Lebensjahres und eine Aufnahmeprüfung.",[("j",46)])
MC("j-taschengeld",[],"Woran war das Taschengeld für Schüler*innen geknüpft?","An fünf Jahre Arbeit im Jugendamt nach der Ausbildung",["An den Eintritt in eine Partei","An ein Studium im Ausland","An den Verzicht auf den Berufstitel"],"Alle befanden, eine Stellung „quasi als Leibeigener“ sei nicht erstrebenswert.")
MC("j-parteien",[26],"Welche Idee steht hinter „aus Parteien sollen Klienten werden“?","Case Work: ein anderes Verhältnis zu den Menschen im Amt",["Mitarbeiter*innen sollen Parteimitglieder werden","Jugendämter sollen politisch neutral wählen","Klient*innen sollen Gebühren zahlen"],"Die praktische Umsetzung ließ laut Text noch lange auf sich warten.",[("j",56)])
MC("j-parteien",[17],"Bis wann blieb die NS-Teilung in Organisations- und Erziehungsfachfürsorgerin bestehen?","Bis 1971",["Bis 1945","Bis 1954","Bis 2002"],"Dann wurden beide Aufgaben in der Leitenden Sozialarbeiterin zusammengelegt.",[("j",57)])
TF("j-wilhelm",[17],"Ein Schreiben von 1950 sieht das Schloss Wilhelminenberg für schwer erziehbare Kinder vor, die noch am Spiegelgrund waren.",True,"Das zeigt, wie Einrichtungen auch nach dem Krieg weiterliefen.")
MC("j-wegen",[25,20],"Was ist der „Wiener Weg der Jugendwohlfahrt“?","Von Zwang und Kontrolle zu Freiwilligkeit und Beratung",["Von Pflegefamilien zurück zu Großheimen","Von der Beratung zur strengen Nachschau","Von der Stadt Wien zur Bundesverwaltung"],"Kontrollierende Eingriffe sollten nur noch im äußersten Notfall stattfinden.")
TF("j-wegen",[25],"Ab den 1970ern gab es in der Praxis keine alten Kontrolltraditionen mehr.",False,"Mitunter wurde weiter daran festgehalten, viele Großheime blieben bis Mitte der 1970er autoritär.")
MC("j-schock",[25],"Was erlebten viele junge Sozialarbeiter*innen beim Eintritt ins Amt?","Einen „Entidealisierungsschock“",["Sofortige Beförderung zur Amtsleitung","Weniger Arbeit als im Studium erwartet","Ein Amt ganz ohne Hierarchie"],"Die Realität lag weit von ihren Vorstellungen entfernt.",[("j",66)])
MC("j-schock",[],"Wo wurde die lange Konkurrenz von Sozialarbeit und Sozialpädagogik erstmals überwunden?","Im Krisenzentrum FIDUZ, wo beide erstmals zusammenarbeiteten",["In der Stadt des Kindes","In der Kinderstube von 1926","In der KÜST ab 1925"],"Multiprofessionelle Teams sind seither Standard.",[("j",74)])
MC("j-titel",[24],"Wann ersetzte der neue Berufstitel laut Zusatztext offiziell die „Fürsorgerin“?","1981",["1912","1945","2002"],"Andere Unterlagen nennen 1968 und 1976, siehe Stolperfallen.",[("j",61)])
MC("j-titel",[24],"Was waren die 1968 eingestellten „Fürsorgeassistentinnen“?","Kräfte, die die Ausbildung binnen fünf Jahren berufsbegleitend nachholen mussten",["Ärztinnen in Mutterberatungsstellen","Sekretärinnen der Amtsleiter","Praktikantinnen ohne Bezahlung"],"So sollte der anhaltende Personalmangel ausgeglichen werden.",[("j",64)])
MC("j-clearing",[],"Was löste das Clearingmodell ab?","Das alte Sprengelmodell",["Das Vieraugenprinzip","Die Krisenzentren","Die Paar- und Familienberatung"],"Die Aufgabenteilung wurde in den 1990er Jahren in Ottakring erprobt.",[("j",70)])
MC("j-heim",[20],"Was zeigte die Studie zur Heimunterbringung von 1992?","Negative Folgen für die Gesamtbiographie ehemaliger Heimkinder",["Dass Großheime Kosten sparen","Dass Heime bei Kindern beliebt sind","Dass keine Reform nötig ist"],"Die Ablehnung richtete sich gegen das System Heim selbst.",[("j",73)])
TF("j-heim",[20],"Heute soll der erste Tag der Fremdunterbringung auch der Beginn der Rückführungsarbeit zu den Eltern sein.",True,"Das passt zum Motto „so kurz wie möglich“.",[("j",74)])
MC("j-heim",[],"Wie modifizierte eine Sozialpädagogin Tandlers Satz für die Zeit nach der KÜST?","„Wer Kindern Wohngemeinschaften und Krisenzentren baut, reißt Heimmauern nieder“",["„Wer Kindern Heime baut, spart Paläste“","„Wer Kindern Häuser baut, braucht keine Eltern“","„Wer Kindern Kasernen baut, schützt die Stadt“"],"Die KÜST wurde 1999 geschlossen, einst als „Juwel“ gefeiert.",[("j",73)])
MC("h-aufarbeitung",[],"Was begann 2010?","Ehemalige Wiener Heimkinder machten ihre Gewalterfahrungen öffentlich",["Die erste Heimreform in Wien","Die Schließung der KÜST","Der Modellversuch in Hernals"],"Daraufhin wurden der Weiße Ring und die Historikerkommission eingesetzt.")
MATCH("h-aufarbeitung",[],"Wer übernahm was bei der Aufarbeitung?",[("Weißer Ring","Prüfung und Entschädigungszahlungen"),("Reinhard Sieder","Historikerkommission zur Heimerziehung"),("Barbara Helige","Kommission Wilhelminenberg"),("FH Campus Wien","Untersuchung zu Pflegekindern")],"Viele ehemalige Heimkinder nahmen zudem Einsicht in ihre Kinderakten.")
MC("h-folgen",[],"Was wurde 2012 in sozialpädagogischen Einrichtungen eingeführt?","Verpflichtende jährliche interne Revisionen",["Das Taschengeld für Jugendliche","Die Puppenadoption","Das Fürsorgebuch"],"Es geht darum, strukturelle Probleme aufzudecken.")
TF("h-folgen",[],"Das Motto des Tags der offenen Tür 2013 lautete „Damit es sich nicht wiederholt“.",True,"Eingeladen waren ehemalige Heim- und Pflegekinder.")
MC("h-umf",[],"Was obliegt dem Jugendamt seit der Grundversorgung von 2004?","Rechtsvertretung im Asylverfahren und Unterbringung",["Die Abschiebung Minderjähriger","Nur die Ausstellung von Reisepässen","Gar keine Aufgaben mehr"],"Die Betreuung übernahm laut Text der Fonds Soziales Wien.")
ORD("h-umf",[],"Reihe die Schritte bei unbegleiteten Minderjährigen.",[("1969","Betreuung wird zusätzlicher Arbeitsauftrag"),("2003","„Drehscheibe“ für Krisenaufnahme"),("2004","Grundversorgung tritt in Kraft"),("2015","Koordinierungsstelle in der MAG ELF")],"Flüchtlinge waren nach beiden Weltkriegen und danach wiederholt eine zentrale Aufgabe.")
MC("h-heute",[20,21],"Wie lautet das heutige Motto der Wiener Kinder- und Jugendhilfe?","„Kinder schützen, Eltern unterstützen“",["„Erst die Familie, dann das Amt“","„Erfassen und erheben“","„Familie ist Privatsache“"],"Das Vorwort nennt dazu Kinderrechte, Beteiligung und Transparenz.",[("j",5),("j",7)])
TF("h-heute",[20],"Das Vier-Augen-Prinzip und die Krisenzentren gelten laut Vorwort als Wiener Innovationen.",True,"Sie fanden überwiegend Eingang in das Bundes-Kinder- und Jugendhilfegesetz.",[("j",7)])
MC("h-ambulant",[],"Was ist das FIT-Familienintensivtraining?","Aufsuchende und reflexive Erziehungsberatung",["Ein Sportangebot für Heimkinder","Eine Prüfung für Pflegeeltern","Eine Kontrolle durch die Polizei"],"Es entstand 2007 aus einem Pilotprojekt.",[("j",76)])

COURSE = dict(
    id="geschichte",
    name="Geschichte der Sozialen Arbeit",
    lecturer="FH-Hon.Prof.in Mag.a Dr.in Gudrun Wolfgruber-Thanel",
    term="WS 2026/27",
    exams=[dict(id="vz", label="Vollzeit (VZ)", date="2026-11-04"), dict(id="bb", label="Berufsbegleitend (BB)", date="2026-11-12")],
)
