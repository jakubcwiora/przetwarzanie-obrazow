import cv2

image = cv2.imread('Lab2/faceIq.jpg')


image2x_1 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
image4x_1 = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
cv2.imwrite("Skala2xMetodaResize.jpg", image2x_1)
cv2.imwrite("Skala4xMetodaResize.jpg", image4x_1)

image2x_1 = cv2.pyrUp(image)
image4x_1 = cv2.pyrUp(image2x_1)

cv2.imwrite("Skala2xMetodaPyrUp.jpg", image2x_1)
cv2.imwrite("Skala4xMetodaPyrUp.jpg", image4x_1)