import os
import sqlite3
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QIODevice, QBuffer, QByteArray
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QPushButton, QLabel


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        Dialog.setMaximumSize(QtCore.QSize(700, 600))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setStyleSheet("#Dialog{background:rgb(255, 255, 255)}")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_16 = QtWidgets.QWidget(Dialog)
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
        ExitIcon.addPixmap(QtGui.QPixmap("../images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(ExitIcon)
        self.exit.setIconSize(QtCore.QSize(30, 30))

        self.exit.setObjectName("exit")
        self.verticalLayout_5.addWidget(self.exit)
        self.verticalLayout_6.addWidget(self.widget_16)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WithLogo = QtWidgets.QWidget(self.widget)
        self.WithLogo.setMinimumSize(QtCore.QSize(564, 80))
        self.WithLogo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.WithLogo.setStyleSheet("#WithLogo{border-image: url(images/Crackterize.png) 175 0 175 0 stretch;}")
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
        self.result_Img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.result_Img.setStyleSheet("#result_Img{\n"
                                      "border-image: url(:/images/img.png) 10 10 10 10 stretch;\n"
                                      "border-radius: 20px;\n"
                                      "opacity: 100;\n"
                                      "border: none;\n"
                                      "}")
        self.result_Img.setObjectName("result_Img")
        self.image = cv2.imread('temp_image.jpg')
        self.update_image(self.image)
        self.horizontalLayout_9.addWidget(self.result_Img)
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
                                             "    \n"
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
        file_path_length = '../Predicted_height.txt'
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
        file_path_Width = '../Predicted_width.txt'
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

        file_path_Neg = '../Negative_score.txt'
        file_path_Pos = '../Positive_score.txt'
        file_path_Class = '../Predicted_Class_name.txt'
        if os.path.isfile(file_path_Neg and file_path_Pos and file_path_Class):
            with open(file_path_Neg, 'r') as f:
                self.Neg_score = f.read()
            self.LabelNeg.setText("Negative Crack Probability is " + self.Neg_score)
            with open(file_path_Pos, 'r') as f:
                self.Pos_score = f.read()
            self.LabelPos.setText("Positive Crack Probability is " + self.Pos_score)
            with open('../Predicted_Class_name.txt', 'r') as f:
                self.name = f.read()

            self.concretecracked.setText("The image is classified as " + self.name + ".")
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
                                      "background: #6F4B27;\n"
                                      "font-weight:bold;\n"
                                      "color: white;\n"
                                      "border-radius: 7px;\n"
                                      "font-family: Inter;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "#adddetails:hover{\n"
                                      "color: #6F4B27;\n"
                                      "border : 3px solid rgb(144,115,87);\n"
                                      "background-color: white;\n"
                                      "}\n"
                                      "")
        self.adddetails.setObjectName("adddetails")
        self.horizontalLayout.addWidget(self.adddetails)
        self.print1 = QtWidgets.QPushButton(self.widget_17)
        self.print1.setMinimumSize(QtCore.QSize(0, 35))
        self.print1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.print1.setStyleSheet("#print1{\n"
                                  "background: #2E74A9;\n"
                                  "font-weight:bold;\n"
                                  "color: white;\n"
                                  "border-radius: 7px;\n"
                                  "font-family: Inter;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#print1::hover{\n"
                                  "color: #2E74A9;\n"
                                  "border : 3px solid  #2E74A9;\n"
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
        self.widthlbl.setText(_translate("Dialog", "50.91 mm"))
        self.widgetPosition.setText(_translate("Dialog", "Position:"))
        self.position_lbl.setText(_translate("Dialog", "Horizontal"))
        self.adddetails.setText(_translate("Dialog", "Add Details"))
        self.print1.setText(_translate("Dialog", "Print"))
        self.savebtn.setText(_translate("Dialog", "Save"))

    def Choose_where_to_save(self):
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 365)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 20, 421, 311))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(100, 50, 211, 71))
        self.widget_2.setObjectName("widget_2")
        self.existingproject = QtWidgets.QPushButton("Save Existing Project", self.widget_2)
        self.existingproject.setGeometry(QtCore.QRect(0, 20, 211, 41))
        self.existingproject.clicked.connect(self.Save_to_existing_folder)
        self.existingproject.setStyleSheet("#existingproject{\n"
                                           "font-weight:bold;\n"
                                           "color: white;\n"
                                           "background-color: #6F4B27;\n"
                                           "border-top-left-radius: 20px;\n"
                                           "border-top-right-radius: 20px;\n"
                                           "border-bottom-left-radius: 20px;\n"
                                           "border-bottom-right-radius: 20px;\n"
                                           "font-family: Inter;\n"
                                           "font-size: 12px;\n"
                                           "text-align: center;\n"
                                           "}\n"
                                           "#existingproject:hover{\n"
                                           "color: rgb(144,115,87);\n"
                                           "border : 3px solid rgb(144,115,87);\n"
                                           "background-color: white;\n"
                                           "}\n"
                                           "")
        self.existingproject.setObjectName("existingproject")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(100, 120, 211, 61))
        self.widget_3.setObjectName("widget_3")
        self.createnew = QtWidgets.QPushButton("Create New", self.widget_3)
        self.createnew.setGeometry(QtCore.QRect(0, 10, 211, 41))
        self.createnew.setStyleSheet("#createnew{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #2E74A9;\n"
                                     "border-top-left-radius: 20px;\n"
                                     "border-top-right-radius: 20px;\n"
                                     "border-bottom-left-radius: 20px;\n"
                                     "border-bottom-right-radius: 20px;\n"
                                     "font-family: Inter;\n"
                                     "font-size: 12px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#createnew:hover{\n"
                                     "color: #2E74A9;\n"
                                     "border : 3px solid  #2E74A9;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.createnew.setObjectName("createnew")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(100, 180, 211, 71))
        self.widget_4.setObjectName("widget_4")
        self.back = QtWidgets.QPushButton("Back", self.widget_4)
        self.back.setGeometry(QtCore.QRect(0, 10, 211, 41))
        self.back.clicked.connect(Dialog.close)
        self.back.setStyleSheet("#back{\n"
                                "font-weight:bold;\n"
                                "color: white;\n"
                                "background-color: #6A6E72;\n"
                                "border-top-left-radius: 20px;\n"
                                "border-top-right-radius: 20px;\n"
                                "border-bottom-left-radius: 20px;\n"
                                "border-bottom-right-radius: 20px;\n"
                                "font-family: Inter;\n"
                                "font-size: 12px;\n"
                                "text-align: center;\n"
                                "}\n"
                                "#back:hover{\n"
                                "color: #6A6E72;\n"
                                "border : 3px solid#6A6E72;\n"
                                "background-color: white;\n"
                                "}\n"
                                "")
        self.back.setObjectName("back")
        Dialog.exec()

    def Save_to_existing_folder(self):
        self.existing_folder_dialog = QtWidgets.QDialog()
        self.existing_folder_dialog.setObjectName("Dialog")
        self.existing_folder_dialog.resize(419, 365)
        # Create the main layout
        layout = QVBoxLayout(self.existing_folder_dialog)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, '../Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # create a table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS Location_Folder
                                                     (id INTEGER PRIMARY KEY, project_name TEXT, folder_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        # fetch data from the database
        c.execute("SELECT * FROM Projects")
        data = c.fetchall()
        print(data)  # Debugging line

        # Create a label above the scroll area
        label = QLabel("This is a label above the scroll area")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16pt; font-weight: bold;")
        layout.addWidget(label)

        # Create buttons based on the data
        for item in data:
            project_name = str(item[1])
            button = QPushButton(project_name)
            button.setMinimumSize(0, 70)
            button.setMaximumSize(500, 70)
            button.clicked.connect(self.select_folder)
            button.clicked.connect(self.existing_folder_dialog.close)
            layout.addWidget(button)

        # Create a button below the scroll area
        button = QPushButton("This is a button below the scroll area")
        button.setMinimumSize(0, 70)
        button.setMaximumSize(500, 70)
        layout.addWidget(button)

        # Create a scroll area for the layout
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedSize(300, 300)

        # Create a widget to contain the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the widget as the content of the scroll area
        scroll_area.setWidget(widget)

        # Set the main layout for the dialog to the scroll area
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(button)
        self.existing_folder_dialog.setLayout(main_layout)
        self.existing_folder_dialog.exec()

    def select_folder(self):
        self.project_name = self.existing_folder_dialog.sender().text()
        self.select_folder_dialog = QtWidgets.QDialog()
        self.select_folder_dialog.setObjectName("Dialog")
        self.select_folder_dialog.resize(419, 365)
        # Create the main layout
        layout = QVBoxLayout(self.select_folder_dialog)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, '../Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # fetch data from the database
        c.execute("SELECT * FROM Location_Folder WHERE project_name = ?", (self.project_name,))
        data = c.fetchall()
        print(data)  # Debugging line

        # Create a label above the scroll area
        label = QLabel("This is a label above the scroll area")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16pt; font-weight: bold;")
        layout.addWidget(label)

        # Create buttons based on the data
        for item in data:
            project_name = str(item[2])
            button = QPushButton(project_name)
            button.setMinimumSize(0, 70)
            button.setMaximumSize(500, 70)
            button.clicked.connect(self.save_result_image_to_db)
            button.clicked.connect(self.select_folder_dialog.close)
            layout.addWidget(button)

        # Create a button below the scroll area
        button = QPushButton("This is a button below the scroll area")
        button.setMinimumSize(0, 70)
        button.setMaximumSize(500, 70)
        layout.addWidget(button)

        # Create a scroll area for the layout
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedSize(300, 300)

        # Create a widget to contain the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the widget as the content of the scroll area
        scroll_area.setWidget(widget)

        # Set the main layout for the dialog to the scroll area
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(button)
        self.select_folder_dialog.setLayout(main_layout)
        self.select_folder_dialog.exec()

    def save_result_image_to_db(self):
        # Convert the QImage to a QPixmap
        qimage = QImage(self.image.data, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)

        # Convert the QPixmap to a bytes object
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG")
        image_data = bytes(byte_array)

        self.folder_name = self.select_folder_dialog.sender().text()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, '../Projects.db')

        # Create a connection to a SQLite database or create it if it doesn't exist
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Check if the Save_Files table exists, and create it if it doesn't
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Save_Files' ''')
        if c.fetchone()[0] == 0:
            c.execute('''CREATE TABLE Save_Files
                                 (id INTEGER PRIMARY KEY, folder_name TEXT, image BLOB, width TEXT, length TEXT, position TEXT, No Crack, Crack, Status, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        # Insert the data into the Save_Files table
        sql = """INSERT INTO Save_Files (folder_name, image, width, length, position)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        c.execute(sql, (self.folder_name, image_data, self.width, self.length, "horizontal"))

        conn.commit()
        conn.close()

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
