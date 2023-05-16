import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QStyledItemDelegate, QListView


class mng_folder(object):
    def __init__(self, background_widget, projects, history, proj_name_lbl, button, clear_layout,
                 fetch_folders_of_projects, scroll_widget):
        self.bg_widget = background_widget
        self.myProjects = projects
        self.history = history
        self.project_name_lbl = proj_name_lbl
        self.clear_btn = button
        self.clear_layout = clear_layout
        self.fetch_folders_of_projects = fetch_folders_of_projects
        self.scroll_widget = scroll_widget

    def setupUi(self, Dialog):
        self.Manage_Folder_Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setFixedSize(700, 600)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        radius = 20
        self.widget.setStyleSheet("""
                            background-color:white;
                            border-top-left-radius:{0}px;
                            border-bottom-left-radius:{0}px;
                            border-top-right-radius:{0}px;
                            border-bottom-right-radius:{0}px;
                            """.format(radius))
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(548, 397))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.widget_7.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_7.setMaximumSize(QtCore.QSize(8899, 58))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(
            "<html><head/><body><p align=\"center\">Choose an action for this project:</p></body></html>",
            self.widget_7)
        self.label.setStyleSheet("#label{\n"
                                 "height:40px;\n"
                                 "font-weight:600;\n"
                                 "font-size:26px;\n"
                                 "color: #555555;\n"
                                 "font-family: Inter;\n"
                                 "\n"
                                 "}")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(
            "<html><head/><body><p align=\"center\"><span style=\" color:#3d3d3e;\">Rename current project</span></p></body></html>",
            self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(185, 0))
        self.label_2.setMaximumSize(QtCore.QSize(8899, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "background-color:#e4e9ed;\n"
                                   "border-radius:10px;\n"
                                   "font-size:12px;"
                                   "font-weight:400;\n"
                                   "}")
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.rename_proj_LE = QtWidgets.QLineEdit(self.widget_2)
        self.rename_proj_LE.setMinimumSize(QtCore.QSize(185, 40))
        self.rename_proj_LE.setMaximumSize(QtCore.QSize(32, 16777215))

        self.rename_proj_LE.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rename_proj_LE.setFont(font)
        self.rename_proj_LE.setStyleSheet(
            "     border-radius: 10px;\n"
            "        font-size: 12px;\n"
            "        font-family: Arial;\n"
            "font-weight:400;"
            "        color:rgb(144, 115, 87);"
            "        background-color: #fff;\n"
            "        border: 2px solid #aaa;\n"
            "        padding: 2px;\n")
        self.rename_proj_LE.setObjectName("rename_proj_LE")
        with open('selected_project.txt', 'r') as f:
            self.project_name = f.read()
        self.rename_proj_LE.setPlaceholderText(self.project_name)
        self.horizontalLayout_3.addWidget(self.rename_proj_LE)
        self.save_proj = QtWidgets.QPushButton("Save Changes", self.widget_2)
        self.save_proj.setMinimumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.save_proj.setFont(font)
        self.save_proj.setStyleSheet("#save_proj{\n"
                                     "background-color:\n"
                                     "#4a93d6;\n"
                                     "border-radius:10px;\n"
                                     "font-size:12px;"
                                     "font-weight:400;\n"
                                     "color:white;\n"
                                     "}\n"
                                     "#save_proj::hover{\n"
                                     "background-color:\n"
                                     "white;\n"
                                     "border:2px solid #4a93d6;\n"
                                     "color:#4a93d6;\n"
                                     "}")
        self.save_proj.setObjectName("save_proj")
        self.save_proj.clicked.connect(self.save_proj_new_name)
        self.horizontalLayout_3.addWidget(self.save_proj)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(
            "<html><head/><body><p align=\"center\"><span style=\" color:#3d3d3e;\">Rename Folders</span></p></body></html>",
            self.widget_5)
        self.label_3.setMinimumSize(QtCore.QSize(185, 0))
        self.label_3.setMaximumSize(QtCore.QSize(8899, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "\n"
                                   "background-color:\n"
                                   "#e4e9ed;\n"
                                   "border-radius:10px;\n"
                                   "font-size:12px;"
                                   "font-weight:400;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.foldername_cb = QtWidgets.QComboBox(self.widget_5)
        self.foldername_cb.setMinimumSize(QtCore.QSize(185, 40))
        self.foldername_cb.setMaximumSize(QtCore.QSize(185, 16777215))
        self.foldername_cb.setStyleSheet("#foldername_cb {\n"
                                         "        border-radius: 10px;\n"
                                         "font-size:12px;"
                                         "font-weight:400;\n"
                                         "        font-family: Arial;\n"
                                         "        color:rgb(144, 115, 87);"
                                         "        border: 2px solid #aaa;\n"
                                         "        padding: 2px;\n"
                                         "padding-left:20px;\n"
                                         "    }\n"
                                         "\n"
                                         "#foldername_cb::drop-down{\n"
                                         " image:url(images/arrowdown.png);\n"
                                         "margin:10px;\n"
                                         "width: 15px;\n"
                                         "height: 15px;\n"
                                         "}\n"
                                         "#foldername_cb::drop-down::pressed{\n"
                                         " image:url(images/arrowup.png);\n"
                                         "margin:10px;\n"
                                         "width: 15px;\n"
                                         "height: 15px;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         "#foldername_cb QAbstractItemView {\n"
                                         "background-color: rgb(228,233,237);\n"
                                         "margin-top:5px;"
                                         "outline: none;\n"
                                         "color:rgb(144, 115, 87);"
                                         "border-radius: 5px;\n"
                                         " text-align: center;}\n"

                                         "\n"
                                         "#foldername_cb QAbstractItemView::item {\n"
                                         " color: #4A3B28;\n"
                                         "color:rgb(144, 115, 87);"
                                         " text-align: center;\n"
                                         "min-height: 10px; min-width: 10px;\n"
                                         " border:0px;}\n"
                                         "\n"
                                         "#foldername_cb QListView{\n"
                                         "border: none;\n"
                                         " font-weight:bold;\n"
                                         "color:rgb(144, 115, 87);"
                                         " text-align: center;}\n"
                                         "#foldername_cb QListView::item{border:0px;\n"
                                         "border-radius: 5px;\n"
                                         "  padding:8px; \n"
                                         "margin:5px;}\n"
                                         "#foldername_cb QListView::item:selected { \n"
                                         "color: white; \n"
                                         "background-color: #4A3B28}")
        self.foldername_cb.setObjectName("foldername_cb")
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, 'Projects.db')
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("SELECT folder_name FROM Location_Folder WHERE project_name = ?", (self.project_name,))
        rows = self.c.fetchall()

        delegate = QStyledItemDelegate(self.foldername_cb)
        self.foldername_cb.setItemDelegate(delegate)
        self.foldername_cb.setEditable(True)
        self.foldername_cb.lineEdit().setReadOnly(True)
        self.foldername_cb.lineEdit().setAlignment(Qt.AlignCenter)

        self.foldername_cb.setEditText("")
        for row in rows:
            self.foldername_cb.addItem(row[0])

        self.foldername_cb.activated.connect(self.show_widget)
        self.horizontalLayout_4.addWidget(self.foldername_cb)
        self.foldername_cb_btn = QtWidgets.QPushButton(self.widget_2)
        self.foldername_cb_btn.hide()
        self.foldername_cb_btn.setObjectName("foldername_cb_btn")
        self.foldername_cb_btn.setMinimumSize(QtCore.QSize(185, 40))
        self.foldername_cb_btn.setMaximumSize(QtCore.QSize(185, 16777215))
        self.foldername_cb_btn.setStyleSheet("#foldername_cb_btn{\n"
                                             "background-color:\n"
                                             "rgb(144, 115, 87);\n"
                                             "font-size:12px;"
                                             "border-radius:10px;\n"
                                             "font-weight:400;\n"
                                             "color:white;\n"
                                             "}\n"
                                             "#foldername_cb_btn::hover{\n"
                                             "background-color:\n"
                                             "white;\n"
                                             "border:2px solid rgb(144, 115, 87);\n"
                                             "color:rgb(144, 115, 87);\n"
                                             "}")
        self.horizontalLayout_4.addWidget(self.foldername_cb_btn)

        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.hide()
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_9 = QtWidgets.QWidget(self.widget_6)
        self.widget_9.setMinimumSize(QtCore.QSize(185, 0))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_5.addWidget(self.widget_9)
        self.rename_fold_LE = QtWidgets.QLineEdit(self.widget_6)
        self.rename_fold_LE.setPlaceholderText("Enter new name here")
        self.rename_fold_LE.setMinimumSize(QtCore.QSize(185, 40))
        self.rename_fold_LE.setMaximumSize(QtCore.QSize(185, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rename_fold_LE.setFont(font)
        self.rename_fold_LE.setStyleSheet("        border-radius: 10px;\n"
                                          "        font-size: 12px;\n"
                                          "        font-family: Arial;\n"

                                          "font-weight:400;"
                                          "        color:rgb(144, 115, 87);"
                                          "        background-color: #fff;\n"
                                          "        border: 2px solid #aaa;\n"
                                          "        padding: 2px;\n")
        self.rename_fold_LE.setObjectName("rename_fold_LE")
        self.rename_fold_LE.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_5.addWidget(self.rename_fold_LE)
        self.save_fold = QtWidgets.QPushButton("Save Changes", self.widget_6)
        self.save_fold.setMinimumSize(QtCore.QSize(130, 40))
        self.save_fold.setMaximumSize(QtCore.QSize(8899, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.save_fold.setFont(font)
        self.save_fold.clicked.connect(self.rename_folder)
        self.save_fold.setStyleSheet("#save_fold{\n"
                                     "background-color:\n"
                                     "#4a93d6;\n"
                                     "border-radius:10px;\n"
                                     "font-size:12px;"
                                     "font-weight:400;\n"
                                     "color:white;\n"
                                     "}\n"
                                     "#save_fold::hover{\n"
                                     "background-color:\n"
                                     "white;\n"
                                     "border:2px solid #4a93d6;\n"
                                     "color:#4a93d6;\n"
                                     "}")
        self.save_fold.setObjectName("save_fold")
        self.horizontalLayout_5.addWidget(self.save_fold)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel("<html><head/><body><p align=\"center\">Delete Folder</p></body></html>",
                                        self.widget_3)
        self.label_4.setFixedSize(QtCore.QSize(185, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
                                   "background-color:#fff3f3;\n"
                                   "border: 1px solid #ff8889;\n"
                                   "border-radius:10px;\n"
                                   "font-size:12px;"
                                   "font-weight:400;\n"
                                   "color:#ff8889;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.del_folder_cb = QtWidgets.QComboBox(self.widget_3)
        self.del_folder_cb.setMinimumSize(QtCore.QSize(185, 40))
        self.del_folder_cb.setMaximumSize(QtCore.QSize(185, 16777215))
        self.del_folder_cb.setStyleSheet("#del_folder_cb {\n"
                                         "        border-radius: 10px;\n"
                                         "font-size:12px;"
                                         "font-weight:400;\n"
                                         "        font-family: Arial;\n"
                                         "        color:rgb(144, 115, 87);"
                                         "        border: 2px solid #aaa;\n"
                                         "        padding: 2px;\n"
                                         "padding-left:20px;\n"
                                         "    }\n"
                                         "\n"
                                         "#del_folder_cb::drop-down{\n"
                                         " image:url(images/arrowdown.png);\n"
                                         "margin:10px;\n"
                                         "width: 15px;\n"
                                         "height: 15px;\n"
                                         "}\n"
                                         "#del_folder_cb::drop-down::pressed{\n"
                                         " image:url(images/arrowup.png);\n"
                                         "margin:10px;\n"
                                         "width: 15px;\n"
                                         "height: 15px;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         "#del_folder_cb QAbstractItemView {\n"
                                         "background-color: rgb(228,233,237);\n"
                                         "margin-top:5px;"
                                         "outline: none;\n"
                                         "color:rgb(144, 115, 87);"
                                         "border-radius: 5px;\n"
                                         " text-align: center;}\n"

                                         "\n"
                                         "#del_folder_cb QAbstractItemView::item {\n"
                                         " color: #4A3B28;\n"
                                         "color:rgb(144, 115, 87);"
                                         " text-align: center;\n"
                                         "min-height: 10px; min-width: 10px;\n"
                                         " border:0px;}\n"
                                         "\n"
                                         "#del_folder_cb QListView{\n"
                                         "border: none;\n"
                                         " font-weight:bold;\n"
                                         "color:rgb(144, 115, 87);"
                                         " text-align: center;}\n"
                                         "#del_folder_cb QListView::item{border:0px;\n"
                                         "border-radius: 5px;\n"
                                         "  padding:8px; \n"
                                         "margin:5px;}\n"
                                         "#del_folder_cb QListView::item:selected { \n"
                                         "color: white; \n"
                                         "background-color: #4A3B28}")
        self.del_folder_cb.setObjectName("del_folder_cb")
        delegate = QStyledItemDelegate(self.del_folder_cb)
        self.del_folder_cb.setItemDelegate(delegate)
        self.del_folder_cb.setEditable(True)
        self.del_folder_cb.lineEdit().setReadOnly(True)
        self.del_folder_cb.lineEdit().setAlignment(Qt.AlignCenter)
        for row in rows:
            self.del_folder_cb.addItem(row[0])
        self.del_folder_cb.activated.connect(self.show_del_button)
        self.horizontalLayout_6.addWidget(self.del_folder_cb)
        self.del_folder_cb_btn = QtWidgets.QPushButton(self.widget_2)
        self.del_folder_cb_btn.hide()
        self.del_folder_cb_btn.setObjectName("del_folder_cb_btn")
        self.del_folder_cb_btn.setMinimumSize(QtCore.QSize(185, 40))
        self.del_folder_cb_btn.setMaximumSize(QtCore.QSize(185, 16777215))
        self.del_folder_cb_btn.setStyleSheet("#del_folder_cb_btn{\n"
                                             "background-color:\n"
                                             "rgb(144, 115, 87);\n"
                                             "border-radius:10px;\n"
                                             "font-size:12px;"
                                             "font-weight:400;\n"
                                             "color:white;\n"
                                             "}\n"
                                             "#del_folder_cb_btn::hover{\n"
                                             "background-color:\n"
                                             "white;\n"
                                             "border:2px solid rgb(144, 115, 87);\n"
                                             "color:rgb(144, 115, 87);\n"
                                             "}")
        self.horizontalLayout_6.addWidget(self.del_folder_cb_btn)
        self.del_fold = QtWidgets.QPushButton("Delete", self.widget_3)
        self.del_fold.setMinimumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.del_fold.setFont(font)
        self.del_fold.setStyleSheet("#del_fold{\n"
                                    "background-color:\n"
                                    "#FF7B7B;\n"
                                    "border-radius:10px;\n"
                                    "font-size:12px;"
                                    "font-weight:400;\n"
                                    "color:white;\n"
                                    "}\n"
                                    "#del_fold::hover{\n"
                                    "background-color:\n"
                                    "white;\n"
                                    "border:2px solid #FF7B7B;\n"
                                    "color:#FF7B7B;\n"
                                    "}")
        self.del_fold.setObjectName("del_fold")
        if self.foldername_cb.count() == 0:
            print("Combobox is empty")
        else:
            self.del_fold.clicked.connect(self.confirm_delete)
        self.horizontalLayout_6.addWidget(self.del_fold)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_10 = QtWidgets.QWidget(self.widget_4)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_7.addWidget(self.widget_10)
        self.del_proj = QtWidgets.QPushButton("Delete current project", self.widget_4)
        self.del_proj.setMinimumSize(QtCore.QSize(185, 40))
        self.del_proj.setMaximumSize(QtCore.QSize(40, 16777215))
        self.del_proj.setStyleSheet("#del_proj{\n"
                                    "background-color:\n"
                                    "#FF7B7B;\n"
                                    "border-radius:10px;\n"
                                    "font-size:12px;"
                                    "font-weight:400;\n"
                                    "color:white;\n"
                                    "}\n"
                                    "#del_proj::hover{\n"
                                    "background-color:\n"
                                    "white;\n"
                                    "border:2px solid #FF7B7B;\n"
                                    "color:#FF7B7B;\n"
                                    "}")
        self.del_proj.setObjectName("del_proj")
        self.del_proj.clicked.connect(self.confirm_delete_project)
        self.horizontalLayout_7.addWidget(self.del_proj)
        self.back = QtWidgets.QPushButton("Back", self.widget_4)
        self.back.setMinimumSize(QtCore.QSize(100, 40))
        self.back.setMaximumSize(QtCore.QSize(10, 16777215))
        self.back.setStyleSheet("#back{\n"
                                "background-color:\n"
                                "#6A6D72;\n"
                                "border-radius:10px;\n"
                                "font-size:12px;"
                                "font-weight:400;\n"
                                "color:white;\n"
                                "}\n"
                                "#back::hover{\n"
                                "background-color:\n"
                                "white;\n"
                                "border:2px solid #6A6D72;\n"
                                "color:#6A6D72;\n"
                                "}")
        self.back.setObjectName("back")
        self.back.clicked.connect(self.Manage_Folder_Dialog.close)
        self.back.clicked.connect(self.bg_widget.hide)
        self.horizontalLayout_7.addWidget(self.back)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def show_widget(self):
        self.widget_6.show()
        self.foldername_cb.hide()
        self.foldername_cb_btn.show()
        selected_fold = self.foldername_cb.currentIndex()
        if selected_fold == -1 and self.foldername_cb.count() == 1:
            selected_fold = 0
        if selected_fold == -1:
            self.foldername_cb.setCurrentIndex(0)
            selected_fold = 0

        selected_text_fold = self.foldername_cb.itemText(selected_fold)
        self.foldername_cb_btn.setText(selected_text_fold)
        self.foldername_cb_btn.clicked.connect(self.show_folder_cb)

    def show_folder_cb(self):
        self.foldername_cb.show()
        self.foldername_cb_btn.hide()

    def show_del_button(self):
        self.del_folder_cb.hide()
        self.del_folder_cb_btn.show()
        selected_fold = self.del_folder_cb.currentIndex()
        if selected_fold == -1 and self.del_folder_cb.count() == 1:
            selected_fold = 0
        if selected_fold == -1:
            self.del_folder_cb.setCurrentIndex(0)
            selected_fold = 0

        selected_text_fold = self.del_folder_cb.itemText(selected_fold)
        self.del_folder_cb_btn.setText(selected_text_fold)
        self.del_folder_cb_btn.clicked.connect(self.show_del_cb)

    def show_del_cb(self):
        self.del_folder_cb.show()
        self.del_folder_cb_btn.hide()

    def delete_fold_function(self):
        selected_fold = self.del_folder_cb.currentIndex()
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, 'Projects.db')
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        try:
            if selected_fold == -1:
                self.del_folder_cb.setCurrentIndex(0)
                selected_fold = 0
            selected_text_fold = self.del_folder_cb.itemText(selected_fold)

            if self.table_exists(self.c, 'Location_Folder'):
                self.c.execute("DELETE FROM Location_Folder WHERE folder_name=?",
                               (selected_text_fold,))
            if self.table_exists(self.c, 'Save_Files'):
                self.c.execute("DELETE FROM Save_Files WHERE folder_name=?",
                               (selected_text_fold,))

            self.widget_6.hide()
            self.foldername_cb.clear()
            self.del_folder_cb.clear()
            self.del_folder_cb.show()
            self.del_folder_cb_btn.hide()
            self.c.execute("SELECT folder_name FROM Location_Folder WHERE project_name = ?", (self.project_name,))
            rows = self.c.fetchall()
            for row in rows:
                self.del_folder_cb.addItem(row[0])
                self.foldername_cb.addItem(row[0])

            self.conn.commit()
            self.conn.close()
            self.clear_layout(self.scroll_widget.layout())
            self.clear_btn.clear()
            self.fetch_folders_of_projects()
            self.closeDialog.close()

        except Exception as e:
            print(e)

    def confirm_delete(self):
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
        self.message.setText("Are you sure you want to delete this folder?")
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
        self.Yes.clicked.connect(self.delete_fold_function)
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

    def confirm_delete_project(self):
        closeDialog = QDialog()
        self.closeDialog_proj = closeDialog
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
        self.message.setText("Are you sure you want to delete this project?")
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
        self.Yes.clicked.connect(closeDialog.close)
        self.Yes.setMinimumSize(QtCore.QSize(20, 32))
        self.Yes.setMaximumSize(QtCore.QSize(100, 32))
        self.Yes.clicked.connect(self.delete_project)
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

    def delete_project(self):
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, 'Projects.db')
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        try:
            if self.table_exists(self.c, "Projects"):
                self.c.execute("DELETE FROM Projects WHERE project_name = ?", (self.project_name,))
            if self.table_exists(self.c, "Location_Folder"):
                self.c.execute("DELETE FROM Location_Folder WHERE project_name = ?", (self.project_name,))
            if self.table_exists(self.c, "Save_Files"):
                self.c.execute("DELETE FROM Save_Files WHERE project_name = ?", (self.project_name,))
            self.conn.commit()
            self.Manage_Folder_Dialog.close()
            self.bg_widget.hide()

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

        except Exception as e:
            print(e)

    def rename_folder(self):
        selected_fold = self.foldername_cb.currentIndex()
        new_fold_name = self.rename_fold_LE.text()
        if selected_fold == -1 and self.foldername_cb.count() == 1:
            selected_fold = 0
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, 'Projects.db')
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        try:
            if selected_fold == -1:
                self.foldername_cb.setCurrentIndex(0)
                selected_fold = 0
            selected_text_fold = self.foldername_cb.itemText(selected_fold)

            if not new_fold_name:
                print("New folder name is empty.")
            else:
                if self.table_exists(self.c, 'Location_Folder'):
                    self.c.execute("UPDATE Location_Folder SET folder_name=? WHERE folder_name=?",
                                   (new_fold_name, selected_text_fold))
                if self.table_exists(self.c, 'Save_Files'):
                    self.c.execute("UPDATE Save_Files SET folder_name=? WHERE folder_name=?",
                                   (new_fold_name, selected_text_fold))

                self.widget_6.hide()
                self.foldername_cb.clear()
                self.del_folder_cb.clear()
                self.foldername_cb_btn.setText(new_fold_name)
                self.c.execute("SELECT folder_name FROM Location_Folder WHERE project_name = ?", (self.project_name,))
                rows = self.c.fetchall()
                print(rows)
                for row in rows:
                    self.foldername_cb.addItem(row[0])
                    self.del_folder_cb.addItem(row[0])

            self.conn.commit()
            self.conn.close()
            self.clear_layout(self.scroll_widget.layout())
            self.clear_btn.clear()
            self.fetch_folders_of_projects()

        except Exception as e:
            print(e)

    def table_exists(self, cursor, table_name):
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, 'Projects.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return c.fetchone() is not None

    def save_proj_new_name(self):

        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            db_path = os.path.join(dir_path, 'Projects.db')
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            self.input_rename = self.rename_proj_LE.text()
            if not self.input_rename:
                print("New folder name is empty.")
            else:
                if self.table_exists(self.c, 'Projects'):
                    self.c.execute("UPDATE Projects SET project_name=? WHERE project_name=?",
                                   (self.input_rename, self.project_name))

                if self.table_exists(self.c, 'Location_Folder'):
                    self.c.execute("UPDATE Location_Folder SET project_name=? WHERE project_name=?",
                                   (self.input_rename, self.project_name))

                if self.table_exists(self.c, 'Save_Files'):
                    self.c.execute("UPDATE Save_Files SET project_name=? WHERE project_name=?",
                                   (self.input_rename, self.project_name))

                with open('selected_project.txt', 'w') as f:
                    f.write(self.input_rename)

            self.conn.commit()

            # self.project_name_lbl.setText(self.input_rename)
            self.myProjects.clear()
            self.c.execute("SELECT project_name FROM Projects ORDER BY created_at DESC")
            rows = self.c.fetchall()
            for row in rows:
                self.myProjects.addItem(row[0])
                self.myProjects.setEditText("My Projects")
            self.project_name_lbl.setText(self.input_rename)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = mng_folder()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
