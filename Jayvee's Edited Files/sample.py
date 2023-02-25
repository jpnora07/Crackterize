from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the size of the widget
        self.setFixedSize(200, 200)

        # Load the image as a QPixmap
        pixmap = QPixmap("my_image.png")

        # Set the background image of the widget using stylesheet
        self.setStyleSheet(f"background-image: url({pixmap});"
                           "background-position: center;"
                           "background-repeat: no-repeat;")


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
