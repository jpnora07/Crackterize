
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 542)
        MainWindow.setStyleSheet("#MainWindow{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "width: fit-content;\n"
                                 "                                heigth: fit-content;\n"
                                 "                                 block-size: fit-content;\n"
                                 "} ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.045, y1:0.261, x2:0.988636, y2:0.955, stop:0 rgba(235, 209, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                         "width: fit-content;\n"
                                         "                                heigth: fit-content;\n"
                                         "                                 block-size: fit-content;\n"
                                         "} ")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(764, 89))
        self.widget_2.setMaximumSize(QtCore.QSize(764, 89))
        self.widget_2.setStyleSheet("#widget_2 {\n"
                                    "border-image:url(images/Crackterize.png) 200 -350 190 100 stretch stretch;\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.loccrack = QtWidgets.QLabel(self.widget_7)
        self.loccrack.setStyleSheet("#loccrack {\n"
                                    "    font: 700 9pt \"Franklin Gothic Medium\";\n"
                                    "    font: 600 9pt \"Franklin Gothic Medium\";\n"
                                    "position: absolute;\n"
                                    "width: 50px;\n"
                                    "height: 50px;\n"
                                    "left: 143px;\n"
                                    "top: 236px;\n"
                                    "\n"
                                    "font-family: \'Franklin Gothic Medium\';\n"
                                    "font-style: normal;\n"
                                    "font-weight: 600;\n"
                                    "font-size: 20px;\n"
                                    "line-height: 42px;\n"
                                    "text-align: center;\n"
                                    "\n"
                                    "color: \n"
                                    "#664323;\n"
                                    "}")
        self.loccrack.setObjectName("loccrack")
        self.verticalLayout_4.addWidget(self.loccrack)
        self.cracktype = QtWidgets.QLabel(self.widget_7)
        self.cracktype.setStyleSheet("#cracktype {\n"
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
                                     "font-size: 20px;\n"
                                     "line-height: 42px;\n"
                                     "text-align: center;\n"
                                     "\n"
                                     "color: \n"
                                     "#664323;\n"
                                     "}")
        self.cracktype.setObjectName("cracktype")
        self.verticalLayout_4.addWidget(self.cracktype)
        self.crackprogression = QtWidgets.QLabel(self.widget_7)
        self.crackprogression.setStyleSheet("#crackprogression {\n"
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
                                            "font-size: 20px;\n"
                                            "line-height: 42px;\n"
                                            "text-align: center;\n"
                                            "\n"
                                            "color: \n"
                                            "#664323;\n"
                                            "}")
        self.crackprogression.setObjectName("crackprogression")
        self.verticalLayout_4.addWidget(self.crackprogression)
        self.horizontalLayout.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setContentsMargins(-1, -1, 150, -1)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.loc_box = QtWidgets.QComboBox(self.widget_8)
        self.loc_box.setMaximumSize(QtCore.QSize(396, 41))
        self.loc_box.setAutoFillBackground(False)
        self.loc_box.setStyleSheet("#loc_box {\n"
                                   "        border-radius: 10px;\n"
                                   "        font-size: 18px;\n"
                                   "        font-family: Arial;\n"
                                   "        color: #333;\n"
                                   "        background-color: #fff;\n"
                                   "        border: 2px solid #aaa;\n"
                                   "        padding: 10px;\n"
                                   "    }\n"
                                   "\n"
                                   "                                      #loc_box::drop-down{\n"
                                   "                                      image:url(images/arrowdown.png);\n"
                                   "                                      width: 20px;\n"
                                   "                                      height: 20px;\n"
                                   "        padding: 8px;\n"
                                   "                                      }\n"
                                   "                                      #loc_box::drop-down::pressed{\n"
                                   "                                      image:url(images/arrowup.png);\n"
                                   "                                      width: 20px;\n"
                                   "                                      height: 20px;\n"
                                   "                                      text-align: center;\n"
                                   "                                      }\n"
                                   "\n"
                                   "                                      #loc_box QAbstractItemView {\n"
                                   "                                      background-color: rgb(255, 255, 255);\n"
                                   "                                      outline: none;\n"
                                   "                                      text-align: center;}\n"
                                   "\n"
                                   "                                      #loc_box QAbstractItemView::item {\n"
                                   "                                      background-color: #F4EBE6;\n"
                                   "                                      color: #4A3B28;\n"
                                   "                                      text-align: center;\n"
                                   "                                      min-height: 35px; min-width: 50px;\n"
                                   "                                      border:0px;}\n"
                                   "\n"
                                   "                                      #loc_box QListView{\n"
                                   "                                      border: none;\n"
                                   "                                      font-weight:bold;\n"
                                   "                                      text-align: center;}\n"
                                   "\n"
                                   "                                      #loc_box QListView::item{\n"
                                   "                                      border:0px;\n"
                                   "                                      border-radius: 15px;\n"
                                   "                                      padding:8px; \n"
                                   "                                      margin:5px;}\n"
                                   "                                      \n"
                                   "\n"
                                   "                                      #loc_box QListView::item:selected { \n"
                                   "                                      color: white; \n"
                                   "                                      background-color: #4A3B28}")
        self.loc_box.setObjectName("loc_box")
        self.verticalLayout_5.addWidget(self.loc_box)
        self.type_box = QtWidgets.QComboBox(self.widget_8)
        self.type_box.setMaximumSize(QtCore.QSize(396, 41))
        self.type_box.setStyleSheet("#type_box {\n"
                                    "        border-radius: 10px;\n"
                                    "        font-size: 18px;\n"
                                    "        font-family: Arial;\n"
                                    "        color: #333;\n"
                                    "        background-color: #fff;\n"
                                    "        border: 2px solid #aaa;\n"
                                    "        padding: 10px;\n"
                                    "    }\n"
                                    "\n"
                                    "                                      #type_box::drop-down{\n"
                                    "                                      image:url(images/arrowdown.png);\n"
                                    "                                      width: 20px;\n"
                                    "                                      height: 20px;\n"
                                    "        padding: 8px;\n"
                                    "                                      }\n"
                                    "                                      #type_box::drop-down::pressed{\n"
                                    "                                      image:url(images/arrowup.png);\n"
                                    "                                      width: 20px;\n"
                                    "                                      height: 20px;\n"
                                    "                                      text-align: center;\n"
                                    "                                      }\n"
                                    "\n"
                                    "                                      #type_box QAbstractItemView {\n"
                                    "                                      background-color: rgb(255, 255, 255);\n"
                                    "                                      outline: none;\n"
                                    "                                      text-align: center;}\n"
                                    "\n"
                                    "                                      #type_box QAbstractItemView::item {\n"
                                    "                                      background-color: #F4EBE6;\n"
                                    "                                      color: #4A3B28;\n"
                                    "                                      text-align: center;\n"
                                    "                                      min-height: 35px; min-width: 50px;\n"
                                    "                                      border:0px;}\n"
                                    "\n"
                                    "                                      #type_box QListView{\n"
                                    "                                      border: none;\n"
                                    "                                      font-weight:bold;\n"
                                    "                                      text-align: center;}\n"
                                    "\n"
                                    "                                      #type_box QListView::item{\n"
                                    "                                      border:0px;\n"
                                    "                                      border-radius: 15px;\n"
                                    "                                      padding:8px; \n"
                                    "                                      margin:5px;}\n"
                                    "                                      \n"
                                    "\n"
                                    "                                      #type_box QListView::item:selected { \n"
                                    "                                      color: white; \n"
                                    "                                      background-color: #4A3B28}")
        self.type_box.setObjectName("type_box")
        self.verticalLayout_5.addWidget(self.type_box)
        self.progression_box = QtWidgets.QComboBox(self.widget_8)
        self.progression_box.setMaximumSize(QtCore.QSize(396, 41))
        self.progression_box.setStyleSheet("#progression_box {\n"
                                           "        border-radius: 10px;\n"
                                           "        font-size: 18px;\n"
                                           "        font-family: Arial;\n"
                                           "        color: #333;\n"
                                           "        background-color: #fff;\n"
                                           "        border: 2px solid #aaa;\n"
                                           "        padding: 10px;\n"
                                           "    }\n"
                                           "\n"
                                           "                                      #progression_box::drop-down{\n"
                                           "                                      image:url(images/arrowdown.png);\n"
                                           "                                      width: 20px;\n"
                                           "                                      height: 20px;\n"
                                           "        padding: 8px;\n"
                                           "                                      }\n"
                                           "                                      #progression_box::drop-down::pressed{\n"
                                           "                                      image:url(images/arrowup.png);\n"
                                           "                                      width: 20px;\n"
                                           "                                      height: 20px;\n"
                                           "                                      text-align: center;\n"
                                           "                                      }\n"
                                           "\n"
                                           "                                      #progression_box QAbstractItemView {\n"
                                           "                                      background-color: rgb(255, 255, 255);\n"
                                           "                                      outline: none;\n"
                                           "                                      text-align: center;}\n"
                                           "\n"
                                           "                                      #progression_box QAbstractItemView::item {\n"
                                           "                                      background-color: #F4EBE6;\n"
                                           "                                      color: #4A3B28;\n"
                                           "                                      text-align: center;\n"
                                           "                                      min-height: 35px; min-width: 50px;\n"
                                           "                                      border:0px;}\n"
                                           "\n"
                                           "                                      #progression_box QListView{\n"
                                           "                                      border: none;\n"
                                           "                                      font-weight:bold;\n"
                                           "                                      text-align: center;}\n"
                                           "\n"
                                           "                                      #progression_box QListView::item{\n"
                                           "                                      border:0px;\n"
                                           "                                      border-radius: 15px;\n"
                                           "                                      padding:8px; \n"
                                           "                                      margin:5px;}\n"
                                           "                                      \n"
                                           "\n"
                                           "                                      #progression_box QListView::item:selected { \n"
                                           "                                      color: white; \n"
                                           "                                      background-color: #4A3B28}")
        self.progression_box.setObjectName("progression_box")
        self.verticalLayout_5.addWidget(self.progression_box)
        self.horizontalLayout.addWidget(self.widget_8)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.remarks = QtWidgets.QLabel(self.widget_3)
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
        self.verticalLayout_6.addWidget(self.remarks)
        self.notes = QtWidgets.QTextEdit(self.widget_3)
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
        self.verticalLayout_6.addWidget(self.notes)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.discard = QtWidgets.QPushButton(self.widget_6)
        self.discard.setStyleSheet("#discard{\n"
                                   " background-color: #6A6E72;\n"
                                   "            color: white;\n"
                                   "font: bold;\n"
                                   "            border-radius: 10px;\n"
                                   "            padding: 10px 20px;\n"
                                   "}")
        self.discard.setObjectName("discard")
        self.horizontalLayout_2.addWidget(self.discard)
        self.save1 = QtWidgets.QPushButton(self.widget_6)
        self.save1.setStyleSheet("#save1{\n"
                                 " background-color: #6F4B27;\n"
                                 "            color: white;\n"
                                 "font: bold;\n"
                                 "            border-radius: 10px;\n"
                                 "            padding: 10px 20px;\n"
                                 "}")
        self.save1.setObjectName("save1")
        self.horizontalLayout_2.addWidget(self.save1)
        self.print1 = QtWidgets.QPushButton(self.widget_6)
        self.print1.setStyleSheet("#print1{\n"
                                  " background-color: #2E74A9;\n"
                                  "            color: white;\n"
                                  "font: bold;\n"
                                  "            border-radius: 10px;\n"
                                  "            padding: 10px 20px;\n"
                                  "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/print_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print1.setIcon(icon)
        self.print1.setObjectName("print1")
        self.horizontalLayout_2.addWidget(self.print1)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loccrack.setText(_translate("MainWindow", "Location of Crack:"))
        self.cracktype.setText(_translate("MainWindow", "Crack Type:"))
        self.crackprogression.setText(_translate("MainWindow", "Crack Progression:"))
        self.loc_box.setPlaceholderText(_translate("MainWindow", "Select the location of crack"))
        self.type_box.setPlaceholderText(_translate("MainWindow", "Select the crack type"))
        self.progression_box.setPlaceholderText(_translate("MainWindow", "Select the crack progression"))
        self.remarks.setText(_translate("MainWindow", "Remarks:"))
        self.discard.setText(_translate("MainWindow", "Discard"))
        self.save1.setText(_translate("MainWindow", "Save"))
        self.print1.setText(_translate("MainWindow", "Print"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
