import cv2
from tkinter import Tk, filedialog
import os

# Select the input image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp"),
        ("All files", "*.*")
    ],
    initialdir=os.path.expanduser("~/OneDrive/Documents")
)

root.destroy()

if not image_path:
    print("No image selected.")
    raise SystemExit

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read the selected image.")
    raise SystemExit

# Flip horizontally along the Y-axis
flipped_image = cv2.flip(image, 1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Y-Axis Flipped Image", flipped_image)

# Save the result in the same folder
output_path = os.path.join(
    os.path.dirname(image_path),
    "rotated_image.jpg"
)
cv2.imwrite(output_path, flipped_image)

print("Image saved at:", output_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
