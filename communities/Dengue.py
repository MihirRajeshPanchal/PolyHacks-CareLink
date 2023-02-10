import streamlit as st
import json
from streamlit_card import card
import requests

def app():
    i=0
    tab1, tab2, tab3, tab4 = st.tabs(["Hospitals", "Doctors", "Specialists","NGO"])
    with tab1:
        f = open('assets/dengue/dengue_hospitals.json')
        data = json.load(f)
        for key in data:
            col1, col2= st.columns(2)
            with col1:
                card(
                title="",
                text="",
                image=data[key]["urlToimage"],
                url=data[key]["website"]
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
                st.button("Book Now",key=i)
                # st.button("BOOK NOW", on_click=openURL)
            i+=1
            f.close()
    with tab2:
        f = open('assets/dengue/dengue_surgeons.json')
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
                st.button("Book Now",key=i)
                # st.button("BOOK NOW", on_click=openURL)
            i+=1
            f.close()
        with tab3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

        
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 