import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class RoundedButton(QPushButton):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 50, 50)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)
        self.button = RoundedButton('Rounded Button', self)
        self.button.setGeometry(100, 100, 100, 40)
        self.button.setStyleSheet("background-color: blue; color: white")
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("Button clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())