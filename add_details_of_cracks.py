import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


class add_details_dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(700, 600)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setStyleSheet("background-color:rgb(255,255,255);")
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
        self.WithLogo.setMinimumSize(QtCore.QSize(500, 80))
        self.WithLogo.setMaximumSize(QtCore.QSize(500, 80))
        self.WithLogo.setStyleSheet("#WithLogo{border-image: url(images/Crackterize.png) 400 0 400 0 stretch;}")
        self.WithLogo.setObjectName("WithLogo")
        self.horizontalLayout_2.addWidget(self.WithLogo)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WithLogo)

        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
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
                                    "  background-color: transparent;  \n"
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
                                   "color:rgb(144, 115, 87);"
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
                                   "color:rgb(144, 115, 87);"
                                   " text-align: center;}\n"
                                   "\n"
                                   "#loc_box QAbstractItemView::item {\n"
                                   "background-color: #F4EBE6;\n"
                                   " color: #4A3B28;\n"
                                   "color:rgb(144, 115, 87);"
                                   " text-align: center;\n"
                                   "min-height: 35px; min-width: 50px;\n"
                                   " border:0px;}\n"
                                   "\n"
                                   "#loc_box QListView{\n"
                                   "border: none;\n"
                                   " font-weight:bold;\n"
                                   "color:rgb(144, 115, 87);"
                                   " text-align: center;}\n"
                                   "#loc_box QListView::item{border:0px;\n"
                                   "border-radius: 15px;\n"
                                   "  padding:8px; \n"
                                   "margin:5px;}\n"
                                   "#loc_box QListView::item:selected { \n"
                                   "color: white; \n"
                                   "background-color: #4A3B28}")
        self.loc_box.setObjectName("loc_box")
        self.loc_box.setMaxVisibleItems(10)
        self.loc_box.addItems([
            "Balconies and decks",
            "Basements",
            "Bridges",
            "Ceilings",
            "Chimneys",
            "Concrete slabs",
            "Dams",
            "Electrical systems",
            "Exterior surfaces",
            "Fireplaces",
            "Floors",
            "Foundations",
            "Historic structures",
            "Parking structures",
            "Pavements",
            "Pipes and plumbing",
            "Retaining walls",
            "Roofs",
            "Silos",
            "Staircases",
            "Storage tanks",
            "Tunnels",
            "Walls",
            "Windows and doors"
        ])
        # self.loc_box.currentIndexChanged.connect(self.location_function)
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

                                     "  background-color: transparent;  \n"
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
                                    "color:rgb(144, 115, 87);"
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
                                    "color:rgb(144, 115, 87);"
                                    " text-align: center;}\n"
                                    "\n"
                                    "#type_box QAbstractItemView::item {\n"
                                    "background-color: #F4EBE6;\n"
                                    " color: #4A3B28;\n"
                                    "color:rgb(144, 115, 87);"
                                    " text-align: center;\n"
                                    "min-height: 35px; min-width: 50px;\n"
                                    " border:0px;}\n"
                                    "\n"
                                    "#type_box QListView{\n"
                                    "border: none;\n"
                                    " font-weight:bold;\n"
                                    "color:rgb(144, 115, 87);"
                                    " text-align: center;}\n"
                                    "#type_box QListView::item{border:0px;\n"
                                    "border-radius: 15px;\n"
                                    "  padding:8px; \n"
                                    "margin:5px;}\n"
                                    "#type_box QListView::item:selected { \n"
                                    "color: white; \n"
                                    "background-color: #4A3B28}")
        self.type_box.setObjectName("type_box")
        self.type_box.setMaxVisibleItems(10)
        self.type_box.addItems(
            ["Abrasion cracks", "Alkali-aggregate reaction (AAR) cracks", "Blistering cracks",
             "Chemical reaction cracks", "Construction joints", "Corner cracks", "Craze cracks", "Crazing cracks",
             "Diagonal cracks", "Drying shrinkage cracks", "Excessive load cracks", "Flexural cracks", "Impact cracks",
             "Inadequate curing cracks", "Joint reflection cracks", "Lateral cracks", "Overloading cracks",
             "Overlapping cracks", "Plastic shrinkage cracks", "Reflection cracks", "Scaling cracks",
             "Settlement cracks", "Shear cracks", "Shrinkage cracks", "Spalling cracks", "Structural cracks",
             "Temperature cracks", "Thermal cracks", "Vibration cracks"])
        # self.type_box.currentIndexChanged.connect(self.type_function)
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
                                            "  background-color: transparent;  \n"
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
                                           "color:rgb(144, 115, 87);"
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
                                           "color:rgb(144, 115, 87);"
                                           " text-align: center;}\n"
                                           "\n"
                                           "#progression_box QAbstractItemView::item {\n"
                                           "background-color: #F4EBE6;\n"
                                           " color: #4A3B28;\n"
                                           "color:rgb(144, 115, 87);"
                                           " text-align: center;\n"
                                           "min-height: 35px; min-width: 50px;\n"
                                           " border:0px;}\n"
                                           "\n"
                                           "#progression_box QListView{\n"
                                           "border: none;\n"
                                           " font-weight:bold;\n"
                                           "color:rgb(144, 115, 87);"
                                           " text-align: center;}\n"
                                           "#progression_box QListView::item{border:0px;\n"
                                           "border-radius: 15px;\n"
                                           "  padding:8px; \n"
                                           "margin:5px;}\n"
                                           "#progression_box QListView::item:selected { \n"
                                           "color: white; \n"
                                           "background-color: #4A3B28}")
        self.progression_box.addItems([
            'Buckling',
            'Convergence',
            'Corrosion',
            'Corrosion-induced cracking',
            'Creep rupture',
            'Delayed cracking',
            'Delamination',
            'Erosion',
            'Erosion or weathering cracks',
            'Fatigue cracking',
            'Frost heave cracks',
            'Intersecting',
            'Joint spalling',
            'Longitudinal cracking',
            'Mud cracking',
            'Network',
            'Pattern cracking',
            'Propagation',
            'Reinforcement corrosion',
            'Spalling',
            'Structural failure',
            'Thermal expansion and contraction cracks',
            'Transverse cracking',
            'Veining',
            'Water infiltration cracks'
        ])
        self.progression_box.setObjectName("progression_box")
        # self.progression_box.currentIndexChanged.connect(self.progression_function)
        self.horizontalLayout_6.addWidget(self.progression_box)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.remarks = QtWidgets.QLabel(self.widget_4)
        self.remarks.setStyleSheet("#remarks {\n"

                                   "  background-color: transparent;  \n"
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
        try:
            remark = 'Remarks_written.txt'
            if os.path.isfile(remark):
                with open(remark, 'r') as f:
                    self.input_txt = f.read()
                    self.notes.setText(self.input_txt)
        except Exception as e:
            print(e)
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

        self.reload_current_save()

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

    def add_to_text_file(self):

        selected_loc = self.loc_box.currentIndex()
        selected_type = self.type_box.currentIndex()
        selected_prog = self.progression_box.currentIndex()
        if selected_loc == -1:
            self.loc_box.setCurrentIndex(0)
            selected_loc = 0
        selected_text_loc = self.loc_box.itemText(selected_loc)

        if selected_type == -1:
            self.type_box.setCurrentIndex(0)
            selected_type = 0
        selected_text_type = self.type_box.itemText(selected_type)

        if selected_prog == -1:
            self.progression_box.setCurrentIndex(0)
            selected_prog = 0
        selected_text_prog = self.progression_box.itemText(selected_prog)

        with open('Selected_location_crack.txt', 'w') as f:
            f.write(selected_text_loc)

        with open('Selected_type_crack.txt', 'w') as f:
            f.write(selected_text_type)

        with open('Selected_progression_crack.txt', 'w') as f:
            f.write(selected_text_prog)

        with open('Remarks_written.txt', 'w') as f:
            f.write(self.notes.toPlainText())

        self.Dialog.close()

    def reload_current_save(self):
        try:
            selected_loc = 'Selected_location_crack.txt'
            if os.path.isfile(selected_loc):
                with open(selected_loc, 'r') as f:
                    selected_text1 = f.read().strip()
                    for index1 in range(self.loc_box.count()):
                        if self.loc_box.itemText(index1) == selected_text1:
                            self.loc_box.setCurrentIndex(index1)
                            break
        except Exception as e:
            print(e)

        try:
            selected_type = 'Selected_type_crack.txt'
            if os.path.isfile(selected_type):
                with open(selected_type, 'r') as f:
                    selected_text2 = f.read().strip()
                    for index2 in range(self.type_box.count()):
                        if self.type_box.itemText(index2) == selected_text2:
                            self.type_box.setCurrentIndex(index2)
                            break
        except Exception as e:
            print(e)

        try:
            selected_prog = 'Selected_progression_crack.txt'
            if os.path.isfile(selected_prog):
                with open(selected_prog, 'r') as f:
                    selected_text = f.read().strip()
                    for index in range(self.progression_box.count()):
                        if self.progression_box.itemText(index) == selected_text:
                            self.progression_box.setCurrentIndex(index)
                            break
        except Exception as e:
            print(e)
