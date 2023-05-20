import os
from collections import deque

import cv2
import keras
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QFile
from PyQt5.QtGui import QPixmap, QImage, QMovie
from PyQt5.QtWidgets import QDialog

from keras.applications.resnet import ResNet50, preprocess_input, decode_predictions
import tensorflow as tf

from resultsss import result_new_dialog


class getLength_of_crack(QThread):
    finished = pyqtSignal()

    def run(self):
        try:
            desired_size = (2500, 2500)
            self.img = cv2.imread('threshold_image.jpg')
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

            avg_width = sum(crack_widths) / len(crack_widths)
            avg_width_write = f"{avg_width:.2f}"
            print(f"Crack width: {avg_width:.2f} mm")
            with open('Predicted_width.txt', 'w') as f:
                f.write(avg_width_write)
            with open('Input_Distance.txt', 'w') as f:
                f.write(str(known_distance_cm))

            self.finished.emit()
        except Exception as e:
            print(e)


class NoiseRemovalThread(QThread):
    finished = pyqtSignal(np.ndarray)

    def __init__(self, thresholded):
        super().__init__()
        self.thresholded = thresholded

    def run(self):
        try:
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
        except Exception as e:
            print(e)


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

        try:
            if len(self.image.shape) == 2:
                height, width = self.image.shape
            else:
                print("Error: Image has invalid shape")
                return

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

        except Exception as e:
            print(e)


def is_black(pixel):
    return pixel == 0


