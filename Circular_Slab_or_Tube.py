import sys
import math
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QWidget


class CircularSlabCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Circular Slab Calculator')
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "width: fit-content;\n"
            "heigth: fit-content;\n"
            "block-size: fit-content;\n"
            "}\n"
        )
        self.setGeometry(100, 100, 400, 650)

        self.outer_diameter_label = QLabel('Outer Diameter:')
        self.outer_diameter_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.outer_diameter_input = QLineEdit()
        self.outer_diameter_input.setStyleSheet("Height: 30;  background-color: white; ")
        self.inner_diameter_label = QLabel('Inner Diameter:')
        self.inner_diameter_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.inner_diameter_input = QLineEdit()
        self.inner_diameter_input.setStyleSheet("Height: 30;  background-color: white;")
        self.length_label = QLabel('Length/Height:')
        self.length_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.length_input = QLineEdit()
        self.length_input.setStyleSheet("Height: 30;  background-color: white;")
        self.quantity_label = QLabel('Quantity:')
        self.quantity_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.quantity_input = QLineEdit()
        self.quantity_input .setStyleSheet("Height: 30;  background-color: white;")
        self.unit_label = QLabel('Units:')
        self.unit_label .setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.unit_dropdown = QComboBox()
        self.unit_dropdown.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")
        self.unit_dropdown.setStyleSheet("Height: 30;  background-color: white;")
        self.unit_dropdown.addItems(['inches', 'feet', 'yards', 'meters', 'centimeters'])

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")

        self.calculate_button.clicked.connect(self.calculate_volume)

        self.result_label = QLabel('Total Volume:')
        self.result_label.setStyleSheet("font-size: 15pt; font-family: Inter; font-weight: Bold; ")

        self.result_output = QLabel()
        self.result_output.setStyleSheet("font-size: 10pt; font-family: Inter; font-weight: Bold; ")

        vbox = QVBoxLayout()
        vbox.addWidget(self.outer_diameter_label)
        vbox.addWidget(self.outer_diameter_input)
        vbox.addWidget(self.inner_diameter_label)
        vbox.addWidget(self.inner_diameter_input)
        vbox.addWidget(self.length_label)
        vbox.addWidget(self.length_input)
        vbox.addWidget(self.quantity_label)
        vbox.addWidget(self.quantity_input)
        vbox.addWidget(self.unit_label)
        vbox.addWidget(self.unit_dropdown)
        vbox.addWidget(self.calculate_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.result_output)

        self.setLayout(vbox)

    def calculate_volume(self):
        outer_diameter = float(self.outer_diameter_input.text())
        inner_diameter = float(self.inner_diameter_input.text())
        length = float(self.length_input.text())
        quantity = float(self.quantity_input.text())
        units = self.unit_dropdown.currentText()

        if units == "inches":
            factor = 1.0
        elif units == "feet":
            factor = 12.0
        elif units == "yards":
            factor = 36.0
        elif units == "meters":
            factor = 39.37
        elif units == "centimeters":
            factor = 0.3937
        else:
            factor = 1.0

        outer_diameter = outer_diameter * factor
        inner_diameter = inner_diameter * factor
        length = length * factor

        outer_radius = outer_diameter / 2
        inner_radius = inner_diameter / 2
        volume = ((math.pi * (outer_radius ** 2)) - (math.pi * (inner_radius ** 2))) * length
        total_volume = volume * quantity

        if factor == 1.0:
            self.result_output.setText(f"{total_volume:.2f} cubic inches")
        elif factor == 12.0:
            self.result_output.setText(f"{total_volume:.2f} cubic feet")
        elif factor == 36.0:
            self.result_output.setText(f"{total_volume:.2f} cubic yards")
        elif factor == 39.37:
            self.result_output.setText(f"{total_volume:.2f} cubic meters")
        elif factor == 0.3937:
            self.result_output.setText(f"{total_volume:.2f} cubic centimeters")
        else:
            self.result_output.setText(f"{total_volume:.2f} cubic inches")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CircularSlabCalculator()
    calc.show()
    app.exec_()
