from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 210)
        Dialog.setMaximumSize(QtCore.QSize(310, 210))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.existingproject = QtWidgets.QPushButton("Save Existing Project", self.widget_2)
        self.existingproject.clicked.connect(self.Save_to_existing_folder)
        self.existingproject.setMinimumSize(QtCore.QSize(70, 35))
        self.existingproject.setMaximumSize(QtCore.QSize(200, 35))
        self.existingproject.setStyleSheet("#existingproject{\n"
                                           "font-weight:bold;\n"
                                           "color: white;\n"
                                           "background-color: #6F4B27;\n"
                                           "border-top-left-radius: 7px;\n"
                                           "border-top-right-radius: 7px;\n"
                                           "border-bottom-left-radius: 7px;\n"
                                           "border-bottom-right-radius: 7px;\n"
                                           "font-family: Inter;\n"
                                           "font-size: 15px;\n"
                                           "text-align: center;\n"
                                           "}\n"
                                           "#existingproject:hover{\n"
                                           "color: rgb(144,115,87);\n"
                                           "border : 3px solid rgb(144,115,87);\n"
                                           "background-color: white;\n"
                                           "}\n"
                                           "")
        self.existingproject.setObjectName("existingproject")
        self.horizontalLayout_2.addWidget(self.existingproject)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.createnew = QtWidgets.QPushButton("Create New", self.widget_3)
        self.createnew.setMinimumSize(QtCore.QSize(200, 35))
        self.createnew.setMaximumSize(QtCore.QSize(200, 35))
        self.createnew.setStyleSheet("#createnew{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #2E74A9;\n"
                                     "border-top-left-radius: 7px;\n"
                                     "border-top-right-radius: 7px;\n"
                                     "border-bottom-left-radius: 7px;\n"
                                     "border-bottom-right-radius: 7px;\n"
                                     "font-family: Inter;\n"
                                     "font-size: 15px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#createnew:hover{\n"
                                     "color: #2E74A9;\n"
                                     "border : 3px solid  #2E74A9;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.createnew.setObjectName("createnew")
        self.horizontalLayout_3.addWidget(self.createnew)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.back = QtWidgets.QPushButton("Back", self.widget_4)
        self.back.setMinimumSize(QtCore.QSize(200, 35))
        self.back.setMaximumSize(QtCore.QSize(200, 35))
        self.back.clicked.connect(Dialog.close)
        self.back.setStyleSheet("#back{\n"
                                "font-weight:bold;\n"
                                "color: white;\n"
                                "background-color: #6A6E72;\n"
                                "border-top-left-radius: 7px;\n"
                                "border-top-right-radius: 7px;\n"
                                "border-bottom-left-radius: 7px;\n"
                                "border-bottom-right-radius: 7px;\n"
                                "font-family: Inter;\n"
                                "font-size: 15px;\n"
                                "text-align: center;\n"
                                "}\n"
                                "#back:hover{\n"
                                "color: #6A6E72;\n"
                                "border : 3px solid#6A6E72;\n"
                                "background-color: white;\n"
                                "}\n"
                                "")
        self.back.setObjectName("back")
        self.horizontalLayout_4.addWidget(self.back)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.existingproject.setText(_translate("Dialog", "Save to existing project"))
        self.createnew.setText(_translate("Dialog", "Create New"))
        self.back.setText(_translate("Dialog", "Back"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
