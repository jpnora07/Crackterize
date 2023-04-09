

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class spinner(object):
    def setupUi(self, Dialog):
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 235)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setStyleSheet("background-color:#ffffff;")
        radius = 15
        Dialog.setStyleSheet("""
                                                    background:#EFEEEE;
                                                    border-top-left-radius:{0}px;
                                                    border-bottom-left-radius:{0}px;
                                                    border-top-right-radius:{0}px;
                                                    border-bottom-right-radius:{0}px;
                                                    """.format(radius))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color:#ffffff;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_process = QtWidgets.QLabel("Uploading...", self.widget)
        self.label_process.setStyleSheet("background-color:#ffffff;\n"
                                   "font-size:30px;\n"
                                   "color: #6c757d;\n"
                                   "font-style: Inter;")
        self.label_process.setScaledContents(True)
        self.label_process.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_process.setWordWrap(True)
        self.label_process.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_process)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("background-color:#ffffff;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.movie = QMovie("../images/spin_loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = spinner()
    ui.setupUi(Dialog)
    Dialog.exec_()
