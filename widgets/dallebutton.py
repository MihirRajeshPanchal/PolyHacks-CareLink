from scripts import dalle
import streamlit as st

def dallecall():
    prompt="anything"
    dalle.dalle(prompt)
    
st.button("Dalle",on_click=dallecall)