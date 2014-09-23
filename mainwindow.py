from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # image label
        self.ui.imageLabel = ImageLabel()
        self.ui.imageLabel.setPixmap(QPixmap.fromImage(QImage('data/a2.png').scaled(640, 480)))
        self.ui.imageLayout.addWidget(self.ui.imageLabel)

class ImageLabel(QLabel):
    def __init__(self, brushWidth = 1, brushValue = 1):
        super(ImageLabel, self).__init__()

        self.brushWidth = brushWidth
        self.brushValue = brushValue

    def setBrushWidth(self, width):
        self.brushWidth = width

    def setBrushValue(self, value):
        self.brushValue = value

    def mouseMoveEvent(self, event):
        super(ImageLabel, self).mouseMoveEvent(event)
