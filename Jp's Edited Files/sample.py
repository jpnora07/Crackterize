from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint, QRect


class ImageCropper(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.crop_start = QPoint()
        self.crop_end = QPoint()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Image Cropper')

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, 800, 600)

        self.btn_open = QPushButton('Open', self)
        self.btn_open.setGeometry(10, 10, 60, 30)
        self.btn_open.clicked.connect(self.openImage)

        self.btn_crop = QPushButton('Crop', self)
        self.btn_crop.setGeometry(80, 10, 60, 30)
        self.btn_crop.clicked.connect(self.cropImage)

    def openImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', 'Image files (*.jpg *.gif *.png)')
        if fname:
            self.image = QPixmap(fname)
            scaled_image = self.image.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio)
            self.image = scaled_image
            self.label.setPixmap(self.image)
            self.repaint()

    def mousePressEvent(self, event):
        if self.image:
            if event.button() == Qt.LeftButton:
                self.crop_start = event.pos()

    def mouseMoveEvent(self, event):
        if self.image:
            if event.buttons() & Qt.LeftButton:
                self.crop_end = event.pos()
                self.repaint()

    def mouseReleaseEvent(self, event):
        if self.image:
            if event.button() == Qt.LeftButton:
                self.crop_end = event.pos()
                self.repaint()

    def paintEvent(self, event):
        if self.image:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self.image)

            if not self.crop_start.isNull() and not self.crop_end.isNull():
                rect = self.getRect()
                painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
                painter.drawRect(rect)

    def getRect(self):
        x1 = min(self.crop_start.x(), self.crop_end.x())
        y1 = min(self.crop_start.y(), self.crop_end.y())
        x2 = max(self.crop_start.x(), self.crop_end.x())
        y2 = max(self.crop_start.y(), self.crop_end.y())
        return QRect(x1, y1, x2-x1, y2-y1)

    def cropImage(self):
        if self.image:
            rect = self.getRect()
            cropped = self.image.copy(rect)
            cropped.save('cropped.png')
            self.image = None
            self.label.clear()
            self.repaint()

if __name__ == '__main__':
    app = QApplication([])
    window = ImageCropper()
    window.show()
    app.exec_()
