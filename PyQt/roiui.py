# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 473)
        self.selectfile = QtWidgets.QPushButton(Form)
        self.selectfile.setGeometry(QtCore.QRect(40, 340, 75, 23))
        self.selectfile.setObjectName("selectfile")
        self.savefile = QtWidgets.QPushButton(Form)
        self.savefile.setGeometry(QtCore.QRect(40, 380, 75, 23))
        self.savefile.setObjectName("savefile")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 281, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.selectimage = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.selectimage.setContentsMargins(0, 0, 0, 0)
        self.selectimage.setObjectName("selectimage")
        self.image1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image1.setText("")
        self.image1.setObjectName("image1")
        self.selectimage.addWidget(self.image1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, 30, 281, 261))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.afterroi = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.afterroi.setContentsMargins(0, 0, 0, 0)
        self.afterroi.setObjectName("afterroi")
        self.image2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.image2.setText("")
        self.image2.setObjectName("image2")
        self.afterroi.addWidget(self.image2)
        self.backface = QtWidgets.QCommandLinkButton(Form)
        self.backface.setGeometry(QtCore.QRect(510, 430, 172, 41))
        self.backface.setObjectName("backface")
        self.complex = QtWidgets.QPushButton(Form)
        self.complex.setGeometry(QtCore.QRect(150, 320, 111, 41))
        self.complex.setObjectName("complex")
        self.single = QtWidgets.QPushButton(Form)
        self.single.setGeometry(QtCore.QRect(150, 380, 111, 41))
        self.single.setObjectName("single")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(360, 320, 141, 131))
        self.groupBox.setObjectName("groupBox")
        self.canny = QtWidgets.QPushButton(self.groupBox)
        self.canny.setGeometry(QtCore.QRect(30, 30, 81, 31))
        self.canny.setObjectName("canny")
        self.LOG = QtWidgets.QPushButton(self.groupBox)
        self.LOG.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.LOG.setObjectName("LOG")
        self.tezhengtiqu = QtWidgets.QCommandLinkButton(Form)
        self.tezhengtiqu.setGeometry(QtCore.QRect(510, 390, 172, 41))
        self.tezhengtiqu.setObjectName("tezhengtiqu")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.selectfile.setText(_translate("Form", "打开"))
        self.savefile.setText(_translate("Form", "保存"))
        self.backface.setText(_translate("Form", "返回"))
        self.complex.setText(_translate("Form", "复杂背景提取"))
        self.single.setText(_translate("Form", "单一背景提取"))
        self.groupBox.setTitle(_translate("Form", "边缘检测"))
        self.canny.setText(_translate("Form", "canny算子"))
        self.LOG.setText(_translate("Form", "LOG算子"))
        self.tezhengtiqu.setText(_translate("Form", "特征提取"))

