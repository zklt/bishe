from PyQt5.QtGui import QImage, QPixmap
import cv2
import os

def convert(cv_image):
    cv2.imwrite("tmp.jpg", cv_image)
    ret = QPixmap()
    if ret.load("tmp.jpg"):
        return ret

if __name__ == '__main__':
    i = cv2.imread("a.jpg")
    print(convert(i) is None)
