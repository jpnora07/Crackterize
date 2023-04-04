import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QTimer, pyqtSignal, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QScrollArea, QWidget, QLabel

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # self.data_added.connect(self.refreshWidget)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 489)
        MainWindow.setMaximumSize(600, 489)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setMinimumSize(600, 489)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        radius = 30
        self.centralwidget.setStyleSheet(
            """
            background:rgb(255, 255, 255);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )

        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
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
            self.selected_item = f.read()
            self.project_name_lbl.setText(self.selected_item)
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
        icon.addPixmap(QtGui.QPixmap("images/add_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addfolder_icon.setIcon(icon)
        self.addfolder_icon.setIconSize(QtCore.QSize(20, 20))
        self.addfolder_icon.clicked.connect(self.creating_new_Location)
        self.addfolder_icon.setObjectName("addfolder_icon")
        self.horizontalLayout_2.addWidget(self.addfolder_icon)

        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setContentsMargins(10, 10, 10, 10)
        # buttons
        self.buttons = []
        self.max_per_row = 4

        layout = QHBoxLayout()
        button = QPushButton(self.widget_3)  # magaadd ng buttons
        button.setIcon(QIcon("images/add_folder.png"))
        button.setStyleSheet("QPushButton { border: none;padding-bottom: 58px;}")
        button.setText('')
        button.setIconSize(QSize(100, 70))
        button.move(100, 105)
        button.setFixedSize(120, 140)
        button.clicked.connect(self.creating_new_Location)
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

        layout.addWidget(button)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        vbox = QVBoxLayout(self.scroll_widget)
        vbox.addLayout(layout)  # Enable wrapping

        # create label for add button
        self.add_label = QLabel(button)
        self.add_label.setText('Add Image ')
        self.add_label.setWordWrap(True)
        self.add_label.move(0, 77)
        self.add_label.resize(120, 77)
        self.add_label.setStyleSheet(
            "font: 700 9pt \"Franklin Gothic Medium\";\n"
            "font-family: \'Franklin Gothic Medium\';\n"
            "font-style: normal;\n"
            "font-weight: 200;\n"
            "font-size: 13px;\n"
            "line-height: 42px;\n"
            "text-align: center;\n"
            "color: #664323;\n"
            "padding-bottom: 10px;")
        self.add_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        main_layout = QVBoxLayout(self.widget_3)
        main_layout.addWidget(self.scroll)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
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
        self.back.clicked.connect(MainWindow.close)
        self.back.setObjectName("back")
        self.horizontalLayout_3.addWidget(self.back)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Calling a function that fetch the folders of project
        self.fetch_folders_of_projects()

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
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, 'Projects.db')
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
        for row in data:
            # Create a new button for each row in the fetched data
            self.btn = QPushButton(self.scroll_widget)
            self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.btn.setIcon(QIcon("images/folder.png"))
            self.btn.setStyleSheet(
                "QPushButton {border: none; font-size: 16px; text-align: center;padding-bottom: 58px;}")

            self.btn.setIconSize(QSize(90, 100))
            self.btn.setFixedSize(120, 140)
            self.buttons.append(self.btn)

            # add to layout
            if len(self.buttons) % self.max_per_row == 1:
                self.hbox = QHBoxLayout()
                self.scroll_widget.layout().insertLayout(0, self.hbox)
            else:
                self.hbox = self.scroll_widget.layout().itemAt(0).layout()

            self.hbox.insertWidget(0, self.btn)
            self.hbox.setAlignment(Qt.AlignTop | Qt.AlignLeft)

            # Set the label text of the button
            btn_label = QLabel(str(row[2]), self.btn)
            btn_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            btn_label.move(0, 75)
            btn_label.resize(120, 77)
            btn_label.setWordWrap(True)
            btn_label.setStyleSheet(
                "font: 700 9pt \"Franklin Gothic Medium\";\n"
                "font-family: \'Franklin Gothic Medium\';\n"
                "font-style: normal;\n"
                "font-weight: 200;\n"
                "font-size: 13px;\n"
                "line-height: 42px;\n"
                "color: #664323;\n"
                "padding-bottom: 5px;")

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

    def fetch_folders_of_projects(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'Projects.db')
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())