
import cv2
import numpy as np
from tkinter import Tk, filedialog

# Select input image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Sample Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read image
image = cv2.imread(image_path)

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Top-Hat operation
top_hat_image = cv2.morphologyEx(
    gray_image,
    cv2.MORPH_TOPHAT,
    kernel
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Top Hat Image", top_hat_image)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
