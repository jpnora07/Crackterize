# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_project.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 168)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("#label_2{\n"
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
        self.textEditrename = QtWidgets.QTextEdit(self.widget_3)
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
        self.rename.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/edit_remarks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename.setIcon(icon)
        self.rename.setIconSize(QtCore.QSize(50, 50))
        self.rename.setAutoDefault(False)
        self.rename.setFlat(True)
        self.rename.setObjectName("rename")
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
        self.deletebtn = QtWidgets.QPushButton(self.widget_6)
        self.deletebtn.setMinimumSize(QtCore.QSize(0, 30))
        self.deletebtn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.deletebtn.setStyleSheet("#cancelbtn{\n"
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
        self.deletebtn.setObjectName("deletebtn")
        self.horizontalLayout_3.addWidget(self.deletebtn)
        self.okaybtn = QtWidgets.QPushButton(self.widget_6)
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
        self.horizontalLayout_3.addWidget(self.okaybtn)
        self.verticalLayout.addWidget(self.widget_6)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Edit Project"))
        self.textEditrename.setHtml(_translate("Dialog",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "hr { height: 1px; border-width: 0; }\n"
                                               "li.unchecked::marker { content: \"\\2610\"; }\n"
                                               "li.checked::marker { content: \"\\2612\"; }\n"
                                               "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.deletebtn.setText(_translate("Dialog", "Delete"))
        self.okaybtn.setText(_translate("Dialog", "Okay"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())