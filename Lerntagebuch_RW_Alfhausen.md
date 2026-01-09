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
Ich habe mir heute etwas über das Programmieren von Trading Bots in Python angeschaut und mir erste Schritte überlegt und notiert. Angefangen mit dem Laden historischer Daten (siehe oben). Als nächstes werde ich mir die Daten (Datum, Preise/MWh) visualisieren lassen in Jupyter Notebook. Ich habe Jupyter Notebook gewählt, weil es mir ermöglicht den Code zu unterteilen in Teilprogramme, die ich separat laufen lassen kann. Mir fällt gerade ein, dass ich noch viel mehr schreiben könnte, werde mich allerdings nur auf das Nötigste beschränken. Alles in allem habe ich heute einen Blick dafür bekommen, wie komplex der Strommarkt und das Stromnetz sind, welche Wirtschaftssubjekte beteiligt sind und das es dadurch jetzt schon gefühlt einen riesen Haufen an Parameter gibt, die später das Verhalten des Trading-Bots bestimmen werden. 

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
- PyCharm einrichten und Umgang trainieren
# Tag 74 (14.11.2025):

Freitag 7:20 - 13:40 = 6,33

- PyCharm einrichten und zurechtfinden
- Datenpflege (Ausbildungsordner sortieren)
- PyCharm: Üben von Klassen und mehreren Programmen (dateiübergreifend)
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Python (& Finance) Basics (397-403)

# Tag 75 (15.11.2025):

Samstag 11:15 - 13:30  + 14:00 - 15:15 (Unterbrechung/Pause) = 3,5

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Python (& Finance) Basics (Programmierübung exercise 1+411)
- Anmeldung SecIT Hannover, FMB Bad Salzuflen und Python Barcamp Karlsruhe

# Tag 76 (17.11.2025):

Montag 8:00 - 14:30 + 19:15 - 20:45 = 8

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Python (& Finance) Basics (411-418)+Exercise_3.ipynb

# Tag 77 (18.11.2025):

Dienstag 7:00 - 13:00 = 6

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Python (& Finance) Basics (419-426), Exercise 4 start

# Tag 78 (19.11.2025):

Mittwoch 8:20 - 16:40 (13:15-13:45 Pause) = 7,83

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Python (& Finance) Basics (427-432), User-Defined-Functions (445-454), Day Trading, Online Brokers and APIs (7-9)

# Tag 79 (20.11.2025):

Donnerstag 7:20 - 16:40 (13:00-13:30 Pause) = 8,83

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 3 - Day Trading with OANDA - Deep Dive (20-28), Abschnitt 1 -Introduction to Time Series Datas in Panda (107-)
- Programmieren in JPYNB: API starten, Accountdaten erfassen, DataFrame manipulieren
- Gespräch mit Hendrik: 4 Quadrantenmodell Energietechnik, Blindleistung, Wirkleistung und Scheinleistung (Bierglasmodell)
- OANDA Trade Training
- Recherche: Hochfrequenzhandel und Arbitrage, Python vs. C++ im Energiehandel

# Tag 79 (20.11.2025):

Freitag 8:40 - 13:40 = 5 

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 1 -Introduction to Time Series Datas in Panda (107-111)
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 12: Financial Data Analysis with Python and Pandas - a deep introduction (119-121)
- Buch: Python 3 - Programmieren für Einsteiger (S.13-16)
- Compiler VS Interpreter https://www.youtube.com/watch?v=DYsQj5bJaZI
- Funktion vs. Methode mit Paper Mario erklärt https://www.youtube.com/watch?v=QxKQEfLmG-Q
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 12: Financial Data Analysis with Python and Pandas - a deep introduction (122 start, parallel Datei class_Investment im Exercises Ordner erstellt)

# Tag 80 (24.11.2025):

