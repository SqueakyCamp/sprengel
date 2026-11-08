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

MC("gr-netze",[1],"Welche Ebene sozialer Absicherung verbindet die Einführung ausdrücklich mit dem Subsidiaritätsprinzip?","Familie und Ehrenamt",["Staatliche Sozialleistungen","Leistungen der Länder","Leistungen der Gemeinden"],"Die Einführung unterscheidet drei Ebenen sozialer Absicherung: staatliche Sozialleistungen, Leistungen von Ländern und Gemeinden sowie Familie und Ehrenamt. Das Subsidiaritätsprinzip gehört zur dritten Ebene: Zuerst sollen Familie und freiwillige Helfer*innen einspringen, erst danach öffentliche Stellen. Dieses Prinzip begegnet dir in der Armenfürsorge der Monarchie wieder.")
MC("gr-begriffe",[],"Wie lautet die grob vereinfachte Unterscheidung?","Sozialarbeit hilft erzieherisch, Sozialpädagogik erzieht helfend",["Sozialarbeit erzieht strafend, Sozialpädagogik berät freiwillig","Sozialarbeit betreut Erwachsene, Sozialpädagogik nur Kinder","Sozialarbeit ist ehrenamtlich, Sozialpädagogik ist bezahlt"],"So steht es in der Einführung: Sozialarbeit hilft erzieherisch und ist eher fürsorgerisch-sozialpolitisch, Sozialpädagogik erzieht helfend und ist eher pädagogisch-sozialerzieherisch. Die Unterscheidung ist bewusst grob, weil die Begriffe und Felder historisch nicht konstant waren. Darum verfolgt die LV einen Konvergenzansatz.")
TF("gr-begriffe",[],"Die Vorlesung arbeitet mit einem Differenzansatz zwischen Sozialarbeit und Sozialpädagogik.",False,"Die Folie sagt das Gegenteil: Die LV verfolgt einen Konvergenzansatz statt eines Differenzansatzes. Sozialarbeit und Sozialpädagogik werden also als zusammenwachsende Felder betrachtet, nicht als streng getrennte Disziplinen. Das passt dazu, dass Begriffe und Arbeitsfelder sich im Lauf der Geschichte immer wieder verschoben haben.")
MC("gr-quellen",[],"Warum müssen historische Quellen laut LV kontextualisiert werden?","Quellen sind immer auch Deutungen",["Quellen sind meist gefälscht","Es gibt erst ab 1945 Quellen","Nur Gesetze gelten als Quelle"],"Quellen sind nie neutral, sie sind immer auch Deutungen. Darum fragt man: Wer hat sie verfasst, wann und zu welchem Zweck? Akten zeigen den Blick der Behörde, Zeitzeug*innenberichte den Blick der Betroffenen; erst im Kontext ergeben sie ein Bild.")
TF("gr-quellen",[],"Gesetzestexte zeigen zuverlässig, wie die Fürsorge in der Praxis ablief.",False,"Gesetzestexte geben wenig Information über die Praxis, sie spiegeln vor allem die Intentionen von Behörden und Gesetzgebung. Wie die Fürsorge tatsächlich ablief, zeigen eher Akten, Berichte und Erinnerungen von Betroffenen. Darum ist die Kontextualisierung so wichtig.",[("e",16)])
MULTI("gr-mandat",[19],"Welche Begriffe verwendet die Einführung, um den Ausgangspunkt Sozialer Arbeit zu beschreiben?",["Hilfestellung","Disziplinierung","Kontrolle"],["Gewinnorientierung","Selbstverwaltung"],"Die Einführung beschreibt Soziale Arbeit als Reaktion auf problematische Lebenslagen. Sie war von Anfang an beides: Hilfestellung, aber auch Disziplinierung und Kontrolle. Diese Spannung heißt doppeltes Mandat und zieht sich durch alle Epochen, von der Armenfürsorge bis heute.",[("e",19)])
MULTI("gr-mandat",[],"Welche Bewegungen haben laut Einführung die Soziale Arbeit historisch geprägt?",["Arbeiter*innenbewegung","Frauenrechtsbewegung","Jugendbewegung","1968er Bewegung"],["Friedensbewegung der 1920er"],"Neben den genannten Bewegungen nennt die Einführung auch die Frauenbewegung der 1970er/80er Jahre. Soziale Bewegungen haben immer wieder neue Problemlagen sichtbar gemacht und neue Angebote erzwungen. Die bürgerliche Frauenbewegung etwa trieb die Verberuflichung der Fürsorge voran.",[("e",20)])
MC("gr-pruefung",[],"Wie viele Überblicksfragen enthält die schriftliche Prüfung?","7",["5","10","26"],"Die schriftliche Prüfung hat 7 Überblicksfragen in 90 Minuten; dazu kommt eine schriftliche Reflexion mit mindestens 3500 Zeichen. Die 26 Leitfragen sind der Fragenkatalog zur Vorbereitung, die Prüfungsfragen kommen aus diesem Pool. Basis sind Präsentationen, Zeittafel und Zusatztexte.")
MC("gr-netze",[],"Seit wann gibt es laut Einführung soziale staatliche Absicherung und soziale Netze?","Erst seit Mitte des 19. Jahrhunderts",["Seit dem Mittelalter","Erst seit 1945","Seit der Römerzeit"],"Soziale Netze und staatliche Absicherung sind relativ junge Errungenschaften und haben sich erst Mitte des 19. Jahrhunderts entwickelt. Davor waren Familie, Kirche und private Wohltätigkeit zuständig. Soziale Arbeit hängt bis heute an der Frage, ob es einen rechtlichen Anspruch auf Hilfe gibt.",[("e",8)])

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

MC("mon-heimat",[4],"Was gewährte das Heimatrechtsgesetz von 1863 den Heimatberechtigten?","Ungestörten Aufenthalt und Anspruch auf Armenversorgung",["Eine staatliche Pension und freie Wohnungswahl","Das Wahlrecht und einen fixen Unterhaltsbetrag","Eine Ausbildung und freie Arbeitsplatzwahl"],"Das Heimatrechtsgesetz von 1863 war die Basis des Armenwesens. Nur wer in einer Gemeinde heimatberechtigt war, hatte dort das Recht auf ungestörten Aufenthalt und Anspruch auf Armenversorgung; alle anderen konnten in ihre Heimatgemeinde abgeschoben werden. Einen einklagbaren Rechtsanspruch auf Versorgung gab es trotzdem nicht.")
MC("mon-heimat",[4],"Welchem Zweck diente das Heimatgesetz laut Folie vor allem?","Präventive Abschottung vor Armenversorgungsansprüchen",["Förderung der Zuwanderung nach Wien","Schaffung eines Rechtsanspruchs für alle Armen","Aufbau einer staatlichen Sozialversicherung"],"Das Heimatrecht war vor allem eine präventive Abschottung: Ein Großteil der Armen, etwa zugezogene Arbeiter*innen, fiel aus den Regelungen heraus. So hielten die Gemeinden ihre Kosten gering. Auch die Novelle von 1896 änderte daran wenig.",[("a1",8)])
MC("mon-heimat",[4],"Was änderte die Novelle des Heimatrechts von 1896?","Heimatrecht nach zehn Jahren ununterbrochenem Aufenthalt",["Heimatrecht für alle in Wien Arbeitenden ab dem ersten Tag","Abschaffung des Heimatrechts in allen Gemeinden","Heimatrecht nur noch durch Geburt in der Gemeinde"],"Die Novelle von 1896 brachte das Ersitzungsprinzip: Heimatrecht gab es nun auch nach zehn Jahren ununterbrochenem Aufenthalt, nicht mehr nur durch Geburt oder Heirat. Den Nachweis schafften aber vor allem sozial stabile Facharbeiter*innen. Wer oft umziehen musste, blieb weiter ausgegrenzt.",[("a1",9)])
MULTI("mon-heimat",[4],"Für wen war der Aufenthaltsnachweis nach dem Ersitzungsprinzip besonders schwierig?",["Bettgeher*innen","Saisonarbeiter*innen","Tagelöhner*innen","Dienstbot*innen"],["Facharbeiter in stabiler Anstellung"],"Zehn Jahre ununterbrochener Aufenthalt waren für mobile, arme Menschen kaum nachweisbar, weil sie oft Wohnung und Arbeit wechseln mussten. Sozial stabilere Facharbeiterkreise waren die Ausnahme. Die anderen blieben häufig rechtlich und sozial ausgegrenzt.",[("a1",9)])
TF("mon-heimat",[4],"Auf die Armenversorgung nach dem Heimatrechtsgesetz bestand ein Rechtsanspruch.",False,"Die Folie hält fest: Ein Rechtsanspruch auf Armenversorgung bestand nicht. Heimatberechtigte hatten zwar Anspruch auf Aufenthalt und Versorgung, durchsetzen konnten sie ihn aber nicht. Erst das Rote Wien sprach von einem allgemeinen Anrecht auf Fürsorge.",[("a1",7)])
TF("mon-heimat",[4,3],"Laut Resümee der Folie dienten Gesetz und Reform der Geringhaltung der Gemeindekosten.",True,"Genau so lautet das Resümee zur Novelle von 1896: Gesetz und Reform dienten der Geringhaltung der Gemeindekosten. Das Ersitzungsprinzip öffnete den Zugang nur scheinbar, weil die meisten Armen die zehn Jahre nicht nachweisen konnten.",[("a1",9)])
MC("mon-subs",[1],"Wann bestand nach dem Subsidiaritätsprinzip eine Versorgungspflicht der Gemeinde?","Wenn keine gesetzlich verpflichteten Personen zur Verfügung standen",["Sobald eine Person in der Gemeinde wohnte","Wenn eine Person dies schriftlich beantragte","Immer dann, wenn der Staat es anordnete"],"Nach dem Subsidiaritätsprinzip sprang die Gemeinde erst ein, wenn keine gesetzlich verpflichteten Personen zur Verfügung standen. Vorrangig zuständig waren Verwandte, Ehegatten und Vormünder, danach private Vereine und Stiftungen. Das hielt die öffentlichen Kosten niedrig.",[("a1",7)])
MC("mon-subs",[1],"Wer übernahm die Armenversorgung, bevor die Gemeinde eintrat?","Private Vereine und Stiftungen",["Das Ministerium für Soziale Fürsorge","Die staatliche Arbeitslosenversicherung","Die Bezirksjugendämter"],"Vor der Gemeinde kamen private Vereine und Stiftungen. Erst wenn diese privaten Träger finanziell überfordert waren, trat die Gemeinde ein. Das ist das Subsidiaritätsprinzip, das die ganze Armenfürsorge der Monarchie prägte.",[("a1",7)])
TF("mon-subs",[1],"In der offenen Armenkinderpflege waren zuerst Familie oder Verwandte zuständig.",True,"In der offenen Armenkinderpflege waren zuerst Familie oder Verwandte zuständig. Erst nach einer Überprüfung gab es öffentliche Erziehungs-, Waisen- und Kostgelder. Auch hier zeigt sich das Subsidiaritätsprinzip.",[("a1",27)])
TF("mon-epochen",[2],"In der christlichsozialen Ära gab es erstmals einen einheitlichen gesamtstaatlichen Versorgungsanspruch.",False,"Auch in der christlichsozialen Ära 1895 bis 1918 gab es „weiterhin keinen“ einheitlichen gesamtstaatlichen Anspruch. Neuerungen gab es vor allem im Gesundheitswesen, die fehlende Versorgung kompensierten Private und Familien. Ein allgemeines Anrecht auf Fürsorge kam erst mit dem Roten Wien.",[("a1",4)])
MATCH("mon-epochen",[2,3],"Ordne die Merkmale den Ären zu.",[("Liberale Ära","„Jeder muss sich selbst helfen“"),("Christlichsoziale Ära","Neuerungen im Gesundheitswesen"),("Rotes Wien","Allgemeines Anrecht auf Fürsorge"),("Austrofaschismus","Rücknahme des Anrechts auf Fürsorge")],"Das Subsidiaritätsprinzip prägt die Monarchie: In der liberalen Ära galt „Jeder muss sich selbst helfen“, die christlichsoziale Ära brachte Neuerungen im Gesundheitswesen. Das Rote Wien bricht damit und spricht vom allgemeinen Anrecht auf Fürsorge. Der Austrofaschismus nimmt diesen Bruch wieder zurück.",[("a1",3),("a1",4),("rw",9),("t",5)])
MC("mon-epochen",[3],"Welcher Grundsatz galt laut Folie insbesondere in den Städten?","„Überleben kann nur, wer arbeitet.“",["„Arbeit ist Privatsache.“","„Die Gemeinde sorgt für alle.“","„Jedem nach seinen Bedürfnissen.“"],"In den Städten galt der Grundsatz „Überleben kann nur, wer arbeitet“. Hinzu kam das Interesse an der Aufrechterhaltung der öffentlichen Ordnung: Arme, Bettler*innen und Arbeitslose galten als Gefahr. Hilfe war daher eng mit Arbeitspflicht und Kontrolle verbunden.",[("a1",5)])
MC("mon-armut",[3],"Wie deuteten das katholische und das liberale Lager Armut?","Als selbstverschuldet, als „Charakterschwäche“",["Als politische Frage der Verteilung","Als unvermeidliche Folge von Krankheit","Als staatliches Versagen"],"Katholisches und liberales Lager sahen Armut als selbstverschuldet, als „Charakterschwäche“; der Diskurs folgte sittlich-moralischen Kriterien. Ausnahme waren krankheitsbedingte Ursachen. Die Sozialdemokratie dagegen sah in der sozialen Frage eine politische Frage.",[("a1",6)])
MC("mon-armut",[3],"Was sahen die Zwangsarbeitergesetze von 1885 vor?","Anhaltung in Zwangsarbeits- und Besserungsanstalten",["Einen Arbeitsplatz für jede arbeitslose Person","Eine Versicherung gegen Arbeitsunfälle","Verpflichtende Lehrstellen für Waisen"],"Die Zwangsarbeitergesetze von 1885 sahen die Anhaltung in Zwangsarbeits- und Besserungsanstalten vor. Grund konnten eine Verurteilung wegen Landstreicherei, Bettelei oder „Arbeitsscheu“ sein. Das ist die Kriminalisierung von Armut, mitten in einer Zeit hoher Arbeitslosigkeit.",[("a1",11)])
TF("mon-armut",[3],"Die Sozialdemokratie sah in der sozialen Frage eine politische Frage und forderte Sozialreformen.",True,"Die Sozialdemokratie sah in der sozialen Frage eine politische Frage und forderte Sozialreformen. Damit grenzte sie sich vom katholischen und liberalen Lager ab, die Armut moralisch als Charakterschwäche deuteten. Ihr Kommunalprogramm von 1896 wurde später zur Grundlage des Roten Wien.",[("a1",6)])
MC("mon-armut",[],"Welcher Widerspruch prägte die große Depression ab 1873?","Arbeitslosigkeit stieg stark an und wurde zugleich als „arbeitsscheu“ gedeutet",["Löhne stiegen stark, doch niemand wollte arbeiten","Die Gemeinden hatten viel Geld, aber keine Armen","Die Armen wanderten ab, die Anstalten blieben voll"],"Die große Depression 1873 bis 1896 begann mit dem Börsenkrach; Arbeitslosigkeit und Mobilität stiegen stark. Trotzdem wurden Arme als „arbeitsscheu“ gedeutet und ab 1885 kriminalisiert. Eine wirtschaftliche Krise wurde also moralisch bewertet und bestraft.",[("a1",10),("a1",11)])
MATCH("mon-formen",[3],"Offen oder geschlossen?",[("Armenanstalten mit Arbeitspflicht","geschlossene Fürsorge"),("Vorübergehende Geldaushilfen","offene Fürsorge"),("Lainzer Versorgungshaus","geschlossene Fürsorge"),("Mietzinsbeihilfen","offene Fürsorge")],"Geschlossene Fürsorge fand in einer Anstalt statt, etwa in Armenanstalten mit Arbeitspflicht oder im Lainzer Versorgungshaus. Offene Fürsorge war Unterstützung außerhalb, etwa vorübergehende Geldaushilfen oder Mietzinsbeihilfen. Beide sollten nur das „Notdürftigste“ abdecken.",[("a1",19),("a1",20),("a1",21)])
MC("mon-formen",[3],"Was war Voraussetzung für Hilfen in der offenen Armenfürsorge?","Verkauf der letzten eigenen Wertgegenstände",["Ein Jahr Mitgliedschaft in einer Gewerkschaft","Bestätigung des Pfarrers über gute Sitten","Eintritt in eine Armenanstalt"],"Offene Armenfürsorge, also vorübergehende Geldaushilfen, gab es oft erst nach dem Verkauf der letzten eigenen Wertgegenstände. Die Maßnahme sollte dazu beitragen, dass die Betroffenen möglichst ohne Unterstützung der Gemeinde überleben. Hilfe war also abschreckend gestaltet.",[("a1",20)])
MC("mon-formen",[3],"Welcher Satz fasst die Haltung der geschlossenen Armenpflege zusammen?","„Wer nicht arbeitet, soll auch nicht essen“",["„Wer Kindern Paläste baut, reißt Kerkermauern nieder“","„Die Gesellschaft ist ihr Sachwalter“","„So kurz wie notwendig“"],"„Wer nicht arbeitet, soll auch nicht essen“ fasst die Haltung der geschlossenen Armenpflege zusammen: Anstalten mit Arbeitspflicht, Unterstützung nur für das „Notdürftigste“. Die anderen Sätze stammen aus späteren Epochen. Die Fürsorge hatte damit klar sozialdisziplinierenden Charakter.",[("a1",19)])
MC("mon-unsicht",[3],"Was war das Ziel der Verlegung Armer in Anstalten an der Peripherie?","Armut aus dem Blickfeld zu bringen",["Bessere Luft zur Heilung aller Kranken","Billiger Boden für neue Gemeindebauten","Nähe zu Arbeitsplätzen in der Industrie"],"Aus Angst vor der Berührung mit Armut setzte man auf Wegsperren und Verstecken: Unsichtbarmachung des Elends. Anstalten wurden ausgebaut und in die Peripherie verlegt, etwa das Lainzer Versorgungshaus. Sie blieben trotzdem bis zum Ersten Weltkrieg überfüllt.")
MC("mon-unsicht",[],"Welche Funktion hatte das Lainzer Versorgungshaus von 1904?","Zentralstelle der geschlossenen Armenpflege für Personen über 14",["Erste Schule für Fürsorgerinnen in Wien","Heim für verlassene Säuglinge","Sitz der städtischen Berufsvormundschaft"],"Das Lainzer Versorgungshaus von 1904 war ein großer Armenhauskomplex und Zentralstelle der geschlossenen Armenpflege für Personen über 14. Von dort wurden Menschen auf andere Anstalten verteilt, daher die „Drehscheibenfunktion“. Es steht für die Verlagerung der Armut an den Stadtrand.")
MC("mon-obdach",[],"Was bedeutet „Bettgeher*innentum“?","Mehrere Personen nutzen dasselbe Bett, ohne Mietvertrag",["Kranke werden zu Hause von Ärzten besucht","Arme schlafen in städtischen Notspitälern","Kinder werden zu Pflegefamilien verschickt"],"Bettgeher*innen nutzten dasselbe Bett nacheinander, ohne eigenen Mietvertrag. Das war eine Folge der „Wucherzinse“, also der extrem hohen Mieten. Statt Wohnungspolitik gab es Obdachlosenfürsorge mit bewusst abschreckenden Massenquartieren.",[("a1",15)])
TF("mon-obdach",[4],"Die Mehrheit der Obdachlosen in Wien war dort heimatberechtigt.",False,"Die Mehrheit der Obdachlosen war nicht in Wien heimatberechtigt, meist jung, ledig und vorwiegend männlich. Damit hatten sie keinen Anspruch auf Armenversorgung in Wien und konnten abgeschoben werden. Hier wirkt das Heimatrecht als Ausschluss.",[("a1",15)])
TF("mon-vers",[],"Die Sozialversicherung der Zeit galt nur für Lohnarbeiter*innen, sie sparte damit einen großen Teil der Armen aus.",True,"Kranken- und Unfallversicherung der 1880er Jahre galten nur für Lohnarbeiter*innen und wurden von Arbeiter- und Unternehmerseite finanziert. Damit trennten sich Arbeiter*innen- und Armenpolitik. Die Versicherung war bescheiden, aber weniger diskriminierend als die Armenhilfe, die alle anderen weiter traf.",[("a1",13)])
MULTI("mon-vers",[],"Was kam vor 1918 trotz Debatten nicht zustande oder fehlte?",["Staatliche Arbeitslosenversicherung","Witwen- und Waisenversicherung","Alters- und Invaliditätssicherung"],["Kranken- und Unfallversicherung"],"Damals existierten nur Kranken- und Unfallversicherung, finanziert aus Beiträgen. Eine Alters-, Invaliditäts- oder Arbeitslosenversicherung fehlte trotz Debatten. Wer alt, invalid oder arbeitslos war, fiel auf die diskriminierende Armenfürsorge zurück.",[("a1",13)])
MC("mon-vers",[],"Mit welchen Methoden sollte die soziale Frage laut Folie bearbeitet werden?","Individualisierung, Pädagogisierung, Medikalisierung",["Verstaatlichung, Enteignung, Umverteilung","Mitbestimmung, Selbstverwaltung, Streik","Digitalisierung, Automatisierung, Auslagerung"],"Die soziale Frage sollte durch Individualisierung, Pädagogisierung und Medikalisierung bearbeitet werden: Armut wurde als Problem einzelner Menschen gesehen, die man erziehen oder behandeln muss. Daraus ergibt sich eine Kontinuität der Fürsorge, die Verknüpfung von Hilfe, Schutz und Kontrolle.",[("a1",14)])
MC("mon-kinder",[],"Welches Interesse stand in der Kinder- und Jugendfürsorge vor 1900 im Vordergrund?","Kontrollieren und möglichst billig verwahren",["Individuelle Förderung aller Begabungen","Psychoanalytische Beratung der Eltern","Rückführung in die Herkunftsfamilie"],"Kinder- und Jugendfürsorge war Teil der Armenfürsorge: Es ging darum, unversorgte, verwaiste und „verwahrloste“ Kinder zu kontrollieren und möglichst billig zu verwahren. Die Folie spricht vom Disziplinierungscharakter der Fürsorge. Erziehung und Prävention kamen erst um die Jahrhundertwende als Idee auf.",[("a1",26)])
MC("mon-kinder",[],"Was brachte die Reform der Armenkinderpflege von 1901 für Frauen?","Erstmals auch Frauen als Bezirksarmenrät*innen",["Das aktive Wahlrecht auf Bezirksebene","Bezahlte Stellen in allen Waisenhäusern","Die rechtliche Obsorge für ihre Kinder"],"Mit der Reform der Armenkinderpflege von 1901 konnten erstmals auch Frauen Bezirksarmenrätinnen werden. Ihnen oblagen Betreuung und Organisation der Armenkinderpflege. Das ist ein früher Schritt der Frauen in die öffentliche Fürsorge, allerdings in typisch weiblich zugeschriebenen Bereichen.",[("a1",26)])
TF("mon-kost",[],"Das Kostkinderwesen war bis 1914 vielfach ungeregelt und unkontrolliert.",True,"Das Kostkinderwesen, also die Unterbringung bei Pflegefamilien gegen Kostgeld, war bis 1914 vielfach ungeregelt und unkontrolliert. Es gab erwiesene Missstände in Pflegefamilien. Diese Kontinuität reicht bis in die 1960er Jahre.")
MC("mon-kost",[],"Welche Motive hatten ländliche Pflegefamilien laut Folie oft?","Pflegegeld und potentielle Arbeitskräfte",["Religiöser Auftrag und Schulpflicht","Prestige und politische Ämter","Adoption und Erbschaft"],"Ländliche Pflegefamilien hatten oft egoistische Motive: Interesse am Pflegegeld und an den Kindern als potenziellen Arbeitskräften. Für die Gemeinden war die Unterbringung am Land billiger. Kontrolle fehlte weitgehend.")
MC("mon-verw",[],"Womit wurde ein „verwahrlostes“ Kind in einem Zitat gleichgestellt?","Mit einem an einem epidemischen Leiden Erkrankten",["Mit einem Opfer eines Verbrechens","Mit einem begabten, aber armen Kind","Mit einem Waisenkind in Not"],"Ein „verwahrlostes“ Kind wurde in einem Zitat mit einem an einem epidemischen Leiden Erkrankten gleichgestellt. Das zeigt die moralische Komponente des Begriffs: Es ging um Separation wegen angeblicher „Ansteckungsgefahr“, nicht um Schutz. Erst mit der Erziehungsfürsorge nach der Jahrhundertwende änderte sich der Blick.")
TF("mon-verw",[],"Der Bezirksschulrat agierte als „pädagogische Polizei“ und gab nicht angepasste Kinder in Besserungsanstalten ab.",True,"Der Bezirksschulrat agierte als „pädagogische Polizei“ und gab nicht angepasste Kinder in Besserungsanstalten ab. Noch 1906 legitimierte das Vagabundengesetz solche Einweisungen. Schule und Fürsorge waren damit Teil eines Kontrollsystems.")
MC("mon-poli",[11],"Was war am sozialdemokratischen Kommunalprogramm von 1896 neu?","Konzentration auf Bedürftige, die nicht Lohnarbeiter sind",["Abschaffung aller privaten Wohltätigkeit","Die Einführung der Generalvormundschaft","Das Ende des Heimatrechts"],"Neu am sozialdemokratischen Kommunalprogramm von 1896 war die Konzentration auf Bedürftige, die keine Lohnarbeiter*innen waren: Säuglinge, Schwangere, Wöchnerinnen und Menschen mit bestimmten Krankheiten. Es war ein erstes Modell für Familien-, Bevölkerungs- und Gesundheitspolitik. Die Folie verweist hier auf das Rote Wien ab 1919, das darauf aufbaute.")
ORD("mon-epochen",[2,3],"Bringe die Ereignisse der Monarchie in die richtige Reihenfolge.",[("1863","Heimatrechtsgesetz"),("1885","Zwangsarbeitergesetze"),("1896","Novelle mit Ersitzungsprinzip"),("1901","Reform der Armenfürsorge")],"Die Reihenfolge führt vom Heimatrecht 1863 über die Kriminalisierung der Armut 1885 und die Novelle des Heimatrechts 1896 zu den ersten Reformen der Armenfürsorge um 1901. Die Linie zeigt, wie aus Abschottung und Strafe langsam Reform wurde, ohne dass ein Rechtsanspruch entstand.",[("a1",7),("a1",11),("a1",9),("a2",3)])

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

