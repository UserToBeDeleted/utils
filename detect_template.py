import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def detect_template(detect_path="camera0_end_frame.jpg", template_path="temp_franme.tif"):
    img = cv.imread(detect_path)
    temp = cv.imread(template_path)
    img2gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    temp2gray = cv.cvtColor(temp, cv.COLOR_BGR2GRAY)
    height, width = temp2gray.shape
    result = cv.matchTemplate(img2gray, temp2gray, cv.TM_SQDIFF)
    minval, maxval, minloc, maxloc = cv.minMaxLoc(result)
    top_left = minloc
    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv.rectangle(img, top_left, bottom_right, (0, 0, 255), 3)
    plt.subplot(121)
    plt.imshow(img,cmap="gray")
    plt.title("match result")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(temp,cmap="gray")
    plt.title("template")
    plt.xticks([])
    plt.yticks([])
    plt.show()
