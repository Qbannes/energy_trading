

# **Pandas**

## 1. Daten einlesen/speichern

0. **einlesen CSV / EXCEL**

```Python
pd.read_csv(r'Pfad+Name')
```

```Python
pd.read_excel(r'Pfad+Name')
```

0.1. **speichern CSV / EXCEL**

```Python
Dateiname.to_csv('NeuerName.csv')
```

```Python
Dateiname.to_excel('NeuerName.xls')
```

1. **Nur bestimmte Spalten einlesen**

Lese nur die benötigten Spalten aus einer Datei:

  

```python

pd.read_csv(r"Pfad+Dateiname", usecols=["spalte1", "spalte2"])

```

```Python
close = pd.read_csv(r"C:\Users\bedla\Documents\Ausbildung_Informatik\1_Praktikum\Praktikum_Daten-_und_Prozessanalyse\energy_trading\PyCharm_Notebook\Data\close.csv", index_col = "Date", parse_dates = ["Date"])
```

2. **Datumsangaben direkt beim Einlesen parsen**

Direkt beim Einlesen in ein Datumsformat umwandeln lassen:

  

```python

pd.read_csv("datei.csv", parse_dates=["datums_spalte"])

```

  

3. **Datentypen festlegen**

Spare Speicherplatz, indem du beispielsweise Kategorien schon beim Einlesen deklarierst:

  

```python

pd.read_csv("datei.csv", dtype={"spalte": "category"})

```

  

4. **Index setzen**

Setze beim Importieren direkt den Index (z. B. bei Zeitreihen):

  

```python

pd.read_csv("datei.csv", index_col="zeitstempel")

```

  

5. **Begrenzte Zeilenzahl laden**

Lese nur eine bestimmte Anzahl an Zeilen ein:

  

```python

pd.read_csv("datei.csv", nrows=100)

```

  

6. **Zeilen überspringen**

Überspringe unerwünschte / fehlerhafte Zeilen:

  

```python

pd.read_csv("datei.csv", skiprows=[0, 2])

```

  

7. **NA-Werte bestimmen**

Bestimme benutzerdefinierte Werte als NA:

  

```python

pd.read_csv("datei.csv", na_values=["?", "keineAngabe"])

```

  

8. **Boolesche Werte setzen**

Konvertiere "Yes"/"No" Spalten direkt:

  

```python

pd.read_csv("datei.csv", true_values=["Yes"], false_values=["No"])

```

  

9. **Daten aus mehreren Dateien laden**

Mehrere Dateien mit `glob` einlesen:

  

```python

import glob

files = glob.glob("daten/*.csv")

df = pd.concat([pd.read_csv(f) for f in files])

```

  

10. **Direkt aus der Zwischenablage laden**

Daten aus Excel kopieren und per Pandas laden:

  

```python

df = pd.read_clipboard()

```

  

11. **Tabellen aus PDFs lesen**

Tabellen aus PDF-Dateien lesen (z. B. mit tabula-py):

  

```python

import tabula

tabula.read_pdf("datei.pdf", pages="all")

```

  
12. **Register aus Excel wählen**

```Python
pd.read_excel('Pfad+Dateiname', sheet_name=`Register2`)
```

***

  

## 2. Explorative Datenanalyse (EDA)

  

12. **EDA Cheat**

Ein komplettes Reporting mit `pandas-profiling`:

  

```python

import pandas_profiling

df.profile_report()

```

  
  

***

  

## 3. Datentypen (dtypes)

  

13. **Spalten nach Datentyp filtern**

  

```python

df.select_dtypes(include=["number"])

```

  

14. **Datentyp automatisch erkennen lassen**

  

```python

df["spalte"] = pd.to_numeric(df["spalte"], errors="coerce")

```

  

15. **Downcasting (Typ-Verkleinerung)**

Speicher sparen durch Downcasting:

  

```python

df["spalte"] = pd.to_numeric(df["spalte"], downcast="float")

```

  

16. **Manuelle Konvertierung**

Fehler robust abfangen und NAs ersetzen:

  

```python

df["spalte"] = pd.to_numeric(df["spalte"], errors="coerce").fillna(0)

```

  

17. **Alle Spalten auf einmal konvertieren**

  

```python

df = df.apply(pd.to_numeric, errors="coerce")

```

  
  

***

  

## 4. Spalten-Operationen

  

18. **Spalten umbenennen**

  

```python

df.rename(columns={"alt": "neu"}, inplace=True)

```

  

19. **Suffix oder Präfix hinzufügen**

  

```python

df.add_prefix("vor_").add_suffix("_nach")

```

  

20. **Neue Spalten erstellen (Mutate)**

  

```python

df["neu"] = df["a"] + df["b"]

```

  

21. **Spalten an bestimmter Position einfügen**

  

```python

df.insert(0, "neue_spalte", wert)

```

  

22. **if-then-else Logik**

  

```python

df["kategorie"] = np.where(df["wert"] > 0, "positiv", "negativ")

```

  

23. **Spalten löschen**

  

```python

df.drop("spalte", axis=1, inplace=True)

```

  
Liste erstellen (passend zur Zeilenanzahl) und als Index setzen 

```Python
new_index = [f'Spaltenname{i}' for i in range(1,summer.index.size+1)]
df.index=new_index
```
***

  

## 5. String-Operationen

  

24. **Spaltennamen zu Kleinbuchstaben**

  

```python

df.columns = df.columns.str.lower()

```

  

25. **Enthält einen String?**

  

```python

df[df["spalte"].str.contains("suchbegriff")]

```

  

26. **Alle Treffer mit findall**

  

```python

df["matches"] = df["text"].str.findall("regex")

```

  
  

***

  

## 6. Fehlende Werte

  

27. **Fehlende Werte prüfen**

  

```python

df.isna().sum()

```

  

28. **Fehlende Werte verarbeiten**

```python

df.fillna(0, inplace=True)

```

29. Fehlende Werte löschen

```Python
df.dropna()
```
  
30. Fehlende Werte Anzeigen

```Python
df.isna()
```

30. Nicht fehlende Werte Anzeigen

```Python
df.notna()
```
***

  

## 7. Datumsoperationen

  

29. **X Tage/Stunden/Wochen ab heute**

  

```python

pd.Timestamp.today() - pd.Timedelta(days=3)

```

  

30. **Nach Zeitraum filtern**

  

```python

df[(df["datum"] >= "2023-01-01") & (df["datum"] <= "2023-12-31")]

```

  

31. **Nach Tag/Monat/Jahr filtern**

  

```python

df[df["datum"].dt.month == 1]

```

  
  

***

  

## 8. DataFrame-Styling

  

32. **Zahlenformat**

  

```python

df.style.format({"spalte": "{:.2f}"})

```

  

33. **Farbige Hervorhebung**

  

```python

df.style.applymap(lambda x: "background-color: yellow" if x < 0 else "")

```

  
  

***

  

## 9. Verschiedenes

  

34. **Index des Maximums / Minimums erhalten**

  

```python

df["spalte"].idxmax()

df["spalte"].idxmin()

```

  

35. **Funktion auf DataFrame anwenden**

  

```python

df.apply(np.sqrt)

```

  

36. **Daten zufällig mischen**

  

```python

df.sample(frac=1).reset_index(drop=True)

```

  

37. **Prozentuale Veränderung**

  

```python

df["ret"] = df["preis"].pct_change()

```

  

38. **Rang berechnen**

  

```python

df["rang"] = df["wert"].rank()

```

  

39. **Speichernutzung überprüfen**

  

```python

df.memory_usage(deep=True)

```

  

40. **Listenwerte auf Zeilen aufteilen („explode“)**

  

```python

df.explode("listen_spalte")

```

  

41. **Kleine Kategorien zu 'Andere' gruppieren**

  

```python

top = df["kat"].value_counts().nlargest(5).index

df["kat_neu"] = np.where(df["kat"].isin(top), df["kat"], "Andere")

```




