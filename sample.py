import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QScrollArea


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.buttons = []
        self.max_per_row = 5

        # create initial button
        self.add_button = QPushButton('Add button', self)
        self.add_button.clicked.connect(self.add_new_button)
        self.buttons.append(self.add_button)

        # create scroll area
        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll.setWidget(self.scroll_widget)

        # set layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.add_button)
        vbox = QVBoxLayout(self.scroll_widget)
        vbox.addLayout(hbox)

        # set main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Adding buttons')
        self.show()

    def add_new_button(self):
        # create new button
        btn = QPushButton('Button {}'.format(len(self.buttons)), self.scroll_widget)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.buttons.append(btn)

        # add to layout
        row_num = len(self.buttons) // self.max_per_row
        col_num = len(self.buttons) % self.max_per_row

        if col_num == 0:
            hbox = QHBoxLayout()
            self.scroll_widget.layout().addLayout(hbox)
        else:
            hbox = self.scroll_widget.layout().itemAt(self.scroll_widget.layout().count() - 1).layout()

        hbox.addWidget(btn)

        # move add button to bottom left corner
        self.scroll_widget.layout().removeWidget(self.add_button)
        self.scroll_widget.layout().itemAt(row_num).insertWidget(col_num, self.add_button)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