MC("ref-1901",[],"Was war das Ziel der Reform der Armenfürsorge von 1901?","Bessere Zusammenarbeit privater und öffentlicher Armenpflege und mehr Kontrolle",["Abschaffung der privaten Armenpflege zugunsten der Gemeinde","Einführung eines allgemeinen Anrechts auf Fürsorge","Trennung von Gesundheitsfürsorge und Jugendwohlfahrt"],"Die christlich-soziale Reform von 1901 wollte die Zusammenarbeit von privater und öffentlicher Armenpflege verbessern und differenzierte die Fürsorge nach Alter und Bedarf. Zugleich brachte sie mehr Kontrolle der Armen; „Erfassen“ steht auf der Folie als Stichwort dafür. Hilfe und Kontrolle wuchsen also gemeinsam.")
MC("ref-ehren",[9],"Welche zwei Merkmale kennzeichnen das Amt der Armenrät*innen?","Unbezahlt und keine Ausbildung",["Bezahlt und mit Matura","Unbezahlt und zweijährige Ausbildung","Bezahlt und ohne Ausbildung"],"Armenrät*innen arbeiteten unbezahlt und brauchten keine Ausbildung. Das Amt setzte zudem männliche Gemeindemitglieder voraus, eine Ausnahme waren die Kostkinder, wo auch Frauen eingesetzt wurden. Ehrenamt glich so die fehlende staatliche Versorgung aus.",[("a2",7)])
TF("ref-ehren",[9,23],"Frauen wurden als Armenrätinnen vor allem bei den Kostkindern und Waisenkindern eingesetzt.",True,"Frauen wurden als Armenrätinnen vor allem bei den Kost- und Waisenkindern eingesetzt. Die Folie vermerkt dazu „Geschlechterrollen!!“: Die geschlechtsspezifische Arbeitsteilung wies Frauen die Sorge um Kinder zu. Später wurde daraus der Frauenberuf Fürsorgerin.",[("a2",7)])
MC("ref-ehren",[9],"Was warf die Sozialdemokratie der privaten „Wohltäterei“ vor?","Beschenkte stehen in Schuld und müssen sich dankbar verhalten",["Die Hilfe war zu großzügig und zu teuer","Wohltäter arbeiteten ohne jede Religion","Sie finanzierte die Gewerkschaften"],"Die Sozialdemokratie kritisierte die private „Wohltäterei“, weil Beschenkte in Schuld standen und sich dankbar und wohlverhaltend zeigen mussten. Privatwohltätigkeit operierte somit keineswegs als neutrales Hilfskonzept, sondern als Mittel der Kontrolle. Dagegen setzte das Rote Wien das Anrecht auf Fürsorge.",[("a2",13)])
MULTI("ref-ehren",[9],"Welche Prinzipien der freiwilligen Fürsorge nennt die Folie?",["Individuelle Bedürftigkeit","Gesetzlicher Anspruch nicht notwendig","Ehrenamt"],["Allgemeines Anrecht auf Fürsorge","Berufsausbildung als Pflicht"],"Vorbild der freiwilligen Fürsorge war das Elberfelder System: ehrenamtliche Armenpfleger in kleinen Quartieren, die wenige Familien persönlich betreuten und Hilfe individuell prüften. Damit verband sich Hilfe mit genauer Kontrolle der Armen.",[("a2",8)])
TF("ref-ehren",[9],"In Österreich spielte private Wohltätigkeit eine größere Rolle als in den USA und Deutschland.",False,"Private Wohltätigkeit spielte in Österreich eine vergleichsweise geringe Rolle, weniger als in den USA und in Deutschland. Wegen der schwachen Sozialgesetzgebung blieb sie aber trotzdem relevant, weil sie Lücken der öffentlichen Versorgung füllte.",[("a2",12)])
MULTI("ref-elb",[7],"Was gehört zu den Charakteristika des Elberfelder Systems?",["Quartierprinzip","Ehrenamtlichkeit","Friendly Visiting","Dezentralisierung"],["Zentrale staatliche Verwaltung","Rechtsanspruch auf Hilfe"],"Das Elberfelder System von 1853 setzte auf Dezentralisierung, Ehrenamt, das Quartierprinzip und den Hausbesuch als Friendly Visiting. Dazu kommen Hilfe zur Selbsthilfe und die geistige Mütterlichkeit. Es entstand als Antwort auf Zuwanderung und wachsende Armut in den Textilstädten und wurde Vorbild der freiwilligen Fürsorge.")
MC("ref-elb",[7],"Was ist mit „Friendly Visiting“ gemeint?","Der Hausbesuch",["Der Besuch in einer Klinik","Eine Spendengala","Ein Kurs für Eltern"],"Friendly Visiting meint den Hausbesuch: Ehrenamtliche besuchten die Armen zu Hause, um ihre Lage persönlich einzuschätzen. Das Hausbesuchsprinzip wurde über Jahrzehnte zentral für die Fürsorge. Später diente es auch als Kontrollinstrument, etwa bei der Nachschau der Fürsorgerinnen.",[("a2",9)])
MC("ref-elb",[7],"Wann wurde das Elberfelder System entwickelt?","1853",["1889","1901","1917"],"Das Elberfelder System entstand 1853. Ausgangspunkt waren Zuwanderung, dichte Besiedelung und immer mehr Arme in den Textilstädten. Die Antwort war ein dezentrales System mit Ehrenamtlichen, die in kleinen Quartieren zuständig waren.",[("a2",9)])
MC("ref-selbst",[7],"Was meint „Hilfe zur Selbsthilfe“?","Temporäre, gezielte Hilfe, damit Menschen danach ohne Fürsorge auskommen",["Dauerhafte finanzielle Absicherung aller Armen","Armen wird das Betteln grundsätzlich erlaubt","Familien müssen Angehörige selbst pflegen"],"Hilfe zur Selbsthilfe heißt: Einmalige Gaben helfen nicht, die Hilfe soll temporär und gezielt sein, damit Menschen danach ohne Fürsorge auskommen. Die Folie spricht von Selbstermächtigung und Empowerment. Sie merkt aber auch an, dass ökonomische Interessen dahinter standen.")
TF("ref-selbst",[],"Hinter „Hilfe zur Selbsthilfe“ standen neben dem Hilfsaspekt auch ökonomische Interessen.",True,"Neben dem Hilfsaspekt standen ökonomische Interessen: Soziale Ausgaben sollten nicht zu hoch werden. Wer schnell wieder ohne Fürsorge auskommt, kostet weniger. Das Doppelgesicht von Hilfe und Kostenkontrolle zieht sich durch die Geschichte.")
MC("ref-mutter",[23],"Was ist „geistige Mütterlichkeit“?","Ideal der bürgerlichen Frauenbewegung: weiblicher Beitrag über soziales Ehrenamt",["Eine Ausbildung für Mütter in Geburtskliniken","Ein Gesetz über die Obsorge unverheirateter Mütter","Das Mutterkreuz als öffentliche Auszeichnung"],"Geistige Mütterlichkeit war ein Ideal der bürgerlichen Frauenbewegung: Neben die biologische Mutterschaft trat eine soziale Mütterlichkeit, die Frauen über das soziale Ehrenamt in die Gesellschaft einbringen sollten. Soziale Arbeit wird damit als öffentliche Reproduktionsarbeit weiblich definiert.")
TF("ref-mutter",[23],"Die geistige Mütterlichkeit brach mit dem bürgerlichen Geschlechterrollenmodell.",False,"Die Folie nennt die geistige Mütterlichkeit eine Fortsetzung des bürgerlichen Geschlechterrollenmodells, keinen Bruch damit. Frauen bekamen zwar einen öffentlichen Raum, aber nur in der Rolle der Sorgenden. Das prägte Soziale Arbeit lange als Frauenberuf.")
MC("ref-modelle",[7],"Welches Modell gilt als Vorläufer der Gemeinwesenarbeit?","Das Settlement",["Das Social Case Work","Das Elberfelder Quartier","Die Berufsvormundschaft"],"Das Settlement, also die Nachbarschaftshilfe nach dem Vorbild von Toynbee Hall, gilt als Vorläufer der Gemeinwesenarbeit. Case Work, die Einzelfallhilfe nach Mary Richmond, ist dagegen Vorläufer der vertieften Einzelfallhilfe. Beide Modelle entstanden aus der Verelendung im Zuge der Industrialisierung.")
MATCH("ref-modelle",[7],"Verbinde Person und Einrichtung.",[("Barnett","Toynbee Hall, London"),("Jane Addams","Hull House, Chicago"),("Mary Richmond","Altamont Hotel, Baltimore"),("Marie Lang","Ottakringer Settlement, Wien")],"Samuel Barnett gründete Toynbee Hall in London, Jane Addams Hull House in Chicago, Marie Lang das Ottakringer Settlement in Wien: Sie stehen für das Settlement. Mary Richmond im Altamont Hotel in Baltimore steht für die Einzelfallhilfe mit sozialer Diagnose.",[("a2",16),("a2",26),("a2",34),("a2",55)])
MC("ref-toynbee",[7],"Was war die Kernidee von Toynbee Hall?","Gemeinsames Leben mit den Armen, um zu lehren und von ihnen zu lernen",["Arme in Anstalten am Stadtrand unterbringen","Spenden reicher Familien zentral verteilen","Kinder in Pflegefamilien am Land vermitteln"],"Kernidee von Toynbee Hall war das gemeinsame Leben mit den Armen: Akademiker lebten als Settler im Armenviertel, um zu lehren und von den Bewohner*innen zu lernen. Die persönliche Beziehung zwischen Settlern und Bewohner*innen stand im Zentrum. Bildung und Kultur sollten die Sozialdisziplinierung ersetzen.",[("a2",18)])
MC("ref-toynbee",[7],"Was kritisierte Toynbee Hall an der karitativen Armenfürsorge?","Ungleiches Verhältnis von Geber und Empfänger zerstört die Selbstachtung",["Sie gab den Armen zu viel Geld","Sie war zu stark wissenschaftlich fundiert","Sie schloss Akademiker von der Arbeit aus"],"Toynbee Hall kritisierte das ungleiche Verhältnis von Geber und Empfänger, weil es die Selbstachtung der Armen zerstört. Statt Mitleid und Gewissensberuhigung durch Spenden sollte es praktische Tätigkeit und Hilfe geben. Das ist eine frühe Kritik an der Wohltätigkeit.",[("a2",17)])
TF("ref-toynbee",[7],"Die Tätigkeit der „Settler“ in Toynbee Hall wurde bezahlt.",True,"Die Tätigkeit der Settler wurde bezahlt. Die Settler waren junge Männer, in der Regel aus der sozialen Oberschicht, die für eine Zeit im Armenviertel lebten. Das unterscheidet Toynbee Hall vom rein ehrenamtlichen Elberfelder System.",[("a2",18)])
MC("ref-toynbee",[26],"Woran erinnern die wöchentlichen Vieraugengespräche zwischen Barnett und den Bewohnern laut Folie?","An Supervision",["An ein Verhör","An eine Bilanzprüfung","An eine Beichte"],"Barnett führte wöchentliche Vieraugengespräche mit den Bewohnern, um sich auszutauschen und zu beraten. Die Folie verweist selbst auf Supervision. Reflexion der eigenen Arbeit ist also kein neues Element der Sozialen Arbeit.",[("a2",20)])
MC("ref-hull",[7],"Worin ähnelte Hull House Toynbee Hall?","Unter den Armen leben und von ihnen lernen",["Als rein männliche Einrichtung von Akademikern","Als behördliche Kontrollstelle der Stadt","Als Heim für Waisen unter 6 Jahren"],"Wie Toynbee Hall setzte Hull House darauf, unter den Armen zu leben und von ihnen zu lernen. Hull House war aber auf mittellose Frauen und Kinder konzentriert, mit Kindergarten, Volksküche und Bildung. Die Mitarbeiterinnen waren in der Regel ehrenamtliche Frauen.",[("a2",27),("a2",28)])
MC("ref-hull",[7],"Was sah Addams in der Großstadt?","Einen Sozialisierungsraum mit eigener positiver Bedeutung",["Die Hauptursache allen sozialen Übels","Einen Ort, den Arme verlassen sollten","Einen Markt für billige Arbeitskräfte"],"Jane Addams sah die Großstadt als Sozialisierungsraum mit eigener positiver Bedeutung. Die Folie betont, dass es ihr nicht um Kritik an der Großstadt ging. Sie wollte die Lebensbedingungen im Viertel verstehen und verbessern, nicht die Menschen aus der Stadt herausholen.",[("a2",33)])
MULTI("ref-hull",[7],"Welche Forderungen stellte Hull House sozialpolitisch?",["Arbeitslosenhilfe","Arbeitszeitverkürzung","Mindestlöhne"],["Abschaffung der Schulpflicht","Einführung von Zwangsarbeit"],"Hull House engagierte sich auch sozialpolitisch und untersuchte die Lebensbedingungen im Viertel. Zu den Forderungen gehörte auch die Verbesserung des Arbeitsschutzes. Addams verband so Nachbarschaftsarbeit mit politischer Einflussnahme.",[("a2",33)])
MC("ref-richmond",[7,26],"Worauf gründete Mary Richmonds Hilfskonzept?","Auf einer wissenschaftlich fundierten „sozialen Diagnose“",["Auf Nachbarschaftsabenden und Musik","Auf gesetzlichen Zwangsmaßnahmen","Auf religiöser Unterweisung"],"Mary Richmond gründete ihr Hilfskonzept auf eine wissenschaftlich fundierte soziale Diagnose. Vorbild war die ärztliche Diagnose: Gesucht wurden die individuellen körperlichen und psychischen Ursachen sozialer Not. Daraus entstand die Einzelfallhilfe, Social Case Work.",[("a2",37)])
MC("ref-richmond",[7],"Wann erschien „Social Diagnosis“?","1917",["1889","1902","1929"],"„Social Diagnosis“ erschien 1917 und gilt als zentrales Werk der sozialen Einzelfallhilfe. Richmond forderte damit auch eine professionelle Ausbildung. Ihr Ansatz kam später über Case Work nach Österreich.",[("a2",39)])
TF("ref-richmond",[5],"Richmond war Vorbild sowohl für Alice Salomon als auch für Ilse Arlt.",True,"Laut Folie war Mary Richmond Vorbild sowohl für Alice Salomon als auch für Ilse Arlt. Ihre Idee, Hilfe auf Wissen und Diagnose zu gründen, prägte die frühen Ausbildungen. Bei Arlt zeigt sich das in der Bedürfnislehre.",[("a2",37)])
MC("ref-richmond",[24],"Warum forderte Richmond Fortbildungskurse im Friendly Visiting?","Soziale Arbeit soll organisiert statt punktuell sein",["Ehrenamtliche sollten Spenden sammeln lernen","Frauen sollten vom Beruf ferngehalten werden","Der Staat sollte die Kurse kontrollieren"],"Richmond forderte Fortbildungskurse im Friendly Visiting, weil Soziale Arbeit organisiert statt punktuell sein sollte. Geschäftsmäßig organisiert, sollte sie die vorhandenen Ressourcen optimal nutzen. Das ist ein Schritt vom Ehrenamt zur Professionalisierung.",[("a2",38)])
MC("ref-salomon",[5],"Was gründete Alice Salomon 1908 in Berlin?","Die erste interkonfessionelle Soziale Frauenschule",["Die Akademie für soziale Verwaltung","Das erste Jugendamt Deutschlands","Das Settlement in Ottakring"],"Alice Salomon gründete 1908 in Berlin die erste interkonfessionelle Soziale Frauenschule. Die Ausbildung dauerte 2 Jahre und vermittelte Wissen und Haltung, eine „Pflanzstätte sozialer Gesinnung“. Sie war Vorbild für Ilse Arlts Schule in Wien.",[("a2",47),("eb",11)])
MATCH("ref-salomon",[],"Ordne Salomons Lebensdaten zu.",[("1899","erster Jahreskurs zur Wohlfahrtspflege"),("1908","Soziale Frauenschule"),("1925","Deutsche Akademie"),("1937","Ausweisung, Emigration in die USA")],"1899 gab es den ersten Jahreskurs zur Wohlfahrtspflege, 1908 gründete sie die Soziale Frauenschule, 1925 die Deutsche Akademie für Führungskräfte. 1937 wurde sie von den Nationalsozialisten ausgewiesen und emigrierte in die USA. Ein Leben zwischen Frauenbewegung, Ausbildung und Vertreibung.",[("a2",46),("a2",47),("a2",50),("a2",52)])
TF("ref-salomon",[],"Salomon promovierte 1906 über die Ursachen der ungleichen Entlohnung von Männer- und Frauenarbeit.",True,"Salomon promovierte 1906 über die Ursachen der ungleichen Entlohnung von Männer- und Frauenarbeit, ein in der Frauenbewegung kontrovers diskutiertes Thema. Sie verband Wissenschaft, Frauenbewegung und Ausbildung. Das machte sie zur Schlüsselfigur der Verberuflichung.",[("a2",46)])
MC("ref-ott",[7],"Nach welchem Vorbild entstand das Ottakringer Settlement?","Toynbee Hall in London",["Hull House in Chicago","Altamont Hotel in Baltimore","Elberfeld in Deutschland"],"Das Ottakringer Settlement entstand nach dem Vorbild von Toynbee Hall in London. Gegründet wurde es 1901 vom Verein Wiener Settlement um Marie Lang. Es kümmerte sich um Kinder ärmerer Schichten und um die Weiterbildung der Mütter.")
TF("ref-ott",[],"Das Ottakringer Settlement schloss laut Statuten jede politische Tätigkeit aus.",True,"Ziel war laut Statuten die Hebung des „geistigen, körperlichen und sittlichen Niveaus“, „unter Ausschluss jeder politischen Thätigkeit“. Anders als Hull House wollte das Settlement also nicht sozialpolitisch wirken. 1938 wurde der Verein enteignet und aufgelöst.",[("a2",54)])
TF("ref-ott",[15],"Nach 1945 kehrten die jüdischen Mitarbeiterinnen ins Ottakringer Settlement zurück.",False,"Die jüdischen Mitarbeiterinnen fehlten nach 1945: Sie mussten emigrieren oder wurden ermordet. Der Verein wurde 1938 enteignet, erst 1950 kam er in das leere Haus zurück. Der Bruch durch den Nationalsozialismus ist hier besonders deutlich.",[("a2",60)])
MC("ref-key",[],"Was kritisierte Ellen Key in „Das Jahrhundert des Kindes“?","Erziehungspraktiken von Zucht und Drill",["Die Ausbildung von Fürsorgerinnen","Die Schließung der Waisenhäuser","Den Bau neuer Kindergärten"],"Ellen Key kritisierte in „Das Jahrhundert des Kindes“ von 1902 Erziehungspraktiken von Zucht und Drill. Das Buch der schwedischen Reformpädagogin war ein zeitgenössisches Standardwerk. Auf den Folien steht ihr Name auch als „Kay“.")

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

