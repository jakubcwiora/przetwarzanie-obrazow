import cv2

img = cv2.imread('Lab3/cwr.jpg')
img_big_cheese = cv2.imread('Lab3/bigseruch.png')
if img is None:
    raise FileNotFoundError("Could not read 'Lab3/cwr.jpg' — check the path and file.")

img = cv2.resize(img, (800, 400), interpolation=cv2.INTER_AREA)
title: str = "Big chees!"
cv2.imshow(title.encode('utf-8').decode('latin1'), img)
cv2.waitKey(0)
cv2.destroyAllWindows()