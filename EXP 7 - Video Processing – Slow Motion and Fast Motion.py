import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Video",
    filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
)

video = cv2.VideoCapture(path)

if not video.isOpened():
    print("Error: Video not found!")
else:
    fps = video.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    print("Press N for normal, S for slow, F for fast, Q to quit")

    speed = 1

    while True:
        ret, frame = video.read()

        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        cv2.imshow("Video Processing", frame)

        key = cv2.waitKey(max(1, int(1000 / fps / speed))) & 0xFF

        if key == ord('n'):
            speed = 1
        elif key == ord('s'):
            speed = 0.5
        elif key == ord('f'):
            speed = 2
        elif key == ord('q'):
            break

    video.release()

cv2.destroyAllWindows()
