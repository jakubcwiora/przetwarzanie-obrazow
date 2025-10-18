import numpy as np

img = np.zeros((3, 3), dtype=np.uint8)

img[0] = [1, 2, 3]
img[1] = [5, 6, 6]
img[2] = [7, 8, 0]

print(img)
