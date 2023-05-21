from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)
        self.maximizeButton = QPushButton('Maximize', self)
        self.maximizeButton.clicked.connect(self.maximizeDialog)
        self.setCentralWidget(self.maximizeButton)

    def maximizeDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Dialog')
        dialog.setLayout(QVBoxLayout())
        dialog.layout().addWidget(QPushButton('Close', dialog))
        dialog.layout().addWidget(QPushButton('Center', dialog))
        dialog.show()

        if self.isMaximized():
            desktop = QApplication.desktop()
            screenRect = desktop.availableGeometry(desktop.primaryScreen())
            dialog.move(screenRect.center() - dialog.rect().center())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
