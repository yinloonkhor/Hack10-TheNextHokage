from ultralytics import YOLO
import os

model = YOLO('best.pt') # Validate the model
model.val(data=os.getcwd()+'/Naruto.v2-naruto_augmented.yolov8/data.yaml', iou=0.6, conf=0.001, imgsz=(640,640))
