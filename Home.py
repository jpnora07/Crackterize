from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QPalette
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(180, 50, 180, 60)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.threeBtn = QtWidgets.QWidget(self.widget_2)

        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setColor(QtGui.QColor(144, 115, 87, 100))
        effect.setOffset(QtCore.QPointF(0, 4))
        self.threeBtn.setGraphicsEffect(effect)

        self.threeBtn.setMinimumSize(QtCore.QSize(0, 0))
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
        self.myProjects.view().parentWidget().setStyleSheet('border: none;')
        self.myProjects.setStyleSheet("#myProjects {\n"
                                      "padding-left: 10px;\n"
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
                                      "#myProjects QComboBox { background-color: black; }"
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
                                      "border: none;"
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
        self.history.view().parentWidget().setStyleSheet('border: none;')
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
        list_view = QListView()
        list_view.setLayoutDirection(Qt.RightToLeft)
        self.howtoUse.setView(list_view)
        self.howtoUse.view().parentWidget().setStyleSheet('border: none;')
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
        self.verticalLayout_3.addWidget(self.threeBtn)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setStyleSheet("background-image:url(images/Crackterize.png);\n"
                                    "background-repeat: no-repeat; \n"
                                    "background-position: center;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(300, 20, 300, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widgetUpload = QtWidgets.QWidget(self.widget_4)
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
        self.uploadImg = QtWidgets.QPushButton("Upload Image", self.widgetUpload)
        self.uploadImg.clicked.connect(self.upload_image)
        self.uploadImg.setIcon(QIcon('images/uploadIcon.png'))
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
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # new image upload function for upload button
    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.jpg *.jpeg)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)

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
        self.save_btn.clicked.connect(self.show_dialog_success_save)
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget_1)
        NewProjectDialog.exec()

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
