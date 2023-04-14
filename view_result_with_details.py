import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QByteArray, QSizeF
from PyQt5.QtGui import QPixmap, QImage, QTextDocument, QTextCursor, QPainter, QFont, QTextCharFormat, QTextImageFormat, \
    QTextFrameFormat
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QDialog, QMessageBox


class result_with_details(object):
    def __init__(self, background_widget):
        self.background_widget = background_widget

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        data = self.fetch_save_files_of_projects()
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        Dialog.setMaximumSize(QtCore.QSize(700, 600))
        Dialog.setStyleSheet("#Dialog{background:rgb(255, 255, 255)}")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_7 = QtWidgets.QWidget(Dialog)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_16 = QtWidgets.QWidget(self.widget_7)
        self.widget_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widget_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_5.setContentsMargins(0, 5, 5, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.exit = QtWidgets.QPushButton(self.widget_16)
        self.exit.setMinimumSize(QtCore.QSize(0, 25))
        self.exit.setMaximumSize(QtCore.QSize(25, 25))
        self.exit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setDefault(False)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.exit_function)
        self.verticalLayout_5.addWidget(self.exit)
        self.verticalLayout_7.addWidget(self.widget_16)
        self.widget = QtWidgets.QWidget(self.widget_7)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WithLogo = QtWidgets.QWidget(self.widget)
        self.WithLogo.setMinimumSize(QtCore.QSize(564, 80))
        self.WithLogo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.WithLogo.setStyleSheet("#WithLogo{border-image: url(images/Crackterize.png) 400 0 400 0 stretch;}")
        self.WithLogo.setObjectName("WithLogo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WithLogo)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addWidget(self.WithLogo)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setMaximumSize(QtCore.QSize(340, 16777215))
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_image = QtWidgets.QLabel(self.widget_12)
        self.label_image.setStyleSheet("border: 1px solid grey;")
        self.label_image.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label_image)
        self.horizontalLayout_2.addWidget(self.widget_12)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(280, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(280, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.concretecracked_2 = QtWidgets.QLabel(self.widget_6)
        self.concretecracked_2.setStyleSheet("#concretecracked_2{\n"
                                             "    \n"
                                             "color: #2E74A9;\n"
                                             "font: bold;\n"
                                             "border: 2px solid white;\n"
                                             "font-size: 20px;\n"
                                             "border-bottom-color: rgb(172, 172, 172);;\n"
                                             "}")
        self.concretecracked_2.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked_2.setWordWrap(True)
        self.concretecracked_2.setObjectName("concretecracked_2")
        self.verticalLayout_2.addWidget(self.concretecracked_2)
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.widget_10)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.lengthlbl = QtWidgets.QLabel(self.widget_10)
        self.lengthlbl.setStyleSheet("#lengthlbl{\n"
                                     "    color:  #555555;\n"
                                     "font: bold;\n"
                                     "    font-size: 15px}")
        self.lengthlbl.setObjectName("lengthlbl")
        self.horizontalLayout_10.addWidget(self.lengthlbl)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_13 = QtWidgets.QWidget(self.widget_6)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.widget_13)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.widthlbl = QtWidgets.QLabel(self.widget_13)
        self.widthlbl.setStyleSheet("#widthlbl{\n"
                                    "    color:  #555555;\n"
                                    "font: bold;\n"
                                    "    font-size: 15px;\n"
                                    "}")
        self.widthlbl.setObjectName("widthlbl")
        self.horizontalLayout_11.addWidget(self.widthlbl)
        self.verticalLayout_2.addWidget(self.widget_13)
        self.widget_11 = QtWidgets.QWidget(self.widget_6)
        self.widget_11.setObjectName("widget_11")
        self.widget_11.hide()
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widgetPosition = QtWidgets.QLabel(self.widget_11)
        self.widgetPosition.setStyleSheet("#widgetPosition{\n"
                                          "color: rgba(111, 75, 39, 0.77);\n"
                                          "font-size: 13px;\n"
                                          "font-weight: bold;\n"
                                          "}")
        self.widgetPosition.setObjectName("widgetPosition")
        self.horizontalLayout_13.addWidget(self.widgetPosition)
        self.position_lbl = QtWidgets.QLabel(self.widget_11)
        self.position_lbl.setStyleSheet("#position_lbl{\n"
                                        "    color:  #555555;\n"
                                        "font: bold;\n"
                                        "    font-size: 15px;\n"
                                        "}")
        self.position_lbl.setObjectName("position_lbl")
        self.horizontalLayout_13.addWidget(self.position_lbl)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_15 = QtWidgets.QWidget(self.widget_6)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetPos_2 = QtWidgets.QLabel(self.widget_15)
        self.widgetPos_2.setMinimumSize(QtCore.QSize(180, 0))
        self.widgetPos_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetPos_2.setStyleSheet("#widgetPos_2{\n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "font-size: 13px;\n"
                                       "font-weight: bold;\n"
                                       "}")
        self.widgetPos_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.widgetPos_2.setWordWrap(True)
        self.widgetPos_2.setObjectName("widgetPos_2")
        self.verticalLayout_3.addWidget(self.widgetPos_2)
        self.verticalLayout_2.addWidget(self.widget_15)
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widgetNeg = QtWidgets.QLabel(self.widget_5)
        self.widgetNeg.setMinimumSize(QtCore.QSize(180, 0))
        self.widgetNeg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetNeg.setStyleSheet("#widgetNeg{\n"
                                     "color: rgba(111, 75, 39, 0.77);\n"
                                     "font-size: 13px;\n"
                                     "font-weight: bold;\n"
                                     "}")
        self.widgetNeg.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.widgetNeg.setWordWrap(True)
        self.widgetNeg.setObjectName("widgetNeg")
        self.verticalLayout_4.addWidget(self.widgetNeg)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_14 = QtWidgets.QWidget(self.widget_6)
        self.widget_14.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.i = QtWidgets.QLabel(self.widget_14)
        self.i.setMinimumSize(QtCore.QSize(30, 30))
        self.i.setMaximumSize(QtCore.QSize(30, 30))
        self.i.setStyleSheet("#i{\n"
                             "    border-image: url(images/i.png)  ;}")
        self.i.setText("")
        self.i.setAlignment(QtCore.Qt.AlignCenter)
        self.i.setWordWrap(False)
        self.i.setObjectName("i")
        self.horizontalLayout_12.addWidget(self.i)
        self.concretecracked = QtWidgets.QLabel(self.widget_14)
        self.concretecracked.setStyleSheet("#concretecracked{\n"
                                           "color: #2E74A9;\n"
                                           "font: bold;\n"
                                           "font-size: 15px;\n"
                                           "}")
        self.concretecracked.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked.setWordWrap(True)
        self.concretecracked.setObjectName("concretecracked")
        self.horizontalLayout_12.addWidget(self.concretecracked)
        self.verticalLayout_2.addWidget(self.widget_14)
        self.widget_17 = QtWidgets.QWidget(self.widget_6)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.del_btn = QtWidgets.QPushButton(self.widget_17)
        self.del_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.del_btn.setMaximumSize(QtCore.QSize(119, 35))
        self.del_btn.setStyleSheet("#del_btn{\n"
                                   "color: #2E74A9;\n"
                                   "border : 3px solid   #6F4B27;\n"
                                   "background-color: :#E3E9ED;\n"
                                   "border-radius: 7px;\n"
                                   "}\n"
                                   "\n"
                                   "#del_btn::hover{\n"
                                   "background: #E3E9ED;\n"
                                   "font-family: Inter;\n"
                                   "}\n"
                                   "")
        self.del_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_btn.setIcon(icon1)
        self.del_btn.setObjectName("del_btn")
        self.del_btn.clicked.connect(self.delete_result)
        self.horizontalLayout.addWidget(self.del_btn)
        self.print1 = QtWidgets.QPushButton(self.widget_17)
        self.print1.setMinimumSize(QtCore.QSize(0, 35))
        self.print1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.print1.setStyleSheet("\n"
                                  "#print1{\n"
                                  "color: #2E74A9;\n"
                                  "border : 3px solid   #2E74A9;\n"
                                  "background-color: :#2E74A9;\n"
                                  "border-radius: 7px;\n"
                                  "}\n"
                                  "\n"
                                  "#print1::hover{\n"
                                  "background: #E3E9ED;\n"
                                  "font-family: Inter;\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.print1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print1.setIcon(icon2)
        self.print1.setIconSize(QtCore.QSize(16, 16))
        self.print1.setObjectName("print1")
        self.horizontalLayout.addWidget(self.print1)
        self.print1.clicked.connect(self.printpreviewDialog)
        self.verticalLayout_2.addWidget(self.widget_17)
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.view_details = QtWidgets.QPushButton(self.widget_2)
        self.view_details.setMinimumSize(QtCore.QSize(0, 35))
        self.view_details.setMaximumSize(QtCore.QSize(16777215, 35))
        self.view_details.clicked.connect(self.view_details_function)
        self.view_details.setStyleSheet("#view_details{\n"
                                        "background: #6F4B27;\n"
                                        "font-weight:bold;\n"
                                        "color: white;\n"
                                        "border-radius: 7px;\n"
                                        "font-family: Inter;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "#view_details:hover{\n"
                                        "color: #6F4B27;\n"
                                        "border : 3px solid rgb(144,115,87);\n"
                                        "background-color: white;\n"
                                        "}\n"
                                        "")
        self.view_details.setObjectName("view_details")
        self.horizontalLayout_5.addWidget(self.view_details)
        self.update = QtWidgets.QPushButton(self.widget_2)
        self.update.setMinimumSize(QtCore.QSize(0, 35))
        self.update.setMaximumSize(QtCore.QSize(16777215, 35))
        self.update.setStyleSheet("#update{\n"
                                  "background: #2E74A9;\n"
                                  "font-weight:bold;\n"
                                  "color: white;\n"
                                  "border-radius: 7px;\n"
                                  "font-family: Inter;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#update::hover{\n"
                                  "color: #2E74A9;\n"
                                  "border : 3px solid  #2E74A9;\n"
                                  "background-color: white;\n"
                                  "}\n"
                                  "")
        self.update.setObjectName("update")
        self.update.clicked.connect(self.update_result)
        self.horizontalLayout_5.addWidget(self.update)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout_7.addWidget(self.widget)
        self.verticalLayout_6.addWidget(self.widget_7)

        if data:
            try:
                self.width = data[0][4]
                self.length = data[0][5]
                self.position = data[0][6]
                self.no_crack = data[0][7]
                self.crack = data[0][8]
                self.status = data[0][9]

                self.loc = data[0][10]
                self.type = data[0][11]
                self.prog = data[0][12]
                self.remarks = data[0][13]
                self.date = data[0][14]
                self.image = data[0][2]
                self.image_orig = data[0][3]
                # Convert the image data to QPixmap
                byte_array = QByteArray(self.image)
                self.pixmap = QPixmap()
                self.pixmap.loadFromData(byte_array)

                byte_array_orig = QByteArray(self.image_orig)
                self.pixmap_orig = QPixmap()
                self.pixmap_orig.loadFromData(byte_array_orig)

                self.label_image.setFixedSize(322, 447)
                label_size = self.label_image.size()
                scaled_pixmap = self.pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

                scaled_pixmap_orig = self.pixmap_orig.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                scaled_pixmap_orig.save('image_for_doc.png')
                self.label_image.setPixmap(scaled_pixmap)
                self.widthlbl.setText(self.width + " mm")
                self.position_lbl.setText(self.position)
                self.lengthlbl.setText(self.length + " cm")
                self.concretecracked.setText("The image classified " + self.status + ".")
                self.widgetPos_2.setText("Positive Crack Probability is " + self.crack + ".")
                self.widgetNeg.setText("Negative Crack Probability is " + self.no_crack + ".")
            except Exception as e:
                print(e)
        else:
            print("No data found.")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_function(self):
        self.Dialog.close()
        new_remark = 'New_Remark.txt'
        if os.path.isfile(new_remark):
            os.remove(new_remark)
        self.background_widget.close()

    def printpreviewDialog(self):
        printer = QPrinter()
        printer.setPageSize(QPrinter.Letter)
        printer.setOrientation(QPrinter.Portrait)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("preview.pdf")

        doc = QTextDocument()
        doc.setPageSize(QSizeF(792, 612))  # set page size to 11x8.5 inches (in points)
        doc.setDocumentMargin(36)  # set margin to 0.5 inch (36 points)
        cursor = QTextCursor(doc)

        # Load the image file
        image_path = os.path.abspath("image_for_doc.png")
        image = QImage(image_path)
        if image.isNull():
            print("Error: Could not load image")
            return

        # Insert the image into the document
        pixmap = QPixmap.fromImage(image)
        try:
            if not pixmap.isNull():
                # Add the title to the document
                title_format = QTextCharFormat()
                title_format.setFont(QFont("Arial", 20, QFont.Bold))
                cursor.insertText("                              Crackterized Result", title_format)
                cursor.insertBlock()

                image_format = QTextImageFormat()
                image_format.setWidth(pixmap.width())
                image_format.setHeight(pixmap.height())
                image_format.setName(image_path)

                # Create a QTextFrameFormat and set its properties
                frame_format = QTextFrameFormat()
                frame_format.setBorder(1)  # set border width to 1
                frame_format.setBorderStyle(QTextFrameFormat.BorderStyle_Solid)  # set border style to solid
                frame_format.setBorderBrush(Qt.black)  # set border color to black
                frame_format.setPadding(5)  # set padding to 5
                frame_format.setMargin(5)

                # Insert the image into a QTextFrame and set its format
                frame = cursor.insertFrame(frame_format)
                frame_cursor = QTextCursor(frame)
                frame_cursor.insertImage(image_format, QTextFrameFormat.FloatRight)
        except Exception as e:
            print(e)

        # Create a QTextCharFormat object with the desired font properties
        font_format = QTextCharFormat()
        font_format.setFont(QFont("Arial", 15))

        # Add the data to the document
        cursor.insertText(f"The image characterized as: {self.status}\n", font_format)
        cursor.insertText(f"Length: {self.length}\n", font_format)
        cursor.insertText(f"Width: {self.width}\n", font_format)
        # cursor.insertText(f"Orientation: {self.position}\n", font_format)
        cursor.insertText(f"Positive Crack Probability: {self.crack}\n", font_format)
        cursor.insertText(f"Negative Crack Probability: {self.no_crack}\n", font_format)
        cursor.insertText(f"Location of Crack: {self.loc}\n", font_format)
        cursor.insertText(f"Crack Type: {self.type}\n", font_format)
        cursor.insertText(f"Crack Progression: {self.prog}\n", font_format)
        cursor.insertText(f"Date Added: {self.date}\n", font_format)

        painter = QPainter()
        if painter.begin(printer):
            doc.setPageSize(QSizeF(printer.pageRect().size()))
            doc.drawContents(painter)
            painter.end()

        preview = QPrintPreviewDialog(printer)
        preview.paintRequested.connect(doc.print_)
        preview.exec_()

    def delete_result(self):
        try:
            with open('image_id.txt', 'r') as f:
                result_id = f.read()
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, 'Projects.db')
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            try:
                # Ask the user for confirmation before deleting the record
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("Are you sure you want to delete this record?")
                msg_box.setWindowTitle("Confirmation")
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                response = msg_box.exec_()
                if response == QMessageBox.Yes:
                    self.c.execute("DELETE FROM Save_Files WHERE id = ?", (result_id,))
                    self.conn.commit()
                    self.Dialog.close()
                    print("Record deleted successfully")
                else:
                    print("Deletion cancelled by user")
            except Exception as e:
                print(f"Error deleting record: {e}")
            finally:
                self.conn.close()

        except Exception as e:
            print(e)

    def update_result(self):
        with open('image_id.txt', 'r') as f:
            result_id = f.read()
        new_remark = 'New_Remark.txt'
        if os.path.isfile(new_remark):
            with open(new_remark, 'r') as f:
                self.input_txt = f.read()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("No Changes")
            msg_box.setText("You did not make any changes.")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.exec_()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'Projects.db')
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        try:
            self.c.execute("UPDATE Save_Files SET remarks = ? WHERE id = ?", (self.input_txt, result_id))
            self.conn.commit()
            print("Record updated successfully")
            os.remove(new_remark)
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Update Successfully!")
            msg_box.setText("Record updated successfully.")
            msg_box.setInformativeText("Are you sure you want to exit?")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            response = msg_box.exec_()
            if response == QMessageBox.Yes:
                self.Dialog.close()
                self.background_widget.hide()
        except Exception as e:
            print(f"Error updating record: {e}")
        finally:
            self.conn.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.concretecracked_2.setText(_translate("Dialog", "Detected:"))
        self.label_2.setText(_translate("Dialog", "Length:"))
        self.label_3.setText(_translate("Dialog", "Width: "))
        self.widgetPosition.setText(_translate("Dialog", "Orientation:"))
        self.view_details.setText(_translate("Dialog", "View Details"))
        self.update.setText(_translate("Dialog", "Update"))

    def fetch_save_files_of_projects(self):
        with open('image_id.txt', 'r') as f:
            result_id = f.read()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'Projects.db')
        # Create a connection to a SQLite database or create it if it doesn't exist
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        # create a table if it doesn't exist
        self.c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Save_Files' ''')
        if self.c.fetchone()[0] == 0:
            self.c.execute('''CREATE TABLE Save_Files (id INTEGER PRIMARY KEY, folder_name TEXT, 
                                image_result BLOB, image_original BLOB,  width TEXT, 
            length TEXT, position TEXT, No_Crack TEXT, Crack TEXT, Status TEXT, selected_loc TEXT, selected_type 
            TEXT, selected_prog TEXT, remarks TEXT created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        # fetch data from the database
        self.c.execute("SELECT * FROM Save_Files WHERE id = ?", (result_id,))
        data = self.c.fetchall()
        print(data)
        return data

    def view_details_function(self):
        Function_Dialog = QDialog()
        self.details_dialog = Function_Dialog
        Function_Dialog.setObjectName("Dialog")
        Function_Dialog.resize(372, 398)
        Function_Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Function_Dialog.setStyleSheet("#Dialog{background:rgb(255, 255, 255); border:1px solid grey;}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Function_Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_6 = QtWidgets.QWidget(Function_Dialog)
        self.widget_6.setMinimumSize(QtCore.QSize(280, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.concretecracked_2 = QtWidgets.QLabel("Details:", self.widget_6)
        self.concretecracked_2.setStyleSheet("#concretecracked_2{\n"
                                             "    \n"
                                             "color: #2E74A9;\n"
                                             "font: bold;\n"
                                             "border: 2px solid white;\n"
                                             "font-size: 20px;\n"
                                             "border-bottom-color: rgb(172, 172, 172);\n"
                                             "}")
        self.concretecracked_2.setAlignment(QtCore.Qt.AlignCenter)
        self.concretecracked_2.setWordWrap(True)
        self.concretecracked_2.setObjectName("concretecracked_2")
        self.verticalLayout_2.addWidget(self.concretecracked_2)
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel("Location of Crack:", self.widget_10)
        self.label_2.setStyleSheet("#label_2{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.location_label = QtWidgets.QLabel(self.widget_10)
        self.location_label.setMinimumSize(QtCore.QSize(134, 0))
        self.location_label.setMaximumSize(QtCore.QSize(134, 16777215))
        self.location_label.setStyleSheet("#location_label{\n"
                                          "    color:  #555555;\n"
                                          "font: bold;\n"
                                          "    font-size: 15px}")
        self.location_label.setAlignment(QtCore.Qt.AlignCenter)
        self.location_label.setWordWrap(True)
        self.location_label.setObjectName("location_label")
        self.horizontalLayout_10.addWidget(self.location_label)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_13 = QtWidgets.QWidget(self.widget_6)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel("Crack Type:", self.widget_13)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.type_label = QtWidgets.QLabel(self.widget_13)
        self.type_label.setMinimumSize(QtCore.QSize(134, 0))
        self.type_label.setMaximumSize(QtCore.QSize(134, 16777215))
        self.type_label.setStyleSheet("#type_label{\n"
                                      "    color:  #555555;\n"
                                      "font: bold;\n"
                                      "    font-size: 15px;\n"
                                      "}")
        self.type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.type_label.setWordWrap(True)
        self.type_label.setObjectName("type_label")
        self.horizontalLayout_11.addWidget(self.type_label)
        self.verticalLayout_2.addWidget(self.widget_13)
        self.widget_11 = QtWidgets.QWidget(self.widget_6)
        self.widget_11.setObjectName("widget_11")

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widgetPosition = QtWidgets.QLabel("Crack Progression:", self.widget_11)
        self.widgetPosition.setStyleSheet("#widgetPosition{\n"
                                          "color: rgba(111, 75, 39, 0.77);\n"
                                          "font-size: 13px;\n"
                                          "font-weight: bold;\n"
                                          "}")
        self.widgetPosition.setObjectName("widgetPosition")
        self.horizontalLayout_13.addWidget(self.widgetPosition)
        self.prog_label = QtWidgets.QLabel(self.widget_11)
        self.prog_label.setMinimumSize(QtCore.QSize(134, 0))
        self.prog_label.setMaximumSize(QtCore.QSize(134, 16777215))
        self.prog_label.setStyleSheet("#prog_label{\n"
                                      "    color:  #555555;\n"
                                      "font: bold;\n"
                                      "    font-size: 15px;\n"
                                      "}")
        self.prog_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prog_label.setWordWrap(True)
        self.prog_label.setObjectName("prog_label")
        self.horizontalLayout_13.addWidget(self.prog_label)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_6)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QtWidgets.QLabel("Date Added:", self.widget_12)
        self.label_4.setStyleSheet("#label_4{\n"
                                   "color: rgba(111, 75, 39, 0.77);\n"
                                   "font-size: 13px;\n"
                                   "font-weight: bold;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.date_added = QtWidgets.QLabel(self.widget_12)
        self.date_added.setMinimumSize(QtCore.QSize(134, 0))
        self.date_added.setMaximumSize(QtCore.QSize(134, 16777215))
        self.date_added.setStyleSheet("#date_added{\n"
                                      "    color:  #555555;\n"
                                      "font: bold;\n"
                                      "    font-size: 15px}")
        self.date_added.setAlignment(QtCore.Qt.AlignCenter)
        self.date_added.setWordWrap(True)
        self.date_added.setObjectName("date_added")
        self.horizontalLayout_12.addWidget(self.date_added)
        self.verticalLayout_2.addWidget(self.widget_12)
        self.widget_15 = QtWidgets.QWidget(self.widget_6)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_15)
        self.widget.setStyleSheet("#widget{\n"
                                  "    \n"
                                  "border: 2px solid white;\n"
                                  "border-bottom-color: rgb(172, 172, 172);;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widgetPos_2 = QtWidgets.QLabel("Remarks:", self.widget)
        self.widgetPos_2.setMinimumSize(QtCore.QSize(180, 0))
        self.widgetPos_2.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widgetPos_2.setStyleSheet("#widgetPos_2{\n"
                                       "color: rgba(111, 75, 39, 0.77);\n"
                                       "font-size: 13px;\n"
                                       "font-weight: bold;\n"
                                       "}")
        self.widgetPos_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.widgetPos_2.setWordWrap(True)
        self.widgetPos_2.setObjectName("widgetPos_2")
        self.horizontalLayout_2.addWidget(self.widgetPos_2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.edit_remarks = QtWidgets.QPushButton(self.widget)
        self.edit_remarks.setMinimumSize(QtCore.QSize(23, 23))
        self.edit_remarks.setMaximumSize(QtCore.QSize(23, 23))
        self.edit_remarks.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_remarks.setIcon(icon)
        self.edit_remarks.setIconSize(QtCore.QSize(20, 25))
        self.edit_remarks.setFlat(True)
        self.edit_remarks.setObjectName("edit_remarks")
        self.horizontalLayout_2.addWidget(self.edit_remarks)
        self.verticalLayout_3.addWidget(self.widget)
        self.remarks = QtWidgets.QLineEdit(self.widget_15)
        # Toggle QLineEdit widget between enabled/disabled
        is_enabled = self.remarks.isEnabled()
        self.remarks.setEnabled(not is_enabled)
        self.edit_remarks.clicked.connect(self.edit_remarks_enable)
        self.remarks.setMinimumSize(QtCore.QSize(0, 50))
        self.remarks.setMaximumSize(QtCore.QSize(16777215, 50))
        self.remarks.setStyleSheet("#remarks{\n"
                                   "    color:  #555555;\n"
                                   "font: bold;\n"
                                   "    font-size: 15px;\n"
                                   "}")
        self.remarks.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.remarks.setObjectName("remarks")
        self.verticalLayout_3.addWidget(self.remarks)
        self.verticalLayout_2.addWidget(self.widget_15)
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.savebtn = QtWidgets.QPushButton("Okay", self.widget_3)
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
        self.savebtn.clicked.connect(self.edit_remarks_function)
        self.horizontalLayout_5.addWidget(self.savebtn)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_6)
        data = self.fetch_save_files_of_projects()
        if data:
            try:
                loc = data[0][10]
                type = data[0][11]
                prog = data[0][12]
                remarks = data[0][13]
                date = data[0][14]

                self.location_label.setText(loc)
                self.type_label.setText(type)
                self.prog_label.setText(prog)

                new_remark = 'New_Remark.txt'
                if os.path.isfile(new_remark):
                    with open(new_remark, 'r') as f:
                        self.input_txt = f.read()
                        self.remarks.setText(self.input_txt)
                else:
                    self.remarks.setText(remarks)
                self.date_added.setText(date)
            except Exception as e:
                print(e)
        else:
            print("No data found.")
        Function_Dialog.exec()

    def edit_remarks_enable(self):
        # Enable the QLineEdit
        self.remarks.setEnabled(True)

    def edit_remarks_function(self):
        try:
            self.input_remark = self.remarks.text()
            with open('New_Remark.txt', 'w') as f:
                f.write(self.input_remark)
        except Exception as e:
            print(e)
        self.details_dialog.close()
