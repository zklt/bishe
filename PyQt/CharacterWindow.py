from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
import CharacterUI
import cv2
import CVImageToPixmap
import utils
import os
from PyQt5 import QtGui
import time
import newLBP
from numbers import *
import re
import numpy as np

class CharacterWindow(QWidget):

    def __init__(self, p):
        super(CharacterWindow, self).__init__(p)
        palette1 = QtGui.QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./bg3.jpg').scaled(698, 485)))  # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)
        self.ui = CharacterUI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ORB.clicked.connect(self.run("orb"))
        self.ui.SURF.clicked.connect(self.run("surf"))
        self.ui.pushButton.clicked.connect(self.run("sift"))
        self.ui.ORB_2.clicked.connect(self.lbp)
        self.ui.openfile.clicked.connect(self.selectfile)
        self.ui.saveimg.clicked.connect(self.savefile)
        self.ui.backface.clicked.connect(self.backfaceButton)
        self.__simpleImage = None
        self.readImage = None
        self.path = None
        self.kv = {'chenfan':'陈凡', 'ciren':'次仁', 'huangcanming':'黄灿铭', 'lishaokai':'李韶凯', 'zhasen':'查森', 'zhangke':'张可', 'renbin':'任昺', 'morongwei':'莫镕蔚', 'maixiongjie':'麦雄杰', 'kade':'卡德', 'zhangwei':'张伟', 'linweihao':'林炜豪', 'panqiu':'潘秋', 'sunkailai':'孙开来', 'wenjialin':'温佳琳', 'xuguanghui':'徐光辉', 'wujunqiang':'吴俊强', 'yangshaobo':'杨少博', 'yinweimin':'尹卫民', 'zhaole':'赵乐'}


    def selectfile(self):
        self.path = QFileDialog.getOpenFileName(parent=self, caption="Open File", directory="./Images/testroi", filter="*.jpg *.png")
        self.readImage = cv2.imread(self.path[0])
        self.ui.selectshow.setScaledContents(True)
        if self.readImage is not None:
            self.ui.selectshow.setPixmap(CVImageToPixmap.convert(self.readImage))

    def savefile(self):
        path = QFileDialog.getSaveFileName(parent=self, caption="Save File", directory=".", filter="*.jpg")
        if self.__simpleImage is not None and path and path[0] != '':
            cv2.imwrite(path[0], self.__simpleImage)

    def backfaceButton(self):
        self.close()

    def run(self, type):
        def ret():
            files = os.listdir("./Images/roi")
            start = time.time()
            if type == "orb":
                f = self.orb
            elif type == "sift":
                f = self.sift
            elif type == "surf":
                f = self.surf
            res = 99999999
            name = None
            for i in files:
                img = cv2.imread("./Images/roi/" + i)
                #img = utils.hand2(img)
                # cv2.imwrite("pipei.jpg", img)
                # img = cv2.imread("pipei.jpg")

                res_ = f(img)
                res_ = res_ if res_ is not None else 9999999
                name = name if res_ > res else i
                res = res if res_ > res else res_
            if name is not None:
                stop = time.time()
                runtime = stop - start
                ret = QPixmap()
                ret.load('./Images/' + name)
                self.ui.label_2.setPixmap(ret)
                self.ui.label_2.setScaledContents(True)
                rname = re.sub(r'[0-9].*$', "", name)
                if rname in self.kv.keys():
                    rname = self.kv[rname]
                # QMessageBox.about(self, "掌纹主人的名字为:", rname)
                QMessageBox.about(self, "输出", "掌纹主人的名字为: " + rname + '\n耗时：' + '{0:.2f}'.format(runtime) + '秒')

        return ret

    def orb(self, img):
        if isinstance(self.readImage, np.ndarray):
            src1 = self.readImage.copy()
            return utils.cacORBFeatureSAndCompare(src1, img)
        else:
            print("读取图片为NONE")
        # img = cv2.Canny(img, 40, 50)
        # src1 = cv2.Canny(src1, 40, 50)

    def sift(self, img):
        if isinstance(self.readImage, np.ndarray):
            src1 = self.readImage.copy()
            return utils.cacSIFTFeatureAndCompare(src1, img)
        else:
            print("读取图片为NONE")
        # img = cv2.Canny(img, 40, 50)
        # src1 = cv2.Canny(src1, 40, 50)


    def surf(self, img):
        if isinstance(self.readImage, np.ndarray):
            src1 = self.readImage.copy()
            return utils.cacSURFFeatureAndCompare(src1, img, 5)
        else:
            print("读取图片为NONE")
        # img = cv2.Canny(img, 40, 50)
        # src1 = cv2.Canny(src1, 40, 50)

    def lbp(self):
        result = newLBP.inf
        with open("allLBPoperator", "rb") as f:
            allLBPoperator = newLBP.pickle.load(f)
        with open("allexHistograms", "rb") as f:
            allexHistograms = newLBP.pickle.load(f)
        with open("names", "rb") as f:
            names = newLBP.pickle.load(f)
        src1 = None
        if isinstance(self.readImage, np.ndarray):
            src1 = self.readImage.copy()
            src1 = cv2.cvtColor(src1, cv2.COLOR_RGB2GRAY)
            # runLBP(allTuPianPath, src1)
            start1 = time.time()
            for i in range(len(allLBPoperator)):
                jresult, i = newLBP.judgePalm(newLBP.mat(src1).flatten(), allLBPoperator[i], allexHistograms[i])
                realname = re.sub(r'[0-9].*$', "", names[i])
                stop1 = time.time()
                runtime1 = stop1 - start1
                rname = "Unknow"
                if realname in self.kv.keys():
                    rname = self.kv[realname]
                # QMessageBox.about(self, "掌纹主人的名字为:", realname)
                QMessageBox.about(self, "输出", "掌纹主人的名字为: " + rname + '\n耗时：' + '{0:.2f}'.format(runtime1) + '秒')
        else:
            print("读取图片为NONE")


