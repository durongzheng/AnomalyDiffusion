import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QAction

class AnomalyDiffusion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&F文件')

        open_act = QAction('&O打开', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.openImg)
        fileMenu.addAction(open_act)

        exit_act = QAction('&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(QApplication.instance().quit)
        fileMenu.addAction(exit_act)

        self.resize(1080,800)
        self.move(0,0)
        self.setWindowTitle('缺陷扩散')

    def openImg(self):
        pass

def main():
    app = QApplication(sys.argv)
    win = AnomalyDiffusion()
    win.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()