import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Load pre-trained YOLO model for person detection
net = cv2.dnn.readNet("yolo-coco/yolov3.weights", "yolo-coco/yolov3.cfg")
layer_names = net.getUnconnectedOutLayersNames()

def detect_social_distance_violation(original_image):
    # Convert image to blob and perform forward pass
    height, width, _ = original_image.shape
    blob = cv2.dnn.blobFromImage(original_image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)

    class_ids = []
    confidences = []
    boxes = []

    # Extract information from the output
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:  # Class ID 0 corresponds to person
                center_x, center_y, w, h = list(map(int, detection[0:4] * np.array([width, height, width, height])))
                x, y = center_x - w // 2, center_y - h // 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Counters for people and violations
    total_people = len(boxes)
    people_violating_distance = 0
    safe_people = 0

    # Check social distance violation
    for i in range(total_people):
        if i in indices:
            for j in range(i + 1, total_people):
                if j in indices:
                    distance = np.linalg.norm(np.array(boxes[i][:2]) - np.array(boxes[j][:2]))
                    if distance < 100:  # Adjust this threshold based on your scenario
                        people_violating_distance += 1
                    else:
                        safe_people += 1

    return total_people, people_violating_distance, safe_people, indices, boxes

def process_image(image_path, original_image):
    total_people, people_violating_distance, safe_people, indices, boxes = detect_social_distance_violation(original_image)

    # Draw bounding boxes on the image
    for i, box in enumerate(boxes):
        if i in indices:
            x, y, w, h = box
            color = (0, 0, 255) if i in indices else (0, 255, 0)
            cv2.rectangle(original_image, (x, y), (x + w, y + h), color, 2)

    # Show the image with bounding boxes
    cv2.imshow("Social Distance Detection", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Update the result label
    if people_violating_distance > 0:
        return "Alert", None
    else:
        return "Safe", None

class SocialDistanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Distance Violation Detection")

        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)

        browse_button = tk.Button(root, text="Browse Image", command=self.browse_image)
        browse_button.pack(pady=10)

        process_button = tk.Button(root, text="Process Image", command=self.process_image)
        process_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.png")])
        self.image_path = file_path
        self.display_image(file_path)

    def display_image(self, image_path):
        image = Image.open(image_path)
        image = ImageTk.PhotoImage(image)

        self.image_label.config(image=image)
        self.image_label.image = image

    def process_image(self):
        if hasattr(self, 'image_path'):
            original_image = cv2.imread(self.image_path)
            result, _ = process_image(self.image_path, original_image)

            # Update the result label
            self.result_label.config(text=result)

# Create Tkinter window
root = tk.Tk()
app = SocialDistanceApp(root)
root.mainloop()