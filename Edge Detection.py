import sys
import numpy as np
import cv2
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGraphicsView, QGraphicsScene, QSlider, QGridLayout, \
    QApplication, QPushButton


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
        # Initialize the edge detector with the default threshold values
        self.threshold1 = 52
        self.threshold2 = 1000

        self.threshold1_label = QLabel("0")
        self.threshold2_label = QLabel("0")

        # Create a grid layout to hold the widgets
        layout = QGridLayout(central_widget)
        layout.addWidget(self.original_view, 0, 0)
        layout.addWidget(self.edges_view, 0, 1)
        layout.addWidget(QLabel('Threshold 1'), 1, 0)
        layout.addWidget(self.threshold1_slider, 1, 1)
        layout.addWidget(QLabel('Threshold 2'), 2, 0)
        layout.addWidget(self.threshold2_slider, 2, 1)
        layout.addWidget(QLabel('Current Threshold 1:'), 3, 0)
        layout.addWidget(self.threshold1_label, 3, 1)
        layout.addWidget(QLabel('Current Threshold 2:'), 4, 0)
        layout.addWidget(self.threshold2_label, 4, 1)

        # Load the input image and display it
        self.img = cv2.imread('images/crack_sample.jpg')
        self.show_image(self.img, self.original_view)


        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.blurred = cv2.GaussianBlur(self.img, (5, 5), 0)
        edges = cv2.Canny(self.blurred, self.threshold1, self.threshold2)
        edges = cv2.dilate(edges, None, iterations=1)
        edges = cv2.erode(edges, None, iterations=1)

        self.show_edges(edges, self.edges_view)

        # Find contours and draw non-overlapping bounding boxes around them
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = [x for x in contours if cv2.contourArea(x) > 50]
        boxes = []
        self.lengths = []
        self.widths = []
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


        # Create a button to calculate and print total length and width of the detected cracks
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_totals)

        # Add the button to the layout
        layout.addWidget(self.calculate_button)

        # Display the result
        self.show_image(self.img, self.edges_view)

        # Connect the sliders to update the edge detection in real-time
        self.threshold1_slider.valueChanged.connect(self.update_edges)
        self.threshold2_slider.valueChanged.connect(self.update_edges)

    def calculate_totals(self):
        # Calculate total length and width of the detected cracks in cm
        total_length = sum(self.lengths)
        total_width = sum(self.widths)
        # Print total length and width of the detected cracks in cm
        print("Total Length: {} cm".format(round(total_length, 2)))
        print("Total Width: {} cm".format(round(total_width, 2)))

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
        # Define the actual dimensions of the image in cm
        img_width_cm = 48
        img_height_cm = 49

        # Define the pixel-to-size ratio for the image
        pixel_to_cm = img_width_cm / self.img.shape[1]

        # Get the new threshold values from the sliders
        threshold1 = 157
        threshold2 = 21
        self.threshold1_label.setText(str(threshold1))
        self.threshold2_label.setText(str(threshold2))

        # Detect edges using Canny algorithm
        edges = cv2.Canny(self.blurred, threshold1, threshold2)

        # Find contours and draw bounding boxes around them
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        img_with_boxes = self.img.copy()
        for contour in contours:
            # Compute the bounding box and aspect ratio
            x, y, w, h = cv2.boundingRect(contour)

            # Check if the contour is roughly horizontal and has a minimum area
            min_area = 10  # adjust this to suit your needs
            max_aspect_ratio = 1.0  # adjust this to suit your needs
            aspect_ratio = 0
            if h != 0 and w != 0 and aspect_ratio < max_aspect_ratio and cv2.contourArea(contour) > min_area:
                # Draw the bounding box
                cv2.rectangle(img_with_boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Measure length and width of the bounding box in cm
                length_cm = np.sqrt(w ** 2 + h ** 2) * pixel_to_cm
                width_cm = w * pixel_to_cm

                # Print the length and width in cm
                print("Number of pixels: {}".format(w * h))
                print("Length of crack: {:.2f} cm".format(length_cm))
                print("Width of crack: {:.2f} cm".format(width_cm))

                # Store the length and width in lists for later use
                self.lengths.append(length_cm)
                self.widths.append(width_cm)

        # Display the updated images
        self.show_edges(edges, self.edges_view)
        self.show_image(img_with_boxes, self.original_view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.setGeometry(100, 100, 800, 600)
    sys.exit(app.exec_())
