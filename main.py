import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)
image = st.file_uploader("Upload Your Image", type=['jpg', 'jpeg', 'png', 'jfif'])
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)
    size.markdown(f"<h6>Size : {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode : {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format : {img.format}</h6>", unsafe_allow_html=True)

