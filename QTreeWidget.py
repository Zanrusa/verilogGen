# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testscrollbar.ui'
#
# Created: Tue Sep 13 21:39:06 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(80, 60, 256, 121))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.header().setCascadingSectionResizes(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, _translate("Form", "a"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "saf"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "dsaf"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "saf"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Form", "sdfd"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("Form", "sdfds"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("Form", "fdsfsdaf"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

