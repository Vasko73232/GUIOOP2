import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QVariant, QModelIndex
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QHeaderView, QSizePolicy, QFileDialog, QPushButton, QTableWidgetItem, QButtonGroup, \
    QTableView


class Table(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.centralwidget  = QtWidgets.QWidget(self)

        self.view           = QTableView(self.centralwidget)
        self.comboBox       = QtWidgets.QComboBox()


        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.gridLayout.addWidget(self.view, 1, 0, 1, 3)


        self.setCentralWidget(self.centralwidget)


        self.model = QtGui.QStandardItemModel(self)
        self.data = [("Йода.mp3", "dsad", "ddd", ' ', ' '), ('d', 'asd', '1', "asdas", "asdasd"),("ddd",'asd', '1', "asdas", "asdasd"),("ww",'asd', '1', "asdas", "asdasd")]
        for rowName in self.data:
            self.model.invisibleRootItem().appendRow(
                [   QtGui.QStandardItem(rowName[column])
                    for column in range(5)
                    ]
                )

        self.model.setHorizontalHeaderLabels(['Название', 'Жанр', 'Автор', 'Дата создания', 'Альбом', 'Скачать музыку'])

        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)

        self.view.setModel(self.proxy)

        self.comboBox.addItems(["Column {0}".format(x) for x in range(self.model.columnCount())])
        self.buttonGroup = QButtonGroup(self)
        row = 0
        flag = False

        for tup in self.data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if (flag == False and col > 3):
                    button = QPushButton("Скачать")
                    self.buttonGroup.addButton(button, row)
                    self.view.setIndexWidget(self.proxy.index(row, 5), button)
                    flag = True

                col += 1
            flag = False
            row += 1
        self.buttonGroup.buttonClicked[int].connect(self.copyMusic)
        # self.lineEdit.textChanged.connect(self.on_lineEdit_textChanged)
        # self.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

        self.horizontalHeader = self.view.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)


    @QtCore.pyqtSlot(int)
    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):

        self.logicalIndex   = logicalIndex
        self.menuValues     = QtWidgets.QMenu(self)
        self.signalMapper   = QtCore.QSignalMapper(self)
        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(self.logicalIndex)
        self.comboBox.blockSignals(True)

        valuesUnique = [    self.model.item(row, self.logicalIndex).text()
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

        row = 0
        flag = False


        for tup in self.data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if (flag == False and col > 3):
                    button = QPushButton("Скачать")
                    self.buttonGroup.addButton(button, row)
                    self.view.setIndexWidget(self.proxy.index(row, 5), button)
                    flag = True

                col += 1
            flag = False
            row += 1
        self.buttonGroup.buttonClicked[int].connect(self.copyMusic)
    @QtCore.pyqtSlot()
    def on_actionAll_triggered(self):
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp(  "",
                                        QtCore.Qt.CaseInsensitive,
                                        QtCore.QRegExp.RegExp
                                        )

        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    @QtCore.pyqtSlot(int)
    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp(  stringAction,
                                        QtCore.Qt.CaseSensitive,
                                        QtCore.QRegExp.FixedString
                                        )

        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        search = QtCore.QRegExp(    text,
                                    QtCore.Qt.CaseInsensitive,
                                    QtCore.QRegExp.RegExp
                                    )

        self.proxy.setFilterRegExp(search)

    @QtCore.pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self, index):
        self.proxy.setFilterKeyColumn(index)

    def copyMusic(self, row):




        self.nameMusic = self.view.indexAt(QPoint(0,30*row)).data(Qt.DisplayRole)
        self.albumMusic = self.view.indexAt(QPoint(400, 30*row)).data(Qt.DisplayRole)
        self.dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        if self.dirlist!="":
            if (str(self.albumMusic) != ' ' and str(self.albumMusic) != ''):
                shutil.copy("E:\\" + self.albumMusic + '\\' + self.nameMusic,
                            # место "E:\\"+self.albumMusic+'\\'+self.nameMusic
                            str(self.dirlist))  # написать директорию с музыкой
            else:
                shutil.copy("E:\\" + self.nameMusic, str(self.dirlist))