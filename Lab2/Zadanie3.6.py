import cv2

image = cv2.imread('Lab2/faceIq.jpg')


imageHalfx_1 = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
imageQuaterx_1 = cv2.resize(image, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
cv2.imwrite("Skala0.5xMetodaResize.jpg", imageHalfx_1)
cv2.imwrite("Skala0.25xMetodaResize.jpg", imageQuaterx_1)

imageHalfx_1 = cv2.pyrDown(image)
imageQuaterx_1 = cv2.pyrDown(imageHalfx_1)

cv2.imwrite("Skala0.5xMetodaPyrDown.jpg", imageHalfx_1)
cv2.imwrite("Skala0.25xMetodaPyrDown.jpg", imageQuaterx_1)