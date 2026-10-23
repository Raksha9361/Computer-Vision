import cv2
import os
from tkinter import Tk, filedialog

# Select the input image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Your Image",
    initialdir=r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp"),
        ("All files", "*.*")
    ]
)

root.destroy()

if not image_path:
    print("No image selected!")
    raise SystemExit

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read the selected image!")
    raise SystemExit

# Flip horizontally along the Y-axis
flipped_image = cv2.flip(image, 1)

# Rotate 270 degrees clockwise
rotated_image = cv2.rotate(
    flipped_image,
    cv2.ROTATE_90_COUNTERCLOCKWISE
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated 270 Degrees", rotated_image)

# Save the output in the same folder
output_path = os.path.join(
    os.path.dirname(image_path),
    "rotated_image_270.jpg"
)

cv2.imwrite(output_path, rotated_image)
print("Image saved successfully:", output_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
