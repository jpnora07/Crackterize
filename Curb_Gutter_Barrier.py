
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class curb(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(600, 600)
        Dialog.setMinimumSize(QtCore.QSize(600, 600))
        Dialog.setMaximumSize(QtCore.QSize(600, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("#label{\n"
                                 "font: 200 15pt Segoe UI Black;\n"
                                 "alignment: center;\n"
                                 "color: rgba(111, 75, 39, 0.77);\n"
                                 "                                 }")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CDepth = QtWidgets.QLabel(self.widget_11)
        self.CDepth.setStyleSheet("#CDepth{\n"
                                  "font: 200 11pt Arial, Sans Serif;\n"
                                  "alignment: center;\n"
                                  "color: rgba(111, 75, 39, 0.77);\n"
                                  "}\n"
                                  "")
        self.CDepth.setObjectName("CDepth")
        self.horizontalLayout.addWidget(self.CDepth, 0, QtCore.Qt.AlignHCenter)
        self.curb_ln = QtWidgets.QLineEdit(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curb_ln.sizePolicy().hasHeightForWidth())
        self.curb_ln.setSizePolicy(sizePolicy)
        self.curb_ln.setObjectName("curb")
        self.horizontalLayout.addWidget(self.curb_ln, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GWidth = QtWidgets.QLabel(self.widget_7)
        self.GWidth.setStyleSheet("#GWidth{\n"
                                  "font: 200 11pt Arial, Sans Serif;\n"
                                  "alignment: center;\n"
                                  "color: rgba(111, 75, 39, 0.77);\n"
                                  "}")
        self.GWidth.setObjectName("GWidth")
        self.horizontalLayout_2.addWidget(self.GWidth, 0, QtCore.Qt.AlignHCenter)
        self.gut_ln = QtWidgets.QLineEdit(self.widget_7)
        self.gut_ln.setObjectName("gut_ln")
        self.horizontalLayout_2.addWidget(self.gut_ln, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CHeight = QtWidgets.QLabel(self.widget_3)
        self.CHeight.setStyleSheet("#CHeight{\n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.CHeight.setObjectName("CHeight")
        self.horizontalLayout_3.addWidget(self.CHeight, 0, QtCore.Qt.AlignHCenter)
        self.CuHeight_ln = QtWidgets.QLineEdit(self.widget_3)
        self.CuHeight_ln.setObjectName("CuHeight_ln")
        self.horizontalLayout_3.addWidget(self.CuHeight_ln, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.FThickness = QtWidgets.QLabel(self.widget_8)
        self.FThickness.setStyleSheet("#FThickness{\n"
                                      "font: 200 11pt Arial, Sans Serif;\n"
                                      "alignment: center;\n"
                                      "color: rgba(111, 75, 39, 0.77);\n"
                                      "}")
        self.FThickness.setObjectName("FThickness")
        self.horizontalLayout_4.addWidget(self.FThickness, 0, QtCore.Qt.AlignHCenter)
        self.flag_ln = QtWidgets.QLineEdit(self.widget_8)
        self.flag_ln.setObjectName("flag_ln")
        self.horizontalLayout_4.addWidget(self.flag_ln, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.length = QtWidgets.QLabel(self.widget_4)
        self.length.setStyleSheet("#length{\n"
                                  "font: 200 11pt Arial, Sans Serif;\n"
                                  "alignment: center;\n"
                                  "color: rgba(111, 75, 39, 0.77);\n"
                                  "}")
        self.length.setObjectName("length")
        self.horizontalLayout_5.addWidget(self.length, 0, QtCore.Qt.AlignHCenter)
        self.length_ln = QtWidgets.QLineEdit(self.widget_4)
        self.length_ln.setObjectName("length_ln")
        self.horizontalLayout_5.addWidget(self.length_ln, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.quantity = QtWidgets.QLabel(self.widget_5)
        self.quantity.setStyleSheet("#quantity{\n"
                                    "font: 200 11pt Arial, Sans Serif;\n"
                                    "alignment: center;\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "}")
        self.quantity.setObjectName("quantity")
        self.horizontalLayout_6.addWidget(self.quantity, 0, QtCore.Qt.AlignHCenter)
        self.quantity_ln = QtWidgets.QLineEdit(self.widget_5)
        self.quantity_ln.setObjectName("quantity_ln")
        self.horizontalLayout_6.addWidget(self.quantity_ln, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.unit = QtWidgets.QLabel(self.widget_9)
        self.unit.setStyleSheet("#unit{\n"
                                "font: 200 11pt Arial, Sans Serif;\n"
                                "alignment: center;\n"
                                "color: rgba(111, 75, 39, 0.77);\n"
                                "}")
        self.unit.setObjectName("unit")
        self.horizontalLayout_7.addWidget(self.unit, 0, QtCore.Qt.AlignHCenter)
        self.unit_comboBox = QtWidgets.QComboBox(self.widget_9)
        self.unit_comboBox.setStyleSheet("#unit_comboBox{\n"
                                         "font: 200 11pt Arial, Sans Serif;\n"
                                         "alignment: center;\n"
                                         "color: rgba(111, 75, 39, 0.77);\n"
                                         "}")
        self.unit_comboBox.setObjectName("unit_comboBox")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.unit_comboBox, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.calculateBtn = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculateBtn.sizePolicy().hasHeightForWidth())
        self.calculateBtn.setSizePolicy(sizePolicy)
        self.calculateBtn.setStyleSheet("#calculateBtn{\n"
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
                                        "#calculateBtn:hover{\n"
                                        "color: rgb(144,115,87);\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}")
        self.calculateBtn.setObjectName("calculateBtn")
        self.calculateBtn.clicked.connect(self.calculate)
        self.horizontalLayout_8.addWidget(self.calculateBtn)
        self.closeBtn = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setStyleSheet("#closeBtn{\n"
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
                                    "#closeBtn:hover{\n"
                                    "color: rgb(144,115,87);\n"
                                    "border :2px solid rgb\n"
                                    "#6A6E72;\n"
                                    "background-color: white;\n"
                                    "}")
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.clicked.connect(Dialog.close)
        self.horizontalLayout_8.addWidget(self.closeBtn)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setContentsMargins(10, 0, 8, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.result = QtWidgets.QLabel(self.widget_10)
        self.result.setStyleSheet("#result{\n"
                                  "font: 200 12pt Segoe UI Black;\n"
                                  "alignment: center;\n"
                                  "}")
        self.result.setObjectName("result")
        self.verticalLayout_3.addWidget(self.result, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Curb and Gutter Barrier Calculator"))
        self.CDepth.setText(_translate("Dialog", "Curb Depth:"))
        self.GWidth.setText(_translate("Dialog", "Gutter Width:"))
        self.CHeight.setText(_translate("Dialog", "Curb Height:"))
        self.FThickness.setText(_translate("Dialog", "Flag Thickness:"))
        self.length.setText(_translate("Dialog", "Length:"))
        self.quantity.setText(_translate("Dialog", "Quantity:"))
        self.unit.setText(_translate("Dialog", "Unit"))
        self.unit_comboBox.setItemText(0, _translate("Dialog", "Inches"))
        self.unit_comboBox.setItemText(1, _translate("Dialog", "Feet"))
        self.unit_comboBox.setItemText(2, _translate("Dialog", "Yards"))
        self.unit_comboBox.setItemText(3, _translate("Dialog", "Meters"))
        self.unit_comboBox.setItemText(4, _translate("Dialog", "Centimeters"))
        self.calculateBtn.setText(_translate("Dialog", "Calculate"))
        self.closeBtn.setText(_translate("Dialog", "Close"))

    def calculate(self):
        try:
            # Input values
            curb_depth = float(self.curb_ln.text())
            gutter_width = float(self.gut_ln.text())
            curb_height = float(self.CuHeight_ln.text())
            flag_thickness = float(self.flag_ln.text())
            length = float(self.length_ln.text())
            quantity = float(self.quantity_ln.text())

            # Convert length to inches
            unit = self.unit_comboBox.currentText()
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
            self.result.setText(result)
            self.result.setStyleSheet("font-size: 14pt; font-family: Inter; font-weight: Bold;")


        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = curb()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
