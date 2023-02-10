import json
import streamlit as st
from scripts import chatgpt
from scripts import tts
from streamlit_card import card
# from team import Prinkal, Mihir

st.set_page_config(
    page_title="CareLink - About Us",
    page_icon="❗",
)

st.title("About Us")

i=0
f = open('assets/team/teams.json')
data = json.load(f)
for key in data:
    col1, col2= st.columns(2)
    with col1:
        card(
        title="",
        text="",
        image=data[key]["urlToimage"],
        # url=data[key]["website"]
        )
            # st.header("Fortis Hospital")
            # st.image("https://medsurgeindia.com/wp-content/uploads/2020/03/Seven-Hills-Hospital-Mumbai1.jpg", width=200)
    with col2:
        # def openURL():
        #     r=requests.get(data[key]["booknow"])
        st.text(data[key]["sr"])
        st.header(data[key]["name"])
        st.text("📩 "+data[key]["mail"])
        st.text("📞 "+data[key]["phone"])
        st.button("Connect Now",key=i)
        # st.button("BOOK NOW", on_click=openURL)
    i+=1
    f.close()

# col1, col2 = st.columns(2)

# with col1:
#    st.image("assets/team/Mihir.jpeg")
#    st.image("assets/team/Prinkal.jpg")

# with col2:
#    st.header("Mihir Panchal")
   
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 