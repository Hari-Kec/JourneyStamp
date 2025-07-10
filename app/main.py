import streamlit as st
from PIL import Image
import uuid
import json
from utils.inference import detect_objects
from utils.tag_generator import generate_final_tags

st.set_page_config(page_title="JourneyStamp AutoTagger", layout="centered")

st.title("JourneyStamp AutoTagger POC")
st.markdown("Upload an image and provide context to get intelligent tags.")

image_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
role = st.selectbox("Select Your Role", options=[
    "Bank Officer",
    "Delivery Agent",
    "Field Executive",
    "Traveler",
    "Other"
])
lat = st.text_input("Latitude (e.g., 19.4567)", value="")
lon = st.text_input("Longitude (e.g., 72.8912)", value="")

if st.button("Generate Tags") and image_file:
    try:
        image = Image.open(image_file).convert("RGB")
        visual_tags = detect_objects(image)

        final_tags = generate_final_tags(visual_tags, role)

        gps_context = "Indoor Office" if "Chair" in visual_tags and "Laptop" in visual_tags else "Outdoor"

        output = {
            "image_id": str(uuid.uuid4())[:8],
            "role": role,
            "gps": {
                "lat": lat or "N/A",
                "lon": lon or "N/A"
            },
            "visual_tags": visual_tags,
            "location_context": gps_context,
            "final_tags": final_tags
        }

        st.json(output)
        st.download_button(
            label="Download JSON",
            data=json.dumps(output, indent=2),
            file_name="output.json",
            mime="application/json"
        )
    except Exception as e:
        st.error(f"Error processing image: {e}")
else:
    st.info("Please upload an image and fill all fields.")