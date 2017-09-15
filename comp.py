# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bcomponent1.ui'
#
# Created: Mon Sep 12 19:43:43 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Comp_groupMember(QtWidgets.QWidget):
    def __init__(self,Form):
        super().__init__(Form)
        self.resize(600, 50)
        self.setupUi(self)
        
    def setupUi(self, Form):
        self.groupMember_3 = QtWidgets.QWidget(Form)
        self.groupMember_3.resize(600, 50)
        self.groupMember_3.setObjectName("groupMember_3")
        self.groupMember = QtWidgets.QHBoxLayout(self.groupMember_3)
        self.groupMember.setContentsMargins(0, 0, 0, 0)
        self.groupMember.setObjectName("groupMember")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name = QtWidgets.QLabel(self.groupMember_3)
        self.name.setObjectName("name")
        self.horizontalLayout_2.addWidget(self.name)
        self.nameEdit = QtWidgets.QLineEdit(self.groupMember_3)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_2.addWidget(self.nameEdit)
        self.groupMember.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.type = QtWidgets.QLabel(self.groupMember_3)
        self.type.setObjectName("type")
        self.horizontalLayout_6.addWidget(self.type)
        self.typeInput = QtWidgets.QComboBox(self.groupMember_3)
        self.typeInput.setObjectName("typeInput")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.horizontalLayout_6.addWidget(self.typeInput)
        self.groupMember.addLayout(self.horizontalLayout_6)
        self.widthWidget = QtWidgets.QWidget(self.groupMember_3)
        self.widthWidget.setObjectName("widthWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widthWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.width = QtWidgets.QLabel(self.widthWidget)
        self.width.setObjectName("width")
        self.horizontalLayout_8.addWidget(self.width)
        self.widthEdit = QtWidgets.QLineEdit(self.widthWidget)
        self.widthEdit.setObjectName("widthEdit")
        self.horizontalLayout_8.addWidget(self.widthEdit)
        self.groupMember.addWidget(self.widthWidget)
        self.valueWidget = QtWidgets.QWidget(self.groupMember_3)
        self.valueWidget.setObjectName("valueWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.valueWidget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.value = QtWidgets.QLabel(self.valueWidget)
        self.value.setObjectName("value")
        self.horizontalLayout_9.addWidget(self.value)
        self.valueEdit = QtWidgets.QLineEdit(self.valueWidget)
        self.valueEdit.setObjectName("valueEdit")
        self.horizontalLayout_9.addWidget(self.valueEdit)
        self.groupMember.addWidget(self.valueWidget)

        self.retranslateUi(Form)
        self.typeInput.currentTextChanged['QString'].connect(self.ifChanged)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "Name"))
        self.type.setText(_translate("Form", "Type"))
        self.typeInput.setItemText(0, _translate("Form", "input"))
        self.typeInput.setItemText(1, _translate("Form", "output reg"))
        self.typeInput.setItemText(2, _translate("Form", "output wire"))
        self.typeInput.setItemText(3, _translate("Form", "inout"))
        self.typeInput.setItemText(4, _translate("Form", "parameter"))
        self.typeInput.setItemText(5, _translate("Form", "localparam"))
        self.width.setText(_translate("Form", "Width"))
        self.value.setText(_translate("Form", "Value"))

    def ifChanged(self):
        _currentIndex = self.typeInput.currentIndex()
        if 0<=_currentIndex<=3:
            self.valueWidget.hide()
            self.widthWidget.show()
        else:
            self.valueWidget.show()
            self.widthWidget.hide()

