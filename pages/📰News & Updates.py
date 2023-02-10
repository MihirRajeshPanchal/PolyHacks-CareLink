import streamlit as st
import requests
from streamlit_card import card

news_api_key = "748632a42f504dbb8db801b55f963575"
url = f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={news_api_key}"

r = requests.get(url)
data = r.json()
data = data["articles"]
print(data)



st.title('News & Update')
for i in range(20):
    if data[i]["urlToImage"] is not None:
        img = data[i]["urlToImage"]
    else:
        img = "https://media.istockphoto.com/id/1032637132/photo/a-cup-of-coffee-glasses-and-newspaper-titled-health-medical.jpg?s=612x612&w=0&k=20&c=W52Q_4CXrdJs24wI_5qt4t72Hcs1AzpzkoSzntByUoY="
    col1, col2 = st.columns(2, gap="medium")
    if i%2 == 0:
        with col1:
            hasClicked = card(
            title="",
            text="",
            image=img,
            url=data[i]["url"],
            key=i,
            )
        with col2:
            placeholder = st.empty()
            placeholder.text(f"News {i+1}")
            st.subheader(data[i]["title"])
    else:
        with col2:
            hasClicked = card(
            title="",
            text="",
            image=img,
            url=data[i]["url"],
            key=i
            )
        with col1:
            placeholder = st.empty()
            placeholder.text(f"News {i+1}")
            st.subheader(data[i]["title"])
            



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 