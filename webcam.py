import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

# Define a video transformer class for frame processing


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # You can perform any image processing here
        # Example: Convert the image to grayscale
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img


# Set up the Streamlit interface
st.title("Webcam Stream with Streamlit")
st.write("This application uses your webcam to display a live feed.")

# Create a webrtc streamer
webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
