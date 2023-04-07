from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QDialog, QLabel

class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Loading...')
        self.setGeometry(100, 100, 200, 200)

        # create the QLabel widget with the QMovie
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 200, 200)
        self.movie = QMovie("../images/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

if __name__ == '__main__':
    app = QApplication([])
    dialog = LoadingDialog()
    dialog.exec_()
