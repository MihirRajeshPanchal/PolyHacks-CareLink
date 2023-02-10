import streamlit as st
from scripts import chatgpt
from scripts import tts

st.set_page_config(
    page_title="CareLink - Connect",
    page_icon="👪",
)

def ttscall():
    prompt="Hi"
    tts.tts(prompt)  

def chatgptcall():
    chatgpt.chatgpt("hello")
    

st.title('Connect Us')
st.button("Create a Google Mee",on_click=chatgptcall)
st.button("TTS",on_click=ttscall)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 