MC("ber-bv",[8],"Warum brauchte es überhaupt eine Vormundschaft für uneheliche Kinder?","Mütter durften die rechtliche Obsorge nicht übernehmen",["Väter hatten kein Interesse an Geld","Die Kirche untersagte jede Pflege durch Mütter","Kinder hatten sonst keinen Schulplatz"],"Mütter unehelicher Kinder durften die rechtliche Obsorge nicht übernehmen, darum brauchten die Kinder einen Vormund als rechtlichen Vertreter. Diese Frage der rechtlichen Vertretung war der Kern des Problems. Die Listenvormünder lösten es nicht, darum entstand die Berufsvormundschaft.")
MC("ber-bv",[8],"Was waren „Listenvormünder“?","Aus Wählerlisten bestimmte Männer, die nur pro forma Vormund waren",["Ausgebildete Fürsorgerinnen der Gemeinde","Ärzte aus den städtischen Geburtskliniken","Väter unehelicher Kinder auf einer Meldeliste"],"Listenvormünder waren Männer aus den Wählerlisten, die die Vertretung übernahmen, wenn kein männlicher Verwandter da war. Sie waren nur pro forma Vormund und kümmerten sich nicht um das Wohl der Kinder. Als Lösung entstand ab 1913 die Berufsvormundschaft.",[("eb",3)])
MULTI("ber-aufgaben",[8],"Welche Aufgaben hatte die Berufsvormundschaft?",["Väter unehelicher Kinder ausforschen","Unterhaltszahlungen einholen","Ärztliche Kontrolle der Mündel","Hausbesuche bei ledigen Müttern"],["Schulen für Fürsorgerinnen leiten"],"Die Berufsvormundschaft forschte Väter aus, holte Unterhalt ein und ließ die „Mündel“ ärztlich kontrollieren; Hausbesuche dienten der Belehrung lediger Mütter. Dazu kam der Verbindungsdienst mit Geburtskliniken. Hilfe und Kontrolle gingen hier Hand in Hand.")
MC("ber-aufgaben",[22],"Was geschah im „Verbindungsdienst“ mit Geburtskliniken?","Ausforschen bedürftiger Mütter und Kinder",["Finanzierung neuer Krankenhäuser","Ausbildung von Hebammen","Verteilung von Spenden aus dem Ausland"],"Im Verbindungsdienst mit Geburtskliniken wurden bedürftige Mütter und Kinder ausgeforscht, also erfasst. Das war ein Instrument von Hilfe und Erfassung zugleich. In späteren Epochen wurde es erweitert, etwa im Ersten Weltkrieg und im Roten Wien.")
MC("ber-bv",[8,24],"Was geschah 1913 in der Berufsvormundschaft erstmals?","10 Dienststellen für bezahlte Berufspflegerinnen",["Einführung der Generalvormundschaft für ganz Wien","Akademische Ausbildung für alle Pflegerinnen","Abschaffung des Ehrenamts in der Jugendwohlfahrt"],"1913 gab es erstmals 10 Dienststellen für bezahlte Berufspflegerinnen. Grund war der Mangel an ehrenamtlichem Personal. Es war der erste Schritt zu entlohnter sozialer Berufsarbeit, aber noch ohne Ausbildung als Voraussetzung.",[("eb",5)])
TF("ber-bv",[24],"Die ersten bezahlten Berufspflegerinnen 1913 mussten eine abgeschlossene Ausbildung nachweisen.",False,"Die Folie betont: entlohnte soziale Berufsarbeit „ohne Ausbildung als Voraussetzung“. Bezahlung kam also vor der Ausbildung. Erst mit Arlts Fachkursen und den städtischen Fachkursen wurde die Ausbildung zur Regel.",[("eb",5)])
MULTI("ber-bv",[8],"Wer arbeitete im Team der Berufsvormundschaft?",["Arzt","Rechtskundiger Berufsvormund","Pflegerinnen","Juristen"],["Psychoanalytiker"],"Das Team der Berufsvormundschaft bestand aus bezahlten Berufskräften und wurde von ehrenamtlichen Mitarbeiter*innen ergänzt. Diese Mischung aus Beruf und Ehrenamt war typisch für den Übergang zur professionellen Fürsorge.",[("eb",5)])
MC("ber-arlt",[5],"Wann gründete Ilse Arlt die Vereinigten Fachkurse für Volkspflege?","1912",["1899","1917","1921"],"Ilse Arlt gründete 1912 die Vereinigten Fachkurse für Volkspflege, die erste österreichische Ausbildungseinrichtung für soziale Arbeit. Sie wollte ein neues weibliches Berufsfeld schaffen und die Fürsorge professionalisieren. Vorbild war Salomons Soziale Frauenschule in Berlin.")
MC("ber-arlt",[5],"Was war das Ziel von Arlts Schule?","Neues weibliches Berufsfeld und Professionalisierung der Fürsorge",["Abschaffung der freien Liebestätigkeit","Ausbildung von Beamten für das Ministerium","Vorbereitung von Frauen auf die Ehe"],"Arlt wollte ein neues weibliches Berufsfeld und die Professionalisierung der Fürsorge. Die freie Liebestätigkeit wollte sie nicht verdrängen, sondern stützen. Bezahlte und unbezahlte Arbeit sollten dieselbe gründliche Vorbereitung bekommen.")
TF("ber-arlt",[5],"Arlt wollte die Ausbildung für unbesoldete Hilfstätigkeit einfacher halten als für bezahlte Berufsarbeit.",False,"Arlt machte keinen Unterschied zwischen bezahlter und unbezahlter Arbeit, denn unbesoldete Arbeit soll genauso gründlich getan werden. Gute Fürsorge braucht Wissen, egal wer sie leistet. Das ist ein zentraler Gedanke ihrer Professionalisierung.",[("eb",12)])
MC("ber-arlt",[5],"Wie waren die Aufnahmekriterien an Arlts Schule?","Offen: 17 bis 35 Jahre, unterschiedliche Vorbildung",["Nur Maturantinnen ab 21 Jahren","Nur Kinderlose mit zwei Jahren Praxis","Nur Frauen mit Kindergartenprüfung"],"Die Aufnahme war offen: Frauen zwischen 17 und 35 Jahren mit unterschiedlicher Vorbildung. Es sollten möglichst viele Frauen gewonnen werden, wesentlich war die Persönlichkeit. Erst die spätere Akademie für soziale Verwaltung verlangte die Matura.",[("eb",13)])
MULTI("ber-arlt",[5],"Welche Inhalte gehörten zu Arlts Lehrplan?",["Gesundheitsfürsorgerische Inhalte","Psychologische Inhalte","Volkswirtschaftslehre"],["Rassenkunde","Kirchenrecht als Hauptfach"],"Arlts Lehrplan war umfassend und vielseitig, auch mit Gastlehrenden von der Universität. Er verband praktische Fächer mit wissenschaftlichen Grundlagen. Soziale Arbeit sollte für sie Wissenschaft und Praxis zugleich sein.",[("eb",14)])
MC("ber-arlt",[5],"Welches Vorbild nennt die Folie für Arlts Schule?","Alice Salomons Soziale Frauenschule",["Jane Addams’ Hull House","Tandlers Wohlfahrtsamt","Ellen Keys Reformschule"],"Als Vorbild für Arlts Schule nennt die Folie Alice Salomons Soziale Frauenschule in Berlin. Für die Methode beziehen sich die Folien außerdem auf Mary Richmond. Arlt verband diese Einflüsse mit ihrer eigenen Bedürfnislehre.",[("eb",2),("eb",11)])
MATCH("ber-arlt",[],"Welches Werk erschien wann?",[("1921","Die Grundlagen der Fürsorge"),("1923","Die Gestaltung der Hilfe"),("1958","Wege zu einer Fürsorgewissenschaft")],"1921 erschien „Die Grundlagen der Fürsorge“, 1923 „Die Gestaltung der Hilfe“, 1958 „Wege zu einer Fürsorgewissenschaft“. Die Werke zeigen Arlts Überzeugung, dass Soziale Arbeit Wissenschaft und Praxis zugleich ist.",[("eb",17)])
MC("ber-beduerf",[6],"Wie viele Bedürfnisklassen unterscheidet Ilse Arlt?","Dreizehn",["Sieben","Sechsundzwanzig","Drei"],"Arlt unterscheidet dreizehn Bedürfnisklassen, entwickelt aus Einzelfällen. Sie reichen von Luft, Licht und Wärme bis zur Geistespflege und dienen als Maßstab für Forschung und Hilfe. So lässt sich genau benennen, wo ein Mensch unterversorgt ist.")
MULTI("ber-beduerf",[6],"Welche gehören zu Arlts Bedürfnisklassen?",["Luft, Licht, Wärme","Rechtsschutz","Erholung","Familienleben"],["Besitz und Vermögen"],"Die Bedürfnisklassen sind allen Menschen gemeinsam, variieren aber je nach Alter, Schicht, Religion und Behinderung. Dazu gehören etwa Ernährung, Wohnung, Körperpflege, Kleidung, Erholung und Geistespflege. Arlt wollte damit Armut messbar und Hilfe gezielt machen.",[("eb",18)])
MC("ber-beduerf",[6],"Wann muss Fürsorge laut Arlt einschreiten?","Bei Spannung zwischen einfachster ausreichender Befriedigung und Unterbefriedigung",["Erst bei offensichtlicher, akuter Notlage","Wenn eine Behörde sie ausdrücklich anfordert","Wenn die betroffene Person arbeitslos gemeldet ist"],"Laut Arlt soll Fürsorge schon einschreiten, wenn eine Spannung zwischen einfachster ausreichender Bedürfnisbefriedigung und Unterbefriedigung vorliegt. Hilfe soll also als Prophylaxe wirken, nicht erst im Notfall. Das ist ein früher präventiver Ansatz.",[("eb",20)])
TF("ber-beduerf",[6],"Arlts Kenntnis der Bedürfnisse sollte die Annahme stützen, dass Armut selbstverschuldet ist.",False,"Arlts Kenntnis der Bedürfnisse sollte das Gegenteil leisten: Annahmen über selbstverschuldete Armut und das Vorurteil einer homogenen Gruppe von Armen widerlegen. Wer genau hinschaut, sieht unterschiedliche Ursachen und Bedürfnisse. Das unterscheidet sie von der moralischen Armutsdeutung der Monarchie.",[("eb",18)])
MC("ber-wk",[],"Was entstand 1916 auf staatlicher Ebene?","Ein Ministerium für soziale Fürsorge",["Die Akademie für soziale Verwaltung","Das Rote Wien","Die Generalvormundschaft"],"1916 entstand ein Ministerium für soziale Fürsorge. Im selben Jahr bekam die Jugendfürsorge auch ein eigenes Referat der Gemeinde Wien. Der Krieg mit steigender Säuglingssterblichkeit und Not beschleunigte den Ausbau der staatlichen Fürsorge.")
MC("ber-wk",[22],"Was bekamen bedürftige Mütter im Ersten Weltkrieg über den Verbindungsdienst?","Beihilfen in Geld, Lebensmitteln und Säuglingswäsche",["Eine bezahlte Ausbildung als Pflegerin","Das Recht auf Obsorge über ihr Kind","Einen freien Platz im Gemeindebau"],"Über den Verbindungsdienst bekamen bedürftige Mütter Beihilfen in Geld, Lebensmitteln und Säuglingswäsche. Die Wäsche nähten Arbeitslose in einer Nähstube. Der Verbindungsdienst an Gebäranstalten wurde im Krieg ausgebaut.",[("eb",24)])
TF("ber-wk",[],"NEU im Ersten Weltkrieg war die Konzentration auf Fälle „erzieherischer Gefährdung“.",True,"Neu im Ersten Weltkrieg war die Konzentration auf Fälle „erzieherischer Gefährdung“. Begründet wurde das mit der außerhäuslichen Berufsarbeit der Mütter. Die Jugendfürsorge erweiterte sich damit vom Armenkind auf die Erziehung.",[("eb",22)])
MC("ber-ehe",[23],"Was verlangte der Gemeinderatsbeschluss vom 27.4.1917?","Ehe- und Kinderlosigkeit für das Fürsorgerinnenamt",["Matura für alle Pflegerinnen","Männliche Vormünder für jedes Kind","Unbezahlte Probezeit von zwei Jahren"],"Der Gemeinderatsbeschluss vom 27.4.1917 verlangte Ehe- und Kinderlosigkeit für das Fürsorgerinnenamt, weil ehrenamtliche Kräfte fehlten. 1919 wurde die Regel wieder aufgehoben, wegen verstärkter Nachfrage nach weiblichem Personal. Der Beruf lässt sich auch als Lebensentwurf jenseits von Familie lesen.")
TF("ber-ehe",[23],"Die Ehe- und Kinderlosigkeit galt für Fürsorgerinnen über mehrere Jahrzehnte.",False,"Die Regel galt nur von 1917 bis 1919. Dann wurde sie aufgehoben, weil mehr weibliches Personal gebraucht wurde. Sie zeigt, wie eng der Beruf an Vorstellungen von Weiblichkeit geknüpft war.")
MC("ber-ja",[24],"Welchen Berufstitel führten die Absolventinnen der städtischen Fachkurse von 1917?","Fürsorgerin",["Sozialarbeiterin","Wohlfahrtspflegerin","Volkspflegerin"],"Die Absolventinnen führten den Berufstitel „Fürsorgerin“. Die städtischen Fachkurse dauerten 2 Jahre; 1918 wurden sie in eine Akademie für soziale Verwaltung umgewandelt. Damit war der Beruf mit eigener Ausbildung und Titel etabliert.",[("eb",27)])
TF("ber-ja",[24],"Die Akademie für soziale Verwaltung setzte ab 1919 einen Schulabschluss mit Matura voraus.",True,"Die Akademie für soziale Verwaltung setzte ab 1919 einen Schulabschluss mit Matura voraus. Ganz im Unterschied zu vorher, als Arlts Kurse Frauen mit unterschiedlicher Vorbildung aufnahmen. Die Ausbildung wurde damit akademischer und exklusiver.",[("eb",27)])
ORD("ber-ja",[24,5],"Von den ersten Kursen zum Jugendamt: Was kam wann?",[("1912","Arlts Vereinigte Fachkurse"),("1913","10 Stellen für Berufspflegerinnen"),("1917","Gründung des Wiener Jugendamtes"),("1918","Akademie für soziale Verwaltung")],"1912 gründete Arlt die Vereinigten Fachkurse, 1913 gab es die ersten 10 Stellen für bezahlte Berufspflegerinnen, 1917 wurde das Wiener Jugendamt gegründet und 1918 wurden die städtischen Fachkurse zur Akademie für soziale Verwaltung. In wenigen Jahren wird aus dem Ehrenamt ein Beruf mit Ausbildung und Amt.",[("eb",11),("eb",5),("z",1)])

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

