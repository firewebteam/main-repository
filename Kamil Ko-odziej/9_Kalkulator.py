from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtWidgets import QMessageBox


class Okienko(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        etl = QLabel('Wpisz liczby:', self)
        et2 = QLabel('Pierwsza liczba:', self)
        et3 = QLabel('Druga liczba:', self)
        et4 = QLabel('Wynik:', self)
        #et5 = QLabel('', self)

        uklad = QGridLayout()
        uklad.addWidget(etl, 0, 0)
        uklad.addWidget(et2, 0, 1)
        uklad.addWidget(et3, 0, 2)
        uklad.addWidget(et4, 0, 3)
        #uklad.addWidget(et5, 1, 1)

        self.edt1 = QLineEdit()
        uklad.addWidget(self.edt1, 1, 1)

        self.edt2 = QLineEdit()
        uklad.addWidget(self.edt2, 1, 2)

        self.edt3 = QLineEdit()
        uklad.addWidget(self.edt3, 1, 3)
        self.edt3.readonly = True

        butt1 = QPushButton('-', self)
        uklad.addWidget(butt1, 4, 3)

        #butt2 = QPushButton('%11', self)
        #uklad.addWidget(butt2, 1, 1)

        butt3 = QPushButton('+', self)
        uklad.addWidget(butt3, 5, 3)

        butt4 = QPushButton('*', self)
        uklad.addWidget(butt4, 3, 3)

        butt5 = QPushButton('/', self)
        uklad.addWidget(butt5, 2, 3)

        butt6 = QPushButton('^2', self)
        uklad.addWidget(butt6, 2, 2)

        self.setLayout(uklad)

        butt1.clicked.connect(self.dzialanie)
        #butt2.clicked.connect(self.dzialanie)
        butt3.clicked.connect(self.dzialanie)
        butt4.clicked.connect(self.dzialanie)
        butt5.clicked.connect(self.dzialanie)
        butt6.clicked.connect(self.dzialanie)
        #butt7.clicked.connect(self.dzialanie)

        self.setGeometry(1000, 250, 500, 150)
        self.setWindowTitle('Kalkulator')
        self.show()

    def dzialanie(self):

        nadawca = self.sender()

        try:
            liczba1 = float(self.edt1.text())
            liczba2 = float(self.edt2.text())
            wynik = ''

            if nadawca.text() == '-':
                wynik = liczba1 - liczba2

            elif nadawca.text() == '+':
                wynik = liczba1 + liczba2

            elif nadawca.text() == '/':
                wynik = liczba1 / liczba2

            elif nadawca.text() == '*':
                wynik = liczba1 * liczba2

            elif nadawca.text() == '^2':
                wynik = liczba1 ** 2

            self.edt3.setText(str(wynik))
        except ValueError:
            QMessageBox.warning(self, 'Błąd', 'Błąd danych!', QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Okienko()

    sys.exit(app.exec_())