## 10. Einstellungen

### 1. Anzahl der angezeigten Zeilen steuern

  

Mit dieser Option bestimmst du, wie viele Zeilen eines DataFrames im Output angezeigt werden. Praktisch bei großen Datensätzen!

  

```python

import pandas as pd

  

pd.set_option('display.max_rows', 10)

```

  

**Beschreibung:**

Damit werden nur maximal 10 Zeilen eines DataFrame angezeigt. Das „…“ zeigt an, dass weitere Zeilen existieren.

  

***

  

### 2. Anzahl der angezeigten Spalten steuern

  

Hiermit kontrollierst du, wie viele Spalten beim Anzeigen sichtbar sind.

  

```python

pd.set_option('display.max_columns', 5)

```

  

**Beschreibung:**

Nur bis zu 5 Spalten werden dargestellt. Bei mehr Spalten als eingestellt, erscheinen sie ausgeblendet mit „…“.

  

***

  

### 3. Wissenschaftliche Notation unterdrücken

  

Mit dieser Einstellung vermeidest du, dass Fließkommazahlen als wissenschaftliche Notation (z. B. 1e+10) dargestellt werden.

  

```python

pd.set_option('display.float_format', '{:.2f}'.format)

```

  

**Beschreibung:**

Alle Fließkommazahlen werden mit zwei Dezimalstellen und als normale Zahl angezeigt.

  

***

  

### 4. Genauigkeit von Fließkommazahlen (Floating Point Precision)

  

Bestimme, wie viele Dezimalstellen Fließkommazahlen im Output haben sollen.

  

```python

pd.set_option('precision', 3)

```

  

**Beschreibung:**

Werte werden z.B. als 3.142 statt 3.14159265 angezeigt, also auf drei Nachkommastellen gerundet.

  

***

  

### 5. Format der Dezimaltrennung bestimmen

  

In manchen Ländern wird beim Dezimalformat z. B. ein Komma statt eines Punktes verwendet. Dies lässt sich über die Format-Option anpassen.

  

```python

pd.set_option('display.float_format', lambda x: '{:,.2f}'.format(x))

```

  

**Beschreibung:**

Damit erscheinen z. B. 12345.678 als 12,345.68 (mit Komma und zwei Dezimalstellen).

*Hinweis: Für deutsche Konvention kann man mit Projekten wie Babel lokalisieren.*

  

***

  

### 6. Backend für Plotting ändern

  

Pandas kann unterschiedliche Backend-Bibliotheken für Diagramme verwenden. Die Standardbibliothek ist Matplotlib – dies kann aber geändert werden.

  

```python

pd.options.plotting.backend = "plotly"

```

  

**Beschreibung:**

Diagramme werden dann z.B. mit Plotly statt Matplotlib erzeugt und sind oft interaktiv.

  

***

  

### 7. Alle Anzeigeoptionen zurücksetzen

  

Wenn du alle gesetzten Optionen auf die Pandas-Standardwerte zurücksetzen willst, kannst du diese Methode nutzen.

  

```python

pd.reset_option('all')

```

  

**Beschreibung:**

Das entfernt alle benutzerdefinierten Anzeigeoptionen und stellt die Default-Anzeige wieder her.



## 11. pd.DataFrame

### 1. DataFrame aus Listen erstellen 

```Python
Gesamtdaten=pd.DataFrame({'Alter': Altersdaten, 'Einkommen': Einkommensdaten})
```
### 2. Aus Dict-Listen (transpose): Mit custom Index
```Python
Gesamtdaten=pd.DataFrame([{'Alter': 25, 'Einkommen': 50000}, {'Alter': 30, 'Einkommen': 60000}])
```

### 3. Aus 2D-Liste: Manuelle Spalten
```Python
Gesamtdaten=pd.DataFrame([[25, 50000], [30, 60000]], columns=['Alter', 'Einkommen'])
```

### 4. Aus NumPy-Array für numerische Daten

```Python
Gesamtdaten=pd.DataFrame(np.array([[25, 50000], [30, 60000]]), columns=['Alter', 'Einkommen'])
```

### 5. Leeres DataFrame für schrittweises befüllen

```Python
Gesamtdaten=pd.DataFrame(columns=['Alter', 'Einkommen'])
```

### 6. Aus Series Einzelspalte erweitern

```Python
pd.DataFrame({'Alter': pd.Series(Altersdaten)})
```

### 7. Aus Liste von Dicts: Zeilen als Dicts

```Python
pd.DataFrame([{'Alter': 25, 'Einkommen': 50000}, {'Alter': 30, 'Einkommen': 60000}])` – Zeilen als Dicts.
```

## 12. Display Options/Anzeigeoptionen

### 12.1 max/minimal möglich anzuzeigende  
```Python
pd.options.display.max_rows
```

```Python
pd.options.display.min_rows
```

### 12.2 Head (erste 5 Zeilen)
```Python
df.head(-Anzahl der Zeilen-)
```

### 12.3 Tail (letzte 5 Zeilen)
```Python
df.tail(-Anzahl der Zeilen-)
```

### 12.4 Statistik

Gibt statistische Werte wie Durchschnitt, Min, Max, Perzentile, Standardabweichung und Anzahl aus
```Python
df.describe()
```

Gibt statistische Werte für Objekte(-spalten) (Strings/Text) aus
```python
df.describe(include='O')
```

Minimum jeder numerischen Spalte
```Python
df.min(numeric_only=True)
```

Durchschnitt jeder numerischen Spalte
```Python
df.mean(numeric_only=True)
```
## 13. Atribute (Index, Spalten, Größe, Form, Infos)

zeigt die Form an (Anzahl Zeilen und Anzahl Spalten)
```Python
df.shape
```

Gesamtzahl aller Elemente
```Python
df.size
```

Indexinformationen
```Python
df.index
```

Spalten anzeigen
```Python
df.columns
```

Informationen (Spalte, Nicht-Null-Anazhl, Datentyp)
```Python
df.info()
```


## 14. Sortieren

```Python
df.sort_values()
```
# **Matplotlib**

## 1. Liniendiagramm (Line Plot)

  

```python

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y = [10, 20, 25, 30]

plt.plot(x, y)

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

plt.title('Einfache Linie')

plt.show()

```

DataFrame plotten
```Python
msft[['Returns','Leverage_Returns']].plot(figsize=(15,8),fontsize=13)  
plt.legend(fontsize=13)  
plt.show()
```

Mit mathematischen Funktionen versehendes DataFrame plotten
```Python
msft[['Returns','Leverage_Returns']].add(1).cumprod().plot(figsize=(15,8),fontsize=13)  
plt.legend(fontsize=13)  
plt.show()
```
*(Vorschau: Liniendiagramm)*

  

***

  

## 2. Balkendiagramm (Bar Plot)

  

```python

categories = ['A', 'B', 'C']

values = [3, 7, 5]

plt.bar(categories, values)

plt.title('Balkendiagramm')

plt.show()

```


  

## 3. Histogramm

  

```python

import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30)

plt.title('Histogramm')

plt.show()

```

  
  

***

  

## 4. Punktwolke (Scatterplot)

  

```python

plt.scatter(x, y)

plt.title('Streudiagramm')

plt.show()

```

  
  

***

  

## 5. Tortendiagramm (Pie Chart)

  

```python

labels = ['A', 'B', 'C', 'D']

sizes = [15, 30, 45, 10]

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.axis('equal')

plt.title('Tortendiagramm')

plt.show()

```

  
  

***

  

## 6. Achsentitel und Diagrammtitel (Titles und Labels)

  

```python

plt.plot(x, y)

plt.title("Individueller Titel", fontsize=16, color='blue', loc='center')

plt.xlabel("X-Achse", fontsize=12, color='green')

plt.ylabel("Y-Achse", fontsize=12, color='red')

plt.show()

```

  
  

***

  

## 7. Legende erstellen

  

```python

