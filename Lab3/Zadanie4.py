import cv2

img = cv2.imread('Lab3/Lenna_(test_image).png', cv2.IMREAD_GRAYSCALE)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)
print("Przed: min =", minVal, "max =", maxVal)

# Normalizacja — metoda OpenCV
norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)


minVal2, maxVal2, _, _ = cv2.minMaxLoc(norm)
print("Po normalizacji: min =", minVal2, "max =", maxVal2)

cv2.imshow("original", img)
cv2.imshow("normalized", norm)
cv2.waitKey(0)
cv2.destroyAllWindows()