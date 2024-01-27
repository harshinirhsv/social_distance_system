import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

class FaceMaskDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Mask Detection")
        
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.predict_button = tk.Button(root, text="Predict", command=self.predict_image)
        self.predict_button.pack(pady=20)

        self.prediction_label = tk.Label(root, text="")
        self.prediction_label.pack()

        self.image_path = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            self.image_path = file_path
            self.show_image(file_path)

    def show_image(self, file_path):
        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

    def predict_image(self):
        if self.image_path:
            self.prediction_label.config(text="Predicting...")
            self.root.update()

            image = cv2.imread(self.image_path)
            predictions = self.predict(image)
            self.display_results(image, predictions)

    def predict(self, image):
        (h, w) = image.shape[:2]

        blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()

        predictions = []

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                face = image[startY:endY, startX:endX]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)
                face = np.expand_dims(face, axis=0)

                (mask, without_mask) = model.predict(face)[0]
                label = "Mask" if mask > without_mask else "No Mask"
                confidence = max(mask, without_mask) * 100
                predictions.append((label, confidence, (startX, startY, endX, endY)))
                
                
                
                
                
                
                
                
                
                
                

        return predictions

    def display_results(self, image, predictions):
        for (label, confidence, (startX, startY, endX, endY)) in predictions:
            cv2.putText(image, "{}: {:.2f}%".format(label, confidence), (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

        output_path = "result.jpg"
        cv2.imwrite(output_path, image)
        self.show_image(output_path)
        self.prediction_label.config(text="Detection completed.")

if __name__ == "__main__":
    prototxtPath = "face_detector/deploy.prototxt"
    weightsPath = "face_detector/res10_300x300_ssd_iter_140000.caffemodel"
    net = cv2.dnn.readNet(prototxtPath, weightsPath)
    
    model = load_model("classifier.model")

    root = tk.Tk()
    app = FaceMaskDetectionApp(root)
    root.mainloop()
