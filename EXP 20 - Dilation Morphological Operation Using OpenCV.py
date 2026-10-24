import cv2
import numpy as np
import os
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(
    title="Select Input Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)
if not image_path:
    print("Error: No image selected.")
    exit()
image = cv2.imread(image_path)
if image is None:
    print("Error: Unable to read the image.")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(gray, kernel, iterations=1)
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Dilated Image", dilated_image)
folder = os.path.dirname(image_path)

output_path = os.path.join(
    folder,
    "dilated_image.jpg"
)
cv2.imwrite(output_path, dilated_image)
print("Dilation operation completed successfully.")
print("Dilated image saved at:")
print(output_path)
cv2.waitKey(0)
cv2.destroyAllWindows()
