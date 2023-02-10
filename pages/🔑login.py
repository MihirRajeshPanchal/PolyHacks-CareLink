import streamlit as st
from scripts import tts
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

st.set_page_config(
    page_title="CareLink - Login",
    page_icon="🔑",
)
st.title('Login')

email = st.text_input('Enter your email', placeholder='abc@gmail.com')

password = st.text_input('Enter your password', '', type='password')

if st.button('Login'):
    if email == '' or password == '':
        st.error("Please fill the credentials")
        tts.tts("Please fill the credentials")
    else:
        st.success("Login Successful")
        tts.tts("Login Successful")
        db = firestore.client()
        doc_ref = db.collection(u'polyhacks').document(u'login')
        doc_ref.set({
            u'email': email,
            u'password': password,
        })
        st.balloons()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 