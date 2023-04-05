import os
import sqlite3
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QIODevice, QBuffer, QByteArray, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QPushButton, QLabel, QHBoxLayout, QLayout, QMessageBox

from add_details_of_cracks import add_details_dialog


class Result_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        Dialog.setMaximumSize(QtCore.QSize(700, 600))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(15)
        effect.setColor(QtGui.QColor(144, 115, 87, 100))
        effect.setOffset(0, 0)
        radius = 15
        Dialog.setStyleSheet("""
                                            background:#EFEEEE;
                                            border-top-left-radius:{0}px;
                                            border-bottom-left-radius:{0}px;
                                            border-top-right-radius:{0}px;
                                            border-bottom-right-radius:{0}px;
                                            """.format(radius))
        Dialog.setGraphicsEffect(effect)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget_16 = QtWidgets.QWidget(self.widget)
        self.widget_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.exit = QtWidgets.QPushButton(self.widget_16)
        self.exit.setMinimumSize(QtCore.QSize(0, 25))
        self.exit.clicked.connect(Dialog.close)
        self.exit.setMaximumSize(QtCore.QSize(25, 25))
        self.exit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.exit.setDefault(False)
        self.exit.setFlat(True)

        ExitIcon = QtGui.QIcon()
        ExitIcon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(ExitIcon)
        self.exit.setIconSize(QtCore.QSize(30, 30))

        self.exit.setObjectName("exit")
        self.verticalLayout_5.addWidget(self.exit)

        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.addWidget(self.widget_16)
        self.verticalLayout.setContentsMargins(-1, 9, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WithLogo = QtWidgets.QWidget(self.widget)
        self.WithLogo.setMinimumSize(QtCore.QSize(500, 80))
        self.WithLogo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.WithLogo.setStyleSheet("#WithLogo{border-image: url(images/Crackterize.png) 400 0 400 0 stretch;}")
        self.WithLogo.setObjectName("WithLogo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WithLogo)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addWidget(self.WithLogo)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setMaximumSize(QtCore.QSize(340, 16777215))
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.result_Img = QtWidgets.QLabel(self.widget_12)
        self.result_Img.setMinimumSize(QtCore.QSize(300, 300))
        self.result_Img.setAlignment(QtCore.Qt.AlignCenter)
        self.result_Img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.result_Img.setStyleSheet("#result_Img{\n"

                                      "opacity: 100;\n"
                                      "border: 1px solid grey;\n"
                                      "}")
        self.result_Img.setObjectName("result_Img")
        file_path_Class = 'Predicted_Class_name.txt'
        if os.path.isfile(file_path_Class):
            with open(file_path_Class, 'r') as f:
                status = f.read()
                if status.strip() == 'No Detected Crack':
                    self.image = cv2.imread('bg.jpg')
                else:
                    self.image = cv2.imread('threshold_image.jpg')
        else:
            print('Error: Predicted_Class_name.txt does not exist')

        self.update_image(self.image)
        self.horizontalLayout_9.addWidget(self.result_Img)
        self.horizontalLayout_2.addWidget(self.widget_12)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(280, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(280, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.concretecracked_2 = QtWidgets.QLabel(self.widget_6)
        self.concretecracked_2.setStyleSheet("#concretecracked_2{\n"
                                             "    \n"
                                             "color: #2E74A9;\n"
                                             "font: bold;\n"
                                             "border: 2px solid #EFEEEE;\n"
                                             "font-size: 20px;\n"
                                             "border-bottom-color: rgb(172, 172, 172);;\n"
                                             "}")
        self.concretecracked_2.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked_2.setWordWrap(True)
        self.concretecracked_2.setObjectName("concretecracked_2")
        self.verticalLayout_2.addWidget(self.concretecracked_2)
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.widget_10)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.lengthlbl = QtWidgets.QLabel(self.widget_10)
        self.lengthlbl.setStyleSheet("#lengthlbl{\n"
                                     "    color:  #555555;\n"
                                     "font: bold;\n"
                                     "    font-size: 15px}")
        self.lengthlbl.setObjectName("lengthlbl")
        file_path_length = 'Predicted_height.txt'
        if os.path.isfile(file_path_length):
            with open(file_path_length, 'r') as f:
                self.length = f.read()
            self.lengthlbl.setText(self.length + " cm")
        else:
            self.lengthlbl.setText('0 cm')
        self.horizontalLayout_10.addWidget(self.lengthlbl)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_13 = QtWidgets.QWidget(self.widget_6)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.widget_13)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.widthlbl = QtWidgets.QLabel(self.widget_13)
        self.widthlbl.setStyleSheet("#widthlbl{\n"
                                    "    color:  #555555;\n"
                                    "font: bold;\n"
                                    "    font-size: 15px;\n"
                                    "}")
        self.widthlbl.setObjectName("widthlbl")
        file_path_Width = 'Predicted_width.txt'
        if os.path.isfile(file_path_Width):
            with open(file_path_Width, 'r') as f:
                self.width = f.read()
            self.widthlbl.setText(self.width + " mm")
        else:
            self.widthlbl.setText('0 mm')
        self.horizontalLayout_11.addWidget(self.widthlbl)
        self.verticalLayout_2.addWidget(self.widget_13)
        self.widget_11 = QtWidgets.QWidget(self.widget_6)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widgetPosition = QtWidgets.QLabel(self.widget_11)
        self.widgetPosition.setStyleSheet("#widgetPosition{\n"
                                          "color: rgba(111, 75, 39, 0.77);\n"
                                          "font-size: 13px;\n"
                                          "font-weight: bold;\n"
                                          "}")
        self.widgetPosition.setObjectName("widgetPosition")
        self.horizontalLayout_13.addWidget(self.widgetPosition)
        self.position_lbl = QtWidgets.QLabel(self.widget_11)
        self.position_lbl.setStyleSheet("#position_lbl{\n"
                                        "    color:  #555555;\n"
                                        "font: bold;\n"
                                        "    font-size: 15px;\n"
                                        "}")
        self.position_lbl.setObjectName("position_lbl")
        self.horizontalLayout_13.addWidget(self.position_lbl)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_15 = QtWidgets.QWidget(self.widget_6)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LabelPos = QtWidgets.QLabel(self.widget_15)
        self.LabelPos.setMinimumSize(QtCore.QSize(180, 0))
        self.LabelPos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LabelPos.setStyleSheet("#LabelPos{\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "font-size: 13px;\n"
                                    "font-weight: bold;\n"
                                    "}")
        self.LabelPos.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LabelPos.setWordWrap(True)
        self.LabelPos.setObjectName("LabelPos")
        self.verticalLayout_3.addWidget(self.LabelPos)
        self.verticalLayout_2.addWidget(self.widget_15)
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LabelNeg = QtWidgets.QLabel(self.widget_5)
        self.LabelNeg.setMinimumSize(QtCore.QSize(180, 0))
        self.LabelNeg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LabelNeg.setStyleSheet("#LabelNeg{\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "font-size: 13px;\n"
                                    "font-weight: bold;\n"
                                    "}")
        self.LabelNeg.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LabelNeg.setWordWrap(True)
        self.LabelNeg.setObjectName("LabelNeg")
        self.verticalLayout_4.addWidget(self.LabelNeg)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_14 = QtWidgets.QWidget(self.widget_6)
        self.widget_14.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.i = QtWidgets.QLabel(self.widget_14)
        self.i.setMinimumSize(QtCore.QSize(30, 30))
        self.i.setMaximumSize(QtCore.QSize(30, 30))
        self.i.setStyleSheet("#i{\n"
                             "    border-image: url(images/i.png)  ;}")
        self.i.setText("")
        self.i.setAlignment(QtCore.Qt.AlignCenter)
        self.i.setWordWrap(False)
        self.i.setObjectName("i")
        self.horizontalLayout_12.addWidget(self.i)
        self.concretecracked = QtWidgets.QLabel(self.widget_14)
        self.concretecracked.setStyleSheet("#concretecracked{\n"
                                           "color: #2E74A9;\n"
                                           "font: bold;\n"
                                           "font-size: 15px;\n"
                                           "}")
        self.concretecracked.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked.setWordWrap(True)

        file_path_Neg = 'Negative_score.txt'
        file_path_Pos = 'Positive_score.txt'
        if os.path.isfile(file_path_Neg and file_path_Pos and file_path_Class):
            with open(file_path_Neg, 'r') as f:
                self.Neg_score = f.read()
            self.LabelNeg.setText("Negative Crack Probability is " + self.Neg_score)
            with open(file_path_Pos, 'r') as f:
                self.Pos_score = f.read()
            self.LabelPos.setText("Positive Crack Probability is " + self.Pos_score)
            with open('Predicted_Class_name.txt', 'r') as f:
                self.status = f.read()

            self.concretecracked.setText("The image is classified as " + self.status + ".")
        else:
            self.concretecracked.setText("The image is classified as error.")

        self.concretecracked.setObjectName("concretecracked")
        self.horizontalLayout_12.addWidget(self.concretecracked)
        self.verticalLayout_2.addWidget(self.widget_14)
        self.widget_17 = QtWidgets.QWidget(self.widget_6)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.adddetails = QtWidgets.QPushButton(self.widget_17)

        self.adddetails.setMinimumSize(QtCore.QSize(0, 35))
        self.adddetails.setMaximumSize(QtCore.QSize(16777215, 35))
        self.adddetails.setStyleSheet("#adddetails{\n"
                                      "background: #2E74A9;\n"
                                      "font-weight:bold;\n"
                                      "color: white;\n"
                                      "border-radius: 7px;\n"
                                      "font-family: Inter;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "#adddetails:hover{\n"
                                      "color: #2E74A9;\n"
                                      "border : 3px solid  #2E74A9;\n"
                                      "background-color: white;\n"
                                      "}\n"
                                      "")

        self.adddetails.setObjectName("adddetails")
        try:
            file_path_Class = 'Predicted_Class_name.txt'
            if os.path.isfile(file_path_Class):
                with open(file_path_Class, 'r') as f:
                    status = f.read()
                    if status == 'No Detected Crack':
                        self.adddetails.hide()
                    else:
                        self.adddetails.show()
        except Exception as e:
            print(e)
        self.adddetails.clicked.connect(self.add_details_function)
        self.horizontalLayout.addWidget(self.adddetails)
        self.print1 = QtWidgets.QPushButton(self.widget_17)
        self.print1.setMinimumSize(QtCore.QSize(0, 35))
        self.print1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.print1.setStyleSheet("#print1{\n"

                                  "background: #6F4B27;\n"
                                  "font-weight:bold;\n"
                                  "color: white;\n"
                                  "border-radius: 7px;\n"
                                  "font-family: Inter;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#print1::hover{\n"

                                  "color: #6F4B27;\n"
                                  "border : 3px solid rgb(144,115,87);\n"
                                  "background-color: white;\n"
                                  "}\n"
                                  "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/print_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print1.setIcon(icon)
        self.print1.setIconSize(QtCore.QSize(30, 30))
        self.print1.setObjectName("print1")
        self.horizontalLayout.addWidget(self.print1)
        self.verticalLayout_2.addWidget(self.widget_17)
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.savebtn = QtWidgets.QPushButton(self.widget_2)
        self.savebtn.setMinimumSize(QtCore.QSize(0, 35))
        self.savebtn.clicked.connect(self.Choose_where_to_save)
        self.savebtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.savebtn.setStyleSheet("#savebtn{\n"
                                   "background: #2E74A9;\n"
                                   "font-weight:bold;\n"
                                   "color: white;\n"
                                   "border-radius: 7px;\n"
                                   "font-family: Inter;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "#savebtn::hover{\n"
                                   "color: #2E74A9;\n"
                                   "border : 3px solid  #2E74A9;\n"
                                   "background-color: white;\n"
                                   "}\n"
                                   "")
        self.savebtn.setObjectName("savebtn")
        self.horizontalLayout_5.addWidget(self.savebtn)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout_6.addWidget(self.widget)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.concretecracked_2.setText(_translate("Dialog", "Detected:"))
        self.label_2.setText(_translate("Dialog", "Length:"))
        self.label_3.setText(_translate("Dialog", "Width: "))
        self.widgetPosition.setText(_translate("Dialog", "Position:"))
        self.position_lbl.setText(_translate("Dialog", "Horizontal"))
        self.adddetails.setText(_translate("Dialog", "Add Details"))
        self.print1.setText(_translate("Dialog", "Print"))
        self.savebtn.setText(_translate("Dialog", "Save"))

    def add_details_function(self):
        try:
            result_dialog = QtWidgets.QDialog(self.Dialog)
            x = (self.Dialog.width() - self.Dialog.width()) // 2
            y = (self.Dialog.height() - self.Dialog.height()) // 2
            ui = add_details_dialog()

            ui.setupUi(result_dialog)
            result_dialog.move(x, y)
            result_dialog.show()
            result_dialog.exec_()

        except Exception as e:
            print(e)

    def Choose_where_to_save(self):
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 210)
        Dialog.setMaximumSize(QtCore.QSize(310, 210))
        Dialog.setStyleSheet(
            '''#Dialog{background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));width: fit-content; heigth: fit-content; block-size: fit-content;} ''')
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.existingproject = QtWidgets.QPushButton("Save Existing Project", self.widget_2)
        self.existingproject.clicked.connect(Dialog.close)
        self.existingproject.clicked.connect(self.Save_to_existing_Project)
        self.existingproject.clicked.connect(Dialog.close)
        self.existingproject.setMinimumSize(QtCore.QSize(70, 35))
        self.existingproject.setMaximumSize(QtCore.QSize(200, 35))
        self.existingproject.setStyleSheet("#existingproject{\n"
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
                                           "#existingproject:hover{\n"
                                           "color: rgb(144,115,87);\n"
                                           "border : 3px solid rgb(144,115,87);\n"
                                           "background-color: white;\n"
                                           "}\n"
                                           "")
        self.existingproject.setObjectName("existingproject")
        self.horizontalLayout_2.addWidget(self.existingproject)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.createnew = QtWidgets.QPushButton("Create New", self.widget_3)
        self.createnew.setMinimumSize(QtCore.QSize(200, 35))
        self.createnew.setMaximumSize(QtCore.QSize(200, 35))

        self.createnew.clicked.connect(Dialog.close)
        self.createnew.clicked.connect(self.creating_new_project)
        self.createnew.setStyleSheet("#createnew{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #2E74A9;\n"
                                     "border-top-left-radius: 7px;\n"
                                     "border-top-right-radius: 7px;\n"
                                     "border-bottom-left-radius: 7px;\n"
                                     "border-bottom-right-radius: 7px;\n"
                                     "font-family: Inter;\n"
                                     "font-size: 15px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#createnew:hover{\n"
                                     "color: #2E74A9;\n"
                                     "border : 3px solid  #2E74A9;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.createnew.setObjectName("createnew")
        self.horizontalLayout_3.addWidget(self.createnew)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.back = QtWidgets.QPushButton("Back", self.widget_4)
        self.back.setMinimumSize(QtCore.QSize(200, 35))
        self.back.setMaximumSize(QtCore.QSize(200, 35))
        self.back.clicked.connect(Dialog.close)
        self.back.setStyleSheet("#back{\n"
                                "font-weight:bold;\n"
                                "color: white;\n"
                                "background-color: #6A6E72;\n"
                                "border-top-left-radius: 7px;\n"
                                "border-top-right-radius: 7px;\n"
                                "border-bottom-left-radius: 7px;\n"
                                "border-bottom-right-radius: 7px;\n"
                                "font-family: Inter;\n"
                                "font-size: 15px;\n"
                                "text-align: center;\n"
                                "}\n"
                                "#back:hover{\n"
                                "color: #6A6E72;\n"
                                "border : 3px solid#6A6E72;\n"
                                "background-color: white;\n"
                                "}\n"
                                "")
        self.back.setObjectName("back")
        self.horizontalLayout_4.addWidget(self.back)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.exec()

    def Save_to_existing_Project(self):
        self.existing_folder_dialog = QtWidgets.QDialog()
        self.existing_folder_dialog.setObjectName("Dialog")
        self.existing_folder_dialog.setFixedSize(346, 334)
        self.existing_folder_dialog.setStyleSheet(
            '''#Dialog{background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));width: fit-content; heigth: fit-content; block-size: fit-content;
            } ''')
        self.existing_folder_dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.existing_folder_dialog.resize(419, 365)
        # Create the main layout
        layout = QVBoxLayout(self.existing_folder_dialog)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # create a table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS Location_Folder
                                                     (id INTEGER PRIMARY KEY, project_name TEXT, folder_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        # check if table Projects exists, and create it if it doesn't
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Projects' ''')
        if c.fetchone()[0] == 0:
            c.execute(
                '''CREATE TABLE Projects (id INTEGER PRIMARY KEY, project_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        # fetch data from the database
        c.execute("SELECT * FROM Projects")
        data = c.fetchall()
        print(data)
        # Debugging line

        # Create a label above the scroll area
        label = QLabel("Choose an existing project")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("#label{\n"
                            "    font: 900 13pt \"Segoe UI Black\";\n"
                            "    alignment: center;\n"
                            "    color: rgba(111, 75, 39, 0.77);\n"
                            "}")
        label.setObjectName("label")
        layout.addWidget(label)

        # Create buttons based on the data
        for item in data:
            project_name = str(item[1])
            project_button = QPushButton(project_name)
            project_button.setMinimumSize(0, 35)
            project_button.setMaximumSize(500, 35)
            project_button.clicked.connect(self.existing_folder_dialog.close)
            project_button.clicked.connect(self.select_folder)
            project_button.setStyleSheet("#button{\n"
                                         "margin: 0px 0px 0px 10px;"
                                         "font-weight:bold;\n"
                                         "color: white;\n"
                                         "background-color: #6F4B27;\n"
                                         "border-top-left-radius: 7px;\n"
                                         "border-top-right-radius: 7px;\n"
                                         "border-bottom-left-radius: 7px;\n"
                                         "border-bottom-right-radius: 7px;\n"
                                         "font-family: Inter;\n"
                                         "font-size: 11px;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         "#button:hover{\n"
                                         "color: rgb(144,115,87);\n"
                                         "border : 3px solid rgb(144,115,87);\n"
                                         "background-color: white;\n"
                                         "}\n"
                                         "")
            project_button.setObjectName("button")
            layout.addWidget(project_button)

        # Create a scroll area for the layout
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumSize(QtCore.QSize(323, 210))
        scroll_area.setMaximumSize(QtCore.QSize(323, 210))
        scroll_area.setObjectName("scroll_area")
        scroll_area.setStyleSheet(
            "#scroll_area {border: none;background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));} "
            "#scroll_area QScrollBar:vertical {background-color: #c3c3c3; width: 15px;margin: 15px 3px 15px 3px;border: 1px transparent #2A2929;border-radius: 4px;} "
            "#scroll_area QScrollBar::handle:vertical {background-color: #8c8c8c;min-height: 5px;border-radius: 4px;}"
            "QScrollBar::sub-line:vertical{margin: 3px 0px 3px 0px;border-image: url(:/images/up_arrow_disabled.png);height: 10px;width: 10px;subcontrol-position: top;subcontrol-origin: margin;}"
            "QScrollBar::add-line:vertical{margin: 3px 0px 3px 0px;border-image: url(:/images/up_arrow_disabled.png);height: 10px;width: 10px;subcontrol-position: top;subcontrol-origin: margin;}"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{background: none;}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background: none;}"
        )

        # Create a widget to contain the layout
        widget = QWidget()
        widget.setStyleSheet('''
            background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));
            width: fit-content;
            height: fit-content;
            block-size: fit-content;
            margin-left: 10px;
        ''')
        widget.setLayout(layout)

        # Set the widget as the content of the scroll area
        scroll_area.setWidget(widget)
        # Create a layout for the buttons at the bottom
        button_layout = QHBoxLayout()
        # Create the existing button and add it to the layout
        Create_new = QPushButton("Create New Project")
        Create_new.setMinimumSize(143, 35)
        Create_new.clicked.connect(self.existing_folder_dialog.close)
        Create_new.clicked.connect(self.creating_new_project)
        Create_new.setMaximumSize(143, 35)
        Create_new.setObjectName("Create_new")
        Create_new.setStyleSheet("#Create_new{\n"
                                 "margin-left: 9px;"
                                 "font-weight:bold;\n"
                                 "color: white;\n"
                                 "background-color: #6F4B27;\n"
                                 "border-top-left-radius: 7px;\n"
                                 "border-top-right-radius: 7px;\n"
                                 "border-bottom-left-radius: 7px;\n"
                                 "border-bottom-right-radius: 7px;\n"
                                 "font-family: Inter;\n"
                                 "font-size: 11px;\n"
                                 "text-align: center;\n"
                                 "}\n"
                                 "#Create_new:hover{\n"
                                 "color: rgb(144,115,87);\n"
                                 "border : 3px solid rgb(144,115,87);\n"
                                 "background-color: white;\n"
                                 "}\n"
                                 "")
        button_layout.addWidget(Create_new)

        # Create the new button and add it to the layout
        back = QPushButton("Back")
        back.setMinimumSize(143, 35)
        back.setMaximumSize(143, 35)
        back.setStyleSheet("#back{\n"
                           "margin-right: 12px;"
                           "font-weight:bold;\n"
                           "color: white;\n"
                           "background-color: #6F4B27;\n"
                           "border-top-left-radius: 7px;\n"
                           "border-top-right-radius: 7px;\n"
                           "border-bottom-left-radius: 7px;\n"
                           "border-bottom-right-radius: 7px;\n"
                           "font-family: Inter;\n"
                           "font-size: 11px;\n"
                           "text-align: center;\n"
                           "}\n"
                           "#back:hover{\n"
                           "color: rgb(144,115,87);\n"
                           "border : 3px solid rgb(144,115,87);\n"
                           "background-color: white;\n"
                           "}\n"
                           "")
        back.setObjectName("back")
        back.clicked.connect(self.existing_folder_dialog.close)
        back.clicked.connect(self.Choose_where_to_save)
        button_layout.addWidget(back)

        # Set the main layout for the dialog to the scroll area
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(button_layout)
        self.existing_folder_dialog.setLayout(main_layout)
        self.existing_folder_dialog.exec()

    def creating_new_project(self):
        # Create dialog box
        NewProjectDialog = QtWidgets.QDialog()
        NewProjectDialog.setObjectName("NewFolderDialog")
        NewProjectDialog.setWindowFlags(Qt.FramelessWindowHint)
        NewProjectDialog.resize(500, 300)
        NewProjectDialog.setMinimumSize(QtCore.QSize(500, 300))
        NewProjectDialog.setMaximumSize(QtCore.QSize(500, 300))
        # set corner radius of dialog box
        # NewProjectDialog.setWindowOpacity(0.6)
        radius = 20
        NewProjectDialog.setStyleSheet("""
                    background:#EFEEEE;
                    border-top-left-radius:{0}px;
                    border-bottom-left-radius:{0}px;
                    border-top-right-radius:{0}px;
                    border-bottom-right-radius:{0}px;
                    """.format(radius))

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(NewProjectDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_1 = QtWidgets.QWidget(NewProjectDialog)
        self.widget_1.setStyleSheet("width: fit-content;\n"
                                    "block-size: fit-content;")
        self.widget_1.setObjectName("widget_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_1)
        self.widget_3.setEnabled(True)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(-1, 17, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ET_newproject = QtWidgets.QTextEdit(self.widget_2)
        self.ET_newproject.setMaximumSize(QtCore.QSize(16777215, 53))
        self.ET_newproject.setStyleSheet("#ET_newproject{\n"
                                         "text-allign:center;\n"
                                         "font-size:20px;\n"
                                         "padding:8px;\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-top-left-radius :12px;\n"
                                         "border-top-right-radius : 12px; \n"
                                         "border-bottom-left-radius : 12px; \n"
                                         "border-bottom-right-radius : 12px;\n"
                                         "}")
        self.ET_newproject.setTabChangesFocus(False)
        self.ET_newproject.setPlaceholderText("          Type name of your new project")
        self.ET_newproject.setAlignment(Qt.AlignCenter)
        self.ET_newproject.setObjectName("ET_newproject")
        self.verticalLayout_3.addWidget(self.ET_newproject)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_1)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(-1, 30, -1, 30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(self.widget)
        self.back_btn.setText("Back")
        self.back_btn.setStyleSheet("#back_btn{\n"
                                    "height:40px;\n"
                                    "font-weight:bold;\n"
                                    "font-size:18px;\n"
                                    "color:white;\n"
                                    "background-color: #6A6E72;\n"
                                    "border-top-left-radius :20px;\n"
                                    "border-top-right-radius : 20px; \n"
                                    "border-bottom-left-radius : 20px; \n"
                                    "border-bottom-right-radius : 20px;\n"
                                    "}\n"
                                    "#back_btn:hover{\n"
                                    "color:#6A6E72;\n"
                                    "border :2px solid #6A6E72;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(NewProjectDialog.close)
        self.horizontalLayout.addWidget(self.back_btn)
        self.save_btn = QtWidgets.QPushButton(self.widget)
        self.save_btn.setText("Save")
        self.save_btn.setStyleSheet("#save_btn{\n"
                                    "height:40px;\n"
                                    "font-weight:bold;\n"
                                    "font-size:18px;\n"
                                    "color:white;\n"
                                    "background-color: rgb(144, 115, 87);\n"
                                    "border-top-left-radius :20px;\n"
                                    "border-top-right-radius : 20px; \n"
                                    "border-bottom-left-radius : 20px; \n"
                                    "border-bottom-right-radius : 20px;\n"
                                    "}\n"
                                    "#save_btn:hover{\n"
                                    "color:rgb(144, 115, 87);\n"
                                    "border :2px solid rgb(144, 115, 87);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(NewProjectDialog.close)
        self.save_btn.clicked.connect(self.add_new_project_in_db)
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget_1)
        NewProjectDialog.exec()

    def add_new_project_in_db(self):
        # Get the text from the QTextEdit widget
        new_projects = self.ET_newproject.toPlainText()

        if len(new_projects) == 0:
            # If new_projects is empty, show an error message
            self.creating_new_project()
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, 'Projects.db')
            # Create a connection to a SQLite database or create it if it doesn't exist
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()

            # Check if the Projects table already exists in the database
            self.c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Projects'")
            if self.c.fetchone()[0] == 0:
                # If the Projects table does not exist, create it
                self.c.execute(
                    '''CREATE TABLE Projects (id INTEGER PRIMARY KEY, project_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
                self.conn.commit()

            # Check if the project name already exists in the database
            self.c.execute("SELECT COUNT(*) FROM Projects WHERE project_name = ?", (new_projects,))
            result = self.c.fetchone()

            if result[0] == 0:
                # If the project name doesn't exist, insert it into the database
                self.c.execute("INSERT INTO Projects (project_name) VALUES (?)", (new_projects,))
                self.conn.commit()
                self.show_dialog_success_save()
                self.Save_to_existing_Project()
            else:
                # If the project name already exists, show a dialog message to inform the user
                self.creating_new_project()

    def select_folder(self):
        self.project_name = self.existing_folder_dialog.sender().text()
        self.select_folder_dialog = QtWidgets.QDialog()
        self.select_folder_dialog.setObjectName("Dialog")
        self.select_folder_dialog.setFixedSize(346, 334)
        self.select_folder_dialog.setStyleSheet(
            '''#Dialog{background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));width: fit-content; heigth: fit-content; block-size: fit-content;
            } ''')
        self.select_folder_dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.select_folder_dialog.resize(419, 365)
        # Create the main layout
        layout = QVBoxLayout(self.select_folder_dialog)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # create a table if it doesn't exist
        c.execute("SELECT * FROM Location_Folder WHERE project_name = ?", (self.project_name,))
        data = c.fetchall()
        print(data)  # Debugging line

        # Create a label above the scroll area
        label = QLabel("Choose folder to save")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("#label{\n"
                            "    font: 900 13pt \"Segoe UI Black\";\n"
                            "    alignment: center;\n"
                            "    color: rgba(111, 75, 39, 0.77);\n"
                            "}")
        label.setObjectName("label")
        layout.addWidget(label)

        # Create buttons based on the data
        for item in data:
            folder_name = str(item[2])
            folder_button = QPushButton(folder_name)
            folder_button.setMinimumSize(0, 35)
            folder_button.setMaximumSize(500, 35)
            folder_button.clicked.connect(self.select_folder_dialog.close)
            folder_button.clicked.connect(self.save_result_image_to_db)
            folder_button.setStyleSheet("#button{\n"
                                        "margin: 0px 0px 0px 10px;"
                                        "font-weight:bold;\n"
                                        "color: white;\n"
                                        "background-color: #6F4B27;\n"
                                        "border-top-left-radius: 7px;\n"
                                        "border-top-right-radius: 7px;\n"
                                        "border-bottom-left-radius: 7px;\n"
                                        "border-bottom-right-radius: 7px;\n"
                                        "font-family: Inter;\n"
                                        "font-size: 11px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "#button:hover{\n"
                                        "color: rgb(144,115,87);\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}\n"
                                        "")
            folder_button.setObjectName("button")
            layout.addWidget(folder_button)

        # Create a scroll area for the layout
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumSize(QtCore.QSize(323, 210))
        scroll_area.setMaximumSize(QtCore.QSize(323, 210))
        scroll_area.setObjectName("scroll_area")
        scroll_area.setStyleSheet(
            "#scroll_area {border: none;background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));} "
            "#scroll_area QScrollBar:vertical {background-color: #c3c3c3; width: 15px;margin: 15px 3px 15px 3px;border: 1px transparent #2A2929;border-radius: 4px;} "
            "#scroll_area QScrollBar::handle:vertical {background-color: #8c8c8c;min-height: 5px;border-radius: 4px;}"
            "QScrollBar::sub-line:vertical{margin: 3px 0px 3px 0px;border-image: url(:/images/up_arrow_disabled.png);height: 10px;width: 10px;subcontrol-position: top;subcontrol-origin: margin;}"
            "QScrollBar::add-line:vertical{margin: 3px 0px 3px 0px;border-image: url(:/images/up_arrow_disabled.png);height: 10px;width: 10px;subcontrol-position: top;subcontrol-origin: margin;}"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{background: none;}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background: none;}"
        )

        # Create a widget to contain the layout
        widget = QWidget()
        widget.setStyleSheet('''
            background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));
            width: fit-content;
            height: fit-content;
            block-size: fit-content;
            margin-left: 10px;
        ''')
        widget.setLayout(layout)

        # Set the widget as the content of the scroll area
        scroll_area.setWidget(widget)
        # Create a layout for the buttons at the bottom
        button_layout = QHBoxLayout()
        # Create the existing button and add it to the layout
        Create_new_folder = QPushButton("Create New Folder")
        Create_new_folder.setMinimumSize(143, 35)
        Create_new_folder.clicked.connect(self.select_folder_dialog.close)
        Create_new_folder.clicked.connect(self.creating_new_folder)
        Create_new_folder.setMaximumSize(143, 35)
        Create_new_folder.setObjectName("Create_new")
        Create_new_folder.setStyleSheet("#Create_new{\n"
                                        "margin-left: 9px;"
                                        "font-weight:bold;\n"
                                        "color: white;\n"
                                        "background-color: #6F4B27;\n"
                                        "border-top-left-radius: 7px;\n"
                                        "border-top-right-radius: 7px;\n"
                                        "border-bottom-left-radius: 7px;\n"
                                        "border-bottom-right-radius: 7px;\n"
                                        "font-family: Inter;\n"
                                        "font-size: 11px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "#Create_new:hover{\n"
                                        "color: rgb(144,115,87);\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}\n"
                                        "")
        button_layout.addWidget(Create_new_folder)

        # Create the new button and add it to the layout
        back = QPushButton("Back")
        back.setMinimumSize(143, 35)
        back.setMaximumSize(143, 35)
        back.setStyleSheet("#back{\n"
                           "margin-right: 12px;"
                           "font-weight:bold;\n"
                           "color: white;\n"
                           "background-color: #6F4B27;\n"
                           "border-top-left-radius: 7px;\n"
                           "border-top-right-radius: 7px;\n"
                           "border-bottom-left-radius: 7px;\n"
                           "border-bottom-right-radius: 7px;\n"
                           "font-family: Inter;\n"
                           "font-size: 11px;\n"
                           "text-align: center;\n"
                           "}\n"
                           "#back:hover{\n"
                           "color: rgb(144,115,87);\n"
                           "border : 3px solid rgb(144,115,87);\n"
                           "background-color: white;\n"
                           "}\n"
                           "")
        back.setObjectName("back")
        back.clicked.connect(self.select_folder_dialog.close)
        back.clicked.connect(self.Save_to_existing_Project)
        button_layout.addWidget(back)

        # Set the main layout for the dialog to the scroll area
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(button_layout)
        self.select_folder_dialog.setLayout(main_layout)
        self.select_folder_dialog.exec()

    def save_result_image_to_db(self):
        try:
            with open('Selected_location_crack.txt', 'r') as f:
                selected_loc1 = f.read()
            with open('Selected_type_crack.txt', 'r') as f:
                selected_type1 = f.read()
            with open('Selected_progression_crack.txt', 'r') as f:
                selected_prog1 = f.read()
            with open('Remarks_written.txt', 'r') as f:
                remarks1 = f.read()

            print(selected_loc1, selected_type1, selected_prog1, remarks1)
            file_path_Class = 'Predicted_Class_name.txt'
            if os.path.isfile(file_path_Class):
                with open(file_path_Class, 'r') as f:
                    status = f.read()
                    if status == 'No Detected Crack':
                        selected_loc = 'No Detected Crack'
                        selected_type = 'No Detected Crack'
                        selected_prog = 'No Detected Crack'
                        remarks = 'No Detected Crack'
                    else:
                        selected_loc = selected_loc1
                        selected_type = selected_type1
                        selected_prog = selected_prog1
                        remarks = remarks1
        except Exception as e:
            print(e)
        try:
            # Convert the QImage to a QPixmap
            qimage = QImage(self.image.data, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)

            # Scale the image if it's larger than a certain size
            max_size = 1000
            if qimage.width() > max_size or qimage.height() > max_size:
                qimage = qimage.scaled(max_size, max_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            pixmap = QPixmap.fromImage(qimage)

            # Convert the QPixmap to a bytes object
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")
            image_data = bytes(byte_array)
        except Exception as e:
            print(e)
        self.folder_name = self.select_folder_dialog.sender().text()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'Projects.db')

        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # c.execute("DROP TABLE IF EXISTS Save_Files")
        try:
            c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Save_Files' ''')
            if c.fetchone()[0] == 0:
                c.execute('''CREATE TABLE Save_Files (
                                id INTEGER PRIMARY KEY, 
                                folder_name TEXT, 
                                image BLOB, 
                                width TEXT, 
                                length TEXT, 
                                position TEXT, 
                                No_Crack TEXT, 
                                Crack TEXT, 
                                Status TEXT, 
                                selected_loc TEXT, 
                                selected_type TEXT, 
                                selected_prog TEXT, 
                                remarks TEXT, 
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )''')

            sql = """INSERT INTO Save_Files (
                        folder_name, 
                        image, 
                        width, 
                        length, 
                        position, 
                        No_Crack, 
                        Crack, 
                        Status, 
                        selected_loc, 
                        selected_type, 
                        selected_prog, 
                        remarks, 
                        created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

            # Check for null values
            self.Neg_score = self.Neg_score if self.Neg_score else None
            self.Pos_score = self.Pos_score if self.Pos_score else None
            selected_loc = selected_loc if selected_loc else None
            selected_type = selected_type if selected_type else None
            selected_prog = selected_prog if selected_prog else None
            remarks = remarks if remarks else None

            c.execute(sql, (
                self.folder_name,
                image_data,
                self.width,
                self.length,
                "horizontal",
                self.Neg_score,
                self.Pos_score,
                self.status,
                selected_loc,
                selected_type,
                selected_prog,
                remarks,
                None
            ))

        except Exception as e:
            print(e)
        conn.commit()
        conn.close()
        self.show_dialog_success_save()

    def creating_new_folder(self):
        # Create dialog box
        NewFolderDialog = QtWidgets.QDialog()
        NewFolderDialog.setObjectName("NewFolderDialog")
        NewFolderDialog.setWindowFlags(Qt.FramelessWindowHint)
        NewFolderDialog.resize(500, 300)
        NewFolderDialog.setMinimumSize(QtCore.QSize(500, 300))
        NewFolderDialog.setMaximumSize(QtCore.QSize(500, 300))
        # NewFolderDialog.setWindowOpacity(0.6)
        radius = 20
        NewFolderDialog.setStyleSheet("""
                    background:#EFEEEE;
                    border-top-left-radius:{0}px;
                    border-bottom-left-radius:{0}px;
                    border-top-right-radius:{0}px;
                    border-bottom-right-radius:{0}px;
                    """.format(radius))

        horizontalLayout_2 = QtWidgets.QHBoxLayout(NewFolderDialog)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        widget_1 = QtWidgets.QWidget(NewFolderDialog)
        widget_1.setStyleSheet("width: fit-content;\n"
                               "block-size: fit-content;")
        widget_1.setObjectName("widget_1")
        verticalLayout = QtWidgets.QVBoxLayout(widget_1)
        verticalLayout.setObjectName("verticalLayout")
        widget_3 = QtWidgets.QWidget(widget_1)
        widget_3.setEnabled(True)
        widget_3.setMinimumSize(QtCore.QSize(0, 10))
        widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        widget_3.setObjectName("widget_3")
        verticalLayout_2 = QtWidgets.QVBoxLayout(widget_3)
        verticalLayout_2.setObjectName("verticalLayout_2")
        widget_2 = QtWidgets.QWidget(widget_3)
        widget_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        widget_2.setAutoFillBackground(False)
        widget_2.setObjectName("widget_2")
        verticalLayout_3 = QtWidgets.QVBoxLayout(widget_2)
        verticalLayout_3.setContentsMargins(-1, 17, -1, 0)
        verticalLayout_3.setObjectName("verticalLayout_3")
        self.ET_newfolder = QtWidgets.QTextEdit(widget_2)
        self.ET_newfolder.setMaximumSize(QtCore.QSize(16777215, 53))
        self.ET_newfolder.setStyleSheet("#ET_newproject{\n"
                                        "text-allign:center;\n"
                                        "font-size:20px;\n"
                                        "padding:8px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-top-left-radius :12px;\n"
                                        "border-top-right-radius : 12px; \n"
                                        "border-bottom-left-radius : 12px; \n"
                                        "border-bottom-right-radius : 12px;\n"
                                        "}")
        self.ET_newfolder.setTabChangesFocus(False)
        self.ET_newfolder.setPlaceholderText("          Type name of your new folder")
        self.ET_newfolder.setAlignment(Qt.AlignCenter)
        self.ET_newfolder.setObjectName("ET_newproject")
        verticalLayout_3.addWidget(self.ET_newfolder)
        verticalLayout_2.addWidget(widget_2)
        verticalLayout.addWidget(widget_3)
        widget_4 = QtWidgets.QWidget(widget_1)
        widget_4.setObjectName("widget_4")
        verticalLayout_4 = QtWidgets.QVBoxLayout(widget_4)
        verticalLayout_4.setContentsMargins(-1, 30, -1, 30)
        verticalLayout_4.setObjectName("verticalLayout_4")
        widget = QtWidgets.QWidget(widget_4)
        widget.setStyleSheet("")
        widget.setObjectName("widget")
        horizontalLayout = QtWidgets.QHBoxLayout(widget)
        horizontalLayout.setContentsMargins(20, -1, 20, -1)
        horizontalLayout.setSpacing(30)
        horizontalLayout.setObjectName("horizontalLayout")
        back_btn = QtWidgets.QPushButton(widget)
        back_btn.setText("Back")
        back_btn.setStyleSheet("#back_btn{\n"
                               "height:40px;\n"
                               "font-weight:bold;\n"
                               "font-size:18px;\n"
                               "color:white;\n"
                               "background-color: #6A6E72;\n"
                               "border-top-left-radius :20px;\n"
                               "border-top-right-radius : 20px; \n"
                               "border-bottom-left-radius : 20px; \n"
                               "border-bottom-right-radius : 20px;\n"
                               "}\n"
                               "#back_btn:hover{\n"
                               "color:#6A6E72;\n"
                               "border :2px solid #6A6E72;\n"
                               "background-color: rgb(255, 255, 255);\n"
                               "}")
        back_btn.setObjectName("back_btn")
        back_btn.clicked.connect(NewFolderDialog.close)
        horizontalLayout.addWidget(back_btn)
        save_btn = QtWidgets.QPushButton(widget)
        save_btn.setText("Save")
        save_btn.setStyleSheet("#save_btn{\n"
                               "height:40px;\n"
                               "font-weight:bold;\n"
                               "font-size:18px;\n"
                               "color:white;\n"
                               "background-color: rgb(144, 115, 87);\n"
                               "border-top-left-radius :20px;\n"
                               "border-top-right-radius : 20px; \n"
                               "border-bottom-left-radius : 20px; \n"
                               "border-bottom-right-radius : 20px;\n"
                               "}\n"
                               "#save_btn:hover{\n"
                               "color:rgb(144, 115, 87);\n"
                               "border :2px solid rgb(144, 115, 87);\n"
                               "background-color: rgb(255, 255, 255);\n"
                               "}")
        save_btn.setObjectName("save_btn")
        save_btn.clicked.connect(NewFolderDialog.close)
        save_btn.clicked.connect(self.add_new_folder_in_db)
        horizontalLayout.addWidget(save_btn)
        verticalLayout_4.addWidget(widget)
        verticalLayout.addWidget(widget_4)
        horizontalLayout_2.addWidget(widget_1)
        NewFolderDialog.exec()

    def add_new_folder_in_db(self):
        # Get the text from the QTextEdit widget
        new_folder = self.ET_newfolder.toPlainText()

        if len(new_folder) == 0:
            # If new_projects is empty, show an error message
            self.creating_new_folder()
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, 'Projects.db')
            # Create a connection to a SQLite database or create it if it doesn't exist
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()

            # Check if the Projects table already exists in the database
            self.c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Projects'")
            if self.c.fetchone()[0] == 0:
                # If the Projects table does not exist, create it
                self.c.execute(
                    '''CREATE TABLE Location_Folder (id INTEGER PRIMARY KEY, project_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
                self.conn.commit()

            # Check if the project name already exists in the database
            self.c.execute("SELECT COUNT(*) FROM Location_Folder WHERE folder_name = ?", (new_folder,))
            result = self.c.fetchone()

            if result[0] == 0:
                # If the project name doesn't exist, insert it into the database
                self.c.execute("INSERT INTO Location_Folder (project_name,folder_name) VALUES (?,?)",
                               (self.project_name, new_folder,))
                self.conn.commit()
                self.show_dialog_success_save()
                self.select_folder()
            else:
                # If the project name already exists, show a dialog message to inform the user
                self.creating_new_folder()

    def show_dialog_success_save(self):
        # Create dialog box
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        timer = QTimer()
        timer.timeout.connect(Dialog.close)
        timer.start(1000)
        # Dialog.setWindowOpacity(0.6)
        radius = 20
        Dialog.setStyleSheet("""
                            background:#EFEEEE;
                            border-top-left-radius:{0}px;
                            border-bottom-left-radius:{0}px;
                            border-top-right-radius:{0}px;
                            border-bottom-right-radius:{0}px;
                            """.format(radius))

        verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        verticalLayout_2.setObjectName("verticalLayout_2")
        widget = QtWidgets.QWidget(Dialog)
        widget.setObjectName("widget")
        horizontalLayout = QtWidgets.QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")
        widget_2 = QtWidgets.QWidget(widget)
        widget_2.setObjectName("widget_2")
        verticalLayout = QtWidgets.QVBoxLayout(widget_2)
        verticalLayout.setObjectName("verticalLayout")
        widget_5 = QtWidgets.QWidget(widget_2)
        widget_5.setObjectName("widget_5")
        verticalLayout_4 = QtWidgets.QVBoxLayout(widget_5)
        verticalLayout_4.setContentsMargins(-1, 20, -1, 0)
        verticalLayout_4.setObjectName("verticalLayout_4")
        label = QtWidgets.QLabel(widget_5)
        label.setText("Successfully Saved!")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        label.setFont(font)
        label.setStyleSheet(
            "QLabel { font: 900 \"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 22pt;}")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setWordWrap(True)
        label.setObjectName("label")
        verticalLayout_4.addWidget(label)
        verticalLayout.addWidget(widget_5)
        widget_3 = QtWidgets.QWidget(widget_2)
        widget_3.setObjectName("widget_3")
        verticalLayout_3 = QtWidgets.QVBoxLayout(widget_3)
        verticalLayout_3.setContentsMargins(-1, 0, -1, 20)
        verticalLayout_3.setObjectName("verticalLayout_3")
        widget_4 = QtWidgets.QWidget(widget_3)
        widget_4.setAutoFillBackground(False)
        widget_4.setStyleSheet("#widget_4{\n"
                               "background-image: url(images/ok3.png);\n"
                               "background-repeat: no-repeat; \n"
                               "background-position: center;}")
        widget_4.setObjectName("widget_4")
        verticalLayout_3.addWidget(widget_4)
        verticalLayout.addWidget(widget_3)
        horizontalLayout.addWidget(widget_2)
        verticalLayout_2.addWidget(widget)
        Dialog.exec()

    def update_image(self, image):
        # Get the size of the label
        label_size = self.result_Img.size()

        # Convert the image to a QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.result_Img.setPixmap(pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))


