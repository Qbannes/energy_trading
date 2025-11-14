# Main.py

from Bibliothek import BibliothekVerwaltung


def main():
    meine_bibliothek = BibliothekVerwaltung()
    # Bücher hinzufügen
    meine_bibliothek.buch_hinzufuegen("Der Prozess", "Franz Kafka")
    meine_bibliothek.buch_hinzufuegen("Faust", "Johann Wolfgang von Goethe")
    meine_bibliothek.buch_hinzufuegen("Effi Briest", "Theodor Fontane")

    # Bücher ausgeben
    print("Bücher in der Bibliothek:")
    for buch_str in meine_bibliothek.buecher_auflisten():
        print(f"- {buch_str}")


if __name__ == "__main__":
    main()
