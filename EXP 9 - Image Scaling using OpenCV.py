import cv2
import os

folder = os.path.dirname(os.path.abspath(__file__))


image_path = None

for name in os.listdir(folder):
    if name.lower() in ["sample.jpg", "sample.jpeg", "sample.png"]:
        image_path = os.path.join(folder, name)
        break

if image_path is None:
    print("Error: Place sample.jpg in the Experiments folder!")
else:
    image = cv2.imread(image_path)

    bigger_image = cv2.resize(
        image, None, fx=2, fy=2,
        interpolation=cv2.INTER_LINEAR
    )

    smaller_image = cv2.resize(
        image, None, fx=0.5, fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger_image)
    cv2.imshow("Smaller Image", smaller_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
