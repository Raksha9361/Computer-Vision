import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select your image",
    filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp")]
)

if path:
    image = cv2.imread(path)

    if image is not None:
        kernel = np.ones((5, 5), np.uint8)
        eroded = cv2.erode(image, kernel, iterations=1)

        cv2.imshow("Original Image", image)
        cv2.imshow("Eroded Image", eroded)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Unable to read this image.")
else:
    print("No image selected.")
