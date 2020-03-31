import sys
# pyuic5 AddMusic.ui -o AddMusic.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from AddMusic import AddMusic
from Table import Table
from PyQt5 import QtGui



class Application(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("YourMusic")
        self.setGeometry(700, 500, 400, 500)
        self.setWindowIcon(QIcon("icon.png"))
        self.buttonAddMusic = QPushButton("Добавить музыку", self)
        self.buttonAddMusic.setGeometry(75, 55, 250, 150)
        self.buttonAddMusic.clicked.connect(self.buttonClickedAddMusic)
        self.buttonMusicList = QPushButton("Список музыки", self)
        self.buttonMusicList.setGeometry(75, 250, 250, 150)
        self.buttonMusicList.clicked.connect(self.buttonClickedListMusic)

        font = QtGui.QFont()
        font.setPointSize(20)
        self.buttonAddMusic.setFont(font)
        self.buttonMusicList.setFont(font)
    def buttonClickedAddMusic(self):
        addMusic = AddMusic(self)
        addMusic.show()
        addMusic.exec()

    def buttonClickedListMusic(self):
        table = Table(self)
        table.show()
        table.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())
