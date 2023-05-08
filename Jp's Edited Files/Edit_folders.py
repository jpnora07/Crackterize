import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSizeF, QSize
from PyQt5.QtGui import QTextCursor, QPainter, QTextImageFormat, QTextDocument
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton


class edit_folders(object):

    def __init__(self, background_widget, history, projects, mainwindow):
        self.MainWindow = mainwindow
        self.history = history
        self.myProjects = projects
        self.background_widget = background_widget

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.resize(493, 297)
        Dialog.setStyleSheet(
            '''#Dialog{border: 1px solid grey;} ''')
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_2.setMaximumSize(QtCore.QSize(200, 300))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel("Select a Folder", self.widget_4)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setStyleSheet("#label{\n"
                                 "    font: 900 12pt \"Segoe UI Black\";\n"
                                 "    alignment: center;\n"
                                 "    color: rgba(111, 75, 39, 0.77);\n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.folder_names_cb = QtWidgets.QComboBox(self.widget_4)
        self.folder_names_cb.setObjectName("folder_names_cb")
        try:
            with open('../selected_project.txt', 'r') as f:
                self.project_name = f.read()
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            db_path = os.path.join(dir_path, '../Projects.db')
            # Create a connection to a SQLite database or create it if it doesn't exist
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM Location_Folder WHERE project_name = ?", (self.project_name,))
            rows = self.c.fetchall()
            for row in rows:
                count = str(row[2])
                self.folder_names_cb.addItem(count)
        except Exception as e:
            print(e)

        self.folder_names_cb.currentIndexChanged.connect(self.addItemToTable)
        self.verticalLayout_3.addWidget(self.folder_names_cb)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 200))
        self.widget_5.setObjectName("widget_5")
        self.radioButton_delete = QtWidgets.QRadioButton("Delete", self.widget_5)
        self.radioButton_delete.setGeometry(QtCore.QRect(20, 20, 89, 20))
        self.radioButton_delete.setStyleSheet("#radioButton_delete{\n"
                                              "font-weight:bold;\n"
                                              "}\n"
                                              "#radioButton_delete::indicator{\n"
                                              "color: red;\n"
                                              "\n"
                                              "}")
        self.radioButton_delete.setObjectName("radioButton_delete")
        self.radioButton_print = QtWidgets.QRadioButton("Print", self.widget_5)
        self.radioButton_print.setGeometry(QtCore.QRect(20, 50, 89, 20))
        self.radioButton_print.setStyleSheet("#radioButton_print {\n"
                                             "font-weight:bold;\n"
                                             "}")
        self.radioButton_print.setObjectName("radioButton_print")
        self.radioButton_rename = QtWidgets.QRadioButton("Rename", self.widget_5)
        self.radioButton_rename.setGeometry(QtCore.QRect(20, 80, 89, 20))
        self.radioButton_rename.setStyleSheet("#radioButton_rename {\n"
                                              "font-weight:bold;\n"
                                              "}")
        self.radioButton_rename.setObjectName("radioButton_rename")
        self.verticalLayout.addWidget(self.widget_5)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_7)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 162, 151))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setStyleSheet("#tableWidget{\n"
                                       "border-style: solid; border-width: 2px; border-color: rgba(111, 75, 39, 0.77);;\n"
                                       "}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Folder Name', 'Remove'])
        self.tableWidget.horizontalHeader().resizeSection(0, 150)

        self.tableWidget.horizontalHeader().resizeSection(1, 50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.tableWidget, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_6.setSizeIncrement(QtCore.QSize(0, 200))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancelbtn = QtWidgets.QPushButton("Cancel", self.widget_6)
        self.cancelbtn.setMinimumSize(QtCore.QSize(0, 30))
        self.cancelbtn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.cancelbtn.setStyleSheet("#cancelbtn{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #6A6E72;\n"
                                     "border-top-left-radius: 7px;\n"
                                     "border-top-right-radius: 7px;\n"
                                     "border-bottom-left-radius: 7px;\n"
                                     "border-bottom-right-radius: 7px;\n"
                                     "font-family: Inter;\n"
                                     "font-size: 11px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#cancelbtn:hover{\n"
                                     "color: #6A6E72;\n"
                                     "border : 3px solid#6A6E72;\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.cancelbtn.setObjectName("cancelbtn")
        self.horizontalLayout_3.addWidget(self.cancelbtn)
        self.okaybtn = QtWidgets.QPushButton("Okay", self.widget_6)
        self.okaybtn.setMinimumSize(QtCore.QSize(0, 30))
        self.okaybtn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.okaybtn.setStyleSheet("#okaybtn{\n"
                                   "font-weight:bold;\n"
                                   "color: white;\n"
                                   "background-color: #6F4B27;\n"
                                   "border-top-left-radius: 7px;\n"
                                   "border-top-right-radius: 7px;\n"
                                   "border-bottom-left-radius: 7px;\n"
                                   "border-bottom-right-radius: 7px;\n"
                                   "font-family: Inter;\n"
                                   "font-size: 11px;\n"
                                   "text-align: center;\n"
                                   "}\n"
                                   "#okaybtn:hover{\n"
                                   "color: rgb(144,115,87);\n"
                                   "border : 3px solid rgb(144,115,87);\n"
                                   "background-color: white;\n"
                                   "}")
        self.okaybtn.setObjectName("okaybtn")
        self.okaybtn.clicked.connect(self.printTableItems)
        self.horizontalLayout_3.addWidget(self.okaybtn)

        self.verticalLayout_2.addWidget(self.widget_6)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def addItemToTable(self, index):
        # Get the selected item from the ComboBox
        item = self.folder_names_cb.itemText(index)
        # Add the item to the table in the ScrollArea
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowCount + 1)
        newItem = QTableWidgetItem(item)
        self.tableWidget.setItem(rowCount, 0, newItem)

        button = QPushButton()
        button.setMinimumSize(QtCore.QSize(0, 0))
        button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setFlat(True)
        button.clicked.connect(lambda _, i=rowCount: self.remove_item(i))
        self.tableWidget.setCellWidget(rowCount, 1, button)

    def remove_item(self, row):
        self.tableWidget.removeRow(row)

    def printTableItems(self):
        # Store the items in a list
        items = []
        numRows = self.tableWidget.rowCount()
        for i in range(numRows):
            item = self.tableWidget.item(i, 0)
            items.append(item.text())

        if len(items) == 0:
            print("The list is empty!")
        else:
            print("The list contains items.")

        if self.radioButton_delete.isChecked() and len(items) > 0:
            print(self.radioButton_delete.text())

        elif self.radioButton_print.isChecked() and len(items) > 0:
            self.printer(items)
            print(self.radioButton_print.text())

        elif self.radioButton_rename.isChecked() and len(items) > 0:
            print(self.radioButton_rename.text())

        else:
            # Handle the case where none of the radio buttons are checked
            print('No radio button is checked')

        # Print the list of items
        print(items)

    def printer(self, folders):
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            db_path = os.path.join(dir_path, '../Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # folders = ['efw', 'asfasf']

            # Create a comma-separated string of the folder names
            folders_string = ','.join(["'{}'".format(f) for f in folders])

            c.execute(f"SELECT * FROM Save_Files WHERE folder_name IN ({folders_string})")
            rows = c.fetchall()

            if not rows:
                print("No data found for the selected folders")
            else:
                try:
                    printer = QPrinter()
                    printer.setPageSize(QPrinter.Letter)
                    printer.setOrientation(QPrinter.Portrait)
                    printer.setOutputFormat(QPrinter.PdfFormat)
                    printer.setOutputFileName("preview.pdf")

                    # create a QTextDocument to hold the text to be printed
                    doc = QTextDocument()
                    doc.setPageSize(QSizeF(792, 612))  # set page size to 11x8.5 inches (in points)
                    doc.setDocumentMargin(36)

                    # create a QTextCursor to insert text into the QTextDocument
                    cursor = QTextCursor(doc)

                    # loop through the fetched data and add each row to a separate page
                    for row in rows:
                        # image_data = row[15]
                        # pixmap = QPixmap()
                        # pixmap.loadFromData(image_data)
                        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
                        images_path = os.path.join(dir_path, 'Result Images')

                        if not os.path.exists(images_path):
                            os.makedirs(images_path)

                        # save the image to a file with the id as the name
                        # file_path = os.path.join(images_path, f"{row[0]}.png")
                        # pixmap.save(file_path, "PNG")

                        # get all the image file names in the folder
                        file_names = [f for f in os.listdir(images_path) if
                                      os.path.isfile(os.path.join(images_path, f))]

                        # find the file name that matches the row ID
                        for file_name in file_names:
                            if os.path.splitext(file_name)[0] == str(row[0]):
                                # add the saved image to the document
                                max_size = QSize(700, 450)
                                image_format = QTextImageFormat()
                                image_format.setWidth(max_size.width())
                                image_format.setHeight(max_size.height())
                                image_format.setName(os.path.join(images_path, file_name))
                                table_html = f'''
                                    <table>
                                        <tr>
                                            <td>
                                                <p style='font-size: 16px;'>The image characterized as: <b>{row[9]}</b></p>
                                                <p style='font-size: 16px;'>Length: <b>{row[5]}</b></p>
                                                <p style='font-size: 16px;'>Width: <b>{row[4]}</b></p>
                                                <p style='font-size: 16px;'>Positive Crack Probability: <b>{row[8]}</b></p>
                                                <p style='font-size: 16px;'>Negative Crack Probability: <b>{row[7]}</b></p>
                                                <p style='font-size: 16px;'>Location of Crack: <b>{row[10]}</b></p>
                                                <p style='font-size: 16px;'>Name of Project: <b>{row[16]}</b></p>
                                                <p style='font-size: 16px;'>Name of Folder: <b>{row[1]}</b></p>
                                                <p style='font-size: 16px;'>Date Added: <b>{row[14]}</b></p>
                                                <p style='font-size: 16px;'>Remarks: <b>{row[13]}</b></p>
                                            </td>
                                        </tr>
                                    </table>
                                '''
                                cursor.insertImage(image_format)
                                cursor.insertHtml(table_html)
                                cursor.setPosition(0, QTextCursor.MoveAnchor)
                                cursor.insertHtml("<br><br><br>")
                                break
                                # clear the QTextCursor to start a new page

                    # create a QPrinter to print the document
                    printer = QPrinter()
                    printer.setPageSize(QPrinter.Letter)
                    printer.setOrientation(QPrinter.Portrait)
                    printer.setOutputFormat(QPrinter.PdfFormat)
                    printer.setOutputFileName("preview.pdf")

                    # create a QPainter to paint the document onto the printer
                    painter = QPainter()
                    if painter.begin(printer):
                        doc.setPageSize(QSizeF(printer.pageRect().size()))
                        doc.drawContents(painter)
                        painter.end()

                    # preview the document using a QPrintPreviewDialog
                    preview = QPrintPreviewDialog(printer)
                    preview.paintRequested.connect(doc.print_)
                    preview.exec_()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select a Folder"))
        self.radioButton_delete.setText(_translate("Dialog", "Delete"))
        self.radioButton_print.setText(_translate("Dialog", "Print"))
        self.radioButton_rename.setText(_translate("Dialog", "Rename"))
        self.okaybtn.setText(_translate("Dialog", "Okay"))
        self.cancelbtn.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = edit_folders(None,None,None,None )
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
