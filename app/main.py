import streamlit as st
from PIL import Image
from app.utils.model_loader import load_model
from app.utils.image_utils import pil_to_cv2
from app.utils.inference import get_visual_tags
from app.utils.tag_generator import enrich_tags
from app.utils.gps_utils import get_location_context

def main():
    st.set_page_config(page_title="SceneSenseAI", layout="centered")
    st.title("📸 SceneSenseAI: Auto Tagging POC")

    # User inputs
    role = st.selectbox("Select User Role", ["Field Agent", "Bank Officer", "Delivery Executive", "Surveyor"])
    gps_lat = st.text_input("GPS Latitude (optional)", "")
    gps_lon = st.text_input("GPS Longitude (optional)", "")

    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        image = pil_to_cv2(Image.open(uploaded_image))

        with st.spinner("Analyzing image..."):
            model = load_model()
            tags = get_visual_tags(model, image)
            location_context = get_location_context(gps_lat, gps_lon)
            final_tags = enrich_tags(role, tags, gps={"lat": gps_lat, "lon": gps_lon})

            output_json = {
                "image_id": uploaded_image.name,
                "role": role,
                "gps": {
                    "lat": gps_lat,
                    "lon": gps_lon
                },
                "visual_tags": tags,
                "location_context": location_context,
                "final_tags": final_tags
            }

            st.success("Visual Tags Extracted ✅")
            st.json(output_json)

if __name__ == "__main__":
    main()
