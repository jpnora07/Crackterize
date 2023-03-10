import sys

import cv2
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGraphicsView, QGraphicsScene, QSlider, QGridLayout, \
    QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a widget to hold the image and sliders
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create labels for the original image and the detected edges
        self.original_label = QLabel()
        self.edges_label = QLabel()

        # Create graphics views to display the images
        self.original_view = QGraphicsView()
        self.original_view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.original_view.setScene(QGraphicsScene(self))
        self.edges_view = QGraphicsView()
        self.edges_view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.edges_view.setScene(QGraphicsScene(self))

        # Create sliders for the threshold values
        self.threshold1_slider = QSlider(Qt.Horizontal)
        self.threshold1_slider.setMinimum(0)
        self.threshold1_slider.setMaximum(255)
        self.threshold1_slider.setSingleStep(1)
        self.threshold2_slider = QSlider(Qt.Horizontal)
        self.threshold2_slider.setMinimum(0)
        self.threshold2_slider.setMaximum(255)
        self.threshold2_slider.setSingleStep(1)

        # Create a grid layout to hold the widgets
        layout = QGridLayout(central_widget)
        layout.addWidget(self.original_view, 0, 0)
        layout.addWidget(self.edges_view, 0, 1)
        layout.addWidget(QLabel('Threshold 1'), 1, 0)
        layout.addWidget(self.threshold1_slider, 1, 1)
        layout.addWidget(QLabel('Threshold 2'), 2, 0)
        layout.addWidget(self.threshold2_slider, 2, 1)

        # Load the input image and display it
        self.img = cv2.imread('images/crack_sample.jpg')
        self.show_image(self.img, self.original_view)

        # Initialize the edge detector with the default threshold values
        self.threshold1 = 50
        self.threshold2 = 150
        edges = cv2.Canny(self.img, self.threshold1, self.threshold2)
        self.show_edges(edges, self.edges_view)

        # Find contours and draw non-overlapping bounding boxes around them
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        boxes = []
        for contour in contours:
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

            # Measure length and width of the bounding box in cm
            pixel_to_cm = 0.1
            length_cm = w * pixel_to_cm
            width_cm = h * pixel_to_cm

            # Print length and width of the bounding box in cm
            print("Length: {} cm".format(round(length_cm, 2)))
            print("Width: {} cm".format(round(width_cm, 2)))

        # Display the result
        self.show_image(self.img, self.edges_view)

        # Connect the sliders to update the edge detection in real-time
        self.threshold1_slider.valueChanged.connect(self.update_edges)
        self.threshold2_slider.valueChanged.connect(self.update_edges)

    def show_image(self, img, view):
        # Convert the image to a QPixmap and display it in the view
        qimg = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qimg)

        # Set the pixmap size to match the view size while preserving aspect ratio
        pixmap = pixmap.scaled(view.width(), view.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        view.scene().addPixmap(pixmap)

    def show_edges(self, edges, view):
        qimg = QImage(edges.data, edges.shape[1], edges.shape[0], QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qimg)

        # Set the pixmap size to match the view size while preserving aspect ratio
        pixmap = pixmap.scaled(view.width(), view.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Clear the previous contents of the view and add the new pixmap
        view.scene().clear()
        view.scene().addPixmap(pixmap)

    def update_edges(self):
        # Get the new threshold values from the sliders
        self.threshold1 = self.threshold1_slider.value()
        self.threshold2 = self.threshold2_slider.value()

        # Detect edges using Canny algorithm
        edges = cv2.Canny(self.img, self.threshold1, self.threshold2)

        # Find contours and draw bounding boxes around them
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        img_with_boxes = self.img.copy()
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img_with_boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the updated images
        self.show_edges(edges, self.edges_view)
        self.show_image(img_with_boxes, self.original_view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.setGeometry(100, 100, 800, 600)
    sys.exit(app.exec_())
