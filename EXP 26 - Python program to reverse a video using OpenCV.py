
import cv2
import os

def reverse_video(input_video_path, output_video_path):

    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error: Cannot open input video")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    
    frames.reverse()

    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        output_video_path,
        fourcc,
        fps,
        (frame_width, frame_height)
    )

    for frame in frames:
        out.write(frame)

    out.release()

    print("Reversed video saved successfully!")
    print("Output:", output_video_path)

    
    video = cv2.VideoCapture(output_video_path)

    while True:
        ret, frame = video.read()

        if not ret:
            break

        cv2.imshow("Reversed Video", frame)

        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

folder = r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments"


input_video = os.path.join(folder, "input_video.mp4")
output_video = os.path.join(folder, "output_reversed.mp4")

reverse_video(input_video, output_video)
