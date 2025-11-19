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
  ksizes = [3, 7, 15]
  for k in ksizes:
    out = cv2.medianBlur(img, k)
    fname = f"{base}_median_{k}.jpg"
    cv2.imwrite(fname, out)
    print("Saved", fname)


if __name__ == "__main__":
  main()
