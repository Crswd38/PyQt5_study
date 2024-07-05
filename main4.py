import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Exam(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요.")

        menu = self.menuBar() # 메뉴 생성
        menu_file = menu.addMenu('File') # 그룹 생성
        menu_edit = menu.addMenu('Edit') # 그룹 생성
        menu_view = menu.addMenu('View') # 그룹 생성

        file_exit = QAction('Exit', self) # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 영원히 빠이빠이")
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction("파이썬 파일", self)
        view_stat = QAction("상태표시줄", self, checkable=True)
        view_stat.setCheckable(True)

        file_exit.triggered.connect(QCoreApplication.instance().quit)
        view_stat.triggered.connect(self.tglStat)

        file_new = QMenu('New', self) # 서브 그룹

        file_new.addAction(new_txt) # 서브 메뉴 추가
        file_new.addAction(new_py)

        menu_file.addMenu(file_new) # 메뉴 등록
        menu_file.addAction(file_exit) # 메뉴 등록
        menu_view.addAction(view_stat)

        self.resize(450, 400)
        self.show()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)
        quit = cm.addAction("quit")
        action = cm.__reduce_ex__(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            qApp.quit()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())