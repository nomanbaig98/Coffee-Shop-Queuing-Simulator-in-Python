from PIL import Image

import streamlit as st
from utils import add_logo

st.set_page_config(
    page_title="CQC - Home",
    page_icon="img/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)
hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Add logo to sidebar top
add_logo()


canteen_str = """The coffee shop is a type of beverage service location where students and faculty members get coffee from baristas."""

qt_str = """Queuing Theory is one way of assessing and calculating the existing queue in a specific area.
       This queuing theory calculator was made to determine the measures of performance in waiting for lines which can be used to design services and reduce its adverse impact to tolerable levels.
       Features and queuing models that it has will be based on what are the different characteristics that the coffee shop consist of."""

st.markdown("### Coffee Shop Queuing Simulator in Python")
st.markdown("###### Hosted on Streamlit")
st.markdown("## Submitted to: Dr. Shaista Raees")
title_container = st.container()
col1, col2 = st.columns([8, 20])
image = Image.open("img/canteen.png")
with title_container:
    with col1:
        st.image(image)
    with col2:
        st.markdown(canteen_str, unsafe_allow_html=True)

st.write("\n\n")
st.write("\n\n")

st.markdown("#### Queuing theory on Coffee Shop")
title_container = st.container()
col1, col2 = st.columns([20, 8])
image = Image.open("img/qt.webp")
with title_container:
    with col2:
        st.image(image)
    with col1:
        st.markdown(qt_str, unsafe_allow_html=True)
