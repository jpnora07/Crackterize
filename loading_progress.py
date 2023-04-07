from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QDesktopWidget

class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, flags=Qt.FramelessWindowHint)

        self.setGeometry(0, 0, 100, 100)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: transparent;")
        # create the QLabel widget with the QMovie
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 100, 100)
        self.label.setScaledContents(True)
        self.movie = QMovie("images/load_bg.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # center the dialog
        self.center()

    def center(self):
        # get the screen resolution
        screen_resolution = QDesktopWidget().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()

        # move the dialog to the center of the screen
        self.move((width - self.width()) // 2, (height - self.height()) // 2)

if __name__ == '__main__':
    app = QApplication([])
    dialog = LoadingDialog()
    dialog.exec_()
