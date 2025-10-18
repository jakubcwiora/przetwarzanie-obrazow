import cv2

FILENAME = 'Lab1/mogger.jpg'

image = cv2.imread(FILENAME, 0)

cv2.imshow("Janek Szafir - evil", image)

cv2.waitKey(0)
cv2.destroyAllWindows()