import streamlit as st
from streamlit_card import card
from multiapp import MultiApp
from communities import Dengue,Chickenpox

app = MultiApp()

app.add_app("Dengue", Dengue.app)
app.add_app("Chickenpox", Chickenpox.app)

app.run()

# tab1, tab2, tab3, tab4 = st.tabs(["Hospitals", "Surgens", "Specialists","NGO"])

# with tab1:
#    col1, col2= st.columns(2)
#    with col1:
#     # card(
#     # title="",
#     # text="",
#     # image="https://medsurgeindia.com/wp-content/uploads/2020/03/Seven-Hills-Hospital-Mumbai1.jpg",
#     # )
#         st.header("Fortis Hospital")
#         st.image("https://medsurgeindia.com/wp-content/uploads/2020/03/Seven-Hills-Hospital-Mumbai1.jpg", width=200)
# with col2:
#        st.text("HELLO")

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


# # import components.authenticate as authenticate

# # st.set_page_config(
# #     page_title="Dashboard",
# #     page_icon="📈",
# # )

# # st.write("# Welcome to Dashboard! 👋")
 
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 