import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(200, 200)

notification_list = QListWidget(window)

for i in range(30):
    item = QListWidgetItem("Notification " + str(i + 1))
    notification_list.addItem(item)

notification_list.show()

sys.exit(app.exec_())
