import streamlit as st
# import components.authenticate as authenticate

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Welcome to Dshboard! 👋")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 