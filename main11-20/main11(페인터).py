import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.a = "쉽고 재밌는 것"

        self.setGeometry(300, 300, 500, 450)
        self.setWindowTitle("Drawing text")
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # self.drawText(event, qp)
        # self.drawPoints(qp)
        # self.drawRectangles(qp)
        # self.drawLines(qp)
        self.drawBrushes(qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('gulim', 10))
        qp.drawText(event.rect(), Qt.AlignHCenter, self.a)

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(0, size.width())
            y = random.randint(0, size.height())
            qp.drawPoint(x, y)

    def drawRectangles(self, qp):
        col = QColor()
        col.setNamedColor('#521E80')
        qp.setPen(col)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 45, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 45, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 45, 90, 60)

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        
        qp.setPen(pen)
        qp.drawLine(20, 100, 250, 100)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 140, 250, 140)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 180, 250, 180)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 220, 250, 220)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 260, 250, 260)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 300, 250, 300)

    def drawBrushes(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.diagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerpaPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
    