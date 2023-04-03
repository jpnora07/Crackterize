from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class FootingsCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hole/Column/Round Footings Calculator")
        self.setStyleSheet("font-size: 14px; font-family: Arial, sans-serif;")
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "width: fit-content;\n"
            "heigth: fit-content;\n"
            "block-size: fit-content;\n"
            "}\n"
            )
        self.setGeometry(200, 200, 500, 650)
        self.setMaximumSize(500, 400)
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)


        self.diameter_label = QLabel("Diameter:")
        self.diameter_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.diameter_label.move(100, 150)
        self.diameter_edit = QLineEdit()
        self.diameter_edit.setStyleSheet("Height: 25; Width: 20; background-color: white; ")
        self.diameter_edit.setFixedWidth(280)
        self.diameter_unit_combo = QComboBox()
        self.diameter_unit_combo.setStyleSheet("Height: 25; ")
        self.diameter_unit_combo.addItems(["inches", "feet", "yards", "meters", "centimeters"])
        self.diameter_unit_combo.setCurrentIndex(0)

        self.depth_label = QLabel("Depth/Height:")
        self.depth_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.depth_label.move(100, 150)
        self.depth_edit = QLineEdit()
        self.depth_edit.setStyleSheet("Height: 25; background-color: white ")
        self.depth_edit.setFixedWidth(150)
        self.depth_unit_combo = QComboBox()
        self.depth_unit_combo.setStyleSheet("Height: 25; ")
        self.depth_unit_combo.addItems(["inches", "feet", "yards", "meters", "centimeters"])
        self.depth_unit_combo.setCurrentIndex(0)

        self.quantity_label = QLabel("Quantity:")
        self.quantity_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.quantity_label.move(100, 150)
        self.depth_edit.setFixedWidth(280)
        self.quantity_edit = QLineEdit()
        self.quantity_edit.setStyleSheet("Height: 25; background-color: white; ")

        self.calculate_button = QPushButton("Calculate")

        self.calculate_button.clicked.connect(self.calculate)
        self.calculate_button.setStyleSheet("font-size: 17pt; font-family: Inter; font-weight: Bold; ")
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row1.addWidget(self.diameter_label)
        row1.addWidget(self.diameter_edit)
        row1.addWidget(self.diameter_unit_combo)

        row2 = QHBoxLayout()
        row2.addWidget(self.depth_label)
        row2.addWidget(self.depth_edit)
        row2.addWidget(self.depth_unit_combo)

        row3 = QHBoxLayout()
        row3.addWidget(self.quantity_label)
        row3.addWidget(self.quantity_edit)

        row4 = QHBoxLayout()
        row4.addWidget(self.calculate_button)


        self.layout.addLayout(row1)
        self.layout.addLayout(row2)
        self.layout.addLayout(row3)
        self.layout.addLayout(row4)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)





    def calculate(self):
        try:
            diameter = float(self.diameter_edit.text())
            depth = float(self.depth_edit.text())
            quantity = int(self.quantity_edit.text())
            diameter_unit = self.diameter_unit_combo.currentText()
            depth_unit = self.depth_unit_combo.currentText()

            # Convert diameter to inches
            if diameter_unit == "feet":
                diameter *= 12
            elif diameter_unit == "yards":
                diameter *= 36
            elif diameter_unit == "meters":
                diameter *= 39.37
            elif diameter_unit == "centimeters":
                diameter *= 0.3937

            # Convert depth to inches
            if depth_unit == "feet":
                depth *= 12
            elif depth_unit == "yards":
                depth *= 36
            elif depth_unit == "meters":
                depth *= 39.37
            elif depth_unit == "centimeters":
                depth *= 0.3937

            volume = 3.14159 * (diameter / 2) ** 2 * depth * quantity

            result = (
                f"Total volume of concrete needed: \n"
                f"{volume:.2f} cubic inches \n"
                f"{volume / 1728:.2f} cubic feet \n"
                f"{volume / 46656:.2f} cubic yards \n"
                f"{volume / 61023.74:.2f} cubic meters \n"
                f"{volume * 16.387:.2f} cubic centimeters"
            )


            self.result_label.setText(result)
            self.result_label.setStyleSheet("font-size: 17pt; font-family: Inter; font-weight: Bold; ")

        except ValueError:
            self.result_label.setText("Please enter valid input values.")


if __name__ == "__main__":
    app = QApplication([])
    calculator = FootingsCalculator()
    calculator.show()
    app.exec_()