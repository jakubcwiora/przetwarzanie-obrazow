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

  k_sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
  s1 = cv2.filter2D(img, -1, k_sharp)
  cv2.imwrite(f"{base}_sharpen_kernel.jpg", s1)
  print("Saved", f"{base}_sharpen_kernel.jpg")

  blur = cv2.GaussianBlur(img, (9, 9), 10)
  amount = 1.5
  us = cv2.addWeighted(img, 1 + amount, blur, -amount, 0)
  cv2.imwrite(f"{base}_sharpen_unsharp.jpg", us)
  print("Saved", f"{base}_sharpen_unsharp.jpg")

  lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
  lap = cv2.convertScaleAbs(lap)
  lap_boost = cv2.addWeighted(img, 1.0, lap, 0.7, 0)
  cv2.imwrite(f"{base}_sharpen_laplacian.jpg", lap_boost)
  print("Saved", f"{base}_sharpen_laplacian.jpg")


if __name__ == "__main__":
  main()
