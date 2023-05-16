from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.combo = QtGui.QComboBox()
        self.combo.setEditable(True)
        self.combo.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.combo.addItems('One Two Three Four Five'.split())
        layout.addWidget(self.combo)


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())