# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'concreteCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog


class concrete_cal(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Concrete Calculator")
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
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("#label{\n"
                                 "  background-color: transparent;  \n"
                                 "font: 200 15pt Segoe UI Black;\n"
                                 "alignment: center;\n"
                                 "color: rgba(111, 75, 39, 0.77);\n"
                                 "                                 }")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial, Sans Serif;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.length_lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.length_lineEdit.setObjectName("length_lineEdit")
        self.verticalLayout_4.addWidget(self.length_lineEdit)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.width_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.width_lineEdit.setObjectName("width_lineEdit")
        self.verticalLayout_5.addWidget(self.width_lineEdit)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setStyleSheet("#label_4{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.thickness_lineEdit = QtWidgets.QLineEdit(self.widget_6)
        self.thickness_lineEdit.setObjectName("thickness_lineEdit")
        self.verticalLayout_6.addWidget(self.thickness_lineEdit)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.widget_9)
        self.label_5.setStyleSheet("#label_5{\n"
                                   "  background-color: transparent;  \n"
                                   "font: 200 11pt Arial;\n"
                                   "alignment: center;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.type_comboBox = QtWidgets.QComboBox(self.widget_9)
        self.type_comboBox.setStyleSheet("#comboBox{\n"
                                         "font: 11pt Arial;\n"
                                         "alignment: center;\n"
                                         "color: rgba(111, 75, 39, 0.77);\n"
                                         "}")
        self.type_comboBox.setObjectName("type_comboBox")
        self.type_comboBox.addItem('Square Slab')
        self.type_comboBox.addItem('Round Slab')
        self.type_comboBox.addItem('Wall')
        self.type_comboBox.addItem('Footer')
        self.type_comboBox.addItem('Square Column')
        self.type_comboBox.addItem('Round Column')
        self.type_comboBox.addItem('Steps')
        self.type_comboBox.addItem('Curb & Gutter')
        self.verticalLayout_10.addWidget(self.type_comboBox)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setContentsMargins(82, 0, 82, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.calculateBtn = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculateBtn.sizePolicy().hasHeightForWidth())
        self.calculateBtn.setSizePolicy(sizePolicy)
        self.calculateBtn.setMinimumSize(QtCore.QSize(24, 0))
        self.calculateBtn.setStyleSheet("#calculateBtn{\n"
                                        "font-weight:bold;\n"
                                        "color: white;\n"
                                        "background-color: #6F4B27;\n"
                                        "font-family: Inter;\n"
                                        "border-top-left-radius: 12px;\n"
                                        "border-top-right-radius: 12px;\n"
                                        "border-bottom-left-radius: 12px;\n"
                                        "border-bottom-right-radius: 12px;\n"
                                        "font-size: 15px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "#calculateBtn:hover{\n"
                                        "color: rgb(144,115,87);\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}")
        self.calculateBtn.setFlat(False)
        self.calculateBtn.setObjectName("calculateBtn")
        self.calculateBtn.clicked.connect(self.calculate_concrete)
        self.verticalLayout_7.addWidget(self.calculateBtn)
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
                                    "border-top-left-radius: 12px;\n"
                                    "border-top-right-radius: 12px;\n"
                                    "border-bottom-left-radius: 12px;\n"
                                    "border-bottom-right-radius: 12px;\n"
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
        self.verticalLayout_7.addWidget(self.closeBtn)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.result = QtWidgets.QLabel(self.widget_8)
        self.result.setStyleSheet("#result{\n"
                                  "  background-color: transparent;  \n"
                                  "font: 200 12pt Segoe UI Black;\n"
                                  "alignment: center;\n"
                                  "}")
        self.result.setObjectName("result")
        self.verticalLayout_9.addWidget(self.result)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Concrete Calculator"))
        self.label_2.setText(_translate("Dialog", "Length (ft)"))
        self.label_3.setText(_translate("Dialog", "Width (ft)"))
        self.label_4.setText(_translate("Dialog", "Thickness (in)"))
        self.label_5.setText(_translate("Dialog", "Concrete Type"))
        self.type_comboBox.setItemText(0, _translate("Dialog", "Square Slab"))
        self.type_comboBox.setItemText(1, _translate("Dialog", "Round Slab"))
        self.type_comboBox.setItemText(2, _translate("Dialog", "Wall"))
        self.type_comboBox.setItemText(3, _translate("Dialog", "Footer"))
        self.type_comboBox.setItemText(4, _translate("Dialog", "Square Column"))
        self.type_comboBox.setItemText(5, _translate("Dialog", "Round Column"))
        self.type_comboBox.setItemText(6, _translate("Dialog", "Steps"))
        self.type_comboBox.setItemText(7, _translate("Dialog", "Curb & Gutter"))
        self.calculateBtn.setText(_translate("Dialog", "Calculate"))
        self.closeBtn.setText(_translate("Dialog", "Close"))
        self.result.setText(_translate("Dialog", " "))

    def calculate_concrete(self):
        try:
            self.calculate_concrete()
            length = float(self.length_lineEdit.text())
            width = float(self.width_lineEdit.text())
            thickness = float(self.thickness_lineEdit.text())
            concrete_type = self.type_comboBox.currentText()

            if concrete_type == 'Standard':
                weight_per_cubic_ft = 150
            else:
                weight_per_cubic_ft = 160

                volume = length * width * (thickness / 12.0)
                weight = volume * weight_per_cubic_ft
                cubic_yards = volume / 27.0

                self.result.setText('You will need %.2f pounds or %.2f cubic yards of %s concrete.' % (
                    weight, cubic_yards, concrete_type.lower()))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = concrete_cal()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
