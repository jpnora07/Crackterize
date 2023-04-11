from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QGridLayout
import math

class sci_Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "width: fit-content;\n"
            "heigth: fit-content;\n"
            "block-size: fit-content;\n"
            "}\n"
        )
        self.setGeometry(300, 300, 400, 400)

        # Create the grid layout for the buttons
        grid = QGridLayout()

        # Create the text box
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 10)
        self.textbox.setFixedWidth(380)
        self.textbox.setReadOnly(True)

        # Create the buttons
        buttons = [
            ['7', '8', '9', '+', 'C'],
            ['4', '5', '6', '-', 'π'],
            ['1', '2', '3', '*', 'e'],
            ['0', '.', '=', '/', 'sqrt'],
            ['sin', 'cos', 'tan', 'log', 'ln']
        ]

        # Add the buttons to the grid
        for i, row in enumerate(buttons):
            for j, label in enumerate(row):
                button = QPushButton(label, self)
                button.setFixedHeight(40)
                button.setFixedWidth(70)

                # Connect the button to the function that handles button clicks
                button.clicked.connect(self.buttonClicked)

                grid.addWidget(button, i, j)

        # Create a vertical layout to hold the text box and grid layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addLayout(grid)

        # Create a horizontal layout to hold the close button
        hbox = QHBoxLayout()
        close_button = QPushButton('Close', self)
        close_button.clicked.connect(self.close)
        hbox.addStretch(1)
        hbox.addWidget(close_button)

        # Add the layouts to the dialog
        layout = QVBoxLayout(self)
        layout.addLayout(vbox)
        layout.addLayout(hbox)

        self.show()

    def buttonClicked(self):
        sender = self.sender()
        digit = sender.text()

        if digit == 'C':
            self.textbox.clear()
        elif digit == '=':
            try:
                self.textbox.setText(str(eval(self.textbox.text())))
            except:
                self.textbox.setText('Error')
        elif digit == 'sqrt':
            try:
                self.textbox.setText(str(math.sqrt(float(self.textbox.text()))))
            except:
                self.textbox.setText('Error')
        elif digit == 'π':
            self.textbox.setText(str(math.pi))
        elif digit == 'e':
            self.textbox.setText(str(math.e))
        elif digit == 'sin':
            try:
                self.textbox.setText(str(math.sin(float(self.textbox.text()))))
            except:
                self.textbox.setText('Error')
        elif digit == 'cos':
            try:
                self.textbox.setText(str(math.cos(float(self.textbox.text()))))
            except:
                self.textbox.setText('Error')
        elif digit == 'tan':
            try:
                self.textbox.setText(str(math.tan(float(self.textbox.text()))))
            except:
                self.textbox.setText('Error')
        elif digit == 'log':
            try:
                self.textbox.setText(str(math.log10(float(self.textbox.text()))))
            except:
                self.textbox.setText('Error')
        elif digit == 'ln':
            try:
                self.textbox.setText(str(math.log(float(self.textbox.text()))))
            except:
                self.textbox.setText('Error')
        else:
            self.textbox.setText(self.textbox.text() + digit)

if __name__ == '__main__':
    app = QApplication([])
    calc = sci_Calculator()
    app.exec_()