class ImageProcessingThread(QThread):
    finished = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def run(self):
        try:
            # Load and process the image here
            image = cv2.imread(self.image_path)
            # Save the image to a temporary file
            temp_file_path = 'temp_image_original.jpg'
            cv2.imwrite(temp_file_path, image)
            # Check if the image is valid
            if image is not None:
                self.imageCnn = cv2.resize(image, (224, 224))
                self.imageCnn = np.expand_dims(self.imageCnn, axis=0)
                self.imageCnn = preprocess_input(self.imageCnn)

                self.modelCnn = keras.models.load_model('resnet_model_cnn.h5')
                predictions = self.modelCnn.predict(self.imageCnn, verbose=0)

                kernel = np.array([[-1, -1, -1], [-1, 11, -1], [-1, -1, -1]])

                # 1. sharpen the image to fine-tune the edges using the kernel
                sharpen = cv2.filter2D(image, -1, kernel)
                # 2. filter out small edges by using blur method
                blurred = cv2.GaussianBlur(sharpen, (3, 3), 0)
                # 3. convert image to grayscale
                gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
                # 4. convert grayscale image to binary image
                (T, threshInv) = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
                # 5. detect contours in binary image
                contours, h = cv2.findContours(threshInv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                # reverse the colors
                threshInv = 255 - threshInv

                # cv2.imwrite('result.png', threshInv)

                score = tf.nn.softmax(predictions)
                print(score)
                class_names = ['No Detected Crack', 'Contains Crack']

                # Get the index of the predicted class
                predicted_class_index = np.argmax(score, axis=1)[0]

                # Get the name and score of the predicted class
                predicted_class_name = class_names[predicted_class_index]

                predicted_class_score = 100 * score[0][predicted_class_index]
                if predicted_class_index == 0:
                    predicted_Negative_score = predicted_class_score
                    predicted_Positive_score = 100 - predicted_Negative_score
                else:
                    predicted_Positive_score = predicted_class_score
                    predicted_Negative_score = 100 - predicted_Positive_score

                print(f"Positive crack probability: {predicted_Positive_score:.2f}%")
                print(f"Negative crack probability: {predicted_Negative_score:.2f}%")
                Negative_score = f"{predicted_Negative_score:.2f}%"
                Positive_score = f"{predicted_Positive_score:.2f}%"
                with open('Negative_score.txt', 'w') as f:
                    f.write(Negative_score)
                with open('Positive_score.txt', 'w') as f:
                    f.write(Positive_score)
                with open('Predicted_Class_name.txt', 'w') as f:
                    f.write(predicted_class_name)
                self.finished.emit(threshInv)

            else:
                self.error.emit("Invalid image format")

        except Exception as e:
            print(e)
            self.error.emit(str(e))


class Detect_Crack_Dialog(object):

    def __init__(self, image_path, background_widget, history, projects, mainwindow):
        self.Mainwindow = mainwindow
        self.image_path = image_path
        self.myProjects = projects
        self.history = history
        self.background_widget = background_widget

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 430)
        Dialog.setMinimumSize(QtCore.QSize(750, 430))
        Dialog.setMaximumSize(QtCore.QSize(750, 430))
        self.Dialog = Dialog
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setStyleSheet("background-color:rgb(255,255,255);")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_7 = QtWidgets.QWidget(Dialog)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setStyleSheet("#label{\n"
                                   "    font: 200 17pt \"Segoe UI Black\";\n"
                                   "    color: rgba(111, 75, 39, 0.77);}")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.exit_2 = QtWidgets.QPushButton(self.widget_7)
        self.exit_2.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_2.setMaximumSize(QtCore.QSize(30, 30))
        self.exit_2.clicked.connect(Dialog.close)
        self.exit_2.clicked.connect(self.background_widget.hide)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_2.setIcon(icon)
        self.exit_2.setFlat(True)
        self.exit_2.setObjectName("exit_2")
        self.horizontalLayout_7.addWidget(self.exit_2)
        self.verticalLayout_6.addWidget(self.widget_7)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(350, 350))
        self.widget_2.setMaximumSize(QtCore.QSize(350, 350))
        self.widget_2.setStyleSheet("#widget_2{\n"
                                    "    \n"
                                    "border: 3px solid white;\n"
                                    "border-color: rgb(172, 172, 172);;\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        image = cv2.imread(self.image_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        self.upload_image = QtWidgets.QLabel(self.widget_2)
        self.upload_image.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_image.setStyleSheet(
            "  background-color: transparent; ")
        self.upload_image.setMinimumSize(QtCore.QSize(300, 300))
        self.upload_image.setMinimumSize(QtCore.QSize(300, 300))
        self.upload_image.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.upload_image.setObjectName("upload_image")
        self.horizontalLayout_3.addWidget(self.upload_image)

        self.update_image(rgb_image)

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(0, 6, 0, 65)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_41 = QtWidgets.QWidget(self.widget_3)
        self.widget_41.setObjectName("widget_4")
        self.widget_41.setMinimumSize(QtCore.QSize(16777215, 78))
        self.widget_41.setMaximumSize(QtCore.QSize(16777215, 78))
        self.verticalLayout.addWidget(self.widget_41)
        self.loc_widget = QtWidgets.QWidget(self.widget_3)
        self.loc_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.loc_widget.setObjectName("loc_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.loc_widget)
        self.verticalLayout_3.setContentsMargins(32, 0, 32, 9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.loc_widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("#label_2 {\n"
                                   "font-family: \'Franklin Gothic Medium\';\n"
                                   "font-size: 17px;\n"
                                   "color: \n"
                                   "#664323;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.loc_box = QtWidgets.QComboBox(self.loc_widget)
        self.loc_box.addItems([
            "Column",
            "Beam",
            "Slab (Suspended)",
            "Slab (On Grid)",
            "Walls",
            "Window Edges",
            "Door Edges",
            "Canopy",
            "Roof Deck"
        ])
        self.loc_box.setStyleSheet("#loc_box {\n"
                                   "        border-radius: 10px;\n"
                                   "        font-size: 18px;\n"
                                   "        font-family: Arial;\n"
                                   "color:rgb(144, 115, 87);"
                                   "        background-color: #fff;\n"
                                   "        border: 2px solid #aaa;\n"
                                   "        padding: 2px;\n"
                                   "padding-left:8px;\n"
                                   "    }\n"
                                   "\n"
                                   "#loc_box::drop-down{\n"
                                   " image:url(images/arrowdown.png);\n"
                                   " width: 15px;\n"
                                   " height: 15px;\n"
                                   "padding: 6px;\n"
                                   "}\n"
                                   "#loc_box::drop-down::pressed{\n"
                                   " image:url(images/arrowup.png);\n"
                                   "width: 15px;\n"
                                   " height: 15px;\n"
                                   "text-align: center;\n"
                                   "}\n"
                                   "#loc_box QAbstractItemView {\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "outline: none;\n"
                                   "color:rgb(144, 115, 87);"
                                   " text-align: center;}\n"
                                   "\n"
                                   "#loc_box QAbstractItemView::item {\n"
                                   "background-color: #F4EBE6;\n"
                                   " color: #4A3B28;\n"
                                   "color:rgb(144, 115, 87);"
                                   " text-align: center;\n"
                                   "min-height: 35px; min-width: 50px;\n"
                                   " border:0px;}\n"
                                   "\n"
                                   "#loc_box QListView{\n"
                                   "border: none;\n"
                                   " font-weight:bold;\n"
                                   "color:rgb(144, 115, 87);"
                                   " text-align: center;}\n"
                                   "#loc_box QListView::item{border:0px;\n"
                                   "border-radius: 15px;\n"
                                   "  padding:8px; \n"
                                   "margin:5px;}\n"
                                   "#loc_box QListView::item:selected { \n"
                                   "color: white; \n"
                                   "background-color: #4A3B28}")
        self.loc_box.setObjectName("loc_box")
        self.verticalLayout_3.addWidget(self.loc_box)
        self.verticalLayout.addWidget(self.loc_widget)
        self.remarks_widget = QtWidgets.QWidget(self.widget_3)
        self.remarks_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.remarks_widget.setObjectName("remarks_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.remarks_widget)
        self.verticalLayout_2.setContentsMargins(0, 9, 5, 9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.remarks_widget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setStyleSheet("#label_6 {\n"
                                   "font-family: \'Franklin Gothic Medium\';\n"
                                   "font-size: 15px;\n"
                                   "color: \n"
                                   "#664323;\n"
                                   "}")
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.widget_9 = QtWidgets.QWidget(self.remarks_widget)
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setContentsMargins(30, 9, 63, 9)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.widget_9)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/i.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(28, 28))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.NumOfDistance = QtWidgets.QLineEdit(self.widget_9)
        self.NumOfDistance.setMinimumSize(QtCore.QSize(0, 30))
        self.NumOfDistance.setMaximumSize(QtCore.QSize(40, 40))
        self.NumOfDistance.setToolTipDuration(8)
        self.NumOfDistance.setAlignment(QtCore.Qt.AlignCenter)
        self.NumOfDistance.setObjectName("NumOfDistance")
        self.horizontalLayout_4.addWidget(self.NumOfDistance)
        self.units = QtWidgets.QComboBox(self.widget_9)
        self.units.setEnabled(True)
        self.units.setMinimumSize(QtCore.QSize(0, 30))
        self.units.addItems(["Millimeter (mm)", "Centimeter (cm)", "Inch (in)", "Foot (ft)", "Yard (yd)", "Meter (m)"])
        self.units.setStyleSheet("#units {\n"
                                 "        border-radius: 10px;\n"
                                 "        font-size: 18px;\n"
                                 "        font-family: Arial;\n"
                                 "color:rgb(144, 115, 87);"
                                 "        background-color: #fff;\n"
                                 "        border: 2px solid #aaa;\n"
                                 "        padding: 2px;\n"
                                 "padding-left:8px;\n"
                                 "    }\n"
                                 "\n"
                                 "#units::drop-down{\n"
                                 " image:url(images/arrowdown.png);\n"
                                 " width: 15px;\n"
                                 " height: 15px;\n"
                                 "padding: 6px;\n"
                                 "}\n"
                                 "#units::drop-down::pressed{\n"
                                 " image:url(images/arrowup.png);\n"
                                 "width: 15px;\n"
                                 " height: 15px;\n"
                                 "text-align: center;\n"
                                 "}\n"
                                 "#units QAbstractItemView {\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "outline: none;\n"
                                 "color:rgb(144, 115, 87);"
                                 " text-align: center;}\n"
                                 "\n"
                                 "#units QAbstractItemView::item {\n"
                                 "background-color: #F4EBE6;\n"
                                 " color: #4A3B28;\n"
                                 "color:rgb(144, 115, 87);"
                                 " text-align: center;\n"
                                 "min-height: 35px; min-width: 50px;\n"
                                 " border:0px;}\n"
                                 "\n"
                                 "#units QListView{\n"
                                 "border: none;\n"
                                 " font-weight:bold;\n"
                                 "color:rgb(144, 115, 87);"
                                 " text-align: center;}\n"
                                 "#loc_box QListView::item{border:0px;\n"
                                 "border-radius: 15px;\n"
                                 "  padding:8px; \n"
                                 "margin:5px;}\n"
                                 "#units QListView::item:selected { \n"
                                 "color: white; \n"
                                 "background-color: #4A3B28}")
        self.units.setObjectName("units")
        self.units.setAutoFillBackground(False)
        self.horizontalLayout_4.addWidget(self.units)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.verticalLayout.addWidget(self.remarks_widget)

        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setContentsMargins(80, 0, 80, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.proceed = QtWidgets.QPushButton(self.widget_4)
        self.proceed.setMinimumSize(QtCore.QSize(0, 35))
        self.proceed.setMaximumSize(QtCore.QSize(400, 35))
        self.proceed.setStyleSheet("#proceed{\n"
                                   "background: #2E74A9;\n"
                                   "font-weight:bold;\n"
                                   "color: white;\n"
                                   "border-radius: 7px;\n"
                                   "font-family: Inter;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "#proceed::hover{\n"
                                   "color: #2E74A9;\n"
                                   "border : 3px solid  #2E74A9;\n"
                                   "background-color: white;\n"
                                   "}\n"
                                   "")
        self.proceed.setObjectName("proceed")
        self.proceed.clicked.connect(self.proceed_to_result)
        self.horizontalLayout_5.addWidget(self.proceed)
        self.verticalLayout.addWidget(self.widget_4)

        self.widget_41 = QtWidgets.QWidget(self.widget_3)
        self.widget_41.setObjectName("widget_4")
        self.verticalLayout.addWidget(self.widget_41)

        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_6.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def proceed_to_result(self):
        try:
            try:
                distance = float(self.NumOfDistance.text())
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

        except Exception as e:
            print(e)
        try:
            selected_loc = self.loc_box.currentIndex()
            if selected_loc == -1:
                self.loc_box.setCurrentIndex(0)
                selected_loc = 0
            selected_text_loc = self.loc_box.itemText(selected_loc)

            selected_text_type = "None"

            selected_text_prog = "None"

            with open('Selected_location_crack.txt', 'w') as f:
                f.write(selected_text_loc)

            with open('Selected_type_crack.txt', 'w') as f:
                f.write(selected_text_type)

            with open('Selected_progression_crack.txt', 'w') as f:
                f.write(selected_text_prog)
            try:
                self.load_dialog = self.loading()
                self.load_dialog.show()
                self.background_widget.show()

                # Create a new thread for the image processing task
                self.thread = ImageProcessingThread(self.image_path)
                self.thread.start()
                self.thread.finished.connect(lambda image_result: self.on_processing_finished(image_result))

            except Exception as e:
                print(e)
            self.Dialog.close()
        except Exception as e:
            print(e)

    def on_processing_finished(self, image_result):
        try:
            file_path_Class = 'Predicted_Class_name.txt'
            if os.path.isfile(file_path_Class):
                with open(file_path_Class, 'r') as f:
                    status = f.read()
                    if status == 'No Detected Crack':
                        self.getLength_of_crack_function_finish()
                    else:
                        try:
                            self.load_dialog.show()
                            _, self.thresholded = cv2.threshold(image_result, 50, 255, cv2.THRESH_BINARY)
                            # Create the noise removal thread and start it
                            self.noise_thread = NoiseRemovalThread(self.thresholded)
                            self.noise_thread.start()
                            self.noise_thread.finished.connect(self.show_result_noise)
                        except Exception as e:
                            print(e)
        except Exception as e:
            print(e)

    def show_result_noise(self, result):
        self.result = result
        temp_file_path = 'temp_image_result.jpg'
        cv2.imwrite(temp_file_path, self.result)

        self.load_dialog.close()
        self.getWidth_of_crack_function(self.result)

    def getWidth_of_crack_function(self, result):
        try:
            self.load_dialog_measure = self.loading_measuring()
            self.load_dialog_measure.show()

            self.compute_thread_width = getWidth_of_crack(float(self.NumOfDistance.text()),
                                                          self.units.currentText(), 132.28, result)
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
        try:
            self.load_dialog_measure.close()
            result_dialog = QtWidgets.QDialog(self.Mainwindow)
            ui = result_new_dialog(self.background_widget, self.history, self.myProjects, self.Mainwindow)
            ui.setupUi(result_dialog)
            x = (self.Mainwindow.width() - result_dialog.width()) // 2
            y = (self.Mainwindow.height() - result_dialog.height()) // 2
            result_dialog.move(x, y)
            result_dialog.exec_()
            print("Finish length")
        except Exception as e:
            print("getLength_of_crack_function_finish", e)
            self.load_dialog.close()
            result_dialog = QtWidgets.QDialog(self.Mainwindow)
            ui = result_new_dialog(self.background_widget, self.history, self.myProjects, self.Mainwindow)
            ui.setupUi(result_dialog)
            x = (self.Mainwindow.width() - result_dialog.width()) // 2
            y = (self.Mainwindow.height() - result_dialog.height()) // 2
            result_dialog.move(x, y)
            result_dialog.exec_()

    def update_image(self, image):
        # Get the size of the label
        self.upload_image.setAlignment(QtCore.Qt.AlignCenter)
        label_size = self.upload_image.size()

        # Convert the image to a QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.upload_image.setPixmap(pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

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

    def loading(self):
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
        self.label_process = QtWidgets.QLabel("Processing image for crack detection...", self.widget)
        self.label_process.setStyleSheet("background-color:#ffffff;\n"
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Location: "))
        # self.label_3.setText(_translate("Dialog", "Crack Type: "))

        # self.label_4.setText(_translate("Dialog", "Crack Progression: "))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p align='center'>Distance between the camera and concrete:</p></body></html>"))

        self.pushButton.setToolTip(
            _translate("Dialog", "Please input the distance between the camera and the concrete surface in \n"
                                 "order to calculate the length and width of any present cracks in the image."))
        self.proceed.setToolTip(_translate("Dialog", "Proceed to result"))
        self.proceed.setText(_translate("Dialog", "Proceed"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Detect_Crack_Dialog(None, None, None, None, None)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
