# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_add.ui'
#
# Created: Mon Sep 12 20:03:18 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from comp import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 280)
        MainWindow.setMinimumSize(QtCore.QSize(920, 0))
        MainWindow.setMaximumSize(QtCore.QSize(920, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(820, 40, 93, 28))
        self.btnPlus.setObjectName("btnPlus")
        self.addGroup = QtWidgets.QPushButton(self.centralwidget)
        self.addGroup.setGeometry(QtCore.QRect(820, 160, 93, 28))
        self.addGroup.setObjectName("addGroup")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 181, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.groupEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.groupEdit.setObjectName("groupEdit")
        self.horizontalLayout.addWidget(self.groupEdit)
        self.btnPlus_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus_2.setGeometry(QtCore.QRect(820, 90, 93, 28))
        self.btnPlus_2.setObjectName("btnPlus_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
####        self.verticalLayoutWidget.setpolicy(0, 60, geometry().width(), geometry().height()-60)
##        print(self.verticalLayoutWidget.sizePolicy())
##        _treesize = self.verticalLayoutWidget.sizePolicy()
##        _treesize.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)
##        self.verticalLayoutWidget.resize(781 ,200)
        self.verticalLayoutWidget.setGeometry(20, 50, 781 ,200)
##        self.verticalLayoutWidget.setSizePolicy(_treesize)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainVLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVLayout.setObjectName("mainVLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.basicComplist = []
        self.basicComplist.append(Comp_groupMember(MainWindow))
        self.mainVLayout.addWidget(self.basicComplist[0])
        
        self.retranslateUi(MainWindow)
        self.btnPlus.clicked.connect(self.ifPlus)
        self.btnPlus_2.clicked.connect(self.ifMinus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPlus.setText(_translate("MainWindow", "Plus"))
        self.addGroup.setText(_translate("MainWindow", "Add Group"))
        self.label.setText(_translate("MainWindow", "Group Name"))
        self.btnPlus_2.setText(_translate("MainWindow", "Minus"))

    def ifPlus(self):
        self.basicComplist.append(Comp_groupMember(MainWindow))
        self.mainVLayout.addWidget(self.basicComplist[-1])

    def ifMinus(self):
        self.basicComplist[-1].close()
        del self.basicComplist[-1]
        
##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = Ui_MainWindow()
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())

