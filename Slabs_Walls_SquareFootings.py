
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class slabs(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("#widget{\n"
                                 
                                  "border-top-left-radius: 10px;\n"
                                  "border-top-right-radius: 10px;\n"
                                  "border-bottom-left-radius: 10px;\n"
                                  "border-bottom-right-radius: 10px;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
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
                                 "  background-color: transparent;  \n"
                                 "font: 200 13pt Segoe UI Black;\n"
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
        self.label_4 = QtWidgets.QLabel(self.widget_11)
        self.label_4.setStyleSheet("#label_4{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.length_lineEdit = QtWidgets.QLineEdit(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_lineEdit.sizePolicy().hasHeightForWidth())
        self.length_lineEdit.setSizePolicy(sizePolicy)
        self.length_lineEdit.setObjectName("length_lineEdit")
        self.horizontalLayout.addWidget(self.length_lineEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setStyleSheet("#label_5{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.width_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.width_lineEdit.setObjectName("width_lineEdit")
        self.horizontalLayout_2.addWidget(self.width_lineEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CHeight = QtWidgets.QLabel(self.widget_3)
        self.CHeight.setStyleSheet("#CHeight{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.CHeight.setObjectName("CHeight")
        self.horizontalLayout_3.addWidget(self.CHeight, 0, QtCore.Qt.AlignHCenter)
        self.thickHeight_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.thickHeight_lineEdit.setObjectName("thickHeight_lineEdit")
        self.horizontalLayout_3.addWidget(self.thickHeight_lineEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        self.label_6.setStyleSheet("#label_6{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setStyleSheet("#label_7{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.unit_comboBox = QtWidgets.QComboBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_comboBox.sizePolicy().hasHeightForWidth())
        self.unit_comboBox.setSizePolicy(sizePolicy)
        self.unit_comboBox.setStyleSheet("#unit_comboBox{\n"
                                         "font: 200 11pt Arial, Sans Serif;\n"
                                         "alignment: center;\n"
                                         "color: rgba(111, 75, 39, 0.77);\n"
                                         "}")
        self.unit_comboBox.setObjectName("unit_comboBox")
        self.unit_comboBox.addItem("Inches")
        self.unit_comboBox.addItem("Feet")
        self.unit_comboBox.addItem("Yards")
        self.unit_comboBox.addItem("Meters")
        self.unit_comboBox.addItem("Centimeters")
        self.horizontalLayout_5.addWidget(self.unit_comboBox, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.calculateBtn = QtWidgets.QPushButton(self.widget_5)
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
        self.horizontalLayout_6.addWidget(self.calculateBtn)
        self.closeBtn = QtWidgets.QPushButton(self.widget_5)
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
        self.horizontalLayout_6.addWidget(self.closeBtn)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget_9)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 500 12pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.total_area = QtWidgets.QLabel(self.widget_9)
        self.total_area.setStyleSheet("#total_area{\n"
                                      "  background-color: transparent;  \n"
                                      "font: 200 10pt Segoe UI Black;\n"
                                      "alignment: center;\n"
                                      "}")
        self.total_area.setObjectName("total_area")
        self.horizontalLayout_7.addWidget(self.total_area)
        self.verticalLayout_2.addWidget(self.widget_9, 0, QtCore.Qt.AlignHCenter)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 500 12pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.total_volume = QtWidgets.QLabel(self.widget_6)
        self.total_volume.setStyleSheet("#total_volume{\n"
                                        "  background-color: transparent;  \n"
                                        "font: 200 10pt Segoe UI Black;\n"
                                        "alignment: center;\n"
                                        "}")
        self.total_volume.setObjectName("total_volume")
        self.horizontalLayout_8.addWidget(self.total_volume)
        self.verticalLayout_2.addWidget(self.widget_6, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Slabs, Walls, and Square Footings Calculator"))
        self.label_4.setText(_translate("Dialog", "Length:"))
        self.label_5.setText(_translate("Dialog", "Width:"))
        self.CHeight.setText(_translate("Dialog", "Thickness/Height:"))
        self.label_7.setText(_translate("Dialog", "Units:"))
        self.unit_comboBox.setItemText(0, _translate("Dialog", "Inches"))
        self.unit_comboBox.setItemText(1, _translate("Dialog", "Feet"))
        self.unit_comboBox.setItemText(2, _translate("Dialog", "Yards"))
        self.unit_comboBox.setItemText(3, _translate("Dialog", "Meters"))
        self.unit_comboBox.setItemText(4, _translate("Dialog", "Centimeters"))
        self.calculateBtn.setText(_translate("Dialog", "Calculate"))
        self.closeBtn.setText(_translate("Dialog", "Close"))
        self.label_2.setText(_translate("Dialog", "Total Area: "))
        self.label_3.setText(_translate("Dialog", "Total Volume: "))

    def calculate(self):
        length = float(self.length_lineEdit.text())
        width = float(self.width_lineEdit.text())
        thickness = float(self.thickHeight_lineEdit.text())
        units = self.unit_comboBox.currentText()

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

        self.total_area.setText(f"{area:.2f} sq. {units.lower()}")
        self.total_volume.setText(f"{volume:.2f} cu. {units.lower()}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = slabs()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