MC("rot-kontext",[10],"Womit finanzierte das Rote Wien Wohnbau und Fürsorge?","Mit den „Breitner-Steuern“ auf Besitz, Verkehr und Boden",["Mit einer Kopfsteuer auf alle Arbeiter","Mit Krediten der Habsburger","Mit Zöllen auf Lebensmittel"],"Das Rote Wien finanzierte Wohnbau und Fürsorge mit den Breitner-Steuern auf Besitz, Verkehr und Boden, also Luxussteuern mit Verteilung von oben nach unten. Hugo Breitner war Finanzstadtrat.",[("rw",6)])
MC("rot-kontext",[],"Wie viele kommunale Wohnungen brachten die drei Wohnbauprogramme von 1923–1927 ungefähr?","Etwa 60.000",["Etwa 6.000","Etwa 600.000","Etwa 250"],"Die Wohnbauprogramme von 1923 bis 1927 brachten etwa 60.000 kommunale Wohnungen, mit eigenem Wasseranschluss und Toiletten. Den Bedarf deckten sie trotzdem nicht. Wohnungswesen und Fürsorge hingen eng zusammen.",[("rw",7)])
TF("rot-kontext",[10],"Wien war ab 1919 die einzige Millionenstadt unter rein sozialdemokratischer Verwaltung.",True,"Nach den ersten allgemeinen Wahlen am 4.5.1919 war Wien die einzige Millionenstadt unter rein sozialdemokratischer Verwaltung. Bald wurde Wien auch ein eigenes Bundesland. Das ermöglichte eigene Steuern und eine eigene Fürsorgepolitik.",[("rw",2)])
MC("rot-kontext",[],"Worauf zielte die Sozialpolitik im Wohnbau familienpolitisch ab?","Die normative Arbeiter-Kleinfamilie nach kleinbürgerlichem Vorbild",["Die Großfamilie nach bäuerlichem Vorbild","Die Auflösung der Familie zugunsten von Kollektiven","Das Einzelwohnen junger Erwachsener"],"Familienpolitisch zielte der Wohnbau auf die normative Arbeiter-Kleinfamilie nach kleinbürgerlichem Vorbild. Wohnungswesen und Fürsorge hingen eng zusammen: Die Fürsorgerin kontrollierte auch, ob die Familie dieser Norm entsprach.",[("rw",6)])
MC("rot-anrecht",[10],"Was war der zentrale Wendepunkt des Roten Wien im fürsorgerischen Selbstverständnis?","Die Formulierung eines allgemeinen Anrechts auf Fürsorge",["Die Einführung des Heimatrechts","Die Rückkehr zum Ehrenamt","Der Ausschluss der Unehelichen"],"Zentraler Wendepunkt war die Formulierung eines allgemeinen Anrechts auf Fürsorge. Das bedeutete die Abkehr von individueller Wohltat hin zum kollektiven Hilfeanspruch. Tandlers Wohlfahrtsamt verband dazu alle Einrichtungen zu einem engen Netz.")
MC("rot-anrecht",[10],"Wie lautet Tandlers Grundsatz der Jugendfürsorge?","„Die Kinder haben ein Anrecht auf Fürsorge und die Gesellschaft ist ihr Sachwalter.“",["„Wer nicht arbeitet, soll auch nicht essen.“","„Jedes Kind gehört der Familie allein.“","„Die Armen tragen selbst die Schuld.“"],"„Die Kinder haben ein Anrecht auf Fürsorge und die Gesellschaft ist ihr Sachwalter.“ Der Satz markiert den kollektiven Hilfeanspruch statt der Wohltätigkeit. Zugleich legitimierte er weitreichende Eingriffe, weil die Gesellschaft über das Kindeswohl wachte.")
TF("rot-anrecht",[10,9],"Die sozialdemokratische Wohlfahrt setzte die ehrenamtliche Wohltätigkeit bewusst fort.",False,"Die sozialdemokratische Wohlfahrt grenzte sich deutlich von der ehrenamtlichen Wohltätigkeit ab. Sie verstand sich als „kollektivistische Hilfeleistung“ mit Anrecht statt Almosen. Die Wohltätigkeit galt ihr als demütigend, weil Beschenkte Dankbarkeit schuldeten.",[("rw",9)])
MC("rot-anrecht",[],"Was bedeutet die Errichtung von Fürsorgesprengeln?","Dezentralisierung des Jugendamtes durch Einteilung in Bezirke",["Einsparung aller Hausbesuche","Privatisierung der Kindergärten","Verlegung von Heimen aufs Land"],"Mit den Fürsorgesprengeln wurde das Jugendamt dezentralisiert und in Bezirke eingeteilt. Das war Teil von Tandlers straffer Organisation und engmaschigem Netz. Jede Familie hatte damit eine zuständige Fürsorgerin in ihrer Nähe.",[("rw",8)])
MC("rot-eugenik",[12],"Was meint „positive Eugenik“ bei Tandler?","Qualitative Bevölkerungspolitik zur Hebung der Geburten und besseren „Aufzucht“",["Verbot jeder Heirat durch den Staat","Völlige Trennung von Fürsorge und Medizin","Förderung der Alten vor den Kindern"],"Positive Eugenik war bei Tandler qualitative Bevölkerungspolitik: mehr Geburten, weniger Säuglingssterblichkeit und eine bessere „Aufzucht“. Die Familie galt als „Keimzelle aller sozialen Organisation“. Die Grenze zur Selektion war dabei nicht scharf, wie die Beratungsstellen zeigen.")
MC("rot-eugenik",[12],"Wem wurde in den Beratungsstellen nahegelegt, auf Kinder zu verzichten?","Personen mit erblichen, psychiatrischen oder Suchterkrankungen",["Allen Arbeiterfrauen unter 25 Jahren","Allen Unverheirateten","Allen Personen ohne Heimatrecht"],"In den Beratungsstellen wurde Personen mit erblichen, psychiatrischen oder Suchterkrankungen nahegelegt, auf Kinder zu verzichten. Stichwort ist „vernünftige Zuchtwahl“, vergleiche den Film „Hygiene der Ehe“. Eugenisches Gedankengut war also schon im Roten Wien Teil der Fürsorge.",[("rw",11)])
MC("rot-eugenik",[12],"Welche Ausgaben galten als „bevölkerungspolitisch unproduktiv“?","Leistungen für „Gebrechliche, Alte und Irre“",["Leistungen für Kindergärten und Horte","Ausgaben für die Jugendfürsorge","Ausgaben für die Säuglingsfürsorge"],"Leistungen für „Gebrechliche, Alte und Irre“ galten als bevölkerungspolitisch unproduktiv. Sie sollten möglichst gering gehalten werden, um nicht auf Kosten der „produktiven“ Bevölkerung zu gehen. Hier zeigt sich die dunkle Seite der Tandler'schen Fürsorge.",[("rw",11)])
TF("rot-eugenik",[12],"Eugenik spielte in der Fürsorge des Roten Wien keine Rolle, sie kam erst mit dem NS-Regime.",False,"Eugenik spielte schon im Roten Wien eine Rolle: Tandlers Konzeption war maßgeblich bevölkerungspolitisch geleitet. Das Thema ist auch deshalb Prüfungsstoff, weil es zeigt, dass die NS-Selektion an vorhandene Denkweisen anknüpfen konnte. Der Unterschied liegt im Ausmaß und in der Vernichtung.",[("rw",10)])
MC("rot-erfassen",[12,22],"Was geschah mit dem Säuglingswäschepaket von 1927?","Alle Mütter bekamen es unentgeltlich beim Hausbesuch",["Nur bedürftige Mütter konnten es kaufen","Es wurde an Schulen an Väter ausgeteilt","Es war eine Prämie für die Eheschließung"],"Ab 1927 bekamen alle Mütter das Säuglingswäschepaket unentgeltlich beim Hausbesuch, unabhängig von der Bedürftigkeit. Das war Hilfe für alle, aber auch ein Türöffner: So kam die Fürsorgerin in jede Wohnung und konnte die Familie einschätzen. Das Paket ist ein Lehrbeispiel für das doppelte Mandat.",[("rw",14)])
MULTI("rot-erfassen",[12,22],"Mit welchen Instrumenten wurde Bedürftigkeit „erfasst“?",["Verbindungsdienst in Geburtsabteilungen","Säuglingswäschepaket","Obligatorische Schulfürsorge","Hausbesuch"],["Freiwillige Online-Beratung"],"Bedürftigkeit wurde über vier Wege erfasst: Verbindungsdienst, Säuglingswäschepaket, Schulfürsorge und Hausbesuch. Jeder davon verband Hilfe mit Kontrolle. So kam die Fürsorgerin als Beauftragte der Gesellschaft an praktisch alle Familien heran.",[("rw",14)])
MC("rot-erfassen",[12],"Was überprüfte die Fürsorgerin beim Hausbesuch vor allem?","Sauberkeit, Ordnung und Hygiene",["Einkommen und Parteizugehörigkeit","Schulnoten und Religion","Mietvertrag und Heimatrecht"],"Beim Hausbesuch überprüfte die Fürsorgerin vor allem Sauberkeit, Ordnung und Hygiene, bis hin zum „distanzlosen Öffnen der Kästen“. Laut Folie war das jahrzehntelang gängige Praxis. Maßstab war die normierte kleinbürgerliche Familie, die viele Arbeiterfamilien gar nicht erfüllen konnten.",[("rw",14),("rw",16)])
MATCH("rot-erfassen",[10],"Was bedeutet was im Amt des Roten Wien?",[("Hilfsfürsorgerin","stammt aus dem Arbeitermilieu, schlechter gestellt"),("Kinder-Evidenzkataster","fasst alle betreuten Kinder einheitlich zusammen"),("Nachschau","zentrale Kontrollaufgabe der Fürsorgerin")],"Hilfsfürsorgerinnen stammten aus dem Arbeitermilieu und waren schlechter gestellt; ihr Einsatz ab 1926 sollte den schwierigen Kontakt zu den Müttern erleichtern. Der Kinder-Evidenzkataster fasste alle betreuten Kinder einheitlich zusammen, die Nachschau war die zentrale Kontrollaufgabe. Das Amt war damit sehr systematisch organisiert.",[("rw",15),("rw",16)])
TF("rot-erfassen",[12],"Hausbesuche dienten im Roten Wien auch der Disziplinierung der Mütter.",True,"Hausbesuche dienten im Roten Wien auch der Disziplinierung der Mütter, bis zur Androhung, ihre Kinder wegzunehmen. Hilfe war also an Wohlverhalten nach bürgerlichem Maßstab geknüpft. Diese Seite des Roten Wien gehört genauso zur Prüfungsantwort wie die Errungenschaften.",[("rw",16)])
MC("rot-jugendamt",[8],"Was übernahm die Gemeinde Wien mit der Generalvormundschaft?","Die Vormundschaft über alle in Wien ledig geborenen Kinder",["Das Vermögen aller Waisenkinder","Die Aufsicht über alle Volksschulen","Die Pflege aller Kranken"],"Mit der Generalvormundschaft übernahm die Gemeinde Wien die Vormundschaft über alle in Wien ledig geborenen Kinder, die „Mündel“. Ausnahme waren Fälle mit männlichen Verwandten. Mütter konnten die rechtliche Obsorge nicht übernehmen, das Jugendamt registrierte, überwachte und beriet.")
MC("rot-jugendamt",[],"Bis wann konnten Mütter unehelicher Kinder laut Folie keine rechtliche Obsorge übernehmen?","1989",["1934","1954","2000"],"Laut Folie konnten Mütter unehelicher Kinder bis 1989 keine rechtliche Obsorge übernehmen; die Folie setzt „SIC!“ dazu. 1954 kam zwar eine erste Lockerung, die generelle Übertragung erst 1989. Das zeigt, wie lange die Kontrolle lediger Mütter rechtlich verankert blieb.",[("rw",12),("n",27),("zs",9)])
TF("rot-jugendamt",[],"Uneheliche Kinder standen bis zur Volljährigkeit mit 21 Jahren unter der Vormundschaft der Gemeinde Wien.",True,"Uneheliche Kinder standen bis zur Volljährigkeit mit 21 Jahren unter der Vormundschaft der Gemeinde Wien. Die allgemeine Zuständigkeit des Jugendamts reichte dagegen bis 18. Uneheliche Kinder waren also länger unter Aufsicht als andere.",[("rw",12)])
MC("rot-verw",[12],"Wen stufte man im Roten Wien als „verwahrlosungsgefährdet“ ein?","Uneheliche Kinder oder Kinder, die nur mit der Mutter aufwuchsen",["Kinder, deren Eltern im Gemeindebau wohnten","Kinder, die einen Kindergarten besuchten","Kinder von Fürsorgerinnen"],"Als „verwahrlosungsgefährdet“ galten schon uneheliche Kinder oder Kinder, die nur mit der Mutter aufwuchsen. Maßstab war das Vater-Mutter-Kind-Familienmodell. Viele Arbeiterfamilien konnten dieses bürgerliche Ideal aus sozialen Gründen gar nicht erfüllen.")
TF("rot-verw",[12],"Der Begriff „Verwahrlosung“ war eng und klar definiert.",False,"„Verwahrlosung“ war weit gefasst: ein Kampfbegriff für alle festgestellten „Mängel“, der das Eingreifen legitimierte. Gerade weil er so unscharf war, konnte er auf viele Familien angewandt werden. Wie der Begriff gedeutet wurde, ändert sich von Epoche zu Epoche.")
MC("rot-aichhorn",[13],"Wie sah Aichhorn „Verwahrlosung“?","Als individuelle Reaktion auf soziale und psychische Erfahrungen",["Als vererbte Eigenschaft","Als Charakterschwäche","Als Folge fehlender Religion"],"Aichhorn sah Verwahrlosung als individuelle Reaktion auf soziale und psychische Erfahrungen, nicht als Erbe oder Charakterschwäche. Der Verwahrloste ist für ihn nicht Störenfried, sondern „hilfsbedürftige Person“. Das war ein Bruch mit der moralischen Deutung der Monarchie.",[("rw",18)])
MC("rot-aichhorn",[13],"Was änderte Aichhorn in Oberhollabrunn?","Prügelstrafe abgeschafft, keine verschlossenen Türen",["Einführung von Drill und Zucht","Reine Beschäftigung in der Fabrik","Verlegung aller Kinder in Pflegefamilien"],"In Oberhollabrunn schaffte Aichhorn die Prügelstrafe ab, es gab keine verschlossenen Türen, und das Gespräch trat an die Stelle der Strafe. Das war ein Bruch mit den Methoden der Straferziehungsanstalten. 1921 wurde die Einrichtung aus Kostengründen aufgelöst.",[("rw",38)])
MC("rot-aichhorn",[13],"Als was verstand Aichhorn die Rolle des Erziehungsberaters?","„Verständnisvoller Verbündeter“ der Verwahrlosten",["Strenger Vertreter der Behörde","Beobachter ohne jeden Kontakt","Polizeilicher Ermittler"],"Als Erziehungsberater verstand sich Aichhorn als „verständnisvoller Verbündeter“ der Verwahrlosten. Hinter dem Konzept stehen die Psychoanalyse und das Ziel, Familien zu unterstützen statt Kinder zu bestrafen. Später arbeitete Rosa Dworschak mit ihm in der Erziehungsberatung.",[("rw",23)])
MC("rot-aichhorn",[13],"Auf welcher theoretischen Grundlage arbeitete Aichhorn?","Psychoanalyse",["Rassenhygiene","Katholische Soziallehre","Betriebswirtschaft"],"Aichhorn arbeitete auf Grundlage der Psychoanalyse; er machte selbst eine Analyse bei Sigmund Freud. Er vermittelte die Psychoanalyse auch den Fürsorgerinnen. Damit kam ein verstehender Zugang in die Jugendfürsorge.",[("rw",20),("rw",22)])
TF("rot-aichhorn",[13],"Oberhollabrunn wurde Vorbild für die Umgestaltung der Anstalten Eggenburg und Weinzierl.",True,"Oberhollabrunn wurde Vorbild für die Umgestaltung der Anstalten Eggenburg und Weinzierl. Besserungsanstalten wurden zu Erziehungsfürsorgeanstalten. Aichhorns Ansatz wirkte so über seine eigene Einrichtung hinaus.",[("rw",39)])
MC("rot-aichhorn",[13],"Was gilt als Zitat Aichhorns zur Anstaltserziehung?","„Das dissoziale Kind braucht ein Milieu, das ihm Bewegungsfreiheit gibt.“",["„Ein verwahrlostes Kind ist ein Krankheitsherd.“","„Es soll nur der befürsorgt werden, welcher der Fürsorge bedarf.“","„Überleben kann nur, wer arbeitet.“"],"„Das dissoziale Kind braucht ein Milieu, das ihm Bewegungsfreiheit gibt“ stammt aus Aichhorns Schrift „Über die Erziehung in Besserungsanstalten“ von 1923. Gemeint ist: Zwang und Strafe verstärken Verwahrlosung, ein freieres Umfeld ermöglicht Beziehung und Veränderung.",[("rw",37)])
MC("rot-kinderstube",[13,26],"Was nimmt die Kinderstube von 1926 laut Folie vorweg?","Case Work",["Das Säuglingswäschepaket","Den Verbindungsdienst","Die Heimkommission"],"Die Kinderstube von 1926 ergänzte die Erziehungsberatung mit Spiel und Lernhilfe. Dort gab es erstmals Fallbesprechungen im Team. Damit nahm sie laut Folie das spätere Case Work vorweg, das später aus den USA kam.",[("rw",24)])
TF("rot-kinderstube",[],"Die Erziehungsberatung im Wiener Jugendamt begann 1919 mit Franz Winkelmayer.",True,"Die Erziehungsberatung im Wiener Jugendamt begann 1919 mit Franz Winkelmayer. Seine spätere Rolle zeigt die Brüche der Geschichte: 1943 leitete er kommissarisch das Erziehungsheim Am Spiegelgrund. Personen aus dem Roten Wien wirkten also auch im NS-System mit.",[("rw",18),("z",2)])
MC("rot-dwor",[26],"Welche Rolle spielte Rosa Dworschak für das Case Work?","Entscheidende Vermittlerin unter ihren Kolleginnen",["Gründerin des Elberfelder Systems","Erfinderin der KÜST-Intelligenztests","Autorin von „Social Diagnosis“"],"Rosa Dworschak war die entscheidende Vermittlerin des Case Work unter ihren Kolleginnen. Sie stand in der Tradition Aichhorns und machte die Methode bekannt, als sie in Österreich noch nicht etabliert war. 1949 baute sie das Institut für Erziehungshilfe auf.",[("rw",28)])
MC("rot-dwor",[],"Wo erwarb Rosa Dworschak ihre Fürsorgeausbildung?","Bei Ilse Arlts Vereinigten Fachkursen",["An Salomons Akademie in Berlin","Bei Mary Richmond in Baltimore","An der Akademie für Sozialarbeit"],"Rosa Dworschak absolvierte Ilse Arlts Vereinigte Fachkurse, Abschluss 1918, danach wurde sie im Wiener Jugendamt angestellt. Sie arbeitete als Sprengelfürsorgerin und ab 1923 mit Aichhorn in der Erziehungsberatung. Ihre Biografie verbindet Arlt, Rotes Wien und Case Work.",[("rw",25)])
TF("rot-dwor",[],"Der historische Name des Barackenlagers in Ottakring ist laut Folie Ausdruck rassistisch-eugenischer Ideologie.",True,"Der historische Name des Barackenlagers in Ottakring ist laut Folie Ausdruck rassistisch-eugenischer Ideologie; darum kürzt die Folie ihn ab und nennt ihn problematisch. Dworschaks „Dorfgeschichten aus der Großstadt“ erzählen von diesem Lager. Es wurde 1952 abgerissen.",[("rw",25),("rw",26)])
MC("rot-heime",[11],"Was gilt als zentrale Leistung des Roten Wien in der Fremdunterbringung?","Schrittweise Umgestaltung von Anstalten zu Heimen",["Völlige Abschaffung der Kindesabnahme","Unterbringung aller Kinder bei Verwandten","Schließung aller Pflegefamilien"],"Als zentrale Leistung des Roten Wien gilt die schrittweise Umgestaltung von Anstalten zu Heimen: mehr Licht, mehr Platz, Unterscheidung nach heilpädagogischen Gesichtspunkten. Bisher wurden abgenommene Kinder primär in Anstalten verwahrt. Der Mangel an Plätzen blieb trotzdem groß.",[("rw",30)])
MC("rot-heime",[11],"Wo stand „Wer Kindern Paläste baut, reißt Kerkermauern nieder!“?","Beim Eingang der Kinderübernahmestelle",["Auf dem Rathaus","Am Karl-Marx-Hof","Im Jugendamt Ottakring"],"„Wer Kindern Paläste baut, reißt Kerkermauern nieder!“ ist Tandlers Motto und stand beim Eingang der Kinderübernahmestelle, der KÜST. Der Satz steht für die Abkehr von der Anstalt hin zum Heim. Später wurde er für die Zeit nach der KÜST abgewandelt.",[("rw",30)])
MC("rot-kuest",[11],"Wofür diente die KÜST als „Drehscheibe“?","Abklärung über die weitere Unterbringung in Pflegefamilie oder Heim",["Vermittlung von Lehrstellen für Jugendliche","Aufnahme von Müttern zur Entbindung","Ausbildung von Hilfsfürsorgerinnen"],"Die KÜST war Drehscheibe für abgenommene Kinder: Nach einigen Wochen Beobachtung und psychologischen Tests wurde über Pflegefamilie oder Heim entschieden. Die Folie nennt sie eine „panoptische Anlage“, das überstellte Kind wurde zum Objekt der Beobachtung. Sie galt zugleich als „Juwel der modernen Kinderfürsorge“.")
TF("rot-kuest",[11],"Die Begutachtung auf Basis der KÜST-Tests blieb jahrzehntelang üblich.",True,"Die Folie vermerkt eine jahrzehntelange Begutachtung auf Basis der KÜST-Tests, etwa mit den Kleinkindertests von Bühler und Hetzer. Die Testverfahren waren defizitorientiert und klassifizierten Kinder. So wirkte das Erbe des Roten Wien weit über das Rote Wien hinaus.",[("rw",34)])
MC("rot-kuest",[],"Wie beschreibt eine ehemalige Verbindungsfürsorgerin den Aufenthalt in der KÜST?","Körperlich gut behandelt, aber wie „in einer Glasbox“",["Hart, doch sehr kindgerecht","Liebevoll, aber gesundheitlich gefährlich","Völlig frei von jeder Beobachtung"],"Eine ehemalige Verbindungsfürsorgerin erinnert sich: körperlich gut behandelt, aber wie „in einer Glasbox“. Das Zitat zeigt die Spannung der KÜST: Die Betreuung konzentrierte sich primär auf das gesundheitliche Wohl, emotionale Bedürfnisse kamen zu kurz.",[("rw",35)])
MC("rot-kuest",[11],"Welche Funktion hatte das Kinderheim Schloss Wilhelminenberg ab 1927?","Heilpädagogische Beobachtungsstelle für „auffällige“ Kinder",["Ausbildungsstätte für Fürsorgerinnen","Sitz der Wiener Sängerknaben","Mutter-Kind-Heim für 25 Mütter"],"Ab 1927 war das Kinderheim Schloss Wilhelminenberg heilpädagogische Beobachtungsstelle für „auffällige“ Kinder. Klassifiziert wurde mit defizitorientierten Testverfahren. 1934 kam es an die Sängerknaben, später war Wilhelminenberg ein Ort schwerer Gewalt an Heimkindern.",[("rw",36),("t",2)])
MULTI("rot-neu",[11],"Was nennt die Folie als relevante Neuerungen des Roten Wien?",["Erweiterung der Jugendfürsorge bis zum 18. Lebensjahr","Vereinheitlichung im städtischen Jugendamt","Ziehkindergesetz","Mehr Berufsfürsorgerinnenposten"],["Abschaffung des Hausbesuchs"],"Die letzte Folie zum Roten Wien nennt Heimbauten, Jugendfürsorge bis 18, Familienfürsorge, Zusammenarbeit der Stellen, Vereinheitlichung im Jugendamt, Ziehkindergesetz und mehr Berufsfürsorgerinnen. Dazu kommen bauliche Tätigkeit, Verankerung in der Familienfürsorge und Zusammenarbeit öffentlicher und privater Stellen. Einiges davon wirkte über Jahrzehnte.")
MATCH("rot-aichhorn",[11],"Wer steht wofür im Roten Wien?",[("Julius Tandler","Wohlfahrtsamt, Stadtrat"),("Hugo Breitner","Steuern, Finanzstadtrat"),("August Aichhorn","Erziehungsberatung, Oberhollabrunn"),("Rosa Dworschak","Sprengelfürsorge, Case Work")],"Julius Tandler leitete als Stadtrat das Wohlfahrtsamt, Hugo Breitner finanzierte als Finanzstadtrat Wohnbau und Fürsorge mit seinen Steuern. August Aichhorn steht für Erziehungsberatung und Oberhollabrunn, Rosa Dworschak für Sprengelfürsorge und Case Work. Vier Namen, die in einer Überblicksfrage zum Roten Wien vorkommen können.",[("rw",6),("rw",8),("rw",20),("rw",28)])
ORD("rot-kuest",[11],"Reihe die Eckdaten des Roten Wien.",[("1919","Beginn der Erziehungsberatung"),("1921","Wohlfahrtsamt"),("1925","Eröffnung der KÜST"),("1927","Säuglingswäschepaket")],"1919 begann die Erziehungsberatung, 1921 folgte Tandlers Wohlfahrtsamt, 1925 die Eröffnung der KÜST und 1927 das Säuglingswäschepaket für alle Mütter. Die Reihe zeigt, wie schnell das Rote Wien ein engmaschiges Netz aus Beratung, Begutachtung und Erfassung aufbaute.",[("z",2),("rw",8),("rw",14)])

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

