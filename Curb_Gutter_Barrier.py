import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "width: fit-content;\n"
            "heigth: fit-content;\n"
            "block-size: fit-content;\n"
            "}\n"
        )
        self.setMaximumSize(500, 600)

    def initUI(self):
        # Labels
        lbl_curb_depth = QLabel('Curb Depth:', self)
        lbl_curb_depth.move(20, 20)
        lbl_curb_depth.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")

        lbl_gutter_width = QLabel('Gutter Width:', self)
        lbl_gutter_width.move(20, 60)
        lbl_gutter_width.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        lbl_curb_height = QLabel('Curb Height:', self)
        lbl_curb_height.move(20, 100)
        lbl_curb_height.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        lbl_flag_thickness = QLabel('Flag Thickness:', self)
        lbl_flag_thickness.move(20, 140)
        lbl_flag_thickness.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        lbl_length = QLabel('Length:', self)
        lbl_length.move(20, 180)
        lbl_length.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")



        lbl_quantity = QLabel('Quantity:', self)
        lbl_quantity.move(20, 220)
        lbl_quantity.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        lbl_unit = QLabel('Unit:', self)
        lbl_unit.move(20, 260)
        lbl_unit.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        # Textboxes
        self.txt_curb_depth = QLineEdit(self)
        self.txt_curb_depth.move(150, 20)
        self.txt_curb_depth.setStyleSheet("Height: 30; Width: 200;  background-color: white;")

        self.txt_gutter_width = QLineEdit(self)
        self.txt_gutter_width.move(150, 60)
        self.txt_gutter_width.setStyleSheet("Height: 30;  Width: 200;  background-color: white;")


        self.txt_curb_height = QLineEdit(self)
        self.txt_curb_height.move(150, 100)
        self.txt_curb_height.setStyleSheet("Height: 30;  Width: 200;  background-color: white;")


        self.txt_flag_thickness = QLineEdit(self)
        self.txt_flag_thickness.move(150, 140)
        self.txt_flag_thickness.setStyleSheet("Height: 30;  Width: 200;  background-color: white;")


        self.txt_length = QLineEdit(self)
        self.txt_length.move(150, 180)
        self.txt_length.setStyleSheet("Height: 30;  Width: 200;  background-color: white;")


        self.txt_quantity = QLineEdit(self)
        self.txt_quantity.move(150, 220)
        self.txt_quantity.setStyleSheet("Height: 30;  Width: 200;  background-color: white;")


        # Combo box
        self.cmb_unit = QComboBox(self)
        self.cmb_unit.addItem('Inches')
        self.cmb_unit.addItem('Feet')
        self.cmb_unit.addItem('Yards')
        self.cmb_unit.addItem('Meters')
        self.cmb_unit.addItem('Centimeters')
        self.cmb_unit.move(150, 260)

        # Button
        btn_calculate = QPushButton('Calculate', self)
        btn_calculate.move(20, 300)
        btn_calculate.clicked.connect(self.calculate)
        btn_calculate.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        # Output label
        self.lbl_output = QLabel(self)
        self.lbl_output.move(20, 340)
        self.lbl_output.resize(400, 40)

        # Window settings
        self.setGeometry(100, 100, 450, 400)
        self.setWindowTitle('Curb and Gutter Barrier Calculator')
        self.show()

    def calculate(self):
        try:
            # Input values
            curb_depth = float(self.txt_curb_depth.text())
            gutter_width = float(self.txt_gutter_width.text())
            curb_height = float(self.txt_curb_height.text())
            flag_thickness = float(self.txt_flag_thickness.text())
            length = float(self.txt_length.text())
            quantity = float(self.txt_quantity.text())

            # Convert length to inches
            unit = self.cmb_unit.currentText()
            if unit == 'Inches':
                length_inches = length
            elif unit == 'Feet':
                length_inches = length * 12
            elif unit == 'Yards':
                length_inches = length * 36
            elif unit == 'Meters':
                length_inches = length * 39.37
            elif unit == 'Centimeters':
                length_inches = length * 0.3937

            # Calculate volume in cubic inches
            volume = (curb_depth + gutter_width) * curb_height * length_inches * flag_thickness * quantity

            # Convert volume to appropriate unit
            if volume < 1728:
                unit = 'in^3'
            elif volume < 46656:
                volume /= 1728
                unit = 'ft^3'
            elif volume < 46656000:
                volume /= 46656
                unit = 'yd^3'
            else:
                volume /= 46656000
                unit = 'm^3'

            # Display result
            result = f'Volume: {volume:.2f} {unit}'
            self.lbl_output.setText(result)
            self.lbl_output.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        except ValueError:
            self.lbl_output.setText('Error: Invalid input')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())

