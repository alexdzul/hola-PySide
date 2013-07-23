'''
Created on 27/06/2013

@author: alex
'''
import sys
import PySide
from PySide.QtCore import *
from PySide.QtGui import *


app = QApplication(sys.argv)

class main(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(400,185)
        self.setWindowTitle('Mi Primer Programa')
        self.lbl_nombre = QLabel('Tu nombre:',self)
        self.lbl_nombre.move(10,10)
        self.txt_nombre = QLineEdit(self)
        self.txt_nombre.setMinimumWidth(285)
        self.txt_nombre.move(100,10)
        self.lbl_saludo = QLabel('Esperando para saludarte....',self)
        self.lbl_saludo.move(200,100)
        self.btn_saludar = QPushButton('Saludar',self)
        self.btn_saludar.setMinimumWidth(145)
        self.btn_saludar.move(250,150)
        self.btn_saludar.clicked.connect(self.clicked_btn_saludar)
    
    def clicked_btn_saludar(self):
        saludo = 'Hola %s!!'%self.txt_nombre.text()
        self.lbl_saludo.setText(saludo)
    
    def run(self):
        self.show()
        app.exec_()

app_main = main()
app_main.run()