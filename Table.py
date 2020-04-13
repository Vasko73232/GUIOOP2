from PyQt5 import QtCore, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QFileDialog, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import shutil

from PyQt5 import QtCore, QtGui


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
#
        self.centralwidget = QtWidgets.QWidget(self)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.view = QtWidgets.QTableView(self.centralwidget)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)

        self.model = QtGui.QStandardItemModel(self)

        for rowName in self.data:
            self.model.invisibleRootItem().appendRow(
                [QtGui.QStandardItem(rowName[column])
                 for column in range(1)
                 ]
            )
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.view.setModel(self.proxy)

        self.horizontalHeader = self.view.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)
#

        self.horizontalHeader = self.view.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)

    @QtCore.pyqtSlot(int)
    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):

        self.logicalIndex = logicalIndex
        self.menuValues = QtWidgets.QMenu(self)
        self.signalMapper = QtCore.QSignalMapper(self)
        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(self.logicalIndex)
        self.comboBox.blockSignals(True)

        valuesUnique = [self.model.item(row, self.logicalIndex).text()
                        for row in range(self.model.rowCount())
                        ]
        actionAll = QtWidgets.QAction("All", self)
        actionAll.triggered.connect(self.on_actionAll_triggered)
        self.menuValues.addAction(actionAll)
        self.menuValues.addSeparator()
        for actionNumber, actionName in enumerate(sorted(list(set(valuesUnique)))):
            action = QtWidgets.QAction(actionName, self)
            self.signalMapper.setMapping(action, actionNumber)
            action.triggered.connect(self.signalMapper.map)
            self.menuValues.addAction(action)
        self.signalMapper.mapped.connect(self.on_signalMapper_mapped)
        headerPos = self.view.mapToGlobal(self.horizontalHeader.pos())
        posY = headerPos.y() + self.horizontalHeader.height()
        posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)

        self.menuValues.exec_(QtCore.QPoint(posX, posY))

    @QtCore.pyqtSlot()
    def on_actionAll_triggered(self):
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp("",
                                      QtCore.Qt.CaseInsensitive,
                                      QtCore.QRegExp.RegExp
                                      )

        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    @QtCore.pyqtSlot(int)
    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp(stringAction,
                                      QtCore.Qt.CaseSensitive,
                                      QtCore.QRegExp.FixedString
                                      )

        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        search = QtCore.QRegExp(text,
                                QtCore.Qt.CaseInsensitive,
                                QtCore.QRegExp.RegExp
                                )

        self.proxy.setFilterRegExp(search)

    @QtCore.pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self, index):
        self.proxy.setFilterKeyColumn(index)

    def copyMusic(self, row):
        self.nameMusic = self.tableWidget.item(row, 0).text()
        self.albumMusic = self.tableWidget.item(row, 3).text()
        self.dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        if (str(self.albumMusic) != ' ' and str(self.albumMusic) != ''):
            shutil.copy("E:\\" + self.albumMusic + '\\' + self.nameMusic,# место "E:\\"+self.albumMusic+'\\'+self.nameMusic
                        str(self.dirlist))                               # написать директорию с музыкой
        else:
            shutil.copy("E:\\" + self.nameMusic, str(self.dirlist))
