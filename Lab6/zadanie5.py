import cv2
import numpy as np

# Load the image (use an image with geometric shapes, e.g., shapes.jpg)
image = cv2.imread("Lab6/shapes.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform binarization
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Perform edge detection (using Canny)
edges = cv2.Canny(binary, 100, 200)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display results
cv2.imshow("Original", image)
cv2.imshow("Binary", binary)
cv2.imshow("Edges", edges)
cv2.imshow("Contours", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
