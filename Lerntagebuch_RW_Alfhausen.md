# Praktikum_Daten-_und_Prozessanalyse -> Ziel: Energiehandel an der Börse automatisieren

# Zielsetzungen:
  - Englisch aufbessern (Lesen)
  - Strommarkt/Stromnetz-Kenntnisse aneignen
  - Programmierkenntnissse in Python aneignen
  - Fortschritte/Arbeit Dokumentieren
  - Algorithmus für den Stromhandel programmieren

# Beginn Lerntagebuch (20.10.2025), Praktikumsbeginn (20.10.2025):

    In diesem Tagebuch werden meine Lernfortschritte, Misserfolge, Erkenntnisse, Ergebnisse sowie offenen Fragen festgehalten. Das Tagebuch beginnt mit dem 20.10.2025. Vermittelte Inhalte sind in Dokumentation_RW_Alfhausen.md notiert und werden täglich festgehalten. 
    Das Lerntagebuch dient zum einem, das gelernte systematisch zu dokumentieren, zu verarbeiten und zu reflektieren, um so den Lernprozess nachhaltig zu gestalten. Weiter dient es auch als Nachweiß über erbrachte Leistungen (Proof Of Work).


# Tag 56 (20.10.2025):

Montag 8:20-16:30 (13:10-13:40 Pause) = 7,67

- Begrüßung der Mitarbeiter in ihren jeweiligen Abteilungen
- Einrichten des Arbeitsplatzes
- Recherche Energiemärkte:
	 - Merit-Order
	 - Market-Clearing-Price


# Tag 57 (21.10.2025):

Dienstag 7:20 - 16:30 (13:30 - 14:00 Pause) = 8,67