Montag 7:20 - 17:40 (15:00-15:30 Pause) = 9,83

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 12: Financial Data Analysis with Python and Pandas - a deep introduction (122-132[8:00]) - Datei: simple_returns_vs_log_returns
- Simple Returns (Einfache Renditen) vs. Logarithmic Returns (logarithmische Renditen)
	- Simple Return (Einfacher Ertrag):  $$R=\left( \frac{Pneu-Palt}{Palt}\right)

$$
	- Logarithmic Return (Logarithmischer Ertrag):  $$ r = \ln \left( \frac{P_{\text{neu}}}{P_{\text{alt}}} \right) $$
	- Eulerische Zahl e: $$( e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n ) $$
	- Prozentuale Veränderung der Log-Perioden: $$e^r-1$$
- Python: Lambda-Funktion

# Tag 81 (25.11.2025):

Dienstag 8:35 - 17:40 (14:45-15:15 Pause) = 8,58

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 12: Financial Data Analysis with Python and Pandas - a deep introduction (132-144[0:20]) - Datei: 04_Short_Selling_Short_Positions_Returns.ipynb, 05_Short_Selling_Short_Position_Returns.ipynb, 06_Covariance_and_Correlation.ipynb, 07_Portfolio_and_Portfolio_Returns.ipynb

# Tag 82 (26.11.2025):

Mittwoch 7:20 - 16:40 (13:30-14:00) = 8,83

- Finanzmathematik aus Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS übertragen in Finanzmathematik.md
- Plaintext: Formeln erstellen in Finance_Statistics.md
- In Python: pct_changes() Quellcode einsehen und verstehen lernen https://github.com/pandas-dev/pandas/blob/main/pandas/core/generic.py#L11245
- Anlegen eines Code-Snippets als Python_Code_Snippets.md
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 12: Financial Data Analysis with Python and Pandas - a deep introduction (144[5:00]) - Datei: 08_Margin_Trading_and_Levered_Returns

# Tag 83 (27.11.2025):

Donnerstag 7:15 - 16:40 (13:30-14:00) = 8,92

-  Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 12: Financial Data Analysis with Python and Pandas - a deep introduction (144-146]) - Datei: 08_Margin_Trading_and_Levered_Returns
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: Abschnitt 13: Advanced Topics (147-149)
- Fehlersuche in 09_ImportData_MergingAligning_DatetimeIndex_Filling_ConvertingTimezones.ipynb
	- Fehler gefunden: mit to_excel(SP500) hatte ich versehentlich die Hauptdatei (SP500.xls) überschrieben, was zu mehreren Fehlern geführt hatte.
	  Fehler: **Excel file format cannot be determined, you must specify an engine manually** und **BadZipFile: File is not a zip file** hatten zu Verwirrung geführt. Durch try and error fand ich den Fehler. 

# Tag 84 (28.11.2025):

Freitag 9:15 - 11:30; 12:15 - 13:15; 15:00 - 15:45 = 4

 - Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS:
	 - Abschnitt 13: Advanced Topics (149-153)
 - OANDA Trading: Positionen geschlossen 
	 - 09:57 - Gewinn/Verlust (EUR/USD): +3679,88€
	 - 10:46 - Gewinn/Verlust (EUR/USD): +1292.59€
	 - 10:59 - Gewinn/Verlust (EUR/USD): +1523,48€
	 - 12:55 - Gewinn/Verlust (EUR/USD): +2341,65€
	 - 13:17 - Gewinn/Verlust (EUR/USD):   +479,70€
	 - 15:46 - Gewinn/Verlust (EUR/USD): +1297,07€
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 14: Object Oriented Programming (OOP): Creating a Financial Analysis Class (154-157 end)

# Tag 85 (01.12.2025):

Montag 6:20 - 14:40 (10:00-10:15 / 13:00-13:15 Pause) = 7,83

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 14: Object Oriented Programming (OOP): Creating a Financial Analysis Class (WIederholung 154-157 end) -> Wichtig1: Klassen erstellen ab Lektion 158
	- Abschnitt 14: Object Oriented Programming (OOP): Creating a Financial Analysis Class (WIederholung 158-166)
	- Abschnitt 15: Defining and Testing Trading Strategies (172-177)
	- Abschnitt 16: Defining and Backtesting SMA (Simply Moving-) Strategies (178-181)
