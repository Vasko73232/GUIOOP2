import sys
# pyuic5 AddMusic.ui -o AddMusic.py
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from AddMusic import AddMusic
from Table import Table
from PyQt5 import QtGui
from AddGenre import AddGenre
from AddAuthor import AddAuthor
from AddAlbum import AddAlbum


class Application(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("YourMusic")
        self.setGeometry(700, 500, 400, 500)
        self.setWindowIcon(QIcon("icon.png"))

        self.buttonAddMusic = QPushButton("Добавить музыку", self)
        self.buttonAddMusic.setGeometry(75, 25, 250, 125)
        self.buttonAddMusic.clicked.connect(self.buttonClickedAddMusic)

        self.buttonMusicList = QPushButton("Список музыки", self)
        self.buttonMusicList.setGeometry(75, 175, 250, 125)
        self.buttonMusicList.clicked.connect(self.buttonClickedListMusic)

        self.buttonAddAuthor = QPushButton("Добавить \n исполнителя", self)
        self.buttonAddAuthor.setGeometry(25, 325, 100, 100)
        self.buttonAddAuthor.clicked.connect(self.buttonClickedAddAuthor)

        self.buttonAddAlbum = QPushButton("Добавить \n альбом", self)
        self.buttonAddAlbum.setGeometry(150, 325, 100, 100)
        self.buttonAddAlbum.clicked.connect(self.buttonClickedAddAlbum)

        self.buttonAddGenre = QPushButton("Добавить \n жанр", self)
        self.buttonAddGenre.setGeometry(275, 325, 100, 100)
        self.buttonAddGenre.clicked.connect(self.buttonClickedAddGenre)

        self.setStyleSheet("11.png")
        font = QtGui.QFont()
        font.setPointSize(20)
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        self.buttonAddMusic.setFont(font)
        self.buttonMusicList.setFont(font)
        self.buttonAddGenre.setFont(font1)
        self.buttonAddAuthor.setFont(font1)
        self.buttonAddAlbum.setFont(font1)
    def buttonClickedAddMusic(self):
        addMusic = AddMusic(self)
        addMusic.show()
        addMusic.exec()

    def buttonClickedListMusic(self):
        table = Table(self)
        table.show()
        table.resize(800, 600)


    def buttonClickedAddAuthor(self):
        table = AddAuthor(self)
        table.show()
        table.exec()

    def buttonClickedAddAlbum(self):
        table = AddAlbum(self)
        table.show()
        table.exec()

    def buttonClickedAddGenre(self):
        table = AddGenre(self)
        table.show()
        table.exec()

if __name__ == '__main__':
    app = QApplication([])
    s = QStyleFactory.create('Fusion')
    app.setStyle(s)
    ex = Application()

    ex.show()
    sys.exit(app.exec_())