- Recherche Energiemärkte:
     - Kritik Merit-Order
     - Strombörse: Stromhandel am Termin- und Spotmarkt (https://www.youtube.com/watch?v=cmvuYbUjyxA, https://www.youtube.com/watch?v=sXA3T1EPelI)
     - OTC-Handel (Over The Counter)
     - Merit-Order-Effekt
     - Ask- und Bid-Preis
     - Ask-Bid-Spread (https://www.youtube.com/watch?v=mbBloMnklB0)
     - Arbitrage
- Strukturierung und Verlinkung Wissensdatenbank in Obsidian
     - Markdownverlinkung

Wie in jedem neuen Thema oder Projekt ist sich zunächst in die Materie einzulesen. Der heutige Tag bestand lediglich daraus. Der Handel mit Energie an der Börse scheint sehr spannend zu sein. 

# Tag 58 (22.10.2025):

Mittwoch 7:20 - 16:30 (13:30 - 14:00 Pause) = 8,67

- Comet-Browser testen in Combination GWDG Jupyter Notebook (https://jupyter-cloud.gwdg.de/jhub/user/0532562/lab/tree/TradingEnergy/TradingEnergy.ipynb)
- Recherche: Trading Bot Python (https://www.youtube.com/watch?v=QAo0x9fE6ck&list=PLcFcktZ0wnNmdgAdv4-Yl_nzS5LiKnhnn, https://www.youtube.com/watch?v=1xClSutmwg8&list=PLwEOixRFAUxZmM26EYI1uYtJG39HDW1zm)
- Singularity Machine Learning (https://quantum.cloud.ibm.com/docs/de/guides/multiverse-computing-singularity)
- Erweiterungen VS Code installieren (Jupyter Notebook, Libraries)
- Gespräch mit Hendrik: leichter Einstieg in Stromnetze (50hz-Problematik, Primärregelung, Stromerzeugungsarten, Übertragungsnetzbetreiber, Strombörsenzeiten, Erwartungshaltung an der Börse, weiterführende Links zu Sektorkoppelung)
- Recherche Energiemarkt: download historische Strommarktdaten https://www.smard.de/home/downloadcenter/download-marktdaten/
- Marktdaten in Jupyter einlesen

Heute habe ich mich mit Hendrik etwas ausgetauscht über den Strommarkt und einigen technischen Komponenten des Stromnetzes. Beim Gespräch sind einige Schlagwörter gefallen, die ich am gestrigen und am Tag zuvor nachgeschlagen hatte und diese in mein Energy_Wiki festgehalten habe, um darin immer nachschlagen zu können und damit ich das niedergeschriebene besser im Kopf behalte. Weiter hat mir Hendrik die Strombörse live gezeigt. Interessant war unter anderem, welche Wirtschaftssubjekte Forecast-Daten bereitstellen. Während des Gespräches habe ich mir einige Notizen gemacht mit Fachbegriffen und Verweisen zu Internetseiten zum Nachschlagen. 
Ich habe mir heute etwas über das Programmieren von Trading Bots in Python angeschaut und mir erste Schritte überlegt und notiert. Angefangen mit dem Laden historischer Daten (siehe oben). Als nächstes werde ich mir die Daten (Datum, Preise/MWh) visualisieren lassen in Jupyter Notebook. Ich habe Jupyter Notebook gewählt, weil es mir ermöglicht den Code zu unterteilen in Teilprogramme, die ich separat laufen lassen kann. Mir fällt gerade ein, dass ich noch viel mehr schreiben könnte, werde mich allerdings nur auf das Nötigste beschränken. Alles in allem habe ich heute einen Blick dafür bekommen, wie komplex der Strommarkt und das Stromnetz sind, welche Wirtschaftssubjekte beteiligt sind und das es dadurch jetzt schon gefühlt einen riesen Haufen an Parameter gibt, die später das Verhalten des Trading-Bots beeinflussen werden. 

# Tag 59 (23.10.2025):

Donnertag 7:20 - 16:30 (13:30 - 14:00 Pause) = 8,67

- Recherche: aktuelle Stromhandelspreise (EU)
- Programmieren lernen Jupyter Noteboook (VS Code - lokal und Jupyter-Cloud): Stromhandelspreise abrufen (https://www.smard.de/) mittels REST-API als csv speichern und visualisieren (plotten)
	- Hilfe von Claude AI und Perplexity AI, Westermann Bücher (Fachstufe II, Technische IT-Berufe)
- Personalfragebogen ausfüllen
- Code auseinandernehmen und verstehen Stromdaten_BundesNetzAgentur_REST_API.ipynb
	- Unix Timestamp: ist eine laufende Zahl in Sekunden seit Donnerstag, dem 1. Januar 1970, 00:00, Bsp: 23.10.2025 01:00 -> 1729674000000 Sekunden
	- Funktionen und Parameter: Übergabe von Werten
- Recherche: 50-Hertz-Problematik, Übertragungsnetzbetreiber (ÜNB) und Verteilungsnetzbetreiber (VNB)


# Tag 60 (24.10.2025):

Freitag 6:20 - 12:40 = 6,16

- Agenten in VS Code einrichten
	- Agenten testen und Programme schreiben lassen
- Erweiterungen und Bibliotheken in VS Code installieren
- Buch Fachstufe II Daten- und Prozessanalyse mit Haftmarker versehen
- Hendrik fragen: Zugänge Udemy und Strommarktpreise
- Programmierkurs in Python https://www.udemy.com/course/programmieren-lernen-fur-arbeitsuchende/learn/lecture/41970570#overview
- Python üben https://www.hackerrank.com/, https://campus.datacamp.com, https://www.youtube.com/watch?v=KZpYtNtGxSU
- Erkundung firmeneigenes Strompreisportal http://gamma.rw.energy:3000

Die erste Woche ist nun zu Ende, und mein erster Eindruck ist durchweg positiv. Ich habe in kurzer Zeit sehr viele neue Eindrücke gesammelt und konnte bereits wertvolle Einblicke  gewinnen. Besonders spannend finde ich die Verbindung zwischen meinem fachlichen Schwerpunkt und den praktischen Aufgaben, die mir hier die Möglichkeit geben, mein Wissen gezielt zu vertiefen und weiter auszubauen.

Darüber hinaus fasziniert mich die deutliche wirtschaftliche Komponente, insbesondere der Bezug zur internationalen Strombörse. Diese Kombination aus technischer und ökonomischer Perspektive eröffnet mir ein vielseitiges und zukunftsorientiertes Arbeitsfeld, schätze ich.

In der kommenden Woche steht erneut viel Neues an, sowohl fachlich als auch organisatorisch. Insgesamt war der Einstieg sehr motivierend und stimmt mich optimistisch für die nächsten Wochen.

# Tag 61 (27.10.2025):

Montag 9:20 - 17:40 (14:00 - 14:30 Pause) = 7,83

- Recherche: 
	- Übertragungsnetzbetreiber + Verteilungsnetzbetreiber
	- 4- bzw. 6-Stunden-Regel
- Buch: Python Grundkurs (2024):
	- Verzweigungen und Schleifen S.133-152
		- **W**iederholungsaufgaben **W**1-**W**2

Der heutige Tag ging komplett für Python drauf. Ich werde nur das nötigste lernen um vorwärts zu kommen, zumal ich noch gar nicht weiß was das nötigste umfasst um weiter zu kommen. Morgen geht es mit Aufgabe W3 aus dem Buch Python Grundkurs weiter. 

# Tag 62 (28.10.2025):

Dienstag 6:20 - 14:40 (12:45 - 13:15Pause) = 7,83

- Buch: Python Grundkurs (2024):
	- Verzweigungen und Schleifen S.133-152
		- **W**iederholungsaufgaben **W**3-**W**8 (W9 ausstehend)
- Udemy:
	- Das Python Grundlagen Bootcamp: Datenstrukturen, Zahlen, Variablen, Strings (Indexing + Slicing)

Das Wiederholen von Grundlagen mittels Udemy hat mir sehr geholfen und das werde ich auch weiterführen bis zum Schluss. Ich werde das Buch Python Grundkurs (2024) und Udemy im Wechsel nutzen. Das Buch bietet knifflige Aufgaben wohingegen Udemy einfachere Aufgaben bietet, um eine gewisse Sicherheit zu erlangen. Morgen werde ich ein wenig am Energy_Wiki weiterarbeiten, das kleine Einmal-Eins Stromhandels und -netzes. 

# Tag 63 (29.10.2025):

Mittwoch 6:15 - 13:40 = 7,41

- Udemy: Das Python Grundlagen Bootcamp: Listen, Dictionaries, Tupel, Anweisungen, Methoden und Funktionen, Bool´sche Parameter, Map und Filter
- List-Comprehension: https://www.youtube.com/watch?v=jA8C52Xm3D0&t=408s

# Tag 64 (30.10.2025):

Donnerstag 7:20 - 15:40 (13:00 - 13:30Pause) = 8,16

- Udemy: Das Python Grundlagen Bootcamp: NumPy, Pandas (Sieries), 

# Tag 65 (03.11.2025):

Montag 7:00 - 16:00 (11:40 - 12:10 Pause) = 8,5

- Strombörse beobachten, Fragen notieren
- Udemy: Grundlagen Bootcamp: Dataframes Teil 1, 2, 3

# Tag 66 (04.11.2025):

Dienstag 7:30 - 16:45 (Unterbrechungen/Pause 11:50-12:10, 13:45-14:00) = 8,66

- Strombörse beobachten, Fragen notieren
- Podcast: 1 GW BESS Portfolio im Trading, Peter Reitz (CEO EEX), E#87 Wärmenetzausbau Gaskraftwerkplanung und Energiepreise 
- Recherche: Battery Energy Storage System (BESS), Independent Power Producer (IPP), Frequency Containment Reserve (FCR), Flexible Connection Agreements (FCA), Performance Warrenties, 4 ÜNB (Amprion, TransnetBW, Tennet TSO und 50Hertz), Batteriespeicher Unternehmen (terralayr, Terra One), Co-located Assets, Business-to-Customer (B2C), Graustrom, Standalone-Speicher, Netzdienlich Netzneutral Netzschädlich, Dispatch Redispatch, Nodal (oder auch locational marginal pricing, LMP )

Die Lernkurve ist steil am Anfang? Definitiv, wenn man betrachtet, was sich für ein Berg an Wissen auftut, der gemeistert werden will. 
Die Podcastfolgen über den Energiemarkt und Algorithmen war sehr spannend. Manchmal war es etwas schwierig, sich zu konzentrieren, da ich heute auf dem Rückweg nach Osnabrück den Zug genommen habe und es stellenweise sehr laut und auch sehr eng wurde.
Heute kam ich nicht dazu für Python zu lernen, werde dies aber spätestens Ende der Woche wieder angehen. 
Die Fragen und dazugehörige Screenshots über das Börsenchart habe ich mir in Word in der Fragen_Stromboerse.docx-Datei notiert.

# Tag 67 (05.11.2025):

Mittwoche 7:20 - 16:40 (14:30-15:00 Pause) = 8,83

- Eintragung Fachvokabular in Energy_Wiki.md
- E#86 'Strom': Dr. Tim Meyers Marktentscheidungen und die Kraft der Innovation
- Udemy: Python Grundlagen Bootcamp: Fehlende Daten, Gruppieren nach, Merging, Joining, Concatanating
- Interdisziplinär: 
	- Docker vs. VM Ware


# Tag 68 (06.11.2025):

Donnerstag 8:20 - 16:20 (13:45-14:15 Pause) = 7,5

- Udemy: Python Grundlagen Bootcamp: DataFrames Operations Teil 1, Teil 2, CSV, EXCEL, Webscraping, SQL, JSON, Matplotlib Teil 1, Teil2, Teil3, Seaborn Distributionplots Teil 1


# Tag 69 (07.11.2025):

Freitag 7:20 - 12:40 =  5,33

- Udemy: Python Grundlagen Bootcamp: Seaborn Distributionsplots Teil 2, Matrix, Regression, Grids, Pandas Visualisierung Teil 1

Die letzten drei Tage waren geprägt von Programmieren. Für den TradingBot werde ich noch viel Programmierkenntnisse benötigen. Ich nutze den ganzen Tag in Vollzeit zum Lernen von Python. Mit jeder neuen Einheit in Python erhöht sich meine Anerkennung anderen Programmieren gegenüber. Kommende Woche werde ich die Programmierkurse fortfahren, aber auch den Strommarkt nicht aus dem Blick verlieren. Ich werde mal fragen, ob ich bei Tradingentscheidungen live dabei sein kann. Auch habe ich noch einige Fragen, die ich mir notiert hatte zu den Charts. Viele Daten und deren Korrelationen erschließen sich mir noch nicht ganz. Das Großprojekt, den Energiehandel zu automatisieren verlangt von mir fundierte Kenntnisse, die erst angeeignet werden müssen. Mein Abschlussprojekt für die Abschlussprüfung starte ich nächstes Jahr.

# Tag 70 (10.11.2025):

Montag 6:20 - 16:40 (14:00-14:30 Pause) = 9,83

- Udemy: Python Grundlagen Bootcamp: Pandas Visualisierung Teil1 + Teil2, Bildgrundlagen NumPy Arrays
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Debug Coding errors
- https://transparency.entsoe.eu/Sercurity : Token für REST API freigeschaltet

# Tag 71 (11.11.2025):

Dienstag 6:20 - 16:40 (14:10-14:40 Pause) = 9,83

Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Day Trading with Oanda ( Abschnit 3: 14-19),  Financial Data Analysis with Python and Pandas (Abschnitt 12: 112-117), API Trading with Python (Abschnitt 8: 70-82)

# Tag 72 (12.11.2025):

Mittwoch 6:20 - 15:40 (14:10-14:40 Pause) = 8,83

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS:  Financial Data Analysis with Python and Pandas (Abschnitt 12: 118-119)
- Erstellung API Entsoe (krachend gescheitert) --> erhalte keine Daten
- Recherche: SKVE, Kerzencharts (zeichnen)

# Tag 73 (13.11.2025):

Donnerstag 7:20 - 12:40 = 5,33

- Kerzencharts verstehen https://www.ig.com/en/ig-academy/the-basics-of-technical-analysis/support-and-resistance
- Programmieren: Jupyter Notebook: Live-Chart mit KI-Hilfe
- Live-Chart über API von Oanda.com in Jupyter-Notebook in GWDG-Cloud
- Download Anaconda-Umgebung, da Live-Chart in VSCode nicht möglich mit JPYNB
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Python (& Finance) Basics (391- 396)
- Installation PyCharm, da Anaconda Jupyter Notebook Cloud begrenzte Recheneinheiten zur Verfügung stellt
- PyCharm einrichten
# Tag 74 (14.11.2025):

Freitag 7:20 - 13:40 = 6,33
