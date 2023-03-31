import os
import pickle
import sqlite3

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QScrollArea, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 489)
        MainWindow.setMinimumSize(QtCore.QSize(600, 489))
        MainWindow.setMaximumSize(QtCore.QSize(600, 489))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WithLogo = QtWidgets.QWidget(self.widget)
        self.WithLogo.setMinimumSize(QtCore.QSize(564, 80))
        self.WithLogo.setMaximumSize(QtCore.QSize(564, 80))
        self.WithLogo.setStyleSheet("#WithLogo{border-image: url(images/Crackterize.png) 175 0 175 0 stretch;}")
        self.WithLogo.setObjectName("WithLogo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WithLogo)
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

        self.widget_img = QtWidgets.QWidget(self.widget_4)
        self.result_Img = QtWidgets.QLabel(self.widget_img)
        self.result_Img.setFixedSize(200, 251)
        self.result_Img.setStyleSheet("#result_Img{\n"
                                      "opacity: 100;\n"
                                      "border: none;\n"
                                      "}")

        # Get the image data from the command line argument
        # image_str = sys.argv[1]
        self.image = cv2.imread('temp_image.jpg')

        # Convert the QImage object to a QPixmap object
        # qpixmap = QPixmap.fromImage(self.image)
        # Set the QPixmap object as the image in the label widget
        self.update_image(self.image)

        self.result_Img.setObjectName("result_Img")
        self.widget_img.setObjectName("widget_6")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_12 = QtWidgets.QWidget(self.widget_6)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.widget_12)
        self.label.setStyleSheet("font-family: \'Inter\';\n"
                                 "color:#250000;\n"
                                 "font-style: normal;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 23px;\n"
                                 "line-height: 61px;\n"
                                 "text-align: center;\n"
                                 "")
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.widget_12)
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.widget_10)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 22px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.lengthlbl = QtWidgets.QLabel(self.widget_10)
        self.lengthlbl.setStyleSheet("#lengthlbl{\n"
                                     "    color:  #555555;\n"
                                     "font: bold;\n"
                                     "    font-size: 18px}")
        self.lengthlbl.setObjectName("lengthlbl")
        file_path_length = 'Predicted_height.txt'
        if os.path.isfile(file_path_length):
            with open(file_path_length, 'r') as f:
                length = f.read()
            self.lengthlbl.setText(length)
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
                                   "font-size: 22px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.widthlbl = QtWidgets.QLabel(self.widget_13)
        self.widthlbl.setStyleSheet("#widthlbl{\n"
                                    "    color:  #555555;\n"
                                    "font: bold;\n"
                                    "    font-size: 18px;\n"
                                    "}")
        self.widthlbl.setObjectName("widthlbl")
        file_path_Width = 'Predicted_width.txt'
        if os.path.isfile(file_path_Width):
            with open(file_path_Width, 'r') as f:
                width = f.read()
            self.widthlbl.setText(width)
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
                                          "font-size: 22px;\n"
                                          "font-weight: bold;\n"
                                          "}")
        self.widgetPosition.setObjectName("widgetPosition")
        self.horizontalLayout_13.addWidget(self.widgetPosition)
        self.position_lbl = QtWidgets.QLabel(self.widget_11)
        self.position_lbl.setStyleSheet("#position_lbl{\n"
                                        "    color:  #555555;\n"
                                        "font: bold;\n"
                                        "    font-size: 18px;\n"
                                        "}")
        self.position_lbl.setObjectName("position_lbl")
        self.horizontalLayout_13.addWidget(self.position_lbl)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_14 = QtWidgets.QWidget(self.widget_6)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.i = QtWidgets.QWidget(self.widget_14)
        self.i.setMinimumSize(QtCore.QSize(20, 0))
        self.i.setStyleSheet("#i{\n"
                             "    border-image: url(images/i.png)  ;}")
        self.i.setObjectName("i")
        self.horizontalLayout_12.addWidget(self.i)

        with open('Predicted_Score.txt', 'r') as f:
            score = f.read()
        with open('Predicted_Class_name.txt', 'r') as f:
            name = f.read()
        self.concretecracked = QtWidgets.QLabel(self.widget_14)
        self.concretecracked.setStyleSheet("#concretecracked{\n"
                                           "color: #2E74A9;\n"
                                           "font: bold;\n"
                                           "font-size: 20px;\n"
                                           "}")
        self.concretecracked.setObjectName("concretecracked")
        self.concretecracked.setText("Concrete is " + score + " " + name)

        self.horizontalLayout_12.addWidget(self.concretecracked)
        self.verticalLayout_2.addWidget(self.widget_14)
        self.horizontalLayout_2.addWidget(self.widget_img)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.discardbtn = QtWidgets.QPushButton(self.widget_2)
        self.discardbtn.setMinimumSize(QtCore.QSize(114, 35))
        self.discardbtn.setMaximumSize(QtCore.QSize(114, 35))
        self.discardbtn.setStyleSheet("#discardbtn{\n"
                                      "background: #6A6E72;\n"
                                      "font-weight:bold;\n"
                                      "color: white;\n"
                                      "border-radius: 16px;\n"
                                      "font-family: Inter;\n"
                                      "}\n"
                                      "\n"
                                      "#discardbtn:hover{\n"
                                      "color: #6A6E72;\n"
                                      "border : 3px solid#6A6E72;\n"
                                      "background-color: white;\n"
                                      "}")
        self.discardbtn.setObjectName("discardbtn")
        self.horizontalLayout_5.addWidget(self.discardbtn)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.savebtn = QtWidgets.QPushButton(self.widget_7)
        self.savebtn.setMinimumSize(QtCore.QSize(0, 35))
        self.savebtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.savebtn.clicked.connect(self.Choose_where_to_save)
        self.savebtn.setStyleSheet("#savebtn{\n"
                                   "background: #2E74A9;\n"
                                   "font-weight:bold;\n"
                                   "color: white;\n"
                                   "border-radius: 16px;\n"
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
        self.horizontalLayout_6.addWidget(self.savebtn)
        self.horizontalLayout_4.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.adddetails = QtWidgets.QPushButton(self.widget_8)
        self.adddetails.setMinimumSize(QtCore.QSize(0, 35))
        self.adddetails.setMaximumSize(QtCore.QSize(16777215, 35))
        self.adddetails.setStyleSheet("#adddetails{\n"
                                      "background: #6F4B27;\n"
                                      "font-weight:bold;\n"
                                      "color: white;\n"
                                      "border-radius: 16px;\n"
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
        self.horizontalLayout_7.addWidget(self.adddetails)
        self.horizontalLayout_4.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.print1 = QtWidgets.QPushButton(self.widget_9)
        self.print1.setMinimumSize(QtCore.QSize(0, 35))
        self.print1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.print1.setStyleSheet("#print1{\n"
                                  "background: #2E74A9;\n"
                                  "font-weight:bold;\n"
                                  "color: white;\n"
                                  "border-radius: 16px;\n"
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
        icon.addPixmap(QtGui.QPixmap("images/print_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print1.setIcon(icon)
        self.print1.setIconSize(QtCore.QSize(30, 30))
        self.print1.setObjectName("print1")
        self.horizontalLayout_8.addWidget(self.print1)
        self.horizontalLayout_4.addWidget(self.widget_9)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Crack Detected:"))
        self.label_2.setText(_translate("MainWindow", "Length:"))
        self.label_3.setText(_translate("MainWindow", "Width: "))
        self.widgetPosition.setText(_translate("MainWindow", "Position:"))
        self.position_lbl.setText(_translate("MainWindow", "Horizontal"))
        self.discardbtn.setText(_translate("MainWindow", "Discard"))
        self.savebtn.setText(_translate("MainWindow", "Save"))
        self.adddetails.setText(_translate("MainWindow", "Add Details"))
        self.print1.setText(_translate("MainWindow", "Print"))

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
        dialog = QtWidgets.QDialog()
        dialog.setObjectName("Dialog")
        dialog.resize(419, 365)
        # Create the main layout
        layout = QVBoxLayout(dialog)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'Projects.db')
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
        dialog.setLayout(main_layout)
        dialog.exec()
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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
