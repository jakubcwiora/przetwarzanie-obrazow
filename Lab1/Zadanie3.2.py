import cv2

FILENAME = 'mogger.jpg'

image = cv2.imread(FILENAME, 0)

cv2.imwrite('kopia.jpg', image)