MC("aut-grund",[14,9],"Was geschah mit dem Anrecht auf Fürsorge im Austrofaschismus?","Es wurde zurückgenommen, zugunsten der „alten Wohltäterei“",["Es wurde gesetzlich auf alle ausgeweitet","Es wurde erstmals formuliert","Es galt nur noch für die Sozialdemokratie"],"Im Austrofaschismus wurde das allgemeine Anrecht auf Fürsorge zurückgenommen, zugunsten der „alten Wohltäterei“, ein Begriff, der von Tandler stammt. Grundlage war die katholische Soziallehre. Mittel flossen an konfessionelle Einrichtungen, öffentliche wurden privatisiert.")
MC("aut-grund",[14],"Was passierte mit dem Kinderheim Schloss Wilhelminenberg 1934?","Es wurde aufgelassen und den Sängerknaben übergeben",["Es wurde zum Gaujugendamt umgebaut","Es wurde vergrößert und saniert","Es wurde zur Ausbildungsstätte"],"1934 wurde das Kinderheim Schloss Wilhelminenberg aufgelassen und den Sängerknaben übergeben. Ein Beispiel für die Privatisierung öffentlicher Einrichtungen. Die Arbeiterzeitung schrieb: „Statt armer Kinder eine klerikale Institution!“",[("t",2),("t",4)])
TF("aut-grund",[14],"Der Ständestaat baute die Fürsorgeangebote strukturell massiv aus.",False,"Im Ständestaat gab es keine strukturell-organisatorischen Neuerungen und keinen weiteren Ausbau. Stattdessen flossen mehr Mittel an konfessionelle Einrichtungen. Die Not stieg, die Mittel der Fürsorgerinnen sanken.",[("t",2)])
MC("aut-grund",[14],"Was war die Vaterländische Front?","Monopolorganisation, die als Einheitspartei fungierte",["Ein Verein für Kinderschutz","Der Berufsverband der Fürsorgerinnen","Eine Abteilung des Jugendamtes"],"Die Vaterländische Front wurde im Mai 1933 unter Dollfuß gegründet. Nach der Ausschaltung von Parlament und Opposition fungierte sie als Monopolorganisation und Einheitspartei. Sie ist der politische Rahmen des Austrofaschismus.",[("t",6)])
MC("aut-familie",[14],"Wer bekam eine Wohnung in den Familienasylen von 1934?","Nur „geordnete Familien“ mit zwei oder mehr Kindern",["Alle Obdachlosen ohne Heimatrecht","Ledige Mütter mit Säuglingen","Mitglieder der Sozialdemokratie"],"Wohnungen in den Familienasylen von 1934 bekamen nur „geordnete Familien“ mit zwei oder mehr Kindern. Dazu kam der Einsatz von Fürsorgerinnen, Arzt und Seelsorger zur „Erziehung zur gesunden Familie“. Hilfe war an katholische Familiennormen geknüpft.")
TF("aut-familie",[14,12],"Die Bevölkerungspolitik des Roten Wien wurde im Austrofaschismus mit sittlich-katholischen Werten verknüpft.",True,"Die Bevölkerungspolitik des Roten Wien wurde im Austrofaschismus mit sittlich-katholischen Werten verknüpft. Auf der Folie steht: christliche Familie gleich „erbgesunde Familie“. Eugenische Gedanken liefen also über die politischen Brüche hinweg weiter.",[("t",7)])
MC("aut-familie",[14],"Wo wurden Fürsorgerinnen im Austrofaschismus ausgebildet?","An der katholischen „Pichlschule“",["An der Sozialen Frauenschule der Stadt Wien","An Arlts Sozialakademie","An der Lehranstalt für gehobene Sozialberufe"],"Fürsorgerinnen wurden an der katholischen „Pichlschule“ ausgebildet. Inhalte waren religiöse und pronatalistische Themen, also Geburtenförderung, dazu Gesundheitsfürsorge, Mutterschutz und Wochenbettpflege. Die Ausbildung folgte der katholischen Soziallehre.",[("t",8)])
MC("aut-not",[14],"Wozu diente das Fürsorgebuch?","Einsparung von Verwaltungskosten und Überprüfbarkeit der Klient*innen",["Vermerk von Schulnoten der Kinder","Abrechnung der Breitner-Steuern","Nachweis der Parteimitgliedschaft"],"Das Fürsorgebuch sollte Verwaltungskosten sparen und die Klient*innen überprüfbar machen. Unterstützung gab es vor allem für kinderreiche Familien. Zugleich stieg die Not: Eine Fürsorgerin erinnert sich an 20 oder 30 Brotmarken für 50 bis 70 Wartende.")
TF("aut-erz",[14],"Für die Übernahme eines Pflegekindes war ein katholisches Religionsbekenntnis Voraussetzung.",True,"Für die Übernahme eines Pflegekindes war ein katholisches Religionsbekenntnis Voraussetzung. Die Fremdunterbringung erfolgte zudem in katholischen Privatanstalten. Fürsorgerinnen überwachten neben Hygiene auch die „sittlich-religiöse Erziehung“.")
MC("aut-erz",[14],"Welcher Begriff kehrte im Austrofaschismus zurück?","„Anstalt“ anstelle von „Heim“",["„Heim“ anstelle von „Anstalt“","„Klient“ anstelle von „Partei“","„Sozialarbeiterin“ anstelle von „Fürsorgerin“"],"Im Austrofaschismus kehrte der Begriff „Anstalt“ anstelle von „Heim“ zurück. Das ist ein sprachlicher Rückschritt gegenüber dem Roten Wien, das bewusst von Heimen sprach. Sprache zeigt hier den Wandel der Haltung.")

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

