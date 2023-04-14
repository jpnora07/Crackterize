import os
from collections import deque

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap, QMovie
from PyQt5.QtWidgets import QMessageBox, QDialog, QFrame

from result import Result_Dialog
from Crack_Line_Length import Line_length


class NoiseRemovalThread(QThread):
    finished = pyqtSignal(np.ndarray)

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
        cv2.imwrite("threshold_image.jpg", result)
        self.finished.emit(result)


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


class getWidth_of_crack(QThread):
    finished = pyqtSignal()

    def __init__(self, distance, unit, focal_length, result_image):
        super().__init__()
        self.distance = distance
        self.unit = unit
        self.focal_length = focal_length
        self.result = result_image

    def run(self):
        try:
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
            for y in range(self.result.shape[0]):
                left_edge, right_edge = None, None
                for x in range(self.result.shape[1]):
                    if self.result[y, x] == 0:
                        if left_edge is None:
                            left_edge = x
                        right_edge = x
                if left_edge is not None and right_edge is not None:
                    width = right_edge - left_edge
                    # Convert pixel width to mm
                    width_mm = width * known_distance_cm / self.focal_length
                    crack_widths.append(width_mm)

            with open('Input_Distance.txt', 'w') as f:
                f.write(str(known_distance_cm))
            avg_width = sum(crack_widths) / len(crack_widths)
            avg_width_write = f"{avg_width:.2f}"
            print(f"Crack width: {avg_width:.2f} mm")
            with open('Predicted_width.txt', 'w') as f:
                f.write(avg_width_write)

            self.finished.emit()
        except Exception as e:
            print(e)


