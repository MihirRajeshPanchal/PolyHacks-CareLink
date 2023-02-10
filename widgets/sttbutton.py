from scripts import stt
import streamlit as st

def sttcall():
    prompt="Hi"
    print(stt.stt())
    res = stt.stt()
    
st.button("TTS",on_click=sttcall)