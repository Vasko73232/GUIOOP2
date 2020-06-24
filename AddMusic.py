from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, uic
import shutil
from os import path

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(313, 422)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.buttonChooseFileMusic = QtWidgets.QPushButton(Dialog)
        self.buttonChooseFileMusic.setGeometry(QtCore.QRect(20, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonChooseFileMusic.setFont(font)
        self.buttonChooseFileMusic.setObjectName("chooseFileMusic")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 130, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameMusic = QtWidgets.QLineEdit(Dialog)
        self.nameMusic.setGeometry(QtCore.QRect(20, 50, 261, 20))
        self.nameMusic.setObjectName("nameMusic")
        self.genreMusic = QtWidgets.QComboBox(Dialog)
        self.genreMusic.setGeometry(QtCore.QRect(20, 160, 100, 20))
        self.genreMusic.setObjectName("genreMusic")
        self.genreMusic.addItem("")
        self.genreMusic.addItem("Электронная музыка")  # Подключить список жанров из бд
        self.genreMusic.addItem("Шансон")
        self.genreMusic.addItem("Джаз")
        self.genreMusic.addItem("Блюз")
        self.genreMusic.addItem("Кантри")
        self.genreMusic.addItem("Рок")
        self.genreMusic.addItem("Хип-хоп")
        self.genreMusic.addItem("Поп")
        self.genreMusic.addItem("Народная песня")


        self.authorMusic = QtWidgets.QComboBox(Dialog)
        self.authorMusic.setGeometry(QtCore.QRect(20, 100, 261, 20))
        self.authorMusic.setObjectName("authorMusic")
        self.authorMusic.addItem("dd")

        self.yearMusic = QtWidgets.QComboBox(Dialog)
        self.yearMusic.setGeometry(QtCore.QRect(130, 160, 100, 20))
        self.yearMusic.setObjectName("yearMusic")
        self.yearMusic.addItem(' ')
        for i in range(1880, 2020):
            self.yearMusic.addItem(str(i))
        self.buttonAddMusic = QtWidgets.QPushButton(Dialog)
        self.buttonAddMusic.setGeometry(QtCore.QRect(100, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonAddMusic.setFont(font)
        self.buttonAddMusic.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.albumchooseMusic = QtWidgets.QComboBox(Dialog)
        self.albumchooseMusic.setGeometry(QtCore.QRect(20, 220, 100, 20))
        self.albumchooseMusic.setObjectName("albomchooseMusic")
        self.albumchooseMusic.addItem("")


        self.albumchooseMusic.addItem("Music")#Брать из сервера
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Жанр"))
        self.label_2.setText(_translate("Dialog", "Автор"))
        self.buttonChooseFileMusic.setText(_translate("Dialog", "Обзор файла"))
        self.label_4.setText(_translate("Dialog", "Год создания"))
        self.label_5.setText(_translate("Dialog", "Выбрать альбом"))
        self.label.setText(_translate("Dialog", "Название музыки"))
        self.buttonAddMusic.setText(_translate("Dialog", "Загрузить музыку"))
        self.label_6.setText(_translate("Dialog", "Выберите файл"))


class AddMusic(QDialog, Ui_Dialog):

    def saveMusic(self):
        self.fileMusic = QFileDialog().getOpenFileName(self, filter="*.mp3 *.mp4 *.ac3 *.wma *.wav *.mid ")
        if (self.fileMusic != ''):
            self.saveMus = True

    def informationMusic(self):
        self.name_MusicText = self.nameMusic.text()
        self.author_MusicText = self.authorMusic.currentText()
        self.genre_MusicText = self.genreMusic.currentText()
        self.year_MusicText = self.yearMusic.currentText()
        self.album_NameMusicText = self.albumchooseMusic.currentText()
        if (self.album_NameMusicText == ''):
            self.album_NameMusicText = self.albumNameMusic.text()

        if (self.name_MusicText != '' and self.author_MusicText != '' and self.genre_MusicText != '' and self.album_NameMusicText != ''):  # Если все заполненно закрыть
            self.infoMusic = True
        if (self.infoMusic == True and self.saveMus == True):
            shutil.copy(str(self.fileMusic[0]),
                        "C:\\" + self.album_NameMusicText)  # Передать название файла музыки!!!Указать путь к каталогу с альбомами
            name = path.basename(self.fileMusic[0])
            nameExpansion = path.splitext(name)[1]


            shutil.move("C:\\"+self.album_NameMusicText+'\\'+name,"C:\\"+self.album_NameMusicText+'\\'+self.name_MusicText+nameExpansion)
            self.close()

    def __init__(self, mainwindow):
        QDialog.__init__(self)
        self.saveMus = False
        self.infoMusic = False
        self.setupUi(self)
        self.setWindowTitle("YourMusic")
        self.setGeometry(700, 500, 300, 400)
        self.setWindowIcon(QIcon("icon.png"))

        self.buttonAddMusic.clicked.connect(self.informationMusic)
        self.buttonChooseFileMusic.clicked.connect(self.saveMusic)
