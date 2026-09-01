import cv2
import numpy as np
from matplotlib import pyplot as plt

image_lambo = cv2.imread("./lambo.png")
image_shapes = cv2.imread("./shapes-1.png")
image_shapes_template = cv2.imread("./shapes_template.jpg")
img_gray = cv2.cvtColor(image_lambo, cv2.COLOR_BGR2GRAY)


def sobel_edge_detection (image):
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    sobel_x = cv2.Sobel(src=img_blur, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1)
    sobel_y = cv2.Sobel(src=img_blur, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=1)

    sobel_xy = cv2.magnitude(sobel_x, sobel_y)

    normalized_sobel =  cv2.normalize(sobel_xy, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    cv2.imshow("Sobel gradient magnitude", normalized_sobel)
    cv2.imwrite("Sobel gradient magnitude.png", normalized_sobel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def canny_edge_detection (image, threshold1, threshold2):
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    edges = cv2.Canny(image=img_blur, threshold1=threshold1, threshold2=threshold2)

    cv2.imshow("Canny Edge Detection", edges)
    cv2.imwrite("Canny Edge Detection.png", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def template_match(image, template):
    img_gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = img_gray_template.shape

    res = cv2.matchTemplate(img_gray_image, img_gray_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

    cv2.imshow("Template_matching", image)
    cv2.imwrite('Template_matching.png', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def resize (image, scale_factor:int, up_or_down:str):
    result = image.copy()

    for i in range(scale_factor):
        rows, cols = result.shape[:2]
        if up_or_down == "up":
            result = cv2.pyrUp(result, dstsize=(2 * cols, 2 * rows))
            cv2.imshow("Upscaled_resize", result)
            cv2.imwrite("Upscaled_resize.png", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif up_or_down == "down":
            result = cv2.pyrDown(result, dstsize=(2 // cols, 2 // rows))
            cv2.imshow("Downscaled_resize", result)
            cv2.imwrite("Downscaled_resize.png", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Has to be either 'up' or 'down'")


#sobel_edge_detection(image_lambo)
#canny_edge_detection(image_lambo, 50, 50)
#template_match(image_shapes, image_shapes_template)
#resize(image_lambo, 2, "up")
#resize(image_lambo, 2, "down")


