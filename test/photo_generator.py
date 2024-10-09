import numpy as np 
from PIL import Image
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical



(x_train, y_train), (x_test, y_test) = mnist.load_data()

labelUsed = [0 for _ in range(10)]

for i in range(y_train.size):
    imgNumber = x_train[i,0:]
    label = y_train[i]

    image = Image.fromarray(imgNumber)
    image.save(f'test/image/image_{label}_{labelUsed[label]}.png')
    labelUsed[label] += 1
    