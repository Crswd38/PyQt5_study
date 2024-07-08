import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('push me!', self)
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.resize(500,500)
        self.setWindowTitle("두 번째 시간")
        self.show()

    def closeEvent(self, QCloseEvent): # 종료 알림 메시지
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No) # yes|no|강조:no
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())