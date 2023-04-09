from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QDesktopWidget

class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, flags=Qt.FramelessWindowHint)

        self.setGeometry(0, 0, 300, 200)
        self.setStyleSheet("background-color: #ffffff;")

        # create the new QLabel widget and set its properties
        self.label_top = QLabel(self)
        self.label_top.setText("Top Label")
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setGeometry(0, 0, 100, 20)

        # create the QLabel widget with the QMovie and set its properties
        self.label = QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(0, 20, 100, 100)
        self.label.setScaledContents(True)

        self.movie = QMovie("../images/spin_loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # get the center position of the dialog
        center_pos = self.frameGeometry().center()

        # get the center position of the label_top
        label_top_pos = self.label_top.frameGeometry().center()

        # calculate the position to move the label_top to the center of the dialog
        move_top_pos = center_pos - label_top_pos

        # get the center position of the label
        label_pos = self.label.frameGeometry().center()

        # calculate the position to move the label to the center of the dialog
        move_pos = center_pos - label_pos

        # move the label_top to the center position
        self.label_top.move(move_top_pos)

        # set the alignment of the label text to the center
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)

        # move the label to the center position
        self.label.move(move_pos)

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
