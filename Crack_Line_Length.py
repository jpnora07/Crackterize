import math
import sys
import numpy as np
import cv2
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QRectF, QPoint
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QCursor
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGraphicsView, QGraphicsScene, QSlider, QGridLayout, \
    QApplication, QDialog, QPushButton, QHBoxLayout


class DrawingWidget(QLabel):
    def __init__(self, image, parent=None):
        super().__init__(parent)
        self.image = image
        self.lines = []  # Add a list to keep track of the lines
        self.drawing = False
        self.drawn = False
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.setMouseTracking(True)
        self.setCursor(QCursor(Qt.CrossCursor))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.drawn:
            self.drawing = True
            self.start_point = event.pos()
            self.end_point = event.pos()
            self.setCursor(QCursor(Qt.CrossCursor))
            self.update()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            self.end_point = event.pos()
            self.setCursor(QCursor(Qt.CrossCursor))
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            self.drawn = True

            y_diff = self.start_point.y() - self.end_point.y()
            x_diff = self.start_point.x() - self.end_point.x()

            angle_rad = math.atan2(y_diff, x_diff)

            angle_deg = math.degrees(angle_rad)

            if angle_deg < -45 and angle_deg >= -135:
                orientation = "vertical"
            elif angle_deg >= -45 and angle_deg <= 45:
                orientation = "horizontal"
            elif angle_deg > 45 and angle_deg <= 135:
                orientation = "vertical"
            else:
                orientation = "horizontal"
            orientation_write = f"{orientation}"
            angle_write = f"{angle_deg:.2f}"
            print(f"The line is " + orientation_write + " and has an angle of " + angle_write + " degrees.")
            with open('Orientation.txt', 'w') as f:
                f.write(orientation_write)
            with open('angle_write.txt', 'w') as f:
                f.write(angle_write)
            self.lines.append((self.start_point, self.end_point))  # Add the start and end points to the list of lines
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.image is not None:
            q_image = QImage(self.image.data, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
            painter.drawPixmap(self.rect(), QPixmap.fromImage(q_image))
        if self.drawn:
            painter.setPen(QPen(Qt.blue, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPoint(self.start_point)
            painter.drawPoint(self.end_point)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawLine(self.start_point, self.end_point)

    def remove_last_line(self):
        if len(self.lines) > 0:
            self.lines.pop()  # Remove the last line from the list
            self.drawn = False  # Reset the flag to allow drawing a new line
            self.update()  # Redraw the image


class Line_length(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        Dialog.setMaximumSize(QtCore.QSize(700, 600))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)


        # Create a grid layout to hold the widgets
        layout = QGridLayout(Dialog)

        #self.slider = QSlider(Qt.Horizontal)
        #self.slider.setRange(-100, 100)
        #self.slider.setValue(0)
        #self.slider.valueChanged.connect(self.update_bbox)
        layout.addWidget(self.slider, 1, 1)

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
                print(f"Length of crack: {length_cm} cm")
                if self.box_lengths:
                    self.box_lengths[-1] += length_cm
                else:
                    self.box_lengths.append(
                        length_cm)
                self.widths.append(h)

        total_length = sum(self.box_lengths)
        total_length_write = f"{total_length:.2f}"
        self.edges_label = DrawingWidget(self.img)
        self.show_image(self.img)
        layout.addWidget(self.edges_label, 0, 1)
        print(total_length_write + " cm")
        with open('Predicted_height.txt', 'w') as f:
            f.write(str(total_length_write))

        # Create a button and add it to the layout
        button = QPushButton("Done")
        button.setFixedSize(150, 35)
        button.setStyleSheet("#button{\n"
                           "margin-right: 12px;"
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
                           "#button:hover{\n"
                           "color: rgb(144,115,87);\n"
                           "border : 3px solid rgb(144,115,87);\n"
                           "background-color: white;\n"
                           "}\n"
                           "")
        button.setObjectName("button")
        button.clicked.connect(self.done_view_length)

        remove_last_line_button = QPushButton('Undo Line')
        remove_last_line_button.clicked.connect(self.remove_last_line)
        remove_last_line_button.setFixedSize(150, 35)
        remove_last_line_button.setStyleSheet("#remove_last_line_button{\n"
                             "margin-right: 12px;"
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
                             "#remove_last_line_button:hover{\n"
                             "color: rgb(144,115,87);\n"
                             "border : 3px solid rgb(144,115,87);\n"
                             "background-color: white;\n"
                             "}\n"
                             "")
        remove_last_line_button.setObjectName("remove_last_line_button")
        layout.addWidget(remove_last_line_button, 1, 1, Qt.AlignHCenter)
        layout.addWidget(button, 2, 1, Qt.AlignHCenter)
        Dialog.setLayout(layout)
        print(f"Image dimensions: {self.img.shape}")

    def update_bbox(self, value):
        # Calculate the new position and size of the bounding box based on the slider value
        x = 100 + value
        y = 100 + value
        w = 200 - value
        h = 200 - value

        # Draw the new bounding box on the image
        img_copy = self.img.copy()
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Update the label with the new image
        self.show_image(img_copy)
    def done_view_length(self):
        self.Dialog.close()
    def remove_last_line(self):
        if self.edges_label.drawn:
            self.edges_label.drawn = False
            self.edges_label.update()
    def show_image(self, image):
        # Create a DrawingWidget object and set its size
        self.edges_label.setFixedSize(500, 400)

        # Get the size of the label
        label_size = self.edges_label.size()

        # Convert the image to a QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.edges_label.setPixmap(pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Line_length()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())