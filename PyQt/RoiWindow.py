from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QImage
import roiui
import  cv2
import CVImageToPixmap
import utils

class RoiWindow(QWidget):
    def __init__(self, p):
        super(RoiWindow, self).__init__(p)
        self.ui = roiui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.backface.clicked.connect(self.backfaceButton)
        self.ui.pushButton_2.clicked.connect(self.simple)

    def simple(self):
        a = cv2.imread('a.jpg')
        a = utils.process_image(a)
        self.ui.image2.setPixmap(CVImageToPixmap.convert(a))

    def backfaceButton(self):
        self.close()

    def usecanny(self):
        img = cv2.imread("./aaa.jpg", 0)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        canny = cv2.Canny(img, 20, 50)
        cv2.imshow('Canny', canny)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
