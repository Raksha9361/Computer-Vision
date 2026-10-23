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
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

root.destroy()

if not image_path:
    print("No image selected!")
    raise SystemExit

# Read the original image
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read image!")
    raise SystemExit

# Keep a copy of the original image
result = image.copy()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Apply Harris Corner Detection
harris_corners = cv2.cornerHarris(
    gray, blockSize=2, ksize=3, k=0.04
)

# Dilate corners for visibility
harris_corners = cv2.dilate(harris_corners, None)

# Mark detected corners in red
threshold = 0.01 * harris_corners.max()
result[harris_corners > threshold] = [0, 0, 255]

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Harris Corner Detection", result)

# Save the output in the same folder
output_path = os.path.join(
    os.path.dirname(image_path),
    "harris_corners.jpg"
)

cv2.imwrite(output_path, result)
print("Image saved at:", output_path)

# Close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