MC("ns-system",[15],"Was wurde 1938 aus dem Wiener Jugendamt?","Das „Gaujugendamt Niederdonau“",["Die Soziale Frauenschule","Die Nationalsozialistische Volkswohlfahrt","Die Kinderübernahmsstelle"],"1938 wurde das Wiener Jugendamt zum „Gaujugendamt Niederdonau“. Strukturell wurde das System weitergeführt, das Sprengelsystem sogar ausgebaut. Die vorhandenen Strukturen des Erfassens wurden so für das Regime nutzbar.")
MC("ns-system",[15],"Was war laut Folie die entscheidende Veränderung im NS-Fürsorgesystem?","Die ideologische Ausrichtung: Dienst am Staat statt an Hilfsbedürftigen",["Der komplette Abbau aller Fürsorgestellen","Die Rückkehr zur katholischen Wohltätigkeit","Die Einführung eines Rechtsanspruchs für alle"],"Entscheidend war die ideologische Ausrichtung: Dienst am Staat statt Dienst an Hilfsbedürftigen. Bestehende Bestimmungen wurden außer Kraft gesetzt, gegen die als nicht „unterstützungswürdig“ Geltenden wurden Zwangsmaßnahmen verhängt. Wer nicht zur „Volksgemeinschaft“ gezählt wurde, war ausgeschlossen.")
TF("ns-system",[15],"Das NS-Regime führte bestehende Fürsorgeeinrichtungen strukturell weiter.",True,"Das NS-Regime führte die bestehenden Fürsorgeeinrichtungen strukturell weiter. Der Bruch lag in der Ideologie, nicht in den Strukturen: Dieselben Instrumente dienten nun Auslese und Ausschluss. Das macht die Kontinuitäten der Nachkriegszeit verständlich.",[("t",12)])
MC("ns-ausschluss",[16],"Wen schloss die Entscheidung vom 21. August 1938 von der Berufsvormundschaft aus?","Jüdische Kinder und als „Zigeuner“ bezeichnete Kinder",["Alle unehelichen Kinder","Alle Kinder unter sechs Jahren","Alle Kinder ohne Heimatrecht"],"Die Entscheidung vom 21. August 1938 schloss jüdische Kinder und als „Zigeuner“ bezeichnete Kinder von der Berufsvormundschaft aus. Die Folie zitiert die Formulierung und benennt sie als Rassismus und Antisemitismus. Juden und Jüdinnen wurden insgesamt aus der Wohlfahrt ausgeschlossen.",[("t",14)])
MC("ns-ausschluss",[15],"Was geschah 1938 mit den Ausbildungsstätten für Fürsorgerinnen?","Alle wurden geschlossen, eine neue Soziale Frauenschule entstand",["Sie blieben unverändert in kirchlicher Hand","Sie wurden zu Akademien aufgewertet","Sie wurden an Universitäten angegliedert"],"1938 wurden alle Ausbildungsstätten für Fürsorgerinnen geschlossen, eine neue Soziale Frauenschule entstand. Die neue Ausbildung diente der Gleichschaltung; SS-Ärzte vermittelten Erb- und Rassenpflege. Das Niveau war geringer als im Roten Wien.",[("t",15),("t",23),("z",2)])
TF("ns-ausschluss",[15],"Fürsorge und Polizei arbeiteten getrennt voneinander.",False,"Fürsorge und Polizei arbeiteten eng zusammen: Die Zusammenarbeit mit Polizei und Gestapo sollte Klient*innen unter die Kontrolle des Regimes zwingen. Private Einrichtungen wurden aufgelöst oder eingegliedert. Der Kontakt mit der Fürsorge konnte damit gefährlich werden.",[("t",14)])
MC("ns-asozial",[16],"In welchen Begriff wurde „Verwahrlosung“ umgedeutet?","„Asozialität“",["„Sozialanpassung“","„Erziehungsnotstand“","„Schwererziehbarkeit“"],"„Verwahrlosung“ wurde zu „Asozialität“ umgedeutet, also zu „gemeinschaftswidrigem Verhalten“. An die Stelle der Erziehung trat der Ausschluss. In der Nachkriegszeit wurde dann „Sozialanpassung“ zum neuen Maßstab.",[("t",18),("n",36)])
MC("ns-asozial",[16],"Was ersetzte die pädagogischen Konzepte des Roten Wien?","Disziplin und Ordnung, Heime mit Drill und Zucht",["Psychoanalytische Beratung","Freiwillige Elternschulen","Offene Wohngemeinschaften"],"Disziplin und Ordnung ersetzten die pädagogischen Konzepte des Roten Wien, Heime arbeiteten mit Drill und Zucht. Heimkinder wurden 1938 zudem zwangsweise in HJ und BDM eingegliedert. Aichhorns verstehender Ansatz war damit beendet.",[("t",19)])
TF("ns-asozial",[16],"An die Stelle von Erziehung trat laut Folie der Ausschluss, in letzter Konsequenz mit tödlichen Folgen.",True,"Laut Folie trat an die Stelle der Erziehung der Ausschluss, in letzter Konsequenz mit tödlichen Folgen. Das ist eine zentrale Aussage zu den Auswirkungen auf Klient*innen. Am Spiegelgrund wurde das grausame Wirklichkeit.",[("t",22)])
MC("ns-asozial",[22],"Zu wem errichtete das Jugendamt einen Verbindungsdienst zur restlosen Erfassung?","Zu HJ und Nationalsozialistischer Volkswohlfahrt (NSV)",["Zu Kirche und Vaterländischer Front","Zu den Gewerkschaften und der Caritas","Zu Schweizer Pflegefamilien"],"Das Jugendamt errichtete einen Verbindungsdienst zur Hitlerjugend und zur Nationalsozialistischen Volkswohlfahrt, der NSV, zur restlosen Erfassung. Stichwort ist Zwangspädagogisierung. Fürsorgerinnen wurde der Beitritt zur NSV nahegelegt.",[("t",22)])
MC("ns-spalt",[16],"Worauf konzentrierte sich die NS-Wohlfahrtspflege auf der helfenden Seite?","Auf die „erbgesunde“, „arische“ Familie als „Urzelle des Volkes“",["Auf alle Armen, unabhängig von Herkunft","Auf Alte und Kranke in Anstalten","Auf Alleinerziehende und ihre Kinder"],"Auf der helfenden Seite konzentrierte sich die NS-Wohlfahrtspflege auf die „erbgesunde“, „arische“ Familie als „Urzelle des Volkes“. Für alle anderen wirkte die Fürsorge an „Selektion und Auslese“ mit. Geburtenförderung und Selektion waren zwei Seiten derselben Politik.",[("t",32)])
TF("ns-spalt",[16],"Für kinderreiche Familien, die als „der Hilfe würdig“ galten, gab es umfassende Unterstützung.",True,"Kinderreiche Familien, die als „der Hilfe würdig“ galten, bekamen umfassende Unterstützung und eigene Budgets. Das meint die „gespaltene Fürsorge“: großzügige Hilfe für die einen, Auslese für die anderen. Rechtliche Basis der Auslese waren die Nürnberger Rassengesetze.",[("t",33)])
MC("ns-spalt",[16],"Woran wirkte das Jugendamt beim „Mutterkreuz“ mit?","Auswahl der Mütter über Erhebungen und Empfehlungen",["Herstellung und Verkauf der Auszeichnung","Überweisung einer monatlichen Rente","Ausschluss aller Mütter mit Beruf"],"Beim „Mutterkreuz“ wirkte das Jugendamt an der Auswahl der Mütter mit, über Erhebungen und Empfehlungen. Laut Folie erhielten es 1939 38.663 kinderreiche Mütter. Die Fürsorge war damit direkt an der Belohnung der „erwünschten“ Familien beteiligt.",[("t",34)])
MC("ns-erfassen",[16],"Wozu diente die Übergabe des Säuglingswäschepakets in der NS-Zeit zusätzlich?","Zur Erhebung von Erbkrankheiten",["Zur Spendensammlung für den Krieg","Zur Werbung für die Ausbildung","Zur Verteilung von Lebensmittelmarken"],"In der NS-Zeit diente die Übergabe des Säuglingswäschepakets zusätzlich der Erhebung von Erbkrankheiten. Ein Instrument aus dem Roten Wien wurde so für die Erbkartei umgenutzt. Hausbesuch, Verbindungsdienst und Schulfürsorge dienten ebenfalls dem totalen Erfassen.",[("t",35)])
MC("ns-erfassen",[16],"Wie viele Personen erfasste die „Erbkartei“ im April 1940?","406.537",["7.868","38.663","1.235"],"Im April 1940 erfasste die Erbkartei 406.537 Personen, im April 1939 waren es noch 7.868. Der rasante Anstieg zeigt, wie effizient die vorhandenen Erfassungswege genutzt wurden. Für viele war der Kontakt mit der Fürsorge gefährlicher, als er half.",[("t",36)])
MC("ns-personal",[15],"Wozu verpflichtete der Diensteid vom 16. März 1938?","Zu Treue und Gehorsam gegenüber Adolf Hitler",["Zum Austritt aus der Kirche","Zur Mitgliedschaft in der SS","Zum Verzicht auf das Gehalt"],"Der Diensteid vom 16. März 1938 verpflichtete zu Treue und Gehorsam gegenüber Adolf Hitler. Ausgenommen waren „jüdische Beamte“, die aus dem Dienst entfernt wurden, ebenso politisch Opponierende. Politische Schulungen und Denunziationsgefahr prägten danach das Klima.",[("t",27)])
MC("ns-personal",[15],"Wer vermittelte Inhalte an der neuen Sozialen Frauenschule?","SS-Ärzte",["Pfarrer","Psychoanalytiker","Vertreterinnen der Frauenbewegung"],"An der neuen Sozialen Frauenschule vermittelten SS-Ärzte die Grundgedanken der Erbgesundheits- und Rassenpflege. Das Niveau war geringer als im Roten Wien. Die Ausbildung diente der Gleichschaltung des Berufs.",[("t",24)])
MC("ns-personal",[15],"Welche zwei Funktionen wurden eingeführt und trennten kontrollierende und helfende Kompetenzen?","Organisationsfürsorgerin (ORGA) und Fachfürsorgerin für Erziehungsberatung",["Hauptfürsorgerin und Hilfsfürsorgerin","Berufsvormund und Listenvormund","Waisenmutter und Armenrätin"],"Eingeführt wurden die Organisationsfürsorgerin (ORGA) und die Fachfürsorgerin für Erziehungsberatung; das trennte kontrollierende und helfende Kompetenzen. De facto hatte die ORGA deutlich mehr Macht. Diese Teilung blieb nach dem Krieg noch lange bestehen.",[("t",25)])
MULTI("ns-personal",[15],"Welche Sanktionen drohten politisch nicht konformen Mitarbeiter*innen?",["Verbot von Hausbesuchen","Versetzung in weit entfernte Sprengel","Versetzung nach Polen","Strafeinsatz in kriegswichtigen Betrieben"],["Aufstieg zur Amtsleitung"],"Politisch nicht konformen Mitarbeiter*innen drohten Sanktionen. Das Klima in den Bezirksjugendämtern war von Angst und Einschüchterung geprägt, dazu kam die Gefahr der Denunziation. Das erklärt, warum Widerstand meist nur verdeckt möglich war.",[("t",30)])
MC("ns-spiel",[15],"Wie sabotierten manche Fürsorgerinnen die „erbbiologische Bestandsaufnahme“?","Sie beantworteten Fragen in den Sippenbögen bewusst anders",["Sie verließen geschlossen das Amt","Sie veröffentlichten die Listen im Ausland","Sie verweigerten offen den Diensteid"],"Manche Fürsorgerinnen beantworteten die Fragen in den Sippenbögen bewusst anders: „Man hat sabotiert“, eine nur äußere Anpassung. Das zeigt, dass es Handlungsspielräume gab. Andere nutzten die Situation dagegen aus Opportunismus für ihre Karriere.",[("t",36)])
TF("ns-spiel",[15],"Alle Fürsorgerinnen leisteten im NS-Regime passiven Widerstand.",False,"Passiven Widerstand leisteten nicht alle, das war durchaus unterschiedlich. Die Erinnerungen nennen auch Anpassung, Opportunismus und illegale Nationalsozialist*innen unter den Fürsorgerinnen. Ein pauschales Bild der Berufsgruppe wäre falsch.",[("t",28),("t",37)])
TF("ns-spiegel",[16],"Am Spiegelgrund sind 789 Todesopfer dokumentiert, die überwiegende Mehrheit in der Säuglingsabteilung (Pavillon 15).",True,"Am Spiegelgrund sind 789 Todesopfer dokumentiert, die überwiegende Mehrheit in der Säuglingsabteilung, dem Pavillon 15. Die Kinderfachabteilung der Anstalt Am Steinhof wurde laut Folie zum Ort der Vernichtung. Jugendfürsorge, KÜST und Spiegelgrund waren organisatorisch eng verbunden.",[("t",38)])
MC("ns-spiegel",[16],"Was zeigt die Geschichte von Otto Zipser laut Folie?","Enge Verbindung von Jugendfürsorge, KÜST und Spiegelgrund",["Dass Einweisungen nur auf Elternwunsch erfolgten","Dass die Anstalt von der Fürsorge unabhängig war","Dass nur Kinder unter sechs betroffen waren"],"Otto Zipser wurde 1940 eingewiesen, vermutlich nach Denunziation durch Hausbewohner. Seine Geschichte zeigt die enge Verbindung von Jugendfürsorge, KÜST und Spiegelgrund. Die Folie spricht von der Fürsorge als Zuträger des Selektions- und Vernichtungsprogramms.",[("t",39)])
TF("ns-spiegel",[16],"Für viele Überlebende war der Spiegelgrund der Ausgangspunkt für jahrelange weitere Heimunterbringungen.",True,"Für viele Überlebende war der Spiegelgrund der Ausgangspunkt für jahrelange weitere Heimunterbringungen. Mitunter nahmen dort auch lebenslange psychiatrische Martyrien ihren Anfang. Das Unrecht endete für sie nicht mit Kriegsende.",[("t",40)])
MC("ns-krieg",[15],"Wie veränderte der Krieg die Fürsorge?","Massive Reduktion der Mittel, Stabilisierung der „Heimatfront“",["Mehr Mittel für Beratung und Therapie","Ende aller Hausbesuche ab 1939","Rückgabe der Heime an private Träger"],"Mit der Dauer des Krieges wurden die Fürsorgemittel massiv reduziert und für den Krieg eingesetzt; Fürsorge diente der Stabilisierung der „Heimatfront“. Neue Aufgaben waren die Betreuung von Umsiedlern, Flüchtlingen und Ausgebombten. Luftangriffe und fehlendes Personal erschwerten den Betrieb.")

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

