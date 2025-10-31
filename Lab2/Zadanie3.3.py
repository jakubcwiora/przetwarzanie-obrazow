import cv2
import numpy as np

image = cv2.imread('Lab2/faceIq.jpg')

def rotateImage():
  try:
    angle = int(input("Podaj kąt obrócenia: ")) # Kąt w stopniach
    center = (image.shape[1] // 2, image.shape[0] // 2) # Środek obrazka
    scale = 1.0 # skala pozostanie niezmieniona

    M = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    rotated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    cv2.imshow("Obrócony obraz", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  except: 
    print("Podano nieprawidłową wartość")
    rotateImage()

rotateImage()

# Bufor 512 słow
# obsłga przetwornika cyfrowo analogowego DMA

# obsługa przerwan od polowy i konca bufora
# czestotliwosc problkowania 8kHz
# z każdych 256 probek policzyc DFT
# oraz umożliwić odczyt amplitud dla poszczegolnych prążkow