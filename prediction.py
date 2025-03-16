import numpy as np
from train_model import model
from PIL import Image, ImageDraw
import tkinter as tk

root = tk.Tk()
result_label = tk.Label(root, text="Predicted Digit: ")
result_label.pack()

def predict_digit(image, model, result_label):
    # Resize image to 28x28 pixels
    image = image.resize((28, 28))
    # Convert image to grayscale
    image = image.convert("L")
    # Convert image to numpy array
    image = np.array(image)
    # Normalize the image
    image = image / 255.0
    # Reshape the image to match the input shape of the model
    image = image.reshape(1, 28, 28, 1)
    # Predict the digit
    prediction = model.predict(image)
    digit = np.argmax(prediction)
    # Update the result label
    result_label.config(text=f"Predicted Digit: {digit}")