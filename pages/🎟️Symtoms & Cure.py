import streamlit as st
from scripts import chatgpt

st.set_page_config(
    page_title="Symtoms & Cure",
    page_icon="🎟️",
)

st.title('Symtoms & Cure')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

txt = st.text_area("Enter your Query")

def chatgptcall():
    prompt=txt
    ans = chatgpt.chatgpt(prompt)
    st.success(ans)
    
    
btn = st.button("Search",on_click=chatgptcall)
# print(btn)