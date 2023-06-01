import streamlit as st

URL = "https://i.ibb.co/J3N4crj/programming-coding-language-b-Ghpbm6-Um-Zqara-Wkp-JRob-Wllr-Wdp-ZWU-1746280966.jpg"


def settings():
    icon = 'content/favicon.png'

    st.set_page_config(page_title="Learn to code",
                       initial_sidebar_state='collapsed',
                       page_icon=icon)

    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://images.hdqwalls.com/download/dark-night-mountains-minimalist-4k-o4-3840x2400.jpg");
        background-size: 100%;
        background-color: rgba(0, 0, 0, 100);
    }
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title("Learn to code")
    st.image('https://wallpaperaccess.com/full/5522966.jpg')