# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeFileList = QtWidgets.QTreeWidget(self.splitter)
        self.treeFileList.setAcceptDrops(False)
        self.treeFileList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.treeFileList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.treeFileList.setAlternatingRowColors(True)
        self.treeFileList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeFileList.setObjectName("treeFileList")
        self.treeFileList.header().setVisible(True)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(200, 0))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        spacerItem = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setDefault(True)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnSettings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSettings.sizePolicy().hasHeightForWidth())
        self.btnSettings.setSizePolicy(sizePolicy)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout.addWidget(self.btnSettings)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAddFile = QtWidgets.QAction(MainWindow)
        self.actionAddFile.setObjectName("actionAddFile")
        self.actionConvert = QtWidgets.QAction(MainWindow)
        self.actionConvert.setObjectName("actionConvert")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionExit.setObjectName("actionExit")
        self.actionOpenForumURL = QtWidgets.QAction(MainWindow)
        self.actionOpenForumURL.setObjectName("actionOpenForumURL")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionViewLog = QtWidgets.QAction(MainWindow)
        self.actionViewLog.setObjectName("actionViewLog")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionSettings.setObjectName("actionSettings")
        self.menu.addAction(self.actionAddFile)
        self.menu.addAction(self.actionConvert)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSettings)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionOpenForumURL)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionAbout)
        self.menu_3.addAction(self.actionDelete)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionViewLog)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.closeApp)
        self.actionAddFile.triggered.connect(MainWindow.addFilesAction)
        self.actionConvert.triggered.connect(MainWindow.startConvert)
        self.btnStart.clicked.connect(MainWindow.startConvert)
        self.actionDelete.triggered.connect(MainWindow.deleteRecAction)
        self.actionOpenForumURL.triggered.connect(MainWindow.openSupportURL)
        self.actionViewLog.triggered.connect(MainWindow.openLog)
        self.actionAbout.triggered.connect(MainWindow.about)
        self.actionSettings.triggered.connect(MainWindow.settings)
        self.btnSettings.clicked.connect(MainWindow.settings)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "fb2mobi"))
        self.treeFileList.headerItem().setText(0, _translate("MainWindow", "Title"))
        self.treeFileList.headerItem().setText(1, _translate("MainWindow", "Author"))
        self.treeFileList.headerItem().setText(2, _translate("MainWindow", "File"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnSettings.setText(_translate("MainWindow", "Settings..."))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menu_2.setTitle(_translate("MainWindow", "Help"))
        self.menu_3.setTitle(_translate("MainWindow", "Edit"))
        self.actionAddFile.setText(_translate("MainWindow", "Add..."))
        self.actionAddFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionConvert.setText(_translate("MainWindow", "Start conversion"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpenForumURL.setText(_translate("MainWindow", "Support forum"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionViewLog.setText(_translate("MainWindow", "View log"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionSettings.setText(_translate("MainWindow", "Settings..."))

