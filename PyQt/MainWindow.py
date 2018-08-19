from PyQt5.QtWidgets import QWidget, QFileDialog
import faceui
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtMultimedia import QCameraImageCapture
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QDir
import RoiWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import cv2
import autorunWindow

class MainWindow(QWidget):
    def __init__(self, p):
        super(MainWindow, self).__init__(parent=p)
        palette1 = QtGui.QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./bg3.jpg').scaled(698,485)))  # 设置背景图片
        self.setPalette(palette1)
        #self.setWindowIcon(QtGui.QIcon('.‪/icon.ico'))
        self.setAutoFillBackground(True)
        self.ui = faceui.Ui_Form()
        self.ui.setupUi(self)
        self.camera = QCamera(self)
        self.viewfinder = QCameraViewfinder(self)
        self.imageCapture = QCameraImageCapture(self.camera)
        self.ui.ImageView.addWidget(self.viewfinder)
        self.ui.ImageShow.setScaledContents(True)
        self.imageCapture.imageCaptured.connect(self.displayImage)
        self.ui.pushButtonopen.clicked.connect(self.openCamera)
        self.ui.pushButtoncapture.clicked.connect(self.captureImage)
        self.ui.pushButtonsave.clicked.connect(self.saveImage)
        self.ui.pushButtonexit.clicked.connect(self.quitCamera)
        self.ui.ROI.clicked.connect(self.roiButton)
        self.ui.commandLinkButton.clicked.connect(self.autorunbutton)

    def displayImage(self, i: int, image: QImage):
        self.ui.ImageShow.setPixmap(QPixmap().fromImage(image))

    def openCamera(self):
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

    def captureImage(self):
        self.imageCapture.capture()

    def saveImage(self):
        fileName = QFileDialog.getSaveFileName(self, "save file", "./Images/paizhao", "jpegfile(*.jpg)")
        pixmap = self.ui.ImageShow.pixmap()
        if pixmap is not None:
            pixmap.save(fileName[0])

    def quitCamera(self):
        self.camera.stop()

    def roiButton(self):
        roiWindow = RoiWindow.RoiWindow(self)
        roiWindow.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        roiWindow.setWindowModality(Qt.WindowModal)
        roiWindow.show()

    def autorunbutton(self):
        import autorunWindow
        autorunWindow = autorunWindow.autorunWindow(self)
        autorunWindow.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        autorunWindow.setWindowModality(Qt.WindowModal)
        autorunWindow.show()
