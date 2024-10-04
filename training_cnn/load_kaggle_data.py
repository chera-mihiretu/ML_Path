import pandas as pd
from tensorflow.keras.utils import to_categorical
# Load the Kaggle training data
kaggle_train_df = pd.read_csv('training_cnn/train.csv')

# Split the data into features (pixels) and labels
x_kaggle_train = kaggle_train_df.drop('label', axis=1).values  # Pixel values
y_kaggle_train = kaggle_train_df['label'].values  # Labels


# Normalize pixel values
x_kaggle_train = x_kaggle_train / 255.0


# Reshape the Kaggle data to (28, 28, 1) to match the MNIST format
x_kaggle_train = x_kaggle_train.reshape(-1, 28, 28, 1)



# Convert Kaggle training labels to one-hot encoded format
y_kaggle_train_encoded = to_categorical(y_kaggle_train, num_classes=10)
