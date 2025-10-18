import cv2

# Read the image
image = cv2.imread('Lab2/faceIq.jpg')

# Define the rectangle coordinates
# (y1:y2, x1:x2) - Note: OpenCV uses (row, column) = (y, x)
x1, y1 = 50, 60   # Top-left corner (column, row)
x2, y2 = 200, 220 # Bottom-right corner (column, row)

# Crop the rectangle
cropped = image[y1:y2, x1:x2]

center = (100, 100)  # (x, y)
size = (50, 50)      # (width, height)
cropped_differently = cv2.getRectSubPix(image, size, center)

# Show the cropped image
cv2.imshow("Cropped Rectangle", cropped)
cv2.imshow("Cropped Differently Rectangle", cropped_differently)
cv2.waitKey(0)
cv2.destroyAllWindows()