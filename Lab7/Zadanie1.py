"""
Prosty skrypt do podmiany tła (green screen) - bez trackbarów.
Ustaw zakres maski HSV ręcznie w zmiennych HSV_LOWER i HSV_UPPER poniżej.
"""

import cv2
import numpy as np
import os
import argparse

# ---------------------------
# Tutaj ręcznie ustaw zakres koloru do maski (HSV)
# Edytuj wartości aby dopasować do twojego zdjęcia (H: 0-179, S:0-255, V:0-255)
HSV_LOWER = np.array([35, 50, 50], dtype=np.uint8)  # przykład: zielony - dół
HSV_UPPER = np.array([85, 255, 255], dtype=np.uint8)  # przykład: zielony - góra
# ---------------------------

DEFAULT_INPUT = "./LAB7/input.jpg"
DEFAULT_BG = "./LAB7/background.jpg"
DEFAULT_OUT = "./LAB7/result.png"


def load_or_create_bg(bg_path, target_shape):
  h, w = target_shape[:2]
  if bg_path and os.path.isfile(bg_path):
    bg = cv2.imread(bg_path)
    if bg is None:
      print("Nie można wczytać pliku tła:", bg_path)
      bg = np.full((h, w, 3), (200, 200, 200), dtype=np.uint8)
    else:
      bg = cv2.resize(bg, (w, h), interpolation=cv2.INTER_AREA)
  else:
    bg = np.full((h, w, 3), (200, 200, 200), dtype=np.uint8)
  return bg


def create_mask_from_hsv(img_bgr, lower_hsv, upper_hsv):
  hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

  # operacje morfologiczne poprawiające maskę
  kernel = np.ones((3, 3), np.uint8)
  mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
  mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

  # wygładzenie krawędzi maski
  mask = cv2.GaussianBlur(mask, (7, 7), 0)

  return mask


def replace_background(foreground_bgr, background_bgr, mask):
  # mask: białe -> regiony tła (kolor do zastąpienia)
  mask_bg = mask
  mask_fg = cv2.bitwise_not(mask_bg)

  fg = cv2.bitwise_and(foreground_bgr, foreground_bgr, mask=mask_fg)
  bg_part = cv2.bitwise_and(background_bgr, background_bgr, mask=mask_bg)
  result = cv2.add(fg, bg_part)
  return result


def main():
  parser = argparse.ArgumentParser(
    description="Podmiana tła (bez trackbarów) - ustaw HSV w kodzie"
  )
  parser.add_argument(
    "--input",
    "-i",
    default=DEFAULT_INPUT,
    help="Ścieżka do selfie (przed zielonym ekranem)",
  )
  parser.add_argument("--bg", "-b", default=DEFAULT_BG, help="Ścieżka do obrazu tła")
  parser.add_argument(
    "--out", "-o", default=DEFAULT_OUT, help="Ścieżka do zapisu wyniku"
  )
  parser.add_argument(
    "--save-on-exit", action="store_true", help="Zapisz wynik po zamknięciu okien"
  )
  args = parser.parse_args()

  img = cv2.imread(args.input)
  if img is None:
    print("Nie można otworzyć pliku wejściowego:", args.input)
    return

  bg = load_or_create_bg(args.bg, img.shape)

  # stwórz maskę używając ręcznie ustawionych HSV
  mask = create_mask_from_hsv(img, HSV_LOWER, HSV_UPPER)
  result = replace_background(img, bg, mask)

  # pokaż obrazy
  cv2.imshow("input", img)
  cv2.imshow("mask", mask)
  cv2.imshow("background", bg)
  cv2.imshow("result", result)

  print("Ustawione HSV_LOWER =", HSV_LOWER.tolist(), "HSV_UPPER =", HSV_UPPER.tolist())
  print("Naciśnij 's' aby zapisać wynik teraz, 'q' lub Esc aby wyjść.")

  while True:
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q") or key == 27:
      if args.save_on_exit:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        cv2.imwrite(args.out, result)
        print("Zapisano wynik do:", args.out)
      break
    elif key == ord("s"):
      os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
      cv2.imwrite(args.out, result)
      print("Zapisano wynik do:", args.out)
      # po zapisie kontynuuj wyświetlanie (użytkownik może zapisać ponownie lub wyjść)

  cv2.destroyAllWindows()


if __name__ == "__main__":
  main()
