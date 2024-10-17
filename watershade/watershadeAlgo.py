import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# This is image segmentation of an image 

image = cv.imread('watershade/image3.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

_, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV)


contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

digits = []
for contour in contours:
    x, y, w, h, = cv.boundingRect(contour)

    if w > 10 and h > 20:
        digit = binary[y:y+h, x:x+w]
        digits.append(digit)

        plt.imshow(digit)
        plt.show()