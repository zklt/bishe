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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 251, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ImageView = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ImageView.setContentsMargins(0, 0, 0, 0)
        self.ImageView.setObjectName("ImageView")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 30, 251, 331))
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
        self.pushButtonopen.setGeometry(QtCore.QRect(50, 370, 111, 41))
        self.pushButtonopen.setObjectName("pushButtonopen")
        self.pushButtoncapture = QtWidgets.QPushButton(Form)
        self.pushButtoncapture.setGeometry(QtCore.QRect(190, 370, 111, 41))
        self.pushButtoncapture.setObjectName("pushButtoncapture")
        self.pushButtonsave = QtWidgets.QPushButton(Form)
        self.pushButtonsave.setGeometry(QtCore.QRect(50, 430, 111, 41))
        self.pushButtonsave.setObjectName("pushButtonsave")
        self.pushButtonexit = QtWidgets.QPushButton(Form)
        self.pushButtonexit.setGeometry(QtCore.QRect(190, 430, 111, 41))
        self.pushButtonexit.setObjectName("pushButtonexit")
        self.ROI = QtWidgets.QCommandLinkButton(Form)
        self.ROI.setGeometry(QtCore.QRect(450, 380, 172, 41))
        self.ROI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ROI.setAutoFillBackground(False)
        self.ROI.setObjectName("ROI")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(450, 430, 172, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "非接触式掌纹识别系统"))
        self.pushButtonopen.setText(_translate("Form", "打开摄像头"))
        self.pushButtoncapture.setText(_translate("Form", "拍照"))
        self.pushButtonsave.setText(_translate("Form", "保存"))
        self.pushButtonexit.setText(_translate("Form", "退出摄像头"))
        self.ROI.setText(_translate("Form", "感兴趣区域提取"))
        self.commandLinkButton.setText(_translate("Form", "自动运行"))

