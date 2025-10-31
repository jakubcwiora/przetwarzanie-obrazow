import cv2

img = cv2.imread('Lab3/cwr.jpg')
if img is None:
    raise FileNotFoundError("Could not read 'Lab3/cwr.jpg' — check the path and file.")

img = cv2.resize(img, (800, 600), interpolation=cv2.INTER_AREA)
img = cv2.convertScaleAbs(img, beta=8)
title: str = "It's gunna be a long year vro..."
cv2.imshow(title.encode('utf-8').decode('latin1'), img)
cv2.waitKey(0)
cv2.destroyAllWindows()