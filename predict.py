from ultralytics import YOLO
import os

model = YOLO(os.getcwd()+'/best.pt')
model.predict(source=os.getcwd()+'/images/bird.jpg', save=True, conf=0.1, iou=0.45, show_labels=True)
