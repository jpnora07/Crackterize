from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.addNewRowLayout()

        self.setGeometry(200, 100, 300, 200)
        self.setWindowTitle("Folder")
        self.show()

    def addNewRowLayout(self):
        self.row_layout = QHBoxLayout()
        self.main_layout.addLayout(self.row_layout)

        self.addButton = QPushButton( self.central_widget)
        self.addButton.clicked.connect(self.addNewButton)
        self.addButton.setIcon(QIcon("../images/add_folder.png"))
        self.addButton.setFixedSize(32, 32)
        self.row_layout.addWidget(self.addButton)

    def addNewButton(self):
        new_button = QPushButton(self.central_widget)
        new_button.clicked.connect(self.deleteButton)

        if self.row_layout.count() >= 5:
            self.addNewRowLayout()

        self.row_layout.addWidget(new_button)

    def deleteButton(self):
        sender_button = self.sender()
        sender_layout = sender_button.parent()
        sender_layout.removeWidget(sender_button)
        sender_button.deleteLater()

        if sender_layout.count() == 1 and sender_layout is not self.row_layout:
            self.main_layout.removeItem(sender_layout)
            sender_layout.deleteLater()

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    app.exec_()
