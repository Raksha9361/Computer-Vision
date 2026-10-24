import cv2
import numpy as np
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Input Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

# Check if an image was selected
if not image_path:
    print("Error: No image selected.")
    exit()

# Read the selected image
image = cv2.imread(image_path)

# Check whether the image was loaded
if image is None:
    print("Error: Unable to read the selected image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter in X direction
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter in Y direction
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert gradients to absolute scale
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y gradients
sobel_combined = cv2.addWeighted(
    sobel_x, 0.5,
    sobel_y, 0.5,
    0
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)

# Save output images in the same folder as the input image
import os

folder = os.path.dirname(image_path)

cv2.imwrite(os.path.join(folder, "sobel_x.jpg"), sobel_x)
cv2.imwrite(os.path.join(folder, "sobel_y.jpg"), sobel_y)
cv2.imwrite(os.path.join(folder, "sobel_combined.jpg"), sobel_combined)

print("Sobel edge detection completed successfully.")
print("Output files saved in:")
print(folder)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
