import cv2


image = cv2.imread('Lab2/faceIq.jpg')

# Definiowanie współrzędnych dla:
x1, y1 = 25, 25       # Lewego górnego wierzchołka
x2, y2 = 175, 175     # Prawego dolnego wierzchołka

# Przycinanie jedną metodą
cropped = image[y1:y2, x1:x2]

# Przycinanie obrazu metodą sub-pixelową
center = (100, 100)  
size = (150, 150)      
cropped_differently = cv2.getRectSubPix(image, size, center) 

# Wyświetlanie
cv2.imshow("Cropped Rectangle", cropped)
cv2.imshow("Cropped Differently Rectangle", cropped_differently)
cv2.waitKey(0)
cv2.destroyAllWindows()