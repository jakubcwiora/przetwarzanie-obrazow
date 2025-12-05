import cv2

# Load the image
image = cv2.imread("Lab6/image.jpg", cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(image, cv2.CV_64F)

laplacian_abs = cv2.convertScaleAbs(laplacian)

blurred = cv2.GaussianBlur(image, (3, 3), 0)
laplacian_blurred = cv2.Laplacian(blurred, cv2.CV_64F)
laplacian_blurred_abs = cv2.convertScaleAbs(laplacian_blurred)

blurred_more = cv2.GaussianBlur(image, (5, 5), 0)
laplacian_blurred_more = cv2.Laplacian(blurred_more, cv2.CV_64F)
laplacian_blurred_more_abs = cv2.convertScaleAbs(laplacian_blurred_more)

# Display results
cv2.imshow("Original", image)
cv2.imshow("Laplacian Default", laplacian_abs)
cv2.imshow("Laplacian with Blur (3x3)", laplacian_blurred_abs)
cv2.imshow("Laplacian with Blur (5x5)", laplacian_blurred_more_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
