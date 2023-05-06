import os
import sqlite3
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create the GUI elements
        self.comboboxes = []
        self.btn_fetch = QtWidgets.QPushButton('Fetch Data')
        self.table = QtWidgets.QTableWidget()

        # set up the layout
        layout = QtWidgets.QVBoxLayout()
        for i in range(3): # add three comboboxes
            combobox = QtWidgets.QComboBox()
            self.comboboxes.append(combobox)
            layout.addWidget(combobox)
        layout.addWidget(self.btn_fetch)
        layout.addWidget(self.table)
        self.setLayout(layout)

        # populate the comboboxes with data from the database
        self.populate_comboboxes()

        # connect the button to fetch data
        self.btn_fetch.clicked.connect(self.fetch_data)

    def populate_comboboxes(self):
        # connect to the database
        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, '../Projects.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # get the distinct values for each column and add them to the corresponding combobox
        for i in range(3):
            column_name = f'column_{i}'
            c.execute(f"SELECT DISTINCT {column_name} FROM Save_Files ORDER BY {column_name}")
            values = [row[0] for row in c.fetchall()]
            combobox = self.comboboxes[i]
            combobox.addItems(values)
        conn.close()

    def fetch_data(self):
        # get the selected values from the comboboxes
        selected_values = [cb.currentText() for cb in self.comboboxes]

        # connect to the database
        conn = sqlite3.connect('../Projects.db')
        c = conn.cursor()

        # build the query based on the selected values
        query = "SELECT * FROM Save_Files WHERE "
        for i, value in enumerate(selected_values):
            column_name = f'column_{i}'
            query += f"{column_name} = '{value}' AND "
        query = query[:-5] # remove the last 'AND'
        query += "ORDER BY created_at DESC"

        # execute the query and populate the table with the results
        c.execute(query)
        rows = c.fetchall()
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(rows[0]))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)

        conn.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ex = ExampleApp()
    ex.show()
    app.exec_()
