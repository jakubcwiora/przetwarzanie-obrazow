import cv2

FILENAME = 'mogger.jpg'

image = cv2.imread(FILENAME)

cv2.imshow("Janek Szafir", image)

cv2.waitKey(0)
cv2.destroyAllWindows()