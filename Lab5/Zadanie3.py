import sys
import cv2
import os

IMAGE_PATH = "./LAB5/input.jpg"


def main():
  img_path = sys.argv[1] if len(sys.argv) > 1 else IMAGE_PATH
  img = cv2.imread(img_path)
  if img is None:
    print("Cannot open", img_path)
    return
  base = os.path.splitext(os.path.basename(img_path))[0]
  params = [
    (5, 75, 75),
    (15, 75, 75),
    (35, 150, 150),
  ]
  for d, sc, ss in params:
    out = cv2.bilateralFilter(img, d, sc, ss)
    fname = f"{base}_bilateral_d{d}_c{sc}_s{ss}.jpg"
    cv2.imwrite(fname, out)
    print("Saved", fname)


if __name__ == "__main__":
  main()
