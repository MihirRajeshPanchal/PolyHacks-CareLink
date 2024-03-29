import streamlit as st
from scripts import tts
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

st.set_page_config(
    page_title="SignUp",
    page_icon="📎",
)

st.title('Signup')

first_name = st.text_input('First Name', placeholder='John')
# st.write('The Patient Name is', first_name)

last_name = st.text_input('Last Name', placeholder='Doe')
# st.write('The Patient Name is', last_name)

email_id = st.text_input('Enter your email id', placeholder= 'abc@gmail.com', type="default")
# st.write('The Patient Name is', email_id)

passwd = st.text_input('Password','',type="password")
# st.write('The Patient Name is', passwd)

if st.button('Sign Up'):
    if first_name == '' or last_name == '' or email_id == '' or passwd == '':
        st.error("Please Fill up all the fields")
        tts.tts("Please Fill up all the fields")
    else:
        st.success('Sign Up Successfull !')
        tts.tts("Sign Up Successfull !")
        db = firestore.client()
        doc_ref = db.collection(u'polyhacks').document(u'signup')
        doc_ref.set({
            u'email': email_id,
            u'password': passwd,
        })
        st.balloons()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 