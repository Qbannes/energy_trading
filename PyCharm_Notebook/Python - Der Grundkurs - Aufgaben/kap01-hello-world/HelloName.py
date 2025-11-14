#!/usr/bin/env python3
import time, locale
name = input('Geben Sie Ihren Namen an: ')
print('Hallo %s!' % name)
# Datum und Zeit in deutscher Lokalisierung ausgeben
locale.setlocale(locale.LC_ALL, 'de_DE')   # für macOS + Linux
# locale.setlocale(locale.LC_ALL, 'german')  # für Windows
time = time.strftime('Heute ist %A der %d. %B.')
print(time)