class getLength_of_crack(QThread):
    finished = pyqtSignal()

    def run(self):
        try:
            self.img = cv2.imread('threshold_image.jpg')
            desired_size = (2500, 2500)
            self.img = cv2.resize(self.img, desired_size)
            self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(self.gray, 50, 255, apertureSize=3)
            edges = cv2.dilate(edges, None, iterations=1)
            edges = cv2.erode(edges, None, iterations=1)
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            boxes = []
            self.box_lengths = []
            self.widths = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if area < 50:
                    continue
                x, y, w, h = cv2.boundingRect(contour)
                new_box = [x, y, x + w, y + h]
                overlaps = False
                for box in boxes:
                    if box[2] > new_box[0] and new_box[2] > box[0] and box[3] > new_box[1] and new_box[3] > box[1]:
                        overlaps = True
                        break
                if not overlaps:
                    boxes.append(new_box)
                    cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    roi_edges = edges[y:y + h, x:x + w]
                    if np.sum(roi_edges[:int(h / 2), :int(w / 2)]) > np.sum(roi_edges[int(h / 2):, int(w / 2):]):
                        cv2.line(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    else:
                        cv2.line(self.img, (x + w, y), (x, y + h), (0, 255, 0), 2)

                    with open('Input_Distance.txt', 'r') as f:
                        dist = f.read()
                    distance_cm = float(dist)
                    angle_degrees = 47.8
                    angle_radians = np.deg2rad(angle_degrees)
                    length_pixels = np.sqrt(w ** 2 + h ** 2)
                    length_cm = distance_cm * np.tan(angle_radians) * length_pixels / 2000.0
                    if self.box_lengths:
                        self.box_lengths[-1] += length_cm
                    else:
                        self.box_lengths.append(
                            length_cm)
                    self.widths.append(h)

            total_length = sum(self.box_lengths)
            total_length_write = f"{total_length:.2f}"
            print(total_length_write + " cm")
            with open('Predicted_height.txt', 'w') as f:
                f.write(str(total_length_write))

            self.finished.emit()
        except Exception as e:
            print(e)


def is_black(pixel):
    return pixel == 0


class Ui_DialogSegment(object):
    def __init__(self, background_widget):
        self.background_widget = background_widget

    def setupUi(self, Dialog):

        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        Dialog.setMaximumSize(QtCore.QSize(700, 600))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setStyleSheet("#Dialog{\n"
                             "background-color: rgb(255,255,255);"
                             "width: fit-content;\n"
                             "heigth: fit-content;\n"
                             "block-size: fit-content;\n"
                             "} ")

        # Load image and convert to grayscale
        # image_path = sys.argv[1]
        # self.image = cv2.imread(image_path)
        self.image = cv2.imread('temp_image_original.jpg')
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setStyleSheet("#widget_2{\n"
                                    "background-color: rgb(255,255,255);"
                                    "width: fit-content;\n"
                                    "heigth: fit-content;\n"
                                    "block-size: fit-content;\n"
                                    "} ")
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(30, 30))
        self.label_5.setMaximumSize(QtCore.QSize(30, 30))
        self.label_5.setStyleSheet(
            "  background-color: transparent; ")
        self.label_5.setPixmap(QtGui.QPixmap("images/slider_1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_5.setWordWrap(False)
        self.label_5.setIndent(23)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setStyleSheet("#widget_7{\n"
                                    "background-color: rgb(255,255,255);"
                                    "width: fit-content;\n"
                                    "heigth: fit-content;\n"
                                    "block-size: fit-content;\n"
                                    "} ")
        self.widget_7.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setContentsMargins(9, 5, 5, 5)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.widget_7)
        self.label.setStyleSheet("#label{\n"
                                 "  background-color: transparent;  \n"
                                 "    font: 200 17pt \"Segoe UI Black\";\n"
                                 "    color: rgba(111, 75, 39, 0.77);}")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.exit = QtWidgets.QPushButton(self.widget_7)
        self.exit.setMinimumSize(QtCore.QSize(30, 30))
        self.exit.setMaximumSize(QtCore.QSize(30, 30))
        self.exit.clicked.connect(self.closeEvent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.horizontalLayout_6.addWidget(self.exit)
        self.horizontalLayout_5.addWidget(self.widget_7)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(Dialog)

        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(393, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setStyleSheet("#widget_8{\n"
                                    "    \n"
                                    "border: 3px solid white;\n"
                                    "border-color: rgb(172, 172, 172);;\n"
                                    "}")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.imageLabel = QtWidgets.QLabel(self.widget_8)
        self.imageLabel.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setStyleSheet(
            "  background-color: transparent; ")
        self.imageLabel.setMinimumSize(QtCore.QSize(400, 400))
        self.imageLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.update_image(self.gray)
        self.verticalLayout_8.addWidget(self.imageLabel)
        self.verticalLayout_6.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget_6)
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_9.setStyleSheet("#widget_9{\n"
                                    "border: 3px solid white;\n"
                                    "border-color: rgb(172, 172, 172);;\n"
                                    "}")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.threshold_slider = QtWidgets.QSlider(self.widget_9)
        self.threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_slider.setObjectName("threshold_slider")

        self.threshold_slider.setRange(0, 255)
        self.threshold_slider.setValue(128)
        self.threshold_slider.valueChanged.connect(self.adjust_threshold)
        # Connect the valueChanged signal of the slider to a function that updates the label
        self.threshold_slider.valueChanged.connect(self.update_slider_value_label)

        self.horizontalLayout_3.addWidget(self.threshold_slider)
        self.thresholderNum = QtWidgets.QLabel("0", self.widget_9)
        self.thresholderNum.setAlignment(QtCore.Qt.AlignCenter)
        self.thresholderNum.setFixedSize(40, 30)
        self.thresholderNum.setStyleSheet(
            "  background-color: transparent; ")
        self.thresholderNum.setObjectName("thresholderNum")
        self.horizontalLayout_3.addWidget(self.thresholderNum)
        self.verticalLayout_6.addWidget(self.widget_9)
        self.horizontalLayout_4.addWidget(self.widget_6)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(200, 500))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("#label_2{\n"
                                   "  background-color: transparent;  \n"
                                   "    \n"
                                   "color: #2E74A9;\n"
                                   "font: bold;\n"
                                   "font-size: 13px;\n"
                                   "border-bottom-color: rgb(172, 172, 172);;\n"
                                   "}")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.widget_10 = QtWidgets.QWidget(self.widget_3)
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NumOfDistance = QtWidgets.QTextEdit(self.widget_10)
        self.NumOfDistance.setEnabled(True)
        self.NumOfDistance.setMinimumSize(QtCore.QSize(0, 40))
        self.NumOfDistance.setMaximumSize(QtCore.QSize(50, 40))
        self.NumOfDistance.setAcceptDrops(True)
        self.NumOfDistance.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NumOfDistance.setAutoFillBackground(False)
        self.NumOfDistance.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.NumOfDistance.setStyleSheet("""
    #NumOfDistance {
        color: black;
        background-color: white;
        border: 1px solid gray;
        padding: 5px;
        text-align: center;
    
    }
""")
        self.NumOfDistance.setLineWidth(0)
        self.NumOfDistance.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.NumOfDistance.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.NumOfDistance.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.NumOfDistance.setReadOnly(False)
        self.NumOfDistance.setObjectName("NumOfDistance")
        self.horizontalLayout_2.addWidget(self.NumOfDistance)
        self.units = QtWidgets.QComboBox(self.widget_10)
        self.units.setMinimumSize(QtCore.QSize(100, 40))
        self.units.setMaximumSize(QtCore.QSize(16777215, 40))
        self.units.setObjectName("units")
        self.units.addItems(["Millimeter (mm)", "Centimeter (cm)", "Inch (in)", "Foot (ft)", "Yard (yd)", "Meter (m)"])
        self.units.setStyleSheet("#NumOfDistance{\n"
                                 "background-color:white;"
                                 "font-size:18px;\n"
                                 "text-allign:center;\n"
                                 "border:1px solid grey;\n"
                                 "}")
        self.horizontalLayout_2.addWidget(self.units)
        self.verticalLayout_7.addWidget(self.widget_10)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(307, 120))
        self.widget_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.removeNoise = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeNoise.sizePolicy().hasHeightForWidth())
        self.removeNoise.setSizePolicy(sizePolicy)
        self.removeNoise.setMinimumSize(QtCore.QSize(0, 35))
        self.removeNoise.setMaximumSize(QtCore.QSize(400, 35))
        self.removeNoise.setStyleSheet("#removeNoise{\n"
                                       "font-weight:bold;\n"
                                       "color: white;\n"
                                       "background-color: #6F4B27;\n"
                                       "font-family: Inter;\n"
                                       "border-top-left-radius: 7px;\n"
                                       "border-top-right-radius:7px;\n"
                                       "border-bottom-left-radius: 7px;\n"
                                       "border-bottom-right-radius: 7px;\n"
                                       "text-align: center;\n"
                                       "}\n"
                                       "#removeNoise:hover{\n"
                                       "color: rgb(144,115,87);\n"
                                       "border : 3px solid rgb(144,115,87);\n"
                                       "background-color: white;\n"
                                       "}\n"
                                       "")
        self.removeNoise.setObjectName("removeNoise")
        self.removeNoise.clicked.connect(self.remove_noise)
        self.verticalLayout_2.addWidget(self.removeNoise)
        self.calculate = QtWidgets.QPushButton("Measure The Crack", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculate.sizePolicy().hasHeightForWidth())
        self.calculate.setSizePolicy(sizePolicy)
        self.calculate.setMinimumSize(QtCore.QSize(68, 35))
        self.calculate.setMaximumSize(QtCore.QSize(16777215, 35))
        self.calculate.setStyleSheet("#height{\n"
                                     "font-weight:bold;\n"
                                     "color: white;\n"
                                     "background-color: #6F4B27;\n"
                                     "font-family: Inter;\n"
                                     "border-top-left-radius: 7px;\n"
                                     "border-top-right-radius:7px;\n"
                                     "border-bottom-left-radius: 7px;\n"
                                     "border-bottom-right-radius: 7px;\n"
                                     "text-align: center;\n"
                                     "}\n"
                                     "#height:hover{\n"
                                     "color: rgb(144,115,87);\n"
                                     "border : 3px solid rgb(144,115,87);\n"
                                     "background-color: white;\n"
                                     "}\n"
                                     "")
        self.calculate.setObjectName("height")
        self.calculate.clicked.connect(self.getWidth_of_crack_function)
        # self.calculate.hide()
        self.verticalLayout_2.addWidget(self.calculate)
        self.verticalLayout_7.addWidget(self.widget_4)
        self.widget_11 = QtWidgets.QWidget(self.widget_3)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_7.addWidget(self.widget_11)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.proceed = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceed.sizePolicy().hasHeightForWidth())
        self.proceed.setSizePolicy(sizePolicy)
        self.proceed.setMinimumSize(QtCore.QSize(0, 35))
        self.proceed.setMaximumSize(QtCore.QSize(400, 35))
        self.proceed.setStyleSheet("#proceed{\n"
                                   "font-weight:bold;\n"
                                   "color: white;\n"
                                   "background-color: #2E74A9;\n"
                                   "font-family: Inter;\n"
                                   "border-top-left-radius: 7px;\n"
                                   "border-top-right-radius: 7px;\n"
                                   "border-bottom-left-radius: 7px;\n"
                                   "border-bottom-right-radius: 7px;\n"
                                   "text-align: center;\n"
                                   "}\n"
                                   "#proceed:hover{\n"
                                   "color: #2E74A9;\n"
                                   "border : 3px solid #2E74A9;\n"
                                   "background-color: white;\n"
                                   "}\n"
                                   "")

        self.proceed.clicked.connect(self.Proceed_to_Result)
        self.proceed.setObjectName("proceed")
        self.verticalLayout_3.addWidget(self.proceed)
        self.verticalLayout_7.addWidget(self.widget_5)
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        # Add transparent white background widget
        self.background_widget_segment = QFrame(self.Dialog)
        self.background_widget_segment.setStyleSheet("background-color: rgba(0, 0, 0, 0.25);")
        self.background_widget_segment.resize(self.Dialog.width(), self.Dialog.height())
        self.background_widget_segment.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Adjust Threshold"))
        self.label_2.setText(_translate("Dialog", "Distance between Crack and Camera"))
        self.removeNoise.setText(_translate("Dialog", "Denoise Image"))
        self.proceed.setText(_translate("Dialog", "Proceed"))

    def closeEvent(self):
        closeDialog = QDialog()
        self.closeDialog = closeDialog
        closeDialog.setWindowFlags(Qt.FramelessWindowHint)
        closeDialog.setObjectName("Dialog")
        closeDialog.setStyleSheet("#Dialog{background-color: rgb(255,255,255); border: 1px solid rgb(144,115,87);}")
        closeDialog.resize(356, 155)
        closeDialog.setMinimumSize(QtCore.QSize(356, 155))
        closeDialog.setMaximumSize(QtCore.QSize(356, 155))
        self.horizontalLayout = QtWidgets.QHBoxLayout(closeDialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(closeDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.exit = QtWidgets.QPushButton(self.widget_5)
        self.exit.setMinimumSize(QtCore.QSize(20, 20))
        self.exit.setMaximumSize(QtCore.QSize(30, 30))
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(closeDialog.close)
        self.horizontalLayout_5.addWidget(self.exit)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(25, 0, 20, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon = QtWidgets.QLabel(self.widget_2)
        self.icon.setMinimumSize(QtCore.QSize(50, 50))
        self.icon.setMaximumSize(QtCore.QSize(50, 50))
        self.icon.setPixmap(QtGui.QPixmap("images/question.png"))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setWordWrap(True)
        self.icon.setObjectName("icon")
        self.icon.setStyleSheet(
            "  background-color: transparent; ")
        self.horizontalLayout_2.addWidget(self.icon)
        self.message = QtWidgets.QLabel(self.widget_2)
        self.message.setStyleSheet("#message{\n"
                                   "  background-color: transparent;  \n"
                                   "font-family: \"Inter\";\n"
                                   "font-size: 13pt; \n"
                                   "color: #000000;\n"
                                   "font: bold;\n"
                                   "font-size: 13px;\n"
                                   "}")
        self.message.setScaledContents(True)
        self.message.setWordWrap(True)
        self.message.setText("Are you sure you want to exit?")
        self.message.setObjectName("message")
        self.horizontalLayout_2.addWidget(self.message)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 12, 12, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.Yes = QtWidgets.QPushButton("Yes", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Yes.sizePolicy().hasHeightForWidth())
        self.Yes.setSizePolicy(sizePolicy)
        self.Yes.setMinimumSize(QtCore.QSize(20, 32))
        self.Yes.setMaximumSize(QtCore.QSize(100, 32))
        self.Yes.clicked.connect(self.Delete_and_close)
        self.Yes.setStyleSheet("#Yes{\n"
                               "font-weight:bold;\n"
                               "color:  #6F4B27;\n"
                               "background-color: white;\n"
                               "font-family: Inter;\n"
                               "border-top-left-radius: 7px;\n"
                               "border-top-right-radius:7px;\n"
                               "border-bottom-left-radius: 7px;\n"
                               "border-bottom-right-radius: 7px;\n"
                               "text-align: center;\n"
                               "border : 3px solid #6F4B27;\n"
                               "}\n"
                               "#Yes:hover{\n"
                               "color: white;\n"
                               "background-color: #6F4B27;\n"
                               "}\n"
                               "")
        self.Yes.setObjectName("Yes")
        self.horizontalLayout_3.addWidget(self.Yes)
        self.No = QtWidgets.QPushButton("No", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.No.sizePolicy().hasHeightForWidth())
        self.No.setSizePolicy(sizePolicy)
        self.No.clicked.connect(closeDialog.close)
        self.No.setMinimumSize(QtCore.QSize(20, 32))
        self.No.setMaximumSize(QtCore.QSize(100, 32))
        self.No.setStyleSheet("#No{\n"
                              "font-weight:bold;\n"
                              "color: white;\n"
                              "background-color: #6F4B27;\n"
                              "font-family: Inter;\n"
                              "border-top-left-radius: 7px;\n"
                              "border-top-right-radius:7px;\n"
                              "border-bottom-left-radius: 7px;\n"
                              "border-bottom-right-radius: 7px;\n"
                              "text-align: center;\n"
                              "}\n"
                              "#No:hover{\n"
                              "color: #6F4B27;\n"
                              "border : 3px solid #6F4B27;\n"
                              "background-color: white;\n"
                              "}\n"
                              "")
        self.No.setObjectName("No")
        self.horizontalLayout_3.addWidget(self.No)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        closeDialog.exec()

    def Delete_and_close(self):
        Negative_score = "Negative_score.txt"
        Input_Distance = "Input_Distance.txt"
        Positive_score = "Positive_score.txt"
        Predicted_Class_name = "Predicted_Class_name.txt"
        self.Predicted_width = "Predicted_width.txt"
        self.Predicted_height = "Predicted_height.txt"
        self.Orientation = "Orientation.txt"
        Predicted_Score = "Predicted_Score.txt"
        threshold = "threshold_image.jpg"

        self.background_widget.hide()
        try:
            os.remove(threshold)
        except FileNotFoundError:
            print(f"{threshold} already removed or does not exist")
        try:
            os.remove(Input_Distance)
        except FileNotFoundError:
            print(f"{Input_Distance} already removed or does not exist")

        try:
            os.remove(Negative_score)
        except FileNotFoundError:
            print(f"{Negative_score} already removed or does not exist")

        try:
            os.remove(self.Orientation)
        except FileNotFoundError:
            print(f"{self.Orientation} already removed or does not exist")

        try:
            os.remove(Positive_score)
        except FileNotFoundError:
            print(f"{Positive_score} already removed or does not exist")

        try:
            os.remove(Predicted_Class_name)
        except FileNotFoundError:
            print(f"{Predicted_Class_name} already removed or does not exist")

        try:
            os.remove(self.Predicted_height)
        except FileNotFoundError:
            print(f"{self.Predicted_height} already removed or does not exist")

        try:
            os.remove(Predicted_Score)
        except FileNotFoundError:
            print(f"{Predicted_Score} already removed or does not exist")

        try:
            os.remove(self.Predicted_width)
        except FileNotFoundError:
            print(f"{self.Predicted_width} already removed or does not exist")
        self.closeDialog.close()
        self.Dialog.close()

    def Proceed_to_Result(self):

        Predicted_width = "Predicted_width.txt"
        Predicted_height = "Predicted_height.txt"
        try:
            # Check that the files exist and are not empty
            if not os.path.isfile(Predicted_width) or os.path.getsize(Predicted_width) == 0:
                icon_image = "images/info.png"
                message = "The image is not completely get the width and length of crack detected."
                self.QMessage_Error_dialog(message, icon_image)

                return

            if not os.path.isfile(Predicted_height) or os.path.getsize(Predicted_height) == 0:
                icon_image = "images/info.png"
                message = "The image is not completely get the length of crack detected."
                self.QMessage_Error_dialog(message, icon_image)
                return
        except Exception as e:
            print(e)
        # Create and show the Result_Dialog
        result_dialog = QtWidgets.QDialog(self.Dialog)

        x = (self.Dialog.width() - self.Dialog.width()) // 2
        y = (self.Dialog.height() - self.Dialog.height()) // 2
        ui = Result_Dialog(self.Dialog, self.background_widget, None)

        ui.setupUi(result_dialog)
        result_dialog.move(x, y)
        result_dialog.show()
        result_dialog.exec_()

    def remove_noise(self):
        # Check if the thresholded image is not empty
        if not hasattr(self, "thresholded") or self.thresholded is None:
            icon_image = "images/warning.png"
            message = "Please apply a threshold to the image first."
            self.QMessage_Error_dialog(message, icon_image)
            return

        try:

            self.load_dialog = self.loading_remove_noise()
            self.load_dialog.show()
            self.background_widget_segment.show()
            # Create the noise removal thread and start it
            self.noise_thread = NoiseRemovalThread(self.thresholded)
            self.noise_thread.start()
            self.noise_thread.finished.connect(self.show_result_noise)
        except AttributeError:
            icon_image = "images/info.png"
            message = "Thresholder value is empty."
            self.QMessage_Error_dialog(message, icon_image)
            return

    def show_result_noise(self, result):
        self.result = result
        self.update_image(result)
        self.load_dialog.close()
        self.background_widget_segment.hide()

    def getWidth_of_crack_function(self):

        try:
            distance = float(self.NumOfDistance.toPlainText())
        except ValueError:

            icon_image = "images/warning.png"
            message = "Please enter a valid distance."
            self.QMessage_Error_dialog(message, icon_image)

            return

        if not distance:
            icon_image = "images/warning.png"
            message = "Please enter a distance."
            self.QMessage_Error_dialog(message, icon_image)
            return

        try:

            # Check if the result from the previous thread is not empty or not done
            if not hasattr(self, "noise_thread") or not self.noise_thread.isFinished():
                icon_image = "images/warning.png"
                message = "Please denoise the image first."
                self.QMessage_Error_dialog(message, icon_image)

                return
            self.load_dialog_measure = self.loading_measuring()
            self.load_dialog_measure.show()
            self.background_widget_segment.show()

            self.compute_thread_width = getWidth_of_crack(float(self.NumOfDistance.toPlainText()),
                                                          self.units.currentText(), 132.28, self.result)
            self.compute_thread_width.start()
            self.compute_thread_width.finished.connect(self.getLength_of_crack_function)


        except Exception as e:
            print(e)

    def getLength_of_crack_function(self):
        print("Finish width")
        try:

            self.compute_thread_length = getLength_of_crack()
            self.compute_thread_length.start()
            self.compute_thread_length.finished.connect(self.getLength_of_crack_function_finish)

        except Exception as e:
            print(e)

    def getLength_of_crack_function_finish(self):
        self.load_dialog_measure.close()
        self.background_widget_segment.hide()
        print("Finish length")

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

    def adjust_threshold(self, value):
        # Apply thresholding
        _, self.thresholded = cv2.threshold(self.gray, value, 255, cv2.THRESH_BINARY)
        # Update the image on the label
        self.update_image(self.thresholded)

    def update_slider_value_label(self, value):
        self.thresholderNum.setText(str(value))

    def loading_remove_noise(self):
        Dialog = QDialog()
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 235)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setStyleSheet("background-color:#ffffff;")
        radius = 15
        Dialog.setStyleSheet("""
                                                            background:#EFEEEE;
                                                            border-top-left-radius:{0}px;
                                                            border-bottom-left-radius:{0}px;
                                                            border-top-right-radius:{0}px;
                                                            border-bottom-right-radius:{0}px;
                                                            """.format(radius))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color:#ffffff;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_process = QtWidgets.QLabel("Removing Noise...", self.widget)
        self.label_process.setStyleSheet(
            "  background-color: transparent;  \n"
            "font-size:20px;\n"
            "color: #6c757d;\n"
            "font-style: Inter;")
        self.label_process.setScaledContents(True)
        self.label_process.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_process.setWordWrap(True)
        self.label_process.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_process)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("background-color:#ffffff;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.movie = QMovie("images/spin_loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.setScaledContents(True)
        self.label.setStyleSheet(
            "  background-color: transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.show()
        return Dialog

    def loading_measuring(self):
        Dialog = QDialog()
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 235)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setStyleSheet("background-color:#ffffff;")
        radius = 15
        Dialog.setStyleSheet("""
                                                            background:#EFEEEE;
                                                            border-top-left-radius:{0}px;
                                                            border-bottom-left-radius:{0}px;
                                                            border-top-right-radius:{0}px;
                                                            border-bottom-right-radius:{0}px;
                                                            """.format(radius))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color:#ffffff;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_process = QtWidgets.QLabel("Calculating the Width and Length...", self.widget)
        self.label_process.setStyleSheet(
            "  background-color: transparent;  \n"
            "font-size:17px;\n"
            "color: #6c757d;\n"
            "font-style: Inter;")
        self.label_process.setScaledContents(True)
        self.label_process.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_process.setWordWrap(True)
        self.label_process.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_process)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("background-color:#ffffff;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.movie = QMovie("images/spin_loading.gif")
        self.label.setMovie(self.movie)
        self.label.setStyleSheet(
            "  background-color: transparent; ")
        self.movie.start()
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.show()
        return Dialog

    def QMessage_Error_dialog(self, message, icon_image):
        Dialog = QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 155)
        Dialog.setMinimumSize(QtCore.QSize(356, 155))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setMaximumSize(QtCore.QSize(356, 155))
        Dialog.setStyleSheet("#Dialog{background-color: rgb(255,255,255);border: 1px solid rgb(144,115,87);}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.exit = QtWidgets.QPushButton(self.widget_5)
        self.exit.setMinimumSize(QtCore.QSize(20, 20))
        self.exit.setMaximumSize(QtCore.QSize(30, 30))
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setFlat(True)
        self.exit.clicked.connect(Dialog.close)
        self.exit.setObjectName("exit")
        self.horizontalLayout_5.addWidget(self.exit)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(25, 0, 20, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon = QtWidgets.QLabel(self.widget_2)
        self.icon.setMinimumSize(QtCore.QSize(50, 50))
        self.icon.setMaximumSize(QtCore.QSize(50, 50))
        self.icon.setPixmap(QtGui.QPixmap(icon_image))
        self.icon.setScaledContents(True)
        self.icon.setStyleSheet(
            "  background-color: transparent; ")
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setWordWrap(True)
        self.icon.setObjectName("icon")
        self.horizontalLayout_2.addWidget(self.icon)
        self.message = QtWidgets.QLabel(self.widget_2)
        self.message.setText(message)
        self.message.setStyleSheet("#message{\n"
                                   "  background-color: transparent;  \n"
                                   "font-family: \"Inter\";\n"
                                   "font-size: 13pt; \n"
                                   "color: #000000;\n"
                                   "font: bold;\n"
                                   "font-size: 13px;\n"
                                   "}")
        self.message.setScaledContents(True)
        self.message.setWordWrap(True)
        self.message.setObjectName("message")
        self.horizontalLayout_2.addWidget(self.message)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 12, 12, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.okBtn = QtWidgets.QPushButton("Okay", self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okBtn.sizePolicy().hasHeightForWidth())
        self.okBtn.setSizePolicy(sizePolicy)
        self.okBtn.clicked.connect(Dialog.close)
        self.okBtn.setMinimumSize(QtCore.QSize(20, 32))
        self.okBtn.setMaximumSize(QtCore.QSize(100, 32))
        self.okBtn.setStyleSheet("#okBtn{\n"
                                 "font-weight:bold;\n"
                                 "color: white;\n"
                                 "background-color: #6F4B27;\n"
                                 "font-family: Inter;\n"
                                 "border-top-left-radius: 7px;\n"
                                 "border-top-right-radius:7px;\n"
                                 "border-bottom-left-radius: 7px;\n"
                                 "border-bottom-right-radius: 7px;\n"
                                 "text-align: center;\n"
                                 "}\n"
                                 "#okBtn:hover{\n"
                                 "color: rgb(144,115,87);\n"
                                 "border : 3px solid rgb(144,115,87);\n"
                                 "background-color: white;\n"
                                 "}\n"
                                 "")
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_3.addWidget(self.okBtn)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        Dialog.exec()
