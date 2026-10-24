import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

# Select input image
image_path = filedialog.askopenfilename(
    title="Select Input Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

# Check whether an image was selected
if not image_path:
    print("Error: No image selected.")
    exit()

# Read the input image
image = cv2.imread(image_path)

# Check whether the image was loaded successfully
if image is None:
    print("Error: Unable to read the image.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(gray, kernel, iterations=1)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Eroded Image", eroded_image)

# Save the eroded image
folder = os.path.dirname(image_path)

output_path = os.path.join(
    folder,
    "eroded_image.jpg"
)

cv2.imwrite(output_path, eroded_image)

print("Erosion operation completed successfully.")
print("Eroded image saved at:")
print(output_path)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
