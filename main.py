import PIL.Image
import streamlit as st
import PIL as pillow


with st.expander("Open Camera"):
    #start camera
    captured_image = st.camera_input("camera")

with st.expander("Open Image from Local"):
    captured_image = st.file_uploader("upload")

if captured_image:
#creating a instance
    img = PIL.Image.open(captured_image) #at first opening image image will be none before capturing

    bwimage=img.convert('L')

    st.image(bwimage)





