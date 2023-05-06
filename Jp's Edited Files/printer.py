# -*- coding: utf-8 -*-
import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSizeF, QByteArray, Qt, QSize
from PyQt5.QtGui import QTextDocument, QFont, QTextCursor, QTextBlockFormat, QPainter, QTextCharFormat, QPixmap, \
    QTextImageFormat
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.widget_count = 1

        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 322)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 322, 196))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.combine = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.combine.setMaximumSize(QtCore.QSize(16777215, 50))
        self.combine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combine.setObjectName("combine")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.combine)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.folders = QtWidgets.QComboBox(self.combine)
        self.folders.setObjectName("folders")
        self.horizontalLayout_4.addWidget(self.folders)
        self.add_folder = QtWidgets.QPushButton(self.combine)
        self.add_folder.setMaximumSize(QtCore.QSize(30, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_folder.setIcon(icon)
        self.add_folder.clicked.connect(self.new_add_folder)
        self.add_folder.setObjectName("add_folder")
        self.horizontalLayout_4.addWidget(self.add_folder)
        self.verticalLayout.addWidget(self.combine)

        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.widget_21 = QtWidgets.QWidget(self.widget)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_15.setContentsMargins(-1, 20, -1, 5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.savebtn = QtWidgets.QPushButton(self.widget_21)
        self.savebtn.setMinimumSize(QtCore.QSize(0, 35))
        self.savebtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.savebtn.setStyleSheet("#savebtn{\n"
                                   "background: #2E74A9;\n"
                                   "font-weight:bold;\n"
                                   "color: white;\n"
                                   "border-radius: 7px;\n"
                                   "font-family: Inter;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "#savebtn::hover{\n"
                                   "color: #2E74A9;\n"
                                   "border : 3px solid  #2E74A9;\n"
                                   "background-color: white;\n"
                                   "}\n"
                                   "")
        self.savebtn.setObjectName("savebtn")
        self.horizontalLayout_15.addWidget(self.savebtn)
        self.printbtn = QtWidgets.QPushButton(self.widget_21)
        self.printbtn.setMinimumSize(QtCore.QSize(0, 35))
        self.printbtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.printbtn.setStyleSheet("#printbtn{\n"
                                    "background: #6F4B27;\n"
                                    "font-weight:bold;\n"
                                    "color: white;\n"
                                    "border-radius: 7px;\n"
                                    "font-family: Inter;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "#printbtn:hover{\n"
                                    "color: #6F4B27;\n"
                                    "border : 3px solid rgb(144,115,87);\n"
                                    "background-color: white;\n"
                                    "}\n"
                                    "")
        self.printbtn.setObjectName("printbtn")
        self.printbtn.clicked.connect(self.print)
        self.horizontalLayout_15.addWidget(self.printbtn)
        self.verticalLayout_2.addWidget(self.widget_21)
        self.horizontalLayout.addWidget(self.widget)
        self.fetch_folders()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def print(self):
        selected_folder = self.folders.currentIndex()
        if selected_folder == -1:
            self.folders.setCurrentIndex(0)
            selected_folder = 0
        selected_folder_text = self.folders.itemText(selected_folder)
        print(selected_folder_text)

        dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        db_path = os.path.join(dir_path, '../Projects.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM Save_Files ORDER BY created_at DESC")
        rows = c.fetchall()

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

            font_format = QTextCharFormat()
            font_format.setFont(QFont("Arial", 13))
            bold_format = QTextCharFormat()
            bold_format.setFont(QFont("Arial", 13))
            bold_format.setFontWeight(QFont.Bold)


            # loop through the fetched data and add each row to a separate page
            for row in rows:
                image_data = row[15]
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
                images_path = os.path.join(dir_path, 'Result Images')

                if not os.path.exists(images_path):
                    os.makedirs(images_path)

                # save the image to a file with the id as the name
                file_path = os.path.join(images_path, f"{row[0]}.png")
                pixmap.save(file_path, "PNG")

                # get all the image file names in the folder
                file_names = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

                # find the file name that matches the row ID
                for file_name in file_names:
                    if os.path.splitext(file_name)[0] == str(row[0]):
                        # add the saved image to the document
                        max_size = QSize(700, 450)
                        image_format = QTextImageFormat()
                        image_format.setWidth(max_size.width())
                        image_format.setHeight(max_size.height())
                        image_format.setName(os.path.join(images_path, file_name))
                        header_html = "<h1>Crackterize Result</h1>"
                        table_html = f'''
                            <table>
                                <tr>
                                    <td>
                                        <p>The image characterized as: <b>{row[9]}</b></p>
                                        <p>Length: <b>{row[5]}</b></p>
                                        <p>Width: <b>{row[4]}</b></p>
                                        <p>Positive Crack Probability: <b>{row[8]}</b></p>
                                        <p>Negative Crack Probability: <b>{row[7]}</b></p>
                                        <p>Location of Crack: <b>{row[10]}</b></p>
                                        <p>Crack Type: <b>{row[11]}</b></p>
                                        <p>Crack Progression: <b>{row[12]}</b></p>
                                        <p>Name of Project: <b>{row[16]}</b></p>
                                        <p>Name of Folder: <b>{row[1]}</b></p>
                                        <p>Date Added: <b>{row[14]}</b></p>
                                        <p>Remarks: <b>{row[13]}</b></p>
                                    </td>
                                </tr>
                            </table>
                        '''
                        html = header_html + table_html
                        cursor.insertImage(image_format)
                        cursor.insertHtml(header_html)
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

    def new_add_folder(self):
        self.widget_count += 1
        self.widget_3.hide()
        self.combine = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.combine.setMaximumSize(QtCore.QSize(16777215, 50))
        self.combine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combine.setObjectName("combine")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.combine)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.folders = QtWidgets.QComboBox(self.combine)
        self.folders.setObjectName("folders")
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            db_path = os.path.join(dir_path, '../Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT * FROM Location_Folder ORDER BY created_at DESC")
            rows = c.fetchall()
            for row in rows:
                self.folders.addItem(str(row[1]))
        except Exception as e:
            print("Empty Location_Folder! Users not yet add Location_Folder: ", e)
        self.horizontalLayout_4.addWidget(self.folders)
        self.add_folder = QtWidgets.QPushButton(f"{self.widget_count}", self.combine)
        self.add_folder.setMaximumSize(QtCore.QSize(30, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_folder.setIcon(icon)
        self.add_folder.clicked.connect(self.new_add_folder)
        self.add_folder.setObjectName("add_folder")
        self.horizontalLayout_4.addWidget(self.add_folder)
        self.verticalLayout.addWidget(self.combine)

    def fetch_folders(self):
        try:
            dir_path = os.path.join(os.environ['APPDATA'], 'Crackterize')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            db_path = os.path.join(dir_path, '../Projects.db')
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT * FROM Location_Folder ORDER BY created_at DESC")
            rows = c.fetchall()
            for row in rows:
                self.folders.addItem(str(row[1]))
        except Exception as e:
            print("Empty Location_Folder! Users not yet add Location_Folder: ", e)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose"))
        self.savebtn.setText(_translate("Dialog", "Cancel"))
        self.printbtn.setText(_translate("Dialog", "Print"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
