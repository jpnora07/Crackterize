import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox


class ConcreteCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Concrete Calculator')
        self.setStyleSheet('''
            background-color: #F2F2F2;
            font-size: 18px;
            font-family: Arial, sans-serif;
        ''')

        # Header
        header_label = QLabel('Concrete Calculator')
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('font-size: 24px; font-weight: bold; margin-bottom: 20px;')


        # Labels
        length_label = QLabel('Length (ft):')
        width_label = QLabel('Width (ft):')
        thickness_label = QLabel('Thickness (in):')
        concrete_type_label = QLabel('Concrete Type:')

        # Line Edits
        self.length_edit = QLineEdit()
        self.width_edit = QLineEdit()
        self.thickness_edit = QLineEdit()

        # Combo Box
        self.concrete_type_combo = QComboBox()
        self.concrete_type_combo.addItem('Square Slab')
        self.concrete_type_combo.addItem('Round Slab')
        self.concrete_type_combo.addItem('Wall')
        self.concrete_type_combo.addItem('Footer')
        self.concrete_type_combo.addItem('Square Column')
        self.concrete_type_combo.addItem('Round Column')
        self.concrete_type_combo.addItem('Steps')
        self.concrete_type_combo.addItem('Curb & Gutter')

        # Buttons
        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_concrete)

        # Result Label
        self.result_label = QLabel()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(header_label)
        layout.addWidget(length_label)
        layout.addWidget(self.length_edit)
        layout.addWidget(width_label)
        layout.addWidget(self.width_edit)
        layout.addWidget(thickness_label)
        layout.addWidget(self.thickness_edit)
        layout.addWidget(concrete_type_label)
        layout.addWidget(self.concrete_type_combo)
        layout.addWidget(calculate_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def calculate_concrete(self):
        length = float(self.length_edit.text())
        width = float(self.width_edit.text())
        thickness = float(self.thickness_edit.text())
        concrete_type = self.concrete_type_combo.currentText()

        if concrete_type == 'Standard':
            weight_per_cubic_ft = 150
        else:
            weight_per_cubic_ft = 160

        volume = length * width * (thickness / 12.0)
        weight = volume * weight_per_cubic_ft
        cubic_yards = volume / 27.0

        self.result_label.setText('You will need %.2f pounds or %.2f cubic yards of %s concrete.' % (weight, cubic_yards, concrete_type.lower()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = ConcreteCalculator()
    calculator.show()
    sys.exit(app.exec_())
