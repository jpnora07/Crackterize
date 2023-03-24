import sys

import cv2
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QInputDialog, QSlider
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from collections import deque


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load image and convert to grayscale
        self.image = cv2.imread("images/10cm.jpg")
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Create a label to display the image
        self.label = QLabel(self)
        self.label.setFixedSize(800, 600)

        # Create a button for threshold adjustment
        self.threshold_slider = QSlider(Qt.Horizontal, self)
        self.threshold_slider.setRange(0, 255)
        self.threshold_slider.setValue(128)
        self.threshold_slider.setGeometry(0, self.label.height(), 300, 20)
        self.threshold_slider.valueChanged.connect(self.adjust_threshold)
        # Create a label to show the current value of the slider
        self.slider_value_label = QLabel(str(self.threshold_slider.value()), self)
        self.slider_value_label.setGeometry(self.threshold_slider.x(),
                                            self.threshold_slider.y() + self.threshold_slider.height(), 50, 20)

        # Connect the valueChanged signal of the slider to a function that updates the label
        self.threshold_slider.valueChanged.connect(self.update_slider_value_label)

        # Create a button for noise removal
        self.noise_removal_button = QPushButton('Remove Noise', self)
        self.noise_removal_button.move(self.threshold_slider.width() + 20, self.label.height())
        self.noise_removal_button.clicked.connect(self.remove_noise)

        # Set the image on the label
        self.update_image(self.gray)
        # Set the size of the window
        self.setFixedSize(800, 700)

    # Function to update the slider value label
    def update_slider_value_label(self, value):
        self.slider_value_label.setText(str(value))
        self.slider_value_label.adjustSize()
        self.slider_value_label.move(self.threshold_slider.x() + self.threshold_slider.width(),
                                     self.slider_value_label.y())
    # Function to update the image on the label
    def update_image(self, image):
        # Get the size of the label
        label_size = self.label.size()

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
        self.label.setPixmap(pixmap)

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

        # Set the known distance and focal length of the camera
        known_distance = 10  # in cm
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
                    print(f"Crack area height: {height_cm:.2f} mm")

        if len(crack_heights) == 0:
            print("No crack areas found")
        else:
            avg_height = sum(crack_heights) / len(crack_heights)
            print(f"Crack height: {avg_height:.2f} cm")

        avg_width = sum(crack_widths) / len(crack_widths)
        print(f"Crack width: {avg_width:.2f} mm")

        # Update the image on the label
        self.update_image(result)


# Function to check if a pixel is black
def is_black(pixel):
    return pixel == 0


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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
