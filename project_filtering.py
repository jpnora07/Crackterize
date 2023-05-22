# -*- coding: utf-8 -*-
import os
import sqlite3
from datetime import datetime

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSizeF, QSize, Qt, QDate
from PyQt5.QtGui import QFontMetrics, QTextCursor, QPainter, QTextImageFormat, QTextDocument, QFont, QTextFrameFormat, \
    QImage, QPixmap, QTextBlockFormat
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QCheckBox, QDialog, QDateEdit, QCalendarWidget, QHeaderView, QTableView


class CustomDateEdit(QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCalendarPopup(True)  # Enable the calendar popup

        # Create a custom QCalendarWidget and set its size
        calendar_widget = QCalendarWidget(self)  # Set the desired size of the custom calendar widget
        font = QtGui.QFont()
        font.setPointSize(6)
        calendar_widget.setFont(font)
        calendar_widget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        calendar_widget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        calendar_widget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        calendar_widget.setStyleSheet('''
            QToolButton#qt_calendar_prevmonth {
                qproperty-iconSize: 15px;
                qproperty-icon: url(images/previous.png);
            }
            QToolButton#qt_calendar_nextmonth {
                qproperty-iconSize: 15px;
                qproperty-icon: url(images/next.png);
            }
            QToolButton#qt_calendar_monthbutton {
                color: grey;
                width: 90px;
                font-size:12px;
            }
            QToolButton#qt_calendar_yearbutton {
                color: grey;
                width: 50px;
                font-size:12px;
            }
            #qt_calendar_navigationbar {
            width:100px;
}
            QCalendarWidget QAbstractItemView
            { 
                selection-background-color: #D8D5D4; 
                selection-color: #555555;
                outline:0px;
            }
            QCalendarWidget QWidget 
            {
              color:grey;
            }
            QCalendarWidget QTableView
            {
                border-width:0px;
            }
}
        ''')

        self.setCalendarWidget(calendar_widget)


class filter_print(object):
    def __init__(self, background_widget):
        super().__init__()
        self.background_widget = background_widget
        self.checkbox_list = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 618)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setStyleSheet("background-color:#FDF3e9;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("#widget{\n"
                                  "background-color: #FDF3e9\n"
                                  ";}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(40, -1, 40, 40)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel("Select Category", self.widget_3)
        self.label.setStyleSheet("#label{\n"
                                 "font-size: 30px;\n"
                                 "color: rgba(111, 75, 39, 0.77);\n"
                                 "font-weight: bold;}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.widgetex = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayout_2.addWidget(self.widgetex)
        self.exit_2 = QtWidgets.QPushButton(self.widget_3)
        self.exit_2.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_2.setMaximumSize(QtCore.QSize(30, 30))
        self.exit_2.setStyleSheet("border:none;")
        self.exit_2.clicked.connect(Dialog.close)
        self.exit_2.clicked.connect(self.background_widget.hide)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_2.setIcon(icon)
        self.exit_2.setAutoDefault(True)
        self.exit_2.setDefault(True)
        self.exit_2.setFlat(True)
        self.exit_2.setObjectName("exit_2")
        self.horizontalLayout_2.addWidget(self.exit_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(750, 450))
        self.widget_2.setMaximumSize(QtCore.QSize(750, 450))
        self.widget_2.setStyleSheet("background-color: rgba(76,146,215,255);\n"
                                    "border-radius: 30px;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setStyleSheet("background-color: white;\n"
                                    "border-radius: 30px;\n"
                                    "")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollAreanew = QtWidgets.QScrollArea(self.widget_4)
        self.scrollAreanew.setStyleSheet("QScrollBar:vertical\n"
                                         "    {\n"
                                         "        background-color: #c3c3c3;\n"
                                         "        width: 15px;\n"
                                         "        margin: 15px 3px 15px 3px;\n"
                                         "        border: 1px transparent #2A2929;\n"
                                         "        border-radius: 4px;\n"
                                         "    }\n"
                                         "\n"
                                         "    QScrollBar::handle:vertical\n"
                                         "    {\n"
                                         "        background-color: #8c8c8c;         /* #605F5F; */\n"
                                         "        min-height: 5px;\n"
                                         "        border-radius: 4px;\n"
                                         "    }\n"
                                         "\n"
                                         "    QScrollBar::sub-line:vertical\n"
                                         "    {\n"
                                         "        margin: 3px 0px 3px 0px;\n"
                                         "        border-image: url(:/images/up_arrow_disabled.png);        /* # <-------- */\n"
                                         "        height: 10px;\n"
                                         "        width: 10px;\n"
                                         "        subcontrol-position: top;\n"
                                         "        subcontrol-origin: margin;\n"
                                         "    }\n"
                                         "\n"
                                         "    QScrollBar::add-line:vertical\n"
                                         "    {\n"
                                         "        margin: 3px 0px 3px 0px;\n"
                                         "        border-image: url(:/images/down_arrow_disabled.png);       /* # <-------- */\n"
                                         "        height: 10px;\n"
                                         "        width: 10px;\n"
                                         "        subcontrol-position: bottom;\n"
                                         "        subcontrol-origin: margin;\n"
                                         "    }\n"
                                         "    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                         "    {\n"
                                         "        background: none;\n"
                                         "    }\n"
                                         "\n"
                                         "    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                         "    {\n"
                                         "        background: none;\n"
                                         "    }")
        self.scrollAreanew.setWidgetResizable(True)
        self.scrollAreanew.setObjectName("scrollAreanew")
        self.scrollAreaWidgetContentsnew = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsnew.setGeometry(QtCore.QRect(0, 0, 432, 432))
        self.scrollAreaWidgetContentsnew.setStyleSheet("")
        self.scrollAreaWidgetContentsnew.setObjectName("scrollAreaWidgetContentsnew")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContentsnew)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.scrollAreaWidgetContentsnew)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 415, 488))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.widget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel("  Projects", self.widget_8)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setStyleSheet("#label_3{\n"
                                   "font-size: 18px;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-weight: bold;}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)

        self.projects_wdgt = QtWidgets.QWidget(self.widget_8)
        self.projects_wdgt.setMinimumSize(QtCore.QSize(0, 0))
        self.projects_wdgt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.projects_wdgt.setObjectName("projects_wdgt")
        self.verticalLayout_8 = QtWidgets.QGridLayout(self.projects_wdgt)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, 'Projects.db')
            # Create a connection to a SQLite database or create it if it doesn't exist
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM Projects")
            rows = self.c.fetchall()
            row_count = 0
            col_count = 0
            for row in rows:
                project_name = str(row[1])
                self.proj_name = project_name
                # Create a checkbox for each project and set its properties
                project_chb = QtWidgets.QRadioButton(self.projects_wdgt)
                self.project_chb = project_chb
                font_metrics = QFontMetrics(project_chb.font())
                # Get the width of the text
                text_width = font_metrics.width(project_chb.text())
                project_chb.setMinimumSize(QtCore.QSize(text_width, 30))
                project_chb.setStyleSheet("#project_chb {border : 1px solid rgba(76,146,215,255);\n"
                                          "border-radius :15px;\n"
                                          "color:black;\n"
                                          "    text-align: center;"
                                          "font-size:13px;\n"
                                          "padding-right:10px;"
                                          "}\n"
                                          "#project_chb::indicator{border : 2px solid rgba(76,146,215,255);\n"
                                          "width : 16px;\n"
                                          "height : 16px;\n"
                                          "border-radius :10px;\n"
                                          "margin-left:5px;}\n"
                                          "#project_chb::indicator:checked {\n"
                                          "image: url(images/checkbox.png);\n"
                                          "}\n"
                                          "")
                project_chb.setObjectName("project_chb")
                project_chb.setText(project_name)
                project_chb.clicked.connect(self.project_chosen)

                # Add the checkbox to the layout
                self.verticalLayout_8.addWidget(project_chb, row_count, col_count)
                col_count += 1
                if col_count == 3:  # Maximum number of columns
                    col_count = 0
                    row_count += 1
        except Exception as e:
            print(e)

        self.verticalLayout_5.addWidget(self.projects_wdgt)
        self.verticalLayout_4.addWidget(self.widget_8)

        self.folders_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.folders_widget.hide()
        self.folders_widget.setObjectName("folders_widget")
        # self.folders_widget.hide()
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.folders_widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_20 = QtWidgets.QWidget(self.folders_widget)
        self.widget_20.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_20.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(" Folders", self.widget_20)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_4.setStyleSheet("#label_4{\n"
                                   "font-size: 18px;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-weight: bold;\n"
                                   "border-right:1px solid grey;\n"
                                   "}")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.select_all_fold = QtWidgets.QPushButton("Select All", self.widget_20)
        font_metrics = QFontMetrics(self.select_all_fold.font())
        # Get the width of the text
        text_width = font_metrics.width(self.select_all_fold.text()) + 20
        self.select_all_fold.setMaximumSize(QtCore.QSize(text_width, 16777215))
        self.select_all_fold.setStyleSheet("#select_all_fold{color: rgba(76,146,215,255);}\n"
                                           "#select_all_fold::hover{border-bottom:1px solid  rgba(76,146,215,255);;}\n"
                                           "")
        self.select_all_fold.setFlat(True)
        self.select_all_fold.setObjectName("select_all_fold")
        self.select_all_fold.clicked.connect(self.mark_all_checkboxes_folder)
        self.horizontalLayout_10.addWidget(self.select_all_fold)
        self.label_11 = QtWidgets.QLabel("∘", self.widget_20)
        self.label_11.setMinimumSize(QtCore.QSize(10, 0))
        self.label_11.setMaximumSize(QtCore.QSize(10, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgba(76,146,215,255);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.clear_all_fold = QtWidgets.QPushButton("Clear all", self.widget_20)
        self.clear_all_fold.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clear_all_fold.setStyleSheet("#clear_all_fold{color: rgba(76,146,215,255);}\n"
                                          "#clear_all_fold::hover{border-bottom:1px solid  rgba(76,146,215,255);;}\n"
                                          "")
        self.clear_all_fold.setFlat(True)
        self.clear_all_fold.setObjectName("clear_all_fold")
        self.clear_all_fold.clicked.connect(self.clear_all_checkboxes_folder)
        self.horizontalLayout_10.addWidget(self.clear_all_fold)
        self.widget_24 = QtWidgets.QWidget(self.widget_20)
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_10.addWidget(self.widget_24)
        self.verticalLayout_6.addWidget(self.widget_20)
        self.widget_fo = QtWidgets.QWidget(self.folders_widget)
        self.widget_fo.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_fo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_fo.setObjectName("widget_fo")
        self.verticalLayout_12 = QtWidgets.QGridLayout(self.widget_fo)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        self.verticalLayout_6.addWidget(self.widget_fo)
        self.verticalLayout_4.addWidget(self.folders_widget)

        self.non_crack_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.non_crack_widget.hide()
        self.non_crack_widget.setObjectName("non_crack_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.non_crack_widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_22 = QtWidgets.QWidget(self.non_crack_widget)
        self.widget_22.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_22.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(" Crack Inclusion / Exclusion", self.widget_22)
        self.label_5.setMinimumSize(QtCore.QSize(255, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setStyleSheet("#label_5{\n"
                                   "font-size: 18px;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-weight: bold;\n"
                                   "border-right:1px solid grey;\n"
                                   "}")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.select_all = QtWidgets.QPushButton("Select All", self.widget_22)
        self.select_all.clicked.connect(self.mark_all_checkboxes_crack_i_e)

        font_metrics = QFontMetrics(self.select_all.font())
        # Get the width of the text
        text_width = font_metrics.width(self.select_all.text()) + 20
        self.select_all.setMaximumSize(QtCore.QSize(text_width, 16777215))
        self.select_all.setStyleSheet("#select_all{color: rgba(76,146,215,255);}\n"
                                      "#select_all::hover{border-bottom:1px solid  rgba(76,146,215,255);;}\n"
                                      "")
        self.select_all.setFlat(True)
        self.select_all.setObjectName("select_all")
        self.horizontalLayout_11.addWidget(self.select_all)
        self.label_17 = QtWidgets.QLabel("∘", self.widget_22)
        self.label_17.setMinimumSize(QtCore.QSize(10, 0))
        self.label_17.setMaximumSize(QtCore.QSize(10, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgba(76,146,215,255);")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_11.addWidget(self.label_17)
        self.clear_all = QtWidgets.QPushButton("Clear all", self.widget_22)
        self.clear_all.clicked.connect(self.clear_all_checkboxes_crack_i_e)
        self.clear_all.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clear_all.setStyleSheet("#clear_all{color: rgba(76,146,215,255);}\n"
                                     "#clear_all::hover{border-bottom:1px solid  rgba(76,146,215,255);;}\n"
                                     "")
        self.clear_all.setFlat(True)
        self.clear_all.setObjectName("clear_all")
        self.horizontalLayout_11.addWidget(self.clear_all)

        self.widget_211 = QtWidgets.QWidget(self.widget_22)
        self.horizontalLayout_11.addWidget(self.widget_211)
        self.verticalLayout_7.addWidget(self.widget_22)
        self.non_crack_2nd_widget = QtWidgets.QWidget(self.non_crack_widget)
        self.non_crack_2nd_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.non_crack_2nd_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.non_crack_2nd_widget.setObjectName("non_crack_2nd_widget")
        self.horizontalLayout_5 = QtWidgets.QGridLayout(self.non_crack_2nd_widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        try:
            rows = ["Images without Detected Cracks", "Images with Detected Cracks"]
            row_count = 0
            col_count = 0
            self.non_crack_chb_list = []
            for row in rows:
                non_crack_name = row
                # Create a checkbox for each project and set its properties
                non_crack_chb = QtWidgets.QCheckBox(self.non_crack_2nd_widget)
                # Get the font metrics of the checkbox's text
                font_metrics = QFontMetrics(non_crack_chb.font())
                # Get the width of the text
                text_width = font_metrics.width(non_crack_chb.text())
                non_crack_chb.setMinimumSize(QtCore.QSize(text_width, 30))
                non_crack_chb.setStyleSheet("#folder_name {border : 1px solid rgba(76,146,215,255);\n"
                                            "border-radius :15px;\n"
                                            "color:black;\n"
                                            "text-align: center;"
                                            "font-size:13px;\n"
                                            "padding-right:10px;\n"
                                            "}\n"
                                            "#folder_name::indicator{border : 2px solid rgba(76,146,215,255);\n"
                                            "width : 16px;\n"
                                            "height : 16px;\n"
                                            "border-radius :10px;\n"
                                            "margin-left:5px;}\n"
                                            "#folder_name::indicator:checked {\n"
                                            "image: url(images/checkbox.png);\n"
                                            "}\n"
                                            "")
                non_crack_chb.setTristate(False)
                non_crack_chb.setObjectName("folder_name")
                non_crack_chb.setText(non_crack_name)
                non_crack_chb.clicked.connect(self.show_chb_loc)
                self.non_crack_chb_list.append(non_crack_chb)

                # Add the checkbox to the layout
                self.horizontalLayout_5.addWidget(non_crack_chb, row_count, col_count)
                col_count += 1
                if col_count == 3:  # Maximum number of columns
                    col_count = 0
                    row_count += 1
        except Exception as e:
            print(e)

        self.verticalLayout_7.addWidget(self.non_crack_2nd_widget)
        self.verticalLayout_4.addWidget(self.non_crack_widget)

        self.crack_loc_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.crack_loc_widget.hide()
        self.crack_loc_widget.setObjectName("crack_loc_widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.crack_loc_widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_23 = QtWidgets.QWidget(self.crack_loc_widget)
        self.widget_23.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_23.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_6 = QtWidgets.QLabel(" Crack Location", self.widget_23)

        self.label_6.setStyleSheet("#label_6{\n"
                                   "font-size: 18px;\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-weight: bold;\n"
                                   "border-right:1px solid grey;\n"
                                   "}")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.adjustSize()
        self.horizontalLayout_18.addWidget(self.label_6)
        self.select_all_loc = QtWidgets.QPushButton("Select All", self.widget_23)
        font_metrics = QFontMetrics(self.select_all_loc.font())
        # Get the width of the text
        text_width = font_metrics.width(self.select_all_loc.text()) + 20
        self.select_all_loc.setMaximumSize(QtCore.QSize(text_width, 16777215))
        self.select_all_loc.setStyleSheet("#select_all_loc{color: rgba(76,146,215,255);}\n"
                                          "#select_all_loc::hover{border-bottom:1px solid  rgba(76,146,215,255);;}\n"
                                          "")
        self.select_all_loc.setFlat(True)
        self.select_all_loc.setObjectName("select_all_loc")
        self.select_all_loc.clicked.connect(self.mark_all_checkboxes_loc)
        self.horizontalLayout_18.addWidget(self.select_all_loc)
        self.label_20 = QtWidgets.QLabel("∘", self.widget_23)
        self.label_20.setMinimumSize(QtCore.QSize(10, 0))
        self.label_20.setMaximumSize(QtCore.QSize(10, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgba(76,146,215,255);")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_18.addWidget(self.label_20)
        self.clear_all_loc = QtWidgets.QPushButton("Clear all", self.widget_23)
        self.clear_all_loc.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clear_all_loc.setStyleSheet("#clear_all_loc{color: rgba(76,146,215,255);}\n"
                                         "#clear_all_loc::hover{border-bottom:1px solid  rgba(76,146,215,255);;}\n"
                                         "")
        self.clear_all_loc.setFlat(True)
        self.clear_all_loc.setObjectName("clear_all_loc")
        self.clear_all_loc.clicked.connect(self.clear_all_checkboxes_loc)
        self.horizontalLayout_18.addWidget(self.clear_all_loc)
        self.widget_12 = QtWidgets.QWidget(self.widget_23)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_18.addWidget(self.widget_12)
        self.verticalLayout_9.addWidget(self.widget_23)
        self.crack_loc_2nd_widget = QtWidgets.QWidget(self.crack_loc_widget)
        self.crack_loc_2nd_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.crack_loc_2nd_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.crack_loc_2nd_widget.setObjectName("crack_loc_2nd_widget")
        self.horizontalLayout_6 = QtWidgets.QVBoxLayout(self.crack_loc_2nd_widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.crack_loc_chb_widget = QtWidgets.QWidget(self.crack_loc_2nd_widget)
        self.crack_loc_chb_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.crack_loc_chb_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.crack_loc_chb_widget.setObjectName("crack_loc_chb_widget")

        self.horizontalLayout_19 = QtWidgets.QGridLayout(self.crack_loc_chb_widget)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")

        try:
            rows = [
                "Column",
                "Beam",
                "Slab (Suspended)",
                "Slab (On Grid)",
                "Walls",
                "Window Edges",
                "Door Edges",
                "Canopy",
                "Roof Deck"
            ]
            row_count = 0
            col_count = 0
            self.crack_loc_chb_list = []
            for row in rows:
                crack_loc_name = row
                # Create a checkbox for each project and set its properties
                crack_loc_chb = QtWidgets.QCheckBox(self.crack_loc_chb_widget)
                font_metrics = QFontMetrics(crack_loc_chb.font())
                # Get the width of the text
                text_width = font_metrics.width(crack_loc_chb.text())
                crack_loc_chb.setMinimumSize(QtCore.QSize(text_width, 30))
                crack_loc_chb.setStyleSheet("#folder_name {border : 1px solid rgba(76,146,215,255);\n"
                                            "border-radius :15px;\n"
                                            "color:black;\n"
                                            "    text-align: center;"
                                            "font-size:13px;\n"
                                            "padding-right:10px;"
                                            "}\n"
                                            "#folder_name::indicator{border : 2px solid rgba(76,146,215,255);\n"
                                            "width : 16px;\n"
                                            "height : 16px;\n"
                                            "border-radius :10px;\n"
                                            "margin-left:5px;}\n"
                                            "#folder_name::indicator:checked {\n"
                                            "image: url(images/checkbox.png);\n"
                                            "}\n"
                                            "")
                crack_loc_chb.setTristate(False)
                crack_loc_chb.setObjectName("folder_name")
                crack_loc_chb.setText(crack_loc_name)
                self.crack_loc_chb_list.append(crack_loc_chb)

                # Add the checkbox to the layout
                self.horizontalLayout_19.addWidget(crack_loc_chb, row_count, col_count)
                col_count += 1
                if col_count == 3:  # Maximum number of columns
                    col_count = 0
                    row_count += 1
        except Exception as e:
            print(e)
        self.horizontalLayout_6.addWidget(self.crack_loc_chb_widget)

        self.verticalLayout_9.addWidget(self.crack_loc_2nd_widget)
        self.verticalLayout_4.addWidget(self.crack_loc_widget)

        self.date_picker_widg = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.date_picker_widg.setObjectName("date_picker_widg")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.date_picker_widg)
        self.verticalLayout_51.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName("verticalLayout_5")
        self.label_31 = QtWidgets.QLabel("  Date", self.date_picker_widg)
        self.label_31.setMinimumSize(QtCore.QSize(0, 40))
        self.label_31.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_31.setStyleSheet("#label_3{\n"
                                    "font-size: 18px;\n"
                                    "color: rgba(111, 75, 39, 0.77);\n"
                                    "font-weight: bold;}")
        self.label_31.setObjectName("label_3")
        self.widget_2datepicker = QtWidgets.QWidget(self.date_picker_widg)
        self.hori_for_date = QtWidgets.QHBoxLayout(self.widget_2datepicker)
        self.hori_for_date.setContentsMargins(0, -1, 0, -1)
        self.hori_for_date.setSpacing(0)
        self.hori_for_date.setObjectName("hori_for_date")

        self.label_312 = QtWidgets.QLabel("  From", self.widget_2datepicker)
        self.label_312.setAlignment(Qt.AlignCenter)
        font_metrics = QFontMetrics(self.label_312.font())
        # Get the width of the text
        text_width = font_metrics.width(self.label_312.text()) + 20
        self.label_312.setFixedSize(text_width, 30)
        self.label_312.setStyleSheet(
            "font-size: 12px;\n"
            "color: #5C5C5C;\n"
            "font-weight: 400;"
            "margin-right:5px;")

        current_date = QDate.currentDate()
        self.date_edit_from = CustomDateEdit(self.widget_2datepicker)
        self.date_edit_from.setCalendarPopup(True)
        self.date_edit_from.setDate(current_date)
        self.date_edit_from.setObjectName("from")
        self.date_edit_from.setMinimumSize(QtCore.QSize(0, 30))
        self.date_edit_from.setMaximumSize(QtCore.QSize(150, 30))
        self.date_edit_from.setStyleSheet("#from {border : 1px solid #D8D5D4;\n"
                                          "padding-left:5px;"
                                          "border-radius :5px;\n"
                                          "color:#555555;\n"
                                          "text-align: center;"
                                          "font-size:13px;\n"
                                          "}\n"
                                          "#from::drop-down{\n"
                                          "background-color:#D8D5D4;"
                                          " image:url(images/calendar_icon.png);\n"
                                          "width: 20px;\n"
                                          "height: 20px;\n"
                                          "padding:5px;"
                                          "}\n"
                                          )

        self.label_to = QtWidgets.QLabel(" To", self.widget_2datepicker)
        self.label_to.setAlignment(Qt.AlignCenter)
        font_metrics = QFontMetrics(self.label_to.font())
        # Get the width of the text
        text_width = font_metrics.width(self.label_to.text()) + 20
        self.label_to.setFixedSize(text_width, 30)
        self.label_to.setStyleSheet(
            "font-size: 12px;\n"
            "color: #5C5C5C;\n"
            "font-weight: 400;"
            "margin-right:5px;")
        self.date_edit_to = CustomDateEdit(self.widget_2datepicker)
        self.date_edit_to.setCalendarPopup(True)
        self.date_edit_to.setDate(current_date)
        self.date_edit_to.setMinimumSize(QtCore.QSize(0, 30))
        self.date_edit_to.setMaximumSize(QtCore.QSize(150, 30))
        self.date_edit_to.setObjectName("to")
        self.date_edit_to.setStyleSheet("#to {border : 1px solid #D8D5D4;\n"
                                        "padding-left:5px;"
                                        "border-radius :5px;\n"
                                        "color:#555555;\n"
                                        "text-align: center;"
                                        "font-size:13px;\n"
                                        "}\n"
                                        "#to::drop-down{\n"
                                        "background-color:#D8D5D4;"
                                        " image:url(images/calendar_icon.png);\n"
                                        "width: 20px;\n"
                                        "height: 20px;\n"
                                        "padding:5px;"
                                        "}\n"
                                        )
        # Access the QCalendarWidget and set its size
        calendar_widget = self.date_edit_to.calendarWidget()
        calendar_widget.resize(150, 200)

        self.hidden_widget1 = QtWidgets.QWidget(self.widget_2datepicker)
        self.hori_for_date.addWidget(self.label_312)
        self.hori_for_date.addWidget(self.date_edit_from)

        self.hori_for_date.addWidget(self.label_to)
        self.hori_for_date.addWidget(self.date_edit_to)
        self.hori_for_date.addWidget(self.hidden_widget1)

        self.verticalLayout_51.addWidget(self.label_31)
        self.verticalLayout_51.addWidget(self.widget_2datepicker)
        self.verticalLayout_4.addWidget(self.date_picker_widg)

        self.prepared_widg = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_511 = QtWidgets.QVBoxLayout(self.prepared_widg)
        self.verticalLayout_511.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_511.setSpacing(0)
        self.verticalLayout_511.setObjectName("verticalLayout_5")
        self.label_311 = QtWidgets.QLabel("  Prepared By:", self.prepared_widg)
        self.label_311.setMinimumSize(QtCore.QSize(0, 40))
        self.label_311.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_311.setStyleSheet("#label_3{\n"
                                     "font-size: 18px;\n"
                                     "color: rgba(111, 75, 39, 0.77);\n"
                                     "font-weight: bold;}")
        self.label_311.setObjectName("label_3")
        self.prepared_by = QtWidgets.QLineEdit(self.prepared_widg)
        self.prepared_by.setPlaceholderText("Type your name here")
        self.prepared_by.setMinimumSize(QtCore.QSize(300, 30))
        self.prepared_by.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.prepared_by.setFont(font)
        self.prepared_by.setStyleSheet("        border-radius: 5px;\n"
                                       "        font-size: 12px;\n"
                                       "        font-family: Arial;\n"
                                       "margin-left:10px;"
                                       "padding-left:5px;"
                                       "font-weight:400;"
                                       "        color:rgb(144, 115, 87);"
                                       "        background-color: #fff;\n"
                                       "        border: 1px solid #aaa;\n")
        self.verticalLayout_51.addWidget(self.label_311)
        self.verticalLayout_51.addWidget(self.prepared_by)
        self.verticalLayout_4.addWidget(self.prepared_widg)

        self.hidden_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.hidden_widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_41.addWidget(self.scrollArea)
        self.scrollAreanew.setWidget(self.scrollAreaWidgetContentsnew)
        self.horizontalLayout_4.addWidget(self.scrollAreanew)

        self.horizontalLayout_3.addWidget(self.widget_4)

        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(160, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(160, 16777215))
        self.widget_5.setStyleSheet("background-color: rgba(76,146,215,255);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 210))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 210))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/icons8-print-96.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.print_btn = QtWidgets.QPushButton("Print", self.widget_7)
        self.print_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.print_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.print_btn.setStyleSheet("#print_btn{\n"
                                     "background: white;\n"
                                     "font-weight:bold;\n"
                                     "color: #2E74A9;\n"
                                     "border-radius: 15px;\n"
                                     "font-family: Inter;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "#print_btn::hover{\n"
                                     "color: #2E74A9;\n"
                                     "border : 3px solid  #2E74A9;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.print_btn.setObjectName("print_btn")
        self.print_btn.clicked.connect(self.printer)
        self.verticalLayout_3.addWidget(self.print_btn)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2.addWidget(self.widget_6)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def printer(self):
        selected_date_from = self.date_edit_from.date()
        selected_date_to = self.date_edit_to.date()
        pre_by = self.prepared_by.text()

        date_text_to = selected_date_to.toString("yyyy-MM-dd")
        date_text_from = selected_date_from.toString("yyyy-MM-dd")

        date_text_to_f = selected_date_to.toString("MM/dd/yyyy")
        date_text_from_f = selected_date_from.toString("MM/dd/yyyy")

        checked_folders = [folders.text() for folders in self.checkbox_list if folders.isChecked()]
        checked_i_e = [i_e.text() for i_e in self.non_crack_chb_list if i_e.isChecked()]
        checked_loc = [loc.text() for loc in self.crack_loc_chb_list if loc.isChecked()]

        mapping = {
            'Images without Detected Cracks': 'No Detected Crack',
            'Images with Detected Cracks': 'Contains Crack'
        }

        # Map the values in checked_i_e list using the mapping dictionary
        mapped_i_e = [mapping.get(value, value) for value in checked_i_e]
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            db_path = os.path.join(dir_path, 'Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Create a comma-separated string of the folder names
            folders_string = ','.join(["'{}'".format(f) for f in checked_folders])
            i_e_string = ','.join(["'{}'".format(f) for f in mapped_i_e])
            loc_string = ','.join(["'{}'".format(f) for f in checked_loc])

            if len(checked_folders) == 0:
                icon_image = "images/warning.png"
                message = "Please choose a folder."
                self.QMessage_Error_dialog(message, icon_image)
            # Check if mapped_i_e is empty
            elif len(mapped_i_e) == 0:
                icon_image = "images/warning.png"
                message = "Choose between crack Inclusion and Exclusion."
                self.QMessage_Error_dialog(message, icon_image)
            # Check if checked_loc is empty
            elif len(checked_loc) == 0:
                icon_image = "images/warning.png"
                message = "Choose the location of a crack."
                self.QMessage_Error_dialog(message, icon_image)
            elif len(pre_by.strip()) == 0:
                icon_image = "images/warning.png"
                message = "Please input your name."
                self.QMessage_Error_dialog(message, icon_image)
            else:
                query = f"SELECT * FROM Save_Files WHERE folder_name IN ({folders_string}) AND Status IN ({i_e_string}) AND selected_loc IN ({loc_string}) AND created_at BETWEEN '{date_text_from} 00:00:00' AND '{date_text_to} 23:59:59' ORDER BY created_at DESC"
                c.execute(query)
                rows = c.fetchall()

                if not rows:
                    icon_image = "images/warning.png"
                    message = "Folder is empty or your selected category is not in the folder."
                    self.QMessage_Error_dialog(message, icon_image)
                else:

                    try:
                        printer = QPrinter()
                        printer.setPageSize(QPrinter.Letter)
                        printer.setOrientation(QPrinter.Landscape)
                        printer.setOutputFormat(QPrinter.PdfFormat)
                        printer.setOutputFileName("preview.pdf")

                        # create a QTextDocument to hold the text to be printed
                        doc = QTextDocument()
                        doc.setPageSize(QSizeF(printer.pageRect().size()))  # set page size to match printer's page rect
                        doc.setDocumentMargin(50)

                        if len(checked_loc) == 1:
                            locc = checked_loc[0].strip("''")
                        elif len(checked_loc) == 2:
                            locc = f"{checked_loc[:-1][0].strip('[]')} <span style='color: #555555;'> and </span> {checked_loc[-1]}"
                        else:
                            locc = f"{', '.join(checked_loc[:-1])}<span style='color: #555555;'>, and </span>{checked_loc[-1]}"

                        if len(checked_folders) == 1:
                            fold = checked_folders[0].strip("''")
                        elif len(checked_folders) == 2:
                            fold = f"{checked_folders[:-1][0].strip('[]')} <span style='color: #555555;'> and </span> {checked_folders[-1]}"
                        else:
                            fold = f"{', '.join(checked_folders[:-1])}<span style='color: #555555;'>, and </span>{checked_folders[-1]}"

                        if len(checked_i_e) == 1:
                            i_e = checked_i_e[0].strip("''")
                        else:
                            i_e = f"{checked_i_e[:-1][0].strip('[]')} <span style='color: #555555;'> and </span> {checked_i_e[-1]}"

                        # create the table HTML including the specified columns
                        table_html = f''' <h2 style="text-align: center; color: #543F24; font-family: Inter; font-weight: bold; font-size: 54px;"> <img src="images/Crackterize_doc.png" 
                        alt="Your Image" style="width: 50px; height: 30px;"> </h2> 
                        
                        <h3 style="text-align: center;font-weight: bold;font-family: Inter; margin-left:10px;margin-right:10px; color: #555555; font-family: Inter;"> 
                        
                         <p style="  font-weight: bold; font-size: 102px;font-family: Inter;" ><b>Summary of Crack Assessment Reports for <span style="color: #907458;">{
                        self.proj_name}</span> project,<br>
                            located in the <span style="color: #907458;">{fold}</span> folder/s,<br>
                            provides an evaluation of <span style="color: #907458;">{i_e}</span><br>
                            at <span style="color: #907458;">{locc}</span><br>
                            from <span style="color: #907458;">{date_text_from_f}</span> to <span style="color: #907458;">{date_text_to_f}</span>.
                            <br></b></p>
                         </h3> 
                        
                        <table border="1" cellpadding="5" style="border-collapse: collapse;">
                            <tr>
                                <th>Project Name</th>
                                <th>Folder Name</th>
                                <th>Assessment</th>
                                <th>Length</th>
                                <th>Width</th>
                                <th>Positive Crack Probability</th>
                                <th>Negative Crack Probability</th>
                                <th>Location</th>
                                <th>Time & Date</th>
                                <th>Remarks</th>
                                <th>Prepared By:</th>
                            </tr>
                        '''
                        # loop through the fetched data and add each row to the table
                        for row in rows:
                            date_obj = datetime.strptime(row[14], '%Y-%m-%d %H:%M:%S')
                            formatted_date = date_obj.strftime('%I:%M%p · %m/%d/%Y')
                            # add a row to the table with the row data
                            row_html = f'''
                                <tr>
                                    <td style="text-align: center;">{row[16]}</td>
                                    <td style="text-align: center;">{row[1]}</td>
                                    <td style="text-align: center;">{row[9]}</td>
                                    <td style="text-align: center;">{row[5]}</td>
                                    <td style="text-align: center;">{row[4]}</td>
                                    <td style="text-align: center;">{row[8]}</td>
                                    <td style="text-align: center;">{row[7]}</td>
                                    <td style="text-align: center;">{row[10]}</td>
                                    <td style="text-align: center;">{formatted_date}</td>
                                    <td style="text-align: center;">{row[13]}</td>
                                    <td style="text-align: center;">{row[6]}</td>
                                </tr>
                            '''
                            table_html += row_html
                        timestamp = datetime.now()
                        # Format the timestamp string
                        hour = timestamp.strftime('%I')
                        minute = timestamp.strftime('%M')
                        period = timestamp.strftime('%p').lower()
                        month = timestamp.strftime('%m')
                        day = timestamp.strftime('%d')
                        year = timestamp.strftime('%Y')
                        timestamp_str = f"{hour}:{minute}{period} · {month}/{day}/{year}"
                        footer_html = f'''
                                <table width = "100%" position = "fixed" bottom = "0" "cellpadding="5" style="border-collapse: collapse;" >
                                    <tr>
                                        <td style="text-align: left; font-size: 18px; color: #3F2A15;"><b>Prepared By:</b> {pre_by} </td>
                                        <td style="text-align: right; font-size: 18px; color: #3F2A15;">{timestamp_str}</td> </tr> </table> 
                        '''

                        cursor = QTextCursor(doc)
                        # close the table HTML
                        table_html += '</table>'
                        doc.setHtml(table_html)
                        cursor.insertHtml(footer_html)
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

        except Exception as e:
            print(e)

    def project_chosen(self):
        self.folders_widget.show()
        radio_project = self.project_chb.sender()
        if radio_project.isChecked():
            project_name = radio_project.text()
            print("Selected project:", radio_project.text())
            try:
                dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                db_path = os.path.join(dir_path, 'Projects.db')
                # Create a connection to a SQLite database or create it if it doesn't exist
                self.conn = sqlite3.connect(db_path)
                self.c = self.conn.cursor()
                self.c.execute("SELECT * FROM Location_Folder WHERE project_name = ?", (project_name,))
                rows = self.c.fetchall()
                row_count = 0
                col_count = 0
                for checkbox in self.checkbox_list:
                    checkbox.setChecked(False)
                    checkbox.setParent(None)
                    checkbox.deleteLater()

                self.checkbox_list = []
                for row in rows:
                    folder_name = str(row[2])
                    # Create a checkbox for each project and set its properties
                    folder_chb = QtWidgets.QCheckBox(self.widget_fo)
                    font_metrics = QFontMetrics(folder_chb.font())
                    # Get the width of the text
                    text_width = font_metrics.width(folder_chb.text())
                    folder_chb.setMinimumSize(QtCore.QSize(text_width, 30))
                    folder_chb.setStyleSheet("#folder_name {border : 1px solid rgba(76,146,215,255);\n"
                                             "border-radius :15px;\n"
                                             "color:black;\n"
                                             "    text-align: center;"
                                             "font-size:13px;\n"
                                             "padding-right:10px;"
                                             "}\n"
                                             "#folder_name::indicator{border : 2px solid rgba(76,146,215,255);\n"
                                             "width : 16px;\n"
                                             "height : 16px;\n"
                                             "border-radius :10px;\n"
                                             "margin-left:5px;}\n"
                                             "#folder_name::indicator:checked {\n"
                                             "image: url(images/checkbox.png);\n"
                                             "}\n"
                                             "")
                    folder_chb.setTristate(False)
                    folder_chb.setObjectName("folder_name")
                    folder_chb.setText(folder_name)
                    folder_chb.clicked.connect(self.folder_list_select)
                    self.checkbox_list.append(folder_chb)

                    # Add the checkbox to the layout
                    self.verticalLayout_12.addWidget(folder_chb, row_count, col_count)
                    col_count += 1
                    if col_count == 3:  # Maximum number of columns
                        col_count = 0
                        row_count += 1
            except Exception as e:
                print(e)

    def QMessage_Error_dialog(self, message, icon_image):
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

    def folder_list_select(self):
        self.non_crack_widget.show()
        checked_folders = [folders.text() for folders in self.checkbox_list if folders.isChecked()]
        print("Checked checkboxes:", checked_folders)

    def show_chb_loc(self):
        self.crack_loc_widget.show()

    def mark_all_checkboxes_folder(self):
        self.non_crack_widget.show()
        for checkbox in self.checkbox_list:
            checkbox.setChecked(True)

    def clear_all_checkboxes_folder(self):
        self.crack_loc_widget.hide()
        self.non_crack_widget.hide()
        for checkbox in self.checkbox_list:
            checkbox.setChecked(False)
            checked_checkboxes = [checkbox.text() for checkbox in self.checkbox_list if checkbox.isChecked()]
            print("Checked checkboxes:", checked_checkboxes)

    def mark_all_checkboxes_crack_i_e(self):
        self.crack_loc_widget.show()
        for checkbox in self.non_crack_chb_list:
            checkbox.setChecked(True)
            checked_checkboxes = [checkbox.text() for checkbox in self.non_crack_chb_list if checkbox.isChecked()]
            print("Checked checkboxes:", checked_checkboxes)

    def clear_all_checkboxes_crack_i_e(self):
        for checkbox in self.non_crack_chb_list:
            checkbox.setChecked(False)

    def mark_all_checkboxes_loc(self):
        for checkbox in self.crack_loc_chb_list:
            checkbox.setChecked(True)
            checked_checkboxes = [checkbox.text() for checkbox in self.crack_loc_chb_list if checkbox.isChecked()]
            print("Checked checkboxes:", checked_checkboxes)

    def clear_all_checkboxes_loc(self):
        for checkbox in self.crack_loc_chb_list:
            checkbox.setChecked(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = filter_print(None)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
