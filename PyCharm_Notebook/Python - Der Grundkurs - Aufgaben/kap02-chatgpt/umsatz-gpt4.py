#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Deine CSV-Daten als String
csv_data = """
;Paris;London;Berlin;Wien;Prag;Rom
2018;88000;52000;110000;86000;29000;72000
2019;90000;53000;115000;87000;30000;74000
2020;95000;54000;117000;85000;31000;75000
2021;98000;55000;119000;83000;32000;76000
2022;103000;53000;120000;82000;35000;45000
2023;107000;54000;120000;55000;40000;45000
2024;109000;54000;121000;54000;48000;46000
"""

# CSV-Daten in einen DataFrame umwandeln
df = pd.read_csv(StringIO(csv_data), sep=';', index_col=0)

# Die letzten vier Jahre auswählen
df_last_4_years = df.tail(4)

# Ein 2x2 Raster von Tortendiagrammen erstellen
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.flatten()  # Flache Liste der Axes für einfacheren Zugriff

for i, (year, row) in enumerate(df_last_4_years.iterrows()):
    axs[i].pie(row, labels=row.index, autopct='%1.1f%%', startangle=140)
    axs[i].set_title(f'Umsatz {year}')

plt.tight_layout()
plt.show()
