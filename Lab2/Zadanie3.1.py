import cv2
import numpy as np

image = cv2.imread('Lab2/faceIq.jpg')

tx, ty = 50, 20 # Wartości translacji
M = np.float32([[1, 0, tx], [0, 1, ty]])

translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Translated (Moved) Image", translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()