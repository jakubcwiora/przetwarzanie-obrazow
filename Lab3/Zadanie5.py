import numpy as np
import cv2

img = cv2.imread('Lab3/image.png', cv2.IMREAD_COLOR_BGR)

b, g, r = cv2.split(img) # Podział na kanały

cv2.imshow("blue", b) # Wyświetlanie tylko 
                      # niebieskiego jako odcienie szarości
cv2.imshow("green", g)
cv2.imshow("red", r)
cv2.waitKey(0)
cv2.destroyAllWindows()