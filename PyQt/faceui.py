# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(698, 485)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 291, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ImageView = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ImageView.setContentsMargins(0, 0, 0, 0)
        self.ImageView.setObjectName("ImageView")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 30, 301, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.ImageShow = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ImageShow.setText("")
        self.ImageShow.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageShow.setObjectName("ImageShow")
        self.vboxlayout.addWidget(self.ImageShow)
        self.pushButtonopen = QtWidgets.QPushButton(Form)
        self.pushButtonopen.setGeometry(QtCore.QRect(50, 330, 111, 41))
        self.pushButtonopen.setObjectName("pushButtonopen")
        self.pushButtoncapture = QtWidgets.QPushButton(Form)
        self.pushButtoncapture.setGeometry(QtCore.QRect(190, 330, 111, 41))
        self.pushButtoncapture.setObjectName("pushButtoncapture")
        self.pushButtonsave = QtWidgets.QPushButton(Form)
        self.pushButtonsave.setGeometry(QtCore.QRect(50, 390, 111, 41))
        self.pushButtonsave.setObjectName("pushButtonsave")
        self.pushButtonexit = QtWidgets.QPushButton(Form)
        self.pushButtonexit.setGeometry(QtCore.QRect(190, 390, 111, 41))
        self.pushButtonexit.setObjectName("pushButtonexit")
        self.ROI = QtWidgets.QCommandLinkButton(Form)
        self.ROI.setGeometry(QtCore.QRect(380, 330, 172, 41))
        self.ROI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ROI.setAutoFillBackground(False)
        self.ROI.setObjectName("ROI")
        self.lbp = QtWidgets.QCommandLinkButton(Form)
        self.lbp.setGeometry(QtCore.QRect(510, 330, 172, 41))
        self.lbp.setObjectName("lbp")
        self.sift = QtWidgets.QCommandLinkButton(Form)
        self.sift.setGeometry(QtCore.QRect(380, 390, 172, 41))
        self.sift.setObjectName("sift")
        self.database = QtWidgets.QCommandLinkButton(Form)
        self.database.setGeometry(QtCore.QRect(510, 390, 172, 41))
        self.database.setObjectName("database")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonopen.setText(_translate("Form", "open"))
        self.pushButtoncapture.setText(_translate("Form", "capture"))
        self.pushButtonsave.setText(_translate("Form", "save"))
        self.pushButtonexit.setText(_translate("Form", "exit"))
        self.ROI.setText(_translate("Form", "ROI提取"))
        self.lbp.setText(_translate("Form", "特征提取"))
        self.sift.setText(_translate("Form", "识别"))
        self.database.setText(_translate("Form", "db"))

