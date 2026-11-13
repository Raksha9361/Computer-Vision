
import cv2

def detect_smile(image_path):

    # Load face and smile classifiers
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        'haarcascade_frontalface_default.xml'
    )

    smile_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        'haarcascade_smile.xml'
    )

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(25, 25)
    )

    smile_count = 0

    for (x, y, w, h) in faces:

        # Select lower part of the face
        face_roi = gray[y + h//2:y + h, x:x + w]

        # Detect smiles
        smiles = smile_cascade.detectMultiScale(
            face_roi,
            scaleFactor=1.3,
            minNeighbors=10,
            minSize=(15, 10)
        )

        # Draw rectangles around smiles
        for (sx, sy, sw, sh) in smiles:

            cv2.rectangle(
                image,
                (x + sx, y + h//2 + sy),
                (x + sx + sw, y + h//2 + sy + sh),
                (0, 255, 0),
                2
            )

            smile_count += 1

    print("Number of smiles detected:", smile_count)

    # Display output
    cv2.imshow("Smile Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Your image path
image_path = r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments\faceimg.png"

# Run smile detection
detect_smile(image_path)
