import sys
import cv2
import os
import numpy as np

IMAGE_PATH = "./Lab5/input.jpg"


def salt_and_pepper(image, amount=0.02, s_vs_p=0.5):
  out = image.copy()
  h, w = out.shape[:2]
  num = int(amount * h * w)
  coords = [np.random.randint(0, i - 1, num) for i in (h, w)]
  out[coords[0], coords[1]] = 255
  coords = [np.random.randint(0, i - 1, num) for i in (h, w)]
  out[coords[0], coords[1]] = 0
  return out


def main():
  img_path = sys.argv[1] if len(sys.argv) > 1 else IMAGE_PATH
  img = cv2.imread(img_path)
  if img is None:
    print("Cannot open", img_path)
    return
  base = os.path.splitext(os.path.basename(img_path))[0]

  noisy = salt_and_pepper(img, amount=0.05)
  cv2.imwrite(f"{base}_snp_noisy.jpg", noisy)
  print("Saved", f"{base}_snp_noisy.jpg")

  gauss = cv2.GaussianBlur(noisy, (5, 5), 0)
  cv2.imwrite(f"{base}_snp_gauss.jpg", gauss)
  print("Saved", f"{base}_snp_gauss.jpg")

  median = cv2.medianBlur(noisy, 5)
  cv2.imwrite(f"{base}_snp_median.jpg", median)
  print("Saved", f"{base}_snp_median.jpg")

  bilateral = cv2.bilateralFilter(noisy, 9, 75, 75)
  cv2.imwrite(f"{base}_snp_bilateral.jpg", bilateral)
  print("Saved", f"{base}_snp_bilateral.jpg")


if __name__ == "__main__":
  main()
