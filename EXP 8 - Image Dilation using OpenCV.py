
import os
import cv2
import numpy as np

# Search for the image in common folders
home = os.path.expanduser("~")

search_locations = [
    os.path.join(home, "OneDrive"),
    os.path.join(home, "Desktop"),
    os.path.join(home, "Documents"),
]

image_path = None

for location in search_locations:
    if not os.path.isdir(location):
        continue

    for root, dirs, files in os.walk(location):
        # Skip hidden/system folders to speed up searching
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file in files:
            if file.lower() in (
                "sample.jpg",
                "sample.jpeg",
                "sample.png",
                "sample.bmp",
            ):
                image_path = os.path.join(root, file)
                break

        if image_path:
            break

    if image_path:
        break

if image_path is None:
    print("Image not found in the searched folders.")
    print("Your Windows home folder is:", home)
else:
    print("Image found at:", image_path)

    image = cv2.imread(image_path)

    if image is not None:
        kernel = np.ones((5, 5), np.uint8)
        dilated_image = cv2.dilate(
            image, kernel, iterations=1
        )

        cv2.imshow("Original Image", image)
        cv2.imshow("Dilated Image", dilated_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("OpenCV could not read the image.")
