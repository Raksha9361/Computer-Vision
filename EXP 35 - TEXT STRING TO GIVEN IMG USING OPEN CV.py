
import cv2

def add_text_to_image(image_path, text):

    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    height, width = image.shape[:2]

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    color = (0, 0, 255)

    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]

    x = (width - text_size[0]) // 2
    y = (height + text_size[1]) // 2

    cv2.putText(image, text, (x, y), font, font_scale,
                color, thickness)

    cv2.imshow("Image with Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



image_path = r"C:\Users\RAKCHA\OneDrive\Documents\Custom Office Templates\Pictures\Desktop\Experiments\sample.png"

user_text = input("Enter the text to display: ")

add_text_to_image(image_path, user_text)
