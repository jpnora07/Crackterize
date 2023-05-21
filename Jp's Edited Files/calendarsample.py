
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(658, 524)
        self.calendar = QtWidgets.QCalendarWidget(Dialog)
        self.calendar.setGeometry(QtCore.QRect(60, 120, 231, 241))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.calendar.setFont(font)
        self.calendar.setStyleSheet("")
        self.calendar.setGridVisible(False)
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(False)
        self.calendar.setObjectName("calendar")

        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(330, 150, 230, 190))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.calendarWidget.setFont(font)
        self.calendarWidget
        self.calendarWidget.setStyleSheet(" QWidget#qt_calendar_navigationbar{background-color:white;}\n"
                                          "#qt_calendar_prevmonth{\n"
                                          "qproperty-iconSize: 20px;\n"
                                          "qproperty-icon:url(:/images/back.png);\n"
                                          "        }\n"
                                          "#qt_calendar_nextmonth{\n"
                                          "qproperty-iconSize: 20px;\n"
                                          "qproperty-icon:url(:/images/back.png);\n"
                                          "        }")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
