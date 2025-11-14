""" Modul zum Test von PyLint
"""

class Auto:
    """ Einfache Klasse. """

    marke="VW"
    preis = 99.99

    def daten_ausgeben(self):
        """ Funktion zur Ausgabe von Daten. """

        print(self.marke)
        print(self.preis) 

mein_auto = Auto()
mein_auto.daten_ausgeben()
