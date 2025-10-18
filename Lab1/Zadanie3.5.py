import cv2

FILENAMES = [
  ('Lab1/kopia.jpg', 'JPG'), 
  ('Lab1/sample1.bmp', 'BMP'), 
  ('Lab1/blackpill.png', 'PNG'), 
  ('Lab1/chico.gif', 'GIF')
  ]

for name in FILENAMES:
  image = cv2.imread(name[0])
  cv2.imshow(f"Obraz {name[1]}", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  