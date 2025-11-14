#!/usr/bin/env python3
import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget
from PyQt6.QtCore import QSize, Qt    

class MyWindow(QMainWindow):
    def __init__(self):
        # Konstruktor von QMainWindow aufrufen
        super().__init__()

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(300, 100))    
        self.setWindowTitle('Hello, Qt!') 

        # Title-Widget erzeugen und in Fenster einbetten
        title = QLabel('Hello, Qt!', self) 
        title.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.setCentralWidget(title)

# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec())
