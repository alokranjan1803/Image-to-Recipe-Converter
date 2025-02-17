import streamlit as st
import requests
from PIL import Image
import io

# Set FastAPI Backend URL
FASTAPI_URL = "https://a57c-35-197-3-46.ngrok-free.app/predict"

# Streamlit App Title
st.title("🍽️ Image To Recipe Converter")

# File uploader
uploaded_file = st.file_uploader("📤 Upload a food image...", type=["jpg", "png"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_container_width=True)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    # Send image to FastAPI backend
    files = {"file": ("image.png", img_bytes, "image/png")}

    with st.spinner("⏳ Processing..."):
        try:
            response = requests.post(FASTAPI_URL, files=files)
            response.raise_for_status()  # Raise error for bad responses

            result = response.json()

            if "food_category" in result and "recipe" in result:
                st.success("✅ Recipe Generated Successfully!")
                st.subheader(f"🍽️ Predicted Dish: {result['food_category']}")
                st.subheader("📜 Generated Recipe:")
                st.write(result["recipe"])
            else:
                st.error("❌ Invalid response format. Please check the backend.")

        except requests.exceptions.RequestException as e:
            st.error("⚠️ Failed to process the image. Please try again.")
            st.write(f"🔍 Error details: {response.text if 'response' in locals() else 'No response received'}")
