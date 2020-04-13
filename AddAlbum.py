
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, uic
import shutil


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(313, 422)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label_3 = QtWidgets.QLabel("Название альбома",Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 1000, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label")

        self.buttonChooseAddAlbum = QtWidgets.QPushButton("Добавить",Dialog)
        self.buttonChooseAddAlbum.setGeometry(QtCore.QRect(130, 65, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonChooseAddAlbum.setFont(font)
        self.buttonChooseAddAlbum.setObjectName("chooseFileMusic")
        self.nameAlbum = QtWidgets.QLineEdit(Dialog)
        self.nameAlbum.setGeometry(QtCore.QRect(20, 35, 261, 20))

        QtCore.QMetaObject.connectSlotsByName(Dialog)


class AddAlbum(QDialog, Ui_Dialog):

    def informationAlbum(self):
        self.name_AlbumText = self.nameAlbum.text()
        self.close()

    def __init__(self, mainwindow):
        QDialog.__init__(self)
        self.saveMus = False
        self.infoMusic = False
        self.setupUi(self)
        self.setWindowTitle("YourMusic")
        self.setGeometry(700, 500, 300, 100)
        self.setWindowIcon(QIcon("icon.png"))

        self.buttonChooseAddAlbum.clicked.connect(self.informationAlbum)