from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QPushButton, QWidget
from PyQt5.QtGui import QTextDocument, QPainter, QPageLayout, QPageSize
from PyQt5.QtCore import Qt, QSize, QSizeF, QMarginsF
from PySide2.QtPrintSupport import QPrintPreviewDialog, QPrinter


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setGeometry(10, 10, 380, 280)

        self.printPreviewBtn = QPushButton("Print Preview", self)
        self.printPreviewBtn.setGeometry(300, 300, 90, 30)
        self.printPreviewBtn.clicked.connect(self.showPreview)

        self.setGeometry(100, 100, 400, 350)
        self.setWindowTitle("Print Preview Example")
        self.show()

    def showPreview(self):
        printer = QPrinter()
        pageLayout = QPageLayout(QPageSize(QPageSize.Letter), QPageLayout.Portrait, QMarginsF())
        printer.setPageLayout(pageLayout)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("preview.pdf")
        painter = QPainter()
        if painter.begin(printer):
            doc = QTextDocument()
            doc.setPlainText(self.textEdit.toPlainText())
            doc.setPageSize(QSizeF(printer.pageRect().size()))
            doc.drawContents(painter)
            painter.end()

        preview = QPrintPreviewDialog(printer)
        preview.exec_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
