# Buch.py

class BuchObjekt:
    """Repräsentiert ein Buch mit Titel und Autor"""

    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor

    def __str__(self):
        return f'"{self.titel}" von {self.autor}'