- 5 Useful Dunder Methods In Python:
	- https://www.youtube.com/watch?v=y1ZWQQEe5PM
- OANDA Chart mit Moving-Average-Anzeige um Trends zu erkennen
	- Einstellung: 
		- Upper Length 200
		- Lower Length 50
		- Upper Offset -20
		- Lower Offset -20
		- Begründung Offset: Trendlinien nach hinten verschieben, um Trend früher zu erkennen
- Chartanalyse EUR/USD - SMA46 | SMA137 (NB_01_SMA.ipynb)![[Pasted image 20251201141051.png]]
	- Trends erkennen/antizipieren

# Tag 86 (02.12.2025):

Dienstag 6:20 - 16:40 (14:45-15:15 Pause) = 9,83

 - OANDA Trading: Positionen geschlossen 
	 - 07:51 - Gewinn/Verlust (EUR/USD): -3885,71€
	 - 07:54 - Gewinn/Verlust (EUR/USD):   -750,54€
	 - 08:14 - Gewinn/Verlust (EUR/USD):+1042,95€
	 - 08:43 - Gewinn/Verlust (EUR/USD):   -483,03€
	 - 08:52 - Gewinn/Verlust (EUR/USD): -1366,90€
	 - 09:28 - Gewinn/Verlust (EUR/USD): -1736,42€
	 - 09:56 - Gewinn/Verlust (EUR/USD):  +662,25€ (Gewinn = 9347,68€)
	 - Starke Seitwärtsbewegungen machen erschweren die Festlegung auf Long- oder Short-Positionen
	 - 12:30 - Gewinn/Verlust (EUR/USD):  +534,21€ (Gewinn = 9881,88€)
	 - 13:24 - Gewinn/Verlust (EUR/USD):  +309,22€ (Gewinn = 10191,10€)
	 - 16:09 - Gewinn/Verlust (EUR/USD):  +451,20€ (Gewinn = 10642,30€)
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 16: Defining and Backtesting SMA (Simply Moving-) Strategies (181-188)

# Tag 87 (03.12.2025):

Mittwoch 7:20 - 16:40 ( Pause) = 8,83

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 16: Defining and Backtesting SMA (Simply Moving-) Strategies (188-190 end)
	- Abschnitt 17: Defining and Backtesting simple Momentum/Contrarian Strategies (191-200)

 - OANDA Trading: Positionen geschlossen 
	 - 07:58 - Gewinn/Verlust (EUR/USD):    +56,41€ (Gewinn = 11.604,03€)
	 - 08:39 - Gewinn/Verlust (EUR/USD):  +961,73€ (Gewinn = 11660,44€)
	 - 09:59 - Gewinn/Verlust (EUR/USD):  +563,99€ (Gewinn = 12224,42€)
	 - 10:26 - Gewinn/Verlust (EUR/USD):  +846,26€ (Gewinn = 13070,68€)
	 - 11:42 - Gewinn/Verlust (EUR/USD):   -767,80€ (Gewinn = 12.302,88€)
	 - 11:42 - Gewinn/Verlust (EUR/USD): -2013,96€ (Gewinn = 10.288,92€)
	 - 13:12 - Gewinn/Verlust (EUR/USD): -2811,69€ (Gewinn =   7.477,23€)
	 - 13:32 - Gewinn/Verlust (EUR/USD):     -27,56€ (Gewinn =    7449,67€)
	 - 15:17 - Gewinn/Verlust (EUR/USD):    +846,38 (Gewinn =    8296,05€)
	 - 15:30 - Gewinn/Verlust (EUR/USD):    +582,14 (Gewinn =    8.878,19€)

# Tag 88 (04.12.2025):

