# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shut.ui'
#
# Created: Mon Mar 20 18:10:31 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_shut(object):
    flag = True
    def setupUi(self, shut):
        shut.setObjectName("shut")
        shut.resize(411, 170)
        shut.setFixedSize(411,170)
        self.label = QtWidgets.QLabel(shut)
        self.label.setGeometry(QtCore.QRect(40, 50, 41, 51))
        self.label.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(shut)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 71, 41))
        self.lineEdit.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(shut)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 31, 31))
        self.label_2.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(shut)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 50, 71, 41))
        self.lineEdit_2.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(shut)
        self.label_3.setGeometry(QtCore.QRect(260, 60, 31, 31))
        self.label_3.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(shut,clicked=self.sd)
        self.pushButton.setGeometry(QtCore.QRect(290, 50, 101, 41))
        self.pushButton.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(shut)
        self.label_4.setGeometry(QtCore.QRect(0, 120, 411, 31))
        self.label_4.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.label_4.setObjectName("label_4")
        
        self.retranslateUi(shut)
        QtCore.QMetaObject.connectSlotsByName(shut)

    def retranslateUi(self, shut):
        _translate = QtCore.QCoreApplication.translate
        shut.setWindowTitle(_translate("shut", "Auto Shutdown by dearvee"))
        self.label.setText(_translate("shut", "At："))
        self.label_2.setText(_translate("shut", "H"))
        self.label_3.setText(_translate("shut", "M"))
        self.label_4.setText(_translate("shut", "Please input time of shutdown~"))
        self.pushButton.setText(_translate("shut", "Set"))

    def sd(self,shut):
        h = self.lineEdit.text()
        m = self.lineEdit_2.text()
        if self.flag:
            self.flag = False
            try:
                os.popen('at '+h+':'+m+' shutdown -s')
                self.label_4.setText('Success! the system will shutdown at today '+h+':'+m+'.')
                self.pushButton.setText('Remove all')
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            except:
                self.label_4.setText('Something is wrong~')
        else:
            self.flag = True
            try:
                os.popen('at /delete /yes')
                self.label_4.setText('Success! already removed~')
                self.pushButton.setText('Set')
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            except:
                self.label_4.setText('Something is wrong~')
        
if __name__ == '__main__':   
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_shut()
    ui.setupUi(Form) 
    Form.show()
    sys.exit(app.exec_())
