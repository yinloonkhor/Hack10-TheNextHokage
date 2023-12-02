from ultralytics import YOLO
import os

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Train the model
model.train(data=os.getcwd()+"/Naruto.v2-naruto_augmented.yolov8/data.yaml", batch=12, epochs=80, imgsz=(640,640), val=True)  # train the model
