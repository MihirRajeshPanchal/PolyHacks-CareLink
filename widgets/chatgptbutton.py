from scripts import chatgpt
import streamlit as st

def chatgptcall():
    prompt="hello"
    chatgpt.chatgpt(prompt)
    
st.button("Chatgpt",on_click=chatgptcall)