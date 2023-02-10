import streamlit as st

import streamlit as st

st.title('Signup')

first_name = st.text_input('Fisrt Name', placeholder='John')
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
    else:
        st.success('Sign Up Successfull !')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 