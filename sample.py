import cv2

# Load image
image = cv2.imread("image.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding box for each contour found
for contour in contours:
    # Get bounding box coordinates
    x, y, w, h = cv2.boundingRect(contour)

    # Draw bounding box
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)

# Save image
cv2.imwrite("image_bbox.jpg", image)
