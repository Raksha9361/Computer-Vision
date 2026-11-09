
import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Sample Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.uint8)


closed_image = cv2.morphologyEx(
    gray_image,
    cv2.MORPH_CLOSE,
    kernel
)


cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Closed Image", closed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
