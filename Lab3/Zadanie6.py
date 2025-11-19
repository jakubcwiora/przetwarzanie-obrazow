import cv2

img = cv2.imread('Lab3/Lenna_(test_image).png', cv2.IMREAD_COLOR_BGR)

if img.shape[2] == 4: # Usuwanie kanału alfa
  bgr = img[:, :, :3]
else:
  bgr = img

hsv_converted = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV) # Zamiana na HSV
cv2.imshow("BGR", bgr)
cv2.imwrite("HSV.jpg", hsv_converted)
cv2.waitKey(0)
cv2.destroyAllWindows()


