import streamlit as st

st.set_page_config(
    page_title="Community",
    page_icon="🗨️",
)

st.title('Community')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 