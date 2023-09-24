import streamlit as st
from chatbot import show as show_chatbot
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import requests
import time

PAGES = {"Chatbot": show_chatbot}
# Set the initial page
if "page" not in st.session_state:
    st.session_state.page = "Initial"


background_image = "https://www.solidbackgrounds.com/images/1920x1080/1920x1080-black-solid-color-background.jpg"
background = f"""
    <style>
    .stApp {{
        background-image: url({background_image});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
"""
st.markdown(background, unsafe_allow_html=True)

loading_animation_url = "https://lottie.host/fc4041d0-6129-4e3d-94ca-e8226011fea7/94nEUWqN9U.json"


custom_html = f"""
<div id="lottie-container" style="height:100vh; display:flex; align-items:center; justify-content:center;">
    <div id="animation-container" style="width:300; height:250;"></div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.9.1/lottie.min.js"></script>
<script>
    var animation = lottie.loadAnimation({{
        container: document.getElementById('animation-container'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: '{loading_animation_url}'
    }});

    setTimeout(function() {{
        document.getElementById('lottie-container').style.display = 'none';
    }}, 5000);
</script>
"""
st.components.v1.html(custom_html, height=650)
if st.session_state.page == "Initial":
    # Use time.sleep to wait for the animation to finish before loading the rest of the page
    time.sleep(5)
    # Second background (animation)
    background_image = "https://fireart.studio/wp-content/uploads/2018/06/dribble-perfect.gif.webp"
    background1 = f"""
        <style>
        .stApp {{
            background-image: url({background_image});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
    """
    st.markdown(background1, unsafe_allow_html=True)
    st.title("Welcome!  ")

    # Create buttons for navigation
    if st.session_state.page == "Initial":
        if st.button("Go to Chatbot"):
            st.session_state.page = "Chatbot"


elif st.session_state.page in PAGES:
    PAGES[st.session_state.page]()
