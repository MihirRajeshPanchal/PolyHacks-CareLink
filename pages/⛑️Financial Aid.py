import streamlit as st
st.set_page_config(
    page_title="Financial Aid",
    page_icon="⛑️",
)

st.title('Financial Aid')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 