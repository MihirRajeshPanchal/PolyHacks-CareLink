import streamlit as st

st.set_page_config(
    page_title="News & Update",
    page_icon="📰",
)

st.title('News & Updates')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 