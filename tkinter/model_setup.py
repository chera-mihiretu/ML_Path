from typing import *
from tensorflow.keras.models import load_model  # type: ignore
import numpy as np
import asyncio


import os
class MyModel:
    def __init__(self):
        self.model = load_model(f'{self.getPath()}/training_cnn/digit_recognition_model_02.h5')
    def getPath(self) -> str:
        return os.getcwd()
    

    def predictNumber(self, data) -> List[float]:
        predicted_class = self.model.predict(data)
        predicted_digit = np.argmax(predicted_class)
        confidence = np.max(predicted_class[0]) * 100 
        return [predicted_digit, confidence ]