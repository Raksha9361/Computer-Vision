import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

# Select the source image
image_path = filedialog.askopenfilename(
    title="Select Source Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

# Check if image was selected
if not image_path:
    print("Error: No image selected.")
    exit()

# Read the source image
image = cv2.imread(image_path)

# Check whether image was loaded
if image is None:
    print("Error: Unable to read the image.")
    exit()

# Make a copy of the original image
result = image.copy()

# Get image dimensions
height, width = image.shape[:2]

# Define the Region of Interest (ROI)
# x1, y1 = starting point
# x2, y2 = ending point

x1 = width // 4
y1 = height // 4
x2 = width // 2
y2 = height // 2

# Crop the ROI
roi = image[y1:y2, x1:x2]

# Copy the ROI
copied_roi = roi.copy()

# Define destination location
paste_x = 10
paste_y = 10

# Get ROI dimensions
roi_height, roi_width = copied_roi.shape[:2]

# Paste the copied ROI at the destination
result[
    paste_y:paste_y + roi_height,
    paste_x:paste_x + roi_width
] = copied_roi

# Display the original image
cv2.imshow("Original Image", image)

# Display the cropped ROI
cv2.imshow("Cropped ROI", roi)

# Display the final image
cv2.imshow("ROI Copied and Pasted", result)

# Save the cropped ROI
folder = os.path.dirname(image_path)

cv2.imwrite(
    os.path.join(folder, "cropped_roi.jpg"),
    roi
)

# Save the final image
cv2.imwrite(
    os.path.join(folder, "roi_copied_pasted.jpg"),
    result
)

print("ROI cropping, copying and pasting completed successfully.")
print("Cropped ROI saved as: cropped_roi.jpg")
print("Final image saved as: roi_copied_pasted.jpg")

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
