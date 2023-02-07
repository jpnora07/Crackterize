from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QListView, QComboBox, QDialog, QVBoxLayout, QApplication, QFileDialog


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(983, 573)
        MainWindow.setMinimumSize(QtCore.QSize(983, 573))
        MainWindow.setMaximumSize(QtCore.QSize(983, 573))
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 931, 601))
        self.widget.setStyleSheet("width: fit-content;\n"
                                  "block-size: fit-content;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.threeBtn = QtWidgets.QWidget(self.widget_2)
        self.threeBtn.setGeometry(QtCore.QRect(180, 60, 531, 61))
        self.threeBtn.setContentsMargins(10, 0, 50, 0)
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(8)
        self.threeBtn.setGraphicsEffect(effect)
        self.threeBtn.setStyleSheet("#threeBtn{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px;\n"
                                    "}\n"
                                    "")
        self.threeBtn.setObjectName("threeBtn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.threeBtn)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.myProjects = QtWidgets.QComboBox(self.threeBtn)

        # edited text allign
        self.myProjects.setMinimumSize(QtCore.QSize(25, 0))
        self.myProjects.setGeometry(200, 150, 150, 30)
        geek_list = ["Project 1", "Project 2", "Project 3", "Project 4"]
        self.myProjects.addItems(geek_list)
        self.myProjects.setEditable(True)
        self.ledit = self.myProjects.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        self.myProjects.setEditText("My Projects")

        def handleSelection(text):
            # change back to default title after item is selected
            self.myProjects.setEditText("My Projects")

        self.myProjects.activated[str].connect(handleSelection)
        # Disable showing the selected item in the title
        view = QListView()
        view.setWordWrap(True)
        self.myProjects.setView(view)
        self.myProjects.setStyleSheet("#myProjects{\n"
                                      "padding-left: 10px;\n"
                                      "border-radius:4px;\n"
                                      "font: 600 12pt \"Segoe UI\";\n"
                                      "color:#4A3B28;\n"
                                      "background: transparent;\n"
                                      "border:0px;"
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

                                      "border:0px;"
                                      "\n"
                                      "}\n"

                                      "#myProjects QAbstractItemView::item {\n"
                                      "background-color: #F4EBE6;\n"
                                      "color: #4A3B28;\n"
                                      "text-align: center;\n"
                                      "min-height: 35px; min-width: 50px;"
                                      "border:0px;"
                                      "}\n"

                                      "#myProjects QListView{"
                                      "border:0px;"
                                      # "color:rgb(87, 96, 134);"
                                      # "background-color:rgb(255, 255, 255);"
                                      "font-weight:bold;"
                                      # "selection-background-color: rgb(47, 175, 178);"
                                      # "show-decoration-selected: 1;"
                                      "text-align: center;\n"
                                      "}"

                                      "#myProjects QListView::item{"
                                      "border:0px;"
                                      "border-radius: 15px;"
                                      "padding:8px; "
                                      "margin:10px;"
                                      "text-align: center;\n"
                                      "}"
                                      "#myProjects QListView::text {"
                                      "left: 27px;}"

                                      "#myProjects QListView::item:selected { "
                                      "color: white; "
                                      "background-color: #4A3B28}")
        self.myProjects.setObjectName("myProjects")

        self.horizontalLayout.addWidget(self.myProjects)

        self.history = QtWidgets.QComboBox(self.threeBtn)
        # edited text allign
        self.history.setMinimumSize(QtCore.QSize(25, 0))
        self.history.setGeometry(200, 150, 150, 30)
        geek_list = ["Image 1", "Image 2", "Image 3", "Image 4"]
        self.history.addItems(geek_list)
        self.history.setEditable(True)
        self.ledit = self.history.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        self.history.setEditText("History")

        def handleSelection(text):
            # change back to default title after item is selected
            self.history.setEditText("History")

        self.history.activated[str].connect(handleSelection)
        # Disable showing the selected item in the title
        view = QListView()
        view.setWordWrap(True)
        self.history.setView(view)
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
        # edited text allign
        self.howtoUse.setGeometry(200, 150, 150, 30)
        self.howtoUse.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.howtoUse.addItems(
            [
                "STEP 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "STEP 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "STEP 3: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",

            ])
        self.howtoUse.setEditable(True)
        self.ledit = self.howtoUse.lineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setAlignment(Qt.AlignCenter)
        self.howtoUse.setEditText("How to Use")

        def handleSelection(text):
            # change back to default title after item is selected
            self.howtoUse.setEditText("How to Use")

        self.howtoUse.activated[str].connect(handleSelection)
        # Disable showing the selected item in the title
        view = QListView()
        view.setMinimumSize(500, 200)
        view.setWordWrap(True)
        self.howtoUse.setView(view)
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

        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setGeometry(QtCore.QRect(210, 0, 481, 100))
        self.widget_6.setStyleSheet("background-image: url(images/Crackterize.png);\n"
                                    "background-repeat: no-repeat; \n"
                                    "background-position: center;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.widgetUpload = QtWidgets.QWidget(self.widget_4)
        self.widgetUpload.setGeometry(QtCore.QRect(270, 0, 341, 120))
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(8)
        self.widgetUpload.setGraphicsEffect(effect)
        self.widgetUpload.setStyleSheet("#widgetUpload{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius:28px;\n"
                                        "box-shadow: 55px 55px 150px black;\n"
                                        "}\n"
                                        "")
        self.widgetUpload.setObjectName("widgetUpload")

        # Upload Button
        self.uploadImg = QtWidgets.QPushButton("Upload Image", self.widgetUpload)
        self.uploadImg.clicked.connect(self.upload_image)

        # effect = QtWidgets.QGraphicsDropShadowEffect()
        # effect.setBlurRadius(8)
        # self.uploadImg.setGraphicsEffect(effect)
        self.uploadImg.setGeometry(QtCore.QRect(70, 30, 201, 41))
        self.uploadImg.setIcon(QIcon('../images/uploadIcon.png'))
        self.uploadImg.setStyleSheet("#uploadImg{\n"
                                     "font-weight:bold;"
                                     "font-size:12px;"
                                     "color:white;"
                                     "background-color: rgb(144, 115, 87);\n"
                                     "border-top-left-radius :20px;"
                                     "border-top-right-radius : 20px; "
                                     "border-bottom-left-radius : 20px; "
                                     "border-bottom-right-radius : 20px;"
                                     "}\n"
                                     "#uploadImg:hover{\n"
                                     "color:rgb(144, 115, 87);"
                                     "border :3px solid rgb(144, 115, 87);"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "}\n")
        self.uploadImg.setObjectName("uploadImg")

        self.textEdit = QtWidgets.QPushButton("or create a new project", self.widgetUpload)

        self.textEdit.setGeometry(QtCore.QRect(100, 80, 161, 21))
        self.textEdit.setStyleSheet("#textEdit{\n"
                                    "font-weight:bold;"
                                    "color:#363131;"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border :3px solid rgb(255, 255, 255);"
                                    "}\n"
                                    "#textEdit:hover{\n"
                                    "background-color:rgb(255, 255, 255);"
                                    )
        # button
        self.textEdit.clicked.connect(self.show_floating_dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.widget_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


#Dialog Box for creating new project
    def show_floating_dialog(self):
        # Create dialog box
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Dialog")
        dialog.resize(500, 300)
        dialog.setWindowFlags(Qt.FramelessWindowHint)
        dialog.setStyleSheet("#dialog{\n"
                             "background-color: #EFEEEE;\n"
                             "width: fit-content;\n"
                             "heigth: fit-content;\n"
                             "block-size: fit-content;\n"
                             "}")
        self.widget_1 = QtWidgets.QWidget(dialog)
        self.widget_1.setGeometry(QtCore.QRect(10, 30, 411, 191))
        self.widget_1.setStyleSheet("width: fit-content;\n"
                                    "block-size: fit-content;")
        self.widget_1.setObjectName("widget_1")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_1)
        self.widget_3.setEnabled(True)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.ET_newproject = QtWidgets.QTextEdit(self.widget_2)
        self.ET_newproject.setGeometry(QtCore.QRect(0, 10, 375, 57))
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
        self.ET_newproject.setPlaceholderText("      Type name of your new project")
        self.ET_newproject.setTabChangesFocus(False)
        self.ET_newproject.setAlignment(Qt.AlignCenter)
        self.ET_newproject.setObjectName("ET_newproject")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_1)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(self.widget)
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
                                    "margin-left:30px;\n"
                                    "margin-right:10px;\n"
                                    "}\n"
                                    "#back_btn:hover{\n"
                                    "color:#6A6E72;\n"
                                    "border :2px solid #6A6E72;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.back_btn.setText("Back")
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(dialog.close)
        self.horizontalLayout.addWidget(self.back_btn)
        self.save_btn = QtWidgets.QPushButton(self.widget)
        self.save_btn.clicked.connect(dialog.close)
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
                                    "margin-left:10px;\n"
                                    "margin-right:30px;\n"
                                    "}\n"
                                    "#save_btn:hover{\n"
                                    "color:rgb(144, 115, 87);\n"
                                    "border :2px solid rgb(144, 115, 87);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.save_btn.setText("Save")
        # button
        self.save_btn.clicked.connect(self.show_floating_dialog_save)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_4)
        dialog.exec()

# Dialog Box for successfully saved project
    def show_floating_dialog_save(self):
        # Create dialog box
        Dialog = QtWidgets.QDialog()
        Dialog.setWindowTitle("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(350, 300)
        Dialog.setStyleSheet("#Dialog{\n"
                             "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
                             "width: fit-content;\n"
                             "heigth: fit-content;\n"
                             "block-size: fit-content;\n"
                             "}\n"
                             "")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(70, 90, 231, 21))

        self.label.setText("New Project Saved!")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "QLabel { font: 900 \"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 16pt;}")
        self.label.setObjectName("label")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(0, 130, 383, 138))
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(100, 10, 151, 101))
        self.widget_4.setStyleSheet("#widget_4{\n"
                                    "background-image: url(images/ok3.png);\n"
                                    "background-repeat: no-repeat; \n"
                                    "background-position: center;}")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout.addWidget(self.widget_2)
        Dialog.exec()

#new image upload function for upload button
    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "Images (*.png *.xpm *.jpg *.bmp *.gif *.jpeg)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)
# QApplication.instance().quit this is clossing application
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
