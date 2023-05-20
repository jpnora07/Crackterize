from PyQt5.QtWidgets import QCalendarWidget, QDateEdit, QApplication
from PyQt5 import QtGui, QtWidgets

class CustomDateEdit(QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCalendarPopup(True)

        calendar_widget = QCalendarWidget(self)
        font = QtGui.QFont()
        font.setPointSize(6)
        calendar_widget.setFont(font)
        calendar_widget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        calendar_widget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        calendar_widget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        calendar_widget.setNavigationBarVisible(True)
        calendar_widget.setStyleSheet('''
            QWidget#qt_calendar_navigationbar {
                color: red;
            }
            QToolButton#qt_calendar_prevmonth {
                qproperty-iconSize: 15px;
                qproperty-icon: url(images/previous.png);
            }
            QToolButton#qt_calendar_nextmonth {
                qproperty-iconSize: 15px;
                qproperty-icon: url(images/next.png);
            }
            QToolButton#qt_calendar_month {
                color: blue;
            }
            QToolButton#qt_calendar_year {
                color: blue;
            }
        ''')

        self.setCalendarWidget(calendar_widget)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    date_edit = CustomDateEdit()
    date_edit.show()

    sys.exit(app.exec_())
