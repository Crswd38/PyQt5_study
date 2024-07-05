import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = f"x: {x}, y: {y}"

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Event object")
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = f"x: {x}, y: {y}"
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())