import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

from Home import Ui_MainWindow


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Crackterize')
        self.setFixedSize(900, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300  # total instance

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        # Add image/logo
        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')
        pixmap = QPixmap('images/Crackterize.png')
        scaled_pixmap = pixmap.scaled(700, 900, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.labelTitle.setPixmap(scaled_pixmap)
        self.labelTitle.setGeometry(1000, 1000, scaled_pixmap.width(), scaled_pixmap.height())

        # center labels
        self.labelTitle.resize(self.width() - 10, 460)
        self.labelTitle.move(0, 50)  # x, y
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 30, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('')
        self.labelDescription.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(500, 12)  # Change the width to 100 pixels
        self.progressBar.move(200, self.labelDescription.y() + -138)
        self.progressBar.setStyleSheet('QProgressBar {border-radius: 400px; padding: 9px; text-align: center;}')
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(10, self.n)
        self.progressBar.setValue(20)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 0)
        self.labelLoading.move(20, self.progressBar.y() + 100)
        self.labelLoading.setObjectName(' ')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText(' ')

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.3):
            self.labelDescription.setText('')
        elif self.counter == int(self.n * 0.6):
            self.labelDescription.setText('')
        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)
            try:
                # Create an instance of the main window and show it
                main_window = QtWidgets.QMainWindow()
                ui = Ui_MainWindow()
                ui.setupUi(main_window)

                # Show the main window
                main_window.show()

            except Exception as e:
                print(e)

        self.counter += 1

if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        #LabelDesc {
            font-size: 5px;
            color: #e9d4cc;
        }

        #LabelLoading {
            font-size: 5px;
            color: #e9d4cc;
        }

        QFrame {
            background-color: #f3e9e2;
            color: rgb(222,193,179);
        }

        QProgressBar {

        background-color: #e9d4cc;
            color: rgb(200, 200, 200);
            border-style: none;
            border-radius: 5px;
            text-align: center;
            font-size: 5px;
        }

        QProgressBar::chunk {
            border-radius: 2px;
            background-color: #8c643b;
        }
    ''')

    splash = SplashScreen()
    splash.show()
    pixmap = splash.grab()

    # Save the screenshot to a file
    pixmap.save("splash.png")

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
