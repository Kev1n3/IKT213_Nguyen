import cv2
import numpy as np

image1 = cv2.imread("./iris-1.png")
emptyPictureArray1 = np.zeros((image1.shape[0], image1.shape[1], 3), image1.dtype)


def padding (image, border_width):
    reflect = cv2.copyMakeBorder(image, border_width, border_width, border_width, border_width, cv2.BORDER_REFLECT)
    cv2.imshow("Reflected_iris-1", reflect)
    cv2.imwrite("Reflected_iris-1.png", reflect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop (image, x_0, x_1, y_0, y_1):
    cropped = image[y_0:y_1, x_0:x_1]
    cv2.imshow("Cropped_iris-1", cropped)
    cv2.imwrite("Cropped_iris-1.png", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize (image, width, height):
    resized = cv2.resize(image, (width, height))
    cv2.imshow("Resized_iris-1", resized)
    cv2.imwrite("Resized_iris-1.png", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def copy (image, emptyPictureArray):
    emptyPictureArray[:] = image
    cv2.imshow("Copied_iris-1", emptyPictureArray)
    cv2.imwrite("Copied_iris-1.png", emptyPictureArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def grayscale (image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale_iris-1', gray)
    cv2.imwrite("Grayscale_iris-1.png", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def hsv (image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("Hsv_iris-1", hsv)
    cv2.imwrite("Hsv_iris-1.png", hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def hue_shifted (image, emptyPictureArray, hue):
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_img[..., 0] = (hsv_img[..., 0] + hue) % 180
    hsv_img[..., 2] = np.clip(hsv_img[..., 2] + 50, 0, 255)
    bgr_img_new = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

    emptyPictureArray[:] = bgr_img_new

    cv2.imshow("Hue_shifted_iris-1", emptyPictureArray)
    cv2.imwrite("Hue_shifted_iris-1.png", emptyPictureArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def smoothing(image):
    blur = cv2.blur(image, (15, 15), cv2.BORDER_DEFAULT)
    cv2.imshow("Smoothing_iris-1", blur)
    cv2.imwrite("Smoothing_iris-1.png", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotate(image, rotation_angle):
    if rotation_angle == 90:
        rotate_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("Rotated_iris-1_90degree", rotate_image)
        cv2.imwrite("Rotated_iris-1_90degree.png", rotate_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif rotation_angle == 180:
        rotate_image = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imshow("Rotated_iris-1_180degree", rotate_image)
        cv2.imwrite("Rotated_iris-1_180degree.png", rotate_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print ("It was either 90 degree or 180 degree LOL")

#padding(image1, 100)
#crop(image1,200, 670, 200, 470)
#resize(image1, 200, 200)
#copy(image1, emptyPictureArray1)
#grayscale(image1)
#hsv(image1)
#hue_shifted(image1, emptyPictureArray1, 50)
#smoothing(image1)
#rotate(image1, 90)
#rotate(image1, 180)

