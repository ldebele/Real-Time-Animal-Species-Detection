import os
import logging
from PIL import Image
import streamlit as st
from ultralytics import YOLO



MODEL_DIR = './runs/detect/train/weights/best.pt'

logging.basicConfig(
            filename="./logs/log.log", 
            filemode='a', 
            level=logging.INFO, 
            format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
        )

# load a model
model = YOLO(MODEL_DIR)

# st.sidebar.title("Info")
st.sidebar.header("**Animal Classes**")

for animal in sorted(os.listdir('./data/raw')):
    st.sidebar.markdown(f"- *{animal.capitalize()}*")

st.title("Animal Species Detection")
st.write()

# Load an image
image = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png', 'mp4'])


if image:
    image = Image.open(image)
     # predict the image
    predict = model.predict(image)

    # plot boxes
    boxes = predict[0].boxes
    plotted = predict[0].plot()[:, :, ::-1]

    if len(boxes) == 0:
        st.markdown("**No Detection**")

    # open the image.
    st.image(plotted, caption="Detected Image", width=600)
    logging.info("Detected Image")

   








