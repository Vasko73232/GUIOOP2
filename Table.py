from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QFileDialog, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import shutil



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 350)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 651, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(self.rowCount)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Название', 'Жанр', 'Автор', 'Дата создания', 'Альбом', 'Скачать музыку'])
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class Table(QDialog, Ui_Dialog):

    def __init__(self, mainwindow):
        QDialog.__init__(self)

        self.rowCount = 2  # Ввести количество строк по количеству песен
        self.setupUi(self)
        self.setWindowTitle("YourMusic")
        self.setGeometry(700, 500, 640, 340)
        self.setWindowIcon(QIcon("icon.png"))

        self.data = [("Йода.mp3", "dsad", "ddd", ' ', 'asd'), ('asd', 'asd', 'asd', "asdas", "asdasd")]# информация из базы данных

        row = 0
        flag = False
        self.buttonGroup = QButtonGroup(self)

        for tup in self.data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if (flag == False and col > 3):
                    button = QPushButton("Скачать")
                    self.buttonGroup.addButton(button, row)
                    self.tableWidget.setCellWidget(row, 5, button)
                    flag = True
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
            flag = False
            row += 1
        self.buttonGroup.buttonClicked[int].connect(self.copyMusic)

    def copyMusic(self, row):
        self.nameMusic = self.tableWidget.item(row, 0).text()
        self.albumMusic = self.tableWidget.item(row, 3).text()
        self.dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        if (str(self.albumMusic) != ' ' and str(self.albumMusic) != ''):
            shutil.copy("E:\\" + self.albumMusic + '\\' + self.nameMusic,# место "E:\\"+self.albumMusic+'\\'+self.nameMusic
                        str(self.dirlist))                               # написать директорию с музыкой
        else:
            shutil.copy("E:\\" + self.nameMusic, str(self.dirlist))
