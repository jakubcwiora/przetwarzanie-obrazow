import cv2

bg = cv2.imread('Lab3/cwr.jpg')
fg = cv2.imread('Lab3/bigseruch.png')
if bg is None:
    raise FileNotFoundError("Could not read 'Lab3/cwr.jpg' — check the path and file.")



bg = cv2.resize(bg, (800, 400), interpolation=cv2.INTER_AREA) 
fg = cv2.resize(fg, (bg.shape[1], bg.shape[0]), interpolation=cv2.INTER_AREA) 



dst = cv2.addWeighted(bg, 0.4, fg, 0.1, 0)
title: str = "Big chees!"


cv2.imshow(title.encode('utf-8').decode('latin1'), dst)
cv2.waitKey(0)
cv2.destroyAllWindows()