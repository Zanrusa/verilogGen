# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_add1.ui'
#
# Created: Mon Sep 12 23:48:33 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from comp import *
import moduleType
import moduleStruct
import modulePrint

DICT_TYPE = {0:'iw',
             1:'or',
             2:'ow',
             3:'bw',
             4:'p',
             5:'l'}
class Ui_groupAdd(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(900, 0))
        Form.setMaximumSize(QtCore.QSize(900, 16777215))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 181, 23))
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
        self.btnPlus_4 = QtWidgets.QPushButton(Form)
        self.btnPlus_4.setGeometry(QtCore.QRect(790, 120, 93, 28))
        self.btnPlus_4.setObjectName("btnPlus_4")
        self.addGroup_2 = QtWidgets.QPushButton(Form)
        self.addGroup_2.setGeometry(QtCore.QRect(790, 190, 93, 28))
        self.addGroup_2.setObjectName("addGroup_2")
        self.btnPlus_3 = QtWidgets.QPushButton(Form)
        self.btnPlus_3.setGeometry(QtCore.QRect(790, 70, 93, 28))
        self.btnPlus_3.setObjectName("btnPlus_3")
        self.basicComplist = []
        self.basicComplist.append(Comp_groupMember(Form))
        self.basicComplist[0].setGeometry(QtCore.QRect(10, 50, 700, 80))

        
        self.retranslateUi(Form)
        self.btnPlus_3.clicked.connect(self.ifPlus)
        self.btnPlus_4.clicked.connect(self.ifMinus)
        self.addGroup_2.clicked.connect(self.ifAddgroup)
        self.addGroup_2.clicked.connect(self.accept)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Group Define"))
        self.label.setText(_translate("Form", "Group Name"))
        self.btnPlus_4.setText(_translate("Form", "Minus"))
        self.addGroup_2.setText(_translate("Form", "Add Group"))
        self.btnPlus_3.setText(_translate("Form", "Plus"))

    def ifPlus(self):
        _temp =Comp_groupMember(self)
        _temp.setGeometry(QtCore.QRect(10, 50+len(self.basicComplist)*70, 700, 80))
        _temp.show()
        self.basicComplist.append(_temp)
        if 50+len(self.basicComplist)*70>=240:
            self.resize(900, 120+len(self.basicComplist)*70)
        
    def ifMinus(self):
        self.basicComplist[-1].close()
        del self.basicComplist[-1]
        self.resize(900, 120+len(self.basicComplist)*70)
        
    def ifAddgroup(self):
        self.inlist = {}
        self.outlist = {}
        self.blist = {}
        self.paralist = {}
        self.lplist = {}
        
        for comp in self.basicComplist:
            try:
                _index = comp.typeInput.currentIndex()
                _itype = DICT_TYPE[_index]
                self.groupName = self.groupEdit.text()
                _iname = self.groupName + '_' + comp.nameEdit.text()
                _ivalue = comp.valueEdit.text()
                _iwidth = comp.widthEdit.text()
                if _index == 0:
                    self.inlist[_iname] = moduleType.judgeType(iname=_iname,itype=_itype,iwidth=_iwidth)
                elif _index == 1 or _index == 2:
                    self.outlist[_iname] = moduleType.judgeType(iname=_iname,itype=_itype,iwidth=_iwidth)    
                elif _index == 3:
                    self.blist[_iname] = moduleType.judgeType(iname=_iname,itype=_itype,iwidth=_iwidth)
                elif _index == 4:
                    self.paralist[_iname] = moduleType.paraType(iname=_iname.upper(),ivalue=_ivalue)
                else:
                    self.lplist[_iname] = moduleType.lpType(iname=_iname.upper(),ivalue=_ivalue)
            finally:
                pass
##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    Form = QtWidgets.QWidget()
##    ui = Ui_groupAdd()
##    ui.setupUi(Form)
##    Form.show()
##    sys.exit(app.exec_())

