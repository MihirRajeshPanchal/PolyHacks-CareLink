from sklearn import preprocessing
import streamlit as st
from scripts import tts
import pandas as pd


def mlmodels():
    global age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
    df=pd.read_csv("./datasets/heart.csv")
    x = df.drop('target',axis='columns')
    y = df['target']
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 0)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.fit_transform(x_test)

    age=int(age)
    sex=int(sex)
    cp=int(cp)
    trestbps=int(trestbps)
    chol=int(chol)
    fbs=int(fbs)
    restecg=int(restecg)
    thalach=int(thalach)
    exang=int(exang)
    oldpeak=float(oldpeak)
    slope=int(slope)
    ca=int(ca)
    thal=int(thal)
    
    # age=int(age)
    # sex=int(sex)
    # cp=int(cp)
    # trestbps=int(trestbps)
    # chol=int(chol)
    # fbs=int(fbs)
    # restecg=int(restecg)
    # thalach=int(thalach)
    # exang=int(exang)
    # oldpeak=float(oldpeak)
    # slope=int(slope)
    # ca=int(ca)
    # thal=int(thal)
    
    if option=="Logistic Classification":
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()
        model.fit(x_train, y_train)
        ans = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
        return ans
    elif option=="Support Vector Machine Classifications":
        from sklearn.svm import SVC
        model = SVC(kernel = 'linear', random_state = 0)
        model.fit(x_train, y_train)
        ans = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
        return ans
    elif option=="Naive Bayes Classification":
        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
        model.fit(x_train, y_train)
        ans = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
        return ans
    elif option=="K Nearest Neighbor Classification":
        from sklearn.neighbors import KNeighborsClassifier
        model = KNeighborsClassifier(n_neighbors=3, metric = 'minkowski', p=2)
        model.fit(x_train, y_train)
        ans = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
        return ans
    elif option=="Decision Tree Classifier":
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
        model.fit(x_train, y_train)
        ans = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
        return ans
    return model.score(x_train,y_train)
    
    

st.set_page_config(
    page_title="Analyze Diease",
    page_icon="🔎",
)
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
    ('Logistic Classification', 'Support Vector Machine Classifications', 'Naive Bayes Classification' , 'K Nearest Neighbor Classification',))

if st.button('Analyze'):
    if age == '' or sex == '' or cp== '' or trestbps=='' or chol == '' or fbs == "" or restecg == "" or thalach=="" or exang=="" or oldpeak=="" or slope=="" or ca=="" or thal=="":
        st.error("Please fill all the data")
        tts.tts("Please fill all the data")
    else:
        pred = mlmodels()
        pred=str(pred)
        if pred == "0":
            st.success("Congrats!! You dont have heart problem")
            st.balloons()
        else:
            st.success("So Sorry, unfortunately You may have heart problem")

        # st.success("Accuracy Received : "+pred)
        # tts.tts("Accuracy Received : "+pred)
        


st.write('You selected:', option)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 