x = [1, 2, 3, 4]

y1 = [10, 20, 25, 30]

y2 = [15, 25, 20, 35]

plt.plot(x, y1, label='Datensatz 1', color='blue')

plt.plot(x, y2, label='Datensatz 2', color='orange')

plt.title('Mit Legende')

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

plt.legend(loc='upper left', ncol=1, facecolor='lightgray', fontsize='medium')

plt.show()

```

  
  

***

  

## 8. Rasterlinien (Gridlines) anpassen

  

```python

import numpy as np

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.title('Gridlines angepasst')

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

plt.grid(color='blue', linestyle='-.', linewidth=1.5, alpha=0.7)

plt.show()

```

  
  

***

  

## 9. Farben und Linien-Stile

  

```python

x = [1, 2, 3, 4]

y1 = [10, 20, 25, 30]

y2 = [15, 25, 20, 35]

plt.plot(x, y1, label='Datensatz A', color='red', linestyle='-', linewidth=2)

plt.plot(x, y2, label='Datensatz B', color='blue', linestyle='--', marker='o', markersize=8)

plt.title('Farben und Stile angepasst')

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

plt.legend()

plt.show()

```

  
  

***

  

## 10. Subplots erstellen

  

```python

import numpy as np

x = np.array([0, 1, 2, 3])

y1 = np.array([3, 8, 1, 10])

y2 = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 1)

plt.plot(x, y1)

plt.title('Diagramm 1')

plt.subplot(1, 2, 2)

plt.plot(x, y2)

plt.title('Diagramm 2')

plt.show()

```

  
  

***

  

## 11. Achs-Limits setzen

  

```python

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.xlim(0, 10)

plt.ylim(-1.5, 1.5)

plt.title('Sinus mit Bereich')

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

plt.grid(True)

plt.show()

```

  
  

***

  

## 12. Achsen teilen (shared axes)

  

```python

x = np.linspace(0, 10, 100)

y1 = np.sin(x)

y2 = np.cos(x)

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

axs[^0].plot(x, y1, color='blue')

axs[^0].set_title('Sinus')

axs[^1].plot(x, y2, color='orange')

axs[^1].set_title('Kosinus')

for ax in axs:

    ax.set_ylabel('Wert')

plt.xlabel('Geteilte X-Achse')

plt.tight_layout()

plt.show()

```

  
  

***

  

## 13. Tabellen erstellen

  

```python

data = [

    ['Jahr', 'Umsatz', 'Gewinn'],

    [2021, 15000, 3000],

    [2022, 20000, 5000],

    [2023, 25000, 7000]

]

fig, ax = plt.subplots()

ax.axis('tight')

ax.axis('off')

table = ax.table(cellText=data, colLabels=['Jahr', 'Umsatz', 'Gewinn'], loc='center', cellLoc='center', rowColours=['lightgrey']*4)

plt.title("Umsatz-Tabelle")

plt.show()

```

  
  

***

  

## 14. Tabelle aus Pandas-DataFrame plotten

  

```python

import pandas as pd

data = {'Jahr': [2021, 2022, 2023], 'Umsatz': [15000, 20000, 25000], 'Gewinn': [3000, 5000, 7000]}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

ax.axis('tight')

ax.axis('off')

table = pd.plotting.table(ax, df, loc='center', cellLoc='center')

plt.title("Tabelle aus DataFrame")

plt.show()

```

  
  

***

  

## 15. Diagramm speichern (verschiedene Formate)

  

```python

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.title('Sinuswelle')

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

for fmt in ['png', 'pdf', 'svg']:

    plt.savefig(f'sinus.{fmt}', dpi=300, bbox_inches='tight')

plt.show()

```

  
  

***

  

## 16. DPI und Figurgröße anpassen

  

**a. Direkt beim Erstellen:**

  

```python

plt.figure(figsize=(8, 6), dpi=100)

plt.plot([1, 2, 3], [1, 4, 9])

plt.title('Eigene Größe/DPI')

plt.show()

```

  

**b. Nachträglich ändern:**

  

```python

fig = plt.figure()

plt.plot([1, 2, 3], [1, 4, 9])

fig.set_size_inches(10, 5)

fig.set_dpi(150)

plt.title('Geänderte Größe/DPI')

plt.show()

```

  

**c. Global über rcParams:**

  

```python

plt.rcParams['figure.figsize'] = (10, 5)

plt.rcParams['figure.dpi'] = 150

plt.plot([1, 2, 3], [1, 4, 9])

plt.title('Globale Defaultwerte')

plt.show()

```

  
  

***

  

## 17. Annotationen und Text

  

```python

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.annotate('Lokal Max', xy=(1.57, 1), xytext=(3, 0.5), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.title('Sinuswelle mit Annotation')

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

plt.grid(True)

plt.show()

```

  
  

***

  

## 18. Achsenbeschriftungen und Ticks anpassen

  

```python

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.xticks(ticks=[0, 1, 2, 3], labels=['Null', 'Eins', 'Zwei', 'Drei'])

plt.yticks(fontsize=10)

plt.title('Angepasste Ticks')

plt.xlabel('X-Achse')

plt.ylabel('Y-Achse')

plt.grid(True)

plt.show()

```

  
  

***

  

## 19. Stylesheets verwenden

  

```python

plt.style.use('ggplot')

x = [1, 2, 3, 4]

y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("ggplot Style")

plt.show()

```

  
  

***

  

**Hinweise:**

  

- Die Bild-URLs sind beispielhaft und sollten ggf. mit echten, generierten Grafiken aus deiner Entwicklungsumgebung ersetzt werden.

- Die Reihenfolge orientiert sich an den Plot-Typen und Features wie auf der Quellseite.

  

---

  

<div align="center">⁂</div>

  

[^1]: https://www.geeksforgeeks.org/blogs/matplotlib-snippets/



# 1) **Numpy**

## Was ist NumPy?

NumPy steht für „Numerical Python“. Die Bibliothek ist speziell entwickelt worden, um numerische Berechnungen effizient durchzuführen und große mehrdimensionale Arrays und Matrizen zu unterstützen. Sie ist schnell (da sie teilweise in C geschrieben ist) und daher in Data Science, maschinellem Lernen und wissenschaftlicher Analyse weit verbreitet.
## 1. Eindimensionale Arrays

  

Ein eindimensionales Array erzeugst du mit `np.array()`:

  

```python

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])

print(arr_1d)

```

  

**Output:**

  

```

[1 2 3 4 5]

```

  
  

***

  

## 2. Zweidimensionale Arrays

  

### 2.1 Ein 2D-Array entsteht mit einer Liste von Listen:

  

```python

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d)

```

**Output:**
```Python

[[1 2 3]

 [4 5 6]]

```

***
### 2.2 Zusammenführen homogener Arrays

```Python
project_1 = np.array([-200, 20, 50, 70, 100, 50, 0, 0])  
project_2 = np.array([-50, 10, 25, 25, 50, 0, 0, 0])  
project_3 = np.array([-1000, 200, 200, 300, 500, 500, 750, 250])  

projects = np.array([project_1, project_2, project_3])
```
  
### 2.3 Auffüllen inhomogener Arrays mit np.pad( )

```Python
projects123 = [[-200, 20, 50, 70, 100, 50], [-50, 10, 25, 25, 50], [-1000, 200, 200, 300, 500, 500, 750, 250]]  
projects = np.array([np.pad(p, (0, 8-len(p))) for p in projects123])  
projects
```
## 3. Arrays mit vordefiniertem Inhalt erstellen

  

**a) Nullen**

  

```python

zeros_array = np.zeros((2, 3))

print(zeros_array)

```

  

**Output:**

  

```

[[0. 0. 0.]

 [0. 0. 0.]]

```

  

**b) Einsen**

  

```python

ones_array = np.ones((3, 3))

print(ones_array)

```

  

**Output:**

  

```

