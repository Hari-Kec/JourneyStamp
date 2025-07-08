import cv2
import numpy as np

def get_visual_tags(model, image):
    results = model(image)
    tags = set()
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = result.names[cls_id]
            tags.add(label)
    return list(tags)
