import sys
from PyQt5.QtWidgets import *

class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('asdcvb', self) # 버튼 생성
        btn.resize(btn.sizeHint())
        btn.setToolTip('툴팁입니다.<b>안녕하세요.<b/>') # 버튼 툴팁
        btn.move(20,30) # 버튼 위치

        self.setGeometry(300,300,400,500) # 창 크기, 창 위치
        self.setWindowTitle("첫 번쨰 시간") # 창 제목
        self.show() # 창 띄우기

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())