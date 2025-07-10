# SceneSenseAI++: Smart Scene Tagger

> An AI-powered Proof of Concept (POC) that intelligently detects scene context, user role, and GPS metadata to generate auto-tag suggestions for images — built for JourneyStamp GPS Camera use-cases.

---

## 🚀 Project Overview

SceneSenseAI++ uses a combination of:
- 🔍 **YOLOv8** for object detection
- 🔠 **OCR (EasyOCR)** for reading text in images (e.g. brand names, documents)
- 🧠 **CLIP (OpenAI)** for semantic understanding and ranking of tags
- 🧩 Rule-based context enrichment based on **user roles**
- 🌍 Optional **GPS coordinates** to enhance tagging with location context

The app returns 3–5 intelligent tags per image in a clean JSON format.

---

## 🛠️ Tech Stack

| Category       | Tech Used                            |
|----------------|--------------------------------------|
| Image Models   | YOLOv8 (Ultralytics), CLIP (OpenAI)  |
| OCR            | EasyOCR                              |
| Language       | Python 3.8+                          |
| Frontend       | Streamlit                            |
| ML Frameworks  | PyTorch, OpenCV, NumPy, PIL          |
| Deployment     | Localhost / Streamlit Cloud (Optional) |

---

## 📂 Folder Structure

```

SceneSenseAI/
├── app/
│   ├── main.py                # Streamlit frontend
│   ├── run.py                 # Entry point
│   └── utils/
│       ├── model\_loader.py   # Loads YOLO model
│       ├── inference.py      # Runs object detection
│       ├── image\_utils.py    # PIL <-> OpenCV conversion
│       ├── gps\_utils.py      # Location context enrichment
│       ├── tag\_generator.py  # Role + context rules
│       ├── clip\_ranking.py   # CLIP-based tag ranking
├── yolov8n.pt                 # YOLOv8 model (download manually)
├── requirements.txt
└── README.md

````

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Hari-Kec/JourneyStamp.git
cd JourneyStamp
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download YOLOv8 Model

```python
from ultralytics import YOLO
YOLO('yolov8n.pt')  # Or download manually from: https://github.com/ultralytics/ultralytics
```

Place `yolov8n.pt` in the project root directory.

---

### 4. Run the App

```bash
streamlit run app/main.py
```

---

## 🧪 Sample Output

```json
{
  "image_id": "swiggy_delivery.jpg",
  "role": "Delivery Executive",
  "gps": { "lat": "19.07", "lon": "72.87" },
  "location_context": "Urban Area",
  "visual_tags": {
    "person": 0.88,
    "package": 0.74
  },
  "ocr_tags": ["swiggy", "food delivery"],
  "ranked_tags": [["package handover", 29.3], ["swiggy delivery", 27.1]],
  "final_tags": ["Package Delivered", "Client Doorstep"]
}
```

---

## 🎥 Demo Link

📎 [Watch the Demo Video](https://drive.google.com/file/d/106Lb6Cjp9WEUwK2xG1oH-4zRMVXjM2rc/view?usp=sharing)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and build upon it.

---

