import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔑",
)
st.title('Login')

email = st.text_input('Enter your email', placeholder='abc@gmail.com')

password = st.text_input('Enter your password', '', type='password')

if st.button('Login'):
    if email == '' or password == '':
        st.error("Please fill the credentials")
    else:
        st.success("login")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 