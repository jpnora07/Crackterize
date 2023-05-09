import sys
from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
combo = QtWidgets.QComboBox()

# Create top-level menu items
top_menu_items = ['Fruits', 'Vegetables']

# Create submenus for 'Fruits' item
fruit_submenus = ['Apple', 'Banana', 'Orange']

# Add top-level menu items to combobox
combo.addItems(top_menu_items)

# Create a model for the combobox
model = QtGui.QStandardItemModel()
combo.setModel(model)

# Add submenus to the 'Fruits' top-level menu item
fruit_item = QtGui.QStandardItem('Fruits')
model.appendRow(fruit_item)
for submenu in fruit_submenus:
    fruit_item.appendRow(QtGui.QStandardItem(submenu))

combo.show()
sys.exit(app.exec_())
