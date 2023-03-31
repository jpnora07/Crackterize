import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QScrollArea, QWidget
import sqlite3


class ButtonDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create the main layout
        self.layout = QVBoxLayout()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, '../Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        # create a table if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS Location_Folder
                                                     (id INTEGER PRIMARY KEY, project_name TEXT, folder_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        # fetch data from the database
        self.c.execute("SELECT * FROM Projects")

        data = self.c.fetchall()
        print(data)  # Debugging line

        # Create a label above the scroll area
        label = QLabel("This is a label above the scroll area")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16pt; font-weight: bold;")
        self.layout.addWidget(label)

        # Create buttons based on the data
        for item in data:
            project_name = str(item[1])
            button = QPushButton(project_name)
            button.setMinimumSize(0, 70)
            button.setMaximumSize(500, 70)
            self.layout.addWidget(button)

        # Create a button below the scroll area
        button = QPushButton("This is a button below the scroll area")
        button.setMinimumSize(0, 70)
        button.setMaximumSize(500, 70)
        self.layout.addWidget(button)

        # Create a scroll area for the layout
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedSize(300, 300)

        # Create a widget to contain the layout
        widget = QWidget()
        widget.setLayout(self.layout)

        # Set the widget as the content of the scroll area
        scroll_area.setWidget(widget)

        # Set the main layout for the dialog to the scroll area
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(button)
        self.setLayout(main_layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ButtonDialog()
    dialog.show()
    print("Dialog shown")  # Debugging line
    sys.exit(app.exec_())
