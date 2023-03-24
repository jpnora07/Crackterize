import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the model from the H5 file
        self.model = keras.models.load_model('resnet_model_cnn.h5')

        # Create a file dialog to select an image file
        self.file_dialog = QtWidgets.QFileDialog(self)
        self.file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        self.file_dialog.setNameFilter("Image files (*.jpg *.jpeg *.png)")

        # Create a label to display the selected image
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setFixedSize(256, 256)

        # Create a button to open the file dialog
        self.open_button = QtWidgets.QPushButton("Select Image", self)
        self.open_button.clicked.connect(self.open_file_dialog)

        # Create a label to display the prediction result
        self.prediction_label = QtWidgets.QLabel(self)
        self.prediction_label.setAlignment(QtCore.Qt.AlignCenter)

        # Create a vertical layout for the widgets
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.prediction_label)

        # Create a central widget and set the layout
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def open_file_dialog(self):
        # Show the file dialog and get the selected file path
        file_path, _ = self.file_dialog.getOpenFileName()

        # If a file was selected, load the image and make a prediction
        if file_path:
            image = cv2.imread(file_path)
            image = cv2.resize(image, (224, 224))
            image = np.expand_dims(image, axis=0)
            predictions = self.model.predict(image)
            score = tf.nn.softmax(predictions[0])

            # Set the image label to display the selected image
            pixmap = QtGui.QPixmap(file_path).scaled(256, 256, QtCore.Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)

            # Set the prediction label to display the result
            if np.argmax(score) == 0:
                self.prediction_label.setText("The image does not contain a crack.")
            else:
                self.prediction_label.setText("The image contains a crack.")

            # Resize the window to fit the image
            self.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
