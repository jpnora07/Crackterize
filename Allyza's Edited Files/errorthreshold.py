# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorthreshold.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog") # start to copy
        Dialog.resize(329, 162)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(21)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(32, 25))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_5.setStyleSheet("#widget_5{\n"
                                    "background-image: url(images/i.png);\n"
                                    "}")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(206, 24))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout.addWidget(self.widget_6)
        self.x = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(23)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.x.sizePolicy().hasHeightForWidth())
        self.x.setSizePolicy(sizePolicy)
        self.x.setMinimumSize(QtCore.QSize(18, 0))
        self.x.setMaximumSize(QtCore.QSize(16777215, 16777195))
        self.x.setSizeIncrement(QtCore.QSize(0, 0))
        self.x.setStyleSheet("#x{\n"
                             "background-image: url(images/exit.png);\n"
                             "}")
        self.x.setText("")
        self.x.setAutoDefault(False)
        self.x.setDefault(False)
        self.x.setFlat(True)
        self.x.setObjectName("x")
        self.horizontalLayout.addWidget(self.x)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(-1, 1, -1, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setStyleSheet("#label{\n"
                                 "font-family: \"Inter\";\n"
                                 "font-size: 13pt; \n"
                                 "color: #000000;\n"
                                 "font: bold;\n"
                                 "font-size: 13px;\n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(109, 4, 109, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okBtn = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okBtn.sizePolicy().hasHeightForWidth())
        self.okBtn.setSizePolicy(sizePolicy)
        self.okBtn.setMinimumSize(QtCore.QSize(20, 0))
        self.okBtn.setMaximumSize(QtCore.QSize(16777196, 16777215))
        self.okBtn.setStyleSheet("#okBtn{\n"
                                 "font-weight:bold;\n"
                                 "color: white;\n"
                                 "background-color: #6F4B27;\n"
                                 "font-family: Inter;\n"
                                 "border-top-left-radius: 14px;\n"
                                 "border-top-right-radius:14px;\n"
                                 "border-bottom-left-radius: 14px;\n"
                                 "border-bottom-right-radius: 14px;\n"
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
        self.verticalLayout_2.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget) #hanggang dine lang ang lagi icopy

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # hindi na isasama ito, ito ung galing sa ui
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please enter the distance."))
        self.okBtn.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
