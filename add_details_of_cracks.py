from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 548)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_16 = QtWidgets.QWidget(Dialog)
        self.widget_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.widget_16)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        self.verticalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_4.addWidget(self.widget_16)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.WithLogo = QtWidgets.QWidget(self.widget_2)
        self.WithLogo.setMinimumSize(QtCore.QSize(564, 80))
        self.WithLogo.setMaximumSize(QtCore.QSize(564, 80))
        self.WithLogo.setStyleSheet("#WithLogo{border-image: url(images/Crackterize.png) 175 0 175 0 stretch;}")
        self.WithLogo.setObjectName("WithLogo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WithLogo)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addWidget(self.WithLogo)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loccrack = QtWidgets.QLabel(self.widget_6)
        self.loccrack.setMinimumSize(QtCore.QSize(200, 30))
        self.loccrack.setMaximumSize(QtCore.QSize(200, 30))
        self.loccrack.setStyleSheet("#loccrack {\n"
                                    "font-family: \'Franklin Gothic Medium\';\n"
                                    "font-size: 17px;\n"
                                    "color: \n"
                                    "#664323;\n"
                                    "}")
        self.loccrack.setObjectName("loccrack")
        self.horizontalLayout_4.addWidget(self.loccrack)
        self.loc_box = QtWidgets.QComboBox(self.widget_6)
        self.loc_box.setMaximumSize(QtCore.QSize(396, 35))
        self.loc_box.setAutoFillBackground(False)
        self.loc_box.setStyleSheet("#loc_box {\n"
                                   "        border-radius: 10px;\n"
                                   "        font-size: 18px;\n"
                                   "        font-family: Arial;\n"
                                   "        color: #333;\n"
                                   "        background-color: #fff;\n"
                                   "        border: 2px solid #aaa;\n"
                                   "        padding: 2px;\n"
                                   "padding-left:8px;\n"
                                   "    }\n"
                                   "\n"
                                   "#loc_box::drop-down{\n"
                                   " image:url(images/arrowdown.png);\n"
                                   " width: 15px;\n"
                                   " height: 15px;\n"
                                   "padding: 6px;\n"
                                   "}\n"
                                   "#loc_box::drop-down::pressed{\n"
                                   " image:url(images/arrowup.png);\n"
                                   "width: 15px;\n"
                                   " height: 15px;\n"
                                   "text-align: center;\n"
                                   "}\n"
                                   "#loc_box QAbstractItemView {\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "outline: none;\n"
                                   " text-align: center;}\n"
                                   "\n"
                                   "#loc_box QAbstractItemView::item {\n"
                                   "background-color: #F4EBE6;\n"
                                   " color: #4A3B28;\n"
                                   " text-align: center;\n"
                                   "min-height: 35px; min-width: 50px;\n"
                                   " border:0px;}\n"
                                   "\n"
                                   "#loc_box QListView{\n"
                                   "border: none;\n"
                                   " font-weight:bold;\n"
                                   " text-align: center;}\n"
                                   "#loc_box QListView::item{border:0px;\n"
                                   "border-radius: 15px;\n"
                                   "  padding:8px; \n"
                                   "margin:5px;}\n"
                                   "#loc_box QListView::item:selected { \n"
                                   "color: white; \n"
                                   "background-color: #4A3B28}")
        self.loc_box.setObjectName("loc_box")
        self.loc_box.addItems(["Vertical Crack/s on Wall","Horizontal Crack/s on Wall","Corner Crack/s", "Crack/s at the Beam Column Junction",
                               "Crack/s on Column", "Crack/s on Slabs", "Crack/s on Slab Foundation", "Crack/s on Foundation",
                               "Crack/s on Pavement"])
        self.loc_box.currentIndexChanged.connect(self.location_function)
        self.horizontalLayout_4.addWidget(self.loc_box)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cracktype = QtWidgets.QLabel(self.widget_7)
        self.cracktype.setMinimumSize(QtCore.QSize(200, 30))
        self.cracktype.setMaximumSize(QtCore.QSize(200, 30))
        self.cracktype.setStyleSheet("#cracktype {\n"
                                     "font-family: \'Franklin Gothic Medium\';\n"
                                     "font-size: 17px;\n"
                                     "color: \n"
                                     "#664323;\n"
                                     "}")
        self.cracktype.setObjectName("cracktype")
        self.horizontalLayout_5.addWidget(self.cracktype)
        self.type_box = QtWidgets.QComboBox(self.widget_7)
        self.type_box.setMaximumSize(QtCore.QSize(396, 41))
        self.type_box.setStyleSheet("#type_box {\n"
                                    "        border-radius: 10px;\n"
                                    "        font-size: 18px;\n"
                                    "        font-family: Arial;\n"
                                    "        color: #333;\n"
                                    "        background-color: #fff;\n"
                                    "        border: 2px solid #aaa;\n"
                                    "        padding: 2px;\n"
                                    "padding-left:8px;\n"
                                    "    }\n"
                                    "\n"
                                    "#type_box::drop-down{\n"
                                    " image:url(images/arrowdown.png);\n"
                                    " width: 15px;\n"
                                    " height: 15px;\n"
                                    "padding: 6px;\n"
                                    "}\n"
                                    "#type_box::drop-down::pressed{\n"
                                    " image:url(images/arrowup.png);\n"
                                    "width: 15px;\n"
                                    " height: 15px;\n"
                                    "text-align: center;\n"
                                    "}\n"
                                    "#type_box QAbstractItemView {\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "outline: none;\n"
                                    " text-align: center;}\n"
                                    "\n"
                                    "#type_box QAbstractItemView::item {\n"
                                    "background-color: #F4EBE6;\n"
                                    " color: #4A3B28;\n"
                                    " text-align: center;\n"
                                    "min-height: 35px; min-width: 50px;\n"
                                    " border:0px;}\n"
                                    "\n"
                                    "#type_box QListView{\n"
                                    "border: none;\n"
                                    " font-weight:bold;\n"
                                    " text-align: center;}\n"
                                    "#type_box QListView::item{border:0px;\n"
                                    "border-radius: 15px;\n"
                                    "  padding:8px; \n"
                                    "margin:5px;}\n"
                                    "#type_box QListView::item:selected { \n"
                                    "color: white; \n"
                                    "background-color: #4A3B28}")
        self.type_box.setObjectName("type_box")
        self.type_box.addItems(["Drying Shrinkage Crack/s","Thermal Crack/s", "Structural Crack/s", "Settlement Crack/s",
                                "Corrosion Induced Crack/s", "Alkali-Silica Reaction", "Heaving Crack/s", "Overloading Crack/s",
                                "Joint Crack/s"])
        self.type_box.currentIndexChanged.connect(self.type_function)
        self.horizontalLayout_5.addWidget(self.type_box)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.crackprogression = QtWidgets.QLabel(self.widget_8)
        self.crackprogression.setMinimumSize(QtCore.QSize(200, 30))
        self.crackprogression.setMaximumSize(QtCore.QSize(200, 30))
        self.crackprogression.setStyleSheet("#crackprogression {\n"
                                            "font-family: \'Franklin Gothic Medium\';\n"
                                            "font-size: 17px;\n"
                                            "color: \n"
                                            "#664323;\n"
                                            "}")
        self.crackprogression.setObjectName("crackprogression")
        self.horizontalLayout_6.addWidget(self.crackprogression)
        self.progression_box = QtWidgets.QComboBox(self.widget_8)
        self.progression_box.setMaximumSize(QtCore.QSize(396, 41))
        self.progression_box.setStyleSheet("#progression_box {\n"
                                           "        border-radius: 10px;\n"
                                           "        font-size: 18px;\n"
                                           "        font-family: Arial;\n"
                                           "        color: #333;\n"
                                           "        background-color: #fff;\n"
                                           "        border: 2px solid #aaa;\n"
                                           "        padding: 2px;\n"
                                           "padding-left:8px;\n"
                                           "    }\n"
                                           "\n"
                                           "#progression_box::drop-down{\n"
                                           " image:url(images/arrowdown.png);\n"
                                           " width: 15px;\n"
                                           " height: 15px;\n"
                                           "padding: 6px;\n"
                                           "}\n"
                                           "#progression_box::drop-down::pressed{\n"
                                           " image:url(images/arrowup.png);\n"
                                           "width: 15px;\n"
                                           " height: 15px;\n"
                                           "text-align: center;\n"
                                           "}\n"
                                           "#progression_box QAbstractItemView {\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "outline: none;\n"
                                           " text-align: center;}\n"
                                           "\n"
                                           "#progression_box QAbstractItemView::item {\n"
                                           "background-color: #F4EBE6;\n"
                                           " color: #4A3B28;\n"
                                           " text-align: center;\n"
                                           "min-height: 35px; min-width: 50px;\n"
                                           " border:0px;}\n"
                                           "\n"
                                           "#progression_box QListView{\n"
                                           "border: none;\n"
                                           " font-weight:bold;\n"
                                           " text-align: center;}\n"
                                           "#progression_box QListView::item{border:0px;\n"
                                           "border-radius: 15px;\n"
                                           "  padding:8px; \n"
                                           "margin:5px;}\n"
                                           "#progression_box QListView::item:selected { \n"
                                           "color: white; \n"
                                           "background-color: #4A3B28}")
        self.progression_box.addItems(["Fatigue Crack/s", "Environmental Crack/s", "Creep Crack Growth",
                                       "Overload Crack Growth", "Thermal Fatigue Crack Growth", "Corrosion Fatigue Crack Growth",
                                       "Stress Corrosion Cracking","Hydrogen Embrittlement", "Wear-Induced Crack Growth"])
        self.progression_box.setObjectName("progression_box")
        self.progression_box.currentIndexChanged.connect(self.progression_function)
        self.horizontalLayout_6.addWidget(self.progression_box)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.remarks = QtWidgets.QLabel(self.widget_4)
        self.remarks.setStyleSheet("#remarks {\n"
                                   "    font: 700 9pt \"Segoe UI\";\n"
                                   "    font: 700 9pt \"Segoe UI\";\n"
                                   "    font: 600 9pt \"Segoe UI\";\n"
                                   "position: absolute;\n"
                                   "width: 50px;\n"
                                   "height: 50px;\n"
                                   "left: 143px;\n"
                                   "top: 236px;\n"
                                   "\n"
                                   "font-family: \'Franklin Gothic Medium\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 600;\n"
                                   "font-size: 15px;\n"
                                   "line-height: 42px;\n"
                                   "text-align: center;\n"
                                   "\n"
                                   "color: \n"
                                   "#664323;\n"
                                   "}")
        self.remarks.setIndent(10)
        self.remarks.setObjectName("remarks")
        self.verticalLayout_3.addWidget(self.remarks)
        self.notes = QtWidgets.QTextEdit(self.widget_4)
        self.notes.setStyleSheet("#notes {\n"
                                 "        border-radius: 10px;\n"
                                 "        font-size: 18px;\n"
                                 "        font-family: Arial;\n"
                                 "        color: #333;\n"
                                 "        background-color: #fff;\n"
                                 "        border: 2px solid #aaa;\n"
                                 "        padding: 10px;\n"
                                 "    }")
        self.notes.setObjectName("notes")
        self.verticalLayout_3.addWidget(self.notes)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.savebtn = QtWidgets.QPushButton(self.widget_5)
        self.savebtn.setMinimumSize(QtCore.QSize(0, 35))
        self.savebtn.setMaximumSize(QtCore.QSize(100, 35))
        self.savebtn.setStyleSheet("#savebtn{\n"
                                   "background: #2E74A9;\n"
                                   "font-weight:bold;\n"
                                   "color: white;\n"
                                   "border-radius: 7px;\n"
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
        self.savebtn.clicked.connect(self.add_to_text_file)
        self.horizontalLayout_7.addWidget(self.savebtn)
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loccrack.setText(_translate("Dialog", "Location of Crack:"))
        self.loc_box.setPlaceholderText(_translate("Dialog", "Select the location of crack"))
        self.cracktype.setText(_translate("Dialog", "Crack Type:"))
        self.type_box.setPlaceholderText(_translate("Dialog", "Select the crack type"))
        self.crackprogression.setText(_translate("Dialog", "Crack Progression:"))
        self.progression_box.setPlaceholderText(_translate("Dialog", "Select the crack progression"))
        self.remarks.setText(_translate("Dialog", "Remarks:"))
        self.savebtn.setText(_translate("Dialog", "Save"))

    def location_function(self, index):
        self.selected_loc = self.loc_box.itemText(index)
        print(self.selected_loc)

    def type_function(self, index):
        self.selected_type = self.type_box.itemText(index)
        print(self.selected_type)

    def progression_function(self, index):
        self.selected_prog = self.progression_box.itemText(index)
        print(self.selected_prog)

    def add_to_text_file(self):
        try:
            with open('Selected_location_crack.txt', 'w') as f:
                f.write(self.selected_loc)
        except AttributeError:
            QMessageBox.critical(Dialog, "Error", "Please select location of crack.")
        try:
            with open('Selected_type_crack.txt', 'w') as f:
                f.write(self.selected_type)
        except AttributeError:
            QMessageBox.critical(Dialog, "Error", "Please select type of crack.")
        try:
            with open('Selected_progression_crack.txt', 'w') as f:
                f.write(self.selected_prog)
        except AttributeError:
            QMessageBox.critical(Dialog, "Error", "Please select progression of crack.")
        try:
            with open('Remarks_written.txt', 'w') as f:
                f.write(self.notes.toPlainText())
        except AttributeError:
            QMessageBox.critical(Dialog, "Error", "Remarks cannot be empty.")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
