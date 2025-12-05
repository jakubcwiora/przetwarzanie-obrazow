import sys
import cv2
import os
import numpy as np

IMAGE_PATH = "./Lab5/input.jpg"


def gaussian_noise(image, mean=0, sigma=15):
  gauss = np.random.normal(mean, sigma, image.shape).astype(np.float32)
  noisy = image.astype(np.float32) + gauss
  noisy = np.clip(noisy, 0, 255).astype(np.uint8)
  return noisy


def main():
  img_path = sys.argv[1] if len(sys.argv) > 1 else IMAGE_PATH
  img = cv2.imread(img_path)
  if img is None:
    print("Cannot open", img_path)
    return
  base = os.path.splitext(os.path.basename(img_path))[0]

  noisy = gaussian_noise(img, sigma=20)
  cv2.imwrite(f"{base}_gaussnoise.jpg", noisy)
  print("Saved", f"{base}_gaussnoise.jpg")

  gauss = cv2.GaussianBlur(noisy, (5, 5), 0)
  cv2.imwrite(f"{base}_gaussnoise_gauss.jpg", gauss)
  print("Saved", f"{base}_gaussnoise_gauss.jpg")

  median = cv2.medianBlur(noisy, 5)
  cv2.imwrite(f"{base}_gaussnoise_median.jpg", median)
  print("Saved", f"{base}_gaussnoise_median.jpg")

  bilateral = cv2.bilateralFilter(noisy, 9, 75, 75)
  cv2.imwrite(f"{base}_gaussnoise_bilateral.jpg", bilateral)
  print("Saved", f"{base}_gaussnoise_bilateral.jpg")


if __name__ == "__main__":
  main()
