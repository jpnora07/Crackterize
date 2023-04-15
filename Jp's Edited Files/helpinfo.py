
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class how_to_use(object):
    def __init__(self, background_widget):
        self.background_widget = background_widget
    def setupUi(self, Dialog):
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
        self.label_11.setPixmap(QtGui.QPixmap("../images/Ilagan.png"))
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
        self.label_12.setPixmap(QtGui.QPixmap("../images/Maiquez.png"))
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
        self.label_13.setPixmap(QtGui.QPixmap("../images/Narvaez.png"))
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
        self.label_15.setPixmap(QtGui.QPixmap("../images/Nora.png"))
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "How To Use                     "))
        self.label_6.setText(_translate("Dialog",
                                        "<b>1.</b> Upload a single image file that you want to analyze by clicking the \"Upload Image\" button on the main menu of the application.<br><br>\n"
                                        "<b>2.</b> Adjust the threshold of the uploaded image by dragging the slider to highlight the cracks in the image.<br><br>\n"
                                        "<b>3.</b> Input the distance between the camera and the subject when the image was taken.<br><br>\n"
                                        "<b>4.</b> Click the \"Denoise Image\" button to remove any unnecessary noise from the image.<br><br>\n"
                                        "<b>5.</b> Click the \"Measure the Crack\" button to analyze the image and detect the measurements of the crack.<br><br>\n"
                                        "<b>6.</b> The results page will display on the screen, indicating whether the image contains cracks or not. If there are cracks found, the measurements of the crack will also be displayed.<br><br>\n"
                                        "<b>7.</b> Click the \"Add Details\" button to provide additional information about the crack, including the Location of Crack, Crack Type, Crack Progression and Remarks which may contain any notes you want to include.<br><br>\n"
                                        "<b>8.</b> Choose where to save the results by clicking the \"Save\" button.<br><br>\n"
                                        "<b>9.</b> If desired, click the \"Print\" button to print or save a PDF copy of the results.<br><br>\n"
                                        "<b>10.</b> That\'s it! With these simple steps, you can quickly and easily use CRACKTERIZE to detect cracks on concrete surfaces."))
        self.label_3.setText(_translate("Dialog", "Creating New Projects & Folders"))
        self.label_4.setText(_translate("Dialog",
                                        "<b>1.</b> Click the \"Create Project\" button displayed on the main menu of the application.<br><br>\n"
                                        "<b>2.</b> Name your project based on the location where the images that will be saved inside it were taken for a more effective file management.<br><br>\n"
                                        "<b>3.</b> Inside your project, create folders to organize your files. You can name your folders based on your preferences. You can also create new folders within your 4, project anytime you want by selecting the \"New Folder\" button within the project.<br><br>\n"
                                        "<b>4.</b> You can upload an image into the folders you\'ve created and it will automatically be processed and proceed to the application’s main function upon uploading or you can go back to the main menu and use the “Upload Image” button as it will give you the option to choose where to save the results. You can select an existing folder within your project, or create a new folder on the spot to save the results in it.<br><br>\n"
                                        "<b>5.</b> After using the main function, the app You can also create new folders within your project anytime you want by selecting the \"Create New Folder\" button within the project.<br><br>\n"
                                        "<b>6.</b> To access your projects and folders later, simply navigate to the main menu and select the project you want to view.<br><br>\n"
                                        "<b>7.</b> Enjoy using the app\'s project feature to keep your files organized and easily accessible!"))
        self.label_7.setText(_translate("Dialog", "Calculator"))
        self.label_5.setText(_translate("Dialog",
                                        "The calculator button in the main menu of the app provides access to different types of engineering-related calculators, such as Scientific Calculator, Stairs Calculator, Curb and Gutter Barrier Calculator, and others. These calculators can be used to perform quick calculations related to various engineering tasks and projects, without the need for a separate calculator app or tool."))
        self.label_8.setText(_translate("Dialog", "Developers"))
        self.label_9.setText(_translate("Dialog", "Ilagan, Jayvee P."))
        self.label_10.setText(_translate("Dialog", "Maiquez, John Carlo M."))
        self.label_14.setText(_translate("Dialog", "Narvaez, Allyza Mae A."))
        self.label_16.setText(_translate("Dialog", "Nora, John Patrick B."))

