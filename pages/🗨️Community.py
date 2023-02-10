import streamlit as st
from streamlit_card import card
from multiapp import MultiApp
from communities import Dengue,Chickenpox

app = MultiApp()

app.add_app("Dengue", Dengue.app)
app.add_app("Chickenpox", Chickenpox.app)

app.run()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 