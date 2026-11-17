
import cv2

def play_video_reverse_slow(video_path):

    cap = cv2.VideoCapture(video_path)

    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("Video not found! Check the file path.")
        return

    print("Playing video in reverse slow motion...")
    print("Press Q to stop.")

    for frame in reversed(frames):

        cv2.imshow("Reverse Slow Motion Video", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


play_video_reverse_slow(
    r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments\video.mp4"
)
