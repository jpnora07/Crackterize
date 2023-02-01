from PyQt5 import QtCore, QtGui, QtWidgets


class ComboBoxTitle(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setReadOnly(True)
        self.line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.setLineEdit(self.line_edit)
        self.view().pressed.connect(self.handleItemPressed)

    def handleItemPressed(self, index):
        self.line_edit.setText(index.data())
        self.hidePopup()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ComboBox Title")
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        self.combo_box = ComboBoxTitle(central_widget)
        self.combo_box.addItems(["Sayian", "Super Saiyan", "Super Sayian 2", "Super Sayian B"])
        layout.addWidget(self.combo_box)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
