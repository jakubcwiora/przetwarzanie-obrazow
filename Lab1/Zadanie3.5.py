import cv2

FILENAMES = [
  ('kopia.jpg', 'JPG'), 
  ('sample1.bmp', 'BMP'), 
  ('blackpill.png', 'PNG'), 
  ('chico.gif', 'GIF')
  ]

for name in FILENAMES:
  image = cv2.imread(name[0])
  cv2.imshow(f"Obraz {name[1]}", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()