Donnerstag 6:20 - 15:40 (14:00 - 14:30 Pause) =  8,83

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 18: Defining and Backtesting Mean-Reversion Strategies (Bollinger) (201-206)
	- Abschnitt 19: Trading Strategies powered by Machine Learning - Regression (208-218)
	- Abschnitt 20: Trading Strategies powered by Machine Learning - Classification (219 start)
- Machine Learning von A-Z: Lerne Python & R für Data Science!
	- Abschnitt 5: Lineare Regression (17-19+22)
	- Abschnitt 8: Lineare Regression mit mehreren Variablen (39-42)
- Regression Überanpassung (Overfitting) https://www.youtube.com/watch?v=eFBq7RX0Xd0
- OANDA Trading: Positionen geschlossen 
	 -  Gewinn/Verlust (EUR/USD):  +638,90€ (Kapital: 100638,90€)

# Tag 89 (05.12.2025):

Freitag 8:20 - 12:40 = 4,33

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 20: Trading Strategies powered by Machine Learning - Classification (219-225 started)
- Python Code Snippet erweitert um Pandas-DataFrame-Funktionen
- Sigmoid-Funktion: Wahrscheinlichkeitskurve von zwei Variablen wobei eine Variable binär ist. Beispiel: Wahrscheinlichkeit zu bestehen oder nicht (1, 0) gegenüber der Anzahl an aufgewendeten Lernstunden.  
	- https://www.youtube.com/watch?v=k-NNGEeWbG0

# Tag 90 (08.12.2025):

Montag 6:15 - 17:40 (14:00-14:30 Pause) = 10,91

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 20: Trading Strategies powered by Machine Learning - Classification (225-228)
	- Abschnitt 21: Advanced Backtesting Techniques (229-242)
	- Abschnitt 22: Part 4: Realt-time Implementation and Automation of Strategy (244-245)
	- Abschnitt: 23: Implementation and Automation with OANDA (246-247)

- Streaming data from ENTSO-E with entsoe_streaming_REST_API.ipynb does not work, probably broken API-Key. Tried another API-key. Support contacted. Waiting for response! 

# Tag 91 (09.12.2025):

Dienstag 8:30 - 16:40 (Pause 14:00-14:30) = 7,66

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 23: Implementation and Automation with OANDA (248-262+269-270)
	- Abschnitt 32: Adding Stop Loss and Take Profit to the Trading Bot (372-373) 
- Installed PyCharm Pro for Students; what´s new in PyCharm Pro ? https://www.youtube.com/watch?v=9ytQ1phbckw

# Tag 92 (10.12.2025):

Mittwoch 7:20 - 16:40 (P 14:50-15:20) = 8,83

- Trading Bot (Bollinger Strategie) programmieren und testen auf oanda.com

# Tag 93 (11.12.2025):

Donnerstag 7:20 - 16:40 (P 12:30-13:00) = 8,83

- Trading Bot (Bollinger Strategie) programmieren und testen auf oanda.com
	- Code-Erklärung erstellt
	- versucht Live-Chart mit Bollinger Bänder zu erstellen 
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 32: Adding Stop Loss and Take Profit to the Trading Bot (374-376 ) 

# Tag 94 (12.12.2025):

Freitag 7:20 - 11:40 = 5,33 (ÜStd=0)

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 32: Adding Stop Loss and Take Profit to the Trading Bot (376-384) 
	- Abschnitt 23: Implementation and Automation with OANDA (263-264 start)
- Testing Contrarian Bot and SMA Bot on Oanda 

# Tag 95 (13.12.2025):

Samstag 9:30 - 14:30 = 5,00 (ÜStd=5)

- Signatur in Outlook erstellt
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 23: Implementation and Automation with OANDA (264-265 Start)


# Tag 96+97 (15.-16.12.2025): krank


# Tag 98 (17.12.2025):

Mittwoch 7:20 - 16:40 (P 14:50-15:20) = 8,83 (ÜStd=5,83)

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 23: Implementation and Automation with OANDA (265-266)
- programming simple Oanda_Machine_Learning_Bot.ipynb

