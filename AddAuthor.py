
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
        self.label_3 = QtWidgets.QLabel("Название автора",Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 1000, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label")

        self.buttonChooseAddAuthor = QtWidgets.QPushButton("Добавить",Dialog)
        self.buttonChooseAddAuthor.setGeometry(QtCore.QRect(130, 65, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonChooseAddAuthor.setFont(font)
        self.buttonChooseAddAuthor.setObjectName("chooseFileMusic")
        self.nameAuthor = QtWidgets.QLineEdit(Dialog)
        self.nameAuthor.setGeometry(QtCore.QRect(20, 35, 261, 20))
        self.nameAuthor.setObjectName("nameMusic")
        QtCore.QMetaObject.connectSlotsByName(Dialog)


class AddAuthor(QDialog, Ui_Dialog):

    def informationAuthor(self):
        self.name_AuthorText = self.nameAuthor.text()
        self.close()

    def __init__(self, mainwindow):
        QDialog.__init__(self)
        self.saveMus = False
        self.infoMusic = False
        self.setupUi(self)
        self.setWindowTitle("YourMusic")
        self.setGeometry(700, 500, 300, 100)
        self.setWindowIcon(QIcon("icon.png"))

        self.buttonChooseAddAuthor.clicked.connect(self.informationAuthor)