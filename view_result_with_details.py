import os
import sqlite3
import sys

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QByteArray, QSizeF, QSize
from PyQt5.QtGui import QPixmap, QImage, QTextDocument, QTextCursor, QPainter, QFont, QTextCharFormat, QTextImageFormat, \
    QTextFrameFormat, QTextBlockFormat
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QDialog, QMessageBox


class result_with_details(object):
    def __init__(self, background_widget, history):
        self.history = history
        self.background_widget = background_widget

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        data = self.fetch_save_files_of_projects()
        Dialog.setObjectName("Dialog")
        Dialog.resize(920, 600)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setMinimumSize(QtCore.QSize(920, 600))
        Dialog.setMaximumSize(QtCore.QSize(920, 600))
        Dialog.setStyleSheet("#Dialog{background:rgb(255, 255, 255)}")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_7 = QtWidgets.QWidget(Dialog)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_16 = QtWidgets.QWidget(self.widget_7)
        self.widget_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widget_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_5.setContentsMargins(0, 5, 5, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.exit = QtWidgets.QPushButton(self.widget_16)
        self.exit.setMinimumSize(QtCore.QSize(0, 25))
        self.exit.setMaximumSize(QtCore.QSize(25, 25))
        self.exit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setDefault(False)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.exit_function)
        self.verticalLayout_5.addWidget(self.exit)
        self.verticalLayout_7.addWidget(self.widget_16)
        self.widget = QtWidgets.QWidget(self.widget_7)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget_212 = QtWidgets.QWidget(self.widget)
        self.horizontalLayout_111 = QtWidgets.QHBoxLayout(self.widget_212)
        self.WithLogo = QtWidgets.QWidget(self.widget)
        self.WithLogo.setMinimumSize(QtCore.QSize(500, 80))
        self.WithLogo.setMaximumSize(QtCore.QSize(500, 80))
        self.WithLogo.setStyleSheet("#WithLogo{border-image: url(images/Crackterize.png) 400 0 400 0 stretch;}")
        self.WithLogo.setObjectName("WithLogo")

        self.horizontalLayout_111.addWidget(self.WithLogo)
        self.verticalLayout.addWidget(self.widget_212)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WithLogo)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

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
        self.widget_123 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setMaximumSize(QtCore.QSize(598, 16777215))
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_9 = QtWidgets.QVBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_image = QtWidgets.QLabel(self.widget_12)
        self.label_image.setStyleSheet("background-color: transparent;")
        self.label_image.setObjectName("label")
        self.label_image.setMinimumSize(QtCore.QSize(570, 391))
        self.label_image.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.prepared_by = QtWidgets.QLabel(self.widget_12)

        self.prepared_by.setMinimumSize(QtCore.QSize(0, 0))
        self.prepared_by.setWordWrap(True)
        self.prepared_by.setScaledContents(True)
        self.prepared_by.setMaximumSize(QtCore.QSize(16777215, 20))
        self.prepared_by.setStyleSheet("#label_6{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 15px;\n"
                                   "background-color: transparent;\n"
                                    "margin-left:12px;"
                                   "}")
        self.prepared_by.setObjectName("label_6")

        self.widget_123.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout_9.addWidget(self.label_image)
        self.horizontalLayout_9.addWidget(self.prepared_by)
        self.horizontalLayout_9.addWidget(self.widget_123)
        self.horizontalLayout_2.addWidget(self.widget_12)

        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(280, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(280, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.concretecracked_2 = QtWidgets.QLabel(self.widget_6)
        self.concretecracked_2.setStyleSheet("#concretecracked_2{\n"
                                             "  background-color: transparent;  \n"

                                             "color: #2E74A9;\n"
                                             "font: bold;\n"
                                             "border: 2px solid white;\n"
                                             "font-size: 20px;\n"
                                             "border-bottom-color: rgb(172, 172, 172);;\n"
                                             "}")
        self.concretecracked_2.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked_2.setWordWrap(True)
        self.concretecracked_2.setObjectName("concretecracked_2")
        self.verticalLayout_2.addWidget(self.concretecracked_2)

        self.widget_101 = QtWidgets.QWidget(self.widget_6)
        self.widget_101.setObjectName("widget_10")
        self.widget_101.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_101.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout(self.widget_101)
        self.horizontalLayout_101.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel("Location of Crack:", self.widget_101)
        self.label_21.setStyleSheet("#label_2{\n"
                                   "  background-color: transparent;  \n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_21.setObjectName("label_2")
        self.horizontalLayout_101.addWidget(self.label_21)
        self.loc_lbl = QtWidgets.QLabel(self.widget_101)
        self.loc_lbl.setStyleSheet("#loc_lbl{\n"
                                     "  background-color: transparent;  \n"
                                     "    color:  #555555;\n"
                                     "font: bold;\n"
                                     "    font-size: 15px}")
        self.loc_lbl.setObjectName("loc_lbl")
        self.loc_lbl.setWordWrap(True)
        self.loc_lbl.setScaledContents(True)
        self.horizontalLayout_101.addWidget(self.loc_lbl)
        self.verticalLayout_2.addWidget(self.widget_101)

        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.widget_10)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "  background-color: transparent;  \n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.lengthlbl = QtWidgets.QLabel(self.widget_10)
        self.lengthlbl.setStyleSheet("#lengthlbl{\n"
                                     "  background-color: transparent;  \n"
                                     "    color:  #555555;\n"
                                     "font: bold;\n"
                                     "    font-size: 15px}")
        self.lengthlbl.setObjectName("lengthlbl")
        self.horizontalLayout_10.addWidget(self.lengthlbl)
        self.verticalLayout_2.addWidget(self.widget_10)

        self.widget_13 = QtWidgets.QWidget(self.widget_6)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.widget_13)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "  background-color: transparent;  \n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.widthlbl = QtWidgets.QLabel(self.widget_13)
        self.widthlbl.setStyleSheet("#widthlbl{\n"
                                    "  background-color: transparent;  \n"
                                    "    color:  #555555;\n"
                                    "font: bold;\n"
                                    "    font-size: 15px;\n"
                                    "}")
        self.widthlbl.setObjectName("widthlbl")
        self.horizontalLayout_11.addWidget(self.widthlbl)
        self.verticalLayout_2.addWidget(self.widget_13)
        self.widget_11 = QtWidgets.QWidget(self.widget_6)
        self.widget_11.setObjectName("widget_11")
        self.widget_11.hide()
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widgetPosition = QtWidgets.QLabel(self.widget_11)
        self.widgetPosition.setStyleSheet("#widgetPosition{\n"
                                          "  background-color: transparent;  \n"
                                          "color: rgba(111, 75, 39, 0.77);\n"
                                          "font-size: 13px;\n"
                                          "font-weight: bold;\n"
                                          "}")
        self.widgetPosition.setObjectName("widgetPosition")
        self.horizontalLayout_13.addWidget(self.widgetPosition)
        self.position_lbl = QtWidgets.QLabel(self.widget_11)
        self.position_lbl.setStyleSheet("#position_lbl{\n"
                                        "  background-color: transparent;  \n"
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
        self.widgetPos_2 = QtWidgets.QLabel(self.widget_15)
        self.widgetPos_2.setMinimumSize(QtCore.QSize(180, 0))
        self.widgetPos_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetPos_2.setStyleSheet("#widgetPos_2{\n"

                                       "  background-color: transparent;  \n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "font-size: 13px;\n"
                                       "font-weight: bold;\n"
                                       "}")
        self.widgetPos_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.widgetPos_2.setWordWrap(True)
        self.widgetPos_2.setObjectName("widgetPos_2")
        self.verticalLayout_3.addWidget(self.widgetPos_2)
        self.verticalLayout_2.addWidget(self.widget_15)

        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widgetNeg = QtWidgets.QLabel(self.widget_5)
        self.widgetNeg.setMinimumSize(QtCore.QSize(180, 0))
        self.widgetNeg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetNeg.setStyleSheet("#widgetNeg{\n"

                                     "  background-color: transparent;  \n"
                                     "color: rgba(111, 75, 39, 0.77);\n"
                                     "font-size: 13px;\n"
                                     "font-weight: bold;\n"
                                     "}")
        self.widgetNeg.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.widgetNeg.setWordWrap(True)
        self.widgetNeg.setObjectName("widgetNeg")
        self.verticalLayout_4.addWidget(self.widgetNeg)
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

                             "  background-color: transparent;  \n"
                             "    border-image: url(images/i.png)  ;}")
        self.i.setText("")
        self.i.setAlignment(QtCore.Qt.AlignCenter)
        self.i.setWordWrap(False)
        self.i.setObjectName("i")
        self.horizontalLayout_12.addWidget(self.i)
        self.concretecracked = QtWidgets.QLabel(self.widget_14)
        self.concretecracked.setStyleSheet("#concretecracked{\n"
                                           "  background-color: transparent;  \n"
                                           "color: #2E74A9;\n"
                                           "font: bold;\n"
                                           "font-size: 15px;\n"
                                           "}")
        self.concretecracked.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked.setWordWrap(True)
        self.concretecracked.setObjectName("concretecracked")
        self.horizontalLayout_12.addWidget(self.concretecracked)
        self.verticalLayout_2.addWidget(self.widget_14)
        self.widget_17 = QtWidgets.QWidget(self.widget_6)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.del_btn = QtWidgets.QPushButton(self.widget_17)
        self.del_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.del_btn.setMaximumSize(QtCore.QSize(119, 35))
        self.del_btn.setStyleSheet("#del_btn{\n"
                                   "color: #2E74A9;\n"
                                   "border : 3px solid   #6F4B27;\n"
                                   "background-color: :#E3E9ED;\n"
                                   "border-radius: 7px;\n"
                                   "}\n"
                                   "\n"
                                   "#del_btn::hover{\n"
                                   "background: #E3E9ED;\n"
                                   "font-family: Inter;\n"
                                   "}\n"
                                   "")
        self.del_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_btn.setIcon(icon1)
        self.del_btn.setObjectName("del_btn")
        self.del_btn.clicked.connect(self.delete_result)
        self.horizontalLayout.addWidget(self.del_btn)
        self.print1 = QtWidgets.QPushButton(self.widget_17)
        self.print1.setMinimumSize(QtCore.QSize(0, 35))
        self.print1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.print1.setStyleSheet("\n"
                                  "#print1{\n"
                                  "color: #2E74A9;\n"
                                  "border : 3px solid   #2E74A9;\n"
                                  "background-color: :#2E74A9;\n"
                                  "border-radius: 7px;\n"
                                  "}\n"
                                  "\n"
                                  "#print1::hover{\n"
                                  "background: #E3E9ED;\n"
                                  "font-family: Inter;\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.print1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print1.setIcon(icon2)
        self.print1.setIconSize(QtCore.QSize(16, 16))
        self.print1.setObjectName("print1")
        self.horizontalLayout.addWidget(self.print1)
        self.print1.clicked.connect(self.printpreviewDialog)
        self.verticalLayout_2.addWidget(self.widget_17)
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.view_details = QtWidgets.QPushButton(self.widget_2)
        self.view_details.setMinimumSize(QtCore.QSize(0, 35))
        self.view_details.setMaximumSize(QtCore.QSize(16777215, 35))
        self.view_details.clicked.connect(self.view_details_function)
        self.view_details.setStyleSheet("#view_details{\n"
                                        "background: #6F4B27;\n"
                                        "font-weight:bold;\n"
                                        "color: white;\n"
                                        "border-radius: 7px;\n"
                                        "font-family: Inter;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "#view_details:hover{\n"
                                        "color: #6F4B27;\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}\n"
                                        "")
        self.view_details.setObjectName("view_details")
        self.horizontalLayout_5.addWidget(self.view_details)
        self.update = QtWidgets.QPushButton(self.widget_2)
        self.update.setMinimumSize(QtCore.QSize(0, 35))
        self.update.setMaximumSize(QtCore.QSize(16777215, 35))
        self.update.setStyleSheet("#update{\n"
                                  "background: #2E74A9;\n"
                                  "font-weight:bold;\n"
                                  "color: white;\n"
                                  "border-radius: 7px;\n"
                                  "font-family: Inter;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#update::hover{\n"
                                  "color: #2E74A9;\n"
                                  "border : 3px solid  #2E74A9;\n"
                                  "background-color: white;\n"
                                  "}\n"
                                  "")
        self.update.setObjectName("update")
        self.update.clicked.connect(self.update_result)
        self.horizontalLayout_5.addWidget(self.update)
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
        self.verticalLayout_7.addWidget(self.widget)
        self.verticalLayout_6.addWidget(self.widget_7)

        if data:
            try:
                self.id = data[0][0]
                self.width = data[0][4]
                self.length = data[0][5]
                self.position = data[0][6]
                self.no_crack = data[0][7]
                self.crack = data[0][8]
                self.status = data[0][9]

                self.loc = data[0][10]
                self.type = data[0][11]
                self.prog = data[0][12]
                self.remarks_db = data[0][13]
                self.date = data[0][14]
                self.image = data[0][2]
                self.image_orig = data[0][3]

                dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
                images_path = os.path.join(dir_path, 'Result Images')

                if not os.path.exists(images_path):
                    os.makedirs(images_path)

                file_names = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
                # Check if any matching files were found
                for file_name in file_names:
                    if os.path.splitext(file_name)[0] == str(self.id):
                        # Read the first matching file
                        self.image_path = os.path.join(images_path, file_name)
                        self.image_print = cv2.imread(self.image_path)
                        self.image_print = cv2.cvtColor(self.image_print, cv2.COLOR_BGR2RGB)
                        print(file_name)
                        print(self.id)

                        # Show the image in a label
                        if self.image_print is not None:
                            self.update_image(self.image_print)
                        else:
                            print("Failed to read image:", self.image_path)
                    else:
                        print("No matching image found for id:", self.id)

                self.widthlbl.setText(self.width)
                self.position_lbl.setText(self.position)
                self.lengthlbl.setText(self.length)
                self.concretecracked.setText("The image classified " + self.status + ".")
                self.widgetPos_2.setText("Positive Crack Probability is " + self.crack + ".")
                self.widgetNeg.setText("Negative Crack Probability is " + self.no_crack + ".")
                self.loc_lbl.setText(self.loc)
                self.prepared_by.setText("<b>Prepared By:</b> "+self.position)
            except Exception as e:
                print(e)
        else:
            print("No data found.")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_function(self):
        self.Dialog.close()
        new_remark = 'New_Remark.txt'
        if os.path.isfile(new_remark):
            os.remove(new_remark)
        selected_folder_vrFile = "selected_folder_vrFile.txt"
        if os.path.exists(selected_folder_vrFile):
            print("Result folder open")
        else:
            self.background_widget.hide()

    def printpreviewDialog(self):
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
            image = QImage(self.image_path)
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
                image_format.setName(self.image_path)

                # Create a QTextBlockFormat and set its properties
                image_block_format = QTextBlockFormat()
                image_block_format.setAlignment(Qt.AlignLeft)
                cursor.insertBlock(image_block_format)

                # Insert the image into the document and set its format
                cursor.insertImage(image_format)
        except Exception as e:
            print(e)

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
        cursor.insertText(f"{self.length}\n\n", bold_format)

        cursor.insertText("Width: ", font_format)
        cursor.insertText(f"{self.width}\n\n", bold_format)

        # cursor.insertText(f"Width: {self.width}\n\n", font_format)
        # cursor.insertText(f"Orientation: {self.orient}\n", font_format)

        cursor.insertText("Positive Crack Probability: ", font_format)
        cursor.insertText(f"{self.crack}\n\n", bold_format)

        cursor.insertText("Negative Crack Probability: ", font_format)
        cursor.insertText(f"{self.no_crack}\n\n", bold_format)

        cursor.insertText("Location of Crack: ", font_format)
        cursor.insertText(f"{self.loc}\n\n", bold_format)

        cursor.insertText("Date Added: ", font_format)
        cursor.insertText(f"{self.date}\n\n", bold_format)

        cursor.insertText("Remarks: ", font_format)
        cursor.insertText(f"{self.remarks_db}\n\n", bold_format)

        painter = QPainter()
        if painter.begin(printer):
            doc.setPageSize(QSizeF(printer.pageRect().size()))
            doc.drawContents(painter)
            painter.end()

        preview = QPrintPreviewDialog(printer)
        preview.paintRequested.connect(doc.print_)
        preview.exec_()

    def delete_result(self):
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, 'Projects.db')
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            try:
                self.closeEvent()
            except Exception as e:
                print(f"Error deleting record: {e}")
            finally:
                self.conn.close()

        except Exception as e:
            print(e)

    def update_result(self):
        with open('image_id.txt', 'r') as f:
            result_id = f.read()
        new_remark = 'New_Remark.txt'
        if os.path.isfile(new_remark):
            with open(new_remark, 'r') as f:
                self.input_txt = f.read()
        else:

            self.QMessage_Error_dialog()
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        db_path = os.path.join(dir_path, 'Projects.db')
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        try:
            self.c.execute("UPDATE Save_Files SET remarks = ? WHERE id = ?", (self.input_txt, result_id))
            self.conn.commit()
            print("Record updated successfully")
            os.remove(new_remark)
            message = "Remark updated successfully!"
            icon = "images/checked.png"
            self.QMessage_success_dialog(message, icon)
        except Exception as e:
            print(f"Error updating record: {e}")
        finally:
            self.conn.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.concretecracked_2.setText(_translate("Dialog", "Detected:"))
        self.label_2.setText(_translate("Dialog", "Length:"))
        self.label_3.setText(_translate("Dialog", "Width: "))
        self.widgetPosition.setText(_translate("Dialog", "Orientation:"))
        self.view_details.setText(_translate("Dialog", "Remarks"))
        self.update.setText(_translate("Dialog", "Update"))

    def closeEvent(self):
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
        self.message.setText("Are you sure you want to delete this record?")
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
        try:
            with open('image_id.txt', 'r') as f:
                result_id = f.read()
            self.c.execute("DELETE FROM Save_Files WHERE id = ?", (result_id,))

            self.history.clear()  # This should work now
            self.c.execute("SELECT * FROM Save_Files ORDER BY created_at DESC")
            rows = self.c.fetchall()
            for row in rows:
                status = str(row[9])
                recent = str(row[14])
                id = str(row[0])
                self.history.addItem(status + " - " + recent, id)
            self.history.setEditText("History")
            self.conn.commit()
            self.Dialog.close()
            self.closeDialog.close()
            selected_folder_vrFile = "selected_folder_vrFile.txt"
            if os.path.exists(selected_folder_vrFile):
                print("Result folder open")
            else:
                self.background_widget.hide()

        except Exception as e:
            print(e)

    def fetch_save_files_of_projects(self):
        with open('image_id.txt', 'r') as f:
            result_id = f.read()

        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        db_path = os.path.join(dir_path, 'Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        # create a table if it doesn't exist
        self.c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Save_Files' ''')
        if self.c.fetchone()[0] == 0:
            self.c.execute('''CREATE TABLE Save_Files (id INTEGER PRIMARY KEY, folder_name TEXT, 
                                image_result BLOB, image_original BLOB,  width TEXT, 
            length TEXT, position TEXT, No_Crack TEXT, Crack TEXT, Status TEXT, selected_loc TEXT, selected_type 
            TEXT, selected_prog TEXT, remarks TEXT, created_at TEXT)''')
        # fetch data from the database
        self.c.execute("SELECT * FROM Save_Files WHERE id = ?", (result_id,))
        data = self.c.fetchall()
        return data

    def view_details_function(self):
        Function_Dialog = QDialog()
        self.details_dialog = Function_Dialog
        Function_Dialog.setObjectName("Dialog")
        Function_Dialog.resize(372, 398)
        Function_Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Function_Dialog.setStyleSheet("#Dialog{background:rgb(255, 255, 255); border:1px solid grey;}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Function_Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_6 = QtWidgets.QWidget(Function_Dialog)
        self.widget_6.setMinimumSize(QtCore.QSize(280, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.widget_15 = QtWidgets.QWidget(self.widget_6)
        self.widget_15.setObjectName("widget_15")
        self.widget_15.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_15)
        self.widget.setStyleSheet("#widget{\n"
                                  "    \n"
                                  "border: 2px solid white;\n"
                                  "border-bottom-color: rgb(172, 172, 172);;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widgetPos_2 = QtWidgets.QLabel("Remarks", self.widget)
        self.widgetPos_2.setMinimumSize(QtCore.QSize(180, 0))
        self.widgetPos_2.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widgetPos_2.setStyleSheet("#widgetPos_2{\n"
                                       "  background-color: transparent;  \n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "font-size: 20px;\n"
                                       "font-weight: bold;\n"
                                       "}")
        self.widgetPos_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.widgetPos_2.setWordWrap(True)
        self.widgetPos_2.setObjectName("widgetPos_2")
        self.horizontalLayout_2.addWidget(self.widgetPos_2)

        self.edit_remarks = QtWidgets.QPushButton(self.widget)
        self.edit_remarks.setMinimumSize(QtCore.QSize(25, 25))
        self.edit_remarks.setMaximumSize(QtCore.QSize(25, 25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/edit_remarks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_remarks.setIcon(icon)
        self.edit_remarks.setIconSize(QtCore.QSize(20, 25))
        self.edit_remarks.setFlat(True)
        self.edit_remarks.setStyleSheet("#edit_remarks{\n"
                                        "font-size: 10px;"
                                   "font-weight:bold;\n"
                                   "color: #6F4B27;\n"
                                   "font-family: Inter;}"
                                   "#edit_remarks::hover{\n"
                                   "color: #555555;\n"
                                   "}\n"
                                   "")
        self.edit_remarks.setObjectName("edit_remarks")
        self.horizontalLayout_2.addWidget(self.edit_remarks)
        self.verticalLayout_3.addWidget(self.widget)
        self.remarks = QtWidgets.QLineEdit(self.widget_15)
        # Toggle QLineEdit widget between enabled/disabled
        is_enabled = self.remarks.isEnabled()
        self.remarks.setEnabled(not is_enabled)
        self.edit_remarks.clicked.connect(self.edit_remarks_enable)
        self.remarks.setMinimumSize(QtCore.QSize(0, 230))
        self.remarks.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.remarks.setStyleSheet("#remarks{\n"

                                   "  background-color: transparent;  \n"
                                   "    color:  #555555;\n"
                                   "font: bold;\n"
                                   "    font-size: 15px;\n"
                                   "}")
        self.remarks.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.remarks.setObjectName("remarks")
        self.verticalLayout_3.addWidget(self.remarks)
        self.verticalLayout_2.addWidget(self.widget_15)
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.savebtn = QtWidgets.QPushButton("Okay", self.widget_3)
        self.savebtn.setMinimumSize(QtCore.QSize(0, 35))
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
        self.savebtn.clicked.connect(self.edit_remarks_function)
        self.horizontalLayout_5.addWidget(self.savebtn)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_6)
        data = self.fetch_save_files_of_projects()
        if data:
            try:
                loc = data[0][10]
                type = data[0][11]
                prog = data[0][12]
                remarks = data[0][13]
                date = data[0][14]

                new_remark = 'New_Remark.txt'
                if os.path.isfile(new_remark):
                    with open(new_remark, 'r') as f:
                        self.input_txt = f.read()
                        self.remarks.setText(self.input_txt)
                else:
                    self.remarks.setText(remarks)
            except Exception as e:
                print(e)
        else:
            print("No data found.")
        Function_Dialog.exec()

    def edit_remarks_enable(self):
        # Enable the QLineEdit
        self.remarks.setEnabled(True)

    def edit_remarks_function(self):
        try:
            self.input_remark = self.remarks.text()
            with open('New_Remark.txt', 'w') as f:
                f.write(self.input_remark)
        except Exception as e:
            print(e)
        self.details_dialog.close()

    def QMessage_Error_dialog(self):
        Dialog = QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 155)
        Dialog.setMinimumSize(QtCore.QSize(356, 155))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setMaximumSize(QtCore.QSize(356, 155))
        Dialog.setStyleSheet("#Dialog{background-color: rgb(255,255,255);border: 1px solid rgb(144,115,87);}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
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
        self.exit.clicked.connect(Dialog.close)
        self.exit.setObjectName("exit")
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
        self.icon.setPixmap(QtGui.QPixmap("images/failed.png"))
        self.icon.setScaledContents(True)
        self.icon.setStyleSheet(
            "  background-color: transparent; ")
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setWordWrap(True)
        self.icon.setObjectName("icon")
        self.horizontalLayout_2.addWidget(self.icon)
        self.message = QtWidgets.QLabel(self.widget_2)
        self.message.setText("You did not make any changes.")
        self.message.setStyleSheet("#message{\n"
                                   "  background-color: transparent;  \n"
                                   "font-family: \"Inter\";\n"
                                   "font-size: 13pt; \n"
                                   "color: #000000;\n"
                                   "font: bold;\n"
                                   "font-size: 13px;\n"
                                   "}")
        self.message.setScaledContents(True)
        self.message.setWordWrap(True)
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
        self.okBtn = QtWidgets.QPushButton("Okay", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okBtn.sizePolicy().hasHeightForWidth())
        self.okBtn.setSizePolicy(sizePolicy)
        self.okBtn.clicked.connect(Dialog.close)
        self.okBtn.setMinimumSize(QtCore.QSize(20, 32))
        self.okBtn.setMaximumSize(QtCore.QSize(100, 32))
        self.okBtn.setStyleSheet("#okBtn{\n"
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
                                 "#okBtn:hover{\n"
                                 "color: rgb(144,115,87);\n"
                                 "border : 3px solid rgb(144,115,87);\n"
                                 "background-color: white;\n"
                                 "}\n"
                                 "")
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_3.addWidget(self.okBtn)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.exec()

    def QMessage_success_dialog(self, message, icon_image):
        Dialog = QDialog()
        self.QMessageDialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 155)
        Dialog.setMinimumSize(QtCore.QSize(356, 155))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setMaximumSize(QtCore.QSize(356, 155))
        Dialog.setStyleSheet("#Dialog{background-color: rgb(255,255,255);border: 1px solid rgb(144,115,87);}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
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
        self.exit.clicked.connect(Dialog.close)
        self.exit.setObjectName("exit")
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
        self.icon.setPixmap(QtGui.QPixmap(icon_image))
        self.icon.setScaledContents(True)
        self.icon.setStyleSheet(
            "  background-color: transparent; ")
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setWordWrap(True)
        self.icon.setObjectName("icon")
        self.horizontalLayout_2.addWidget(self.icon)
        self.message = QtWidgets.QLabel(self.widget_2)
        self.message.setText(message)
        self.message.setStyleSheet("#message{\n"
                                   "  background-color: transparent;  \n"
                                   "font-family: \"Inter\";\n"
                                   "font-size: 13pt; \n"
                                   "color: #000000;\n"
                                   "font: bold;\n"
                                   "font-size: 13px;\n"
                                   "}")
        self.message.setScaledContents(True)
        self.message.setWordWrap(True)
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
        self.okBtn = QtWidgets.QPushButton("Okay", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okBtn.sizePolicy().hasHeightForWidth())
        self.okBtn.setSizePolicy(sizePolicy)
        self.okBtn.clicked.connect(self.close_event)
        self.okBtn.setMinimumSize(QtCore.QSize(20, 32))
        self.okBtn.setMaximumSize(QtCore.QSize(100, 32))
        self.okBtn.setStyleSheet("#okBtn{\n"
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
                                 "#okBtn:hover{\n"
                                 "color: rgb(144,115,87);\n"
                                 "border : 3px solid rgb(144,115,87);\n"
                                 "background-color: white;\n"
                                 "}\n"
                                 "")
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_3.addWidget(self.okBtn)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.exec()

    def close_event(self):
        self.QMessageDialog.close()
        self.Dialog.close()
        selected_folder_vrFile = "selected_folder_vrFile.txt"
        if os.path.exists(selected_folder_vrFile):
            print("Result folder open")
        else:
            self.background_widget.hide()

    def update_image(self, image):
        # Get the size of the label
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        label_size = self.label_image.size()

        # Convert the image to a QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.label_image.setPixmap(pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = result_with_details(None, None)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())