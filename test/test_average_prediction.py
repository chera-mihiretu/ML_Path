import os
from typing import *
from PIL import Image
import numpy as np
from app.App import MyApplication

curr_dir = os.getcwd()
split_curr = curr_dir.split('/')
if split_curr != 'test':
    split_curr.append('test')
split_curr.append('image')
curr_dir = '/'.join(split_curr)

files = os.listdir(curr_dir)


my_app = MyApplication('')



counted = [0 for _ in range(10)]
gotCount = [0 for _ in range(10)]
countIter = 0
files.sort(key=lambda x: int(x.split('_')[2][:-4]))

for i in files[:1000]:
    image = Image.open(f'test/image/{i}')
    
    i, _ = i.split('.')
    _, number, count, = i.split('_')
    image.convert('RGBA')
    
    result = my_app.getTheMatrixFromImage(image)
    value, percent = my_app.model.predictNumber(result)
    print(number, value)
    counted[int(number)] += 1
    gotCount[int(value)] += 1

percentage = []
for i in range(10):
    perVal = (gotCount[i] * 100) / counted[i]
    percentage.append(percentage)





print("Real Val:",counted)
print("Recieved:",gotCount)
