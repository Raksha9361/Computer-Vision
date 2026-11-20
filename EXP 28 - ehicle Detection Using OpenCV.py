
import cv2
import os
import urllib.request

folder = os.path.dirname(os.path.abspath(__file__))

video_path = os.path.join(folder, "traffic_video.mp4")
cascade_path = os.path.join(folder, "cars.xml")

if not os.path.exists(cascade_path):
    print("Downloading cars.xml...")
    url = "https://raw.githubusercontent.com/andrewssobral/vehicle_detection_haarcascades/master/cars.xml"
    urllib.request.urlretrieve(url, cascade_path)

car_cascade = cv2.CascadeClassifier(cascade_path)

if car_cascade.empty():
    print("Error: Invalid cars.xml file")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open traffic_video.mp4")
    exit()

print("Vehicle Detection Started")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    cars = car_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(50, 50)
    )

   
    for (x, y, w, h) in cars:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Vehicle",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Vehicle Detection Completed!")
