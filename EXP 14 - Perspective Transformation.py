import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

# Select input image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Image",
    initialdir=r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

root.destroy()

if not image_path:
    print("No image selected!")
    raise SystemExit

# Read image
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read image!")
    raise SystemExit

rows, cols = image.shape[:2]

# Define four source points
pts1 = np.float32([
    [50, 50],
    [400, 50],
    [50, 400],
    [400, 400]
])

# Define four destination points
pts2 = np.float32([
    [10, 100],
    [300, 50],
    [100, 300],
    [350, 350]
])

# Compute perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
transformed_image = cv2.warpPerspective(
    image, matrix, (cols, rows)
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", transformed_image)

# Save output in the same folder
output_path = os.path.join(
    os.path.dirname(image_path),
    "perspective_transformed.jpg"
)

cv2.imwrite(output_path, transformed_image)
print("Image saved at:", output_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
