from PyQt6.QtWidgets import *
from project1 import *


class Menu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button = self.findChild(QPushButton, "shopbtn")
        self.shopbtn.clicked.connect(lambda: self.cart())
        self.submitbtn.clicked.connect(lambda: self.submit())
        self.exitbtn.clicked.connect(lambda: self.exit())

    def cart(self):
        self.lineEdit.setGeometry(QtCore.QRect(280, 160, 111, 21))
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 190, 111, 21))
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 220, 111, 21))
        self.label_2.setText('Cookie - $1.50')
        self.label_3.setText('Sandwich - $4.00')
        self.label_4.setText('Water - $1.00')
        self.label_3.setGeometry(QtCore.QRect(140, 160, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_2.setGeometry(QtCore.QRect(140, 190, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_4.setGeometry(QtCore.QRect(140, 220, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.submitbtn.setText("submit")
        self.submitbtn.setGeometry(QtCore.QRect(220, 270, 113, 32))
        self.submitbtn.setObjectName("submitbtn")

    def submit(self):
        try:
            cookie = int(self.lineEdit_2.text())
            if cookie < 0 or cookie == '':
                myError = ValueError()
                raise myError
            elif cookie == 1:
                self.label_5.setText(f'{cookie} Cookie added')
            else:
                self.label_5.setText(f'{cookie} Cookies added')

            sandwich = int(self.lineEdit.text())
            if sandwich < 0 or sandwich == '':
                myError = ValueError()
                raise myError
            elif sandwich == 1:
                self.label.setText(f'{sandwich} Sandwich added')
            else:
                self.label.setText(f'{sandwich} Sandwiches added')

            water = int(self.lineEdit_3.text())
            if water < 0 or water == '':
                myError = ValueError()
                raise myError
            elif water == 1:
                self.label_6.setText(f'{water} Water added')
            else:
                self.label_6.setText(f'{water} Waters added')

            self.label_2.clear()
            self.label_3.clear()
            self.label_4.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.submitbtn.setGeometry(QtCore.QRect(0, 0, 0, 0))

            c = float(1.50)
            s = float(4.00)
            w = float(1.00)
            cook_count = c * cookie
            sand_count = s * sandwich
            water_count = w * water
            total = cook_count + water_count + sand_count
            self.label_7.setText(f'FINAL TOTAL: ${total:.2f}')

        except:
            self.label.setText("Need to enter 0 or a")
            self.label_5.setText("positive numeric number")
            self.label_6.setText('in every box')

    def exit(self):
        self.close()


