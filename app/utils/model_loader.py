from ultralytics import YOLO
from app.config import MODEL_PATH

def load_model():
    model = YOLO(MODEL_PATH)
    return model
