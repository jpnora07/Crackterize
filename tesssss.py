from os import name

import self as self
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtGui import QIcon, QFont
import sys


class StairsCalculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stairs Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(300, 300, 400, 250)

        # Create widgets
        self.run_label = QLabel("Run:")
        self.run_line_edit = QLineEdit()
        self.run_combo_box = QComboBox()
        self.run_combo_box.addItems(["inches", "feet", "yards", "meters", "centimeters"])
        self.rise_label = QLabel("Rise:")
        self.rise_line_edit = QLineEdit()
        self.rise_combo_box = QComboBox()
        self.rise_combo_box.addItems(["inches", "feet", "yards", "meters", "centimeters"])
        self.width_label = QLabel("Width:")
        self.width_line_edit = QLineEdit()
        self.width_combo_box = QComboBox()
        self.width_combo_box.addItems(["inches", "feet", "yards", "meters", "centimeters"])
        self.platform_depth_label = QLabel("Platform Depth:")
        self.platform_depth_line_edit = QLineEdit()
        self.platform_depth_combo_box = QComboBox()
        self.platform_depth_combo_box.addItems(["inches", "feet", "yards", "meters", "centimeters"])
        self.num_steps_label = QLabel("Number of Steps:")
        self.num_steps_line_edit = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        self.volume_label = QLabel("Volume of Concrete:")
        self.volume_line_edit = QLineEdit()
        self.volume_line_edit.setReadOnly(True)

        # Create layouts
        self.main_layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()
        self.run_layout = QVBoxLayout()
        self.run_layout.addWidget(self.run_label)
        self.run_layout.addWidget(self.run_line_edit)
        self.run_layout.addWidget(self.run_combo_box)
        self.rise_layout = QVBoxLayout()
        self.rise_layout.addWidget(self.rise_label)
        self.rise_layout.addWidget(self.rise_line_edit)
        self.rise_layout.addWidget(self.rise_combo_box)
        self.width_layout = QVBoxLayout()
        self.width_layout.addWidget(self.width_label)
        self.width_layout.addWidget(self.width_line_edit)
        self.width_layout.addWidget(self.width_combo_box)
        self.platform_depth_layout = QVBoxLayout()
        self.platform_depth_layout.addWidget(self.platform_depth_label)
        self.platform_depth_layout.addWidget(self.platform_depth_line_edit)
        self.platform_depth_layout.addWidget(self.platform_depth_combo_box)
        self.num_steps_layout = QVBoxLayout()
        self.num_steps_layout.addWidget(self.num_steps_label)
        self.num_steps_layout.addWidget(self.num_steps_line_edit)
        self.input_layout.addLayout(self.run_layout)
        self.input_layout.addLayout(self.rise_layout)
        self.input_layout.addLayout(self.width_layout)
        self.input_layout.addLayout(self.platform_depth_layout)
        self.input_layout.addLayout(self.num_steps_layout)
        self.output_layout = QHBoxLayout()
        self.output_layout.addWidget(self.volume_label)
        self.output_layout.addWidget(self.volume_line_edit)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.calculate_button)

        # Add layouts to main layout
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.output_layout)
        self.main_layout.addLayout(self.button_layout)

        # Set main layout
        self.setLayout(self.main_layout)

        # Connect button to slot
        self.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        # Get input values and units
    run_value = float(self.run_value.text())
    rise_value = float(self.rise_value.text())
    width_value = float(self.width_value.text())
    platform_depth_value = float(self.platform_depth_line_edit.text())
    platform_depth_unit = self.platform_depth_combo_box.currentText()
    num_steps = int(self.num_steps_line_edit.text())

    # Convert all units to inches for calculation
    run_inches = self.convert_to_inches(run_value, run_unit)
    rise_inches = self.convert_to_inches(rise_value, rise_unit)
    width_inches = self.convert_to_inches(width_value, width_unit)
    platform_depth_inches = self.convert_to_inches(platform_depth_value, platform_depth_unit)

    # Calculate volume of concrete
    total_height_inches = num_steps * rise_inches
    volume_cubic_inches = (total_height_inches * width_inches * platform_depth_inches) + (run_inches * width_inches * platform_depth_inches)

    # Convert cubic inches to cubic feet and display result
    volume_cubic_feet = volume_cubic_inches / 1728
    self.volume_label.setText(f"{volume_cubic_feet:.2f} cubic feet")

def convert_to_inches(self, value, unit):
    # Convert input value to inches
    if unit == "inches":
        return value
    elif unit == "feet":
        return value * 12
    elif unit == "yards":
        return value * 36
    elif unit == "meters":
        return value * 39.37
    elif unit == "centimeters":
        return value / 2.54
if name == "main":
    app = QApplication(sys.argv)
    window = StairsCalculator()
    sys.exit(app.exec_())