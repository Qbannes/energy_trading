#!/usr/bin/env python3
# Wenn Sie das Beispiel ausprobieren möchten, müssen Sie vorher
# pandas und matplotlib installieren:
#
# pip install matplotlib pandas                       # Windows
# pip3 install matplotlib pandas                      # macOS
# sudo apt update                                     # Debian, Ubuntu
# sudo apt install python3-matplotlib python3-pandas
# sudo dnf install python3-matplotlib python3-pandas  # Fedora, RHEL

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Datei aus dem gleichen Verzeichnis lesen, in dem sich 
# dieses Programm gespeichert ist
srcpath = Path(__file__).parent.absolute()
fname = srcpath.joinpath('umsatz.csv')
df = pd.read_csv(fname, delimiter=';')

# Die letzten vier Jahre auswählen
last_four_years = df.tail(4)

# Diagrammgröße festlegen
plt.figure(figsize=(10, 10))

# Schleife über die letzten vier Jahre
for i, (index, year_data) in \
      enumerate(last_four_years.iterrows(), 1):
    # Daten für das Diagramm extrahieren
    cities = year_data.index[1:]
    values = year_data.values[1:]
    year = year_data.values[0]

    # Diagramm erstellen
    plt.subplot(2, 2, i)
    plt.pie(values, labels=cities, autopct='%1.1f%%')
    # plt.title(f'Umsatzverteilung {index}')  # ChatGPT
    plt.title(f'Umsatz {year}')               # verbessert

# Diagramme anzeigen
plt.tight_layout()
plt.show()
