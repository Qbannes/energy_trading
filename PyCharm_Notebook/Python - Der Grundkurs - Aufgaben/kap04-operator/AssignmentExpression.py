#!/usr/bin/env python3

# Textdatei auslesen, Variante 1 ohne Assignment Expression
with open('readme.txt', 'rt') as txtfile:
    line = txtfile.readline()
    while line:
        print(line, end='')
        line = txtfile.readline()  # nächste Zeile lesen
        
# Textdatei auslesen, Variante 2 mit Assignment Expression 
# erfordert Python 3.8 oder neuer
with open('readme.txt', 'rt') as txtfile:
    while line := txtfile.readline():
        print(line, end='')
        
