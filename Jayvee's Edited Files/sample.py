from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import QSize


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        self.button = QPushButton(self.central_widget)
        self.button.setObjectName("pushButton")
        self.button.setIcon(QIcon(r'C:\Users\Jayvee\PycharmProjects\Crackterize\images\add_folder.png'))
        self.button.setStyleSheet("#pushButton{background-image:url("
                                  "images/add_folder.png);height:100px;background-repeat: "
                                  "no-repeat;background-position: center;background-size: 2px 2px;}")
        self.button.setIconSize(QSize(32, 32))
        self.button.setFixedSize(40, 40)
        self.button.clicked.connect(self.addNewButton)
        self.layout.addWidget(self.button)

        self.setGeometry(200, 300, 100, 200)
        self.setWindowTitle("Folder")
        self.show()

    def addNewButton(self):
        new_button = QPushButton("Delete", self.central_widget)
        new_button.clicked.connect(self.deleteButton)  # connect clicked signal to a delete function
        self.layout.insertWidget(0, new_button)  # add new button to the beginning of the layout

    def deleteButton(self):
        sender_button = self.sender()  # get the button that was clicked
        self.layout.removeWidget(sender_button)  # remove the button from the layout
        self.button.setIcon(QIcon(r'C:\Users\Jayvee\PycharmProjects\Crackterize\images\folder.png'))
        self.button.setStyleSheet("#pushButton{background-image:url("
                                  "images/add_folder.png);height:100px;background-repeat: "
                                  "no-repeat;background-position: center;background-size: 2px 2px;}")
        sender_button.deleteLater()  # delete the button from memory


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    app.exec_()
