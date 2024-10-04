import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical



(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_tran = x_train.astype('float32') / 255.0
x_text = x_test.astype('float32') / 255.0


# converting the 
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)


# converting the label into bit 
y_train = to_categorical(y_train, num_classes=10)  # Convert labels to one-hot encoding
y_test = to_categorical(y_test, num_classes=10)