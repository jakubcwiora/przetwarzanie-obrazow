import cv2
import numpy as np

image = cv2.imread('Lab2/faceIq.jpg')

mirrored_vertical = cv2.flip(image, 0)
mirrored_horizontal = cv2.flip(image, 1)
mirrored_origin = cv2.flip(image, -1)

cv2.imshow("Odbicie pionowe", mirrored_vertical)
cv2.imshow("Odbicie poziome", mirrored_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()