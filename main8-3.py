import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        redb = QPushButton("Red", self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked.connect(self.setColor)

        greenb = QPushButton(self)
        greenb.setStyleSheet("QWidget { background-color: %s }")
        greenb.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("color Dialog")
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
