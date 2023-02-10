import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
import datetime
from datetime import date
# import components.authenticate as authenticate
st.set_page_config(
    page_title="Book Appointment",
    page_icon="📑",
)

# Page configuration
st.title('Book Appointment')

name = st.text_input('Enter your Name', placeholder='John Doe')

number = st.text_input('Enter your Phone', placeholder='1234567890')

d = st.date_input(
"Select an Appointment Date: ",
date.today())

t = st.time_input('Select an Appointment Time:', datetime.time(8, 45))

email = st.text_input('Enter your email', placeholder='abc@gmail.com')

if st.button('Book Appointment'):
    if name == '' or number == '' or d == '' or t == '' or email == '':
        st.error("Please fill the credentials")
    else:
        st.success(f"Appointment Added for {name} : {number} on {d} : {t}")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 