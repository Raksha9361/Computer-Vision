
import cv2

def count_faces(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(20, 20)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

    count = len(faces)

    cv2.putText(image, "Faces: " + str(count),
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    print("Number of faces detected:", count)

    cv2.imshow("Face Detection Output", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments\faceimg.png"

count_faces(image_path)
