from PyQt5 import QtCore, QtGui, QtWidgets

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

    def paint(self, painter, option, index):
        super().paint(painter, option, index)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    combo = QtWidgets.QComboBox()
    delegate = AlignDelegate(combo)
    combo.setItemDelegate(delegate)
    combo.addItems(['Item 1', 'Item 2', 'Item 3'])
    combo.show()
    app.exec_()
