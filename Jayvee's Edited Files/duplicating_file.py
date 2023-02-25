import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

class MyButton(QPushButton):
    def __init__(self, parent=None):
        super(MyButton, self).__init__(parent)
        self.clicked.connect(self.duplicate)

    def duplicate(self):
        new_button = MyButton(self.parent())
        new_button.setIcon(self.icon())
        new_button.setGeometry(self.geometry().translated(20, 20))
        new_button.show()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        # Load the image
        pixmap = QPixmap('add_folder.png')

        # Create the button and set its properties
        button = MyButton(self)
        button.setIcon(QIcon(pixmap))
        button.setIconSize(pixmap.size())
        button.setToolTip('Click to duplicate')
        hbox.addWidget(button)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Image Button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
