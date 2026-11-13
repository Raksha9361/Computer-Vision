
import cv2

def detect_eyes(image_path):

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml'
    )

   
    image = cv2.imread(image_path)

 
    if image is None:
        print("Error: Image not found. Check the image path.")
        return

   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Number of faces detected:", len(faces))

   
    for (x, y, w, h) in faces:

        face_roi = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            face_roi,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(15, 15)
        )

        print("Number of eyes detected:", len(eyes))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                image,
                (x + ex, y + ey),
                (x + ex + ew, y + ey + eh),
                (255, 0, 0),
                2
            )


    cv2.imshow("Eye Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



image_path = r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments\faceimg.png"


detect_eyes(image_path)
