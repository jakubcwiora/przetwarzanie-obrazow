import cv2

FILENAME = 'Lab1/mogger.jpg'
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

image = cv2.imread(FILENAME)

if image is None:
    print("Image not found!")
else:
    
    resized = cv2.resize(image, (WINDOW_WIDTH, WINDOW_HEIGHT), interpolation=cv2.INTER_AREA)

    output = resized.copy()
    # Change properties for shapes
    circle_center = (100, 300)
    circle_radius = 80
    circle_color = (0, 255, 255)  # Żółty
    circle_thickness = 5

    rectangle_top_left = (200, 100)
    rectangle_bottom_right = (400, 350)
    rectangle_color = (255, 0, 255)  # Magenta
    rectangle_thickness = 6

    line_start = (50, 400)
    line_end = (500, 150)
    line_color = (0, 255, 0)  # Zielony
    line_thickness = 7

    # Rysowanie kształtów
    cv2.circle(output, circle_center, circle_radius, circle_color, circle_thickness)
    cv2.rectangle(output, rectangle_top_left, rectangle_bottom_right, rectangle_color, rectangle_thickness)
    cv2.line(output, line_start, line_end, line_color, line_thickness)

    cv2.imshow("Pomazany customowymi figurami", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()