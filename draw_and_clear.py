from tkinter import Canvas
from PIL import ImageDraw, Image

def draw_digit(event, canvas, draw, radius=8):
    x, y = event.x, event.y
    r = radius  # radius of the brush
    draw.ellipse([x - r, y - r, x + r, y + r], fill="white")
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="white")

def clear_canvas(canvas, width, height, draw):
    draw.rectangle([0, 0, width, height], fill="black")
    canvas.delete("all")
