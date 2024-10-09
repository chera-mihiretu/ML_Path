import os
from typing import *
from PIL import Image

from tkinter.App import MyApplication

curr_dir = os.getcwd()
split_curr = curr_dir.split('/')
if split_curr != 'test':
    split_curr.append('test')
split_curr.append('image')
curr_dir = '/'.join(split_curr)

files = os.listdir(curr_dir)





counted = [0 for _ in range(10)]
gotCount = [0 for _ in range(10)]
for i in files:
    image = Image.open(f'test/image/i')

    i = i.split('.')
    _, number, count = i

    result = my_app.getTheMatrixFromImage(image)
    value, percent = my_app.model.predictNumber(result)

    counted[number] += 1
    gotCount[value] += 1

percentage = []
for i in range(10):
    perVal = (gotCount[i] * 100) / counted[i]
    percentage.append(percentage)