[[1. 1. 1.]

 [1. 1. 1.]

 [1. 1. 1.]]

```

  

**c) Mit bestimmtem Wert**

  

```python

full_array = np.full((2, 2), 7)

print(full_array)

```

  

**Output:**

  

```

[[7 7]

 [7 7]]

```

  

**d) Gleichmäßige Werte**

  

```python

range_array = np.arange(0, 10)

print(range_array)

```

  

**Output:**

  

```

[0 1 2 3 4 5 6 7 8 9]

```

  

**e) Gleichmäßig verteilte Werte (mit linspace)**

  

```python

linspace_array = np.linspace(0, 1, 5)

print(linspace_array)

```

  

**Output:**

  

```

[0.   0.25 0.5  0.75 1.  ]

```

  
  

***

  

## 4. Array-Attribute

  

**Form (shape):**

  

```python

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)

```

  

**Output:**

  

```

(2, 3)

```

  

**Datentyp (dtype):**

  

```python

print(arr.dtype)

```

  

**Größe (size):**

  

```python

print(arr.size)

```

  

**Output:**

  

```

6

```

  

**Dimensionen (ndim):**

  

```python

print(arr.ndim)

```

  

**Output:**

  

```

2

```

  
  

***

  

## 5. Indexierung \& Slicing

  

**Eindimensional:**

  

```python

arr_1d = np.array([10, 20, 30, 40, 50])

print(arr_1d[0])    # 10

print(arr_1d[3])    # 40

```

  

**Zweidimensional:**

  

```python

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d[0, 1]) # 2

print(arr_2d[1, 2]) # 6

```

  
  

***

  

## 6. Fortgeschrittenes Slicing

  

```python

# 1D

print(arr_1d[1:4])    # [20 30 40]

  

# 2D

print(arr_2d[:, 1])   # [2 5]

print(arr_2d[0, :])   # [1 2 3]

```

  
  

***

  

## 7. Boolean Indexing (Filtern mit Bedingungen)

  

```python

print(arr_1d[arr_1d > 20])  # [30 40 50]

```

  
  

***

  

## 8. Arrays umformen und Flatten

  

**Umformen:**

  

```python

array1 = np.array([1, 3, 5, 7, 9, 11])

array2 = np.reshape(array1, (2, 3))

print(array2)

```

  

**Output:**

  

```

[[ 1  3  5]

 [ 7  9 11]]

```

  

**Flatten:**

  

```python

flattened_array = array2.flatten()

print(flattened_array)

```

  

**Output:**

  

```

[ 1  3  5  7  9 11]

```

  
  

***

  

## 9. Arrays zusammenfügen und teilen

  

```python

array3 = np.array([[1, 2], [3, 4]])

array4 = np.array([[5, 6], [7, 8]])

  

vertical_concat = np.vstack((array3, array4))

print(vertical_concat)

# [[1 2]

#  [3 4]

#  [5 6]

#  [7 8]]

  

horizontal_concat = np.hstack((array3, array4))

print(horizontal_concat)

# [[1 2 5 6]

#  [3 4 7 8]]

  

split_arrays = np.split(vertical_concat, 2)

print(split_arrays)

```

  
  

***

  

## 10. Werte im Array ändern

  

```python

array1[0] = 100

print(array1)

# [100   3   5   7   9  11]

  

array2[0, 1] = 200

print(array2)

# [[  1 200   5]

#  [  7   9  11]]

```

  
  

***

  

## 11. Elementweise Mathematik

  

```python

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

  

addition = a + b

subtraktion = a - b

multiplikation = a * b

division = a / b

potenz = a ** b

  

print("Addition:", addition)

print("Subtraktion:", subtraktion)

print("Multiplikation:", multiplikation)

print("Division:", division)

print("Potenz:", potenz)

```

  

**Output:**

  

```

Addition: [5 7 9]

Subtraktion: [-3 -3 -3]

Multiplikation: [ 4 10 18]

Division: [0.25 0.4  0.5 ]

Potenz: [  1  32 729]

```

  
  

***

  

## 12. Universal Functions (ufuncs)

  

```python

add_res = np.add(a, b)

print("Ufunc Addition:", add_res)

multiply_res = np.multiply(a, b)

print("Ufunc Multiplikation:", multiply_res)

```

  
  

***

  

## 13. Aggregat-Funktionen

  

```python

arr = np.array([[1, 2, 3], [4, 5, 6]])

  

total_sum = np.sum(arr)

print("Gesamtsumme:", total_sum)

  

mean_value = np.mean(arr)

print("Mittelwert:", mean_value)

  

std_dev = np.std(arr)

print("Standardabweichung:", std_dev)

  

summe_spalten = np.sum(arr, axis=0)

print("Spaltensumme:", summe_spalten)

  

summe_zeilen = np.sum(arr, axis=1)

print("Zeilensumme:", summe_zeilen)

```

  
  

***

  

## 14. Lineare Algebra

  

**Matrixmultiplikation:**

  

```python

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

  

C = A @ B

print(C)

# [[19 22]

#  [43 50]]

D = np.dot(A, B)

print(D)

# [[19 22]

#  [43 50]]

```

  

**Determinante \& Inverse:**

  

```python

matrix = np.array([[4, 2], [3, 1]])

det = np.linalg.det(matrix)

print("Determinante:", det)

inverse = np.linalg.inv(matrix)

print("Inverse:")

print(inverse)

```

  
  

***

  

## 15. Lösen von Gleichungssystemen

  

```python

A = np.array([[3, 2], [1, 2]])

b = np.array([5, 5])

solution = np.linalg.solve(A, b)

print("Lösung:", solution)

# Lösung: [0. 2.5]

```

  
  

***

  

## 16. Statistische Funktionen

  

```python

data = np.array([1, 2, 3, 4, 5, 6])

  

mean_value = np.mean(data)

median_value = np.median(data)

varianz = np.var(data)

std_dev_value = np.std(data)

  

print("Mittelwert:", mean_value)

print("Median:", median_value)

print("Varianz:", varianz)

print("Standardabweichung:", std_dev_value)

```

  
  

***

  

## 17. Korrelation und Kovarianz

  

```python

x = np.array([1, 2, 3, 4, 5])

y = np.array([2, 4, 6, 8, 10])

  

correlation_matrix = np.corrcoef(x, y)

print("Korrelationsmatrix:")

print(correlation_matrix)

  

covariance_matrix = np.cov(x, y)

print("Kovarianzmatrix:")

print(covariance_matrix)

```

  
  

***

  

## 18. Ein-/Ausgabe von/zu Dateien

  

**CSV laden:**

  

```python

data = np.loadtxt('data.csv', delimiter=',')

print("Daten aus CSV geladen:\n", data)

```

  

**Strukturierte Daten mit fehlenden Werten:**

  

```python

structured_data = np.genfromtxt('data.csv', delimiter=',', names=True)

print("Strukturierte Daten:\n", structured_data)

```

  

**Speichern:**

  

```python

array_to_save = np.array([[1, 2], [3, 4]])

np.save('array.npy', array_to_save)

np.savetxt('array.txt', array_to_save, delimiter=',')

```

  

**Laden:**

  

```python

loaded_array = np.load('array.npy')

print("Geladenes Array:\n", loaded_array)

loaded_text_array = np.loadtxt('array.txt', delimiter=',')

print("Geladenes Text-Array:\n", loaded_text_array)

```

  
  

***

  

## 19. Broadcasting

  

```python

array1 = np.array([1, 2, 3])

array2 = np.array([[10], [20], [30]])

result = array1 + array2

print("Broadcasting Result:\n", result)

# [[11 12 13]

#  [21 22 23]

#  [31 32 33]]

```

  
  

***

  

## 20. Zufallszahlen

  

```python

random_floats = np.random.rand(3, 2)

print("Random Floats:\n", random_floats)

random_integers = np.random.randint(0, 10, size=(4,))

