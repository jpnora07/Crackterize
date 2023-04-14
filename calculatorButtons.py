import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from Circular_Slab_or_Tube import circular
from Curb_Gutter_Barrier import curb
from Hole_Column_RoundFootings import hole
from concretevolumecalc import concrete_cal
from scientific_calculator import sci_Calculator
from stairs import stairs


class cal_dialog(object):
    def __init__(self, background_widget):
        self.background_widget = background_widget
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setStyleSheet(
            """
            background:rgb(255, 255, 255);
            """
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_10 = QtWidgets.QWidget(self.widget_4)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout.addWidget(self.widget_10)
        self.exit = QtWidgets.QPushButton(self.widget_4)
        self.exit.setMinimumSize(QtCore.QSize(30, 30))
        self.exit.setMaximumSize(QtCore.QSize(30, 30))
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.exit_function)
        self.horizontalLayout.addWidget(self.exit)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("#label{\n"
                                 
                                             "  background-color: transparent;  \n"
                                 "    font: 900 34pt \"Segoe UI Black\";\n"
                                 "    alignment: center;\n"
                                 "    color: rgba(111, 75, 39, 0.77);\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scientific = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scientific.sizePolicy().hasHeightForWidth())
        self.scientific.setSizePolicy(sizePolicy)
        self.scientific.clicked.connect(self.scifi_function)
        self.scientific.setStyleSheet("#scientific{\n"
                                      "font-weight:bold;\n"
                                      "color: white;\n"
                                      "background-color: #6F4B27;\n"
                                      "font-family: Inter;\n"
                                      "border-top-left-radius: 7px;\n"
                                      "border-top-right-radius: 7px;\n"
                                      "border-bottom-left-radius: 7px;\n"
                                      "border-bottom-right-radius: 7px;\n"
                                      "font-size: 15px;\n"
                                      "text-align: center;\n"
                                      "}\n"
                                      "#scientific:hover{\n"
                                      "color: rgb(144,115,87);\n"
                                      "border : 3px solid rgb(144,115,87);\n"
                                      "background-color: white;\n"
                                      "}\n"
                                      "")
        self.scientific.setFlat(False)
        self.scientific.setObjectName("scientific")
        self.verticalLayout_3.addWidget(self.scientific)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stairs = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stairs.sizePolicy().hasHeightForWidth())
        self.stairs.setSizePolicy(sizePolicy)
        self.stairs.clicked.connect(self.stairs_function)
        self.stairs.setStyleSheet("#stairs{\n"
                                  "font-weight:bold;\n"
                                  "color: white;\n"
                                  "background-color: #6F4B27;\n"
                                  "border-top-left-radius: 7px;\n"
                                  "border-top-right-radius: 7px;\n"
                                  "border-bottom-left-radius: 7px;\n"
                                  "border-bottom-right-radius: 7px;\n"
                                  "font-family: Inter;\n"
                                  "font-size: 15px;\n"
                                  "text-align: center;\n"
                                  "}\n"
                                  "#stairs:hover{\n"
                                  "color: rgb(144,115,87);\n"
                                  "border : 3px solid rgb(144,115,87);\n"
                                  "background-color: white;\n"
                                  "}\n"
                                  "")
        self.stairs.setObjectName("stairs")
        self.verticalLayout_5.addWidget(self.stairs)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_6.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.curbgutter = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curbgutter.sizePolicy().hasHeightForWidth())
        self.curbgutter.setSizePolicy(sizePolicy)
        self.curbgutter.clicked.connect(self.curbgutter_function)
        self.curbgutter.setStyleSheet("#curbgutter{\n"
                                      "font-weight:bold;\n"
                                      "color: white;\n"
                                      "background-color: #6F4B27;\n"
                                      "border-top-left-radius: 7px;\n"
                                      "border-top-right-radius: 7px;\n"
                                      "border-bottom-left-radius: 7px;\n"
                                      "border-bottom-right-radius: 7px;\n"
                                      "font-family: Inter;\n"
                                      "font-size: 15px;\n"
                                      "text-align: center;\n"
                                      "}\n"
                                      "#curbgutter:hover{\n"
                                      "color: rgb(144,115,87);\n"
                                      "border : 3px solid rgb(144,115,87);\n"
                                      "background-color: white;\n"
                                      "}\n"
                                      "")
        self.curbgutter.setObjectName("curbgutter")
        self.verticalLayout_6.addWidget(self.curbgutter)
        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_7.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.slabssquare = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slabssquare.sizePolicy().hasHeightForWidth())
        self.slabssquare.setSizePolicy(sizePolicy)
        self.slabssquare.clicked.connect(self.slabssquare_function)
        self.slabssquare.setStyleSheet("#slabssquare{\n"
                                       "font-weight:bold;\n"
                                       "color: white;\n"
                                       "background-color: #6F4B27;\n"
                                       "border-top-left-radius: 7px;\n"
                                       "border-top-right-radius: 7px;\n"
                                       "border-bottom-left-radius: 7px;\n"
                                       "border-bottom-right-radius: 7px;\n"
                                       "font-family: Inter;\n"
                                       "font-size: 15px;\n"
                                       "text-align: center;\n"
                                       "}\n"
                                       "#slabssquare:hover{\n"
                                       "color: rgb(144,115,87);\n"
                                       "border : 3px solid rgb(144,115,87);\n"
                                       "background-color: white;\n"
                                       "}\n"
                                       "")
        self.slabssquare.setObjectName("slabssquare")
        self.verticalLayout_7.addWidget(self.slabssquare)
        self.verticalLayout_2.addWidget(self.widget_7)

        #
        self.widget_new = QtWidgets.QWidget(self.widget)
        self.widget_new.setObjectName("widget_7")
        self.verticalLayout_new = QtWidgets.QVBoxLayout(self.widget_new)
        self.verticalLayout_new.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_new.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_new.setSpacing(4)
        self.verticalLayout_new.setObjectName("verticalLayout_7")
        self.concrete_cal = QtWidgets.QPushButton("Concrete Calculator", self.widget_new)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concrete_cal.sizePolicy().hasHeightForWidth())
        self.concrete_cal.setSizePolicy(sizePolicy)
        self.concrete_cal.clicked.connect(self.concrete_function)
        self.concrete_cal.setStyleSheet("#concrete_cal{\n"
                                       "font-weight:bold;\n"
                                       "color: white;\n"
                                       "background-color: #6F4B27;\n"
                                       "border-top-left-radius: 7px;\n"
                                       "border-top-right-radius: 7px;\n"
                                       "border-bottom-left-radius: 7px;\n"
                                       "border-bottom-right-radius: 7px;\n"
                                       "font-family: Inter;\n"
                                       "font-size: 15px;\n"
                                       "text-align: center;\n"
                                       "}\n"
                                       "#concrete_cal:hover{\n"
                                       "color: rgb(144,115,87);\n"
                                       "border : 3px solid rgb(144,115,87);\n"
                                       "background-color: white;\n"
                                       "}\n"
                                       "")
        self.concrete_cal.setObjectName("concrete_cal")
        self.verticalLayout_new.addWidget(self.concrete_cal)
        self.verticalLayout_2.addWidget(self.widget_new)
        #

        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_8.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.holecolumn = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.holecolumn.sizePolicy().hasHeightForWidth())
        self.holecolumn.setSizePolicy(sizePolicy)
        self.holecolumn.clicked.connect(self.holecolumn_function)
        self.holecolumn.setStyleSheet("#holecolumn{\n"
                                      "font-weight:bold;\n"
                                      "color: white;\n"
                                      "background-color: #6F4B27;\n"
                                      "border-top-left-radius: 7px;\n"
                                      "border-top-right-radius: 7px;\n"
                                      "border-bottom-left-radius: 7px;\n"
                                      "border-bottom-right-radius: 7px;\n"
                                      "font-family: Inter;\n"
                                      "font-size: 15px;\n"
                                      "text-align: center;\n"
                                      "}\n"
                                      "#holecolumn:hover{\n"
                                      "color: rgb(144,115,87);\n"
                                      "border : 3px solid rgb(144,115,87);\n"
                                      "background-color: white;\n"
                                      "}\n"
                                      "")
        self.holecolumn.setObjectName("holecolumn")
        self.verticalLayout_8.addWidget(self.holecolumn)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_9.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.circularslab = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.circularslab.sizePolicy().hasHeightForWidth())
        self.circularslab.setSizePolicy(sizePolicy)
        self.circularslab.clicked.connect(self.circularslab_function)
        self.circularslab.setStyleSheet("#circularslab{\n"
                                        "font-weight:bold;\n"
                                        "color: white;\n"
                                        "background-color: #6F4B27;\n"
                                        "border-top-left-radius: 7px;\n"
                                        "border-top-right-radius: 7px;\n"
                                        "border-bottom-left-radius: 7px;\n"
                                        "border-bottom-right-radius: 7px;\n"
                                        "font-family: Inter;\n"
                                        "font-size: 15px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "#circularslab:hover{\n"
                                        "color: rgb(144,115,87);\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}\n"
                                        "")
        self.circularslab.setObjectName("circularslab")
        self.verticalLayout_9.addWidget(self.circularslab)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Calculator"))
        self.scientific.setText(_translate("Dialog", "Scientific Calculator"))
        self.stairs.setText(_translate("Dialog", "Stairs Calculator"))
        self.curbgutter.setText(_translate("Dialog", "Curb and Gutter Barrier Calculator"))
        self.slabssquare.setText(_translate("Dialog", "Slabs / Square Footings Calculator"))
        self.holecolumn.setText(_translate("Dialog", "Hole / Round Footings Calculator"))
        self.circularslab.setText(_translate("Dialog", "Circular Slab or Tube Calculator"))

    def exit_function(self):
        self.Dialog.close()
        self.background_widget.hide()
    def scifi_function(self):
        try:

            ui = sci_Calculator() #class name of file dialog
            ui.move(
                QtWidgets.QApplication.desktop().screen().rect().center() - ui.rect().center()
            )
            ui.show()
            ui.exec_()

        except Exception as e:
            print(e)

    def concrete_function(self):
        try:
            concrete_call = QtWidgets.QDialog(self.Dialog)
            x = (self.Dialog.width() - self.Dialog.width()) // 2
            y = (self.Dialog.height() - self.Dialog.height()) // 2
            ui = concrete_cal()

            ui.setupUi(concrete_call)
            concrete_call.move(x, y)
            concrete_call.show()
            concrete_call.exec_()
        except Exception as e:
            print(e)

    def stairs_function(self):
        try:

            qstairs = QtWidgets.QDialog(self.Dialog)
            x = (self.Dialog.width() - self.Dialog.width()) // 2
            y = (self.Dialog.height() - self.Dialog.height()) // 2
            ui = stairs()

            ui.setupUi(qstairs)
            qstairs.move(x, y)
            qstairs.show()
            qstairs.exec_()
        except Exception as e:
            print(e)

    def curbgutter_function(self):
        try:

            curbgutterCalc = QtWidgets.QDialog(self.Dialog)
            x = (self.Dialog.width() - self.Dialog.width()) // 2
            y = (self.Dialog.height() - self.Dialog.height()) // 2
            ui = curb()

            ui.setupUi(curbgutterCalc)
            curbgutterCalc.move(x, y)
            curbgutterCalc.show()
            curbgutterCalc.exec_()
        except Exception as e:
            print(e)

    def slabssquare_function(self):
        try:

            slabs_wallsfootings = QtWidgets.QDialog(self.Dialog)
            x = (self.Dialog.width() - self.Dialog.width()) // 2
            y = (self.Dialog.height() - self.Dialog.height()) // 2
            ui = curb()

            ui.setupUi(slabs_wallsfootings)
            slabs_wallsfootings.move(x, y)
            slabs_wallsfootings.show()
            slabs_wallsfootings.exec_()
        except Exception as e:
            print(e)

    def holecolumn_function(self):
        try:
            holecolumn = QtWidgets.QDialog(self.Dialog)
            x = (self.Dialog.width() - self.Dialog.width()) // 2
            y = (self.Dialog.height() - self.Dialog.height()) // 2
            ui = hole()

            ui.setupUi(holecolumn)
            holecolumn.move(x, y)
            holecolumn.show()
            holecolumn.exec_()
        except Exception as e:
            print(e)

    def circularslab_function(self):
        try:
            circularslabcalc = QtWidgets.QDialog(self.Dialog)
            x = (self.Dialog.width() - self.Dialog.width()) // 2
            y = (self.Dialog.height() - self.Dialog.height()) // 2
            ui = circular()

            ui.setupUi(circularslabcalc)
            circularslabcalc.move(x, y)
            circularslabcalc.show()
            circularslabcalc.exec_()
        except Exception as e:
            print(e)

