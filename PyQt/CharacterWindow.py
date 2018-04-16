from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import CharacterUI
import cv2
import CVImageToPixmap
import utils
import os


class CharacterWindow(QWidget):
    def __init__(self, p):
        super(CharacterWindow, self).__init__(p)
        self.ui = CharacterUI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ORB.clicked.connect(self.run("orb"))
        self.ui.openfile.clicked.connect(self.selectfile)
        self.ui.saveimg.clicked.connect(self.savefile)
        self.ui.backface.clicked.connect(self.backfaceButton)
        self.__simpleImage = None
        self.__readImage = None

    def selectfile(self):
        path = QFileDialog.getOpenFileName(parent=self, caption="Open File", directory=".", filter="*.jpg *.png")
        self.__readImage = cv2.imread(path[0])
        self.ui.selectshow.setScaledContents(True)
        if self.__readImage is not None:
            self.ui.selectshow.setPixmap(CVImageToPixmap.convert(self.__readImage))

    def savefile(self):
        path = QFileDialog.getSaveFileName(parent=self, caption="Save File", directory=".", filter="*.jpg")
        if self.__simpleImage is not None and path and path[0] != '':
            cv2.imwrite(path[0], self.__simpleImage)

    def backfaceButton(self):
        self.close()

    def run(self, type):
        def ret():
            files = os.listdir("./Images")
            if type == "orb":
                f = self.orb
            elif type == "sift":
                f = self.sift
            elif type == "surf":
                f = self.surf
            elif type == "ldp":
                f = self.ldp
            for i in files:
                img = cv2.imread("./Images/" + i)
                img = utils.process_image(img)
                cv2.imwrite("tmp2.jpg", img)
                img = cv2.imread("tmp2.jpg")

                f(img)

        return ret

    def orb(self, img):
        src1 = self.__readImage
        img = cv2.Canny(img, 40, 50)
        src1 = cv2.Canny(src1, 40, 50)
        print(utils.cacORBFeatureSAndCompare(src1, img))

    def sift(self, img):
        src1 = self.__readImage
        img = cv2.Canny(img, 40, 50)
        src1 = cv2.Canny(src1, 40, 50)
        print(utils.cacSIFTFeatureAndCompare(src1,img))

    def surf(self, img):
        src1 = self.__readImage
        img = cv2.Canny(img, 40, 50)
        src1 = cv2.Canny(src1, 40, 50)
        print(utils.cacSURFFeatureAndCompare(src1,img))

    def ldp(self, img):
        pass
