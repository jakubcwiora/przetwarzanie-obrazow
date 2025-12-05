import cv2
import numpy as np

# Load the image
image = cv2.imread("Lab6/image.jpg", cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Combine x and y
sobel_combined = cv2.magnitude(sobelx, sobely)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

# Change parameter: Use smaller kernel size
sobelx_small = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely_small = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_small = cv2.magnitude(sobelx_small, sobely_small)
sobel_small = cv2.convertScaleAbs(sobel_small)

# Change parameter: Use larger kernel size
sobelx_large = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=7)
sobely_large = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=7)
sobel_large = cv2.magnitude(sobelx_large, sobely_large)
sobel_large = cv2.convertScaleAbs(sobel_large)

# Display results
cv2.imshow("Original", image)
cv2.imshow("Sobel Combined ksize=5", sobel_combined)
cv2.imshow("Sobel Combined ksize=3", sobel_small)
cv2.imshow("Sobel Combined ksize=7", sobel_large)
cv2.waitKey(0)
cv2.destroyAllWindows()
