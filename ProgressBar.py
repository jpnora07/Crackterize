import sys
from PySide2 import QtCore, QtWidgets, QtGui

from PySide2extn.RoundProgressBar import roundProgressBar  # IMPORT THE EXTENSION LIBRARY

x = 0
p = 1


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Round Progress Bar'
        self.button = QtWidgets.QPushButton("Click me to change Value")
        self.text = QtWidgets.QLabel("Round Progress Bar")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        # CREATING THE ROUND PROGRESS BAR OBJECT
        self.rpb = roundProgressBar()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        # ADDING THE ROUND PROGRESS BAR OBJECT TO THE                                             # BOTTOM OF THE LAYOUT
        self.layout.addWidget(self.rpb)

        self.setLayout(self.layout)
        self.button.clicked.connect(self.magic)  # BUTTON PRESSED EVENT

    def magic(self):
        global x, p
        x = x + 10 * p
        if x == 100:
            p = -1
        elif x == 0:
            p = 1
        self.rpb.rpb_setValue(x)  # CHANGING THE VALUE OF THE PROGRESS BAR
        out_text = 'Round Progress Bar: ' + str(x) + '%'
        self.text.setText(out_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
