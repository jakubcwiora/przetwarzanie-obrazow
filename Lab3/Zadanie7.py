import cv2

img = cv2.imread('Lab3/Lenna_(test_image).png', cv2.IMREAD_GRAYSCALE)

_, thresh_binary1 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
_, thresh_binary2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
_, thresh_binary3 = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold 180", thresh_binary1)
cv2.imshow("Threshold 120", thresh_binary2)
cv2.imshow("Threshold 60", thresh_binary3)
cv2.waitKey(0)
cv2.destroyAllWindows()
