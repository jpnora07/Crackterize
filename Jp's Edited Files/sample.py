import os
import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from image_cropping import ImageCropWidget

# Assuming that the Django project root is one level above the current directory
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing the necessary Django models
from myapp.models import MyModel

class MainWindow(QLabel):
    def __init__(self):
        super().__init__()

        # Creating an instance of the ImageCropWidget and adding it to the window
        self.crop_widget = ImageCropWidget()
        self.crop_widget.setParent(self)

        # Loading an image and setting it in the crop widget
        self.image_path = '../10cm.jpg'
        self.pixmap = QPixmap(self.image_path)
        self.crop_widget.set_image(self.pixmap)

        # Setting the window properties
        self.setWindowTitle("Image Cropping")
        self.setGeometry(100, 100, 800, 600)
        self.setScaledContents(True)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
