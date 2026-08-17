import numpy as np
import cv2

def print_image_information (image):
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    height, width, channels = image.shape
    print("Height : ", height)
    print("Width : ", width)
    print("Channels : ", channels)
    print("Size : ", image.size)
    print("Datatypo : ", image.dtype)

def print_camera_information():
    cam = cv2.VideoCapture(0)

    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_fps = cam.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

    while True:
        ret, frame = cam.read()
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord ('q'):
            break
    with open("camera_outputs.txt", "w") as f:
        f.write(f"CAMERA FPS : {str(frame_fps)}\n")
        f.write(f"CAMERA HEIGHT : {str(frame_height)}\n")
        f.write(f"CAMERA WIDTH : {str(frame_width)}\n")

    cam.release()
    out.release()
    cv2.destroyAllWindows()



image = cv2.imread("./iris-1.jpg", cv2.IMREAD_UNCHANGED)
print_image_information(image)
print_camera_information()