print("Random Integers:\n", random_integers)

normal_samples = np.random.normal(loc=0.0, scale=1.0, size=(5,))

print("Normalverteilung:\n", normal_samples)

```

  
  

***

  

## 21. Strukturierte Arrays

  

```python

dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

structured_array = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=dtype)

print("Strukturiertes Array:\n", structured_array)

print("Namen:", structured_array['name'])

print("Alter:", structured_array['age'])

```

  
  

***

  

## 22. Integration mit anderen Bibliotheken

  

**Mit Pandas:**

  

```python

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

```

  

**Mit Matplotlib:**

  

```python

import matplotlib.pyplot as plt

df.plot(x='A', y='B', kind='line')

plt.title('Liniendiagramm A vs B')

plt.show()

```

  

**Mit SciPy:**

  

```python

from scipy import stats

data = np.random.normal(loc=0, scale=1, size=1000)

z_score = stats.zscore(data)

print("Z-Scores:\n", z_score)

```

  
  

***

  

## 23. Fehlerbeseitigung – Typische Probleme und Lösungen

  

- **MemoryError:** Nutze kleinere Datentypen oder arbeite mit Daten in Teilstücken, z.B. mit `np.empty()`.

- **Dtype-Fehler:** Überprüfe array.dtype und verwende ggf. `.astype()`.

- **Import-Fehler:** Stelle sicher, dass NumPy korrekt installiert ist.

  

***

  

## 24. Exception Handling bei Array-Operationen

  

```python

import numpy as np

  

try:

    arr = np.array([1, 2, 'drei'])

    arr_sum = np.sum(arr)

except TypeError as e:

    print("TypeError aufgetreten:", e)

  

if arr.ndim != 1:

    print("Array muss eindimensional sein.")

```

  
  

***

  

## 25. Komplettes NumPy-Workflow-Beispiel

  

```python

import numpy as np

  

array_1d = np.array([1, 2, 3, 4, 5])

array_2d = np.array([[1, 2, 3], [4, 5, 6]])

  

print("1D-Array:", array_1d)

print("2D-Array:", array_2d)

  

zeros_array = np.zeros((2, 3))

ones_array = np.ones((3, 3))

arange_array = np.arange(0, 10, 2)

linspace_array = np.linspace(0, 1, 5)

  

print("Zeros Array:", zeros_array)

print("Ones Array:", ones_array)

print("Arange Array:", arange_array)

print("Linspace Array:", linspace_array)

  

addition_result = array_1d + 10

multiplication_result = array_1d * 2

  

print("Addition Result:", addition_result)

print("Multiplikation:", multiplication_result)

  

squared_array = np.square(array_1d)

print("Quadriert:", squared_array)

mean_value = np.mean(array_1d)

std_dev_value = np.std(array_1d)

print("Mittelwert:", mean_value)

print("Standardabweichung:", std_dev_value)

  

sliced_array = array_1d[1:4]

boolean_indexed_array = array_1d[array_1d > 2]

print("Sliced Array:", sliced_array)

print("Boolean Indexed Array:", boolean_indexed_array)

  

reshaped_array = array_2d.reshape(3, 2)

flattened_array = array_2d.flatten()

print("Reshaped Array (3x2):", reshaped_array)

print("Flattened Array:", flattened_array)

  

np.savetxt('array_data.txt', array_2d)

loaded_data = np.loadtxt('array_data.txt')

print("Geladen:", loaded_data)

  

try:

    invalid_operation = np.array([1, 'zwei', 3]) + np.array([4, 5])

except TypeError as e:

    print("TypeError aufgetreten:", e)

  

import pandas as pd

import matplotlib.pyplot as plt

df = pd.DataFrame(array_2d, columns=['Spalte1', 'Spalte2', 'Spalte3'])

print("DataFrame aus NumPy-Array:\n", df)

df.plot(kind='bar')

plt.title('Balkendiagramm')

plt.xlabel('Index')

plt.ylabel('Werte')

plt.show()

```

  

**Output (Beispiele):**

  

```

1D-Array: [1 2 3 4 5]

2D-Array:

 [[1 2 3]

  [4 5 6]]

Zeros Array:

 [[0. 0. 0.]

 [0. 0. 0.]]

...

Boolean Indexed Array: [3 4 5]

Reshaped Array (3x2):

 [[1 2]

  [3 4]

  [5 6]]

Flattened Array: [1 2 3 4 5 6]

...

TypeError aufgetreten: ufunc 'add' did not contain a loop with signature matching types (dtype('<U21'), dtype('int64')) -> None

DataFrame aus NumPy-Array:

   Spalte1  Spalte2  Spalte3

0        1        2        3

1        4        5        6

```

  
  

***

  

**Fazit:**

NumPy bietet schnelle, flexible und umfangreiche Funktionen für numerische Berechnung, Statistik, lineare Algebra, sowie Integration mit Pandas, Matplotlib und SciPy. Nutze diese Snippets als Referenz für deine Python-Data-Science-Projekte!

  

---
## 26. Arbeiten mit strukturierten Arrays und Record-Arrays

  

**Strukturierte Arrays** ermöglichen es, Arrays zu erstellen, die Felder mit unterschiedlichen Datentypen enthalten. Das ist besonders nützlich, wenn komplexe Datensätze (wie Zeilen aus einer Tabelle) verarbeitet werden sollen.

  

```python

# Definieren eines strukturierten Datentyps

dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

  

# Erstellen eines strukturierten Arrays

structured_array = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=dtype)

print("Strukturiertes Array:\n", structured_array)

  

# Zugriff auf einzelne Felder

print("Namen:", structured_array['name'])

print("Alter:", structured_array['age'])

```

  

**Output:**

  

```

Strukturiertes Array:

[('Alice', 25, 5.5) ('Bob', 30, 6. )]

Namen: ['Alice' 'Bob']

Alter: [25 30]

```

  
  

***

  

## 27. NumPy mit anderen Bibliotheken kombinieren

  

NumPy lässt sich hervorragend mit anderen Bibliotheken wie Pandas, Matplotlib und SciPy kombinieren.

  

**Mit Pandas für Datenmanipulation:**

Pandas nutzt NumPy-Arrays intern und stellt Datenrahmen (DataFrames) bereit, mit denen du komplexe Operationen und Analysen machen kannst.

  

```python

import pandas as pd

arr = np.array([[1, 2, 3], [4, 5, 6]])

df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

print(df)

```

  

**Output:**

  

```

   A  B  C

0  1  2  3

1  4  5  6

```

  

**Mit Matplotlib für Visualisierung:**

Matplotlib arbeitet direkt mit NumPy-Arrays und Pandas-DataFrames.

  

```python

import matplotlib.pyplot as plt

df.plot(kind='bar')

plt.title('Balkendiagramm')

plt.xlabel('Index')

plt.ylabel('Werte')

plt.show()

```

  

(Das Ergebnis ist ein Balkendiagramm.)

  

**Mit SciPy für wissenschaftliches Rechnen:**

SciPy basiert auf NumPy und erweitert es um viele weitere mathematische und naturwissenschaftliche Funktionen.

  

```python

from scipy import stats

data = np.random.normal(loc=0, scale=1, size=1000)

z_score = stats.zscore(data)

print("Z-Scores:\n", z_score[:5])

```

  

**Output (Ausschnitt):**

  

```

Z-Scores:

[-0.22987411  0.68747713  0.33761636 -0.50908815 -0.27902877]