TF("n-stunde",[17],"Nach 1945 wurde sofort ein neues Jugendwohlfahrtsgesetz beschlossen.",False,"Nach 1945 blieb die Jugendwohlfahrtsverordnung von 1940 zunächst Grundlage; ein neues Jugendwohlfahrtsgesetz kam erst 1954. Formal gab es einen Neubeginn, rechtlich wirkte NS-Recht aber fast ein Jahrzehnt weiter. Das ist ein Beispiel für Kontinuitäten.",[("n",2),("n",27)])
MC("n-stunde",[17],"Welche Verwaltungsreform gab es 1945?","Trennung von Gesundheitsfürsorge und Jugendwohlfahrt",["Eingliederung des Jugendamtes in die Polizei","Auflösung aller Fürsorgesprengel","Trennung von Sozialarbeit und Sozialpädagogik"],"1945 wurden Gesundheitsfürsorge und Jugendwohlfahrt getrennt, das Wiener Jugendamt wiederhergestellt. Die Fürsorgesprengel wurden als „kleine Reiche“ der Fürsorgerinnen beschrieben. Die Fürsorgerin hatte in ihrem Sprengel also große Macht.",[("n",2)])
MC("n-entnazi",[17],"Was war die Generalamnestie von 1947?","Formalrechtlicher Abschluss der „Entnazifizierung“",["Der Beginn der strengen Strafverfolgung","Eine Entschädigung für Opfer der Fürsorge","Das Verbot jeder Beschäftigung früherer Nationalsozialist*innen"],"Die Generalamnestie von 1947 war der formalrechtliche Abschluss der „Entnazifizierung“. Etwa 90 Prozent wurden wieder bei der Gemeinde Wien eingestellt. Viele Bedienstete waren 1945 nur kurz außer Dienst gestellt worden.")
MC("n-entnazi",[17],"Wie viele frühere Nationalsozialist*innen wurden nach 1947 wieder eingestellt?","Etwa 90 Prozent",["Etwa 10 Prozent","Etwa 50 Prozent","Niemand"],"Nach 1947 wurden etwa 90 Prozent der früheren Nationalsozialist*innen wieder bei der Gemeinde Wien eingestellt. In der Regel gab es nur kurzfristige Berufsverbote und einen Austausch der Amtsleiter. So blieben Personal und Haltungen über 1945 hinaus bestehen.",[("n",6)])
TF("n-entnazi",[17],"Die Erzählungen von Fürsorgerinnen nennen amtsinterne Konflikte wegen unterschiedlicher Erfahrungen in der NS-Zeit.",True,"Die Erzählungen von Fürsorgerinnen nennen amtsinterne Konflikte wegen unterschiedlicher Erfahrungen in der NS-Zeit: darüber, wer wie politisch tätig war, verfolgt wurde oder emigrieren musste. Täter*innen, Mitläufer*innen und Verfolgte arbeiteten nun wieder Tür an Tür.",[("n",7)])
MC("n-ausb",[17],"Woran orientierte sich der Lehrplan nach 1945?","An der medizinisch-gesundheitsfürsorgerischen Ausrichtung der Vorkriegszeit",["An modernen Methoden der US-Sozialarbeit","An der Soziologie der 1968er Bewegung","An einem neuen Universitätsstudium"],"Nach dem Krieg orientierte sich der Lehrplan an der medizinisch-gesundheitsfürsorgerischen Ausrichtung der Vorkriegszeit. Die Fächer „Nationalpolitische Schulung“ und „Erb- und Rassenkunde“ entfielen, sonst blieb vieles gleich. Die Ausbildung war praxisfern und hinkte internationalen Methoden nach.",[("n",10)])
MC("n-ausb",[23],"Ab wann war die Ausbildung auch für männliche Bewerber zugänglich?","Schuljahr 1948/49",["1912","1938","1976"],"Ab dem Schuljahr 1948/49 durften auch Männer die Ausbildung machen. Im Oktober 1949 gab es 76 weibliche und 6 männliche Schüler*innen. Der Beruf blieb also noch lange weiblich geprägt.",[("n",9)])
TF("n-ausb",[17],"Arlts Forderung nach interdisziplinärer Fürsorgeforschung fand in der Nachkriegszeit große Beachtung.",False,"Die Folie sagt, Arlts grundlegende Arbeiten wurden weder in Österreich noch international entsprechend beachtet. Die Rezeption internationaler Methoden war durch den NS unterbrochen. Arlts Forderung nach Fürsorgeforschung blieb so lange ungehört.",[("n",11)])
MC("n-ausb",[23],"Womit warb eine steirische Schule in den 1950er Jahren um Schülerinnen?","„Fraulich-mütterliches Wesen“ könne sich hier entfalten",["Hohes Gehalt und schnelle Karriere","Freie Arbeitszeit und Dienstwagen","Politische Mitbestimmung im Amt"],"Eine steirische Schule warb in den 1950er Jahren damit, dass sich hier ein „fraulich-mütterliches Wesen“ entfalten könne. Der Folder zeigt, wie lange die weibliche Rollenzuschreibung der geistigen Mütterlichkeit wirkte. Professionelle Kompetenz stand dabei im Hintergrund.",[("n",43)])
MC("n-ausb",[],"Warum galt der Beruf in den 1950ern und 1960ern als unattraktiv?","Geringe Entlohnung und niedriges Sozialprestige",["Zu viele Stellen für Männer","Zu kurze Arbeitszeiten","Zu hohe Anforderungen an Fremdsprachen"],"In den 1950ern und 1960ern galt der Beruf wegen geringer Entlohnung und niedrigem Sozialprestige als unattraktiv. Die Folge war ein „katastrophaler Nachwuchsmangel“. Die späteren Reformen reagierten auch darauf.",[("n",41)])
MC("n-alltag",[],"Was organisierte das Jugendamt nach dem Krieg mit Hilfe des Auslands?","Erholungsaufenthalte und Pflege, etwa in der Schweiz",["Studienplätze für Fürsorgerinnen","Wohnungsbau für Mütter in den USA","Auswanderung ganzer Familien"],"Nach dem Krieg organisierte das Jugendamt mit Hilfe des Auslands Erholungsaufenthalte und Pflege, etwa in der Schweiz; 1.010 Kinder wurden von Schweizer Familien in Pflege übernommen. Fürsorgerinnen verteilten auch Care-Güter und kämpften gegen Hunger und Krankheit.",[("n",14)])
TF("n-alltag",[18],"Dass viele Frauen allein für die Familie sorgten, wurde bei der Klage über „Jugendverwahrlosung“ berücksichtigt.",False,"Dass viele Frauen nach dem Krieg allein für die Familie sorgten, fand laut Folie keinerlei Berücksichtigung. Stattdessen wurden die Mütter für die „Jugendverwahrlosung“ verantwortlich gemacht. Die Linie der Schuldzuweisung an Mütter zieht sich durch die Epochen.",[("n",20)])
MC("n-alltag",[],"Was war bei der Suche nach zahlungspflichtigen Vätern ein Problem?","Akten waren vernichtet, Väter gefallen oder vermisst",["Väter zahlten aus Prinzip doppelt","Mütter durften keine Angaben machen","Die Gerichte waren nicht zuständig"],"Bei der Suche nach zahlungspflichtigen Vätern waren Akten vernichtet, Väter gefallen oder vermisst. Väter aus den Besatzungsmächten konnten nicht auf Unterhalt geklagt werden. Viele Mütter blieben so ohne Unterhalt.",[("n",18)])
MC("n-kontrolle",[17,18],"Was bedeutet die „Amts-Kapperl-Methode“?","Autorität nutzen, auch gegen den Willen der Leute",["Beratung in Uniform auf freiwilliger Basis","Spezielle Form der Gruppenarbeit","Verwaltungstechnik im Hausbesuch"],"Die „Amts-Kapperl-Methode“ heißt: Autorität nutzen, auch gegen den Willen der Leute. Eine Fürsorgerin erinnert sich, dass Kinder in der Früh einfach von zu Hause weggeholt wurden. Der in der NS-Zeit verstärkte Kontrollcharakter blieb so in der Nachkriegszeit bestehen.",[("n",25)])
TF("n-kontrolle",[17],"Hausbesuche waren in den 1950er Jahren in der Regel lange, angemeldete Gespräche.",False,"Eine Fürsorgerin berichtet von unangemeldeten, zwei- bis dreiminütigen Besuchen, nur um ein „Stricherl“ auf die Liste zu machen. Hausbesuche dienten vielen als Machtdemonstration und Pflichterfüllung, nicht als Gespräch. Die Überwachung der Mündel blieb bis in die 1980er Jahre zentral.",[("n",21)])
MC("n-kontrolle",[20],"Warum hatten Fürsorgerinnen lange nur ein Taferl mit einem Buchstaben am Tisch?","Um das soziale Gefälle zu betonen und einzuschüchtern",["Damit sich Klient*innen Namen leichter merken","Wegen Papiermangels nach dem Krieg","Weil es zu viele Namensgleichheiten gab"],"Das Taferl mit nur einem Buchstaben sollte das soziale Gefälle betonen und einschüchtern; Fürsorgerinnen blieben für Klient*innen namenlos. Erst Mitte der 70er Jahre kamen Namen auf die Tische. Manche schützte das Taferl auch vor zu großer Identifikation.",[("n",48)])
MC("n-kontrolle",[],"Wer hatte bis Ende der 1960er eine prominente Machtposition im Amt?","ORGAS und die überwiegend männlichen, autoritären Amtsleiter",["Die jungen Praktikant*innen","Die Klient*innen über Beiräte","Die Erziehungsberater*innen"],"Bis Ende der 1960er hatten die ORGAS und die überwiegend männlichen, autoritären Amtsleiter eine prominente Machtposition. „Die Behörde bin ich!“ brüllte einer davon laut einer Erinnerung ins Telefon. Gegen diese Hierarchie richtete sich später die Kritik der jungen Sozialarbeiterinnen.",[("n",49)])
MC("n-disz",[18],"Was wurde nach 1945 anstelle der „Asozialität“ zum Gradmesser?","„Sozialanpassung“",["„Selbstermächtigung“","„Volksgemeinschaft“","„Hilfe zur Selbsthilfe“"],"Nach dem Krieg wurde „Sozialanpassung“ zum Gradmesser und löste die NS-„Asozialität“ ab. Der Direktor von Eggenburg machte sie sogar am äußeren Erscheinungsbild fest. Mitte der 1950er rückte die „moralische und sittliche“ Verwahrlosung ins Zentrum.",[("n",36),("n",37)])
MC("n-disz",[18],"Womit begründete man Verwahrlosung in den 1950ern wie bisher?","Mit Berufstätigkeit und fehlender Aufsichtspflicht von Müttern",["Mit schlechter Bezahlung der Väter","Mit dem Fehlen von Kindergärten","Mit zu großzügigen Sozialleistungen"],"Wie bisher wurde Verwahrlosung mit der Berufstätigkeit und fehlenden Aufsichtspflicht der Mütter begründet. Das setzt die Linie der Verantwortungszuweisung an Mütter fort, die schon im Ersten Weltkrieg begann. Die soziale Lage der Familien blieb dabei ausgeblendet.",[("n",34)])
MC("n-disz",[18],"Welches Kinderbuch landete angeblich gewaltfördernd auf der schwarzen Liste?","„Tom Sawyer“",["„Pippi Langstrumpf“","„Heidi“","„Die Biene Maja“"],"„Tom Sawyer“ landete angeblich wegen gewaltfördernder Inhalte auf der schwarzen Liste. Das war Teil des Kampfs gegen „Schmutz und Schund“ im Sinne des Gesetzes von 1950. Die Episode zeigt den moralisierenden Zeitgeist der 1950er.",[("n",38)])
TF("n-disz",[18],"Mit besserer wirtschaftlicher Lage sanken Abnahmen wegen Not, Unterbringungen wegen „Erziehungsschwierigkeiten“ stiegen stark.",True,"Mit der besseren wirtschaftlichen Lage sanken Abnahmen wegen Not, Unterbringungen wegen „Erziehungsschwierigkeiten“ stiegen dagegen stark. Der Grund für die Disziplinierung verschob sich von materieller Not zu Verhalten, die Praxis blieb bis Ende der 1960er ähnlich.",[("n",34)])
MC("n-familie",[17],"Was änderte das Jugendwohlfahrtsgesetz von 1954 für Mütter?","Sie konnten nach Befund Vormund unehelicher Kinder werden",["Sie erhielten automatisch die volle Obsorge","Sie mussten die Berufstätigkeit aufgeben","Sie wurden zu Hausbesuchen verpflichtet"],"Mit dem Jugendwohlfahrtsgesetz von 1954 konnten Mütter nach einem Befund Vormund ihrer unehelichen Kinder werden. Das war erstmals eine rechtliche Stärkung der Mütter, aber noch keine generelle Reduktion des Kontrollauftrags. Die generelle Obsorge kam erst Jahrzehnte später.",[("n",27)])
MC("n-familie",[17],"Was bedeutet der Wandel zu „familienfördernden“ Maßnahmen?","Familie soll Erziehung selbst leisten, auch Väter werden einbezogen",["Familien werden öfter durch Heime ersetzt","Fürsorgerinnen übernehmen die Erziehung","Der Staat bezahlt alle Mütter für die Heimarbeit"],"Familienfördernde Maßnahmen sollten die Familie befähigen, Erziehung selbst zu leisten, und auch Väter einbeziehen, etwa mit Elternschulen und Väterschulen am Sonntag. Die Fürsorgerin sollte „beratende Freundin“ sein. Die Rollenbilder blieben trotzdem traditionell.",[("n",28)])
TF("n-familie",[],"Die Familienpolitik der 1950er und 1960er Jahre zielte unter anderem auf Geburtenförderung.",True,"Die Familienpolitik der 1950er und 1960er zielte unter anderem auf Geburtenförderung. Hintergrund war ein Geburtenrückgang von fast 50 % zwischen 1947 und 1952. Bevölkerungspolitik blieb also auch nach dem Krieg ein Motiv der Fürsorge.",[("n",28)])
MC("n-puppe",[18,23],"Wofür steht die Puppenadoption ab 1954?","Beibehaltung traditioneller geschlechtsspezifischer Arbeitsteilung",["Frühe Förderung von Buben und Mädchen","Abbau von Vorurteilen gegenüber Pflegefamilien","Beginn der Gemeinwesenarbeit"],"Die Puppenadoption ab 1954 steht für die Beibehaltung traditioneller geschlechtsspezifischer Arbeitsteilung. Mädchen wurden auf die Rolle als gute Mütter vorbereitet, Buben waren nicht beteiligt. Die Tradition lief bis 1976.")
TF("n-puppe",[],"Die Puppen wurden monatlich in einer „Puppenmutterberatungsstelle“ vorgestellt.",True,"Die Puppen wurden monatlich in einer „Puppenmutterberatungsstelle“ vorgestellt, wie bei einer echten Mutterberatung. Bei positivem Befund durften die Mädchen die Puppe nach einem Jahr adoptieren. Kontrolle wurde so schon spielerisch eingeübt.")
MC("n-casework",[26],"Was gehört zu den Forderungen des Case Work?","Anerkennung der Persönlichkeit, psychosoziale Anamnese, Anleitung zur Selbsthilfe",["Unangemeldete Kontrollen und schnelle Abnahmen","Anonymität der Fürsorgerin und Gehorsam","Allein materielle Hilfe ohne jedes Gespräch"],"Case Work forderte die Anerkennung der Persönlichkeit, eine psychosoziale Anamnese und Anleitung zur Selbsthilfe. Es bedeutete eine Absage an den Kontrollcharakter und verlangte eine demokratische Grundhaltung gegenüber Klient*innen. Die Methode kam über Emigrant*innen aus den USA und die Tradition Aichhorns nach Wien.",[("n",45)])
MC("n-casework",[26],"Wo wurde die „vertiefte Einzelfallhilfe“ 1957 modellhaft erprobt?","In einem einzigen Wiener Jugendamt in Hernals",["In allen Bezirksjugendämtern gleichzeitig","In der Stadt des Kindes","An der Wiener Universität"],"Die vertiefte Einzelfallhilfe wurde 1957 modellhaft in einem einzigen Wiener Jugendamt erprobt, in Hernals. Dabei arbeitete man mit den Jugendämtern von Hamburg und Berlin zusammen. Die flächendeckende Einführung dauerte noch lange.",[("n",45)])
TF("n-casework",[26],"Case Work ersetzte die Amtskapperl-Fürsorge in Wien ab 1957 sofort und vollständig.",False,"Case Work wurde nur langsam eingeführt, daneben lief die „Amts-Kapperl-Fürsorge“ weiter. Der Alltag in den Ämtern blieb oft hierarchisch und kontrollierend. Der eigentliche Wandel kam erst Jahre später.",[("n",46)])
MC("n-casework",[26],"Was boten die „psychiatrischen Kurse“ den Fachkräften?","Einführung in Case Work und klientenzentrierte Gesprächsführung",["Ausbildung zur Fachärztin für Psychiatrie","Schulung in Verwaltungsrecht","Kurse für Amtsleiter im Personalwesen"],"Die „psychiatrischen Kurse“ boten eine Einführung in Case Work und klientenzentrierte Gesprächsführung. Fortbildungen in Case Work mit Supervision gab es ab 1954. Sie waren ein Weg, neue Methoden trotz der veralteten Ausbildung ins Amt zu bringen.",[("n",47)])
MC("n-casework",[26,13],"Was wurde 1949 gegründet?","Das Institut für Erziehungshilfe (Child Guidance Klinik)",["Die Kinderstube des Jugendamtes","Die Wiener Heimkommission","Die Sozialakademie"],"1949 wurde das Institut für Erziehungshilfe gegründet, eine Child Guidance Klinik, mitinitiiert von Dworschak und Aichhorn. Es bot Therapie, band Eltern und Kinder ein und arbeitete im multiprofessionellen Team. Damit lebte Aichhorns Ansatz nach dem Krieg weiter.",[("n",39)])
TF("n-casework",[17],"In Österreich vollzog sich der Wandel zu egalitären Methoden schneller als im restlichen Westen.",False,"Der Wandel zu egalitären Methoden vollzog sich laut Folie in Österreich nur langsam, auch wegen der Unterbrechung durch den „Anschluss“. Internationale Entwicklungen wie Case Work kamen verspätet an. Österreich hinkte auch bei der Ausbildung hinterher.",[("n",44)])
MC("n-heim",[18],"Als was bezeichnet die Folie das Heim Anfang der 1960er?","„Totale Institution“",["„Zweites Zuhause“","„Offenes Zentrum“","„Sanfte Schule“"],"Die Folie bezeichnet das Heim Anfang der 1960er als „totale Institution“. Trotz psychologischer Betreuung gab es bis in die 1970er Jahre physische, sexuelle und psychische Gewalt. Erzieher*innen waren oft nicht ausgebildet und teils seit der NS-Zeit im Dienst.",[("n",53)])
TF("n-heim",[18,17],"Heimerzieher*innen verfügten in der Nachkriegszeit vielfach über keine fachspezifische Ausbildung.",True,"Heimerzieher*innen hatten in der Nachkriegszeit vielfach keine fachspezifische Ausbildung. Es gab zudem personelle Konstanz über das NS-Regime hinaus. Beides erklärt, warum autoritäre und gewaltvolle Praktiken so lange weiterwirkten.",[("n",51)])
MC("n-heim",[18],"Was zeigt das Gutachten von 1953 über ein 12-jähriges Mädchen laut Folie?","Das Weiterwirken von NS-Gedankengut",["Einen Fortschritt der klientenzentrierten Arbeit","Den Beginn des Kinderrechtsdenkens","Den Erfolg der Heimreform"],"Das Gutachten von 1953 über ein 12-jähriges Mädchen zeigt laut Folie das Weiterwirken von NS-Gedankengut. Abwertende Zuschreibungen wie „primitiv“ und „triebhaft“ dienten als Basis der Fremdunterbringung. Begutachtung blieb defizitorientiert.",[("n",52)])
MC("n-pflege",[18],"Welche Missstände gab es bei ländlichen Pflegestellen?","Ausbeutung als Arbeitskräfte und mangelhafte Versorgung",["Zu viel Freizeit und zu wenig Aufsicht","Zu teure Schulplätze in den Dörfern","Zu viele Besuche durch die Herkunftsfamilie"],"Bei ländlichen Pflegestellen wurden Wiener Kinder teils als Arbeitskräfte ausgebeutet und mangelhaft versorgt. Eine Fürsorgerin sah Schwielen an Kinderhänden und holte die Kinder zurück, das war aber ein Ausnahmefall. Die Kontinuität zum Kostkinderwesen der Monarchie ist deutlich.",[("n",23),("n",53)])
ORD("n-casework",[17,26],"Vom Kriegsende bis zur Case-Work-Erprobung: Reihe die Ereignisse.",[("1947","Generalamnestie"),("1949","Institut für Erziehungshilfe"),("1954","Neues Jugendwohlfahrtsgesetz"),("1957","Modellversuch in Hernals")],"1947 kam die Generalamnestie, 1949 das Institut für Erziehungshilfe, 1954 das neue Jugendwohlfahrtsgesetz und 1957 der Case-Work-Modellversuch in Hernals. In zehn Jahren werden Kontinuität, etwa bei Personal und Haltung, und Aufbruch zu neuen Methoden zugleich sichtbar.",[("n",6),("n",39),("n",27),("n",45)])

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

