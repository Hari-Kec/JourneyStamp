from ultralytics import YOLO

def load_yolo_model(model_path):
    return YOLO(model_path)