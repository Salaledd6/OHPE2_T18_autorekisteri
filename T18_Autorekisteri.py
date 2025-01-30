# pip install PySide6
import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QPixmap

class Rekisteri(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rekisteri = dict() # {}
        self.alusta_UI()
        
    def alusta_UI(self):
        self.setGeometry(100,100,240,210)
        self.setWindowTitle("Rekisteri")

        self.e1 = QLabel("Rek.nro", self)
        self.e1.setGeometry(10,30,50,20)
        self.tk1 = QLineEdit(self)
        self.tk1.setGeometry(80,30,80,20)

        self.e2 = QLabel("Merkki", self)
        self.e2.setGeometry(10,60,50,20)
        self.tk2 = QLineEdit(self)
        self.tk2.setGeometry(80,60,80,20)

        self.e3 = QLabel("Vuosi", self)
        self.e3.setGeometry(10,90,50,20)
        self.tk3 = QLineEdit(self)
        self.tk3.setGeometry(80,90,80,20)

        self.painike = QPushButton("Lisää", self)
        self.painike.setGeometry(10,130,150,30)
        self.painike.clicked.connect(self.lisaa_tiedot)

        self.painike2 = QPushButton("Hae", self)
        self.painike2.setGeometry(10,170,150,30)
        self.painike2.clicked.connect(self.hae_tiedot)

    def lisaa_tiedot(self):
        rek_nro = self.tk1.text()
        merkki = self.tk2.text()
        vuosi = self.tk3.text()
        # {"rek.nro" : {"merkki":"Volvo", "vuosi":"2019"}}
        self.rekisteri[rek_nro] = {"merkki":merkki, "vuosi":vuosi}

        self.tk1.clear()
        self.tk2.clear()
        self.tk3.clear()


    def hae_tiedot(self):
        rek_nro = self.tk1.text()
        auto = self.rekisteri[rek_nro] # auto = {"merkki":"Volvo", "vuosi":"2019"}
        self.tk2.setText(auto["merkki"])
        self.tk3.setText(auto["vuosi"])


def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Rekisteri() # olio luokasta Rekisteri, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()