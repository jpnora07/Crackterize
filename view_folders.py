import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QTimer, QSizeF
from PyQt5.QtGui import QPainter, QTextImageFormat, QTextCursor, QTextDocument
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QScrollArea, QWidget, QDialog, \
    QTableWidgetItem

from manage_folder import mng_folder
from view_results import view_result_dialog


class view_folder_dialog(object):
    def __init__(self, background_widget, history, projects, mainwindow):
        super(view_folder_dialog, self).__init__()
        self.Mainwindow = mainwindow
        self.history = history
        self.myProjects = projects
        self.background_widget = background_widget

    def setupUi(self, view_folder_dialog):
        # self.data_added.connect(self.refreshWidget)
        self.view_folder_dialog_orig = view_folder_dialog
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
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("verticalLayout_2")
        self.project_name_lbl = QtWidgets.QLabel(self.widget)
        self.project_name_lbl.setMinimumSize(QtCore.QSize(1000, 0))
        self.project_name_lbl.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
            self.selected_item = f.read()
            self.project_name_lbl.setText(self.selected_item)
        self.horizontalLayout_2.addWidget(self.project_name_lbl)

        self.addfolder_icon = QtWidgets.QPushButton("Add Folder", self.widget)
        self.addfolder_icon.setStyleSheet("#addfolder_icon{\n"
                                          "padding:5px;\n"
                                          "background-color:#E3E9ED;"
                                          "color:#664323;\n"
                                          "font: 700 9pt \"Big Sky Regular\";\n"
                                          "margin-left:100px;\n"
                                          "margin-right:0px;\n"
                                          "border: none;"
                                          "border-radius:15px"
                                          "}"
                                          "#addfolder_icon::hover{\n"
                                          "background-color:#CFD9E0;"
                                          "border: none;"
                                          "}"
                                          )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/new_add_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addfolder_icon.setIcon(icon)
        self.addfolder_icon.setIconSize(QtCore.QSize(20, 20))
        self.addfolder_icon.clicked.connect(self.creating_new_Location)
        self.addfolder_icon.setObjectName("addfolder_icon")
        self.horizontalLayout_2.addWidget(self.addfolder_icon)

        self.Settings = QtWidgets.QPushButton("Manage Project", self.widget)
        # self.Settings.setFlat(False)
        self.Settings.setStyleSheet("#Settings{\n"
                                          "padding:5px;\n"
                                          "background-color:#E3E9ED;"
                                          "color:#664323;\n"
                                          "font: 700 9pt \"Big Sky Regular\";\n"
                                          "margin-left:10px;\n"
                                          "border: none;"
                                          "border-radius:15px"
                                          "}"
                                          "#Settings::hover{\n"
                                          "background-color:#CFD9E0;"
                                          "border: none;"
                                          "}"
                                    )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings.setIcon(icon)
        self.Settings.setIconSize(QtCore.QSize(20, 20))
        self.Settings.clicked.connect(self.manage_folders)
        self.Settings.setObjectName("Settings")
        self.horizontalLayout_2.addWidget(self.Settings)

        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(view_folder_dialog)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setContentsMargins(10, 10, 10, 10)
        # buttons
        self.buttons = []
        self.max_per_row = 6

        layout = QHBoxLayout()

        widget = QtWidgets.QWidget(view_folder_dialog)
        widget.setGeometry(QtCore.QRect(100, 50, 140, 140))
        widget.setObjectName("widget")
        verticalLayout = QtWidgets.QVBoxLayout(widget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        button = QtWidgets.QToolButton(widget)
        button.setMinimumSize(QtCore.QSize(90, 100))
        button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        button.setText("Create New Folder")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/new_add_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(90, 100))
        button.setAutoRaise(True)
        button.setObjectName("pushButton")
        button.clicked.connect(self.creating_new_Location)
        button.setStyleSheet(

            "#pushButton{\n"
            "border : none;\n"
            "background-color: white;\n"
            "                font: 700 9pt \\\"Franklin Gothic Medium\\\";\n"
            "                font-family: \\\'Franklin Gothic Medium\\\';\n"
            "               font-style: normal;\n"
            "                font-weight: 200;\n"
            "                font-size: 13px;\n"
            "                line-height: 42px;\n"
            "                color: #664323;\n"
            "}\n"
            "#pushButton:hover{\n"
            "color: #664323;\n"
            "border : none;\n"
            "background-color: white;\n"
            "}\n"
            "")
        verticalLayout.addWidget(button)

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

        self.print = QtWidgets.QPushButton("Edit Folders", self.frame)
        self.print.hide()
        self.print.setStyleSheet("#print{\n"
                                 "height:40px;\n"
                                 "font-weight:bold;\n"
                                 "font-size:15px;\n"
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
        self.print.clicked.connect(self.editFolders)
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
        QtCore.QMetaObject.connectSlotsByName(view_folder_dialog)

        # Calling a function that fetch the folders of project
        self.fetch_folders_of_projects()

    def closeEvent(self):
        selected_folder_vrFile = "selected_folder_vrFile.txt"
        selected_project = "selected_project.txt"
        try:
            os.remove(selected_folder_vrFile)
        except FileNotFoundError:
            print(f"{selected_folder_vrFile} already removed or does not exist")
        try:
            os.remove(selected_project)
        except FileNotFoundError:
            print(f"{selected_project} already removed or does not exist")
        self.view_folder_dialog_orig.close()
        self.background_widget.hide()

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

    def manage_folders(self):
        try:
            mngfolders = QtWidgets.QDialog(self.view_folder_dialog_orig)
            ui = mng_folder()
            ui.setupUi(mngfolders)
            mngfolders.center()
            mngfolders.show()
            mngfolders.exec_()

        except Exception as e:
            print(e)

    def addNewButton_to_Db(self):
        # Get the text from the QTextEdit widget
        location_folder_name = self.ET_newlocation.toPlainText()
        if len(location_folder_name) == 0:
            message = "Cannot be save if empty!"
            # If new_projects is empty, show an error message
            self.show_dialog_empty_text_error(message)
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
                message = f"Project name already exists."
                # If the project name already exists, show a dialog message to inform the user
                self.show_dialog_empty_text_error(message)
                self.creating_new_Location()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clear_layout(child.layout())

    def add_button_folder(self, data):
        for row in data:
            button_name = str(row[2])
            widget = QtWidgets.QWidget(self.scroll_widget)
            widget.setGeometry(QtCore.QRect(100, 50, 140, 140))
            widget.setObjectName("widget")
            verticalLayout = QtWidgets.QVBoxLayout(widget)
            verticalLayout.setContentsMargins(0, 0, 0, 0)
            verticalLayout.setObjectName("verticalLayout")
            btn = QtWidgets.QToolButton(widget)
            btn.setMinimumSize(QtCore.QSize(90, 100))
            btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            btn.setText(button_name)
            btn.setAutoRaise(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn.setIcon(icon)
            btn.setIconSize(QtCore.QSize(90, 100))
            btn.setObjectName("pushButton")
            btn.clicked.connect(lambda checked, button=btn: self.view_folder(button))
            btn.setStyleSheet(

                "#pushButton{\n"
                "border : none;\n"
                "background-color: white;\n"
                "                font: 700 9pt \\\"Franklin Gothic Medium\\\";\n"
                "                font-family: \\\'Franklin Gothic Medium\\\';\n"
                "               font-style: normal;\n"
                "                font-weight: 200;\n"
                "                font-size: 13px;\n"
                "                line-height: 42px;\n"
                "                color: #664323;\n"
                "}\n"
                "#pushButton:hover{\n"
                "color: #664323;\n"
                "border : none;\n"
                "background-color: white;\n"
                "}\n"
                "")
            verticalLayout.addWidget(btn)
            self.buttons.append(btn)

            # add to layout
            if len(self.buttons) % self.max_per_row == 1:
                hbox = QHBoxLayout()
                self.scroll_widget.layout().insertLayout(0, hbox)
            else:
                hbox = self.scroll_widget.layout().itemAt(0).layout()

            hbox.insertWidget(0, widget)
            hbox.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    def view_folder(self, button):
        folder_name = button.text()
        with open('selected_folder_vrFile.txt', 'w') as f:
            f.write(folder_name)
        try:
            result_dialog = QtWidgets.QDialog(self.view_folder_dialog_orig)
            x = (self.view_folder_dialog_orig.width() - self.view_folder_dialog_orig.width()) // 2
            y = (self.view_folder_dialog_orig.height() - self.view_folder_dialog_orig.height()) // 2
            ui = view_result_dialog(self.background_widget, self.view_folder_dialog_orig, self.history, self.myProjects,
                                    self.Mainwindow)

            ui.setupUi(result_dialog)
            result_dialog.move(x, y)
            result_dialog.show()
            result_dialog.exec_()
            print(folder_name)

        except Exception as e:
            print(e)

    def show_dialog_empty_text_error(self, message):
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
        self.label.setText(message)
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
            "QLabel { font:\"Segoe UI\"; color: #4A3B28; font-family: Arial; Text-align: Center; font-size: 15pt;background-color: transparent;}")
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
                                    "background-image: url(images/failed.png);\n"
                                    "background-repeat: no-repeat; \n"
                                    "background-position: center;}")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget)
        Dialog.exec()

    def fetch_folders_of_projects(self):
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        db_path = os.path.join(dir_path, 'Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        # create a table if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS Location_Folder
                                             (id INTEGER PRIMARY KEY, project_name TEXT, folder_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        # fetch data from the database
        self.c.execute("SELECT * FROM Location_Folder WHERE project_name = ?", (self.selected_item,))
        data = self.c.fetchall()
        self.add_button_folder(data)

    def fetch_location_folder_by_id(self, folder_id):
        self.c.execute("SELECT * FROM Location_Folder WHERE id=?", (folder_id,))
        row = self.c.fetchone()
        return row

    def editFolders(self):
        Dialog = QDialog()
        self.editFolders_dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(493, 297)
        Dialog.setStyleSheet(
            '''#Dialog{border: 1px solid grey;background:rgb(255, 255, 255);} ''')
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_2.setMaximumSize(QtCore.QSize(200, 300))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel("Select a Folder", self.widget_4)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setStyleSheet("#label{\n"
                                 "    font: 900 12pt \"Segoe UI Black\";\n"
                                 "    alignment: center;\n"
                                 "background: transparent;"
                                 "    color: rgba(111, 75, 39, 0.77);\n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.folder_names_cb = QtWidgets.QComboBox(self.widget_4)
        self.folder_names_cb.setObjectName("folder_names_cb")
        self.folder_names_cb.setStyleSheet("#folder_names_cb {\n"
                                           "        border-radius: 10px;\n"
                                           "        font-size: 18px;\n"
                                           "        font-family: Arial;\n"
                                           "color:rgb(144, 115, 87);"
                                           "        background-color: #fff;\n"
                                           "        border: 2px solid #aaa;\n"
                                           "        padding: 2px;\n"
                                           "padding-left:8px;\n"
                                           "    }\n"
                                           "\n"
                                           "#folder_names_cb::drop-down{\n"
                                           " image:url(images/arrowdown.png);\n"
                                           " width: 15px;\n"
                                           " height: 15px;\n"
                                           "padding: 6px;\n"
                                           "}\n"
                                           "#folder_names_cb::drop-down::pressed{\n"
                                           " image:url(images/arrowup.png);\n"
                                           "width: 15px;\n"
                                           " height: 15px;\n"
                                           "text-align: center;\n"
                                           "}\n"
                                           "#folder_names_cb QAbstractItemView {\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "outline: none;\n"
                                           "color:rgb(144, 115, 87);"
                                           " text-align: center;}\n"
                                           "\n"
                                           "#folder_names_cb QAbstractItemView::item {\n"
                                           "background-color: #F4EBE6;\n"
                                           " color: #4A3B28;\n"
                                           "color:rgb(144, 115, 87);"
                                           " text-align: center;\n"
                                           "min-height: 35px; min-width: 50px;\n"
                                           " border:0px;}\n"
                                           "\n"
                                           "#folder_names_cb QListView{\n"
                                           "border: none;\n"
                                           " font-weight:bold;\n"
                                           "color:rgb(144, 115, 87);"
                                           " text-align: center;}\n"
                                           "#folder_names_cb QListView::item{border:0px;\n"
                                           "border-radius: 15px;\n"
                                           "  padding:8px; \n"
                                           "margin:5px;}\n"
                                           "#folder_names_cb QListView::item:selected { \n"
                                           "color: white; \n"
                                           "background-color: #4A3B28}")
        try:
            with open('selected_project.txt', 'r') as f:
                self.project_name = f.read()
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, 'Projects.db')
            # Create a connection to a SQLite database or create it if it doesn't exist
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM Location_Folder WHERE project_name = ?", (self.project_name,))
            rows = self.c.fetchall()
            for row in rows:
                fold_name = str(row[2])
                id = str(row[0])
                self.folder_names_cb.addItem(fold_name, [id, fold_name])

        except Exception as e:
            print(e)

        self.folder_names_cb.activated.connect(self.addItemToTable)
        self.verticalLayout_3.addWidget(self.folder_names_cb)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 200))
        self.widget_5.setObjectName("widget_5")
        self.radioButton_delete = QtWidgets.QRadioButton("Delete", self.widget_5)
        self.radioButton_delete.setGeometry(QtCore.QRect(20, 20, 89, 20))
        self.radioButton_delete.setStyleSheet("#radioButton_delete{\n"
                                              "font-weight:bold;\n"
                                              "}\n"
                                              "#radioButton_delete::indicator{\n"
                                              "color: red;\n"
                                              "\n"
                                              "}")
        self.radioButton_delete.setObjectName("radioButton_delete")
        self.radioButton_print = QtWidgets.QRadioButton("Print", self.widget_5)
        self.radioButton_print.setGeometry(QtCore.QRect(20, 50, 89, 20))
        self.radioButton_print.setStyleSheet("#radioButton_print {\n"
                                             "font-weight:bold;\n"
                                             "}")
        self.radioButton_print.setObjectName("radioButton_print")
        self.radioButton_rename = QtWidgets.QRadioButton("Rename", self.widget_5)
        self.radioButton_rename.setGeometry(QtCore.QRect(20, 80, 89, 20))
        self.radioButton_rename.setStyleSheet("#radioButton_rename {\n"
                                              "font-weight:bold;\n"
                                              "}")
        self.radioButton_rename.setObjectName("radioButton_rename")
        self.verticalLayout.addWidget(self.widget_5)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_7)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("#scrollArea {\n"
                                      "background: transparent;\n"
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
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 162, 151))
        self.scrollAreaWidgetContents.setStyleSheet("#scrollAreaWidgetContents{\n"
                                                    "background: transparent;\n"
                                                    "color: #4A3B28;\n"
                                                    "min-height: 35px; min-width: 50px;;\n"
                                                    "                    \n"
                                                    "}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setStyleSheet("#tableWidget {"
                                       "border-style: solid; border-width: 2px; border-color: rgba(111, 75, 39, 0.77);"
                                       "background: transparent;"
                                       "color: rgba(111, 75, 39, 0.77);"
                                       "gridline-color: grey;"
                                       "}"

                                       "#tableWidget QHeaderView::section {"
                                       "background: transparent;"
                                       "color: rgba(111, 75, 39, 0.77);"
                                       "}")

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Folder Name', 'Remove'])
        self.tableWidget.horizontalHeader().resizeSection(0, 150)
        self.tableWidget.horizontalHeader().resizeSection(1, 50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_5.addWidget(self.tableWidget, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_6.setSizeIncrement(QtCore.QSize(0, 200))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancelbtn = QtWidgets.QPushButton("Cancel", self.widget_6)
        self.cancelbtn.setMinimumSize(QtCore.QSize(0, 30))
        self.cancelbtn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.cancelbtn.setStyleSheet("#cancelbtn{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #6A6E72;\n"
                                     "border-top-left-radius: 7px;\n"
                                     "border-top-right-radius: 7px;\n"
                                     "border-bottom-left-radius: 7px;\n"
                                     "border-bottom-right-radius: 7px;\n"
                                     "font-family: Inter;\n"
                                     "font-size: 11px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#cancelbtn:hover{\n"
                                     "color: #6A6E72;\n"
                                     "border : 3px solid#6A6E72;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.clicked.connect(Dialog.close)
        self.horizontalLayout_3.addWidget(self.cancelbtn)
        self.okaybtn = QtWidgets.QPushButton("Okay", self.widget_6)
        self.okaybtn.setMinimumSize(QtCore.QSize(0, 30))
        self.okaybtn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.okaybtn.setStyleSheet("#okaybtn{\n"
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
                                   "#okaybtn:hover{\n"
                                   "color: rgb(144,115,87);\n"
                                   "border : 3px solid rgb(144,115,87);\n"
                                   "background-color: white;\n"
                                   "}")
        self.okaybtn.setObjectName("okaybtn")
        self.okaybtn.clicked.connect(self.printTableItems)
        self.horizontalLayout_3.addWidget(self.okaybtn)

        self.verticalLayout_2.addWidget(self.widget_6)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.exec()

    def addItemToTable(self):
        # Get the selected item and id from the ComboBox
        index = self.folder_names_cb.currentIndex()
        if index == -1 and self.folder_names_cb.count() == 1:
            index = 0
        item = self.folder_names_cb.currentText()
        data = self.folder_names_cb.itemData(index)
        id = data[0]
        fold_name = data[1]

        # Check if the item is already in the table
        rowCount = self.tableWidget.rowCount()
        for row in range(rowCount):
            existing_item = self.tableWidget.item(row, 0)
            if existing_item and existing_item.data(Qt.UserRole)[0] == id:
                return  # Skip adding the item if it's already in the table

        # Add the item and remove button to the table in the ScrollArea
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowCount + 1)
        newItem = QTableWidgetItem(item)
        newItem.setData(Qt.UserRole, [id, fold_name])

        self.tableWidget.setItem(rowCount, 0, newItem)
        button = QPushButton()
        button.setMinimumSize(QtCore.QSize(0, 0))
        button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setFlat(True)
        button.clicked.connect(lambda _, i=rowCount: self.remove_item(i))
        self.tableWidget.setCellWidget(rowCount, 1, button)

    def remove_item(self, row):
        self.tableWidget.removeRow(row)
        # Update the row count
        rowCount = self.tableWidget.rowCount()

        # If there are no more rows, clear the table
        if rowCount == 0:
            self.tableWidget.clearContents()
        else:
            self.tableWidget.setRowCount(rowCount)


    def printTableItems(self):
        try:
            # Store the items in a list
            items_with_id = []
            items = []
            numRows = self.tableWidget.rowCount()
            for i in range(numRows):
                item_id = self.tableWidget.item(i, 0).data(QtCore.Qt.UserRole)[0]
                folder_name_orig = self.tableWidget.item(i, 0).data(QtCore.Qt.UserRole)[1]
                item = self.tableWidget.item(i, 0).text()
                items.append(item)

                item_dict = {'id': item_id, 'text': item, 'orig_text': folder_name_orig}
                items_with_id.append(item_dict)

            if len(items) == 0:
                print("The list is empty!")
            else:
                print("The list contains items.")

            if self.radioButton_delete.isChecked() and len(items) > 0:
                self.confirm_delete(items)

            elif self.radioButton_print.isChecked() and len(items) > 0:
                self.printer(items)

            elif self.radioButton_rename.isChecked() and len(items_with_id) > 0:
                column = self.tableWidget.currentColumn()
                rowCount = self.tableWidget.rowCount()
                for row in range(rowCount):
                    item = self.tableWidget.item(row, column)
                    if item and item.text() != "":
                        print(f"Row {row}, Column {column}: {item.data(Qt.UserRole)} (Original), {item.text()} (New)")

                for item in items_with_id:
                    if self.table_exists(self.c, 'Location_Folder'):
                        self.c.execute("UPDATE Location_Folder SET folder_name=? WHERE id=?",
                                       (item['text'], item['id']))
                    if self.table_exists(self.c, 'Save_Files'):
                        self.c.execute("UPDATE Save_Files SET folder_name=? WHERE folder_name=?",
                                       (item['text'], item['orig_text']))

                self.conn.commit()
                self.conn.close()
                self.buttons.clear()
                self.clear_layout(self.scroll_widget.layout())
                self.fetch_folders_of_projects()
                self.editFolders_dialog.close()

            else:
                icon_image = "images/warning.png"
                message = "Please choose folder management options."
                self.QMessage_Error_dialog(message, icon_image)

            # Print the list of items
            print(items)
        except Exception as e:
            print(e)

    def printer(self, folders):
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            db_path = os.path.join(dir_path, 'Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Create a comma-separated string of the folder names
            folders_string = ','.join(["'{}'".format(f) for f in folders])

            c.execute(f"SELECT * FROM Save_Files WHERE folder_name IN ({folders_string})")
            rows = c.fetchall()

            if not rows:
                icon_image = "images/warning.png"
                message = "Folder is empty."
                self.QMessage_Error_dialog(message, icon_image)
            else:
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
                        file_names = [f for f in os.listdir(images_path) if
                                      os.path.isfile(os.path.join(images_path, f))]

                        # find the file name that matches the row ID
                        for file_name in file_names:
                            if os.path.splitext(file_name)[0] == str(row[0]):
                                # add the saved image to the document
                                max_size = QSize(700, 450)
                                image_format = QTextImageFormat()
                                image_format.setWidth(max_size.width())
                                image_format.setHeight(max_size.height())
                                image_format.setName(os.path.join(images_path, file_name))
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
        except Exception as e:
            print(e)

    def delete_folders(self, folders):
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, 'Projects.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Create a comma-separated string of the folder names
        folders_string = ','.join(["'{}'".format(f) for f in folders])

        if self.table_exists(self.c, "Location_Folder"):
            c.execute(f"DELETE FROM Location_Folder WHERE folder_name IN ({folders_string})")
        if self.table_exists(self.c, "Save_Files"):
            c.execute(f"DELETE FROM Save_Files WHERE folder_name IN ({folders_string})")
        self.history.clear()  # This should work now
        c.execute("SELECT * FROM Save_Files ORDER BY created_at DESC")
        rows = c.fetchall()
        for row in rows:
            status = str(row[9])
            recent = str(row[14])
            id = str(row[0])
            self.history.addItem(status + " - " + recent, id)
        self.history.setEditText("History")
        conn.commit()
        conn.close()
        self.buttons.clear()
        self.clear_layout(self.scroll_widget.layout())
        self.fetch_folders_of_projects()
        self.editFolders_dialog.close()

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

    def confirm_delete(self, items):
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
        self.Yes.clicked.connect(self.delete_folders(items))
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

    def settings(self):
        with open('selected_project.txt', 'r') as f:
            self.project_name = f.read()

        Dialog = QDialog()
        self.setting_dialog = Dialog
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 168)
        Dialog.setStyleSheet("#Dialog{background-color: rgb(255,255,255); border: 1px solid rgb(144,115,87);}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel("Edit Project", self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("#label_2{\n"
                                   "background:transparent;"
                                   "    font: 900 12pt \"Segoe UI Black\";\n"
                                   "    alignment: center;\n"
                                   "    color: rgba(111, 75, 39, 0.77);\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(20, 5, 20, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEditrename = QtWidgets.QLineEdit(self.widget_3)
        self.textEditrename.setText(self.project_name)
        is_enabled = self.textEditrename.isEnabled()
        self.textEditrename.setEnabled(not is_enabled)
        self.textEditrename.setAlignment(QtCore.Qt.AlignCenter)
        self.textEditrename.setStyleSheet("font-size: 15pt ;\n"
                                          "border-style: solid; border-width: 2px; border-color: rgba(111, 75, 39, 0.77);")
        self.textEditrename.setObjectName("textEditrename")

        self.horizontalLayout_2.addWidget(self.textEditrename)
        self.rename = QtWidgets.QPushButton(self.widget_3)
        self.rename.setMinimumSize(QtCore.QSize(30, 30))
        self.rename.setMaximumSize(QtCore.QSize(30, 30))
        self.rename.setStyleSheet("#rename::hover{\n"
                                  "background-color:#CFD9E0;\n"
                                  "border: none;}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/edit_remarks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename.setIcon(icon)
        self.rename.setIconSize(QtCore.QSize(50, 50))
        self.rename.setAutoDefault(False)
        self.rename.setFlat(True)
        self.rename.setObjectName("rename")
        self.rename.clicked.connect(self.edit_remarks_enable)
        self.horizontalLayout_2.addWidget(self.rename)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_6.setSizeIncrement(QtCore.QSize(0, 200))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.deletebtn = QtWidgets.QPushButton("Delete", self.widget_6)
        self.deletebtn.setMinimumSize(QtCore.QSize(0, 30))
        self.deletebtn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.deletebtn.clicked.connect(self.delete_project)
        self.deletebtn.setStyleSheet("#deletebtn{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #6A6E72;\n"
                                     "border-top-left-radius: 7px;\n"
                                     "border-top-right-radius: 7px;\n"
                                     "border-bottom-left-radius: 7px;\n"
                                     "border-bottom-right-radius: 7px;\n"
                                     "font-family: Inter;\n"
                                     "font-size: 11px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#deletebtn:hover{\n"
                                     "color: #6A6E72;\n"
                                     "border : 3px solid#6A6E72;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.deletebtn.setObjectName("deletebtn")
        self.horizontalLayout_3.addWidget(self.deletebtn)
        self.okaybtn = QtWidgets.QPushButton("Ok", self.widget_6)
        self.okaybtn.setMinimumSize(QtCore.QSize(0, 30))
        self.okaybtn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.okaybtn.clicked.connect(self.rename_func)
        self.okaybtn.setStyleSheet("#okaybtn{\n"
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
                                   "#okaybtn:hover{\n"
                                   "color: rgb(144,115,87);\n"
                                   "border : 3px solid rgb(144,115,87);\n"
                                   "background-color: white;\n"
                                   "}")
        self.okaybtn.setObjectName("okaybtn")
        self.horizontalLayout_3.addWidget(self.okaybtn)
        self.verticalLayout.addWidget(self.widget_6)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.exec()

    def delete_project(self):
        if self.table_exists(self.c, "Projects"):
            self.c.execute("DELETE FROM Projects WHERE project_name = ?", (self.project_name,))
        if self.table_exists(self.c, "Location_Folder"):
            self.c.execute("DELETE FROM Location_Folder WHERE project_name = ?", (self.project_name,))
        if self.table_exists(self.c, "Save_Files"):
            self.c.execute("DELETE FROM Save_Files WHERE project_name = ?", (self.project_name,))
        self.conn.commit()
        self.myProjects.clear()
        self.c.execute("SELECT project_name FROM Projects ORDER BY created_at DESC")
        rows = self.c.fetchall()
        for row in rows:
            self.myProjects.addItem(row[0])
        self.myProjects.setEditText("My Projects")

        self.history.clear()
        self.c.execute("SELECT * FROM Save_Files ORDER BY created_at DESC")
        rowss = self.c.fetchall()
        for row1 in rowss:
            status = str(row1[9])
            recent = str(row1[14])
            id = str(row1[0])
            self.history.addItem(status + " - " + recent, id)
        self.history.setEditText("History")

        self.conn.commit()
        self.view_folder_dialog_orig.close()
        self.setting_dialog.close()
        self.background_widget.hide()

    def table_exists(self, cursor, table_name):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return self.c.fetchone() is not None
    def edit_remarks_enable(self):
        self.textEditrename.setEnabled(True)

    def rename_func(self):
        try:
            self.input_rename = self.textEditrename.text()
            if self.table_exists(self.c, 'Projects'):
                self.c.execute("UPDATE Projects SET project_name=? WHERE project_name=?",
                               (self.input_rename, self.project_name))

            if self.table_exists(self.c, 'Location_Folder'):
                self.c.execute("UPDATE Location_Folder SET project_name=? WHERE project_name=?",
                               (self.input_rename, self.project_name))

            if self.table_exists(self.c, 'Save_Files'):
                self.c.execute("UPDATE Save_Files SET project_name=? WHERE project_name=?",
                               (self.input_rename, self.project_name))

            self.conn.commit()
            with open('selected_project.txt', 'w') as f:
                f.write(self.input_rename)
            self.setting_dialog.close()
            self.project_name_lbl.setText(self.input_rename)
            self.myProjects.clear()
            self.c.execute("SELECT project_name FROM Projects ORDER BY created_at DESC")
            rows = self.c.fetchall()
            for row in rows:
                self.myProjects.addItem(row[0])
            self.myProjects.setEditText("My Projects")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = view_folder_dialog(None, None, None, None)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
