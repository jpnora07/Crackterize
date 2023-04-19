import os
import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from PyQt5.QtWidgets import QSlider, QApplication
from PyQt5.QtGui import QPixmap, QImage, QMovie
from PyQt5.QtCore import Qt, QProcess
from PyQt5.QtCore import QThread, pyqtSignal
from collections import deque
class FindBlackBlocksThread(QThread):
    finished = pyqtSignal()
    progress_signal = pyqtSignal(int)
    result_signal = pyqtSignal(list)

    def __init__(self, image, nBlock):
        super().__init__()
        self.image = image
        self.nBlock = nBlock
        self.blocks = []

    def run(self):
        height, width = self.image.shape
        track = {}
        for y in range(height):
            for x in range(width):
                if is_black(self.image[y, x]) and (y, x) not in track:
                    stack = deque()
                    stack.append((y, x))
                    block = []
                    while stack:
                        cy, cx = stack.pop()
                        if (cy, cx) in track:
                            continue
                        track[(cy, cx)] = True
                        block.append((cy, cx))
                        for dy, dx in [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]:
                            ny, nx = cy + dy, cx + dx
                            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                                continue
                            if is_black(self.image[ny, nx]):
                                stack.append((ny, nx))
                    if len(block) >= self.nBlock:
                        self.blocks.append(block)

        self.result_signal.emit(self.blocks)
        self.finished.emit()

class CrackAnalyzer(QThread):

    def __init__(self, distance, unit, focal_length):
        super().__init__()
        self.distance = distance
        self.unit = unit
        self.focal_length = focal_length

    def get_Heigth_Width_Function(self, result):
        # Convert the known distance to centimeters
        if self.unit == "Millimeter (mm)":
            known_distance_cm = self.distance / 10
        elif self.unit == "Centimeter (cm)":
            known_distance_cm = self.distance
        elif self.unit == "Inch (in)":
            known_distance_cm = self.distance * 2.54
        elif self.unit == "Foot (ft)":
            known_distance_cm = self.distance * 30.48
        elif self.unit == "Yard (yd)":
            known_distance_cm = self.distance * 91.44
        elif self.unit == "Meter (m)":
            known_distance_cm = self.distance * 100
        else:
            print("Invalid unit selected")
            return

        # Measure the width of the crack
        crack_widths = []
        for y in range(result.shape[0]):
            left_edge, right_edge = None, None
            for x in range(result.shape[1]):
                if result[y, x] == 0:
                    if left_edge is None:
                        left_edge = x
                    right_edge = x
            if left_edge is not None and right_edge is not None:
                width = right_edge - left_edge
                # Convert pixel width to mm
                width_mm = width * known_distance_cm / self.focal_length
                crack_widths.append(width_mm)


        with open('../Input_Distance.txt', 'w') as f:
            f.write(str(known_distance_cm))
        avg_width = sum(crack_widths) / len(crack_widths)
        avg_width_write = f"{avg_width:.2f} cm"
        print(f"Crack width: {avg_width:.2f} mm")
        with open('../Predicted_width.txt', 'w') as f:
            f.write(avg_width_write)

class NoiseRemovalThread(QThread):
    finished = pyqtSignal(np.ndarray)
    progress_signal = pyqtSignal(int)

    def __init__(self, thresholded):
        super().__init__()
        self.thresholded = thresholded

    def run(self):
        nBlock = 130  # Threshold for black block size
        black_blocks_thread = FindBlackBlocksThread(self.thresholded, nBlock)
        black_blocks_thread.start()
        black_blocks_thread.wait()
        blocks = black_blocks_thread.blocks
        mask = np.zeros_like(self.thresholded, dtype=bool)
        for block in blocks:
            for y, x in block:
                mask[y, x] = True
        result = np.where(mask, self.thresholded, 255)
        cv2.imwrite("segment_img.jpg", result)
        self.finished.emit(result)

