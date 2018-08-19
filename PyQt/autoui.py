# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 485)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 251, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.image = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.image.setContentsMargins(0, 0, 0, 0)
        self.image.setObjectName("image")
        self.imageshow = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.imageshow.setText("")
        self.imageshow.setObjectName("imageshow")
        self.image.addWidget(self.imageshow)
        self.selectfile = QtWidgets.QPushButton(Form)
        self.selectfile.setGeometry(QtCore.QRect(50, 390, 101, 31))
        self.selectfile.setObjectName("selectfile")
        self.calculate = QtWidgets.QGroupBox(Form)
        self.calculate.setGeometry(QtCore.QRect(500, 20, 151, 181))
        self.calculate.setCheckable(False)
        self.calculate.setObjectName("calculate")
        self.LBP = QtWidgets.QRadioButton(self.calculate)
        self.LBP.setGeometry(QtCore.QRect(20, 40, 89, 16))
        self.LBP.setObjectName("LBP")
        self.SIFT = QtWidgets.QRadioButton(self.calculate)
        self.SIFT.setGeometry(QtCore.QRect(20, 80, 89, 16))
        self.SIFT.setObjectName("SIFT")
        self.SURF = QtWidgets.QRadioButton(self.calculate)
        self.SURF.setGeometry(QtCore.QRect(20, 120, 89, 16))
        self.SURF.setObjectName("SURF")
        self.ORB = QtWidgets.QRadioButton(self.calculate)
        self.ORB.setGeometry(QtCore.QRect(20, 160, 89, 16))
        self.ORB.setObjectName("ORB")
        self.background = QtWidgets.QGroupBox(Form)
        self.background.setGeometry(QtCore.QRect(350, 20, 120, 181))
        self.background.setObjectName("background")
        self.complex = QtWidgets.QRadioButton(self.background)
        self.complex.setGeometry(QtCore.QRect(20, 50, 89, 16))
        self.complex.setObjectName("complex")
        self.radioButton_2 = QtWidgets.QRadioButton(self.background)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 90, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.run = QtWidgets.QCommandLinkButton(Form)
        self.run.setGeometry(QtCore.QRect(350, 220, 301, 51))
        self.run.setObjectName("run")
        self.exit = QtWidgets.QCommandLinkButton(Form)
        self.exit.setGeometry(QtCore.QRect(480, 430, 172, 41))
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "非接触式掌纹识别软件"))
        self.selectfile.setText(_translate("Form", "打开"))
        self.calculate.setTitle(_translate("Form", "匹配识别算法选择"))
        self.LBP.setText(_translate("Form", "LBP"))
        self.SIFT.setText(_translate("Form", "SIFT"))
        self.SURF.setText(_translate("Form", "SURF"))
        self.ORB.setText(_translate("Form", "ORB"))
        self.background.setTitle(_translate("Form", "背景选择"))
        self.complex.setText(_translate("Form", "复杂背景"))
        self.radioButton_2.setText(_translate("Form", "单一背景"))
        self.run.setText(_translate("Form", "开始运行"))
        self.exit.setText(_translate("Form", "返回"))

