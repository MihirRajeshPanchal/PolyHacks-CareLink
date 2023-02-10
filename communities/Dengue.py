import streamlit as st
import json
from streamlit_card import card

def app():
    i=0
    tab1, tab2, tab3, tab4 = st.tabs(["Hospitals", "Surgeons", "Specialists","NGO"])
    f = open('assets/dengue.json')
    data = json.load(f)
    for key in data:
        with tab1:
            col1, col2= st.columns(2)
        if(i%2==0):
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
                st.text(data[key]["sr"])
                st.header(data[key]["name"])
        else:
            with col2:
                card(
                title="",
                text="",
                image=data[key]["urlToimage"],
                url=data[key]["website"]
                )
                    # st.header("Fortis Hospital")
                    # st.image("https://medsurgeindia.com/wp-content/uploads/2020/03/Seven-Hills-Hospital-Mumbai1.jpg", width=200)
            with col1:
                st.text(data[key]["sr"])
                st.header(data[key]["name"])
        i+=1
        f.close()
        with tab2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

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