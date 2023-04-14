from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class stairs(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
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
                                 "font: 200 15pt Segoe UI Black;\n"
                                 "alignment: center;\n"
                                 "color: rgba(111, 75, 39, 0.77);\n"
                                 "                                 }")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
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
        self.run_lineEdit = QtWidgets.QLineEdit(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_lineEdit.sizePolicy().hasHeightForWidth())
        self.run_lineEdit.setSizePolicy(sizePolicy)
        self.run_lineEdit.setObjectName("run_lineEdit")
        self.horizontalLayout.addWidget(self.run_lineEdit, 0, QtCore.Qt.AlignLeft)
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
        self.rise_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.rise_lineEdit.setObjectName("rise_lineEdit")
        self.horizontalLayout_2.addWidget(self.rise_lineEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setStyleSheet("#label_8{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.width_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.width_lineEdit.setObjectName("width_lineEdit")
        self.horizontalLayout_3.addWidget(self.width_lineEdit, 0, QtCore.Qt.AlignLeft)
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
        self.depth_lineEdit = QtWidgets.QLineEdit(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depth_lineEdit.sizePolicy().hasHeightForWidth())
        self.depth_lineEdit.setSizePolicy(sizePolicy)
        self.depth_lineEdit.setObjectName("depth_lineEdit")
        self.horizontalLayout_4.addWidget(self.depth_lineEdit, 0, QtCore.Qt.AlignLeft)
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
        self.steps_lineEdit = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steps_lineEdit.sizePolicy().hasHeightForWidth())
        self.steps_lineEdit.setSizePolicy(sizePolicy)
        self.steps_lineEdit.setObjectName("steps_lineEdit")
        self.horizontalLayout_5.addWidget(self.steps_lineEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.unit_comboBox = QtWidgets.QComboBox(self.widget_5)
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
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.unit_comboBox)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.calculateBtn = QtWidgets.QPushButton(self.widget_9)
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
        self.horizontalLayout_7.addWidget(self.calculateBtn)
        self.closeBtn = QtWidgets.QPushButton(self.widget_9)
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
                                    "color: #6A6E72;\n"
                                    "border :2px solid #6A6E72;\n"
                                    "background-color: white;\n"
                                    "}")
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.clicked.connect(Dialog.close)
        self.horizontalLayout_7.addWidget(self.closeBtn)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.result = QtWidgets.QLabel(self.widget_6)
        self.result.setStyleSheet("#result{\n"
                                  "  background-color: transparent;  \n"
                                  "font: 200 10pt Segoe UI Black;\n"
                                  "alignment: center;\n"
                                  "}")
        self.result.setObjectName("result")
        self.horizontalLayout_8.addWidget(self.result)
        self.verticalLayout_2.addWidget(self.widget_6, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Stairs Calculator"))
        self.label_4.setText(_translate("Dialog", "Run:"))
        self.label_5.setText(_translate("Dialog", "Rise:"))
        self.label_8.setText(_translate("Dialog", "Width:"))
        self.label_6.setText(_translate("Dialog", "Platform Depth:"))
        self.label_7.setText(_translate("Dialog", "Number of Steps:"))
        self.label_2.setText(_translate("Dialog", "Units:"))
        self.unit_comboBox.setItemText(0, _translate("Dialog", "Inches"))
        self.unit_comboBox.setItemText(1, _translate("Dialog", "Feet"))
        self.unit_comboBox.setItemText(2, _translate("Dialog", "Yards"))
        self.unit_comboBox.setItemText(3, _translate("Dialog", "Meters"))
        self.unit_comboBox.setItemText(4, _translate("Dialog", "Centimeters"))
        self.calculateBtn.setText(_translate("Dialog", "Calculate"))
        self.closeBtn.setText(_translate("Dialog", "Close"))

    def calculate(self):
        try:
            # Get input values
            run = float(self.run_lineEdit.text())
            rise = float(self.rise_lineEdit.text())
            width = float(self.width_lineEdit.text())
            platform_depth = float(self.depth_lineEdit.text())
            num_steps = int(self.steps_lineEdit.text())

            # Convert input values to inches based on selected unit
            units = self.unit_comboBox.currentText()
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
            self.result.setText(f'Total stair height: {total_height:.2f} inches\nSlope: {slope:.2f}')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = stairs()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
