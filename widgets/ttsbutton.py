from scripts import tts
import streamlit as st

def ttscall():
    prompt="Hi"
    tts.tts(prompt)
    
st.button("TTS",on_click=ttscall)