import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Use the JPG image now
image_base64 = get_base64("birth.jpg")
video_base64 = get_base64("video.mp4")

image_html = f"""
<div style='text-align: center; margin-top: 20px;'>
    <img src='data:image/jpeg;base64,{image_base64}' width='300' height='300' style='border-radius: 20px; box-shadow: 0 4px 15px rgba(214, 51, 108, 0.4);'>
</div>
"""

video_html = f"""
<div style="text-align:center; margin-top: 20px;">
    <video width="400" height="500" controls style="border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
"""

st.set_page_config(page_title="Happy Birthday Khirad", page_icon="🎉", layout="centered")

st.markdown(
    """
    <h1 style="text-align:center; font-family: 'Comic Sans MS', cursive, sans-serif; color: #d6336c;">
        🎉 Happy Birthday Khirad! 🎉
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(image_html, unsafe_allow_html=True)
st.markdown(video_html, unsafe_allow_html=True)

st.markdown(
    """
    <p style="text-align:center; color: #555; font-style: italic; margin-top: 30px;">
        Wishing you all the happiness and success on your special day!
    </p>
    """,
    unsafe_allow_html=True
)

st.balloons()