```

  
  

***

  

## 28. Häufige Fehler und Troubleshooting in NumPy

  

Beim Arbeiten mit NumPy können verschiedene Fehler auftreten:

  

- **MemoryError:** Tritt auf, wenn zu große Arrays angelegt werden und nicht genug Arbeitsspeicher vorhanden ist.

  

**Lösung:**

    - Nutze kleinere Datentypen (`dtype='float32'` statt `float64`), verwende `np.empty()` für große, aber noch zu füllende Arrays oder verarbeite Daten in Teilen (`chunks`).

- **Dtype-Fehler:** Werden z. B. Strings und Zahlen in einem Array gemischt, kann es zu Problemen beim Rechnen kommen.

  

**Lösung:**

    - Überprüfe Datentypen mit `.dtype` und konvertiere sie bei Bedarf mit `.astype()`.

- **Import-Fehler:** Kann auftreten, wenn NumPy nicht korrekt installiert oder die Umgebung fehlerhaft ist.

  

**Lösung:**

    - Prüfe die Installation mit `pip show numpy` oder installiere NumPy mit `pip install numpy`.

  

***

  

## 29. Fehlerbehandlung (Exception Handling) bei Array-Operationen

  

Es ist ratsam, Fehler im Code abzufangen, damit das ganze Programm nicht abstürzt.

  

**Mit try/except-Blöcken:**

  

```python

try:

    arr = np.array([1, 2, 'drei'])

    arr_sum = np.sum(arr)

except TypeError as e:

    print("TypeError aufgetreten:", e)

```

  

**Vor Kontrollstrukturen prüfen:**

  

```python

if arr.ndim != 1:

    print("Array muss eindimensional sein.")

```

  

**Output:**

  

```

TypeError aufgetreten: ufunc 'add' did not contain a loop with signature matching types (dtype('<U21'), dtype('int64')) -> None

Array muss eindimensional sein.

```

  
  

***

  

## 30. Kombiniertes NumPy-Beispiel (Workflow-Snippet)

  

Im folgenden Beispiel sind die wichtigsten NumPy-Techniken und typische Fehlerbehandlung kombiniert.

  

```python

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

  

# Array-Erzeugung

array_1d = np.array([1, 2, 3, 4, 5])

array_2d = np.array([[1, 2, 3], [4, 5, 6]])

  

# Schnelle Analyse

print("Mittelwert 1D:", np.mean(array_1d))

print("Standardabweichung 2D:", np.std(array_2d))

  

# Slicing & Boolesche Filterung

print("Nur Werte > 2:", array_1d[array_1d > 2])

  

# Reshapen & Flatten

reshaped = array_2d.reshape(3, 2)

flattened = array_2d.flatten()

print("Reshaped:", reshaped)

print("Flattened:", flattened)

  

# Dateispeicherung und -einlesen

np.savetxt('array_data.txt', array_2d)

loaded = np.loadtxt('array_data.txt')

print("Geladen:", loaded)

  

# Fehler absichern

try:

    arr_invalid = np.array([1, 'zwei', 3]) + np.array([4, 5])

except TypeError as e:

    print("TypeError aufgetreten:", e)

  

# DataFrame & Plot

df = pd.DataFrame(array_2d, columns=['Spalte1', 'Spalte2', 'Spalte3'])

print("DataFrame aus NumPy-Array:\n", df)

df.plot(kind='bar')

plt.title('Balkendiagramm')

plt.xlabel('Index')

plt.ylabel('Werte')

plt.show()

```

  

**Beispiel Output:**

  

```

Mittelwert 1D: 3.0

Standardabweichung 2D: 1.707825127659933

Nur Werte > 2: [3 4 5]

Reshaped: [[1 2]

 [3 4]

 [5 6]]

Flattened: [1 2 3 4 5 6]

Geladen: [[1. 2. 3.]

 [4. 5. 6.]]

TypeError aufgetreten: ufunc 'add' did not contain a loop with signature matching types (dtype('<U21'), dtype('int64')) -> None

DataFrame aus NumPy-Array:

   Spalte1  Spalte2  Spalte3

0        1        2        3

1        4        5        6

```


# 2) **Numpy Erweitert**

## 2.1. array

  

Erstellt ein eindimensionales oder mehrdimensionales Array aus einer Liste oder einem anderen iterierbaren Objekt.

  

```python

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

```

  

**Output:**

  

```

[1 2 3 4 5]

```

  

Um z.B. eine Pandas Series zu konvertieren:

  

```python

import pandas as pd

sex = pd.Series(['Male', 'Male', 'Female'])

print(np.array(sex))

```

  

**Output:**

  

```

['Male' 'Male' 'Female']

```

  
  

***

  

## 2.2. linspace

  

Erstellt ein Array mit gleichmäßig verteilten Werten über einen Intervall.

  

```python

arr = np.linspace(10, 100, 10)

print(arr)

```

  

**Output:**

  

```

[ 10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]

```

  
  

***

  

## 2.3. arange

  

Erzeugt eine Zahlenreihe mit gegebenem Abstand (step size).

  

```python

arr = np.arange(5, 10, 2)

print(arr)

```

  

**Output:**

  

```

[5 7 9]

```

  
  

***

  

## 2.4. random.uniform

  

Erstellt Zufallswerte aus einer Gleichverteilung innerhalb eines Bereichs.

  

```python

arr = np.random.uniform(5, 10, size=4)

print(arr)

```

  

**Output (Beispiel):**

  

```

[7.72, 8.91, 5.53, 6.54]

```

  
  

***

  

## 2.5. random.randint

  

Erzeugt n Zufalls-Ganzzahlen innerhalb eines Bereichs.

  

```python

arr = np.random.randint(5, 10, 10)

print(arr)

```

  

**Output (Beispiel):**

  

```

[5, 5, 9, 6, 5, 9, 6, 7, 5, 8]

```

  
  

***

  

## 2.6. random.random

  

Generiert n Zufalls-Floatzahlen zwischen 0 und 1.

  

```python

arr = np.random.random(3)

print(arr)

```

  

**Output (Beispiel):**

  

```

[0.04, 0.39, 0.22]

```

  
  

***

  

## 2.7. logspace

  

Erzeugt gleichmäßig verteilte Zahlen auf einer logarithmischen Skala.

  

```python

arr = np.logspace(0, 10, 5, base=2)

print(arr)

```

  

**Output:**

  

```

[1.00000000e+00 5.65685425e+00 3.20000000e+01 1.81019336e+02 1.02400000e+03]

```

  
  

***

  

## 2.8. zeros

  

Erstellt ein Array, das komplett mit Nullen gefüllt ist.

  

```python

arr = np.zeros((2, 3), dtype=int)

print(arr)

```

  

**Output:**

  

```

[[0 0 0]

 [0 0 0]]

```

  

Oder eindimensional:

  

```python

print(np.zeros(5))

```

  

**Output:**

  

```

[0. 0. 0. 0. 0.]

```

  
  

***

  

## 2.9. ones

  

Erstellt ein Array, das komplett mit Einsen gefüllt ist.

  

```python

arr = np.ones((3, 4))

print(arr)

```

  

**Output:**

  

```

[[1. 1. 1. 1.]

 [1. 1. 1. 1.]

 [1. 1. 1. 1.]]

```

  
  

***

  

## 2.10. full

  

Erstellt ein Array mit beliebigem Wert.

  

```python

arr = np.full((2, 4), fill_value=2)

print(arr)

```

  

**Output:**

  

```

[[2 2 2 2]

 [2 2 2 2]]

```

  
## 2.11. eye

  

Erzeugt eine Einheitsmatrix (Identitätsmatrix) der gewünschten Größe.

  

```python

arr = np.eye(3)

print(arr)

```

  

**Output:**

  

```

[[1. 0. 0.]

 [0. 1. 0.]

 [0. 0. 1.]]

```

  
  

***

  

## 2.12. shape

  

Gibt die Form (Dimensionen) eines Arrays als Tupel zurück.

  

```python

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)

```

  

**Output:**

  

```

(2, 3)

```

  

**Beschreibung:**

Zeigt, dass das Array 2 Zeilen und 3 Spalten hat.

  

***

  

## 2.13. reshape

  

Formt ein Array in eine neue Form um, ohne den Inhalt zu verändern.

  

```python

arr = np.arange(6)

reshaped = arr.reshape((2, 3))

