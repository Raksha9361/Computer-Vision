
import cv2
import os

folder = os.path.dirname(os.path.abspath(__file__))


img = None

for file in os.listdir(folder):
    if file.lower() in ["sample.jpg", "sample.jpeg", "sample.png"]:
        img = cv2.imread(os.path.join(folder, file))
        if img is not None:
            break

if img is None:
    print("Error: Image not found!")
    print("Files in Experiments folder:")
    print(os.listdir(folder))
else:
    
    rotated_img = cv2.rotate(
        img, cv2.ROTATE_90_CLOCKWISE
    )

   
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated_img)

    cv2.imwrite(
        os.path.join(folder, "rotated_image.jpg"),
        rotated_img
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()
