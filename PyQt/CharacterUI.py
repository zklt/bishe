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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 281, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectshow = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.selectshow.setText("")
        self.selectshow.setObjectName("selectshow")
        self.horizontalLayout.addWidget(self.selectshow)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(370, 30, 251, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 420, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.ORB = QtWidgets.QPushButton(Form)
        self.ORB.setGeometry(QtCore.QRect(180, 420, 111, 41))
        self.ORB.setObjectName("ORB")
        self.SURF = QtWidgets.QPushButton(Form)
        self.SURF.setGeometry(QtCore.QRect(60, 370, 111, 41))
        self.SURF.setObjectName("SURF")
        self.openfile = QtWidgets.QPushButton(Form)
        self.openfile.setGeometry(QtCore.QRect(70, 320, 81, 31))
        self.openfile.setObjectName("openfile")
        self.saveimg = QtWidgets.QPushButton(Form)
        self.saveimg.setGeometry(QtCore.QRect(200, 320, 81, 31))
        self.saveimg.setObjectName("saveimg")
        self.backface = QtWidgets.QCommandLinkButton(Form)
        self.backface.setGeometry(QtCore.QRect(520, 430, 172, 41))
        self.backface.setObjectName("backface")
        self.ORB_2 = QtWidgets.QPushButton(Form)
        self.ORB_2.setGeometry(QtCore.QRect(180, 370, 111, 41))
        self.ORB_2.setObjectName("ORB_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "非接触式掌纹识别系统"))
        self.pushButton.setText(_translate("Form", "SIFT"))
        self.ORB.setText(_translate("Form", "ORB"))
        self.SURF.setText(_translate("Form", "SURF"))
        self.openfile.setText(_translate("Form", "打开"))
        self.saveimg.setText(_translate("Form", "保存"))
        self.backface.setText(_translate("Form", "返回"))
        self.ORB_2.setText(_translate("Form", "LBP"))

