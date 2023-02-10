import streamlit as st

st.title('Cardiac Prediction')

st.text_input("Enter Your age : ",placeholder='50')

st.text_input("Enter your Sex (0 - 1) : ",placeholder='1')

st.text_input("Enter Chest Pain (0 - 3) : ",placeholder='1')

st.text_input("Enter Resting Blood Pressure (94 - 200) : ",placeholder='100')

st.text_input("Enter Serum Cholestoral in mg/dl (126 - 564) : ",placeholder='150')

st.text_input("Enter Fasting Blood Sugar (0 - 1) : ",placeholder='1')

st.text_input("Enter Resting Electrocardiographic Results (0 - 2) : ",placeholder='1')

st.text_input("Enter Maximum Heart Rate achieved (71 - 202) : ",placeholder='100')

st.text_input("Enter Exercise Induced Angina (0 - 1) : ",placeholder='1')

st.text_input("Enter Old Peak (0.0 - 6.2) : ",placeholder='3.0')

st.text_input("Enter Slope of the Peak Exercise ST segment (0 - 2) : ",placeholder='1')

st.text_input("Enter Number of major vessels (0 - 4) : ",placeholder='1')

st.text_input("Enter Thalassemia (0 - 2) : ",placeholder='1')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 