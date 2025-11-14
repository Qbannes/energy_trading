# Bibliothek.py

import BuchObjekt from Buch


class BibliothekVerwaltung:
    """Verwaltet eine Sammlung von Büchern."""

    def __init__(self):
        self.buecher_liste = []

    def buch_hinzufuegen(self, titel, autor):
        buch = BuchObjekt(titel, autor)
        self.buecher_liste.append(buch)

    def buecher_auflisten(self):
        return [str(buch) for buch in self.buecher_liste]
