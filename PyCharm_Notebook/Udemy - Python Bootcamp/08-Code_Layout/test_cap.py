import unittest
import cap


class TestCap(unittest.TestCase):
    """ Klasse zum testen der Funktion cap_text im Modul cap. """    
    
    def test_ein_wort(self):
        """ Teste mit einem einzelnen Wort im Eingabestring. """
        
        text = 'python'
        ergebnis = cap.cap_text(text)
        self.assertEqual(ergebnis, 'Python')
        
    def test_mehrere_woerter(self):
        """ Teste mit mehreren Woertern im Eingabestring. """
        
        text = 'monty python'
        ergebnis = cap.cap_text(text)
        self.assertEqual(ergebnis, 'Monty Python')
        
    def test_mit_apostroph(self):
        """ Teste mit mehreren Woertern und Apostroph im Eingabestring. """
        
        text = "monty python's flying circus"
        ergebnis = cap.cap_text(text)
        self.assertEqual(ergebnis, "Monty Python's Flying Circus")
        
if __name__ == '__main__':
    unittest.main()