MULTI("sa-68",[25],"Was kritisierte die 1968er Bewegung an der Fürsorge?",["Autoritärer und kontrollierender Charakter","Weibliche Rollenzuschreibung sozialer Arbeit","Autoritär geführte Kinder- und Jugendheime"],["Zu wenig Kontrolle durch den Staat","Zu viel Freiwilligkeit"],"Die 1968er Bewegung kritisierte autoritäre Strukturen, Kontrolle und Rollenzuschreibungen in der Fürsorge. Dazu kam die Forderung nach Öffnung der Heime. Gemeinsam mit der Zweiten Frauenbewegung stieß sie den Wandel zu Freiwilligkeit und Beratung an.",[("zs",2),("zs",3)])
MC("sa-68",[25,20],"In welche Richtung bewegte sich die Praxis nach 1968?","Von Zwang und Kontrolle zu Freiwilligkeit und Beratung",["Von Beratung zu mehr Hausbesuchen und Abnahmen","Von Ambulanz zu mehr Großheimen","Von Beruf zurück zum Ehrenamt"],"Nach 1968 bewegte sich die Praxis von Zwang und Kontrolle zu Freiwilligkeit und Beratung. Niederschwellige, regionale und ambulante Angebote wurden ausgebaut. Hochkonjunktur und Wohlfahrtsstaat schufen den Raum dafür.",[("zs",3)])
MC("sa-heime",[25],"Welche Maßnahme folgte der Heimkritik 1971?","Enquete des Jugendamtes und Wiener Heimkommission",["Schließung aller Wiener Heime im selben Jahr","Gründung der Kinderübernahmestelle","Einführung des Fürsorgebuches"],"Nach der Demonstration von 1970 folgten 1971 eine Enquete des Jugendamtes und die Wiener Heimkommission. Danach gab es längere Ausgangszeiten, kleinere Gruppen und ab 1973 erstmals Taschengeld. Die Heimkritik führte also zu konkreten Verbesserungen.",[("zs",10)])
MULTI("sa-heime",[25],"Was war neu an der „Stadt des Kindes“ von 1974?",["Kleine „Familiengruppen“","Besuch öffentlicher Schulen","Öffentliches Schwimmbad, Öffnung nach außen"],["Interne Heimschule mit Drill","Getrennte Säle für 300 Kinder"],"Die „Stadt des Kindes“ von 1974 war die bauliche Umsetzung der Richtlinien der Heimkommission und wurde zum Symbol der Reform. Laut damals tätigen Sozialpädagog*innen blieb der Betrieb aber autoritär geprägt. Später wurde sie als letztes Wiener Großheim geschlossen.",[("zs",11)])
TF("sa-heime",[25],"Laut damals tätigen Sozialpädagog*innen war die Stadt des Kindes völlig frei von autoritärem Charakter.",False,"Laut damals tätigen Sozialpädagog*innen war der Heimbetrieb in der Stadt des Kindes trotz moderner Architektur deutlich autoritär geprägt. Die Reform der 1970er änderte Bauten und Regeln, nicht das System Heim selbst. Das kritisierte erst die spätere Heimreform.",[("zs",11)])
MC("sa-heime",[],"Was geschah 2002 mit der „Stadt des Kindes“?","Sie wurde als letztes Wiener Großheim geschlossen",["Sie wurde zum Krisenzentrum für Säuglinge","Sie wurde an private Träger verkauft","Sie wurde neu eröffnet und vergrößert"],"2002 wurde die Stadt des Kindes als letztes Wiener Großheim geschlossen. Das Vorzeigeprojekt der 1970er wurde so selbst Teil der Reform Heim 2000, die Großheime durch kleine Wohngemeinschaften und Krisenzentren ersetzte.",[("zs",29)])
MC("sa-beruf",[24,25],"Welche Methoden kamen im „Professionalisierungs- und Modernisierungsschub“ hinzu?","Vertiefte Einzelfallhilfe, nicht-direktive Gesprächsführung, Systemik, Supervision",["Erb- und Rassenkunde, Fürsorgebuch","Kostkinderwesen und Waisenbureau","Nachschau und Amtskapperl"],"Im Professionalisierungs- und Modernisierungsschub kamen vertiefte Einzelfallhilfe, nicht-direktive Gesprächsführung, Systemik und Supervision dazu. Der Schwerpunkt verlagerte sich auf Beratung und Gespräch. Fortbildungen machten die neuen Methoden zugänglich.",[("zs",6)])
MC("sa-beruf",[24],"Was entstand 1976 in Österreich?","Akademien für Sozialarbeit",["Das Institut für Heimerziehung","Das erste Jugendamt","Die FH-Studiengänge"],"1976 entstanden in Österreich die Akademien für Sozialarbeit. Die viersemestrige Ausbildung wurde erst 1987 auf sechs Semester verlängert. Österreich hatte damit international lange hinterhergehinkt.",[("zs",14)])
TF("sa-beruf",[24],"Österreich lag mit den Lehranstalten für gehobene Sozialberufe deutlich hinter dem internationalen Ausbildungsniveau zurück.",True,"Ab 1968 wurde fast in ganz Europa das Ausbildungsniveau angehoben, in Österreich dauerte das bis 1976 mit den Akademien für Sozialarbeit. Die Lehranstalten für gehobene Sozialberufe lagen deutlich darunter.",[("zs",14)])
MC("sa-beruf",[21,20],"Wofür steht der neue Berufstitel „Sozialarbeiterin“ symbolisch?","Wunsch nach weniger Kontrolle, mehr Partnerschaftlichkeit und Freiwilligkeit",["Vollständigen Verzicht auf Kinderschutz","Rückkehr zum sozialen Ehrenamt","Unterordnung unter das Amt"],"Der neue Berufstitel „Sozialarbeiterin“ steht symbolisch für den Wunsch nach weniger Kontrolle, mehr Partnerschaftlichkeit und Freiwilligkeit. Die Folie schreibt, das sei zumindest eine theoretische Verschiebung. In der Praxis blieb der Kontrollauftrag Teil des Berufs.",[("zs",6)])
MC("sa-konflikt",[25],"Worum drehte sich der Generationskonflikt im Amt vor allem?","Um Fragen des Kontrollauftrags",["Um Pensionsansprüche","Um die Wahl der Amtsleiter","Um die Verlegung der Ämter"],"Der Generationenkonflikt im Amt drehte sich vor allem um den Kontrollauftrag. Die jungen Sozialarbeiterinnen kritisierten Bevormundung und fehlende Zeit für menschliche Gespräche. Gegen die fast ausschließlich männlichen Amtsleiter war zunächst kaum anzukommen.")
MC("sa-konflikt",[23],"Wie arbeiteten Männer, die in den 1950er/60er Jahren die Ausbildung machten, meistens?","Mehrheitlich nicht in der Jugendwohlfahrt",["Fast alle als Sprengelfürsorger im Außendienst","Hauptsächlich in Mutterberatungsstellen","Als Heimmütter in Kinderheimen"],"Männer, die in den 1950er/60er Jahren die Ausbildung machten, arbeiteten mehrheitlich nicht in der Jugendwohlfahrt. Viele strebten Karrieren mit höherem Sozialprestige an. Die Jugendwohlfahrt blieb so ein Frauenfeld mit männlicher Leitung.",[("zs",22)])
MC("sa-projekte",[25],"Welche Projekte gingen aus Impulsen der Studierenden der Sozialakademien hervor?","Frauenhäuser, Streetwork, Obdachlosenzeitung „Augustin“",["KÜST, Kinderstube und Wäschepaket","Waisenbureau, Armenanstalten, Kostkinderwesen","Mutterkreuz, Familienasyle, Fürsorgebuch"],"Aus Impulsen politisch engagierter Studierender der Sozialakademien gingen Frauenhäuser, Streetwork und die Obdachlosenzeitung „Augustin“ hervor. Dazu kamen das „Saftbeisl“, Ausstiegshilfen für Prostituierte und die Betreuung von „Gastarbeiterkindern“. Sozialarbeit erschloss so neue Handlungsfelder.")
TF("sa-projekte",[25],"Nach 1968 wurde Sozialarbeit attraktiv, Ausbildungsstätten waren plötzlich überlaufen.",True,"Nach 1968 wurde Sozialarbeit attraktiv, die Ausbildungsstätten waren plötzlich überlaufen. Das ist ein deutlicher Wandel gegenüber dem „katastrophalen Nachwuchsmangel“ der 1950er und 1960er. Neue Projekte und Methoden machten den Beruf interessant.",[("zs",14),("zs",18)])
MC("sa-familie",[8],"Was brachte das Jahr 1989?","Generelle gesetzliche Übertragung des Obsorgerechts an Mütter",["Die Einführung der Generalvormundschaft","Die Gründung des Jugendamtes","Die Schließung aller Pflegestellen"],"1989 kam die generelle gesetzliche Übertragung des Obsorgerechts an ledige und verheiratete Mütter. Damit endete eine lange Tradition: Die zu überwachenden „Mündel“ und die obligatorischen Hausbesuche nahmen ab. Das war die entscheidende Zäsur nach dem Kindschaftsrecht von 1978.",[("zs",9)])
MC("sa-familie",[],"Was bewirkte das neue Kindschaftsrecht von 1978?","Gleichheitsgrundsatz beider Elternteile gegenüber dem Kind",["Alleinige Obsorge des Vaters bei Scheidung","Verpflichtung beider Eltern zu Hausbesuchen","Abschaffung von Unterhaltszahlungen"],"Das neue Kindschaftsrecht von 1978 brachte den Gleichheitsgrundsatz beider Elternteile gegenüber dem Kind und die Verpflichtung zu einvernehmlicher Obsorge. Ledige Mütter bekamen die Obsorge aber erst 1989 generell. Das Recht folgte dem gesellschaftlichen Wandel nur langsam.",[("zs",8)])
TF("sa-pflege",[],"Ab den 1980er Jahren wurden Pflegefamilien erstmals als eigenständige Familienform mit spezifischen Problemen gesehen.",True,"Ab den 1980ern wurden Pflegefamilien als eigenständige Familienform mit spezifischen Problemen gesehen, nicht mehr nur als Ersatz. Davon zeugen die Beratungsstelle ab 1983 und Vorbereitungskurse ab 1985. Auch der Kontakt zur Herkunftsfamilie wurde wichtig.",[("zs",4)])
MC("sa-mandat",[19],"Was meint das „doppelte Mandat“?","Soziale Arbeit steht zwischen Hilfe und Kontrolle",["Eine Fürsorgerin hat zwei Sprengel","Bund und Land finanzieren gemeinsam","Zwei Personen müssen jeden Akt unterschreiben"],"Das doppelte Mandat meint: Soziale Arbeit steht zwischen Hilfe und Kontrolle. Dieses Pendeln ist laut Folie immanenter Teil der Jugendwohlfahrt. Es zieht sich von der Armenfürsorge über das Rote Wien bis heute.")
MC("sa-mandat",[21],"Wie geht moderne Sozialarbeit laut Folie mit dem doppelten Mandat um?","Abkehr von primärer Kontrolle bei Festhalten am umfassenden Kinderschutz",["Völliger Verzicht auf jede Kontrolle","Rückkehr zur Kontrolle durch Hausbesuche","Abgabe des Kinderschutzes an die Polizei"],"Moderne Sozialarbeit kehrt sich von primärer Kontrolle ab und stärkt die Freiwilligkeit, hält aber am Ideal des umfassenden Kinderschutzes fest. Das gilt theoretisch und praktisch; Kontrolle wird also nicht geleugnet, sondern begrenzt und begründet.")
TF("sa-mandat",[21,19],"Das Pendeln zwischen Hilfe und Kontrolle wurde mit der modernen Sozialarbeit endgültig aufgehoben.",False,"Das Pendeln zwischen Hilfe und Kontrolle ist laut Folie immanenter Teil der Jugendwohlfahrt und wurde nicht aufgehoben. Verändert hat sich die Gewichtung: weniger Kontrolle als Grundhaltung, mehr Freiwilligkeit. Beim Kinderschutz bleibt Kontrolle Aufgabe.")
MC("sa-mandat",[21],"Wie fasst eine Sozialarbeiterin die Haltung der 1970er zusammen?","„Kontrolle ja, reduziert aber auf die schwierigsten Fälle“",["„Kontrolle ist immer die beste Hilfe“","„Hilfe nur für die Arbeitswilligen“","„Die Behörde bin ich“"],"Eine Sozialarbeiterin fasst die damalige Haltung so zusammen: „Kontrolle ja, reduziert aber auf die schwierigsten Fälle.“ „Die Behörde bin ich!“ stammt dagegen von einem autoritären Amtsleiter früherer Jahre. Der Satz zeigt die neue Gewichtung des doppelten Mandats.",[("zs",7)])
MC("sa-90",[],"Was kennzeichnet die Sozialpolitik ab Ende der 1980er Jahre?","Schrittweiser Rückzug des Staates und Privatisierungen",["Starker Ausbau aller Leistungen","Wiedereinführung des Heimatrechts","Abschaffung der Sozialversicherung"],"Ab Ende der 1980er zog sich der Staat schrittweise aus der sozialen Sicherung zurück, Bereiche wurden privatisiert. Zugleich gab es mehr armutsgefährdete Menschen, und das Jugendamt sah sich Multiproblemlagen gegenüber. Das prägt die Arbeit bis heute.",[("zs",23)])
MC("sa-90",[],"Was geschah im Jahr 2000 mit dem Jugendamt?","Umbenennung in MAG ELF, Amt für Jugend und Familie",["Auflösung und Verlagerung an Vereine","Eingliederung in das Bundesministerium","Rückbenennung in Wohlfahrtsamt"],"Im Jahr 2000 wurde das Jugendamt zur MAG ELF, dem Amt für Jugend und Familie. Das war ein Bekenntnis zu umfassendem präventivem Kinder- und Jugendschutz mit Betonung von Service und Freiwilligkeit. Der neue Name sollte das alte Amtsbild ablösen.",[("zs",24)])
MC("sa-staerken",[20],"Wofür steht der Wickelrucksack?","Symbol für die Neuorientierung der Jugendwohlfahrt",["Symbol für die Rückkehr zur Erfassung","Prämie für kinderreiche Familien","Ausrüstung der Fürsorgerinnen"],"Der Wickelrucksack ersetzte im Jahr 2000 das Säuglingswäschepaket und ist Symbol für die Neuorientierung der Jugendwohlfahrt. Er spricht auch Väter an. Familienförderung ist nun von bevölkerungspolitischen Interessen abgekoppelt.")
TF("sa-staerken",[20],"Kinderschutz und Familienförderung sind heute laut Folie von bevölkerungspolitischen Interessen abgekoppelt.",True,"Kinderschutz und Familienförderung sind laut Folie heute von bevölkerungspolitischen Interessen abgekoppelt. Das ist ein großer Unterschied zur Linie seit Tandler, der Fürsorge als Bevölkerungspolitik verstand. Im Zentrum steht das einzelne Kind.")
MC("sa-staerken",[],"Was drückt die Umbenennung in „Paar- und Familienberatungsstellen“ aus?","Absage an das normierte Vater-Mutter-Kind-Modell",["Pflicht zur Eheschließung","Trennung von Eltern und Kindern","Ende aller Beratung"],"Die Umbenennung in „Paar- und Familienberatungsstellen“ drückt die Absage an das normierte Vater-Mutter-Kind-Modell aus. Patchwork-Familien werden zunehmend berücksichtigt. Früher war genau dieses Modell der Maßstab für „Verwahrlosung“.")
MC("sa-heim2000",[20],"Wie lautet das neue Motto der Fremdunterbringung?","„So kurz wie möglich“ bzw. „so kurz wie notwendig“",["„So lange wie möglich“","„Wer nicht arbeitet, soll auch nicht essen“","„Erst Heim, dann Familie“"],"Das neue Motto lautet „so kurz wie möglich“ bzw. „so kurz wie notwendig“, früher hieß es „so lange wie möglich“. Dazu kommen regionale Krisenzentren, damit das gewohnte Umfeld des Kindes bleibt. Fremdunterbringung soll eine Ausnahme auf Zeit sein.",[("zs",29)])
MC("sa-heim2000",[20,25],"Was ist der Unterschied zwischen den Heimreformen der 1970er und von 2000?","Früher Kritik am Führungsstil, 2000 Kritik am System Heim selbst",["Früher Kritik an den Kosten, 2000 an der Lage","Früher Schließung aller Heime, 2000 neue Großheime","Früher nur in Wien, 2000 nur in Niederösterreich"],"Die Heimreform der 1970er kritisierte vor allem den autoritären Führungsstil, die Reform Heim 2000 das System Heim selbst, das „Heim als Kindergefängnis“. Darum wurden Großheime geschlossen und durch kleine Wohneinheiten ersetzt. Ein starkes Beispiel, um im Vergleich zu argumentieren.",[("zs",27)])
MC("sa-heim2000",[21],"Wie laufen Erhebungen heute laut Folie ab?","Anlassbezogen nach dem Vieraugenprinzip",["Monatlich und unangemeldet durch eine Person","Telefonisch über die Schule","Durch die Polizei in Uniform"],"Erhebungen laufen heute anlassbezogen nach dem Vieraugenprinzip. Zwangsmaßnahmen werden nur bei „Gefahr im Verzug“ angedroht. Das ist das Gegenteil der früheren Routine-Hausbesuche und der Amts-Kapperl-Methode.",[("zs",29)])
MC("sa-heim2000",[],"Was war FIDUZ 1990?","Die erste Wohngemeinschaft als Krisenzentrum",["Eine Beratungsstelle für Pflegeeltern","Ein Großheim in Niederösterreich","Ein Verein für Streetwork"],"FIDUZ war 1990 die erste Wohngemeinschaft als Krisenzentrum. Säuglinge und Kleinkinder kamen ab 2001 temporär in Krisenpflegefamilien. Krisenzentren sollen Kinder kurzfristig und nahe am gewohnten Umfeld auffangen.",[("zs",28)])
ORD("sa-heim2000",[25,20],"Vom Protest zur Schließung: Bringe die Heimgeschichte in Reihenfolge.",[("1970","Demonstration von Lehrlingen und Jugendlichen"),("1974","Stadt des Kindes"),("1995","Beginn der Reform Heim 2000"),("2013","Schließung des Lindenhofs")],"1970 demonstrierten Lehrlinge und Jugendliche gegen die Heime, 1974 entstand die Stadt des Kindes, 1995 begann die Reform Heim 2000, 2013 wurde der Lindenhof geschlossen. Die Reihe führt von der Kritik an Heimleitungen zur Kritik am System Heim.",[("zs",10),("zs",11),("z",4),("zs",29)])

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

MATCH("x-verw",[11,16,18],"Wie deutet welche Epoche „Verwahrlosung“?",[("Monarchie","Moralisch, wie eine „Ansteckungsgefahr“"),("Aichhorn","Reaktion auf psychische und soziale Erfahrung"),("NS-Regime","„Asozialität“, gemeinschaftswidriges Verhalten"),("1950er","Mangelnde „Sozialanpassung“")],"In der Monarchie galt Verwahrlosung moralisch als „Ansteckungsgefahr“, Aichhorn sah sie als Reaktion auf psychische und soziale Erfahrungen, das NS-Regime deutete sie als „Asozialität“, die 1950er als mangelnde „Sozialanpassung“. Die Deutung bestimmt jeweils, wie eingegriffen wird: aussondern, verstehen, vernichten oder anpassen.")
MATCH("x-paket",[22,20],"Was war das Säuglingspaket wann?",[("1927","Für alle Mütter, Übergabe beim Hausbesuch"),("NS-Zeit","Zugleich Erhebung von Erbkrankheiten"),("Nachkriegszeit","Vorerst nur für bedürftige Mütter"),("2000","Ersetzt durch den Wickelrucksack")],"1927 bekamen alle Mütter das Paket beim Hausbesuch, in der NS-Zeit diente es zugleich der Erhebung von Erbkrankheiten, in der Nachkriegszeit gab es es vorerst nur für bedürftige Mütter, 2000 wurde es durch den Wickelrucksack ersetzt. Hilfe und Kontrolle in einem Paket, ein gutes Beispiel für das doppelte Mandat.")
MC("x-haus",[19,20],"Wie veränderte sich die Mündelbetreuung 1989?","Die obligatorischen Hausbesuche nahmen ab, Tätigkeiten verlagerten sich ins Amt",["Jede Familie bekam nun wöchentlich Besuch","Hausbesuche wurden auf das Land beschränkt","Hausbesuche gingen an die Polizei"],"Mit der Übertragung der Obsorge an die Mütter 1989 nahmen die obligatorischen Hausbesuche bei den Mündeln ab, die Tätigkeiten verlagerten sich ins Amt. Heute geschieht der Hausbesuch anlassbezogen nach dem Vieraugenprinzip. Der Hausbesuch zeigt den Wandel vom Kontroll- zum Hilfeinstrument.",[("zs",9)])
ORD("x-haus",[24],"Reihe die Stationen des Berufs.",[("1912","Vereinigte Fachkurse für Volkspflege"),("1948/49","Ausbildung auch für Männer"),("1976","Akademien für Sozialarbeit"),("2002","Vierjährige FH-Studiengänge")],"1912 die Vereinigten Fachkurse für Volkspflege, 1948/49 die Öffnung der Ausbildung für Männer, 1976 die Akademien für Sozialarbeit, 2002 die vierjährigen FH-Studiengänge. Von den ersten Kursen zum Hochschulstudium.",[("eb",11),("n",9),("zs",14),("z",4)])
ORD("x-verw",[2,11],"Bringe die großen Epochen in Reihenfolge.",[("1861","Liberale Ära der Gemeindeverwaltung"),("1919","Rotes Wien"),("1934","Austrofaschismus"),("1938","Nationalsozialismus")],"1861 beginnt die liberale Ära der Gemeindeverwaltung, 1919 das Rote Wien, 1934 der Austrofaschismus und 1938 der Nationalsozialismus. Die zeitliche Gliederung ist die Basis jeder Überblicksantwort, weil jede Epoche ihr eigenes Verständnis von Fürsorge hatte.",[("a1",3),("rw",2),("t",2),("t",12)])
ORD("x-paket",[11],"Von der Vormundschaft zur Obsorge: Was kam wann?",[("1912","Gemeinderatsbeschluss zur Vormundschaft"),("1954","Mütter können nach Befund Vormund werden"),("1978","Neues Kindschaftsrecht"),("1989","Obsorgerecht generell an Mütter")],"1912 der Gemeinderatsbeschluss zur Vormundschaft, 1954 konnten Mütter nach Befund Vormund werden, 1978 kam das neue Kindschaftsrecht, 1989 das Obsorgerecht generell an die Mütter. Über 70 Jahre vergehen, bis Mütter unehelicher Kinder selbstverständlich Obsorge haben.",[("eb",4),("n",27),("zs",8),("zs",9)])

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


COURSE = dict(
    id="geschichte",
    name="Geschichte der Sozialen Arbeit",
    lecturer="FH-Hon.Prof.in Mag.a Dr.in Gudrun Wolfgruber-Thanel",
    term="WS 2026/27",
    exams=[dict(id="vz", label="Vollzeit (VZ)", date="2026-11-04"), dict(id="bb", label="Berufsbegleitend (BB)", date="2026-11-12")],
)