print(reshaped)

```

  

**Output:**

  

```

[[0 1 2]

 [3 4 5]]

```

  
  

***

  

## 2.14. ravel

  

„Flacht“ ein mehrdimensionales Array zu einem eindimensionalen Array ab.

  

```python

arr = np.array([[1, 2, 3], [4, 5, 6]])

flat = arr.ravel()

print(flat)

```

  

**Output:**

  

```

[1 2 3 4 5 6]

```

  
  

***

  

## 2.15. flatten like ravel but only copy

  

Gibt eine Kopie des Arrays als flaches Array zurück (ähnlich zu `ravel`, aber erzeugt immer eine Kopie).

  

```python

arr = np.array([[1, 2], [3, 4]])

flat = arr.flatten()

print(flat)

```

  

**Output:**

  

```

[1 2 3 4]

```

  
  

***

  

## 2.16. transpose / Transponieren

  

Vertauscht Zeilen und Spalten eines Arrays (Matrix-Transponierung).

  

```python

arr = np.array([[1, 2], [3, 4], [5, 6]])

print(arr.transpose())

```

  

**Output:**

  

```

[[1 3 5]

 [2 4 6]]

```

  

Oder alternativ:

  

```python

print(arr.T)

```

  
  

***

  

## 2.17. expand dim (Dimensionen hinzufügen)

  

Erweitert ein Array um eine neue Achse, z. B. für Batch-Bildung in ML-Projekten.

  

```python

arr = np.array([1, 2, 3])

expanded = np.expand_dims(arr, axis=0)

print(expanded)

```

  

**Output:**

  

```

[[1 2 3]]

```

  
  

***

  

## 2.18. squeeze (Dimensionen entfernen)

  

Entfernt Dimensionen mit Länge 1 (nützlich beim Zurückführen von Modeloutputs).

  

```python

arr = np.array([[[1, 2, 3]]])

squeezed = np.squeeze(arr)

print(squeezed)

```

  

**Output:**

  

```

[1 2 3]

```

  
  

***

  

## 2.19. concatenate

  

Fügt mehrere Arrays entlang einer bestimmten Achse zusammen.

  

```python

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6]])

concat = np.concatenate((arr1, arr2), axis=0)

print(concat)

```

  

**Output:**

  

```

[[1 2]

 [3 4]

 [5 6]]

```

  
  

***

  

## 2.20. hstack

  

Fügt mehrere Arrays horizontal (entlang der Spalten) zusammen.

  

```python

arr1 = np.array([1, 2])

arr2 = np.array([3, 4])

hs = np.hstack((arr1, arr2))

print(hs)

```

  

**Output:**

  

```

[1 2 3 4]

```

  

Oder mit 2D:

  

```python

arr1 = np.array([[1, 2]])

arr2 = np.array([[3, 4]])

hs = np.hstack((arr1, arr2))

print(hs)

```

  

**Output:**

  

```

[[1 2 3 4]]

```

## 2.21. vstack

  

Fügt mehrere Arrays vertikal (untereinander) zusammen.

  

```python

arr1 = np.array([1, 2])

arr2 = np.array([3, 4])

vs = np.vstack((arr1, arr2))

print(vs)

```

  

**Output:**

  

```

[[1 2]

 [3 4]]

```

  
  

***

  

## 2.22. split

  

Teilt ein Array in mehrere Teil-Arrays.

  

```python

arr = np.array([1, 2, 3, 4, 5, 6])

splits = np.split(arr, 3)

print(splits)

```

  

**Output:**

  

```

[array([1, 2]), array([3, 4]), array([5, 6])]

```

  
  

***

  

## 2.23. hsplit

  

Teilt ein Array horizontal (entlang der Spalten).

  

```python

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

hsplits = np.hsplit(arr, 2)

print(hsplits)

```

  

**Output:**

  

```

[array([[1, 2],

       [5, 6]]), array([[3, 4],

       [7, 8]])]

```

  
  

***

  

## 2.24. vsplit

  

Teilt ein Array vertikal (entlang der Zeilen).

  

```python

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

vsplits = np.vsplit(arr, 2)

print(vsplits)

```

  

**Output:**

  

```

[array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]

```

  
  

***

  

## 2.25. unique

  

Gibt die eindeutigen Werte in einem Array zurück.

  

```python

arr = np.array([1, 2, 2, 3, 1, 4])

uniq = np.unique(arr)

print(uniq)

```

  

**Output:**

  

```

[1 2 3 4]

```

  
  

***

  

## 2.26. sort ascendend

  

Sortiert ein Array aufsteigend.

  

```python

arr = np.array([5, 2, 7, 1])

sortiert = np.sort(arr)

print(sortiert)

```

  

**Output:**

  

```

[1 2 5 7]

```

  
  

***

  

## 2.27. argsort

  

Gibt die Indizes zurück, die das sortierte Array ergeben würden.

  

```python

arr = np.array([50, 10, 20])

idx = np.argsort(arr)

print(idx)

```

  

**Output:**

  

```

[1 2 0]

```

  

**Beschreibung:**

Index 1 enthält das kleinste Element, Index 0 das größte.

  

***

  

## 2.28. argmax

  

Gibt den Index des maximalen Werts eines Arrays zurück.

  

```python

arr = np.array([1, 5, 8, 2])

max_index = np.argmax(arr)

print(max_index)

```

  

**Output:**

  

```

2

```

  

**Beschreibung:**

Index 2 (zugehöriger Wert: 8) ist das Maximum im Array.

  

***

  

## 2.29. argmin

  

Gibt den Index des minimalen Werts eines Arrays zurück.

  

```python

arr = np.array([1, 5, -2, 2])

min_index = np.argmin(arr)

print(min_index)

```

  

**Output:**

  

```

2

```

  

**Beschreibung:**

Index 2 (zugehöriger Wert: -2) ist das Minimum im Array.

  

***

  

## 2.30. where + Bedingung

  

Ermittelt die Indizes, an denen eine Bedingung erfüllt ist.

  

```python

arr = np.array([1, 2, 3, 2, 5])

indices = np.where(arr == 2)

print(indices)

```

  

**Output:**

  

```

(array([1, 3]),)

```

  

**Beschreibung:**

An den Indizes 1 und 3 steht im Array der Wert 2.

## 2.31. nonzero

  

Gibt die Indizes aller nicht-null (d.h. von 0 verschiedenen) Elemente eines Arrays zurück.

  

```python

arr = np.array([0, 2, 0, 5, 0, 3])

index = np.nonzero(arr)

print(index)

```

  

**Output:**

  

```

(array([1, 3, 5]),)

```

  

**Beschreibung:**

An den Stellen 1, 3 und 5 stehen Werte ungleich null.

  

***

  

## 2.32. count_nonzero

  

Zählt die Anzahl nicht-null Werte im Array.

  

```python

arr = np.array([0, 1, 2, 0, 4, 0, 8])

anzahl = np.count_nonzero(arr)

print(anzahl)

```

  

**Output:**

  

```

4

```

  

**Beschreibung:**

Vier Werte sind ungleich null.

  

***

  

## 2.33. clip/cut max/min Array

  

Schneidet die Werte eines Arrays auf einen vorgegebenen Minimal- bzw. Maximalwert.

  

```python

arr = np.array([1, 3, 7, 9, 12])

geclippt = np.clip(arr, 3, 10)

print(geclippt)

```

  

**Output:**

  

```

[ 3  3  7  9 10]

```

  

**Beschreibung:**

Alle Werte kleiner als 3 werden auf 3 gesetzt, größer als 10 auf 10.

  

***

  

## 2.34. sum Array

  

Berechnet die Summe aller Elemente im Array (optional: über eine Achse).

  

```python

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(arr))

print(np.sum(arr, axis=0))

print(np.sum(arr, axis=1))

```

  

**Output:**

  

```

21

[5 7 9]

[ 6 15]

