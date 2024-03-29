from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 365)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 20, 421, 311))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(100, 50, 211, 71))
        self.widget_2.setObjectName("widget_2")
        self.existingproject = QtWidgets.QPushButton("Save Existing Project", self.widget_2)
        self.existingproject.setGeometry(QtCore.QRect(0, 20, 211, 41))
        self.existingproject.setStyleSheet("#existingproject{\n"
                                           "font-weight:bold;\n"
                                           "color: white;\n"
                                           "background-color: #6F4B27;\n"
                                           "border-top-left-radius: 20px;\n"
                                           "border-top-right-radius: 20px;\n"
                                           "border-bottom-left-radius: 20px;\n"
                                           "border-bottom-right-radius: 20px;\n"
                                           "font-family: Inter;\n"
                                           "font-size: 12px;\n"
                                           "text-align: center;\n"
                                           "}\n"
                                           "#existingproject:hover{\n"
                                           "color: rgb(144,115,87);\n"
                                           "border : 3px solid rgb(144,115,87);\n"
                                           "background-color: white;\n"
                                           "}\n"
                                           "")
        self.existingproject.setObjectName("existingproject")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(100, 120, 211, 61))
        self.widget_3.setObjectName("widget_3")
        self.createnew = QtWidgets.QPushButton("Create New", self.widget_3)
        self.createnew.setGeometry(QtCore.QRect(0, 10, 211, 41))
        self.createnew.setStyleSheet("#createnew{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #2E74A9;\n"
                                     "border-top-left-radius: 20px;\n"
                                     "border-top-right-radius: 20px;\n"
                                     "border-bottom-left-radius: 20px;\n"
                                     "border-bottom-right-radius: 20px;\n"
                                     "font-family: Inter;\n"
                                     "font-size: 12px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#createnew:hover{\n"
                                     "color: #2E74A9;\n"
                                     "border : 3px solid  #2E74A9;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.createnew.setObjectName("createnew")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(100, 180, 211, 71))
        self.widget_4.setObjectName("widget_4")
        self.back = QtWidgets.QPushButton("Back", self.widget_4)
        self.back.setGeometry(QtCore.QRect(0, 10, 211, 41))
        self.back.setStyleSheet("#back{\n"
                                "font-weight:bold;\n"
                                "color: white;\n"
                                "background-color: #6A6E72;\n"
                                "border-top-left-radius: 20px;\n"
                                "border-top-right-radius: 20px;\n"
                                "border-bottom-left-radius: 20px;\n"
                                "border-bottom-right-radius: 20px;\n"
                                "font-family: Inter;\n"
                                "font-size: 12px;\n"
                                "text-align: center;\n"
                                "}\n"
                                "#back:hover{\n"
                                "color: #6A6E72;\n"
                                "border : 3px solid#6A6E72;\n"
                                "background-color: white;\n"
                                "}\n"
                                "")
        self.back.setObjectName("back")

        QtCore.QMetaObject.connectSlotsByName(Dialog)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
