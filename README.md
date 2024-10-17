# Machine Learning Project Path for Digit Recognition


###### Demo Video
![Demo Video](demo/freecompress-ML%20(1).gif) 
# 1. Introduction to Machine Learning
 - Engaged with various resources to understand the basics of machine learning.
![](demo/Screenshot%20from%202024-10-04%2015-11-12.png)
# 2. Environment Setup
 - Installed Python and necessary libraries like TensorFlow and Keras to create and train the model.

 3. Data Acquisition
 - Downloaded the MNIST dataset, a well-known dataset for handwritten digit recognition.

# 4. Data Preprocessing
#- Prepared the training data by reshaping the images and normalizing pixel values to improve model performance.
 - Converted labels into one-hot encoded format for classification.

# 5. Convolutional Neural Network (CNN) Development
### - Defined a CNN architecture that included:
 - Convolutional Layers: To automatically extract features from the images.
 - Max Pooling Layers: To reduce the spatial dimensions of the feature maps.
 - Flatten Layer: To convert the 2D matrices of features into a 1D vector for the fully connected layers.
 - Dense Layers: To output probabilities for each digit class (0-9) using softmax activation.

# 6. Model Training
 - Trained the CNN model using the prepared dataset, adjusting parameters such as batch size and epochs.

# 7. Model Evaluation
 - Evaluated the model's performance using accuracy metrics to ensure effective recognition of handwritten digits.
 - 

# 8. GUI Development
 - Developed an interactive graphical user interface (GUI) using Tkinter for user interaction.


# 9. Real-time Prediction
 - Implemented a feature that enables real-time digit recognition based on user input from the GUI.
 - ##### [MultiThreading](https://docs.python.org/3/library/threading.html)
    - Used Multithreading to predict the the number as the same time while the programming(GUI) is running with out being disurbed this will allow the model to do the prediction on another thread
 - ##### [ThreadPool](https://superfastpython.com/threadpool-python/)
    - Thread is needing since prediction is heavy operation it is not appropriate to create thread for every single call of motion of the mouse because the thread will continue running for a while even after the user is done drawing. 


# 11. Future Work
 - Considered enhancements for the model, such as integrating additional datasets or exploring advanced techniques for improved accuracy.

# 11. How to Run The Projet 

### Install Necessary modules.
```bash
# for processing the array easily 
pip install numpy
# Visual of the arrays in table form
pip install pandas
# for training the model
pip install tensorflow
# for visualization
pip install matplotlib
```

### Then navigate to [This Folder](ML_Path/)
```bash
cd ML_Path
python app.App.py
```
# Demo
## Training Data
![](demo/Screenshot%20from%202024-10-04%2015-13-22.png)

## More Demo
![](demo/Screenshot%20from%202024-10-04%2008-00-38.png)
![](demo/Screenshot%20from%202024-10-04%2008-01-26.png)
![](demo/Screenshot%20from%202024-10-04%2015-10-46.png)

![](demo/Screenshot%20from%202024-10-04%2015-10-46.png)
# Digit Recognition using Machine Learning

## Project Overview

This project focuses on building a digit recognition system using Machine Learning techniques. The system is trained to recognize hand-written digits from 0 to 9 using the **MNIST** 

## Features

- **Data Preprocessing**: Hand-written digit images are scaled and transformed for optimal model training.
- **Model Training**: Multiple algorithms are used for training (e.g., Support Vector Machines, K-Nearest Neighbors, etc.), and performance is compared.
- **Model Evaluation**: Accuracy and other metrics are evaluated to determine the effectiveness of the model.
- **Digit Prediction**: The model predicts the digit for new, unseen data.

## Technologies Used

- Python
- tensorflow
- Numpy
- Pandas
- Matplotlib

### File Structure Along with description
```bash
ML_Path
├── .gitignore                        # Git ignore file for version control
├── DigitPrediction.ipynb            # Model training code written on Google Colab
├── ModelTraining1.ipynb              # Model training code written on Google Colab
├── NumberRec.ipynb                  # Model training code written on Google Colab
├── README.md                         # Project overview and documentation
├── __init__.py                      # Initialization file for the package
├── first_ml                          # Folder containing the first machine learning project
│   └── main.py                      # Main script for the first ML project
├── multithreading                    # Basics of multithreading
│   └── main.py                      # Main script demonstrating multithreading concepts
├── numpy                             # Basics of NumPy
│   ├── 2dArray.py                   # 2D array operations in NumPy
│   ├── aray.npy                     # Example NumPy array file
│   ├── array.npz                    # Compressed NumPy array file
│   ├── array.txt                    # Text file containing array data
│   ├── array_basics.py              # Basic operations and examples in NumPy
│   ├── array_functions.py            # Functions for manipulating NumPy arrays
│   ├── array_reshaping.py            # Reshaping arrays in NumPy
│   ├── broadcasting.py               # Broadcasting concepts in NumPy
│   ├── missing_data.py               # Handling missing data in NumPy
│   ├── nparray.py                   # Additional NumPy array examples
│   ├── numpyio.py                   # Input/output operations with NumPy
│   ├── numpyoperation.py             # Various operations in NumPy
│   └── stacking_arrays.py            # Stacking multiple arrays in NumPy
├── pandas                            # Basics of Pandas
│   ├── data.csv                      # Sample data file in CSV format
│   ├── pandas_basics.py              # Basic operations and examples in Pandas
│   └── reading_file.py               # Script for reading files using Pandas
├── PIL_tutor                         # Basics in image processing
│   ├── main.py                      # Main script for image processing tutorials
│   └── test.png                     # Sample image for processing
├── test                               # Tests written to check the accuracy of the model
│   ├── .gitignore                    # Git ignore file for test folder
│   ├── __init__.py                  # Initialization file for the test package
│   ├── photo_generator.py            # Script for generating test images
│   └── test_average_prediction.py    # Script for testing average predictions
├── training_cnn                      # Codes for modeling and trained model files
│   ├── arranging_data.py             # Script for arranging training data
│   ├── digit_recognition_model.h5    # Trained digit recognition model file
│   ├── digit_recognition_model_01.h5  # Alternate trained model file
│   ├── digit_recognition_model_02.h5  # Another alternate trained model file
│   ├── load_kaggle_data.py           # Script for loading Kaggle data
│   ├── main.py                      # Main script for training the CNN model
│   ├── model_building.py             # Script for building the CNN model
│   ├── test.csv                      # Test dataset in CSV format
│   └── train.csv                     # Training dataset in CSV format
├── app                                # Contains user interface, model prediction, and GUI implemented with OOP
│   ├── image_processor.py             # Script for processing images in the app
│   ├── model_setup.py                 # Script for setting up the model in the app
│   ├── App.py                        # Main application script for the GUI
│   ├── __init__.py                   # Initialization file for the app package
│   └── main.py                       # Main entry point for the app
└── folder_structure.py               # Script to display the folder structure

```

