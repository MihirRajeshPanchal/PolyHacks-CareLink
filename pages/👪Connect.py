import streamlit as st
from scripts import chatgpt
from scripts import tts

def ttscall():
    prompt="Hi"
    tts.tts(prompt)
    

def chatgptcall():
    chatgpt.chatgpt("hello")
    

st.title('Connect Us')
st.button("Chatgpt",on_click=chatgptcall)
st.button("TTS",on_click=ttscall)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 