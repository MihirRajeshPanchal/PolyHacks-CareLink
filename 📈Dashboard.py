import streamlit as st
from streamlit_card import card
import pandas as pd
import numpy as np
# from multiapp import MultiApp
# from communities import Dengue,Chickenpox

st.title("DASHBOARD")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [19.0760, 72.8777],
#     columns=['lat', 'lon'])

# st.map(df, zoom=1)

st.header("Causes of death(1990 - 2019)")
cols = ["Self-harm","Interpersonal violence","Exposure to forces of nature","Drowning","Environmental heat and cold exposure","Diarrheal diseases","Road injuries","Tuberculosis","HIV/AIDS","Parkinson's disease","Malaria","Fire, heat, and hot substances","Chronic kidney disease","Neoplasms","Digestive diseases","Cirrhosis and other chronic liver diseases","Chronic respiratory diseases","Alzheimer's disease and other dementias","Cardiovascular diseases","Nutritional deficiencies","Drug use disorders","Alcohol use disorders","Lower respiratory infections","Diabetes mellitus","Protein-energy malnutrition","Acute hepatitis"]
choice = st.selectbox("Select a cause", cols)
data = pd.read_csv("./datasets/above-age-70.csv")

data = data[choice]
st.line_chart(data, height=500)