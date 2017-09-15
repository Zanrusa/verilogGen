# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'veri_scan.ui'
#
# Created: Tue Sep 13 20:00:27 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from group_add1 import *
from input_add import *
from output_add import *
from inout_add import *
from others_add import *
from para_add import *
from lp_add import *

import moduleType,moduleStruct,modulePrint
import pickle
import os.path

##class nodupWidget(QtWidgets.QTreeWidgetItem):
##    def __init__(self,upperwidget,widgetname):
##        print(upperwidget.child())
##        _itemlist = upperwidget.findItems(widgetname,QtCore.Qt.MatchExactly,0)
##        for item in _itemlist:
##            upperwidget.takeChild(upperwidget.indexOfChild(item))
##        super().__init__(upperwidget)
##        self.setText(0,widgetname)
            
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.DB = {}
        if os.path.exists('groupMem.pkl'):
            with open('groupMem.pkl','rb') as groupload:
                self.USR_DEF = pickle.load(groupload)
        else:
            with open('groupMem.pkl','wb')as groupdump:
                self.USR_DEF = {}
                pickle.dump(self.USR_DEF,groupdump)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(400, 40, 371, 441))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setObjectName("treeWidget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(543, 515, 228, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGenerate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnGenerate.setObjectName("btnGenerate")
        self.horizontalLayout.addWidget(self.btnGenerate)
        self.btnLoad = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLoad.setObjectName("btnLoad")
        self.horizontalLayout.addWidget(self.btnLoad)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(8, 41, 130, 407))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(-1, 50, -1, -1)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.btnGroup = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnGroup.setObjectName("btnGroup")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.btnGroup)
        self.btnInput = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnInput.setObjectName("btnInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.btnInput)
        self.btnOutput = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnOutput.setObjectName("btnOutput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.btnOutput)
        self.btnInout = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnInout.setObjectName("btnInout")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.btnInout)
        self.btnOthers = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnOthers.setObjectName("btnOthers")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.btnOthers)
        self.btnParameter = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnParameter.setObjectName("btnParameter")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.btnParameter)
        self.btnLocalparam = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnLocalparam.setObjectName("btnLocalparam")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.btnLocalparam)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(11, 11, 268, 23))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_2.addWidget(self.nameLabel)
        self.modName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.modName.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.modName.setInputMask("")
        self.modName.setObjectName("modName")
        self.horizontalLayout_2.addWidget(self.modName)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 130, 95, 216))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(120)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnDel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDel.setObjectName("btnDel")
        self.verticalLayout_2.addWidget(self.btnDel)
        self.treeGroup = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeGroup.setGeometry(QtCore.QRect(143, 41, 151, 441))
        self.treeGroup.setAutoFillBackground(False)
        self.treeGroup.setUniformRowHeights(False)
        self.treeGroup.setWordWrap(False)
        self.treeGroup.setObjectName("treeWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #dialog
        self.parameterDialog = Ui_paraAdd()
        self.localparamDialog = Ui_lpAdd()
        self.inoutDialog = Ui_inoutAdd()
        self.outputDialog = Ui_outputAdd()
        self.inputDialog = Ui_inputAdd()
        self.othersDialog = Ui_othersAdd()
        self.treeTops()
        
        
##        self.userElement = QtWidgets.QTreeWidgetItem(self.treeGroup)
##        self.userGroup = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.deleteTree = self.treeGroup
        
        self.retranslateUi(MainWindow)

        self.btnGroup.clicked.connect(self.ifbtnGroup)
        self.btnInput.clicked.connect(self.ifbtnInput)
        self.btnOutput.clicked.connect(self.ifbtnOutput)
        self.btnInout.clicked.connect(self.ifbtnInout)
        self.btnOthers.clicked.connect(self.ifbtnOthers)
        self.btnParameter.clicked.connect(self.ifbtnParameter)
        self.btnLocalparam.clicked.connect(self.ifbtnLocalparam)
        
        self.btnGenerate.clicked.connect(self.ifbtnGenerate)
        self.btnLoad.clicked.connect(self.ifbtnLoad)
        
        self.btnAdd.clicked.connect(self.ifbtnAdd)
        self.btnDel.clicked.connect(self.ifbtnDel)
        self.treeGroup.itemClicked.connect(self.ifdelChanged_treeGroup)
        self.treeWidget.itemClicked.connect(self.ifdelChanged_treeWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeGroup.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeWidget.setSortingEnabled(False)
        self.btnGenerate.setText(_translate("MainWindow", "Generate"))
        self.btnLoad.setText(_translate("MainWindow", "Load"))
        self.btnGroup.setText(_translate("MainWindow", "Group"))
        self.btnInput.setText(_translate("MainWindow", "Input"))
        self.btnOutput.setText(_translate("MainWindow", "Output"))
        self.btnInout.setText(_translate("MainWindow", "Inout"))
        self.btnOthers.setText(_translate("MainWindow", "Others"))
        self.btnParameter.setText(_translate("MainWindow", "Parameter"))
        self.btnLocalparam.setText(_translate("MainWindow", "Localparam"))
        self.nameLabel.setText(_translate("MainWindow", "Module Name"))
        self.modName.setText(_translate("MainWindow", "default"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDel.setText(_translate("MainWindow", "Del"))

        self.loadGroup()
        
        self.treeGroup.headerItem().setText(0, _translate("Form", "User Group"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "User Port and Define"))
##        self.treeGroup.topLevelItem(0).setText(0, _translate("Form", "test"))
##        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "test"))
        
    def treeTops(self):
        self.topOutput = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.topOutput.setText(0,'output')
        self.topReg = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.topReg.setText(0,'reg')
        self.topWire = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.topWire.setText(0,'wire')
        self.topInput = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.topInput.setText(0,'input')
        self.topInout = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.topInout.setText(0,'inout')
        self.topParameter = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.topParameter.setText(0,'parameter')
        self.topLocalparam = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.topLocalparam.setText(0,'localparam')
        
    def loadGroup(self):
        for gname in self.USR_DEF:
            _groupname = QtWidgets.QTreeWidgetItem(self.treeGroup)
            _groupname.setText(0,gname)
            _temp=self.USR_DEF[gname]
            for ilist in _temp:
                for names in ilist:
                    _item = QtWidgets.QTreeWidgetItem(_groupname)
                    _item.setText(0,names)
        
    def ifbtnGroup(self):
        self.dialog = Ui_groupAdd()
        if self.dialog.exec_():
            _groupname = QtWidgets.QTreeWidgetItem(self.treeGroup)
            _groupname.setText(0,self.dialog.groupName)
            _temp=[self.dialog.inlist,
                   self.dialog.outlist,
                   self.dialog.blist,
                   self.dialog.paralist,
                   self.dialog.lplist]
            for ilist in _temp:
                for names in ilist:
                    _item = QtWidgets.QTreeWidgetItem(_groupname)
                    _item.setText(0,names)
            self.USR_DEF[self.dialog.groupName] = _temp
            with open('groupMem.pkl','wb') as pkl_file:
                pickle.dump(self.USR_DEF,pkl_file)

    def ifbtnOthers(self):
        self.othersDialog.show()
        if self.othersDialog.exec_():
            _temp=[self.othersDialog.reglist,
                   self.othersDialog.wirelist]
            self.topReg.takeChildren()
            self.topWire.takeChildren()
            for names in self.othersDialog.reglist:
                _item = QtWidgets.QTreeWidgetItem(self.topReg)
                _item.setText(0,names)
            for names in self.othersDialog.wirelist:
                _item = QtWidgets.QTreeWidgetItem(self.topWire)
                _item.setText(0,names)
            self.DB['others'] = _temp
            
    def ifbtnInput(self):
        self.inputDialog.show()
        if self.inputDialog.exec_():
            _temp = [self.inputDialog.inlist]
            self.topInput.takeChildren()
            for names in self.inputDialog.inlist:
                _item = QtWidgets.QTreeWidgetItem(self.topInput)
                _item.setText(0,names)
            self.DB['input'] = _temp
            
    def ifbtnOutput(self):
        self.outputDialog.show()
        if self.outputDialog.exec_():
            _temp = [self.outputDialog.outlist]
            self.topOutput.takeChildren()
            for names in self.outputDialog.outlist:
                _item = QtWidgets.QTreeWidgetItem(self.topOutput)
                _item.setText(0,names)
            self.DB['output'] = _temp

    def ifbtnInout(self):
        self.inoutDialog.show()
        if self.inoutDialog.exec_():
            _temp = [self.inoutDialog.blist]
            self.topInout.takeChildren()
            for names in self.inoutDialog.blist:
                _item = QtWidgets.QTreeWidgetItem(self.topInout)
                _item.setText(0,names)
            self.DB['inout'] = _temp

    def ifbtnParameter(self):
        self.parameterDialog.show()
        if self.parameterDialog.exec_():
            _temp = [self.parameterDialog.paralist]
            self.topParameter.takeChildren()
            for names in self.parameterDialog.paralist:
                _item = QtWidgets.QTreeWidgetItem(self.topParameter)
                _item.setText(0,names)
            self.DB['parameter'] = _temp

    def ifbtnLocalparam(self):
        self.localparamDialog.show()
        if self.localparamDialog.exec_():
            _temp = [self.localparamDialog.lplist]
            self.topLocalparam.takeChildren()
            for names in self.localparamDialog.lplist:
                _item = QtWidgets.QTreeWidgetItem(self.topLocalparam)
                _item.setText(0,names)
            self.DB['localparam'] = _temp

    def ifbtnLoad(self):
        self.dialog = QtWidgets.QFileDialog()
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.dialog,'Select Verilog File',
                                                         '/home','Verilog File(*.v)')
        modulelist = moduleStruct.splitFile(fileName[0])
        for mod in modulelist:
            _temp = moduleStruct.originModule(mod)
            #localparam
            self.topLocalparam.takeChildren()
            for names in _temp.DB_lp:
                _item = QtWidgets.QTreeWidgetItem(self.topLocalparam)
                _item.setText(0,names)
            self.DB['localparam'] = [_temp.DB_lp]
            self.localparamDialog.loadElement(self.DB['localparam'])
            #parameter
            self.topParameter.takeChildren()
            for names in _temp.DB_para:
                _item = QtWidgets.QTreeWidgetItem(self.topParameter)
                _item.setText(0,names)
            self.DB['parameter'] = [_temp.DB_para]
            self.parameterDialog.loadElement(self.DB['parameter'])
            #input
            self.topInput.takeChildren()
            for names in _temp.DB_input:
                _item = QtWidgets.QTreeWidgetItem(self.topInput)
                _item.setText(0,names)
            self.DB['input'] = [_temp.DB_input]
            self.inputDialog.loadElement(self.DB['input'])
            #output
            self.topOutput.takeChildren()
            for names in _temp.DB_output:
                _item = QtWidgets.QTreeWidgetItem(self.topOutput)
                _item.setText(0,names)
            self.DB['output'] = [_temp.DB_output]
            self.outputDialog.loadElement(self.DB['output'])
            #inout
            self.topInout.takeChildren()
            for names in _temp.DB_inout:
                _item = QtWidgets.QTreeWidgetItem(self.topInout)
                _item.setText(0,names)
            self.DB['inout'] = [_temp.DB_inout]
            self.inoutDialog.loadElement(self.DB['inout'])
            #others
            self.topReg.takeChildren()
            self.topWire.takeChildren()
            for names in _temp.DB_reg:
                _item = QtWidgets.QTreeWidgetItem(self.topReg)
                _item.setText(0,names)
            for names in _temp.DB_wire:
                _item = QtWidgets.QTreeWidgetItem(self.topWire)
                _item.setText(0,names)
            self.DB['others'] = [_temp.DB_reg,_temp.DB_wire]
            self.othersDialog.loadElement(self.DB['others'])
            

    def ifbtnGenerate(self):
        _modulename = self.modName.text()
        _dbpara = {}
        _dblp = {}
        _dbin = {}
        _dbout ={}
        _dbio = {}
        _dbreg = {}
        _dbwire ={}
        for _name in self.DB:
            if _name is 'localparam':
                _dblp.update(self.DB[_name][0])
            elif _name is 'parameter':
                _dbpara.update(self.DB[_name][0])
            elif _name is 'inout':
                _dbio.update(self.DB[_name][0])
            elif _name is 'input':
                _dbin.update(self.DB[_name][0])
            elif _name is 'output':
                _dbout.update(self.DB[_name][0])
            elif _name is 'others':
                _dbreg.update(self.DB[_name][0])
                _dbwire.update(self.DB[_name][1])
            else:
                _dbin.update(self.DB[_name][0])
                _dbout.update(self.DB[_name][1])
                _dbio.update(self.DB[_name][2])
                _dbpara.update(self.DB[_name][3])
                _dblp.update(self.DB[_name][4])
        modulePrint.genByinfo(modulename = _modulename,
                              dbpara = _dbpara,
                              dblp = _dblp,
                              dbin = _dbin,
                              dbout = _dbout,
                              dbio = _dbio,
                              dbreg = _dbreg,
                              dbwire = _dbwire)
                
            
    def ifbtnAdd(self):
        try:
            _temp = self.treeGroup.currentItem()
            _name = _temp.parent().text(0) if _temp.parent() is not None else _temp.text(0)
            _grouplist = self.USR_DEF[_name]
            _itemlist = self.treeWidget.findItems(_name,QtCore.Qt.MatchExactly,0)
            for item in _itemlist:
                self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item))
            _groupname = QtWidgets.QTreeWidgetItem(self.treeWidget)
            _groupname.setText(0,_name)
            for ilist in _grouplist:
                for names in ilist:
                    _item = QtWidgets.QTreeWidgetItem(_groupname)
                    _item.setText(0,names)
            self.DB[_name] = self.USR_DEF[_name]
        finally:
            pass
                    
    def ifbtnDel(self):
        try:
            if self.deleteTree.currentItem().parent():
                if self.deleteTree == self.treeGroup:
                    del self.USR_DEF[self.deleteTree.currentItem().parent().text(0)]
                else:
                    del self.DB[self.deleteTree.currentItem().parent().text(0)]
                self.deleteTree.takeTopLevelItem(self.deleteTree.indexOfTopLevelItem(self.deleteTree.currentItem().parent()))
            else:
                if self.deleteTree == self.treeGroup:
                    del self.USR_DEF[self.deleteTree.currentItem().text(0)]
                else:
                    del self.DB[self.deleteTree.currentItem().text(0)]
                self.deleteTree.takeTopLevelItem(self.deleteTree.indexOfTopLevelItem(self.deleteTree.currentItem()))
            
        finally:
            pass
            
    def ifdelChanged_treeGroup(self):
        self.deleteTree = self.treeGroup
        
    def ifdelChanged_treeWidget(self):
        self.deleteTree = self.treeWidget
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

