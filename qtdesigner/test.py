import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('mainwindow.ui') # 여기에 ui파일명 입력
form_class = uic.loadUiType(form)[0]

form_second = resource_path('secondwindow.ui')
form_secondwindow = uic.loadUiType(form_second)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btn_main_to_second(self):
        self.hide()
        self.second = secondwindow()
        self.second.exec()
        self.show()

class secondwindow(QWidget, form_secondwindow):
    def __init__(self):
        super(secondwindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
