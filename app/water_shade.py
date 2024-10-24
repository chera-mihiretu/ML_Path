import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

class SeparateImages():
    def splitNumbers(self, image):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        _, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV)
        contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


        digits = []


        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)

            if w > 10 and h > 20:
                digit = binary[y:y+h, x:x+w]

                copy_image = np.copy(digit)
                inverted_image = cv.bitwise_not(copy_image)

                digits.append([x, inverted_image])
        digits.sort(key=lambda item: item[0])

        ordered_list = []
        for i, image in digits:
            ordered_list.append(image)
            
        return ordered_list
    