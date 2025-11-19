import cv2
import os

IMAGE_PATH = "./LAB5/input.jpg"


# Gaussian blur with three kernel sizes
def main():
  img = cv2.imread(IMAGE_PATH)
  if img is None:
    print("Cannot open", IMAGE_PATH)
    return
  base = os.path.splitext(os.path.basename(IMAGE_PATH))[0]
  kernels = [(3, 3), (7, 7), (15, 15)]
  for k in kernels:
    out = cv2.GaussianBlur(img, k, 0)
    fname = f"{base}_gauss_{k[0]}x{k[1]}.jpg"
    cv2.imwrite(fname, out)
    print("Saved", fname)


if __name__ == "__main__":
  main()
