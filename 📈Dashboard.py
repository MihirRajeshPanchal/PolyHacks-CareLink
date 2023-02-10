import streamlit as st
from streamlit_card import card
import pandas as pd
import numpy as np
# from multiapp import MultiApp
# from communities import Dengue,Chickenpox

# app = MultiApp()

# app.add_app("Dengue", Dengue.app)
# app.add_app("Chickenpox", Chickenpox.app)

# app.run()
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


data = pd.read_csv("./datasets/above-age-70.csv")

st.line_chart(data)