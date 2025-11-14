#!/usr/bin/env python3
import locale, platform
if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'german')
elif platform.system() == 'Linux':
    locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')
else:
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
    
s = input('Länge des Rechtecks: ')
laenge = locale.atof(s)
s = input('Breite des Rechtecks: ')
breite = locale.atof(s)
flaeche = laenge * breite
s = locale.format_string('%.2f', flaeche)
print('Flächeninhalt: ', s)
