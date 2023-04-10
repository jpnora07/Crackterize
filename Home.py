import os
import sqlite3

import cv2
import numpy as np

import tensorflow as tf
from tensorflow import keras
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QMouseEvent, QMovie
from PyQt5.QtWidgets import QListView, QComboBox, QDialog, QFileDialog, QStyledItemDelegate, QScrollBar, \
    QAbstractItemView, QLineEdit, QFrame

from Segment_Image import Ui_DialogSegment
from result import Result_Dialog
from view_folders import view_folder_dialog


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

    def paint(self, painter, option, index):
        super().paint(painter, option, index)

from PyQt5.QtCore import QThread, pyqtSignal

class ImageProcessingThread(QThread):
    finished = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def run(self):
        try:
            # Load and process the image here
            image = cv2.imread(self.image_path)
            # Save the image to a temporary file
            temp_file_path = 'temp_image_original.jpg'
            cv2.imwrite(temp_file_path, image)
            # Check if the image is valid
            if image is not None:
                self.imageCnn = cv2.resize(image, (224, 224))
                self.imageCnn = np.expand_dims(self.imageCnn, axis=0)

                self.modelCnn = keras.models.load_model('resnet_model_cnn.h5')
                predictions = self.modelCnn.predict(self.imageCnn)
                score = tf.nn.softmax(predictions)
                print(score)
                class_names = ['No Detected Crack', 'Contains Crack']

                # Get the index of the predicted class
                predicted_class_index = np.argmax(score, axis=1)[0]

                # Get the name and score of the predicted class
                predicted_class_name = class_names[predicted_class_index]

                predicted_class_score = 100 * score[0][predicted_class_index]
                if predicted_class_index == 0:
                    predicted_Negative_score = predicted_class_score
                    predicted_Positive_score = 100 - predicted_Negative_score
                else:
                    predicted_Positive_score = predicted_class_score
                    predicted_Negative_score = 100 - predicted_Positive_score

                print(f"Positive crack probability: {predicted_Positive_score:.2f}%")
                print(f"Negative crack probability: {predicted_Negative_score:.2f}%")
                Negative_score = f"{predicted_Negative_score:.2f}%"
                Positive_score = f"{predicted_Positive_score:.2f}%"
                with open('Negative_score.txt', 'w') as f:
                    f.write(Negative_score)
                with open('Positive_score.txt', 'w') as f:
                    f.write(Positive_score)
                with open('Predicted_Class_name.txt', 'w') as f:
                    f.write(predicted_class_name)
                self.finished.emit(score)

            else:
                self.error.emit("Invalid image format")

        except Exception as e:
            print(e)
            self.error.emit(str(e))

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
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1000, 700)

        # MainWindow.resize(983, 573)
        #MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        # MainWindow.setMaximumSize(QtCore.QSize(983, 573))
        MainWindow.setStyleSheet("#MainWindow{\n"
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
        self.verticalLayout_3.setContentsMargins(180, 50, 180, 60)
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
        self.threeBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.threeBtn.setMaximumSize(QtCore.QSize(650, 58))
        self.threeBtn.setStyleSheet("#threeBtn{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px;\n"
                                    "}\n"
                                    "")
        self.threeBtn.setObjectName("threeBtn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.threeBtn)
        self.horizontalLayout.setContentsMargins(20, 15, 20, 15)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.myProjects = QtWidgets.QComboBox(self.threeBtn)
        self.myProjects.setMinimumSize(QtCore.QSize(25, 0))
        self.myProjects.setGeometry(200, 150, 150, 30)
        self.myProjects.setLineEdit(self.QTComboBoxButton(self.myProjects))
        self.ledit = self.myProjects.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, 'Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT project_name FROM Projects ORDER BY created_at DESC")
            rows = c.fetchall()
            for row in rows:
                self.myProjects.addItem(row[0])
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
                ui = view_folder_dialog(self.background_widget)
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

        self.myProjects.setObjectName("myProjects")
        self.horizontalLayout.addWidget(self.myProjects)
        self.history = QtWidgets.QComboBox(self.threeBtn)
        self.history.view().parentWidget().setStyleSheet('border: none;')
        self.history.setGeometry(200, 150, 150, 30)
        self.history.setEditable(True)
        self.history.setLineEdit(self.QTComboBoxButton(self.history))
        self.ledit = self.history.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, 'Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT * FROM Save_Files ORDER BY created_at DESC")
            rows = c.fetchall()
            print(rows)
            for row in rows:
                status = str(row[9])
                recent = str(row[14])
                self.history.addItem(status + " - " + recent)
        except Exception as e:
            print("Empty History! Users not yet add results: ", e)
        self.history.setEditText("History")

        def handleSelection(text):
            # change back to default title after item is selected
            self.history.setEditText("History")

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
                                   "text-align: center;\n"
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
        self.howtoUse = QtWidgets.QComboBox(self.threeBtn)
        list_view = QListView()
        list_view.setLayoutDirection(Qt.RightToLeft)
        self.howtoUse.setView(list_view)
        self.howtoUse.view().parentWidget().setStyleSheet('border: none;')
        self.howtoUse.setGeometry(200, 150, 150, 30)
        self.howtoUse.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)

        delegate = AlignDelegate(self.howtoUse)
        self.howtoUse.setItemDelegate(delegate)
        self.howtoUse.setEditable(True)
        self.ledit = self.howtoUse.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        self.howtoUse.addItems(
            [
                "STEP 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "STEP 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "STEP 3: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",

            ])
        self.howtoUse.setEditText("How to Use")

        def handleSelection(text):
            # change back to default title after item is selected
            self.howtoUse.setEditText("How to Use")

        self.howtoUse.activated[str].connect(handleSelection)

        # change the background of list in combo box and its corner
        self.howtoUse.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.howtoUse.view().window().setAttribute(Qt.WA_TranslucentBackground)
        view = QListView()
        view.setMinimumSize(500, 200)
        view.setWordWrap(True)
        radius = 20
        view.setStyleSheet(
            """
            background-color :rgba(255, 255, 255, 0.75);
            border-bottom-left-radius:{0}px;
            border-top-right-radius: {0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.howtoUse.setView(view)
        self.howtoUse.view().parentWidget().setStyleSheet('border: none;')
        self.howtoUse.setStyleSheet("#howtoUse{\n"
                                    "padding-left: 10px;\n"
                                    "border-radius:4px;\n"
                                    "font: 600 12pt \"Segoe UI\";\n"
                                    "color:#4A3B28;\n"
                                    "background: transparent;\n"
                                    "border:0px;"
                                    "text-align: center;\n"
                                    "}\n"

                                    "#howtoUse::drop-down{\n"
                                    "image:url(images/arrowdown.png);\n"
                                    "width: 20px;\n"
                                    "height: 20px;\n"
                                    "text-align: center;\n"
                                    "}\n"

                                    "#howtoUse::drop-down::pressed{\n"
                                    "image:url(images/arrowup.png);\n"
                                    "width: 20px;\n"
                                    "height: 20px;\n"
                                    "text-align: center;\n"
                                    "}\n"

                                    "#howtoUse QAbstractItemView {\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "outline: none;"
                                    "text-align: center;\n"
                                    "border:0px;"
                                    "\n"
                                    "}\n"

                                    "#howtoUse QAbstractItemView::item {\n"
                                    "background-color: #F4EBE6;\n"
                                    "color: #4A3B28;\n"
                                    "text-align: center;\n"
                                    "min-height: 35px; min-width: 50px;"
                                    "border:0px;"

                                    "}\n"

                                    "#howtoUse QListView{"
                                    "border:0px;"
                                    # "color:rgb(87, 96, 134);"
                                    # "background-color:rgb(255, 255, 255);"
                                    "font-weight:bold;"

                                    # "selection-background-color: rgb(47, 175, 178);"
                                    # "show-decoration-selected: 1;"
                                    "text-align: left;\n"
                                    "}"

                                    "#howtoUse QListView::item{"
                                    "border:0px;"
                                    "border-radius: 15px;"
                                    "padding:8px; "
                                    "margin:10px;"
                                    "text-align: center;\n"
                                    "}"


                                    "#howtoUse QListView::item:selected { "
                                    "color: white; "
                                    "background-color: #4A3B28}")
        self.howtoUse.setObjectName("howtoUse")
        self.horizontalLayout.addWidget(self.howtoUse)
        self.verticalLayout_3.addWidget(self.threeBtn)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setMaximumSize(QtCore.QSize(929, 150))
        self.widget_6.setStyleSheet("border-image:url(images/Crackterize.png) 400 0 400 0 stretch;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(100, 20, 100, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widgetUpload = QtWidgets.QWidget(self.widget_4)
        self.widgetUpload.setMaximumSize(QtCore.QSize(347, 128))
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setColor(QtGui.QColor(144, 115, 87, 100))
        effect.setOffset(QtCore.QPointF(0, 4))
        self.widgetUpload.setGraphicsEffect(effect)

        self.widgetUpload.setStyleSheet("#widgetUpload{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius:28px;\n"
                                        "}\n"
                                        "        \n"
                                        "")
        self.widgetUpload.setObjectName("widgetUpload")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widgetUpload)
        self.verticalLayout_5.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uploadImg = QtWidgets.QPushButton("  Upload Image", self.widgetUpload)
        self.uploadImg.clicked.connect(self.upload_image)
        self.uploadImg.setIcon(QIcon('images/uploadIcon.png'))
        self.uploadImg.setIconSize(QtCore.QSize(20, 20))
        self.uploadImg.setStyleSheet("#uploadImg{\n"
                                     "height:40px;\n"
                                     "font-weight:bold;\n"
                                     "font-size:15px;\n"
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
        self.verticalLayout_4.addWidget(self.widgetUpload)
        # new
        self.widgetUpload_2 = QtWidgets.QWidget(self.widget_4)
        self.widgetUpload_2.setMaximumSize(QtCore.QSize(347, 128))
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setColor(QtGui.QColor(144, 115, 87, 100))
        effect.setOffset(QtCore.QPointF(0, 4))
        self.widgetUpload_2.setGraphicsEffect(effect)
        self.widgetUpload_2.setStyleSheet("#widgetUpload_2{\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius:28px;\n"
                                          "}\n"
                                          "        \n"
                                          "")
        self.widgetUpload_2.setObjectName("widgetUpload_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widgetUpload_2)
        self.verticalLayout_6.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.calLbl = QtWidgets.QPushButton("Calculate Measurements", self.widgetUpload_2)
        self.calLbl.setStyleSheet("#calLbl{\n"
                                  "font-weight:bold;\n"
                                  " color:#363131;\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border :3px solid rgb(255, 255, 255);\n"
                                  " }\n"
                                  "#calLbl:hover{\n"
                                  "background-color:rgb(255, 255, 255);}\n"
                                  "")
        self.calLbl.setObjectName("calLbl")
        self.verticalLayout_6.addWidget(self.calLbl)
        self.ButtonCal = QtWidgets.QPushButton("Calculator", self.widgetUpload_2)
        self.ButtonCal.setStyleSheet("#ButtonCal{\n"
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
                                     "#ButtonCal:hover{\n"
                                     "color:rgb(144, 115, 87);\n"
                                     "border :2px solid rgb(144, 115, 87);\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "")
        self.ButtonCal.setObjectName("ButtonCal")

        self.ButtonCal.clicked.connect(self.ButtonCal_function)
        self.verticalLayout_6.addWidget(self.ButtonCal)
        self.verticalLayout_4.addWidget(self.widgetUpload_2)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add transparent white background widget
        self.background_widget = QFrame(MainWindow)
        self.background_widget.setStyleSheet("background-color: rgba(0, 0, 0, 0.25);")
        self.background_widget.resize(MainWindow.width(), MainWindow.height())
        self.background_widget.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def upload_image(self):
        image_path = self.open_file_dialog()
        if image_path is not None:
            try:
                self.load_dialog = self.loading()
                self.load_dialog.show()
                self.background_widget.show()

                # Create a new thread for the image processing task
                self.thread = ImageProcessingThread(image_path)
                self.thread.start()
                self.thread.finished.connect(lambda score: self.on_processing_finished(score))

            except Exception as e:
                print(e)
        else:
            print("No file selected.")

    def on_processing_finished(self, score):
        # Update the GUI with the results of the image processing task
        self.load_dialog.close()
        if np.argmax(score) == 0:
            try:
                with open('Predicted_width.txt', 'w') as f:
                    f.write("0")
                with open('Predicted_height.txt', 'w') as f:
                    f.write("0")
            except FileNotFoundError:
                print("The file does not exist.")
            result_dialog = QtWidgets.QDialog(self.Mainwindow)
            ui = Result_Dialog(None, self.background_widget)
            ui.setupUi(result_dialog)
            x = (self.Mainwindow.width() - result_dialog.width()) // 2
            y = (self.Mainwindow.height() - result_dialog.height()) // 2
            result_dialog.move(x, y)
            result_dialog.exec_()

        else:
            segment_dialog = QtWidgets.QDialog(self.Mainwindow)
            ui = Ui_DialogSegment(self.background_widget)
            ui.setupUi(segment_dialog)
            x = (self.Mainwindow.width() - segment_dialog.width()) // 2
            y = (self.Mainwindow.height() - segment_dialog.height()) // 2
            segment_dialog.move(x, y)
            segment_dialog.exec_()

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

                self.myProjects.clear()
                self.c.execute("SELECT project_name FROM Projects ORDER BY created_at DESC")
                rows = self.c.fetchall()
                with open('selected_project.txt', 'w') as f:
                    f.write(new_projects)
                try:
                    folder_dialog = QtWidgets.QDialog(self.Mainwindow)
                    ui = view_folder_dialog()
                    ui.setupUi(folder_dialog)
                    x = (self.Mainwindow.width() - folder_dialog.width()) // 2
                    y = (self.Mainwindow.height() - folder_dialog.height()) // 2
                    folder_dialog.move(x, y)
                    folder_dialog.exec_()
                except Exception as e:
                    print(e)
                for row in rows:
                    self.myProjects.addItem(row[0])
            else:
                # If the project name already exists, show a dialog message to inform the user
                self.show_dialog_failed_save()
                self.creating_new_project()

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
            # Get the path to the directory where the executable is run from
            app_path = getattr(sys, '_MEIPASS', None) or os.path.abspath('.')

            # Create the path to the result.py file
            calculatorButtons = os.path.join(app_path, 'calculatorButtons.py')
            # Execute the result.py file using QProcess
            process = QtCore.QProcess()
            process.start('python', [calculatorButtons])

            if process.waitForFinished() == 0:
                print('Error: failed to execute result.py')
        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

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
        self.label_process.setStyleSheet("background-color:#ffffff;\n"
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
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.show()
        return Dialog

    def loading_getweight(self):
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
        self.label_process = QtWidgets.QLabel("Calculating the Width and Length...", self.widget)
        self.label_process.setStyleSheet("background-color:#ffffff;\n"
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
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.show()
        return Dialog


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
