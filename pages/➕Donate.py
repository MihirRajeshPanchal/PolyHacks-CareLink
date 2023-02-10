import streamlit as st

st.set_page_config(
    page_title="CareLink - Donate",
    page_icon="➕",
)

st.title('Donate')
st.subheader("The donated amount will be used to help people that require financial aids to fight various diseases.")
st.image("assets/qrcode.jpeg", width=200)

name = st.text_input('Name', placeholder='John Doe')

email = st.text_input('Enter your email', placeholder='abc@gmail.com')

amount_paid_file = st.file_uploader("Upload the Snapshot of the payment")

if st.button('Donate'):
    if name != "" and email != "":
        if amount_paid_file:
            st.success("Thanks for donating to this noble cause")
        else:
            st.warning("Please upload the snapshot of the payment")
    else:
        st.warning("Please fill all the fields")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 