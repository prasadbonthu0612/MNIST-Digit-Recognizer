import cv2
import os
import tkinter as tk
import tensorflow as tf
from PIL import Image, ImageDraw
from draw_and_clear import draw_digit, clear_canvas
from prediction import predict_digit

if os.path.exists('mnist_model.h5'):
    print("Loading model from mnist_model.h5")
    model = tf.keras.models.load_model('mnist_model.h5')
else:
    print("Model file 'mnist_model.h5' not found. Please run train_model.py to train the model.")
    exit()

window = tk.Tk()
window.title("Digit Recognizer")

canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

image = Image.new("L", (canvas_width, canvas_height), "black")
draw = ImageDraw.Draw(image)

# Bind mouse events for drawing
canvas.bind("<B1-Motion>", lambda event: draw_digit(event, canvas, draw, radius=15))

# Buttons for prediction and clearing canvas
predict_button = tk.Button(window, text="Predict", command=lambda: predict_digit(image, model, result_label))
predict_button.pack()

clear_button = tk.Button(window, text="Clear", command=lambda: clear_canvas(canvas, canvas_width, canvas_height, draw))
clear_button.pack()

# Label to display the predicted digit
result_label = tk.Label(window, text="Draw a digit and click Predict", font=("Arial", 14))
result_label.pack()

# Run the application
window.mainloop()