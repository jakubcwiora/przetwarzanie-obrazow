import cv2
import numpy as np

# Load the image
image = cv2.imread("Lab6/image.jpg", cv2.IMREAD_GRAYSCALE)

edges_many = cv2.Canny(image, 50, 150)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges_blurred = cv2.Canny(blurred, 50, 150)

edges_fewer = cv2.Canny(image, 100, 200)

kernel = np.ones((3, 3), np.uint8)
eroded = cv2.erode(edges_many, kernel, iterations=1)

# Display results
cv2.imshow("Original Edges (Many)", edges_many)
cv2.imshow("Blurred Before Canny", edges_blurred)
cv2.imshow("Higher Thresholds", edges_fewer)
cv2.imshow("Eroded Edges", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
