import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import os

# Check if the model file exists
model_path = 'mnist_model.h5'
if os.path.exists(model_path):
    print(f"Loading model from {model_path}")
    model = tf.keras.models.load_model(model_path)
else:
    # Loading the MNIST dataset from TensorFlow
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Normalizing the pixel values to be between 0 and 1
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    # Reshaping the data to be in the form of (batch_size, height, width, channels)
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)

    # Building the convolutional neural network model using Keras
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')  
    ])

    # Compiling the model with the Adam optimizer and sparse categorical crossentropy loss
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Training the model on the training data
    history = model.fit(x_train, y_train, epochs=15, validation_data=(x_test, y_test))

    # Saving the model to a file
    model.save(model_path)
    print(f"Model saved to {model_path}")
