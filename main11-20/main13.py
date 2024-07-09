import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sid = QImage("")

        btn = QPushButton("이미지 변경", self)
        btn.resize(btn.sizeHint())
        btn.move(20, 150)
        btn.clicked.connect(self.openFileNameDialog)

        self.setGeometry(1400, 250, 320, 200)
        self.show()

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "불러올 이미지를 선택하세요.", "",
                                                  "All Files (*);;Python Files (*.py)")
        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(120, 120)


app = QApplication([])
ex = Example()
sys.exit(app.exec_())
