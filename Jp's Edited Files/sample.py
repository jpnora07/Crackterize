import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QtWidgets.QPushButton("Click me", self)
        button.clicked.connect(self.show_dialog)
        button.move(50, 50)

        self.setWindowTitle("Dialog Example")
        self.show()

    def show_dialog(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle("Dialog")
        dialog.setText("This is a dialog")
        dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
