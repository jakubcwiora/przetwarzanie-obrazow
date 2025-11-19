import cv2
import numpy as np

img = cv2.imread('Lab3/Lenna_(test_image).png', cv2.IMREAD_COLOR_BGR)

b, g, r = cv2.split(img)
zeros = np.zeros_like(b)

blue_channel = cv2.merge([b, zeros, zeros])
green_channel = cv2.merge([zeros, g, zeros])


cv2.imshow("A", blue_channel)
cv2.imshow("B", green_channel)
cv2.imshow("A + B", blue_channel + green_channel)
cv2.imshow("BASE - B", img - green_channel)
cv2.imshow("B - BASE", green_channel - img)
cv2.imshow("A * B", blue_channel * green_channel)
cv2.imshow("A / B", blue_channel / green_channel)
cv2.imshow("B / A", green_channel / blue_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
