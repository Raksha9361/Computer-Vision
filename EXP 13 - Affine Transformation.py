import cv2
import numpy as np
import os
from tkinter import Tk, filedialog


root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Image",
    initialdir=r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

root.destroy()

if not image_path:
    print("No image selected!")
    raise SystemExit


image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read image!")
    raise SystemExit

rows, cols = image.shape[:2]

pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])


pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

matrix = cv2.getAffineTransform(pts1, pts2)


transformed_image = cv2.warpAffine(
    image, matrix, (cols, rows)
)

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed_image)


output_path = os.path.join(
    os.path.dirname(image_path),
    "affine_transformed.jpg"
)

cv2.imwrite(output_path, transformed_image)
print("Image saved at:", output_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
