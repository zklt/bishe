from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import roiui
import cv2
import CVImageToPixmap
import utils
import CharacterWindow
from PyQt5.QtCore import Qt
import numpy as np
import math

class RoiWindow(QWidget):
    def __init__(self, p):
        super(RoiWindow, self).__init__(p)
        self.ui = roiui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.backface.clicked.connect(self.backfaceButton)
        self.ui.single.clicked.connect(self.simple)
        self.ui.selectfile.clicked.connect(self.selectfile)
        self.ui.savefile.clicked.connect(self.savefile)
        self.ui.complex.clicked.connect(self.complex1)
        self.ui.tezhengtiqu.clicked.connect(self.tztqButton)
        self.__simpleImage = None
        self.__readImage = None

    def savefile(self):
        path = QFileDialog.getSaveFileName(parent=self, caption="Save File", directory=".", filter="*.jpg")
        if self.__simpleImage is not None and path and path[0] != '':
            cv2.imwrite(path[0], self.__simpleImage)
    def selectfile(self):
        path = QFileDialog.getOpenFileName(parent=self, caption="Open File", directory=".", filter="*.jpg *.png")
        self.__readImage = cv2.imread(path[0])
        self.ui.image1.setScaledContents(True)
        if self.__readImage is not None:
            self.ui.image1.setPixmap(CVImageToPixmap.convert(self.__readImage))
    def simple(self):
        self.__simpleImage = self.__readImage
        if self.__simpleImage is not None:
            self.__simpleImage = utils.process_image(self.__simpleImage)
            self.ui.image2.setPixmap(CVImageToPixmap.convert(self.__simpleImage))
            self.ui.image2.setScaledContents(True)

    def backfaceButton(self):
        self.close()

    def tztqButton(self):
        characterWindow = CharacterWindow.CharacterWindow(self)
        characterWindow.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        characterWindow.setWindowModality(Qt.WindowModal)
        characterWindow.show()

    def complex1(self):
        self.__simpleImage = self.__readImage
        if self.__simpleImage is not None:
            self.__simpleImage = utils.hand2(self.__simpleImage)
            self.ui.image2.setPixmap(CVImageToPixmap.convert(self.__simpleImage))
            self.ui.image2.setScaledContents(True)