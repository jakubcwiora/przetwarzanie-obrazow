import cv2

FILENAME = 'Lab1/mogger.jpg'

image = cv2.imread(FILENAME)

cv2.imwrite('kopia.jpg', image)