# Tag 99 (18.12.2025):

Donnerstag 7:20 - 15:40 (ohne Pause) = 8,33 (ÜStd=6,16)

- Running Oanda_Machine_Learning_Bot_II.ipynb
	- result: 1200 ticks (12min) profit: +5,85€
- Udemy: Der ultimative Python-Kurs für Data Science, ML & AI: 
	- Abschnitt 7: Module in Python (81-82)
	- Abschnitt 8: Mathematische Berechnungen: NumPy (83-87)
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 29: Working with two or many strategies (combination) (330-337)
	- Abschnitt 30: A Machine Learning-powered Strategy A-Z (DNN) (338-351)
	- Abschnitt 31: Error Handling: How to make your Trading Bot more stable and reliable (352-354) + (363-365 Start) 365= Error Handling V20 Connection Timeout !!!

# Tag 99 (18.12.2025):

Freitag 8:20 - 13:40 = 5,33  (ÜStd=6,16-2,66=**3,5**)

- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 31: Error Handling: How to make your Trading Bot more stable and reliable (365-366) + (355-362)
	- Abschnitt 34: Appendix 1: Python (& FInance) Basics (404-410) + (433-444)
- Running Oanda_Machine_Learning_Bot_III for 60 minutes

# Tag 100 (22.12.2025):

Montag 13:15 - 17:30 (P 15:30 - 16:00)  = 2,25+1,25 = 4,00

- going deeper in understanding construction of Oanda_Machine_Learning_Bot_III_copied.ipynb
- Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 36: Appendix 3: Numpy, Pandas, Matplotlib and Seaborn Crash Course (455-459 Start)

# Tag 101 (02.01.2026):

Freitag 8:00 - 16:15 (P 12:30-13:00) = 7,75

 Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 36: Appendix 3: Numpy, Pandas, Matplotlib and Seaborn Crash Course (460-465 Start)

# Tag 102 (05.01.2026):

Montag 10:00 - 11:00; 16:00 - 18:45; 20:00 - 22:00 = 5,75

Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 36: Appendix 3: Numpy, Pandas, Matplotlib and Seaborn Crash Course (465-470 Start)

# Tag 103 (06.01.2026):

Dienstag 8:10 - 8:30 (im Zug); 9:00 - 17:00 (14:15-14:45) = 7,83

Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 36: Appendix 3: Numpy, Pandas, Matplotlib and Seaborn Crash Course (474 Start)

Running Machine_Learning_Bot_III: 

Prüfungsvorbereitung Aktuell - Teil 2 der gestreckten Abschlussprüfung: S.7-36

# Tag 104 (07.01.2026):

Mittwoch 8:30 - 19:00 (P 16:45-17:15) = 10

Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 36: Appendix 3: Numpy, Pandas, Matplotlib and Seaborn Crash Course (476-481, 483-486 Start)

Wissen über Trading Bots: https://www.youtube.com/watch?v=SnOTRPKb4I0

Krypto-Trading-Bots: Der umfassende Guide für Einsteiger und Profis https://www.okx.com/de/learn/okx-trading-bot-guide

# Tag 105 (08.01.2026):

Donnerstag 8:30 - 15:00 = 6,5

Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 36: Appendix 3: Numpy, Pandas, Matplotlib and Seaborn Crash Course (486-500 Start)
Abschlussprojektbesprechung: Die Auswahl des Projektes für die Abschlussarbeit so einfach und flach wie möglich zu halten.
- Vorschlag: Maschinendaten überwachen mittels eines Alertsystems

# Tag 106 (09.01.2026):

Freitag 8:30 - 15:30 = 7

Udemy:  Algorithmic Trading A-Z with Python, Machine Learning & AWS: 
	- Abschnitt 36: Appendix 3: Exercises (7-10 Start)

Intern: Jorit stellt seine Bachelorarbeit vor