
import cv2
import numpy as np

def subtract_background(image_path, lower_color, upper_color):

    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array(lower_color, dtype=np.uint8)
    upper = np.array(upper_color, dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)

    mask_inv = cv2.bitwise_not(mask)

    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    cv2.imshow("Original Image", image)
    cv2.imshow("Background Subtracted Image", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments\sample.png"

lower_color = [30, 30, 30]
upper_color = [255, 255, 255]

subtract_background(image_path, lower_color, upper_color)