class Ui_MainWindow(object):
    signal_close = QtCore.pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Load image and convert to grayscale
        image_path = sys.argv[1]
        self.image = cv2.imread(image_path)
        #self.image = cv2.imread('images/10cm.jpg')
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


        self.imageLabel = QtWidgets.QLabel(self.widget_4)
        self.imageLabel.setMaximumSize(QtCore.QSize(500, 16777215))
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setFixedSize(600, 400)

        # Set the image on the label
        self.update_image(self.gray)
        self.horizontalLayout_4.addWidget(self.imageLabel)

        self.verticalLayout.addWidget(self.widget_4)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.thresholder = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.thresholder.sizePolicy().hasHeightForWidth())
        self.thresholder.setSizePolicy(sizePolicy)
        self.thresholder.setMaximumSize(QtCore.QSize(16777215, 50))
        self.thresholder.setObjectName("thresholder")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.thresholder)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.thresholderLbl = QtWidgets.QLabel("Threshold", self.thresholder)
        self.thresholderLbl.setMaximumSize(QtCore.QSize(50, 16777215))
        self.thresholderLbl.setObjectName("thresholderNum")
        self.thresholderLbl.setWordWrap(True)
        self.horizontalLayout_5.addWidget(self.thresholderLbl)

        self.threshold_slider = QSlider(Qt.Horizontal, self.thresholder)
        self.threshold_slider.setRange(0, 255)
        self.threshold_slider.setValue(128)
        self.threshold_slider.setFixedSize(250, self.thresholder.height())
        self.threshold_slider.valueChanged.connect(self.adjust_threshold)
        # Connect the valueChanged signal of the slider to a function that updates the label
        self.threshold_slider.valueChanged.connect(self.update_slider_value_label)
        self.horizontalLayout_5.addWidget(self.threshold_slider)

        self.progressBar = QtWidgets.QLabel("ad", self.thresholder)
        self.progressBar.setMaximumSize(QtCore.QSize(30, 30))
        self.progressBar.setObjectName("progressBar")
        # Loading the GIF
        self.movie = QMovie("../images/giphy.gif")
        self.progressBar.setMovie(self.movie)
        self.progressBar.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.movie.setScaledSize(QtCore.QSize(30, 30))
        # set the scaledContents property to True
        self.progressBar.setScaledContents(True)
        self.horizontalLayout_5.addWidget(self.progressBar)

        self.thresholderNum = QtWidgets.QLabel(self.thresholder)
        self.thresholderNum.setMaximumSize(QtCore.QSize(40, 16777215))
        self.thresholderNum.setObjectName("thresholderNum")
        self.horizontalLayout_5.addWidget(self.thresholderNum)


        self.horizontalLayout.addWidget(self.thresholder)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setMinimumSize(QtCore.QSize(10, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.distanceLbl = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distanceLbl.setFont(font)
        self.distanceLbl.setObjectName("distanceLbl")
        self.horizontalLayout_6.addWidget(self.distanceLbl)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.widget_7.setFont(font)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.NumOfDistance = QtWidgets.QTextEdit(self.widget_7)
        self.NumOfDistance.setMinimumSize(QtCore.QSize(0, 30))
        self.NumOfDistance.setMaximumSize(QtCore.QSize(50, 30))
        self.NumOfDistance.setObjectName("NumOfDistance")
        self.horizontalLayout_7.addWidget(self.NumOfDistance)

        self.units = QtWidgets.QComboBox(self.widget_7)
        self.units.setMinimumSize(QtCore.QSize(0, 30))
        self.units.setMaximumSize(QtCore.QSize(150, 30))
        self.units.setObjectName("units")
        self.units.addItems(["Millimeter (mm)", "Centimeter (cm)", "Inch (in)", "Foot (ft)", "Yard (yd)", "Meter (m)"])
        self.horizontalLayout_7.addWidget(self.units)

        self.verticalLayout_2.addWidget(self.widget_7)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.removeNoise = QtWidgets.QPushButton("Remove Noise", self.widget_2)
        self.removeNoise.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.removeNoise.setObjectName("removeNoise")
        self.removeNoise.clicked.connect(self.remove_noise)
        self.verticalLayout_3.addWidget(self.removeNoise)

        self.crop = QtWidgets.QPushButton("View Height",self.widget_2)
        self.crop.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.crop.setObjectName("crop")
        self.verticalLayout_3.addWidget(self.crop)
        self.crop.clicked.connect(self.Height)

        self.proceed = QtWidgets.QPushButton("Proceed", self.widget_2)
        self.proceed.setObjectName("proceed")
        self.proceed.clicked.connect(MainWindow.close)
        self.proceed.clicked.connect(self.Proceed_to_Result)
        self.verticalLayout_3.addWidget(self.proceed)

        self.process = QProcess()
        self.exit = QtWidgets.QPushButton("Exit", self.widget_2)
        self.exit.setObjectName("Exit")
        self.exit.clicked.connect(MainWindow.close)
        self.process.finished.connect(self.finished)
        self.verticalLayout_3.addWidget(self.exit)

        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.thresholderNum.setText(_translate("MainWindow", "0"))
        self.distanceLbl.setText(_translate("MainWindow", "Distance Between Crack and Camera"))

    def finished(self, exit_code, exit_status):
        # Re-enable the main window when the subprocess finishes
        self.centralwidget.setEnabled(True)
    def closeEvent(self, event):
        # emit the signal when the window is closed
        self.signal_close.emit()
        event.accept()

    def Proceed_to_Result(self):
        try:
            # Get the path to the directory where the executable is run from
            app_path = getattr(sys, '_MEIPASS', None) or os.path.abspath('..')

            # Create the path to the result.py file
            result_file_path = os.path.join(app_path, '../result.py')
            # Execute the result.py file using QProcess
            process = QtCore.QProcess()
            process.start('python', [result_file_path])

            if process.waitForFinished() == 0:
                print('Error: failed to execute result.py')
        except Exception as e:
            print(e)

    def Height(self):
        try:
            # Get the path to the directory where the executable is run from
            app_path = getattr(sys, '_MEIPASS', None) or os.path.abspath('..')

            # Create the path to the result.py file
            Crack_Line_Length = os.path.join(app_path, 'Crack_Line_Length.py')
            # Execute the result.py file using QProcess
            process = QtCore.QProcess()
            process.start('python', [Crack_Line_Length])

            if process.waitForFinished() == 0:
                print('Error: failed to execute result.py')
        except Exception as e:
            print(e)

    def update_image(self, image):
        # Get the size of the label
        label_size = self.imageLabel.size()

        # Resize the image to fit within the label while maintaining aspect ratio
        aspect_ratio = image.shape[1] / image.shape[0]
        new_width = label_size.height() * aspect_ratio
        new_height = label_size.height()
        resized_image = cv2.resize(image, (int(new_width), int(new_height)))

        # Convert the image to a QImage
        height, width = resized_image.shape
        q_image = QImage(resized_image.data, width, height, width, QImage.Format_Grayscale8)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.imageLabel.setPixmap(pixmap)

    # Function to adjust the threshold
    def adjust_threshold(self, value):
        # Apply thresholding
        _, self.thresholded = cv2.threshold(self.gray, value, 255, cv2.THRESH_BINARY)
        # Update the image on the label
        self.update_image(self.thresholded)

    # Function to update the slider value label
    def update_slider_value_label(self, value):
        self.thresholderNum.setText(str(value))

    # Function to remove noise
    def remove_noise(self):
        try:
            distance = float(self.NumOfDistance.toPlainText())
        except ValueError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "Please enter a valid distance.")
            return

        if not distance:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "Please enter a distance.")
            return

        try:
            # Create the noise removal thread and start it
            self.noise_thread = NoiseRemovalThread(self.thresholded)
            self.noise_thread.started.connect(self.on_noise_removal_started)
            self.noise_thread.finished.connect(self.on_noise_removal_finished)

            # Add progress bar to layout
            self.horizontalLayout_5.addWidget(self.progressBar)

            self.noise_thread.start()
        except AttributeError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "Thresholder value is empty.")
            return

    def on_noise_removal_started(self):
        self.movie.start()

    def on_noise_removal_finished(self, result):
        self.update_image(result)
        analyzer = CrackAnalyzer(float(self.NumOfDistance.toPlainText()), self.units.currentText(), 132.28)
        analyzer.get_Heigth_Width_Function(result)
        self.movie.stop()

def is_black(pixel):
    return pixel == 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
