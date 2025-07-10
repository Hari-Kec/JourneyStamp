# config.py
MODEL_PATH = "app/models/yolov8/yolov8s.pt"
LABELS_PATH = "app/models/labels.txt"
CONFIDENCE_THRESHOLD = 0.5
TAG_RULES = {
    "Bank Officer": {
        "Document Laptop Chair Man": ["KYC Visit", "Form Filled", "Office Verification"],
        "Desk Chair Laptop": ["KYC Visit", "Office Verification"]
    },
    "Delivery Agent": {
        "Package Delivery Bag Doorstep": ["Package Delivered", "Client Doorstep", "Delivery Confirmation"],
        "Truck Package": ["Delivery In Progress", "Route Tracking"]
    },
    "Field Executive": {
        "Gate Nameplate House": ["Client Home", "Address Verified"],
        "Storefront Restaurant Sign": ["Business Visit", "Location Verified"]
    },
    "Traveler": {
        "Tree Mountain Hill": ["Hiking", "Nature Trail", "Adventure"],
        "Temple Mosque Church": ["Spiritual", "Religious Site Visit"]
    },
    "Customer Service": {
        "Selfie Group": ["Customer Interaction", "Onsite Support"]
    }
}