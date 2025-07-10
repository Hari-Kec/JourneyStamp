import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from config import MODEL_PATH, CONFIDENCE_THRESHOLD

model = YOLO(MODEL_PATH)

def enhance_image(image):
    # Convert to NumPy array if it's a PIL image
    img_np = np.array(image) if isinstance(image, Image.Image) else image

    # Convert to BGR for OpenCV
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Increase contrast and brightness
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 30    # Brightness control (0-100)
    enhanced = cv2.convertScaleAbs(img_bgr, alpha=alpha, beta=beta)

    return Image.fromarray(cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB))

def detect_objects(image):
    # Enhance image before inference
    enhanced_img = enhance_image(image)

    results = model(enhanced_img, conf=CONFIDENCE_THRESHOLD)
    detected_classes = set()
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls)
            label = model.names[cls_id]
            detected_classes.add(label)
    return list(detected_classes)