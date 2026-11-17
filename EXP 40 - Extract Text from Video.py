
import cv2
import subprocess
import os

def extract_text_from_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video not found!")
        return

    tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    if not os.path.exists(tesseract):
        print("Tesseract OCR software not found!")
        return

    temp_image = os.path.join(
        os.path.dirname(video_path), "temp_frame.jpg"
    )

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Process every 10th frame
        if frame_count % 10 == 0:

            gray = cv2.cvtColor(
                frame, cv2.COLOR_BGR2GRAY
            )

            cv2.imwrite(temp_image, gray)

            result = subprocess.run(
                [tesseract, temp_image, "stdout"],
                capture_output=True,
                text=True
            )

            text = result.stdout.strip()

            if text:
                print("Extracted Text:")
                print(text)

    cap.release()

    if os.path.exists(temp_image):
        os.remove(temp_image)

    print("Text extraction completed!")


extract_text_from_video(
    r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments\video.mp4"
)
