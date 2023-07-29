import streamlit as st
from ultralytics import YOLO


MODEL_DIR = '../models/best.pt'

# load a model
model = YOLO(MODEL_DIR)

st.title("Animal Species Detection")
st.write()

# Load an image
image = st.file_uploader("Upload an image", type=['jpg', 'png', 'mp4'], key=1)

if image:
    # predict the image
    predict = model.predict(source=image, conf=0.25, show=True)
   








