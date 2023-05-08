import os
import sqlite3
from datetime import datetime

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QSizeF, QIODevice, QBuffer, QByteArray, QTimer, QFile
from PyQt5.QtGui import QImage, QPixmap, QTextCharFormat, QTextFrameFormat, QTextCursor, QFont, QTextImageFormat, \
    QTextBlockFormat, QTextDocument, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QScrollArea, QLabel, QDialog


class result_new_dialog(object):

    def __init__(self, background_widget, history, projects, mainwindow):
        self.Mainwindow = mainwindow
        self.myProjects = projects
        self.myHistory = history
        self.background_widget = background_widget

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(920, 600)
        Dialog.setMinimumSize(QtCore.QSize(920, 600))
        Dialog.setMaximumSize(QtCore.QSize(920, 600))
        Dialog.setStyleSheet("background-color:white;")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_18 = QtWidgets.QWidget(Dialog)
        self.widget_18.setStyleSheet("background-color:white;")
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.widget_18)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_5.setStyleSheet("#widget_5{\n"
                                    "color: #2E74A9;\n"
                                    "font: bold;\n"
                                    "border: 2px solid white;\n"
                                    "font-size: 20px;\n"
                                    "border-bottom-color: rgb(172, 172, 172);}")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setStyleSheet("#label_3 {\n"
                                   "    font: 900 34pt \"Segoe UI Black\";\n"
                                   "    alignment: center;\n"
                                   "    color: rgba(111, 75, 39, 0.77);\n"
                                   "background-color: transparent;\n"
                                   "}")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_13.addWidget(self.label_3)
        self.widget_16 = QtWidgets.QWidget(self.widget_5)
        self.widget_16.setMaximumSize(QtCore.QSize(30, 40))
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exit_2 = QtWidgets.QPushButton(self.widget_16)
        self.exit_2.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_2.setMaximumSize(QtCore.QSize(30, 30))
        self.exit_2.setStyleSheet("border:none;")
        self.exit_2.clicked.connect(self.closeEvent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_2.setIcon(icon)
        self.exit_2.setAutoDefault(True)
        self.exit_2.setDefault(True)
        self.exit_2.setFlat(True)
        self.exit_2.setObjectName("exit_2")
        self.verticalLayout_2.addWidget(self.exit_2)
        self.widget_17 = QtWidgets.QWidget(self.widget_16)
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_2.addWidget(self.widget_17)
        self.horizontalLayout_13.addWidget(self.widget_16)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.widget = QtWidgets.QWidget(self.widget_18)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_15 = QtWidgets.QWidget(self.widget)
        self.widget_15.setMinimumSize(QtCore.QSize(570, 500))
        self.widget_15.setMaximumSize(QtCore.QSize(570, 16777215))
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_19 = QtWidgets.QWidget(self.widget_15)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.widget_3 = QtWidgets.QWidget(self.widget_19)
        self.widget_3.setMinimumSize(QtCore.QSize(273, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(273, 350))
        self.widget_3.setStyleSheet("#widget_3{\n"
                                    "    \n"
                                    "border: 3px solid white;\n"
                                    "border-color: rgb(172, 172, 172);;\n"
                                    "}")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        image = cv2.imread('temp_image_original.jpg')
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.original_img = QtWidgets.QLabel(self.widget_3)
        self.original_img.setAlignment(QtCore.Qt.AlignCenter)
        self.original_img.setStyleSheet("background-color: transparent;")
        self.original_img.setMinimumSize(QtCore.QSize(250, 300))
        self.original_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.original_img.setObjectName("original_img")
        self.horizontalLayout_3.addWidget(self.original_img)

        self.original_img_show(rgb_image)
        self.horizontalLayout_14.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget_19)
        self.widget_2.setMinimumSize(QtCore.QSize(273, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(350, 350))
        self.widget_2.setStyleSheet("#widget_2{\n"
                                    "    \n"
                                    "border: 3px solid white;\n"
                                    "border-color: rgb(172, 172, 172);;\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        file_path_Class = 'Predicted_Class_name.txt'
        if os.path.isfile(file_path_Class):
            with open(file_path_Class, 'r') as f:
                status = f.read()
                if status == 'No Detected Crack':
                    image = cv2.imread('images/white.jpg')
                else:
                    image = cv2.imread('temp_image_result.jpg')
        self.result_img = QtWidgets.QLabel(self.widget_2)
        self.result_img.setStyleSheet("background-color: transparent;")
        self.result_img.setMinimumSize(QtCore.QSize(250, 300))
        self.result_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.result_img.setAlignment(QtCore.Qt.AlignCenter)
        self.result_img_show(image)
        self.horizontalLayout.addWidget(self.result_img)
        self.horizontalLayout_14.addWidget(self.widget_2)
        self.verticalLayout_6.addWidget(self.widget_19)
        self.widget_20 = QtWidgets.QWidget(self.widget_15)
        self.widget_20.setMinimumSize(QtCore.QSize(0, 130))
        self.widget_20.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 50)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_9 = QtWidgets.QWidget(self.widget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 140))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setContentsMargins(9, 0, 10, 110)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.remarks = QtWidgets.QLabel(self.widget_9)
        self.remarks.setMaximumSize(QtCore.QSize(16777215, 20))
        self.remarks.setStyleSheet("#remarks{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "background-color: transparent;\n"
                                   "}")
        self.remarks.setObjectName("remarks")
        self.verticalLayout_4.addWidget(self.remarks)
        self.remarksbox = QtWidgets.QTextEdit(self.widget_9)
        self.remarksbox.setMinimumSize(QtCore.QSize(0, 100))
        self.remarksbox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.remarksbox.setStyleSheet("#remarksbox {\n"
                                      "        border-radius: 10px;\n"
                                      "        font-size: 18px;\n"
                                      "        font-family: Arial;\n"
                                      "        color: #333;\n"
                                      "        background-color: #fff;\n"
                                      "        border: 2px solid #aaa;\n"
                                      "        padding: 10px;\n"
                                      "    }")
        self.remarksbox.setObjectName("remarksbox")
        self.verticalLayout_4.addWidget(self.remarksbox)
        self.horizontalLayout_11.addWidget(self.widget_9)
        self.verticalLayout_6.addWidget(self.widget_20)
        self.horizontalLayout_2.addWidget(self.widget_15)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(320, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(320, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.widget_61 = QtWidgets.QWidget(self.widget_4)
        self.widget_61.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_61.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_61.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_61)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.horizontalLayout_4.setSpacing(0)
        self.i = QtWidgets.QLabel(self.widget_61)
        self.i.setMinimumSize(QtCore.QSize(30, 30))
        self.i.setMaximumSize(QtCore.QSize(30, 30))
        self.i.setStyleSheet("#i{\n"
                             "background-color: transparent;"
                             "    border-image: url(images/i.png)  ;}")
        self.i.setAlignment(QtCore.Qt.AlignCenter)
        self.i.setWordWrap(False)
        self.i.setObjectName("i")
        self.horizontalLayout_4.addWidget(self.i)
        self.concretecracked = QtWidgets.QLabel(self.widget_61)
        self.concretecracked.setObjectName('concretecracked')
        self.concretecracked.setStyleSheet("#concretecracked{\n"
                                           "background-color: transparent;"
                                           "color: #2E74A9;\n"
                                           "font: bold;\n"
                                           "font-size: 15px;\n"
                                           "}")
        self.concretecracked.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked.setWordWrap(True)
        file_path_Class = 'Predicted_Class_name.txt'
        if os.path.isfile(file_path_Class):
            with open(file_path_Class, 'r') as f:
                status = f.read()
        self.concretecracked.setText("The image is classified as " + status + ".")
        self.horizontalLayout_4.addWidget(self.i)

        self.horizontalLayout_4.addWidget(self.concretecracked)
        self.verticalLayout_3.addWidget(self.widget_61)

        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setMinimumSize(QtCore.QSize(142, 0))
        self.label_4.setMaximumSize(QtCore.QSize(142, 16777215))
        self.label_4.setStyleSheet("#label_4{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 15px;\n"
                                   "font-weight: bold;\n"
                                   "background-color: transparent;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.location = QtWidgets.QLabel(self.widget_6)
        self.location.setStyleSheet("#location{\n"
                                    "    color:  #555555;\n"
                                    "font: bold;\n"
                                    "    font-size: 15px;\n"
                                    "background-color: transparent;}")
        self.location.setScaledContents(True)
        self.location.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.location.setWordWrap(True)
        self.location.setObjectName("location")
        selected_loc = 'Selected_location_crack.txt'
        if os.path.isfile(selected_loc):
            with open(selected_loc, 'r') as f:
                selected_text1 = f.read()
                self.location.setText(selected_text1)
        self.horizontalLayout_4.addWidget(self.location)
        self.verticalLayout_3.addWidget(self.widget_6)

        self.widget_14 = QtWidgets.QWidget(self.widget_4)
        self.widget_14.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_14.setObjectName("widget_14")
        self.widget_14.hide()
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget_14)
        self.label_6.setMinimumSize(QtCore.QSize(142, 0))
        self.label_6.setMaximumSize(QtCore.QSize(142, 16777215))
        self.label_6.setStyleSheet("#label_6{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 15px;\n"
                                   "font-weight: bold;\n"
                                   "background-color: transparent;\n"
                                   "}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.type = QtWidgets.QLabel(self.widget_14)
        self.type.setStyleSheet("#type{\n"
                                "    color:  #555555;\n"
                                "font: bold;\n"
                                "    font-size: 15px;\n"
                                "background-color: transparent;}")
        self.type.setScaledContents(True)
        self.type.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.type.setWordWrap(True)
        selected_type = 'Selected_type_crack.txt'
        if os.path.isfile(selected_type):
            with open(selected_type, 'r') as f:
                selected_text2 = f.read()
                self.type.setText(selected_text2)
        self.type.setObjectName("type")
        self.horizontalLayout_5.addWidget(self.type)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.widget_10 = QtWidgets.QWidget(self.widget_4)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_10.hide()
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.widget_10)
        self.label_8.setStyleSheet("#label_8{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 15px;\n"
                                   "font-weight: bold;\n"
                                   "background-color: transparent;\n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.progression = QtWidgets.QLabel(self.widget_10)
        self.progression.setStyleSheet("#progression{\n"
                                       "    color:  #555555;\n"
                                       "font: bold;\n"
                                       "    font-size: 15px;\n"
                                       "background-color: transparent;}")
        self.progression.setScaledContents(True)
        self.progression.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.progression.setWordWrap(True)
        selected_prog = 'Selected_progression_crack.txt'
        if os.path.isfile(selected_prog):
            with open(selected_prog, 'r') as f:
                selected_text = f.read()
                self.progression.setText(selected_text)
        self.progression.setObjectName("progression")
        self.horizontalLayout_6.addWidget(self.progression)
        self.verticalLayout_3.addWidget(self.widget_10)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setStyleSheet("#label_10{\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "font-size: 15px;\n"
                                    "font-weight: bold;\n"
                                    "background-color: transparent;\n"
                                    "}")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.length = QtWidgets.QLabel(self.widget_7)
        self.length.setStyleSheet("#length{\n"
                                  "    color:  #555555;\n"
                                  "font: bold;\n"
                                  "    font-size: 15px;\n"
                                  "background-color: transparent;}")
        self.length.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.length.setObjectName("length")
        file_path_length = 'Predicted_height.txt'
        if os.path.isfile(file_path_length) and os.path.getsize(file_path_length) > 0:
            with open(file_path_length, 'r') as f:
                self.lengthh = f.read() + " cm"
                self.length.setText(str(self.lengthh))
        else:
            self.lengthh = "0 cm"
            self.length.setText(str(self.lengthh))
        self.horizontalLayout_7.addWidget(self.length)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.widget_11 = QtWidgets.QWidget(self.widget_4)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.widget_11)
        self.label_12.setStyleSheet("#label_12{\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "font-size: 15px;\n"
                                    "font-weight: bold;\n"
                                    "background-color: transparent;\n"
                                    "}")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.widthlbl = QtWidgets.QLabel(self.widget_11)
        self.widthlbl.setStyleSheet("#widthlbl{\n"
                                    "    color:  #555555;\n"
                                    "font: bold;\n"
                                    "    font-size: 15px;\n"
                                    "background-color: transparent;}")
        self.widthlbl.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        file_path_Width = 'Predicted_width.txt'
        if os.path.isfile(file_path_Width) and os.path.getsize(file_path_Width) > 0:
            with open(file_path_Width, 'r') as f:
                self.width = f.read() + " mm"
                self.widthlbl.setText(str(self.width))
        else:
            self.width = "0 mm"
            self.widthlbl.setText(str(self.width))

        self.widthlbl.setObjectName("widthlbl")
        self.horizontalLayout_8.addWidget(self.widthlbl)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.LabelPos = QtWidgets.QLabel(self.widget_8)
        self.LabelPos.setStyleSheet("#LabelPos{\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "font-size: 15px;\n"
                                    "font-weight: bold;\n"
                                    "background-color: transparent;\n"
                                    "}")
        self.LabelPos.setObjectName("LabelPos")
        self.horizontalLayout_9.addWidget(self.LabelPos)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.LabelNeg = QtWidgets.QLabel(self.widget_12)
        self.LabelNeg.setMinimumSize(QtCore.QSize(0, 40))
        self.LabelNeg.setMaximumSize(QtCore.QSize(16777215, 40))
        self.LabelNeg.setStyleSheet("#LabelNeg{\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "font-size: 15px;\n"
                                    "font-weight: bold;\n"
                                    "background-color: transparent;\n"
                                    "}")
        self.LabelNeg.setObjectName("LabelNeg")
        self.horizontalLayout_10.addWidget(self.LabelNeg)
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

        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_21 = QtWidgets.QWidget(self.widget_4)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_15.setContentsMargins(-1, 20, -1, 5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.printbtn = QtWidgets.QPushButton(self.widget_21)
        self.printbtn.setMinimumSize(QtCore.QSize(0, 50))
        self.printbtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.printbtn.setStyleSheet("#printbtn{\n"
                                    "background: #6F4B27;\n"
                                    "font-weight:bold;\n"
                                    "color: white;\n"
                                    "border-radius: 7px;\n"
                                    "font-family: Inter;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "#printbtn:hover{\n"
                                    "color: #6F4B27;\n"
                                    "border : 3px solid rgb(144,115,87);\n"
                                    "background-color: white;\n"
                                    "}\n"
                                    "")
        self.printbtn.setObjectName("printbtn")
        self.printbtn.clicked.connect(self.printpreviewDialog)
        self.horizontalLayout_15.addWidget(self.printbtn)
        self.verticalLayout_3.addWidget(self.widget_21)
        self.widget_13 = QtWidgets.QWidget(self.widget_4)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.savebtn = QtWidgets.QPushButton(self.widget_13)
        self.savebtn.setMinimumSize(QtCore.QSize(0, 50))
        self.savebtn.setMaximumSize(QtCore.QSize(16777215, 50))
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
        self.savebtn.clicked.connect(self.save_new_result)
        self.horizontalLayout_12.addWidget(self.savebtn)
        self.verticalLayout_3.addWidget(self.widget_13)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.verticalLayout_5.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_18)

        # Take a screenshot of the widget
        self.screenshot = self.widget_19.grab()
        # Save the screenshot to a file
        self.screenshot.save('screenshot.png')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeEvent(self, event):
        closeDialog = QDialog()
        self.closeDialog = closeDialog
        closeDialog.setWindowFlags(Qt.FramelessWindowHint)
        closeDialog.setObjectName("Dialog")
        closeDialog.setStyleSheet("#Dialog{background-color: rgb(255,255,255); border: 1px solid rgb(144,115,87);}")
        closeDialog.resize(356, 155)
        closeDialog.setMinimumSize(QtCore.QSize(356, 155))
        closeDialog.setMaximumSize(QtCore.QSize(356, 155))
        self.horizontalLayout = QtWidgets.QHBoxLayout(closeDialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(closeDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.exit = QtWidgets.QPushButton(self.widget_5)
        self.exit.setMinimumSize(QtCore.QSize(20, 20))
        self.exit.setMaximumSize(QtCore.QSize(30, 30))
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(closeDialog.close)
        self.horizontalLayout_5.addWidget(self.exit)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(25, 0, 20, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon = QtWidgets.QLabel(self.widget_2)
        self.icon.setMinimumSize(QtCore.QSize(50, 50))
        self.icon.setMaximumSize(QtCore.QSize(50, 50))
        self.icon.setPixmap(QtGui.QPixmap("images/question.png"))
        self.icon.setScaledContents(True)
        self.icon.setStyleSheet("#icon{\n"
                                "background-color: transparent;"
                                "}")
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setWordWrap(True)
        self.icon.setObjectName("icon")
        self.horizontalLayout_2.addWidget(self.icon)
        self.message = QtWidgets.QLabel(self.widget_2)
        self.message.setStyleSheet("#message{\n"
                                   "background-color: transparent;"
                                   "font-family: \"Inter\";\n"
                                   "font-size: 13pt; \n"
                                   "color: #000000;\n"
                                   "font: bold;\n"
                                   "font-size: 13px;\n"
                                   "}")
        self.message.setScaledContents(True)
        self.message.setWordWrap(True)
        self.message.setText("Are you sure you want to exit?")
        self.message.setObjectName("message")
        self.horizontalLayout_2.addWidget(self.message)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 12, 12, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.Yes = QtWidgets.QPushButton("Yes", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Yes.sizePolicy().hasHeightForWidth())
        self.Yes.setSizePolicy(sizePolicy)
        self.Yes.setMinimumSize(QtCore.QSize(20, 32))
        self.Yes.setMaximumSize(QtCore.QSize(100, 32))
        self.Yes.clicked.connect(self.Delete_and_close)
        self.Yes.setStyleSheet("#Yes{\n"
                               "font-weight:bold;\n"
                               "color:  #6F4B27;\n"
                               "background-color: white;\n"
                               "font-family: Inter;\n"
                               "border-top-left-radius: 7px;\n"
                               "border-top-right-radius:7px;\n"
                               "border-bottom-left-radius: 7px;\n"
                               "border-bottom-right-radius: 7px;\n"
                               "text-align: center;\n"
                               "border : 3px solid #6F4B27;\n"
                               "}\n"
                               "#Yes:hover{\n"
                               "color: white;\n"
                               "background-color: #6F4B27;\n"
                               "}\n"
                               "")
        self.Yes.setObjectName("Yes")
        self.horizontalLayout_3.addWidget(self.Yes)
        self.No = QtWidgets.QPushButton("No", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.No.sizePolicy().hasHeightForWidth())
        self.No.setSizePolicy(sizePolicy)
        self.No.clicked.connect(closeDialog.close)
        self.No.setMinimumSize(QtCore.QSize(20, 32))
        self.No.setMaximumSize(QtCore.QSize(100, 32))
        self.No.setStyleSheet("#No{\n"
                              "font-weight:bold;\n"
                              "color: white;\n"
                              "background-color: #6F4B27;\n"
                              "font-family: Inter;\n"
                              "border-top-left-radius: 7px;\n"
                              "border-top-right-radius:7px;\n"
                              "border-bottom-left-radius: 7px;\n"
                              "border-bottom-right-radius: 7px;\n"
                              "text-align: center;\n"
                              "}\n"
                              "#No:hover{\n"
                              "color: #6F4B27;\n"
                              "border : 3px solid #6F4B27;\n"
                              "background-color: white;\n"
                              "}\n"
                              "")
        self.No.setObjectName("No")
        self.horizontalLayout_3.addWidget(self.No)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        closeDialog.exec()

    def Delete_and_close(self):
        self.delete_usedtext_file()
        try:
            self.Dialog.close()
            self.closeDialog.close()
            self.background_widget.hide()
        except Exception as e:
            print("Delete_and_close1", e)
        try:
            self.background_widget.hide()
        except Exception as e:
            print("Delete_and_close2", e)

    def printpreviewDialog(self):

        self.selected_loc = 'Selected_location_crack.txt'
        if os.path.isfile(self.selected_loc):
            with open(self.selected_loc, 'r') as f:
                self._selected_loc = f.read()
            if not os.path.exists(self.selected_loc):
                self._selected_loc = None
        else:
            self._selected_loc = None

        self.selected_type = 'Selected_type_crack.txt'
        if os.path.isfile(self.selected_type):
            with open(self.selected_type, 'r') as f:
                self._selected_type = f.read()
            if not os.path.exists(self.selected_type):
                self._selected_type = None
        else:
            self._selected_type = None

        self.selected_prog = 'Selected_progression_crack.txt'
        if os.path.isfile(self.selected_prog):
            with open(self.selected_prog, 'r') as f:
                self._selected_prog = f.read()
            if not os.path.exists(self.selected_prog):
                self._selected_prog = None
        else:
            self._selected_prog = None

        remarks_new = self.remarksbox.toPlainText()

        file_path_orient = 'Orientation.txt'
        if os.path.isfile(file_path_orient):
            with open(file_path_orient, 'r') as f:
                self.orient = f.read()

            if not self.orient:  # check if orient is an empty string
                self.orient = None  # set orient to None
        else:
            self.orient = None  # set orient to None if the file does not exist

        printer = QPrinter()
        printer.setPageSize(QPrinter.Letter)
        printer.setOrientation(QPrinter.Portrait)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("preview.pdf")

        doc = QTextDocument()
        doc.setPageSize(QSizeF(792, 612))  # set page size to 11x8.5 inches (in points)
        doc.setDocumentMargin(36)  # set margin to 0.5 inch (36 points)
        cursor = QTextCursor(doc)

        try:
            # Load the image file
            image_path = os.path.abspath("screenshot.png")
            image = QImage(image_path)
            if image.isNull():
                print("Error: Could not load image")
                return

            # Set a fixed size for the image format
            max_size = QSize(700, 450)

            # Insert the image into the document
            pixmap = QPixmap.fromImage(image)

            if not pixmap.isNull():
                # Add the title to the document
                title_format = QTextCharFormat()
                title_format.setFont(QFont("Arial", 20, QFont.Bold))
                cursor.insertText("                              Crackterized Result", title_format)
                cursor.insertBlock()

                # Center the title
                title_cursor = cursor.block().position()
                title_block = cursor.document().findBlock(title_cursor)
                title_block_format = QTextBlockFormat()
                title_block_format.setAlignment(Qt.AlignCenter)
                title_cursor = QTextCursor(title_block)
                title_cursor.setBlockFormat(title_block_format)

                image_format = QTextImageFormat()
                image_format.setWidth(max_size.width())
                image_format.setHeight(max_size.height())
                image_format.setName(image_path)

                # Create a QTextBlockFormat and set its properties
                image_block_format = QTextBlockFormat()
                image_block_format.setAlignment(Qt.AlignLeft)
                cursor.insertBlock(image_block_format)

                # Insert the image into the document and set its format
                cursor.insertImage(image_format)

        except Exception as e:
            print("printpreviewDialog", e)

        # Create a QTextCharFormat object with the desired font properties
        font_format = QTextCharFormat()
        font_format.setFont(QFont("Arial", 13))
        bold_format = QTextCharFormat()
        bold_format.setFont(QFont("Arial", 13))
        bold_format.setFontWeight(QFont.Bold)
        # Add the data to the document
        cursor.insertText("The image characterized as: ", font_format)
        cursor.insertText(f"{self.status}\n\n", bold_format)

        cursor.insertText("Length: ", font_format)
        cursor.insertText(f"{self.lengthh}\n\n", bold_format)

        cursor.insertText("Width: ", font_format)
        cursor.insertText(f"{self.width}\n\n", bold_format)

        # cursor.insertText(f"Width: {self.width}\n\n", font_format)
        # cursor.insertText(f"Orientation: {self.orient}\n", font_format)

        cursor.insertText("Positive Crack Probability: ", font_format)
        cursor.insertText(f"{self.Pos_score}\n\n", bold_format)

        cursor.insertText("Negative Crack Probability: ", font_format)
        cursor.insertText(f"{self.Neg_score}\n\n", bold_format)

        cursor.insertText("Location of Crack: ", font_format)
        cursor.insertText(f"{self._selected_loc}\n\n", bold_format)

        # cursor.insertText("Crack Type: ", font_format)
        # cursor.insertText(f"{self._selected_type}\n\n", bold_format)

        # cursor.insertText("Crack Progression: ", font_format)
        # cursor.insertText(f"{self._selected_prog}\n\n", bold_format)

        cursor.insertText("Remarks: ", font_format)
        cursor.insertText(f"{remarks_new}\n\n", bold_format)

        # cursor.insertText(f"Date Added: {self.date}\n", font_format)

        painter = QPainter()
        if painter.begin(printer):
            doc.setPageSize(QSizeF(printer.pageRect().size()))
            doc.drawContents(painter)
            painter.end()

        preview = QPrintPreviewDialog(printer)
        preview.paintRequested.connect(doc.print_)
        preview.exec_()

    def original_img_show(self, image):
        # Get the size of the label
        label_size = self.original_img.size()

        # Convert the image to a QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.original_img.setPixmap(pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def result_img_show(self, image):
        # Get the size of the label
        label_size = self.result_img.size()

        # Convert the image to a QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.result_img.setPixmap(pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def save_new_result(self):
        selected_folder_vrFile = "selected_folder_vrFile.txt"
        if os.path.exists(selected_folder_vrFile):
            self.save_result_image_to_db()
            self.background_widget.hide()
            print(selected_folder_vrFile, "exists")
        else:
            print(selected_folder_vrFile, "does not exist")
            self.Choose_where_to_save()

    def Choose_where_to_save(self):
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 210)
        Dialog.setMaximumSize(QtCore.QSize(310, 210))
        Dialog.setStyleSheet(
            '''#Dialog{background-color: #f3e9e2; border: 1px solid grey;} ''')
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
        self.createnew = QtWidgets.QPushButton("Create New Project", self.widget_3)
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
            '''#Dialog{background-color: #f3e9e2; border: 1px solid grey;} ''')
        self.existing_folder_dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.existing_folder_dialog.resize(419, 365)
        # Create the main layout
        layout = QVBoxLayout(self.existing_folder_dialog)
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        db_path = os.path.join(dir_path, 'Projects.db')
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
        c.execute("SELECT * FROM Projects ORDER BY created_at DESC")
        data = c.fetchall()

        # Create a label above the scroll area
        label = QLabel("Choose an existing project")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("#label{\n"
                            "background-color: transparent;"
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
            project_button.clicked.connect(lambda checked, button=project_button: self.selected_project(button))
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
            "#scroll_area {border: none;background-color:#f3e9e2;} "
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
            background-color: #f3e9e2; width: fit-content;
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
        # back.clicked.connect(self.Choose_where_to_save)
        button_layout.addWidget(back)

        # Set the main layout for the dialog to the scroll area
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(button_layout)
        self.existing_folder_dialog.setLayout(main_layout)
        self.existing_folder_dialog.exec()

    def selected_project(self, button):
        self.selected_project_name = button.text()
        with open('selected_project_in_result.txt', 'w') as f:
            f.write(self.selected_project_name)

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
        radius = 15
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
                                         "color:rgb(144, 115, 87);"
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
        try:
            # Get the text from the QTextEdit widget
            new_projects = self.ET_newproject.toPlainText()

            if len(new_projects) == 0:
                # If new_projects is empty, show an error message
                self.creating_new_project()
            else:
                dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                db_path = os.path.join(dir_path, 'Projects.db')
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
                self.c.execute("SELECT COUNT(*) FROM Projects WHERE project_name = ? ORDER BY created_at DESC",
                               (new_projects,))
                result = self.c.fetchone()

                if result[0] == 0:
                    # If the project name doesn't exist, insert it into the database
                    self.c.execute("INSERT INTO Projects (project_name) VALUES (?)", (new_projects,))
                    self.conn.commit()
                    message = f"Successfully create the new project {new_projects}."
                    self.myProjects.clear()
                    self.c.execute("SELECT project_name FROM Projects ORDER BY created_at DESC")
                    rows = self.c.fetchall()
                    for row in rows:
                        self.myProjects.addItem(row[0])

                    self.myProjects.setEditText("My Projects")

                    self.show_dialog_success_save(message)
                    self.Save_to_existing_Project()
                else:
                    # If the project name already exists, show a dialog message to inform the user
                    self.creating_new_project()
        except Exception as e:
            print("add_new_project_in_db", e)

    def select_folder(self):
        with open("selected_project_in_result.txt", 'r') as f:
            self.project_name = f.read()
        # self.project_name = self.existing_folder_dialog.sender().text()
        self.select_folder_dialog = QtWidgets.QDialog()
        self.select_folder_dialog.setObjectName("Dialog")
        self.select_folder_dialog.setFixedSize(346, 334)
        self.select_folder_dialog.setStyleSheet(
            '''#Dialog{background-color: #f3e9e2; border: 1px solid grey;} ''')
        self.select_folder_dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.select_folder_dialog.resize(419, 365)
        # Create the main layout
        layout = QVBoxLayout(self.select_folder_dialog)
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        db_path = os.path.join(dir_path, 'Projects.db')
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
                            "background-color: transparent;"
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
            "#scroll_area {border: none;background-color: #f3e9e2;} "
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
            background-color: #f3e9e2;
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

    def add_new_folder_in_db(self):
        # Get the text from the QTextEdit widget
        new_folder = self.ET_newfolder.toPlainText()

        if len(new_folder) == 0:
            # If new_projects is empty, show an error message
            self.creating_new_folder()
        else:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, 'Projects.db')
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
                message = "Successfully create a new folder"
                self.show_dialog_success_save(message)
                self.select_folder()
            else:
                # If the project name already exists, show a dialog message to inform the user
                self.creating_new_folder()

    def save_result_image_to_db(self):
        remarks_new = self.remarksbox.toPlainText()
        try:
            with open("selected_project_in_result.txt", 'r') as f:
                self.project_name = f.read()

            orient = 'Orientation.txt'
            if os.path.isfile(orient):
                with open(orient, 'r') as f:
                    _orient = f.read()
                if not os.path.exists(orient):
                    _orient = None
            else:
                _orient = None

            selected_loc = 'Selected_location_crack.txt'
            if os.path.isfile(selected_loc):
                with open(selected_loc, 'r') as f:
                    _selected_loc = f.read()
                if not os.path.exists(selected_loc):
                    _selected_loc = None
            else:
                _selected_loc = None

            selected_type = 'Selected_type_crack.txt'
            if os.path.isfile(selected_type):
                with open(selected_type, 'r') as f:
                    _selected_type = f.read()
                if not os.path.exists(selected_type):
                    _selected_type = None
            else:
                _selected_type = None

            selected_prog = 'Selected_progression_crack.txt'
            if os.path.isfile(selected_prog):
                with open(selected_prog, 'r') as f:
                    _selected_prog = f.read()
                if not os.path.exists(selected_prog):
                    _selected_prog = None
            else:
                _selected_prog = None

        except Exception as e:
            print(f"Error at getting files {e}")
        try:
            file_path_Class = 'Predicted_Class_name.txt'
            if os.path.isfile(file_path_Class):
                with open(file_path_Class, 'r') as f:
                    status = f.read()
                    if status == 'No Detected Crack':
                        self.image = cv2.imread('images/white.jpg')
                    else:
                        self.image = cv2.imread('temp_image_result.jpg')
            # Convert the QImage to a QPixmap
            qimage = QImage(self.image.data, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(qimage)

            # Convert the QPixmap to a bytes object
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")
            self.image_data_result = bytes(byte_array)

            img_bytes = cv2.imread('temp_image_original.jpg')
            # Convert the QImage to a QPixmap
            qimageOrig = QImage(img_bytes.data, img_bytes.shape[1], img_bytes.shape[0], QImage.Format_RGB888)

            pixmap_orig = QPixmap.fromImage(qimageOrig)

            # Convert the QPixmap to a bytes object
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            pixmap_orig.save(buffer, "PNG")
            self.image_data_original = bytes(byte_array)

            ss_bytes = cv2.imread('screenshot.png')
            # Convert the QImage to a QPixma
            self.image_data_ss_print = bytes(ss_bytes)

        except Exception as e:
            print(f"Error at database {e}")

        selected_folder_vrFile = "selected_folder_vrFile.txt"
        if os.path.exists(selected_folder_vrFile):
            with open(selected_folder_vrFile, "r") as f:
                self.folder_name = f.read()
        else:
            self.folder_name = self.select_folder_dialog.sender().text()

        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        db_path = os.path.join(dir_path, 'Projects.db')

        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # c.execute("DROP TABLE IF EXISTS Save_Files")
        try:
            c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Save_Files' ''')
            if c.fetchone()[0] == 0:
                try:
                    c.execute('''CREATE TABLE Save_Files (
                                    id INTEGER PRIMARY KEY, 
                                    folder_name TEXT, 
                                    image_result BLOB, 
                                    image_original BLOB, 
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
                                    created_at TEXT,
                                    image_data_ss_print BLOB,
                                    project_name TEXT
                                )''')

                except Exception as e:
                    print(f"Error at parameters c.execute {e}")
            try:
                sql = """INSERT INTO Save_Files (
                            folder_name, 
                            image_result,
                            image_original, 
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
                            created_at,
                            image_data_ss_print,
                            project_name
                        
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

                # Check for null values
                self.Neg_score = self.Neg_score if self.Neg_score else None
                self.Pos_score = self.Pos_score if self.Pos_score else None
                timestamp = datetime.now()
                timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')

                c.execute(sql, (
                    self.folder_name,
                    self.image_data_result,
                    self.image_data_original,
                    self.width,
                    self.lengthh,
                    _orient,
                    self.Neg_score,
                    self.Pos_score,
                    self.status,
                    _selected_loc,
                    _selected_type,
                    _selected_prog,
                    remarks_new,
                    timestamp_str,
                    self.image_data_ss_print,
                    self.project_name
                ))

                row_id = c.lastrowid
                self.save_image_to_appdata(row_id)
            except Exception as e:
                print(f"Error at parameters c.execute sql{e}")
            self.myHistory.clear()  # This should work now
            c.execute("SELECT * FROM Save_Files ORDER BY created_at DESC")
            rows = c.fetchall()
            print(rows)
            for row in rows:
                status = str(row[9])
                recent = str(row[14])
                id = str(row[0])
                self.myHistory.addItem(status + " - " + recent, id)

            self.myHistory.setEditText("History")
        except Exception as e:
            print(f"Error at parameters {e}")
        try:
            conn.commit()
            conn.close()
            self.delete_usedtext_file()
            message = "Successfully saved"
            self.show_dialog_success_save(message)
            selected_project_in_result = "selected_project_in_result.txt"
            try:
                os.remove(selected_project_in_result)
            except FileNotFoundError:
                print(f"{selected_project_in_result} already removed or does not exist")
            selected_folder_vrFile = "selected_folder_vrFile.txt"
            if os.path.exists(selected_folder_vrFile):
                print("Result folder open")
            else:
                self.background_widget.hide()

            self.Dialog.close()
        except Exception as e:
            print(f"Error at closing {e}")

    def save_image_to_appdata(self, row_id):
        ss_bytes = cv2.imread('screenshot.png')
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        images_path = os.path.join(dir_path, 'Result Images')

        if not os.path.exists(images_path):
            os.makedirs(images_path)

        # save the image to a file with the id as the name
        file_path = os.path.join(images_path, f"{row_id}.png")
        cv2.imwrite(file_path, ss_bytes)

    def creating_new_folder(self):
        # Create dialog box
        NewFolderDialog = QDialog()
        NewFolderDialog.setObjectName("NewFolderDialog")
        NewFolderDialog.setWindowFlags(Qt.FramelessWindowHint)
        NewFolderDialog.resize(500, 300)
        NewFolderDialog.setMinimumSize(QtCore.QSize(500, 300))
        NewFolderDialog.setMaximumSize(QtCore.QSize(500, 300))
        # NewFolderDialog.setWindowOpacity(0.6)
        NewFolderDialog.setStyleSheet(
            '''#NewFolderDialog{background-color: #f3e9e2; border: 1px solid grey;} ''')

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
                                        "color:rgb(144, 115, 87);"
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

    def show_dialog_success_save(self, message):
        # Create dialog box
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        timer = QTimer()
        timer.timeout.connect(Dialog.close)
        timer.start(2000)
        # Dialog.setWindowOpacity(0.6)
        radius = 15

        verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        verticalLayout_2.setObjectName("verticalLayout_2")
        widget = QtWidgets.QWidget(Dialog)
        widget.setObjectName("widget")
        widget.setStyleSheet("""
                                    background:#EFEEEE;
                                    border-top-left-radius:{0}px;
                                    border-bottom-left-radius:{0}px;
                                    border-top-right-radius:{0}px;
                                    border-bottom-right-radius:{0}px;
                                    """.format(radius))
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
        label.setText(message)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        label.setFont(font)
        label.setStyleSheet(
            "QLabel { font: 900 \"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 22pt;background-color: transparent;}"
        )
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

    def delete_usedtext_file(self):
        file_names = ["Input_Distance.txt", "Negative_score.txt", "Orientation.txt", "Positive_score.txt",
                      "Predicted_Class_name.txt", "Predicted_height.txt", "Predicted_Score.txt", "Predicted_width.txt",
                      "Remarks_written.txt", "Selected_location_crack.txt", "Selected_progression_crack.txt",
                      "Selected_type_crack.txt", "threshold_image.jpg", "image_id.txt", "screenshot.png",
                      "temp_image_original.jpg", "temp_image_result.jpg"]

        try:
            for file_name in file_names:
                file = QFile(file_name)
                if file.isOpen():
                    print(f"{file_name} is open, closing file...")
                    file.close()
                try:
                    os.remove(file_name)
                except FileNotFoundError:
                    print(f"{file_name} already removed or does not exist")


        except OSError as e:
            print(f"Error:{e.strerror}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Results"))
        self.remarks.setText(_translate("Dialog", "Remarks:"))
        self.label_4.setText(_translate("Dialog", "Location of crack:"))
        self.label_6.setText(_translate("Dialog", "Crack Type:"))
        self.label_8.setText(_translate("Dialog", "Crack Progression:"))
        self.label_10.setText(_translate("Dialog", "Length:"))
        self.label_12.setText(_translate("Dialog", "Width:"))
        self.printbtn.setText(_translate("Dialog", "Print"))
        self.savebtn.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = result_new_dialog(None, None, None, None)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
