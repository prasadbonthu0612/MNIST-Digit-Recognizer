# MNIST-Digit-Recognizer
MNIST-Digit-Recognizer  A handwritten digit recognition system using a CNN model trained on the MNIST dataset. Users can draw digits on a canvas, and the AI predicts them in real-time. Built with Python, TensorFlow, Tkinter, and OpenCV, it features real-time processing, AI-powered recognition, and an interactive GUI. 🚀


---

## **Overview**  
This project is a **Handwritten Digit Recognition System** that utilizes **Convolutional Neural Networks (CNNs)** trained on the **MNIST dataset**. It allows users to **draw a digit on a canvas**, and the trained model predicts the digit in real-time.  

The project is implemented using **Python, TensorFlow, Tkinter, and OpenCV** to provide a simple and interactive GUI for digit recognition.  

---

## **Project Workflow**  
1. **Training the Model**  
   - The model is trained using the **MNIST dataset**, which contains **60,000 training images** and **10,000 test images** of handwritten digits (0-9).  
   - A **CNN model** is built using **TensorFlow and Keras** with layers such as **Conv2D, MaxPooling, Flatten, Dense, and Dropout** for accurate predictions.  
   - The trained model is saved as **mnist_model.h5** for later use.  

2. **Digit Drawing Interface**  
   - A **Tkinter-based GUI** allows users to draw a digit on a canvas.  
   - The drawing is converted into a **28x28 grayscale image** to match the input format of the trained model.  

3. **Prediction**  
   - The drawn image is processed and fed into the CNN model.  
   - The model predicts the digit and displays the result in the GUI.  

---

## **Technology Stack**  
- **Programming Language**: Python  
- **Libraries Used**:  
  - TensorFlow & Keras (For Deep Learning Model)  
  - NumPy (For Image Processing)  
  - Pillow (For Image Manipulation)  
  - Tkinter (For GUI Development)  
  - OpenCV (For Image Handling)  

---

## **Project Files**  
- **`app.py`** → Main GUI application where users draw digits and get predictions.  
- **`draw_and_clear.py`** → Handles canvas drawing and clearing functionality.  
- **`prediction.py`** → Loads the trained model and predicts digits.  
- **`train_model.py`** → Trains a CNN on the MNIST dataset.  
- **`mnist_model.h5`** → Pre-trained model file.  

---

## **How to Use the Project?**  

### **Step 1: Install Dependencies**  
Make sure Python is installed, then install the required libraries:  
```sh
pip install tensorflow numpy pillow opencv-python matplotlib
```

### **Step 2: Train the Model (Optional)**  
If you want to train your own model instead of using the pre-trained one, run:  
```sh
python train_model.py
```
This will generate `mnist_model.h5`.

### **Step 3: Run the Application**  
To start the digit recognition app, run:  
```sh
python app.py
```
- Draw a digit on the canvas.  
- Click the **Predict** button to see the recognized digit.  
- Click **Clear** to redraw.  

---

## **Expected Output**  
- The GUI opens with a black canvas.  
- The user draws a digit using the mouse.  
- The model processes the image and displays the predicted digit.  

---

## **Future Enhancements**  
- Improve accuracy by training on custom handwritten digits.  
- Implement real-time webcam-based digit recognition.  
- Enhance the GUI for a better user experience.  

---

## **Conclusion**  
This project demonstrates the power of **Deep Learning** and **Computer Vision** in recognizing handwritten digits. It is a beginner-friendly application that showcases **CNN-based image classification** and **interactive GUI development**.  

---
![Image](https://github.com/user-attachments/assets/e53a0b72-00b5-44e5-98ec-56a285c8ff7e)
![Image](https://github.com/user-attachments/assets/b91b7f1a-e741-46f7-a0ea-0ec49e9ee2b5)
![Image](https://github.com/user-attachments/assets/2edfdcc0-4a64-44aa-9aab-a016632a6b69)
![Image](https://github.com/user-attachments/assets/47554f11-34bc-4d48-9175-9b60347f8dbb)
![Image](https://github.com/user-attachments/assets/a8578a8f-a58a-4e03-8c93-36736223f176)
![Image](https://github.com/user-attachments/assets/17ec9beb-0b2f-411d-9061-526a89d1cb2f)
![Image](https://github.com/user-attachments/assets/6e03184c-e6d3-4405-8a0a-884b887aa895)
![Image](https://github.com/user-attachments/assets/03243772-5904-4546-879d-6d2f4c8ff4ca)
