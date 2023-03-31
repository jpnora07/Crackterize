import math
import sys
import numpy as np
import cv2
from PyQt5.QtCore import Qt, QRectF, QPoint
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QCursor
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGraphicsView, QGraphicsScene, QSlider, QGridLayout, \
    QApplication

class DrawingWidget(QLabel):
    def __init__(self, image, parent=None):
        super().__init__(parent)
        self.image = image
        self.drawing = False
        self.drawn = False  # Add this variable to keep track of whether the line has been drawn
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.drawn:  # Check if the line has been drawn before allowing a new drawing
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
            self.drawn = True  # Mark the line as drawn when the mouse is released
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.image is not None:
            q_image = QImage(self.image.data, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
            painter.drawPixmap(self.rect(), QPixmap.fromImage(q_image))
        if self.drawn:
            # draw start point
            painter.setPen(QPen(Qt.blue, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPoint(self.start_point)
            # draw end point
            painter.setPen(QPen(Qt.blue, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPoint(self.end_point)
            # draw line
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawLine(self.start_point, self.end_point)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a widget to hold the image and sliders
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a grid layout to hold the widgets
        layout = QGridLayout(central_widget)

        # Load the input image and display i
        self.img = cv2.imread('segment_img.jpg')
        desired_size = (2500, 2500)
        self.img = cv2.resize(self.img, desired_size)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(self.gray, 50, 150, apertureSize=3)
        edges = cv2.dilate(edges, None, iterations=1)
        edges = cv2.erode(edges, None, iterations=1)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        boxes = []
        self.box_lengths = []  # Keep track of the total length within each bounding box
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
                    self.box_lengths.append(length_cm)  # Add the length of this crack to the total length in the current box
                self.widths.append(h)

        total_length = sum(self.box_lengths)
        total_length_write = f"{total_length:.2f}"
        print(total_length_write + " cm")
        with open('Predicted_height.txt', 'w') as f:
            f.write(str(total_length_write))
        # Create the DrawingWidget and pass the image to it
        self.edges_label = DrawingWidget(self.img)
        self.show_image(self.img)
        layout.addWidget(self.edges_label, 0, 1)
        print(f"Image dimensions: {self.img.shape}")

    def show_image(self, image):
        # Create a DrawingWidget object and set its size
        self.edges_label.setFixedSize(900, 800)

        # Get the size of the label
        label_size = self.edges_label.size()

        # Convert the image to a QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Set the image on the label
        pixmap = QPixmap(q_image)
        self.edges_label.setPixmap(pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.setGeometry(100, 100, 800, 600)
    sys.exit(app.exec_())
