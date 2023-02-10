import streamlit as st
from scripts import tts


def mlmodels():
    if option=="Logistic Classification":
        pass
    elif option=="Support Vector Machine Classifications":
        pass
    elif option=="Naive Bayes Classification":
        pass
    

st.title('Cardiac Prediction')

age = st.text_input("Enter Your age : ",placeholder='50')

sex = st.text_input("Enter your Sex (0 - 1) : ",placeholder='1')

cp =st.text_input("Enter Chest Pain (0 - 3) : ",placeholder='1')

trestbps = st.text_input("Enter Resting Blood Pressure (94 - 200) : ",placeholder='100')

chol = st.text_input("Enter Serum Cholestoral in mg/dl (126 - 564) : ",placeholder='150')

fbs = st.text_input("Enter Fasting Blood Sugar (0 - 1) : ",placeholder='1')

restecg = st.text_input("Enter Resting Electrocardiographic Results (0 - 2) : ",placeholder='1')

thalach = st.text_input("Enter Maximum Heart Rate achieved (71 - 202) : ",placeholder='100')

exang = st.text_input("Enter Exercise Induced Angina (0 - 1) : ",placeholder='1')

oldpeak = st.text_input("Enter Old Peak (0.0 - 6.2) : ",placeholder='3.0')

slope = st.text_input("Enter Slope of the Peak Exercise ST segment (0 - 2) : ",placeholder='1')

ca = st.text_input("Enter Number of major vessels (0 - 4) : ",placeholder='1')

thal = st.text_input("Enter Thalassemia (0 - 2) : ",placeholder='1')

option = st.selectbox(
    'Model Making',
    ('Logistic Classification', 'Support Vector Machine Classifications', 'Naive Bayes Classification'))

if st.button('Login'):
    if age == '' or sex == '' or cp== '' or trestbps=='' or chol == '' or fbs == "" or restecg == "" or thalach=="" or exang=="" or oldpeak=="" or slope=="" or ca=="" or thal=="":
        st.error("Please fill all the data")
        tts.tts("Please fill all the data")
    else:
        acc = mlmodels()
        st.success("Accuracy Received : ",acc)
        tts.tts("Accuracy Received : ",acc)
        st.balloons()


st.write('You selected:', option)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 