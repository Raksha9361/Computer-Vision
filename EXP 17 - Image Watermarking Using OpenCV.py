import cv2
import numpy as np
import os
from tkinter import Tk, filedialog


root = Tk()
root.withdraw()


print("Select the ORIGINAL image")
original_path = filedialog.askopenfilename(
    title="Select Original Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

print("Select the WATERMARK image")
watermark_path = filedialog.askopenfilename(
    title="Select Watermark Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

# Check whether files were selected
if not original_path or not watermark_path:
    print("Error: Please select both images.")
    exit()

# Read the images
original = cv2.imread(original_path)
watermark = cv2.imread(watermark_path)

# Check whether images were loaded successfully
if original is None:
    print("Error: Unable to read the original image.")
    exit()

if watermark is None:
    print("Error: Unable to read the watermark image.")
    exit()

height, width = original.shape[:2]

watermark = cv2.resize(watermark, (width, height))


watermarked_image = cv2.addWeighted(
    original, 0.7,
    watermark, 0.3,
    0
)


cv2.imshow("Original Image", original)
cv2.imshow("Watermark Image", watermark)
cv2.imshow("Watermarked Image", watermarked_image)

output_folder = os.path.dirname(original_path)

output_path = os.path.join(
    output_folder,
    "watermarked_image.jpg"
)

cv2.imwrite(output_path, watermarked_image)

print("Watermark inserted successfully.")
print("Watermarked image saved at:")
print(output_path)


cv2.waitKey(0)


cv2.destroyAllWindows()
