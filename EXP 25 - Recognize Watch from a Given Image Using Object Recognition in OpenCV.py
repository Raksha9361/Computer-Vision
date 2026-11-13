
import cv2
from tkinter import Tk, filedialog
from ultralytics import YOLO

# Select image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Watch Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if not image_path:
    print("No image selected!")
    exit()

# Read image
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Load YOLO model
model = YOLO("yolov8s-worldv2.pt")

# Set detection class
model.set_classes(["watch"])

# Detect watch
results = model.predict(image, conf=0.15)

detected = False

# Draw bounding box
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        cv2.rectangle(
            image, (x1, y1), (x2, y2),
            (0, 255, 0), 2
        )

        cv2.putText(
            image, "Watch",
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (0, 255, 0), 2
        )

        detected = True

# Display result
if detected:
    print("Watch detected successfully!")
else:
    print("Watch not detected!")

cv2.imshow("Watch Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
