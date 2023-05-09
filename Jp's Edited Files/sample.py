from PyQt5 import QtCore, QtWidgets


class Container(QtWidgets.QWidget):
    def showEvent(self, event):
        if not event.spontaneous():
            self.setFocus()
            # certain widgets might want to keep focus on tab
            # so we delay the focusNextChild
            QtCore.QTimer.singleShot(0, self.focusNextChild)

    def focusNextPrevChild(self, isNext):
        # keep tab focus on this widget
        super().focusNextPrevChild(isNext)
        return self.isAncestorOf(QtWidgets.QApplication.focusWidget())

    def paintEvent(self, event):
        # stylesheets set on QWidget subclasses need this
        qp = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOption()
        opt.initFrom(self)
        qp.drawPrimitive(QtWidgets.QStyle.PE_Widget, opt)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.menuBar().addMenu('Test').addAction('Action')
        self.stack = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stack)
        self.stack.layout().setStackingMode(QtWidgets.QStackedLayout.StackAll)

        table = QtWidgets.QTableWidget(20, 30)
        self.stack.addWidget(table)

        table.cellDoubleClicked.connect(self.showDialog)

        self.resize(QtWidgets.QApplication.primaryScreen().size() * 2 / 3)

    def showDialog(self, row, column):
        background = QtWidgets.QWidget(objectName='background')
        background.setStyleSheet('''
            #background {
                background: rgba(64, 64, 64, 64);
            }
            Container {
                background: palette(window);
                border: 1px outset palette(window);
                border-radius: 5px;
            }
        ''')
        backLayout = QtWidgets.QVBoxLayout(background)

        container = Container()
        backLayout.addWidget(container, alignment=QtCore.Qt.AlignCenter)
        container.setAutoFillBackground(True)
        layout = QtWidgets.QVBoxLayout(container)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(20)

        font = self.font()
        font.setPointSize(font.pointSize() * 3)
        layout.addWidget(QtWidgets.QLabel('Hello!', font=font, alignment=QtCore.Qt.AlignCenter))
        layout.addWidget(QtWidgets.QLabel(
            'You doubleclicked cell {}, {}'.format(row + 1, column + 1)))
        button = QtWidgets.QPushButton('Close')
        layout.addWidget(button)

        self.centralWidget().addWidget(background)
        self.centralWidget().setCurrentWidget(background)

        # Important! you must always delete the widget when you don't need it
        # anymore. Alternatively, hide it if you want to reuse it again later
        button.clicked.connect(background.deleteLater)


app = QtWidgets.QApplication([])
win = MainWindow()
win.show()
app.exec()