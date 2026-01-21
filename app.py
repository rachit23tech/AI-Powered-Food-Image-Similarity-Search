import streamlit as st
import os
import numpy as np
from PIL import Image
from model.extractor import get_embedding
from search.find import search

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="AI Food Similarity Search",
    page_icon="🍔",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("🍕 AI-Powered Food Image Similarity Search")
st.write("Upload a food image and find visually similar food items using deep learning.")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("Upload Image")
uploaded = st.sidebar.file_uploader(
    "Choose a food image",
    type=["jpg", "png", "jpeg"]
)

# -------------------------------
# Main logic
# -------------------------------
if uploaded:
    os.makedirs("uploads", exist_ok=True)
    path = os.path.join("uploads", uploaded.name)

    with open(path, "wb") as f:
        f.write(uploaded.read())

    # Show query image
    st.subheader("Query Image")
    st.image(path, width=300)

    # Search
    with st.spinner("🔍 Searching similar food images..."):
        results, scores = search(path, return_scores=True)

    st.success("Done! Showing top matches 👇")

    # Display results
    st.subheader("Similar Images")
    cols = st.columns(5)

    for i, (img, score) in enumerate(zip(results, scores)):
        img_path = os.path.join("dataset_flat", img)
        if os.path.exists(img_path):
            cols[i].image(img_path, use_column_width=True)
            cols[i].caption(f"Similarity: {score:.2f}")

else:
    st.info("⬅ Upload a food image from the sidebar to start searching")
