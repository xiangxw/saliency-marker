from PyQt5.QtWidgets import QMainWindow, QScrollArea, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt, QCoreApplication, QEvent
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent = None, flags = Qt.WindowFlags()):
        super().__init__(parent, flags)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # image label
        self.ui.imageScrollArea = ImageScrollArea()
        self.ui.imageScrollArea.setBrushWidth(self.ui.brushSizeSpinBox.value())
        self.ui.imageScrollArea.setBrushValue(self.ui.brushValueDoubleSpinBox.value())
        self.ui.imageGroupBoxLayout.addWidget(self.ui.imageScrollArea)

        # signal and slot
        self.ui.openAction.triggered.connect(self.slotOpen)
        self.ui.brushSizeSpinBox.valueChanged.connect(self.ui.imageScrollArea.setBrushWidth)
        self.ui.brushValueDoubleSpinBox.valueChanged.connect(self.ui.imageScrollArea.setBrushValue)

    # open a image file
    def slotOpen(self):
        filename, selectedFilter = QFileDialog.getOpenFileName(self, self.tr('Open File'), '.',
                self.tr('Images (*.png *.jpg *.jpeg *.bmp *.pbm *.pgm *.ppm *.xbm *.xpm)'))
        if filename and len(filename) > 0:
            self.ui.imageScrollArea.open(filename);

    # translate function
    def tr(self, text):
        return QCoreApplication.translate('MainWindow', text)

class ImageScrollArea(QScrollArea):
    def __init__(self, parent = None):
        super().__init__(parent)

        # image label
        self.imageLabel = QLabel()
        self.setWidget(self.imageLabel)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.imageLabel.installEventFilter(self)

        # internal data
        self.scaleToViewport = True
        self.scale = 1.0
        self.originImage = None
        self.scaledImage = None
        self.brushWidth = 1
        self.brushValue = 1
        self.brushColor = Qt.red

    # set brush width
    def setBrushWidth(self, width):
        self.brushWidth = width

    # set brush value
    def setBrushValue(self, value):
        self.brushValue = value

    # open a image file
    def open(self, filename):
        image = QImage(filename)
        if image.isNull():
            QMessageBox.critical(self, self.tr('Error'),
                                 self.tr('Open image file error: %s') % (filename))
        else:
            self.originImage = image
            self.__scaleImageToSize(self.viewport().size())

    # event filter
    def eventFilter(self, watched, event):
        if watched == self.imageLabel:
            if event.type() == QEvent.MouseMove:
                if (event.buttons() & Qt.LeftButton):
                    pixmap = self.imageLabel.pixmap()
                    painter = QPainter()
                    painter.begin(pixmap)
                    painter.fillRect(event.x() - self.brushWidth, event.y() - self.brushWidth,
                            self.brushWidth * 2, self.brushWidth * 2, self.brushColor)
                    painter.end()
                    self.imageLabel.setPixmap(pixmap)
                    return True
        return super().eventFilter(watched, event)

    # viewport event
    def viewportEvent(self, event):
        if event.type() == QEvent.Resize and self.scaleToViewport and \
                self.originImage and (not self.originImage.isNull()):
            self.__scaleImageToSize(event.size())
        elif event.type() == QEvent.Wheel and event.modifiers() == Qt.ControlModifier:
            numPixels = event.pixelDelta()
            numDegrees = event.angleDelta() / 8
            if (not numPixels.isNull()):
                self.__zoom(numPixels.y() / 30) # not sure for this
            elif (not numDegrees.isNull()):
                self.__zoom(numDegrees.y() / 15)
        return super().viewportEvent(event)

    # zoom
    def __zoom(self, step):
        scale = self.scale + 0.1 * step
        if scale > 0:
            self.scaleToViewport = False
            self.__scaleImage(scale)

    # scale image
    def __scaleImage(self, scale):
        self.scale = scale
        self.scaledImage = self.originImage.scaled(self.scale * self.originImage.width(),
                                                   self.scale * self.originImage.height())
        self.imageLabel.setPixmap(QPixmap.fromImage(self.scaledImage))
        self.imageLabel.resize(self.imageLabel.sizeHint())
        self.__updateStatusBar()

    # scale image
    def __scaleImageToSize(self, size):
        widthScale = size.width() / self.originImage.width()
        heightScale = size.height() / self.originImage.height()
        scale = min(widthScale, heightScale)
        if scale > 1:
            scale = 1
        self.__scaleImage(scale)

    # update status bar
    def __updateStatusBar(self):
        self.window().statusBar().showMessage(self.tr('Origin image size: (%d, %d), scale: %f')
                % (self.originImage.width(), self.originImage.height(), self.scale))

    # clear status bar
    def __clearStatusBar(self):
        self.window().statusBar().showMessage(self.tr('No image'))

    # translate function
    def tr(self, text):
        return QCoreApplication.translate('ImageScrollArea', text)
