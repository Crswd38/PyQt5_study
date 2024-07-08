import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)
        cb = QCheckBox("Show title", self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("QCheckBox")
        self.show()

    def changeTitle(self, state):
        if state:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle(" ")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())