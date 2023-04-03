import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QFont, QPixmap


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Slabs/Square Footings/Walls Calculator")
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "width: fit-content;\n"
                                 "heigth: fit-content;\n"
                                 "block-size: fit-content;\n"
                                 "}\n"
                                 )
        self.setGeometry(100, 150, 500, 650)
        self.setMaximumSize(610, 610)
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)

        imageLabel = QLabel(self)
        pixmap = QPixmap('images/slab.png')
        imageLabel.setPixmap(pixmap)
        imageLabel.setScaledContents(True)
        imageLabel.setGeometry(185, 490, 127, 122)

        self.lengthLabel = QLabel("Length:", self)
        self.lengthLabel.setStyleSheet("font-size: 12pt; font-family: Inter; font-weight: Bold; ")
        self.lengthLabel.setFixedWidth(150)
        self.lengthLabel.move(50, 50)
        self.lengthInput = QLineEdit(self)
        self.lengthInput.move(260, 50)
        self.lengthInput.setFixedWidth(200)
        self.lengthInput.setStyleSheet("background-color: white")

        self.widthLabel = QLabel("Width:", self)
        self.widthLabel.setStyleSheet("font-size: 12pt; font-family: Inter; font-weight: Bold; ")
        self.widthLabel.setFixedWidth(150)
        self.widthLabel.move(50, 100)
        self.widthInput = QLineEdit(self)
        self.widthInput.move(260, 100)
        self.widthInput.setFixedWidth(200)
        self.widthInput.setStyleSheet("background-color: white")


        self.thicknessLabel = QLabel("Thickness/Height:", self)
        self.thicknessLabel.setStyleSheet("font-size: 12pt; font-family: Inter; font-weight: Bold; ")
        self.thicknessLabel.setFixedWidth(150)
        self.thicknessLabel.move(50, 150)
        self.thicknessInput = QLineEdit(self)
        self.thicknessInput.move(260, 150)
        self.thicknessInput.setFixedWidth(200)
        self.thicknessInput.setStyleSheet("background-color: white")

        self.qualityLabel = QLabel("Quality:", self)
        self.qualityLabel.setStyleSheet("font-size: 12pt; font-family: Inter; font-weight: Bold; ")
        self.qualityLabel.setFixedWidth(150)
        self.qualityLabel.move(50, 200)
        self.qualityInput = QComboBox(self)
        self.qualityInput.addItem("Poor")
        self.qualityInput.addItem("Average")
        self.qualityInput.addItem("Good")
        self.qualityInput.addItem("Excellent")
        self.qualityInput.move(260, 200)
        self.qualityInput.setFixedWidth(200)
        self.qualityInput.setStyleSheet("background-color: white")

        self.unitsLabel = QLabel("Units:", self)
        self.unitsLabel.setStyleSheet("font-size: 12pt; font-family: Inter; font-weight: Bold; ")
        self.unitsLabel.setFixedWidth(150)
        self.unitsLabel.move(50, 250)
        self.unitsInput = QComboBox(self)
        self.unitsInput.addItem("Inches")
        self.unitsInput.addItem("Feet")
        self.unitsInput.addItem("Yards")
        self.unitsInput.addItem("Meters")
        self.unitsInput.addItem("Centimeters")
        self.unitsInput.move(260, 250)
        self.unitsInput.setFixedWidth(200)
        self.unitsInput.setStyleSheet("background-color: white")

        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.move(50, 350)
        self.calculateButton.clicked.connect(self.calculate)
        self.calculateButton.setStyleSheet("background-color: white")

        self.resetButton = QPushButton("Reset", self)
        self.resetButton.move(360, 350)
        self.resetButton.clicked.connect(self.reset)
        self.resetButton.setStyleSheet("background-color: white")

        self.areaLabel = QLabel("Total Area:", self)
        self.areaLabel.setFixedWidth(150)
        self.areaLabel.move(50, 400)
        self.areaOutput = QLabel("", self)
        self.areaOutput.setFixedWidth(200)
        self.areaOutput.move(150, 400)
        self.areaOutput.setStyleSheet("background-color: white")

        self.volumeLabel = QLabel("Total Volume:", self)
        self.volumeLabel.setFixedWidth(150)
        self.volumeLabel.move(50, 450)
        self.volumeOutput = QLabel("", self)
        self.volumeOutput.setFixedWidth(250)
        self.volumeOutput.move(175, 450)
        self.volumeOutput.setStyleSheet("background-color: white")


    def calculate(self):
        length = float(self.lengthInput.text())
        width = float(self.widthInput.text())
        thickness = float(self.thicknessInput.text())
        quality = self.qualityInput.currentText()
        units = self.unitsInput.currentText()

        if units == "Inches":
            area = (length * width) / 144
            volume = area * (thickness / 12)
        elif units == "Feet":
            area = length * width
            volume = area * thickness
        elif units == "Yards":
            area = (length * width) / 9
            volume = area * (thickness / 3)
        elif units == "Meters":
            area = length * width
            volume = area * (thickness / 100)
        elif units == "Centimeters":
            area = (length * width) / 10000
            volume = area * (thickness / 100)


        self.areaOutput.setText(f"{area:.2f} sq. {units.lower()}")
        self.volumeOutput.setText(f"{volume:.2f} cu. {units.lower()}")

    def reset(self):
        self.lengthInput.setText("")
        self.widthInput.setText("")
        self.thicknessInput.setText("")
        self.qualityInput.setCurrentIndex(0)
        self.unitsInput.setCurrentIndex(0)
        self.areaOutput.setText("")
        self.volumeOutput.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QPushButton { background-color: #f0f0f0; } QLabel { font-size: 14pt; }")
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

