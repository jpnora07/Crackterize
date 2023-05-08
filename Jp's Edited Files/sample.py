import sys
from PyQt5.QtWidgets import QApplication, QDialog, QComboBox, QVBoxLayout, QScrollArea, QTableWidget, QTableWidgetItem, QPushButton


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ComboBox and ScrollArea Table')
        self.setGeometry(100, 100, 500, 400)

        # Create ComboBox
        self.comboBox = QComboBox()
        self.comboBox.addItem('Item 1')
        self.comboBox.addItem('Item 2')
        self.comboBox.addItem('Item 3')
        self.comboBox.currentIndexChanged.connect(self.addItemToTable)

        # Create ScrollArea
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QTableWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setColumnCount(1)
        self.scrollAreaWidgetContents.setHorizontalHeaderLabels(['Items'])

        # Create Button
        self.button = QPushButton('Print Items')
        self.button.clicked.connect(self.printTableItems)

        # Add widgets to layout
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.scrollArea)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def addItemToTable(self, index):
        # Get the selected item from the ComboBox
        item = self.comboBox.itemText(index)

        # Add the item and button to the table in the ScrollArea
        rowCount = self.scrollAreaWidgetContents.rowCount()
        self.scrollAreaWidgetContents.setRowCount(rowCount + 1)
        newItem = QTableWidgetItem(item)
        self.scrollAreaWidgetContents.setItem(rowCount, 0, newItem)

        button = QPushButton('Print Item')
        button.clicked.connect(lambda _, i=rowCount: self.printItem(i))
        self.scrollAreaWidgetContents.setCellWidget(rowCount, 1, button)

    def printItem(self, row):
        # Get the item from the selected row and print it
        item = self.scrollAreaWidgetContents.item(row, 0)
        print(item.text())


    def printTableItems(self):
        # Store the items in a list
        items = []
        numRows = self.scrollAreaWidgetContents.rowCount()
        for i in range(numRows):
            item = self.scrollAreaWidgetContents.item(i, 0)
            items.append(item.text())

        # Print the list of items
        print(items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
