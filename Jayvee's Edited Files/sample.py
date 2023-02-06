import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

class UploadImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # initialize the UI elements
        self.button = QPushButton("Upload Image", self)
        self.button.clicked.connect(self.upload_image)
        self.image_label = QLabel(self)

        # set the layout
        self.button.move(100, 50)
        self.image_label.move(250, 250)

        # set the window properties
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Upload Image")
        self.show()

    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Images (*.png *.xpm *.jpg *.bmp *.gif *.jpeg)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UploadImageWindow()
    sys.exit(app.exec_())
