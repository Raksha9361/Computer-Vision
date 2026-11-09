
import cv2
import numpy as np
import os
import glob


folder = os.path.dirname(os.path.abspath(__file__))

files = glob.glob(os.path.join(folder, "sample.*"))

if not files:
    print("Error: sample image not found in Experiments folder")
    exit()


image = cv2.imread(files[0])

if image is None:
    print("Unable to read image")
    exit()

print("Image loaded successfully:", files[0])


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


kernel = np.ones((5, 5), np.uint8)


opened_image = cv2.morphologyEx(
    gray_image,
    cv2.MORPH_OPEN,
    kernel
)


cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Opened Image", opened_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
