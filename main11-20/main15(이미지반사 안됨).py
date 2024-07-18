import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.createReflectedImage()
    
    def initUI(self):
        self.img = QImage("C:\\Users\\82104\\Downloads\\다운로드.png")
        if self.img.isNull():
            print("Error loading Image")
            sys.exit(1)
        self.iw = self.img.width()
        self.ih = self.img.height()

        self.setGeometry(200, 200, 250, 450)
        self.setWindowTitle("Reflection")

        self.show()

    def createReflectedImage(self):
        self.refImage = QImage(self.iw, self.ih, QImage.Format_ARGB32)

        painter = QPainter()
        painter.begin(self.refImage)
        painter.drawImage(0, 0, self.img)
        painter.begin(self.refImage)
        painter.drawImage(0, 0, self.img)

        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)

        gradient = QLinearGradient(self.iw/2, 0, self.iw/2, self.ih)

        gradient.setColorAt(1, QColor(0, 0, 0))
        gradient.setColorAt(0, Qt.transparent)

        painter.fillRect(0, 0, self.iw, self.ih, gradient)

        painter.end()
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        painter.drawImage(25, 15, self.img)
        painter.translate(0, 2*self.ih + 15)
        painter.scale(1, -1)
        painter.drawImage(25, 0, self.refImage)

app = QApplication([])
ex = Example()
sys.exit(app.exec_())