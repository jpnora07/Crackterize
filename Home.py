import os
import sqlite3
import torch

import cv2
import numpy as np

import tensorflow as tf
from tensorflow import keras
from keras.applications.resnet import ResNet50, preprocess_input, decode_predictions

import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QMouseEvent, QMovie, QPixmap
from PyQt5.QtWidgets import QListView, QComboBox, QDialog, QFileDialog, QStyledItemDelegate, QScrollBar, \
    QAbstractItemView, QLineEdit, QFrame, QPushButton

from Detect_Crack import Detect_Crack_Dialog
from Segment_Image import Ui_DialogSegment
from calculatorButtons import cal_dialog
from view_result_with_details import result_with_details
from result import Result_Dialog
from view_folders import view_folder_dialog


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

    def paint(self, painter, option, index):
        super().paint(painter, option, index)


class Ui_MainWindow(object):
    class QTComboBoxButton(QLineEdit):
        def __init__(self, combo):
            super().__init__(combo)

        def mousePressEvent(self, e: QMouseEvent) -> None:
            combo = self.parent()
            if isinstance(combo, QComboBox):
                combo.showPopup()

    def setupUi(self, MainWindow):
        self.Mainwindow = MainWindow
        MainWindow.setObjectName("Crackterize")
        # Set the logo using an QIcon object
        logo = QIcon('images/main_icon.png')
        MainWindow.setWindowIcon(logo)
        MainWindow.setWindowModality(QtCore.Qt.NonModal)#
        MainWindow.setEnabled(True)
        # MainWindow.setFixedSize(1000, 700)

        # MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("#Crackterize{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "width: fit-content;\n"
                                 "heigth: fit-content;\n"
                                 "block-size: fit-content;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                         "width: fit-content;\n"
                                         "heigth: fit-content;\n"
                                         "block-size: fit-content;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("width: fit-content;\n"
                                  "block-size: fit-content;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)

        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.threeBtn = QtWidgets.QWidget(self.widget_2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeBtn.sizePolicy().hasHeightForWidth())
        self.threeBtn.setSizePolicy(sizePolicy)

        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setColor(QtGui.QColor(144, 115, 87, 100))
        effect.setOffset(QtCore.QPointF(0, 4))
        self.threeBtn.setGraphicsEffect(effect)
        self.threeBtn.setMinimumSize(QtCore.QSize(800, 0))
        self.threeBtn.setMaximumSize(QtCore.QSize(800, 60))
        self.threeBtn.setStyleSheet("#threeBtn{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px;\n"
                                    "}\n"
                                    "")
        self.threeBtn.setObjectName("threeBtn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.threeBtn)
        self.horizontalLayout.setContentsMargins(100, 15, 100, 15)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.myProjects = QtWidgets.QComboBox(self.threeBtn)
        self.myProjects.setMinimumSize(QtCore.QSize(25, 0))
        self.myProjects.setMaximumSize(QtCore.QSize(150, 16777215))
        self.myProjects.setGeometry(115, 90, 100, 30)
        self.myProjects.setLineEdit(self.QTComboBoxButton(self.myProjects))
        self.projects_icon = QtWidgets.QLabel(self.threeBtn)
        self.projects_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.projects_icon.setGeometry(70, 15, 40, 70)
        self.projects_icon.setStyleSheet("\n"
                                    "background: transparent;")
        #howto_icon = QtGui.QIcon()
        # howto_icon.addPixmap(QtGui.QPixmap("images/howtouse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        myprojects_icon = QPixmap("images/foler.png")
        scaled_pixmap = myprojects_icon.scaled(18, 18)
        self.projects_icon.setPixmap(scaled_pixmap)
        self.projects_icon.setObjectName("projects_icon")
        self.ledit = self.myProjects.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, 'Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT * FROM Projects ORDER BY created_at DESC")
            rows = c.fetchall()
            for row in rows:
                self.myProjects.addItem(str(row[1]))
        except Exception as e:
            print("Empty Projects! Users not yet add projects: ", e)
        self.myProjects.setEditText("My Projects")


        def handleSelection(text):
            # change back to default title after item is selected

            self.myProjects.setEditText("My Projects")
            with open('selected_project.txt', 'w') as f:
                f.write(text)
            try:
                self.background_widget.show()
                folder_dialog = QtWidgets.QDialog(self.Mainwindow)
                ui = view_folder_dialog(self.background_widget, self.history, self.myProjects, self.Mainwindow)
                ui.setupUi(folder_dialog)
                x = (self.Mainwindow.width() - folder_dialog.width()) // 2
                y = (self.Mainwindow.height() - folder_dialog.height()) // 2
                folder_dialog.move(x, y)
                folder_dialog.exec_()
            except Exception as e:
                print(e)

        self.myProjects.activated[str].connect(handleSelection)

        # change the background of list in combo box and its corner
        self.myProjects.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.myProjects.view().window().setAttribute(Qt.WA_TranslucentBackground)
        view = QListView()
        view.setWordWrap(True)

        # border - top - left - radius: {0}px;
        # border - top - right - radius: {0}px;
        view.setStyleSheet(
            """
    QListView{
            background-color :rgba(255, 255, 255, 0.75);
            border-bottom-left-radius:20px;
            border-bottom-right-radius:20px;
            }
    QScrollBar:vertical
    {
        background-color: #c3c3c3;
        width: 15px;
        margin: 15px 3px 15px 3px;
        border: 1px transparent #2A2929;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical
    {
        background-color: #8c8c8c;         /* #605F5F; */
        min-height: 5px;
        border-radius: 4px;
    }

    QScrollBar::sub-line:vertical
    {
        margin: 3px 0px 3px 0px;
        border-image: url(:/images/up_arrow_disabled.png);        /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical
    {
        margin: 3px 0px 3px 0px;
        border-image: url(:/images/down_arrow_disabled.png);       /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
    {
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
    {
        background: none;
    }
            """
        )


        scroll_bar = QScrollBar()
        view.setVerticalScrollBar(scroll_bar)
        self.myProjects.setView(view)
        self.myProjects.view().parentWidget().setStyleSheet('border: none;')

        # set the minimum data list and set the scrollbar
        self.myProjects.setMaxVisibleItems(5)
        self.myProjects.setMaxCount(100)
        # Set the size adjust policy to adjust to contents
        self.myProjects.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        # Set the vertical scrolling mode to ScrollPerPixel for smooth scrolling
        self.myProjects.view().setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        # Show the vertical scrollbar
        self.myProjects.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.myProjects.setStyleSheet("#myProjects {\n"
                                      "border-radius:14px;\n"
                                      "font: 600 12pt \"Segoe UI\";\n"
                                      "color:#4A3B28;\n"
                                      "border: none;"
                                      "text-align: center;\n"
                                      "}\n"
                                      "#myProjects::drop-down{\n"
                                      "image:url(images/arrowdown.png);\n"
                                      "background-position: -10px -10px;"
                                      "width: 20px;\n"
                                      "height: 20px;\n"
                                      "text-align: center;\n"
                                      "}\n"
                                      "#myProjects::drop-down::pressed{\n"
                                      "image:url(images/arrowup.png);\n"
                                      "width: 20px;\n"
                                      "height: 20px;\n"
                                      "text-align: center;\n"
                                      "}\n"
                                      "#myProjects QAbstractItemView {\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "outline: none;"
                                      "text-align: center;\n"
                                      "}\n"
                                      "#myProjects QAbstractItemView::item {\n"
                                      "background-color: #F4EBE6;\n"
                                      "color: #4A3B28;\n"
                                      "text-align: center;\n"
                                      "min-height: 35px; min-width: 50px;"
                                      "border:0px;"
                                      "}\n"
                                      "#myProjects QListView{"
                                      "border: none;"
                                      "font-weight:bold;"
                                      "text-align: center;\n"
                                      "}"
                                      "#myProjects QListView::item{"
                                      "border:0px;"
                                      "border-radius: 15px;"
                                      "padding:8px; "
                                      "margin:10px;"
                                      "}"
                                      "#myProjects QListView::item:selected { "
                                      "color: white; "
                                      "background-color: #4A3B28}\n"
                                      "#myProjects::-webkit-scrollbar {\n"
                                      "width: 10px;\n"
                                      "height: 10px;\n"
                                      "}\n")

        self.myProjects.setIconSize(QtCore.QSize(21, 21))
        self.myProjects.setObjectName("myProjects")
        self.horizontalLayout.addWidget(self.myProjects)

        self.history = QtWidgets.QComboBox(self.threeBtn)
        self.history.view().parentWidget().setStyleSheet('border: none;')
        self.history.setGeometry(300, 150, 150, 30)
        self.history.setEditable(True)
        self.history.setMaximumSize(800, 16777215)
        self.history.setLineEdit(self.QTComboBoxButton(self.history))
        self.history_icon = QtWidgets.QLabel(self.threeBtn)
        self.history_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.history_icon.setGeometry(300, 15, 40, 70)
        self.history_icon.setStyleSheet("\n"
                                         "background: transparent;")
        #history_icon = QtGui.QIcon()
        # howto_icon.addPixmap(QtGui.QPixmap("images/howtouse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        history_icon = QPixmap("images/history_icon.png")
        scaled_pixmap = history_icon.scaled(22, 22)
        self.history_icon.setPixmap(scaled_pixmap)
        self.history_icon.setObjectName("history_icon")
        self.ledit = self.history.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, 'Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT * FROM Save_Files ORDER BY created_at DESC")
            rows = c.fetchall()
            for row in rows:
                status = str(row[9])
                recent = str(row[14])
                id = str(row[0])
                self.history.addItem(status + " - " + recent, id)  # add id as user data
        except Exception as e:
            print("Empty History! Users not yet add results: ", e)
        self.history.setEditText("History")

        def handleSelection(text):
            # change back to default title after item is selected
            self.history.setEditText("History")
            # get the id of the selected item
            index = self.history.currentIndex()
            id = self.history.itemData(index)
            print("Selected id:", id)
            with open('image_id.txt', 'w') as f:
                f.write(id)
            try:
                self.background_widget.show()
                folder_dialog = QtWidgets.QDialog(self.Mainwindow)
                ui = result_with_details(self.background_widget, self.history)
                ui.setupUi(folder_dialog)
                x = (self.Mainwindow.width() - folder_dialog.width()) // 2
                y = (self.Mainwindow.height() - folder_dialog.height()) // 2
                folder_dialog.move(x, y)
                folder_dialog.exec_()
            except Exception as e:
                print(e)

        # connect the activated signal with handleSelection
        self.history.activated[str].connect(handleSelection)
        # Disable showing the selected item in the title
        # change the background of list in combo box and its corner
        self.history.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.history.view().window().setAttribute(Qt.WA_TranslucentBackground)
        view = QListView()
        view.setWordWrap(True)
        radius = 20

        # border - top - left - radius: {0}px;
        # border - top - right - radius: {0}px;
        view.setStyleSheet(
            """
    QListView{
            background-color :rgba(255, 255, 255, 0.75);
            border-bottom-left-radius:20px;
            border-bottom-right-radius:20px;
            }
    QScrollBar:vertical
    {
        background-color: #c3c3c3;
        width: 15px;
        margin: 15px 3px 15px 3px;
        border: 1px transparent #2A2929;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical
    {
        background-color: #8c8c8c;         /* #605F5F; */
        min-height: 5px;
        border-radius: 4px;
    }

    QScrollBar::sub-line:vertical
    {margin: 3px 0px 3px 0px;border-image: url(:/images/up_arrow_disabled.png);height: 10px;width: 10px;subcontrol-position: top;subcontrol-origin: margin;}

    QScrollBar::add-line:vertical
    {
        margin: 3px 0px 3px 0px;
        border-image: url(:/images/down_arrow_disabled.png);       /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{background: none;}

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background: none;
    }
            """
        )
        scroll_bar = QScrollBar()
        view.setVerticalScrollBar(scroll_bar)
        self.history.setView(view)
        self.history.view().parentWidget().setStyleSheet('border: none;')

        # set the minimum data list and set the scrollbar
        self.history.setMaxVisibleItems(5)
        self.history.setMaxCount(100)
        # Set the size adjust policy to adjust to contents
        self.history.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        # Set the vertical scrolling mode to ScrollPerPixel for smooth scrolling
        self.history.view().setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        # Show the vertical scrollbar
        self.history.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.history.setStyleSheet("#history{\n"
                                   "padding-left: 10px;\n"
                                   "border-radius:4px;\n"
                                   "font: 600 12pt \"Segoe UI\";\n"
                                   "color:#4A3B28;\n"
                                   "background: transparent;\n"
                                   "border:0px;"
                                   "text-align: center;\n"
                                   "}\n"

                                   "#history::drop-down{\n"
                                   "image:url(images/arrowdown.png);\n"
                                   "width: 20px;\n"
                                   "height: 20px;\n"
                                   "text-align: bottom;\n"
                                   "}\n"

                                   "#history::drop-down::pressed{\n"
                                   "image:url(images/arrowup.png);\n"
                                   "width: 20px;\n"
                                   "height: 20px;\n"
                                   "text-align: center;\n"
                                   "}\n"

                                   "#history QAbstractItemView {\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "outline: none;"
                                   "text-align: center;\n"

                                   "border:0px;"
                                   "\n"
                                   "}\n"

                                   "#history QAbstractItemView::item {\n"
                                   "background-color: #F4EBE6;\n"
                                   "color: #4A3B28;\n"
                                   "text-align: center;\n"
                                   "min-height: 35px; min-width: 50px;"
                                   "border:0px;"
                                   "}\n"

                                   "#history QListView{"
                                   "border:0px;"
                                   # "color:rgb(87, 96, 134);"
                                   # "background-color:rgb(255, 255, 255);"
                                   "font-weight:bold;"
                                   # "selection-background-color: rgb(47, 175, 178);"
                                   # "show-decoration-selected: 1;"
                                   "text-align: center;\n"
                                   "}"

                                   "#history QListView::item{"
                                   "border:0px;"
                                   "border-radius: 15px;"
                                   "padding:8px; "
                                   "margin:10px;"
                                   "text-align: center;\n"
                                   "}"

                                   "#history QListView::item:selected { "
                                   "color: white; "
                                   "background-color: #4A3B28}")
        self.history.setObjectName("history")
        self.horizontalLayout.addWidget(self.history)

        self.how_widget = QtWidgets.QWidget(self.threeBtn)
        self.how_widget.setGeometry(QtCore.QRect(115, 200, 500, 31))
        self.how_widget.setObjectName("how_widget")
        self.horizontalLayout11 = QtWidgets.QHBoxLayout(self.how_widget)
        self.horizontalLayout11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout11.setSpacing(0)
        self.horizontalLayout11.setObjectName("horizontalLayout")
        self.how_btn2 = QPushButton("Help and Info", self.how_widget)
        pixmap = QPixmap('images/howtouse_icon.png')
        icon_size = QSize(20, 20)
        pixmap_padded = pixmap.scaled(icon_size.width() + 100, icon_size.height(), Qt.KeepAspectRatio,
                                      Qt.SmoothTransformation)
        icon = QIcon(pixmap_padded)
        self.how_btn2.setIcon(icon)
        self.how_btn2.setStyleSheet("font: 600 12pt \"Segoe UI\";\n"
                                    "color:#4A3B28;\n"
                                    "background: transparent;\n"
                                    "padding-left: 10px;")
        self.how_btn2.setIconSize(icon_size)
        self.how_btn2.setFlat(True)
        self.how_btn2.setObjectName("how_btn2")
        self.how_btn2.clicked.connect(self.how_and_help)
        self.horizontalLayout11.addWidget(self.how_btn2)
        self.how_btn = QtWidgets.QPushButton(self.how_widget)
        self.how_btn.setMaximumSize(QtCore.QSize(20, 167))
        self.how_btn.setStyleSheet("\n"
                                   "background: transparent;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/arrowdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.how_btn.setIcon(icon)
        self.how_btn.setIconSize(QtCore.QSize(21, 21))
        self.how_btn.setFlat(True)
        self.how_btn.setObjectName("how_btn")
        self.how_btn.clicked.connect(self.how_and_help)
        self.horizontalLayout11.addWidget(self.how_btn)


        self.horizontalLayout.addWidget(self.how_widget)

        self.verticalLayout_3.addWidget(self.threeBtn)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setMaximumSize(QtCore.QSize(820, 250))
        self.widget_6.setStyleSheet("border-image:url(images/Crackterize.png) 400 0 300 0 stretch;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")

        # new
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(100, 20, 100, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.widget_5 = QtWidgets.QWidget(self.widget_4)

        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setColor(QtGui.QColor(144, 115, 87, 100))
        effect.setOffset(QtCore.QPointF(0, 4))
        self.widget_5.setGraphicsEffect(effect)
        self.widget_5.setMaximumSize(QtCore.QSize(800, 170))
        self.widget_5.setStyleSheet("#widget_5{\n"
                                    "background-color: #cfcec9;\n"
                                    "border-radius:28px;\n"
                                    "}")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widgetUpload = QtWidgets.QWidget(self.widget_5)
        self.widgetUpload.setMinimumSize(QtCore.QSize(550, 0))
        self.widgetUpload.setMaximumSize(QtCore.QSize(550, 170))
        self.widgetUpload.setStyleSheet("#widgetUpload{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius:28px;\n"
                                        "}\n"
                                        "        \n"
                                        "")
        self.widgetUpload.setObjectName("widgetUpload")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widgetUpload)
        self.verticalLayout_5.setContentsMargins(50, 30, 50, 30)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uploadImg = QtWidgets.QPushButton("  Upload Image", self.widgetUpload)
        self.uploadImg.clicked.connect(self.upload_image)
        self.uploadImg.setIcon(QIcon('images/uploadIcon.png'))
        self.uploadImg.setIconSize(QSize(17, 17))
        self.uploadImg.setStyleSheet("#uploadImg{\n"
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
                                     "#uploadImg:hover{\n"
                                     "color:rgb(144, 115, 87);\n"
                                     "border :2px solid rgb(144, 115, 87);\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "")
        self.uploadImg.setObjectName("uploadImg")
        self.verticalLayout_5.addWidget(self.uploadImg)
        self.create = QtWidgets.QPushButton("or create a new project", self.widgetUpload)
        self.create.clicked.connect(self.creating_new_project)
        self.create.setStyleSheet("#create{\n"
                                  "font-weight:bold;\n"
                                  " color:#363131;\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border :3px solid rgb(255, 255, 255);\n"
                                  " }\n"
                                  "#create:hover{\n"
                                  "background-color:rgb(255, 255, 255);}\n"
                                  "")
        self.create.setObjectName("create")
        self.verticalLayout_5.addWidget(self.create)
        self.horizontalLayout_4.addWidget(self.widgetUpload)
        self.widgetUpload_2 = QtWidgets.QWidget(self.widget_5)
        self.widgetUpload_2.setStyleSheet("#widgetUpload{\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius:28px;\n"
                                          "}\n"
                                          "        \n"
                                          "")
        self.widgetUpload_2.setObjectName("widgetUpload_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widgetUpload_2)
        self.verticalLayout_6.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.calLbl = QtWidgets.QPushButton("Concrete Calculator", self.widgetUpload_2)
        self.calLbl.setStyleSheet("#calLbl{\n"
                                  "font-weight:bold;\n"
                                  " color:#363131;\n"
                                  "background-color: #cfcec9;\n"
                                  "border :3px solid #cfcec9;\n"
                                  " }\n"
                                  "#calLbl:hover{\n"
                                  "background-color:#cfcec9;}\n"
                                  "")
        self.calLbl.setObjectName("calLbl")
        self.verticalLayout_6.addWidget(self.calLbl)
        self.ButtonCal = QtWidgets.QPushButton("Calculator", self.widgetUpload_2)
        self.ButtonCal.setStyleSheet("#ButtonCal{\n"
                                     "height:40px;\n"
                                     "font-weight:bold;\n"
                                     "font-size:18px;\n"
                                     "color:white;\n"
                                     "background-color: #818181;\n"
                                     "border-top-left-radius :20px;\n"
                                     "border-top-right-radius : 20px; \n"
                                     "border-bottom-left-radius : 20px; \n"
                                     "border-bottom-right-radius : 20px;\n"
                                     "}\n"
                                     "#ButtonCal:hover{\n"
                                     "color:#818181;\n"
                                     "border :2px solid #818181;\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "")
        self.ButtonCal.setObjectName("ButtonCal")

        self.ButtonCal.clicked.connect(self.ButtonCal_function)
        self.verticalLayout_6.addWidget(self.ButtonCal)
        self.horizontalLayout_4.addWidget(self.widgetUpload_2)

        self.horizontalLayout_3.addWidget(self.widget_5)
        # new

        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add transparent white background widget
        self.background_widget = QFrame(MainWindow)
        self.background_widget.setStyleSheet("background-color: rgba(0, 0, 0, 0.25);")
        self.background_widget.setMinimumSize(QtCore.QSize(1000, 700))
        self.background_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.background_widget.hide()

        self.Mainwindow.resizeEvent = lambda event: self.background_widget.resize(self.Mainwindow.size())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def how_and_help(self):
        try:
            Dialog = QDialog()
            Dialog.setObjectName("Dialog")
            Dialog.resize(645, 624)
            Dialog.setWindowFlags(Qt.FramelessWindowHint)
            self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
            self.verticalLayout.setObjectName("verticalLayout")
            self.widget = QtWidgets.QWidget(Dialog)
            self.widget.setObjectName("widget")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.scrollArea = QtWidgets.QScrollArea(self.widget)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollArea.setStyleSheet("#scrollArea {\n"
                                          "background-color: #F4EBE6;\n"
                                          "    border-top-left-radius: 10px;\n"
                                          "    border-bottom-left-radius: 10px;\n"
                                          "    border-top-right-radius: 10px;\n"
                                          "    border-bottom-right-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "#scrollArea QScrollBar:vertical {\n"
                                          "    background-color: #c3c3c3;\n"
                                          "    width: 15px;\n"
                                          "    margin: 15px 3px 15px 3px;\n"
                                          "    border: 1px transparent #2A2929;\n"
                                          "    border-radius: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "#scrollArea QScrollBar:vertical:hover {\n"
                                          "    width: 20px;\n"
                                          "}\n"
                                          "\n"
                                          "#scrollArea QScrollBar::handle:vertical {\n"
                                          "    background-color: #8c8c8c;\n"
                                          "    min-height: 5px;\n"
                                          "    border-radius: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "#scrollArea QScrollBar::sub-line:vertical {\n"
                                          "    margin: 3px 0px 3px 0px;\n"
                                          "    border-image: url(:/images/up_arrow_disabled.png);\n"
                                          "    height: 10px;\n"
                                          "    width: 10px;\n"
                                          "    subcontrol-position: top;\n"
                                          "    subcontrol-origin: margin;\n"
                                          "}\n"
                                          "\n"
                                          "#scrollArea QScrollBar::add-line:vertical {\n"
                                          "    margin: 3px 0px 3px 0px;\n"
                                          "    border-image: url(:/images/down_arrow_disabled.png);\n"
                                          "    height: 10px;\n"
                                          "    width: 10px;\n"
                                          "    subcontrol-position: bottom;\n"
                                          "    subcontrol-origin: margin;\n"
                                          "}\n"
                                          "\n"
                                          "#scrollArea QScrollBar::up-arrow:vertical,\n"
                                          "#scrollArea QScrollBar::down-arrow:vertical {\n"
                                          "    background: none;\n"
                                          "}\n"
                                          "\n"
                                          "#scrollArea QScrollBar::add-page:vertical,\n"
                                          "#scrollArea QScrollBar::sub-page:vertical {\n"
                                          "    background: none;\n"
                                          "}\n"
                                          "")
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -927, 612, 1673))
            self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(50, 35))
            self.scrollAreaWidgetContents.setStyleSheet("#scrollAreaWidgetContents{\n"
                                                        "background-color: transparent;\n"
                                                        "color: #4A3B28;\n"
                                                        "min-height: 35px; min-width: 50px;;\n"
                                                        "                    \n"
                                                        "}")
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.widget_4.setObjectName("widget_4")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
            self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
            self.verticalLayout_5.setSpacing(0)
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            self.label_2 = QtWidgets.QLabel(self.widget_4)
            font = QtGui.QFont()
            font.setFamily("Segoe UI Black")
            font.setPointSize(17)
            font.setBold(False)
            font.setItalic(False)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("#label_2{\n"
                                       "font: 150 17pt Segoe UI Black;\n"
                                       "alignment: center;\n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "                                 }")
            self.label_2.setObjectName("label_2")
            self.verticalLayout_5.addWidget(self.label_2)
            self.label_6 = QtWidgets.QLabel(self.widget_4)
            self.label_6.setText("<b>1.</b> Upload a single image file that you want to analyze by clicking the \"Upload Image\" button on the main menu of the application.<br><br>\n"
                                        "<b>2.</b> Adjust the threshold of the uploaded image by dragging the slider to highlight the cracks in the image.<br><br>\n"
                                        "<b>3.</b> Input the distance between the camera and the subject when the image was taken.<br><br>\n"
                                        "<b>4.</b> Click the \"Denoise Image\" button to remove any unnecessary noise from the image.<br><br>\n"
                                        "<b>5.</b> Click the \"Measure the Crack\" button to analyze the image and detect the measurements of the crack.<br><br>\n"
                                        "<b>6.</b> The results page will display on the screen, indicating whether the image contains cracks or not. If there are cracks found, the measurements of the crack will also be displayed.<br><br>\n"
                                        "<b>7.</b> Click the \"Add Details\" button to provide additional information about the crack, including the Location of Crack, Crack Type, Crack Progression and Remarks which may contain any notes you want to include.<br><br>\n"
                                        "<b>8.</b> Choose where to save the results by clicking the \"Save\" button.<br><br>\n"
                                        "<b>9.</b> If desired, click the \"Print\" button to print or save a PDF copy of the results.<br><br>\n"
                                        "<b>10.</b> That\'s it! With these simple steps, you can quickly and easily use CRACKTERIZE to detect cracks on concrete surfaces.")
            self.label_6.setStyleSheet("#label_6{\n"
                                       "font:  100 10pt \"Arial\";\n"
                                       "letter-spacing: 1px;\n"
                                       "line-height: 3.5px;\n"
                                       "color: #4A3B28;}")
            self.label_6.setScaledContents(False)
            self.label_6.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
            self.label_6.setWordWrap(True)
            self.label_6.setIndent(-1)
            self.label_6.setObjectName("label_6")
            self.label_6.setMargin(25)
            self.verticalLayout_5.addWidget(self.label_6)
            self.verticalLayout_3.addWidget(self.widget_4)
            self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.widget_7.setObjectName("widget_7")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
            self.verticalLayout_6.setContentsMargins(0, 0, 0, -1)
            self.verticalLayout_6.setSpacing(0)
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            self.label_3 = QtWidgets.QLabel(self.widget_7)
            self.label_3.setStyleSheet("#label_3{\n"
                                       "font: 150 17pt Segoe UI Black;\n"
                                       "alignment: center;\n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "                                 }")
            self.label_3.setObjectName("label_3")
            self.verticalLayout_6.addWidget(self.label_3)
            self.label_4 = QtWidgets.QLabel(self.widget_7)
            self.label_4.setStyleSheet("#label_4{\n"
                                       "font:  100 10pt \"Arial\";\n"
                                       "letter-spacing: 1px;\n"
                                       "line-height: 3.5px;\n"
                                       "color: #4A3B28;}")
            self.label_4.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
            self.label_4.setWordWrap(True)
            self.label_4.setMargin(25)
            self.label_4.setObjectName("label_4")
            self.verticalLayout_6.addWidget(self.label_4)
            self.verticalLayout_3.addWidget(self.widget_7)
            self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.widget_3.setObjectName("widget_3")
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_3)
            self.verticalLayout_7.setContentsMargins(0, 0, 0, -1)
            self.verticalLayout_7.setSpacing(0)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.label_7 = QtWidgets.QLabel(self.widget_3)
            self.label_7.setStyleSheet("#label_7{\n"
                                       "font: 150 17pt Segoe UI Black;\n"
                                       "alignment: center;\n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "                                 }")
            self.label_7.setObjectName("label_7")
            self.verticalLayout_7.addWidget(self.label_7)
            self.label_5 = QtWidgets.QLabel(self.widget_3)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setStrikeOut(False)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.label_5.setFont(font)
            self.label_5.setStyleSheet("#label_5{\n"
                                       "font:  100 10pt \"Arial\";\n"
                                       "letter-spacing: 1px;\n"
                                       "line-height: 3.5px;\n"
                                       "color: #4A3B28;}")
            self.label_5.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
            self.label_5.setWordWrap(True)
            self.label_5.setObjectName("label_5")
            self.label_5.setMargin(25)
            self.verticalLayout_7.addWidget(self.label_5)
            self.verticalLayout_3.addWidget(self.widget_3)
            self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.widget_5.setObjectName("widget_5")
            self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_5)
            self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_8.setObjectName("verticalLayout_8")
            self.widget_10 = QtWidgets.QWidget(self.widget_5)
            self.widget_10.setObjectName("widget_10")
            self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_10)
            self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
            self.verticalLayout_9.setObjectName("verticalLayout_9")
            self.label_8 = QtWidgets.QLabel(self.widget_10)
            self.label_8.setStyleSheet("#label_8{\n"
                                       "font: 150 17pt Segoe UI Black;\n"
                                       "alignment: center;\n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "                                 }")
            self.label_8.setObjectName("label_8")
            self.verticalLayout_9.addWidget(self.label_8)
            self.verticalLayout_8.addWidget(self.widget_10)
            self.widget_11 = QtWidgets.QWidget(self.widget_5)
            self.widget_11.setMinimumSize(QtCore.QSize(200, 0))
            self.widget_11.setObjectName("widget_11")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_11)
            self.horizontalLayout.setContentsMargins(25, -1, -1, -1)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.label_11 = QtWidgets.QLabel(self.widget_11)
            self.label_11.setMinimumSize(QtCore.QSize(70, 70))
            self.label_11.setMaximumSize(QtCore.QSize(70, 70))
            self.label_11.setText("")
            self.label_11.setPixmap(QtGui.QPixmap("images/Ilagan.png"))
            self.label_11.setScaledContents(True)
            self.label_11.setObjectName("label_11")
            self.horizontalLayout.addWidget(self.label_11)
            self.label_9 = QtWidgets.QLabel(self.widget_11)
            self.label_9.setStyleSheet("#label_9{\n"
                                       "font: 150 14pt Segoe UI Black;\n"
                                       "alignment: center;\n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "                                 }")
            self.label_9.setIndent(10)
            self.label_9.setObjectName("label_9")
            self.horizontalLayout.addWidget(self.label_9)
            self.verticalLayout_8.addWidget(self.widget_11)
            self.widget_9 = QtWidgets.QWidget(self.widget_5)
            self.widget_9.setObjectName("widget_9")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_9)
            self.horizontalLayout_2.setContentsMargins(25, -1, -1, -1)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label_12 = QtWidgets.QLabel(self.widget_9)
            self.label_12.setMaximumSize(QtCore.QSize(70, 70))
            self.label_12.setText("")
            self.label_12.setPixmap(QtGui.QPixmap("images/Maiquez.png"))
            self.label_12.setScaledContents(True)
            self.label_12.setObjectName("label_12")
            self.horizontalLayout_2.addWidget(self.label_12)
            self.label_10 = QtWidgets.QLabel(self.widget_9)
            self.label_10.setStyleSheet("#label_10{\n"
                                        "font: 150 14pt Segoe UI Black;\n"
                                        "alignment: center;\n"
                                        "color: rgba(111, 75, 39, 0.77);\n"
                                        "                                 }")
            self.label_10.setIndent(10)
            self.label_10.setObjectName("label_10")
            self.horizontalLayout_2.addWidget(self.label_10)
            self.verticalLayout_8.addWidget(self.widget_9)
            self.widget_8 = QtWidgets.QWidget(self.widget_5)
            self.widget_8.setObjectName("widget_8")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
            self.horizontalLayout_3.setContentsMargins(25, -1, -1, -1)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.label_13 = QtWidgets.QLabel(self.widget_8)
            self.label_13.setMinimumSize(QtCore.QSize(70, 70))
            self.label_13.setMaximumSize(QtCore.QSize(70, 70))
            self.label_13.setText("")
            self.label_13.setPixmap(QtGui.QPixmap("images/Narvaez.png"))
            self.label_13.setScaledContents(True)
            self.label_13.setObjectName("label_13")
            self.horizontalLayout_3.addWidget(self.label_13)
            self.label_14 = QtWidgets.QLabel(self.widget_8)
            self.label_14.setStyleSheet("#label_14{\n"
                                        "font: 150 14pt Segoe UI Black;\n"
                                        "alignment: center;\n"
                                        "color: rgba(111, 75, 39, 0.77);\n"
                                        "                                 }")
            self.label_14.setIndent(10)
            self.label_14.setObjectName("label_14")
            self.horizontalLayout_3.addWidget(self.label_14)
            self.verticalLayout_8.addWidget(self.widget_8)
            self.widget_6 = QtWidgets.QWidget(self.widget_5)
            self.widget_6.setObjectName("widget_6")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
            self.horizontalLayout_4.setContentsMargins(25, -1, -1, -1)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.label_15 = QtWidgets.QLabel(self.widget_6)
            self.label_15.setMinimumSize(QtCore.QSize(70, 70))
            self.label_15.setMaximumSize(QtCore.QSize(70, 70))
            self.label_15.setStyleSheet("#label_15{border-bottom-radius:7px;}")
            self.label_15.setText("")
            self.label_15.setPixmap(QtGui.QPixmap("images/Nora.png"))
            self.label_15.setScaledContents(True)
            self.label_15.setWordWrap(True)
            self.label_15.setObjectName("label_15")
            self.horizontalLayout_4.addWidget(self.label_15)
            self.label_16 = QtWidgets.QLabel(self.widget_6)
            self.label_16.setStyleSheet("#label_16{\n"
                                        "font: 150 14pt Segoe UI Black;\n"
                                        "alignment: center;\n"
                                        "color: rgba(111, 75, 39, 0.77);\n"
                                        "                                 }")
            self.label_16.setIndent(10)
            self.label_16.setObjectName("label_16")
            self.horizontalLayout_4.addWidget(self.label_16)
            self.verticalLayout_8.addWidget(self.widget_6)
            self.verticalLayout_3.addWidget(self.widget_5)

            self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.widget_2.setObjectName("widget_2")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
            self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.toolButton = QtWidgets.QToolButton(self.widget_2)
            self.toolButton.setText("Press Esc to exit.")
            self.toolButton.setMinimumSize(QtCore.QSize(30, 30))
            self.toolButton.setStyleSheet("color:rgba(111, 75, 39, 0.77);")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/asddas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
            self.toolButton.setIconSize(QtCore.QSize(40, 40))
            self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            self.toolButton.setAutoRaise(True)
            self.toolButton.setObjectName("toolButton")
            self.horizontalLayout_5.addWidget(self.toolButton)
            self.verticalLayout_3.addWidget(self.widget_2)

            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout_2.addWidget(self.scrollArea)
            self.verticalLayout.addWidget(self.widget)
            self.label_2.setText("How To Use                     ")
            self.label_3.setText("Creating New Projects & Folders")
            self.label_4.setText(
                                            "<b>1.</b> Click the \"Create Project\" button displayed on the main menu of the application.<br><br>\n"
                                            "<b>2.</b> Name your project based on the location where the images that will be saved inside it were taken for a more effective file management.<br><br>\n"
                                            "<b>3.</b> Inside your project, create folders to organize your files. You can name your folders based on your preferences. You can also create new folders within your 4, project anytime you want by selecting the \"New Folder\" button within the project.<br><br>\n"
                                            "<b>4.</b> You can upload an image into the folders you\'ve created and it will automatically be processed and proceed to the application’s main function upon uploading or you can go back to the main menu and use the “Upload Image” button as it will give you the option to choose where to save the results. You can select an existing folder within your project, or create a new folder on the spot to save the results in it.<br><br>\n"
                                            "<b>5.</b> After using the main function, the app You can also create new folders within your project anytime you want by selecting the \"Create New Folder\" button within the project.<br><br>\n"
                                            "<b>6.</b> To access your projects and folders later, simply navigate to the main menu and select the project you want to view.<br><br>\n"
                                            "<b>7.</b> Enjoy using the app\'s project feature to keep your files organized and easily accessible!")
            self.label_7.setText("Calculator")
            self.label_5.setText("The calculator button in the main menu of the app provides access to different types of engineering-related calculators, such as Curb and Gutter Barrier Calculator, Square Concrete Calculator, Hole/Round Footings Calculator and Circular Slab or Tube Calculator. These calculators can be used to perform quick calculations related to various engineering tasks and projects, without the need for a separate calculator app or tool.")
            self.label_8.setText("Developers")
            self.label_9.setText("Ilagan, Jayvee P.")
            self.label_10.setText("Maiquez, John Carlo M.")
            self.label_14.setText("Narvaez, Allyza Mae A.")
            self.label_16.setText("Nora, John Patrick B.")
            Dialog.exec()
        except Exception as e:
            print(e)

    def close_how(self):
        self.background_widget.hide()
        print("hahaha")

    def upload_image(self):

        selected_folder_vrFile = "selected_folder_vrFile.txt"
        try:
            os.remove(selected_folder_vrFile)
        except FileNotFoundError:
            print(f"{selected_folder_vrFile} already removed or does not exist")
        image_path = self.open_file_dialog()
        if image_path is not None:
            try:
                image = cv2.imread(image_path)
                # Save the image to a temporary file
                temp_file_path = 'temp_image_original.jpg'
                cv2.imwrite(temp_file_path, image)
                self.background_widget.show()
                segment_dialog = QtWidgets.QDialog(self.Mainwindow)
                ui = Detect_Crack_Dialog(image_path, self.background_widget, self.history, self.myProjects, self.Mainwindow)
                ui.setupUi(segment_dialog)
                x = (self.Mainwindow.width() - segment_dialog.width()) // 2
                y = (self.Mainwindow.height() - segment_dialog.height()) // 2
                segment_dialog.move(x, y)
                segment_dialog.exec_()
            except Exception as e:
                print(e)
        else:
            print("No file selected.")

    def open_file_dialog(self):
        file_dialog = QFileDialog(self.Mainwindow)
        file_dialog.setNameFilter('Images (*.png *.jpg *.bmp)')
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            return selected_files[0]
        else:
            print("File dialog closed without selecting a file.")
            return None

    # Dialog Box for creating new project
    def creating_new_project(self):
        # Create dialog box
        NewProjectDialog = QtWidgets.QDialog()
        NewProjectDialog.setObjectName("NewFolderDialog")
        NewProjectDialog.setWindowFlags(Qt.FramelessWindowHint)
        NewProjectDialog.resize(500, 300)
        NewProjectDialog.setMinimumSize(QtCore.QSize(500, 300))
        NewProjectDialog.setMaximumSize(QtCore.QSize(500, 300))
        # set corner radius of dialog box
        NewProjectDialog.setAttribute(Qt.WA_TranslucentBackground)
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
                                         "color:rgb(144, 115, 87);"
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
            self.show_dialog_empty_text_error()
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
            self.c.execute("SELECT COUNT(*) FROM Projects WHERE project_name = ?", (new_projects,))
            result = self.c.fetchone()

            if result[0] == 0:
                # If the project name doesn't exist, insert it into the database
                self.c.execute("INSERT INTO Projects (project_name) VALUES (?)", (new_projects,))
                self.conn.commit()

                self.myProjects.clear()
                self.c.execute("SELECT project_name FROM Projects ORDER BY created_at DESC")
                rows = self.c.fetchall()
                with open('selected_project.txt', 'w') as f:
                    f.write(new_projects)
                try:
                    folder_dialog = QtWidgets.QDialog(self.Mainwindow)
                    ui = view_folder_dialog(self.background_widget, self.history, self.myProjects, self.Mainwindow)
                    ui.setupUi(folder_dialog)
                    x = (self.Mainwindow.width() - folder_dialog.width()) // 2
                    y = (self.Mainwindow.height() - folder_dialog.height()) // 2
                    folder_dialog.move(x, y)
                    folder_dialog.exec_()
                except Exception as e:
                    print(e)
                for row in rows:
                    self.myProjects.addItem(row[0])

                self.myProjects.setEditText("My Projects")
            else:
                # If the project name already exists, show a dialog message to inform the user
                self.show_dialog_failed_save()
                self.creating_new_project()

    def handleClicked(self):
        print("Combobox clicked")
    # Dialog Box for successfully saved project
    def show_dialog_success_save(self):

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
        self.timer.start(1000)
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
        self.label.setText("New Project Saved!")
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
            "QLabel { font: 900 \"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 22pt;}")
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

    def show_dialog_failed_save(self):
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
        self.timer.start(1000)
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
        self.label.setText("Project name already exists in the database!")
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
            "QLabel { font:\"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 15pt;}")
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
            "QLabel { font:\"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 15pt;}")
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

    def ButtonCal_function(self):
        try:
            self.background_widget.show()
            calculatorButtons = QtWidgets.QDialog(self.Mainwindow)
            ui = cal_dialog(self.background_widget)
            ui.setupUi(calculatorButtons)
            x = (self.Mainwindow.width() - calculatorButtons.width()) // 2
            y = (self.Mainwindow.height() - calculatorButtons.height()) // 2
            calculatorButtons.move(x, y)
            calculatorButtons.exec_()
        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Crackterize", "Crackterize"))

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
        self.label_process = QtWidgets.QLabel("Processing image for crack detection...", self.widget)
        self.label_process.setStyleSheet("background-color:#ffffff;\n"
                                         "font-size:20px;\n"
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
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.show()
        return Dialog


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Center the main window on the desktop screen
    desktop = QDesktopWidget().screenGeometry()
    screen_width, screen_height = desktop.width(), desktop.height()
    window_width, window_height = MainWindow.width(), MainWindow.height()
    x, y = (screen_width - window_width) // 2, (screen_height - window_height) // 2
    MainWindow.move(x, y)

    sys.exit(app.exec_())
