import cv2
import numpy as np

# Load the image
image = cv2.imread("Lab6/image.jpg", cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(image, (5, 5), 0)

edges_default = cv2.Canny(blurred, 100, 200)

edges_more = cv2.Canny(blurred, 50, 150)

edges_less = cv2.Canny(blurred, 150, 250)

# Display results
cv2.imshow("Original", image)
cv2.imshow("Canny Default", edges_default)
cv2.imshow("Canny More Edges", edges_more)
cv2.imshow("Canny Fewer Edges", edges_less)
cv2.waitKey(0)
cv2.destroyAllWindows()
