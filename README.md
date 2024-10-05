# Machine Learning Project Path for Digit Recognition

![](demo/Screenshot%20from%202024-10-04%2015-11-12.png)

# 1. Introduction to Machine Learning
 - Engaged with various resources to understand the basics of machine learning.

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

### Then navigate to [This Folder](tkinter/)
```bash
python App.py
```
# Demo
## Training Data
![](demo/Screenshot%20from%202024-10-04%2015-13-22.png)

## More Demo
![](demo/Screenshot%20from%202024-10-04%2008-00-38.png)
![](demo/Screenshot%20from%202024-10-04%2008-00-52.png)
![](demo/Screenshot%20from%202024-10-04%2008-01-05.png)
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

