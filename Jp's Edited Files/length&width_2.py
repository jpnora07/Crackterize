import os

from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QInputDialog, QSlider
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from collections import deque

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Load image and convert to grayscale
        #image_path = sys.argv[1]
        #self.image = cv2.imread(image_path)
        self.image = cv2.imread('images/30cm.jpg')
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
        self.horizontalLayout.setObjectName("horizontalLayout")


        self.thresholder = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.thresholder.sizePolicy().hasHeightForWidth())
        self.thresholder.setSizePolicy(sizePolicy)
        self.thresholder.setMaximumSize(QtCore.QSize(16777215, 50))
        self.thresholder.setObjectName("thresholder")
        self.horizontalLayout.addWidget(self.thresholder)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.thresholder)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # Create a button for threshold adjustment
        self.threshold_slider = QSlider(Qt.Horizontal, self.thresholder)
        self.threshold_slider.setRange(0, 255)
        self.threshold_slider.setValue(128)
        self.threshold_slider.setFixedSize(250,self.thresholder.height())
        self.threshold_slider.valueChanged.connect(self.adjust_threshold)
        # Connect the valueChanged signal of the slider to a function that updates the label
        self.threshold_slider.valueChanged.connect(self.update_slider_value_label)
        self.horizontalLayout_5.addWidget(self.threshold_slider)

        self.thresholderNum = QtWidgets.QLabel("128", self.thresholder)
        self.thresholderNum.setObjectName("thresholderNum")
        self.thresholderNum.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignLeft)
        self.thresholderNum.setFixedSize(20, self.thresholder.height())
        self.horizontalLayout_5.addWidget(self.thresholderNum)

        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.inputDistance = QtWidgets.QTextEdit(self.widget_3)
        self.inputDistance.setMaximumSize(QtCore.QSize(100, 16777215))
        self.inputDistance.setObjectName("inputDistance")
        self.inputDistance.setFixedSize(50,30)
        self.horizontalLayout_2.addWidget(self.inputDistance)

        self.distance = QtWidgets.QComboBox(self.widget_3)
        self.distance.setMaximumSize(QtCore.QSize(100, 16777215))
        self.distance.setObjectName("distance")
        self.distance.addItems(["20cm", "30cm", "40cm", "50cm", "1 meter"])
        self.horizontalLayout_2.addWidget(self.distance)

        self.removeNoise = QtWidgets.QPushButton("Remove Noise", self.widget_3)
        self.removeNoise.setMaximumSize(QtCore.QSize(100, 16777215))
        self.removeNoise.setObjectName("removeNoise")
        self.removeNoise.clicked.connect(self.remove_noise)
        self.horizontalLayout_2.addWidget(self.removeNoise)

        self.cropImg = QtWidgets.QPushButton("Crop", self.widget_3)
        self.cropImg.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cropImg.setObjectName("cropImg")
        self.horizontalLayout_2.addWidget(self.cropImg)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(500, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.get_Heigth_Width = QtWidgets.QPushButton("Proceed", self.widget_2)
        self.get_Heigth_Width.setMaximumSize(QtCore.QSize(100, 16777215))
        self.get_Heigth_Width.setObjectName("get_Heigth_Width")
        self.get_Heigth_Width.clicked.connect(MainWindow.close)
        self.get_Heigth_Width.clicked.connect(self.Proceed_to_Result)
        self.horizontalLayout_3.addWidget(self.get_Heigth_Width)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Proceed_to_Result(self):
        try:
            # Get the path to the directory where the executable is run from
            app_path = getattr(sys, '_MEIPASS', None) or os.path.abspath('..')
            # Create the path to the view_folders.py file
            view_result = os.path.join(app_path, 'fromOldVersion/result.py')
            # Execute the view_folders.py file using QProcess
            process = QtCore.QProcess()
            process.start('python', [view_result])
            if process.waitForFinished() == 0:
                print('Error: failed to execute view_result.py')
        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

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

    # Function to update the slider value label
    def update_slider_value_label(self, value):
        self.thresholderNum.setText(str(value))

    # Function to adjust the threshold
    def adjust_threshold(self, value):
        # Apply thresholding
        _, self.thresholded = cv2.threshold(self.gray, value, 255, cv2.THRESH_BINARY)
        # Update the image on the label
        self.update_image(self.thresholded)

    # Function to remove noise
    def remove_noise(self):
        nBlock = 10  # Threshold for black block size

        # Find connected black blocks
        blocks = find_black_blocks(self.thresholded, nBlock)

        # Create a mask containing all black blocks
        mask = np.zeros_like(self.thresholded, dtype=bool)
        for block in blocks:
            for y, x in block:
                mask[y, x] = True

        # Apply the mask to the thresholded image
        result = np.where(mask, self.thresholded, 255)

        # Update the image on the label
        self.update_image(result)
        self.get_Heigth_Width_Function(result)

    def get_Heigth_Width_Function(self, result):
        # Set the known distance and focal length of the camera
        known_distance = 30  # in cm
        focal_length = 132.28  # in pixels (estimate based on camera specs of samsung a6)

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
                width_mm = width * known_distance / focal_length
                crack_widths.append(width_mm)

        # Measure the height of the crack in non-broken areas
        crack_heights = []
        for x in range(result.shape[1]):
            top_edge, bottom_edge = None, None
            for y in range(result.shape[0]):
                if result[y, x] == 0:
                    if top_edge is None:
                        top_edge = y
                    bottom_edge = y
            if top_edge is not None and bottom_edge is not None:
                # Check if the pixels between top_edge and bottom_edge are part of the crack
                if any(result[top_edge:bottom_edge + 1, x] == 0):
                    height = bottom_edge - top_edge
                    # Convert pixel height to cm
                    height_cm = height * known_distance / focal_length
                    crack_heights.append(height_cm / 10)
                    print(f"Crack area height: {height:.2f} mm")

        if len(crack_heights) == 0:
            print("No crack areas found")
        else:
            avg_height = sum(crack_heights) / len(crack_heights)
            print(f"Crack height: {avg_height:.2f} cm")

        avg_width = sum(crack_widths) / len(crack_widths)
        print(f"Crack width: {avg_width:.2f} mm")

# Function to find connected black blocks
def find_black_blocks(image, nBlock):
    height, width = image.shape

    # Create hashmap to store visited vertices
    track = {}

    # Loop through each pixel in the image
    for y in range(height):
        for x in range(width):

            # Check if the current pixel is black and not already visited
            if is_black(image[y, x]) and (y, x) not in track:

                # Create a stack to store adjacent vertices
                stack = deque()
                stack.append((y, x))

                # Create a list to store the
                # Create a list to store the current block of black pixels
                block = []

                # Traverse adjacent vertices
                while stack:
                    cy, cx = stack.pop()
                    if (cy, cx) in track:
                        continue
                    track[(cy, cx)] = True
                    block.append((cy, cx))

                    # Visit adjacent vertices in sequence A -> A right -> A left -> A up -> A down
                    for dy, dx in [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]:
                        ny, nx = cy + dy, cx + dx
                        if ny < 0 or ny >= height or nx < 0 or nx >= width:
                            continue
                        if is_black(image[ny, nx]):
                            stack.append((ny, nx))

                # Check if the block size is greater than the threshold
                if len(block) >= nBlock:
                    yield block

# Function to check if a pixel is black
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
