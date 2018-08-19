from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
import roiui
import cv2
import CVImageToPixmap
import utils
import CharacterWindow
from PyQt5.QtCore import Qt
import numpy as np
import math
import os
from PyQt5 import QtGui
import autoui
import  time

class autorunWindow(QWidget):
    def __init__(self, p):
        super(autorunWindow, self).__init__(p)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./bg3.jpg').scaled(698, 485)))  # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)
        self.ui = autoui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.exit.clicked.connect(self.backfaceButton)
        self.ui.run.clicked.connect(self.runscript)
        self.ui.selectfile.clicked.connect(self.selectfile)
        self.__simpleImage = None
        self.__readImage = None
        self.temp = None

    def selectfile(self):
        path = QFileDialog.getOpenFileName(parent=self, caption="Open File", directory="./Images/resize",filter="*.jpg *.png")
        self.temp = path[0]
        self.__readImage = cv2.imread(path[0])
        self.ui.imageshow.setScaledContents(True)
        if self.__readImage is not None:
            self.ui.imageshow.setPixmap(CVImageToPixmap.convert(self.__readImage))

    def backfaceButton(self):
        self.close()

    def runscript(self):
        single = self.ui.radioButton_2.isChecked()
        complex = self.ui.complex.isChecked()
        lbp = self.ui.LBP.isChecked()
        sift = self.ui.SIFT.isChecked()
        surf = self.ui.SURF.isChecked()
        orb = self.ui.ORB.isChecked()
        mode = [single, complex]
        handles = [lbp, sift, surf, orb]
        handles_str = ["lbp", 'sift', 'surf', 'orb']
        for i, m in enumerate(mode):
            for j, h in enumerate(handles):
                finded = False
                if m and h:
                    self.__simpleImage = self.__readImage
                    if self.__simpleImage is not None:
                        roitime = time.time()
                        self.__simpleImage = utils.hand2(self.__simpleImage)
                        roitime = time.time() - roitime
                        self.__simpleImage = cv2.resize(self.__simpleImage, (279, 279), interpolation=cv2.INTER_CUBIC)
                        #pipeitime = time.time()
                        QMessageBox.about(self, "输出", '感兴趣区域提取用时:  {0:.2f}'.format(roitime) + '秒')
                        c = CharacterWindow.CharacterWindow(self)
                        c.readImage = self.__simpleImage
                        if j == 0:
                            c.lbp()
                        else:
                            c.run(handles_str[j])()
                    finded = True
                if finded: break
