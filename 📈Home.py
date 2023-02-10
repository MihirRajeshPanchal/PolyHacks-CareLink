import streamlit as st
from streamlit_card import card
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

st.set_page_config(
    page_title="CareLink - Home",
    page_icon="📈",
)
col1, col2 = st.columns(2)
with col1:
    st.image("assets/logo.jpg")
with col2:
    st.title("")
st.subheader("\nBringing hope to those in need")
st.write("The app aims to assist individuals who are unable to afford medical services due to financial constraints. The platform will connect these individuals with various financial aid resources such as NGOs, government agencies, and speciality hospitals that offer schemes and financial assistance for medical treatment. This web application provides a solution for those in need by presenting a centralized and accessible way to find financial support for medical services, helping to mitigate the financial burden and allow for necessary medical treatment.")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# st.title("Dashboard")
st.header("Causes of death(1990 - 2019)")
cols = ["Self-harm","Interpersonal violence","Exposure to forces of nature","Drowning","Environmental heat and cold exposure","Diarrheal diseases","Road injuries","Tuberculosis","HIV/AIDS","Parkinson's disease","Malaria","Fire, heat, and hot substances","Chronic kidney disease","Neoplasms","Digestive diseases","Cirrhosis and other chronic liver diseases","Chronic respiratory diseases","Alzheimer's disease and other dementias","Cardiovascular diseases","Nutritional deficiencies","Drug use disorders","Alcohol use disorders","Lower respiratory infections","Diabetes mellitus","Protein-energy malnutrition","Acute hepatitis"]
choice = st.selectbox("Select a cause", cols)
data = pd.read_csv("./datasets/above-age-70.csv")

data = data[choice]
st.line_chart(data, height=500)



st.header("People in Mumbai with cardio vascular disease")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.0760, 72.8777],
    columns=['lat', 'lon'])
st.map(df)


chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.header("People in San Francisco with cardio vascular disease")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))