from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class StairsCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stairs Calculator')
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "width: fit-content;\n"
            "heigth: fit-content;\n"
            "block-size: fit-content;\n"
            "}\n"
        )
        self.setGeometry(100, 100, 400, 300)



        # Create labels for each input field
        self.run_label = QLabel('Run:', self)
        self.run_label.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")
        self.run_label.setGeometry(20, 20, 80, 20)
        self.rise_label = QLabel('Rise:', self)
        self.rise_label.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")
        self.rise_label.setGeometry(20, 50, 80, 20)
        self.width_label = QLabel('Width:', self)
        self.width_label.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")
        self.width_label.setGeometry(20, 80, 80, 20)
        self.platform_label = QLabel('Platform depth:', self)
        self.platform_label.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")
        self.platform_label.setGeometry(20, 110, 150, 20)
        self.steps_label = QLabel('Number of steps:', self)
        self.steps_label.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")
        self.steps_label.setGeometry(20, 140, 170, 20)
        self.units_label = QLabel('Units:', self)
        self.units_label.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")
        self.units_label.setGeometry(20, 170, 80, 20)

        # Create input fields for each value
        self.run_input = QLineEdit(self)
        self.run_input.setStyleSheet("background-color: white;")
        self.run_input.setGeometry(120, 20, 150, 20)
        self.rise_input = QLineEdit(self)
        self.rise_input.setStyleSheet("background-color: white;")
        self.rise_input.setGeometry(120, 50, 150, 20)
        self.width_input = QLineEdit(self)
        self.width_input.setStyleSheet("background-color: white;")
        self.width_input.setGeometry(120, 80, 150, 20)
        self.platform_input = QLineEdit(self)
        self.platform_input.setStyleSheet("background-color: white;")
        self.platform_input.setGeometry(200, 110, 150, 20)
        self.steps_input = QLineEdit(self)
        self.steps_input.setStyleSheet("background-color: white;")
        self.steps_input.setGeometry(200, 140, 150, 20)

        # Create dropdown menu for units
        self.units_dropdown = QComboBox(self)
        self.units_dropdown.setStyleSheet("background-color: white;")
        self.units_dropdown.setGeometry(120, 170, 150, 22)
        self.units_dropdown.addItems(['inches', 'feet', 'yards', 'meters', 'centimeters'])
        self.units_dropdown.setCurrentIndex(0)

        # Create button to calculate stair height and slope
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.setStyleSheet("font-size: 11pt; font-family: Inter; font-weight: Bold;")
        self.calculate_button.setGeometry(20, 230, 70, 50)
        self.calculate_button.clicked.connect(self.calculate)

        # Create label for output
        self.output_label = QLabel(self)
        self.output_label.setStyleSheet("font-size: 8pt; font-family: Inter; font-weight: Bold; background-color: white;")
        self.output_label.setGeometry(130, 220, 200, 80)

    def calculate(self):
        # Get input values
        run = float(self.run_input.text())
        rise = float(self.rise_input.text())
        width = float(self.width_input.text())
        platform_depth = float(self.platform_input.text())
        num_steps = int(self.steps_input.text())

        # Convert input values to inches based on selected unit
        units = self.units_dropdown.currentText()
        if units == 'inches':
            pass
        elif units == 'feet':
            run *= 12
            rise *= 12
            width *= 12
            platform_depth *= 12
        elif units == 'yards':
            run *= 36
            rise *= 36
            width *= 36
            platform_depth *= 36
        elif units == 'meters':
            run *= 39.3701
            rise *= 39.3701
            width *= 39.3701
            platform_depth *= 39.3701
        elif units == 'centimeters':
            run /= 2.54
            rise /= 2.54
            width /= 2.54
            platform_depth /= 2.54
        else:
            pass

        # Calculate total stair height and slope
        total_height = rise * num_steps
        total_run = run * num_steps + platform_depth
        slope = total_height / total_run

        # Update output label with results
        self.output_label.setText(f'Total stair height: {total_height:.2f} inches\nSlope: {slope:.2f}')

if __name__ == '__main__':
    app = QApplication([])
    stairs_calc = StairsCalculator()
    stairs_calc.show()
    app.exec_()

