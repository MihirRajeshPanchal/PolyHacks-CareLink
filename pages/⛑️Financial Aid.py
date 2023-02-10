import streamlit as st

st.title('Financial Aid')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

name = st.text_input("Name", placeholder="John Doe")

email_id = st.text_input("Email", placeholder="abc@gmail.com", type="default")

mob_no = st.text_input("Mobile Number")

# income = st.slider('Annual Income', 0, 25000000, 10000)
# st.write("Annual Income is ₹",income)



def update_slider():
    st.session_state.slider = st.session_state.numeric
def update_numin():
    st.session_state.numeric = st.session_state.slider            

val = st.number_input('Selected Annual Income', value = 0, key = 'numeric', on_change = update_slider)


income = st.slider('Select Annual Income', min_value = 0, 
                        value = val, 
                        max_value = 2500000,
                        step = 100,
                        key = 'slider', on_change= update_numin)

option = st.selectbox(
    'For which disease you want Financial Aid',
    ('','Heart Problem','Chickenpox ', 'Pneumonia', 'Malaria', 'Dengue'))

st.write('You selected:', option)


if st.button('Apply'):
    if name =='' or email_id == '' or mob_no =='':
        st.error('Please fill the necessary details !')
    else:
        st.success("Applied Successfully !")

# st.write("I'm ", age, 'years old')

# income = st.text_input("Annual Income", placeholder="₹")

# expenses = st.text_input("Annual Expenses0", placeholder="₹")