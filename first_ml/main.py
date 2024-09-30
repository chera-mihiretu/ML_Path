import numpy as np 
import pandas as pd
import os 
import matplotlib.pyplot as pt
from sklearn.tree import DecisionTreeClassifier

curDir = os.getcwd()

curDir = curDir.split('/')
curDir.pop()

curDir =  '/'.join(curDir)

kaggle_data = pd.read_csv(curDir + '/digit-recognizer/train.csv')

print(kaggle_data)
