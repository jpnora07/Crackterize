import os
import sqlite3
import sys
from datetime import datetime
from functools import partial

import tensorflow as tf
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter
from tensorflow import keras
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QByteArray, QThread, QSizeF, QSize
from PyQt5.QtGui import QPixmap, QMovie, QPainter, QTextCursor, QTextImageFormat, QFont, QTextCharFormat, QTextDocument
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QScrollArea, QWidget, QFileDialog, QDialog, QFrame

from Detect_Crack import Detect_Crack_Dialog
from Segment_Image import Ui_DialogSegment
from result import Result_Dialog
from view_result_with_details import result_with_details


class view_result_dialog(object):
    def __init__(self, background_widget, view_folder_dialog_orig, history, projects, mainwindow):
        self.Mainwindow = mainwindow
        self.history = history
        self.myProjects = projects
        self.background_widget = background_widget
        self.view_folder_dialog_orig = view_folder_dialog_orig

    def setupUi(self, view_folder_dialog):
        # self.data_added.connect(self.refreshWidget)
        self.view_folder_dialog = view_folder_dialog
        view_folder_dialog.setObjectName("MainWindow")
        view_folder_dialog.resize(700, 600)
        view_folder_dialog.setMaximumSize(700, 600)
        view_folder_dialog.setWindowFlags(Qt.FramelessWindowHint)
        view_folder_dialog.setMinimumSize(700, 600)
        view_folder_dialog.setStyleSheet(
            """
            background:rgb(255, 255, 255);
            """
        )

        view_folder_dialog.setObjectName("view_folder_dialog")
        self.verticalLayout = QtWidgets.QVBoxLayout(view_folder_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(view_folder_dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("verticalLayout_2")
        self.project_name_lbl = QtWidgets.QLabel(self.widget)
        self.project_name_lbl.setStyleSheet("#project_name_lbl {\n"
                                            "font: 700 9pt \"Franklin Gothic Medium\";\n"
                                            "position: absolute;\n"
                                            "width: 50px;\n"
                                            "height: 50px;\n"
                                            "left: 143px;\n"
                                            "top: 236px;\n"
                                            "font-family: \'Franklin Gothic Medium\';\n"
                                            "font-style: normal;\n"
                                            "font-weight: 600;\n"
                                            "font-size: 30px;\n"
                                            "line-height: 42px;\n"
                                            "text-align: center;\n"
                                            "color: #664323;\n"
                                            "}")
        self.project_name_lbl.setObjectName("project_name_lbl")
        with open('selected_project.txt', 'r') as f:
            self.selected_project = f.read()
        with open('selected_folder_vrFile.txt', 'r') as f:
            self.selected_item = f.read()
            self.project_name_lbl.setText(self.selected_project + " > " + self.selected_item)
        self.horizontalLayout_2.addWidget(self.project_name_lbl)

        self.addfolder_icon = QtWidgets.QPushButton("  Add Image", self.widget)
        self.addfolder_icon.setStyleSheet("#addfolder_icon{\n"
                                          "padding:5px;\n"
                                          "background-color:#E3E9ED;"
                                          "color:#664323;\n"
                                          "font: 700 9pt \"Big Sky Regular\";\n"
                                          "margin-left:100px;\n"
                                          "margin-right:30px;\n"
                                          "border: none;"
                                          "border-radius:5px"
                                          "}"
                                          "#addfolder_icon::hover{\n"
                                          "background-color:#CFD9E0;"
                                          "border: none;"
                                          "}"
                                          )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addfolder_icon.setIcon(icon)
        self.addfolder_icon.setIconSize(QtCore.QSize(10, 10))
        self.addfolder_icon.setFixedSize(250, 33)
        # self.addfolder_icon.clicked.connect(self.creating_new_Location)
        self.addfolder_icon.clicked.connect(self.add_new_image)
        self.addfolder_icon.setObjectName("addfolder_icon")
        self.horizontalLayout_2.addWidget(self.addfolder_icon)

        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(view_folder_dialog)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setContentsMargins(10, 10, 10, 10)
        # buttons
        self.buttons = []
        self.max_per_row = 4

        layout = QHBoxLayout()

        widget = QtWidgets.QWidget(view_folder_dialog)
        widget.setFixedSize(120, 140)
        widget.setObjectName("widget")
        verticalLayout = QtWidgets.QVBoxLayout(widget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        button = QtWidgets.QPushButton(widget)
        button.setMinimumSize(QtCore.QSize(90, 100))
        button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/add-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(90, 100))
        button.setFlat(True)
        button.setObjectName("pushButton")
        button.clicked.connect(self.add_new_image)
        button.setStyleSheet(
            "#pushButton{\n"
            "color: rgb(255, 255, 255);\n"
            "border : none;\n"
            "background-color: white;\n"
            "}\n"
            "#pushButton:hover{\n"
            "color: rgb(255, 255, 255);\n"
            "border : none;\n"
            "background-color: white;\n"
            "}\n"
            "")
        verticalLayout.addWidget(button)
        label = QtWidgets.QLabel('Upload Image', widget)
        label.setStyleSheet("\n"
                            "                font: 700 9pt \\\"Franklin Gothic Medium\\\";\n"
                            "                font-family: \\\'Franklin Gothic Medium\\\';\n"
                            "               font-style: normal;\n"
                            "                font-weight: 200;\n"
                            "                font-size: 13px;\n"
                            "                line-height: 42px;\n"
                            "                color: #664323;\n"
                            "                padding-bottom: 5px;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        verticalLayout.addWidget(label)

        self.buttons.append(button)

        # create scroll area
        self.scroll = QScrollArea(self.widget_3)
        self.scroll.setWidgetResizable(True)
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_widget = QWidget()
        self.scroll.setWidget(self.scroll_widget)
        # set stylesheet for scroll area and scroll widget
        self.scroll.setStyleSheet("""
            QScrollArea {
                background-color: #ffffff;
                border: none;
            }
            QScrollBar:vertical {
                background-color: #ffffff;
                width: 30px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #cfcfcf;
                min-height: 30px;
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        self.scroll_widget.setStyleSheet("""
                    QScrollArea > QWidget > QWidget {
                        background-color: #ffffff; /* set the background color of the scroll area */
                        border: none; /* remove border */
                        width: 20px; /* set width of the scrollbar */
                    }
                """)

        layout.addWidget(widget)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        vbox = QVBoxLayout(self.scroll_widget)
        vbox.addLayout(layout)  # Enable wrapping

        main_layout = QVBoxLayout(self.widget_3)
        main_layout.addWidget(self.scroll)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(view_folder_dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.print = QtWidgets.QPushButton("Print", self.frame)
        self.print.setStyleSheet("#print{\n"
                                 "height:40px;\n"
                                 "font-weight:bold;\n"
                                 "font-size:18px;\n"
                                 "color:white;\n"
                                 "background-color: #2E74A9;\n"
                                 "border-top-left-radius :20px;\n"
                                 "border-top-right-radius : 20px; \n"
                                 "border-bottom-left-radius : 20px; \n"
                                 "border-bottom-right-radius : 20px;\n"
                                 "}\n"
                                 "#print:hover{\n"
                                 "color:#2E74A9;\n"
                                 "border :2px solid #2E74A9;\n"
                                 "background-color: white;\n"
                                 "}\n"
                                 "")
        self.print.setFlat(False)
        self.print.setObjectName("print")
        self.print.clicked.connect(self.printer)
        self.horizontalLayout_3.addWidget(self.print)

        self.back = QtWidgets.QPushButton("Back", self.frame)
        self.back.setStyleSheet("#back{\n"
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
                                "#back:hover{\n"
                                "color:rgb(144, 115, 87);\n"
                                "border :2px solid rgb(144, 115, 87);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "}\n"
                                "")
        self.back.setFlat(False)
        self.back.clicked.connect(self.closeEvent)
        self.back.setObjectName("back")
        self.horizontalLayout_3.addWidget(self.back)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget_2)

        # Add transparent white background widget
        self.background_widget_results = QFrame(view_folder_dialog)
        self.background_widget_results.setStyleSheet("background-color: rgba(0, 0, 0, 0.25);")
        self.background_widget_results.resize(view_folder_dialog.width(), view_folder_dialog.height())
        self.background_widget_results.hide()

        QtCore.QMetaObject.connectSlotsByName(view_folder_dialog)

        # Calling a function that fetch the folders of project
        self.fetch_folders_of_projects()

    def printer(self):

        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, 'Projects.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM Save_Files WHERE folder_name = ? ORDER BY created_at DESC", (self.selected_item,))
        rows = c.fetchall()

        try:
            printer = QPrinter()
            printer.setPageSize(QPrinter.Letter)
            printer.setOrientation(QPrinter.Portrait)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName("preview.pdf")

            # create a QTextDocument to hold the text to be printed
            doc = QTextDocument()
            doc.setPageSize(QSizeF(792, 612))  # set page size to 11x8.5 inches (in points)
            doc.setDocumentMargin(36)

            # create a QTextCursor to insert text into the QTextDocument
            cursor = QTextCursor(doc)

            font_format = QTextCharFormat()
            font_format.setFont(QFont("Arial", 15))
            bold_format = QTextCharFormat()
            bold_format.setFont(QFont("Arial", 15))
            bold_format.setFontWeight(QFont.Bold)

            # loop through the fetched data and add each row to a separate page
            for row in rows:
                # image_data = row[15]
                # pixmap = QPixmap()
                # pixmap.loadFromData(image_data)
                dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
                images_path = os.path.join(dir_path, 'Result Images')

                if not os.path.exists(images_path):
                    os.makedirs(images_path)

                # save the image to a file with the id as the name
                # file_path = os.path.join(images_path, f"{row[0]}.png")
                # pixmap.save(file_path, "PNG")

                # get all the image file names in the folder
                file_names = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

                # find the file name that matches the row ID
                for file_name in file_names:
                    if os.path.splitext(file_name)[0] == str(row[0]):
                        # add the saved image to the document
                        max_size = QSize(700, 450)
                        image_format = QTextImageFormat()
                        image_format.setWidth(max_size.width())
                        image_format.setHeight(max_size.height())
                        image_format.setName(os.path.join(images_path, file_name))
                        header_html = "<h1 style='font-size: 18px;'>Crackterize Result</h1>"
                        table_html = f'''
                            <table>
                                <tr>
                                    <td>
                                        <p style='font-size: 16px;'>The image characterized as: <b>{row[9]}</b></p>
                                        <p style='font-size: 16px;'>Length: <b>{row[5]}</b></p>
                                        <p style='font-size: 16px;'>Width: <b>{row[4]}</b></p>
                                        <p style='font-size: 16px;'>Positive Crack Probability: <b>{row[8]}</b></p>
                                        <p style='font-size: 16px;'>Negative Crack Probability: <b>{row[7]}</b></p>
                                        <p style='font-size: 16px;'>Location of Crack: <b>{row[10]}</b></p>
                                        <p style='font-size: 16px;'>Name of Project: <b>{row[16]}</b></p>
                                        <p style='font-size: 16px;'>Name of Folder: <b>{row[1]}</b></p>
                                        <p style='font-size: 16px;'>Date Added: <b>{row[14]}</b></p>
                                        <p style='font-size: 16px;'>Remarks: <b>{row[13]}</b></p>
                                    </td>
                                </tr>
                            </table>
                        '''
                        cursor.insertImage(image_format)
                        cursor.insertHtml(header_html)
                        cursor.insertHtml(table_html)
                        cursor.setPosition(0, QTextCursor.MoveAnchor)
                        cursor.insertHtml("<br><br><br>")
                        break
                        # clear the QTextCursor to start a new page

            # create a QPrinter to print the document
            printer = QPrinter()
            printer.setPageSize(QPrinter.Letter)
            printer.setOrientation(QPrinter.Portrait)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName("preview.pdf")

            # create a QPainter to paint the document onto the printer
            painter = QPainter()
            if painter.begin(printer):
                doc.setPageSize(QSizeF(printer.pageRect().size()))
                doc.drawContents(painter)
                painter.end()

            # preview the document using a QPrintPreviewDialog
            preview = QPrintPreviewDialog(printer)
            preview.paintRequested.connect(doc.print_)
            preview.exec_()
        except Exception as e:
            print(e)

    def closeEvent(self):
        self.view_folder_dialog.close()

    def add_new_image(self):
        try:
            image_path = self.open_file_dialog()
            image = cv2.imread(image_path)
            # Save the image to a temporary file
            temp_file_path = 'temp_image_original.jpg'
            cv2.imwrite(temp_file_path, image)
            if image_path is not None:
                try:
                    self.view_folder_dialog_orig.close()
                    self.view_folder_dialog.close()
                    self.background_widget.show()
                    segment_dialog = QtWidgets.QDialog(self.Mainwindow)
                    ui = Detect_Crack_Dialog(image_path, self.background_widget, self.history, self.myProjects,
                                             self.Mainwindow)
                    ui.setupUi(segment_dialog)
                    x = (self.Mainwindow.width() - segment_dialog.width()) // 2
                    y = (self.Mainwindow.height() - segment_dialog.height()) // 2
                    segment_dialog.move(x, y)
                    segment_dialog.exec_()
                except Exception as e:
                    print(e)
            else:
                print("No file selected.")
        except Exception as e:
            print(e)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter('Images (*.png *.jpg *.bmp)')
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            return selected_files[0]
        else:
            print("File dialog closed without selecting a file.")
            return None

    def creating_new_Location(self):
        # Create dialog box
        AddLocationDialog = QtWidgets.QDialog()
        AddLocationDialog.setObjectName("NewFolderDialog")
        AddLocationDialog.setWindowFlags(Qt.FramelessWindowHint)
        AddLocationDialog.resize(500, 300)
        AddLocationDialog.setMinimumSize(QtCore.QSize(500, 300))
        AddLocationDialog.setMaximumSize(QtCore.QSize(500, 300))
        # set corner radius of dialog box
        AddLocationDialog.setAttribute(Qt.WA_TranslucentBackground)
        # NewProjectDialog.setWindowOpacity(0.6)
        radius = 20
        AddLocationDialog.setStyleSheet("""
                    background:#EFEEEE;
                    border-top-left-radius:{0}px;
                    border-bottom-left-radius:{0}px;
                    border-top-right-radius:{0}px;
                    border-bottom-right-radius:{0}px;
                    """.format(radius))

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(AddLocationDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_1 = QtWidgets.QWidget(AddLocationDialog)
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
        self.ET_newlocation = QtWidgets.QTextEdit(self.widget_2)
        self.ET_newlocation.setMaximumSize(QtCore.QSize(16777215, 53))
        self.ET_newlocation.setStyleSheet("#ET_newproject{\n"
                                          "text-allign:center;\n"
                                          "font-size:20px;\n"
                                          "padding:8px;\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-top-left-radius :12px;\n"
                                          "border-top-right-radius : 12px; \n"
                                          "border-bottom-left-radius : 12px; \n"
                                          "border-bottom-right-radius : 12px;\n"
                                          "}")
        self.ET_newlocation.setTabChangesFocus(False)
        self.ET_newlocation.setPlaceholderText("                 Type name of location")
        self.ET_newlocation.setAlignment(Qt.AlignCenter)
        self.ET_newlocation.setObjectName("ET_newproject")
        self.verticalLayout_3.addWidget(self.ET_newlocation)
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
        self.back_btn.clicked.connect(AddLocationDialog.close)
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
        self.save_btn.clicked.connect(AddLocationDialog.close)
        self.save_btn.clicked.connect(self.addNewButton_to_Db)
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget_1)
        AddLocationDialog.exec()

    def addNewButton_to_Db(self):
        # Get the text from the QTextEdit widget
        location_folder_name = self.ET_newlocation.toPlainText()
        if len(location_folder_name) == 0:
            # If new_projects is empty, show an error message
            self.show_dialog_empty_text_error()
            self.creating_new_Location()
        else:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, 'Projects.db')
            # Create a connection to a SQLite database or create it if it doesn't exist
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()

            # Create a table in the database if it doesn't exist
            self.c.execute('''CREATE TABLE IF NOT EXISTS Location_Folder
                                     (id INTEGER PRIMARY KEY, project_name TEXT, folder_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

            # Check if the project name already exists in the database
            self.c.execute("SELECT COUNT(*) FROM Location_Folder WHERE folder_name = ?", (location_folder_name,))
            result = self.c.fetchone()
            if result[0] == 0:
                # If the project name doesn't exist, insert it into the database
                self.c.execute("INSERT INTO Location_Folder (project_name, folder_name) VALUES (?, ?)",
                               (self.selected_item, location_folder_name,))
                self.conn.commit()
                self.buttons.clear()
                self.clear_layout(self.scroll_widget.layout())
                self.fetch_folders_of_projects()
            else:
                # If the project name already exists, show a dialog message to inform the user
                self.show_dialog_empty_text_error()
                self.creating_new_Location()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clear_layout(child.layout())

    def add_button_folder(self, data):
        try:
            for row in data:
                button_name = str(row[9])
                image_id = row[0]
                image = row[3]
                # Convert the image data to QPixmap
                byte_array = QByteArray(image)
                pixmap = QPixmap()
                pixmap.loadFromData(byte_array)
                widget = QtWidgets.QWidget(self.scroll_widget)
                widget.setFixedSize(120, 140)
                widget.setObjectName("widget")
                verticalLayout = QtWidgets.QVBoxLayout(widget)
                verticalLayout.setContentsMargins(0, 0, 0, 0)
                verticalLayout.setObjectName("verticalLayout")
                btn = QtWidgets.QPushButton(widget)
                btn.setMinimumSize(QtCore.QSize(90, 100))
                # btn.setText(button_name)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(pixmap), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                btn.setIcon(icon)
                btn.setIconSize(QtCore.QSize(90, 100))
                btn.setFlat(True)
                btn.setObjectName("pushButton")
                btn.clicked.connect(partial(self.view_folder, image_id))
                btn.setStyleSheet(

                    "#pushButton{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border : none;\n"
                    "background-color: white;\n"
                    "}\n"
                    "#pushButton:hover{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border : none;\n"
                    "background-color: white;\n"
                    "}\n"
                    "")
                verticalLayout.addWidget(btn)
                btn_label = QtWidgets.QLabel(button_name, widget)
                btn_label.setWordWrap(True)
                btn_label.setStyleSheet("\n"
                                        "  background-color: transparent;  \n"
                                        "                font: 700 9pt \\\"Franklin Gothic Medium\\\";\n"
                                        "                font-family: \\\'Franklin Gothic Medium\\\';\n"
                                        "               font-style: normal;\n"
                                        "                font-weight: 200;\n"
                                        "                font-size: 13px;\n"
                                        "                line-height: 42px;\n"
                                        "                color: #664323;\n"
                                        "                padding-bottom: 5px;")
                btn_label.setAlignment(QtCore.Qt.AlignCenter)
                btn_label.setObjectName("label")
                verticalLayout.addWidget(btn_label)
                self.buttons.append(btn)

                # add to layout
                if len(self.buttons) % self.max_per_row == 1:
                    hbox = QHBoxLayout()
                    self.scroll_widget.layout().insertLayout(0, hbox)
                else:
                    hbox = self.scroll_widget.layout().itemAt(0).layout()

                hbox.insertWidget(0, widget)
                hbox.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        except Exception as e:
            print(e)

    def view_folder(self, image_id):
        print("Image ID: ", image_id)
        self.id = image_id
        try:
            with open('image_id.txt', 'w') as f:
                f.write(str(self.id))
            view_result_dialog = QtWidgets.QDialog(self.Mainwindow)
            ui = result_with_details(self.background_widget, self.history)

            ui.setupUi(view_result_dialog)
            view_result_dialog.exec_()
        except Exception as e:
            print(e)

    def show_dialog_empty_text_error(self):
        # Create dialog box
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        # set corner radius of dialog box
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QTimer()
        self.timer.timeout.connect(Dialog.close)
        self.timer.start(1500)
        # Dialog.setWindowOpacity(0.6)
        radius = 20
        Dialog.setStyleSheet("""
                                            background:#EFEEEE;
                                            border-top-left-radius:{0}px;
                                            border-bottom-left-radius:{0}px;
                                            border-top-right-radius:{0}px;
                                            border-bottom-right-radius:{0}px;
                                            """.format(radius))

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setText("Project name cannot be empty")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "QLabel { font:\"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 15pt;background-color: transparent;  \n}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setAutoFillBackground(False)
        self.widget_4.setStyleSheet("#widget_4{\n"
                                    "background-image: url(images/ok3.png);\n"
                                    "background-repeat: no-repeat; \n"
                                    "background-position: center;}")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget)
        Dialog.exec()

    def fetch_folders_of_projects(self):
        with open('selected_folder_vrFile.txt', 'r') as f:
            folder_name = f.read()
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
        self.c.execute("SELECT * FROM Save_Files WHERE folder_name = ? ", (folder_name,))
        data = self.c.fetchall()
        self.add_button_folder(data)

    def loading(self):
        Dialog = QDialog()
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 235)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setStyleSheet("background-color:#ffffff;")
        radius = 15
        Dialog.setStyleSheet("""
                                                            background:#EFEEEE;
                                                            border-top-left-radius:{0}px;
                                                            border-bottom-left-radius:{0}px;
                                                            border-top-right-radius:{0}px;
                                                            border-bottom-right-radius:{0}px;
                                                            """.format(radius))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color:#ffffff;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_process = QtWidgets.QLabel("Uploading...", self.widget)
        self.label_process.setStyleSheet(
            "  background-color: transparent;  \n"
            "font-size:30px;\n"
            "color: #6c757d;\n"
            "font-style: Inter;")
        self.label_process.setScaledContents(True)
        self.label_process.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_process.setWordWrap(True)
        self.label_process.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_process)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("background-color:#ffffff;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.movie = QMovie("images/spin_loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "  background-color: transparent;")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.show()
        return Dialog
