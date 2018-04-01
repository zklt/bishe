# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'character.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(698, 482)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 311, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectshow = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.selectshow.setText("")
        self.selectshow.setObjectName("selectshow")
        self.horizontalLayout.addWidget(self.selectshow)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(370, 30, 311, 261))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 310, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.ORB = QtWidgets.QPushButton(Form)
        self.ORB.setGeometry(QtCore.QRect(310, 370, 111, 41))
        self.ORB.setObjectName("ORB")
        self.SURF = QtWidgets.QPushButton(Form)
        self.SURF.setGeometry(QtCore.QRect(310, 310, 111, 41))
        self.SURF.setObjectName("SURF")
        self.LDP = QtWidgets.QPushButton(Form)
        self.LDP.setGeometry(QtCore.QRect(180, 370, 111, 41))
        self.LDP.setObjectName("LDP")
        self.openfile = QtWidgets.QPushButton(Form)
        self.openfile.setGeometry(QtCore.QRect(50, 320, 81, 31))
        self.openfile.setObjectName("openfile")
        self.saveimg = QtWidgets.QPushButton(Form)
        self.saveimg.setGeometry(QtCore.QRect(50, 380, 81, 31))
        self.saveimg.setObjectName("saveimg")
        self.savedb = QtWidgets.QCommandLinkButton(Form)
        self.savedb.setGeometry(QtCore.QRect(520, 380, 172, 41))
        self.savedb.setObjectName("savedb")
        self.backface = QtWidgets.QCommandLinkButton(Form)
        self.backface.setGeometry(QtCore.QRect(520, 430, 172, 41))
        self.backface.setObjectName("backface")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "SIFT"))
        self.ORB.setText(_translate("Form", "ORB"))
        self.SURF.setText(_translate("Form", "SURF"))
        self.LDP.setText(_translate("Form", "LDP"))
        self.openfile.setText(_translate("Form", "打开"))
        self.saveimg.setText(_translate("Form", "保存"))
        self.savedb.setText(_translate("Form", "savedb"))
        self.backface.setText(_translate("Form", "back"))

