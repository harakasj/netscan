# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'netscan.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 328)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.table_ifaces = QtWidgets.QTableWidget(self.centralwidget)
        self.table_ifaces.setAutoFillBackground(False)
        self.table_ifaces.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.table_ifaces.setShowGrid(False)
        self.table_ifaces.setGridStyle(QtCore.Qt.SolidLine)
        self.table_ifaces.setRowCount(0)
        self.table_ifaces.setColumnCount(2)
        self.table_ifaces.setObjectName("table_ifaces")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.table_ifaces.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.table_ifaces.setHorizontalHeaderItem(1, item)
        self.table_ifaces.horizontalHeader().setCascadingSectionResizes(True)
        self.table_ifaces.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.table_ifaces, 0, 0, 1, 1)
        self.btn_scan = QtWidgets.QPushButton(self.centralwidget)
        self.btn_scan.setObjectName("btn_scan")
        self.gridLayout.addWidget(self.btn_scan, 1, 0, 1, 1)
        self.table_arp = QtWidgets.QTableWidget(self.centralwidget)
        self.table_arp.setShowGrid(False)
        self.table_arp.setObjectName("table_arp")
        self.table_arp.setColumnCount(2)
        self.table_arp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_arp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_arp.setHorizontalHeaderItem(1, item)
        self.table_arp.horizontalHeader().setCascadingSectionResizes(True)
        self.table_arp.horizontalHeader().setSortIndicatorShown(True)
        self.table_arp.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.table_arp, 2, 0, 1, 1)
        self.btn_arpscan = QtWidgets.QPushButton(self.centralwidget)
        self.btn_arpscan.setObjectName("btn_arpscan")
        self.gridLayout.addWidget(self.btn_arpscan, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.table_ifaces.setSortingEnabled(True)
        item = self.table_ifaces.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Interface"))
        item = self.table_ifaces.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address"))
        self.btn_scan.setText(_translate("MainWindow", "Scan Interfaces"))
        item = self.table_arp.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP Address"))
        item = self.table_arp.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC Address"))
        self.btn_arpscan.setText(_translate("MainWindow", "Arp Scan"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