```

  

**Beschreibung:**

Die Gesamtsumme ist 21. Aus der Sicht der Achsen: Zeilensummen , Spaltensummen .

  

***

  

## 2.35. cumulative sum

  

Berechnet die kumulierte Summe (aufaddierende Summe).

  

```python

arr = np.array([1, 2, 3])

cums = np.cumsum(arr)

print(cums)

```

  

**Output:**

  

```

[1 3 6]

```

  

**Beschreibung:**

1, dann 1+2=3, dann 1+2+3=6.

```Python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
arr[:,:].cumsum(axis=0) # Kumlierung spaltenweise
```
Output: 



```Python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
arr[:,:].cumsum(axis=0) # Kumlierung zeilenweise
```
***

  

## 2.36. product Array

  

Berechnet das Produkt aller Array-Elemente.

  

```python

arr = np.array([1, 2, 3, 4])

prod = np.prod(arr)

print(prod)

```

  

**Output:**

  

```

24

```

  

**Beschreibung:**

1 * 2 * 3 * 4 = 24.

  

***

  

## 2.37. cumulative product

  

Kumuliertes Produkt der Array-Elemente.

  

```python

arr = np.array([2, 3, 4])

cumprod = np.cumprod(arr)

print(cumprod)

```

  

**Output:**

  

```

[ 2  6 24]

```

  

**Beschreibung:**

2, 2*3=6, 2*3*4=24.

  

***

  

## 2.38. mean

  

Berechnet den Mittelwert der Werte im Array.

  

```python

arr = np.array([2, 4, 6, 8])

mw = np.mean(arr)

print(mw)

```

  

**Output:**

  

```

5.0

```

  
  

***

  

## 2.39. median

  

Gibt den Median des Arrays zurück (Zentralwert).

  

```python

arr = np.array([1, 3, 2, 5, 4])

med = np.median(arr)

print(med)

```

  

**Output:**

  

```

3.0

```

  

**Beschreibung:**

Die mittlere Zahl nach Sortierung ist 3.

  

***

  

## 2.40. standard deviation

  

Gibt die Standardabweichung des Arrays zurück.

  

```python

arr = np.array([1, 2, 3, 4, 5])

sdev = np.std(arr)

print(sdev)

```

  

**Output:**

  

```

1.4142135623730951

```

  

**Beschreibung:**

Maß für Streuung der Werte um den Mittelwert.

## 2.41. variance

  

Berechnet die Varianz eines Arrays; ein Maß für die Streuung.

  

```python

arr = np.array([1, 2, 3, 4, 5])

varianz = np.var(arr)

print(varianz)

```

  

**Output:**

  

```

2.0

```

  
  

***

  

## 2.42. percentile

  

Liefert den Wert, der einem bestimmten Perzentil entspricht.

  

```python

arr = np.array([1, 2, 3, 4, 5])

p90 = np.percentile(arr, 90)

print(p90)

```

  

**Output:**

  

```

4.6

```

  

**Beschreibung:**

90 % der Werte liegen unter 4.6.

  

***

  

## 2.43. corrcoef

  

Liefert die Korrelationsmatrix zweier Arrays.

  

```python

x = np.array([1, 2, 3, 4])

y = np.array([5, 6, 7, 8])

corr_matrix = np.corrcoef(x, y)

print(corr_matrix)

```

  

**Output:**

  

```

[[1. 1.]

 [1. 1.]]

```

  

**Beschreibung:**

Perfekte Korrelation zwischen x und y.

  

***

  

## 2.44. covariance

  

Berechnet die Kovarianzmatrix zweier Arrays.

  

```python

x = np.array([1, 2, 3, 4])

y = np.array([5, 6, 7, 8])

cov_matrix = np.cov(x, y)

print(cov_matrix)

```

  

**Output:**

  

```

[[1.66666667 1.66666667]

 [1.66666667 1.66666667]]

```

  
  

***

  

## 2.45. Skalarprodukt (dot)

  

Matrixprodukt zweier Arrays (Skalarprodukt).

  

```python

a = np.array([1, 2])

b = np.array([3, 4])

produkt = np.dot(a, b)

print(produkt)

```

  

**Output:**

  

```

11

```

  

**Beschreibung:**

1*3 + 2*4 = 3 + 8 = 11

  

***

  

## 2.46. matmul

  

Matrixmultiplikation (auch für mehrdimensionale Arrays).

  

```python

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

C = np.matmul(A, B)

print(C)

```

  

**Output:**

  

```

[[19 22]

 [43 50]]

```

  
  

***

  

## 2.47. outer

  

Berechnet das äußere Produkt zweier Vektoren.

  

```python

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

outer = np.outer(a, b)

print(outer)

```

  

**Output:**

  

```

[[ 4  5  6]

 [ 8 10 12]

 [12 15 18]]

```

  
  

***

  

## 2.48. diag

  

Extrahiert die Diagonale einer Matrix oder erstellt eine Diagonalmatrix aus einem Vektor.

  

```python

arr = np.array([[1, 2], [3, 4]])

d = np.diag(arr)

print(d)

```

  

**Output:**

  

```

[1 4]

```

  

Oder:

  

```python

vec = np.array([1, 2, 3])

dmatrix = np.diag(vec)

print(dmatrix)

```

  

**Output:**

  

```

[[1 0 0]

 [0 2 0]

 [0 0 3]]

```

  
  

***

  

## 2.49. trace Matrix (Summe der Hauptdiagonale)

  

Berechnet die Spur einer Matrix (Summe der Hauptdiagonale).

  

```python

arr = np.array([[1, 2], [3, 4]])

spur = np.trace(arr)

print(spur)

```

  

**Output:**

  

```

5

```

  

**Beschreibung:**

1 + 4 = 5

  

***

  

## 2.50. linalg.inv

  

Berechnet die Inverse einer quadratischen Matrix (sofern invertierbar).

  

```python

arr = np.array([[4, 7], [2, 6]])

inverse = np.linalg.inv(arr)

print(inverse)

```

  

**Output:**

  

```

[[ 0.6 -0.7]

 [-0.2  0.4]]

```
# 3) **Imports/Options**

### 3.1) Pakete

```Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fast')
plt.style.available
# pd.options.display.float_format='{:.4f}'.format
# pd.set_option('display.max_rows', 10)
```

## 3.2) Matplotlib

Imports
```Python
import matplotlib.pyplot as plt
```

Verfügbare Stile abfragen
```Python
plt.style.available
```

Stil nutzen
```Python
plt.style.use()
```
### Stileliste:
 ```
'Solarize_Light2'
 ```
 ```
'_classic_test_patch',
 ```
``` 
'_mpl-gallery'
``` 
```
'_mpl-gallery-nogrid'
```
```
'bmh'
```
```
'classic'
```
```
'dark_background'
```
```
'fast'
```
```
'fivethirtyeight'
```
```
'ggplot'
```
```
'grayscale'
```
```
'petroff10'
```
```
'seaborn-v0_8'
```
```
'seaborn-v0_8-bright'
```
```
'seaborn-v0_8-colorblind'
```
```
'seaborn-v0_8-dark'
```
```
'seaborn-v0_8-dark-palette'
```
```
'seaborn-v0_8-darkgrid'
```
```
'seaborn-v0_8-deep'
```
```
'seaborn-v0_8-muted'
```
```
'seaborn-v0_8-notebook'
```
```
'seaborn-v0_8-paper'
```
```
'seaborn-v0_8-pastel'
```
```
'seaborn-v0_8-poster'
```
```
'seaborn-v0_8-talk'
```
```
'seaborn-v0_8-ticks'
```
```
'seaborn-v0_8-white'
```
```
'seaborn-v0_8-whitegrid'
```
```
'tableau-colorblind10'
```

Stil benutzen
```kopieren
plt.style.use('  ')
```
## 3.3) Pandas
```Python
import pandas as pd
```

## 3.4) Numpy
```Python
import numpy as np
```


