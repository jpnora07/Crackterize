import sqlite3
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        # create a layout for the scrollable area
        self.scroll_layout = QVBoxLayout()

        # create a scrollable area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)

        # create a layout for the main window
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll_area)

        # set the main window layout
        self.setLayout(self.layout)

        # create a connection to the database
        self.conn = sqlite3.connect('Projects.db')
        self.c = self.conn.cursor()

        # create a table if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS Location_Folder
                                     (id INTEGER PRIMARY KEY, project_name TEXT, folder_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        # fetch data from the database
        self.c.execute("SELECT * FROM Location_Folder")
        data = self.c.fetchall()

        # generate buttons for each record in the table
        for record in data:
            name = record[1]
            description = record[2]

            btn = QPushButton(name, self.scroll_widget)
            btn.setToolTip(description)
            btn.clicked.connect(lambda checked, name=name: self.buttonClicked(name))
            self.scroll_layout.addWidget(btn)

    def buttonClicked(self, name):
        print(f"Button '{name}' clicked")

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()
