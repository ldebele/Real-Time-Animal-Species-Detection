import streamlit as st
from PIL import Image
from ultralytics import YOLO


MODEL_DIR = './models/best.pt'

# load a model
model = YOLO(MODEL_DIR)

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

    # open the image.
    st.image(plotted, caption="Detected Image", width=600)

   








