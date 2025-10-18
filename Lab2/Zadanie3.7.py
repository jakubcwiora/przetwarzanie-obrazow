import cv2

image = cv2.imread('Lab2/faceIq.jpg')
imageUpscaled = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Powiekszony x1.5", imageUpscaled)
cv2.waitKey(0)
cv2.destroyAllWindows()