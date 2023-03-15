import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QListView, QVBoxLayout

class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a list view widget
        self.list_view = QListView(self)

    def showPopup(self):
        # Adjust the position and width of the list view widget
        combo_rect = self.rect()
        list_rect = self.list_view.geometry()
        list_rect.setWidth(400)
        list_rect.moveCenter(combo_rect.center())
        self.list_view.setGeometry(list_rect)

        # Show the list view widget
        super().showPopup()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a custom combo box widget
        combo = CustomComboBox(self)

        # Add some items to the combo box
        combo.addItem('Item 1')
        combo.addItem('Item 2')
        combo.addItem('Item 3')
        combo.addItem('Item 4')
        combo.addItem('Item 5')
        combo.addItem('Item 6')

        # Set the minimum width and maximum width of the combo box
        combo.setMinimumWidth(200)
        combo.setMaximumWidth(200)

        # Create a vertical layout
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

        # Set the list view size
        combo.list_view.setFixedWidth(400)
        combo.list_view.setFixedHeight(50)

        # Center the list view widget to the combo box widget
        combo.list_view.move(combo.rect().center() - combo.list_view.rect().center())

        # Add the combo box to the layout
        vbox.addStretch(1)
        vbox.addWidget(combo)
        vbox.addStretch(1)

        # Set the window properties
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Combo Box Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
