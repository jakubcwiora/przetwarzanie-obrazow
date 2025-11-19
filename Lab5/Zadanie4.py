import sys
import cv2
import os
import numpy as np

IMAGE_PATH = "./LAB5/input.jpg"


def main():
  img_path = sys.argv[1] if len(sys.argv) > 1 else IMAGE_PATH
  img = cv2.imread(img_path)
  if img is None:
    print("Cannot open", img_path)
    return
  base = os.path.splitext(os.path.basename(img_path))[0]

  sizes = [3, 5, 9]
  for s in sizes:
    k = np.ones((s, s), dtype=np.float32) / (s * s)
    out = cv2.filter2D(img, -1, k)
    fname = f"{base}_custombox_{s}x{s}.jpg"
    cv2.imwrite(fname, out)
    print("Saved", fname)

  gkern = np.array(
    [
      [1, 4, 6, 4, 1],
      [4, 16, 24, 16, 4],
      [6, 24, 36, 24, 6],
      [4, 16, 24, 16, 4],
      [1, 4, 6, 4, 1],
    ],
    dtype=np.float32,
  )
  gkern /= gkern.sum()
  outg = cv2.filter2D(img, -1, gkern)
  fname = f"{base}_custom_gauss5.jpg"
  cv2.imwrite(fname, outg)
  print("Saved", fname)


if __name__ == "__main__":
  main()
