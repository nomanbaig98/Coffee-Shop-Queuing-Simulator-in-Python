import streamlit as st


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://image.similarpng.com/very-thumbnail/2020/08/Coffee-shop-logo-on-transparent-background-PNG.png);
                background-repeat: no-repeat;
                padding-top: 50px;
                background-position: 20px 30px;
                background-size: 75% 40%;
                margin-top: 10%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
