import cv2

FILENAME = 'Lab1/mogger.jpg'
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600


image = cv2.imread(FILENAME)

if image is None:
    print("Nie znaleziono obrazu")
else:
    resized = cv2.resize(image, (WINDOW_WIDTH, WINDOW_HEIGHT), interpolation=cv2.INTER_AREA)
    text = "Janek Szafir"
    position = (100, 100)                  
    font = cv2.FONT_HERSHEY_COMPLEX        
    font_scale = 2.0                       
    color = (200, 0, 0)                   
    thickness = 1 

    # Doadawanie tekstu
    output1 = resized.copy()
    cv2.putText(output1, text, position, font, font_scale, color, thickness)
    cv2.imshow("Janek Szafir - z podpisem", output1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Właściwości tekstu - zmienione
    text = "MOGGED"
    position = (100, 200)                  
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL       
    font_scale = 5.0                       
    color = (0, 0, 100)                   
    thickness = 5 

    output2 = resized.copy()
    cv2.putText(output2, text, position, font, font_scale, color, thickness)
    cv2.imshow("Janek Szafir - z podpisem (zmienionym)", output2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

