# -*- coding: utf-8 -*-
import math

# Form implementation generated from reading ui file 'circularslabcalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class uwi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(600, 600)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(600, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bg = QtWidgets.QWidget(Dialog)

        self.bg.setObjectName("bg")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_1 = QtWidgets.QWidget(self.bg)
        self.widget_1.setObjectName("widget_1")
        self.widget_1.setStyleSheet("#bg{\n"
                              "background-image: url(images/bg.jpg);\n"
                              "border-top-left-radius: 10px;\n"
                              "border-top-right-radius: 10px;\n"
                              "border-bottom-left-radius: 10px;\n"
                              "border-bottom-right-radius: 10px;\n"
                              "}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_1)
        self.label.setStyleSheet("#label{\n"
                                 "font: 200 15pt Segoe UI Black;\n"
                                 "alignment: center;\n"
                                 "color: rgba(111, 75, 39, 0.77);\n"
                                 "                                 }")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_1)
        self.widget_7 = QtWidgets.QWidget(self.bg)
        self.widget_7.setMaximumSize(QtCore.QSize(600, 600))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.outerD_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.outerD_lineEdit.setObjectName("outerD_lineEdit")
        self.verticalLayout_4.addWidget(self.outerD_lineEdit)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_2 = QtWidgets.QWidget(self.bg)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.innerD_lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.innerD_lineEdit.setObjectName("innerD_lineEdit")
        self.verticalLayout_5.addWidget(self.innerD_lineEdit)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_8 = QtWidgets.QWidget(self.bg)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget_8)
        self.label_4.setStyleSheet("#label_4{\n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.length_lineEdit = QtWidgets.QLineEdit(self.widget_8)
        self.length_lineEdit.setObjectName("length_lineEdit")
        self.verticalLayout_6.addWidget(self.length_lineEdit)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_5 = QtWidgets.QWidget(self.bg)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setStyleSheet("#label_5{\n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.quantity_lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.quantity_lineEdit.setObjectName("quantity_lineEdit")
        self.verticalLayout_7.addWidget(self.quantity_lineEdit)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.bg)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setStyleSheet("#label_6{\n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.unit_comboBox = QtWidgets.QComboBox(self.widget_3)
        self.unit_comboBox.setObjectName("unit_comboBox")
        self.unit_comboBox.setObjectName("unit_comboBox")
        self.unit_comboBox.addItem("Inches")
        self.unit_comboBox.addItem("Feet")
        self.unit_comboBox.addItem("Yards")
        self.unit_comboBox.addItem("Meters")
        self.unit_comboBox.addItem("Centimeters")
        self.verticalLayout_8.addWidget(self.unit_comboBox)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.bg)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 600))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calculatebtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculatebtn.sizePolicy().hasHeightForWidth())
        self.calculatebtn.setSizePolicy(sizePolicy)
        self.calculatebtn.setMaximumSize(QtCore.QSize(150, 150))
        self.calculatebtn.setStyleSheet("#calculatebtn{\n"
                                        "font-weight:bold;\n"
                                        "color: white;\n"
                                        "background-color: #6F4B27;\n"
                                        "font-family: Inter;\n"
                                        "border-top-left-radius: 8px;\n"
                                        "border-top-right-radius: 8px;\n"
                                        "border-bottom-left-radius: 8px;\n"
                                        "border-bottom-right-radius: 8px;\n"
                                        "font-size: 15px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "#calculatebtn:hover{\n"
                                        "color: rgb(144,115,87);\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}")
        self.calculatebtn.setObjectName("calculatebtn")
        self.calculatebtn.clicked.connect(self.calculate_volume)
        self.horizontalLayout.addWidget(self.calculatebtn)
        self.closebtn = QtWidgets.QPushButton(self.widget)
        self.closebtn.setMaximumSize(QtCore.QSize(150, 150))
        self.closebtn.setStyleSheet("#closebtn{\n"
                                    "font-weight:bold;\n"
                                    "color: white;\n"
                                    "background-color: #6A6E72;\n"
                                    "font-family: Inter;\n"
                                    "border-top-left-radius: 8px;\n"
                                    "border-top-right-radius: 8px;\n"
                                    "border-bottom-left-radius: 8px;\n"
                                    "border-bottom-right-radius: 8px;\n"
                                    "font-size: 15px;\n"
                                    "text-align: center;\n"
                                    "}\n"
                                    "#closebtn:hover{\n"
                                    "color: rgb(144,115,87);\n"
                                    "border :2px solid rgb\n"
                                    "#6A6E72;\n"
                                    "background-color: white;\n"
                                    "}")
        self.closebtn.setObjectName("closebtn")
        self.closebtn.clicked.connect(Dialog.close)
        self.horizontalLayout.addWidget(self.closebtn)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_6 = QtWidgets.QWidget(self.bg)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setStyleSheet("#label_8{\n"
                                   "font: 200 11pt Arial, Sans Serif, Bold;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.result = QtWidgets.QLabel(self.widget_6)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout_10.addWidget(self.result)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.bg)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Circular Slab Calculator"))
        self.label_2.setText(_translate("Dialog", "Outer Diameter:"))
        self.label_3.setText(_translate("Dialog", "Inner Diameter:"))
        self.label_4.setText(_translate("Dialog", "Length / Height:"))
        self.label_5.setText(_translate("Dialog", "Quantity:"))
        self.label_6.setText(_translate("Dialog", "Units:"))
        self.calculatebtn.setText(_translate("Dialog", "Calculate"))
        self.closebtn.setText(_translate("Dialog", "Close"))
        self.label_8.setText(_translate("Dialog", "Total Volume:"))

    def calculate_volume(self):
        try:
            outer_diameter = float(self.outerD_lineEdit.text())
            inner_diameter = float(self.innerD_lineEdit.text())
            length = float(self.length_lineEdit.text())
            quantity = float(self.quantity_lineEdit.text())
            units = self.unit_comboBox.currentText()


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
                self.result.setText(f"{total_volume:.2f} cubic inches")
            elif factor == 12.0:
                self.result.setText(f"{total_volume:.2f} cubic feet")
            elif factor == 36.0:
                self.result.setText(f"{total_volume:.2f} cubic yards")
            elif factor == 39.37:
                self.result.setText(f"{total_volume:.2f} cubic meters")
            elif factor == 0.3937:
                self.result.setText(f"{total_volume:.2f} cubic centimeters")
            else:
                self.result.setText(f"{total_volume:.2f} cubic inches")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = uwi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
