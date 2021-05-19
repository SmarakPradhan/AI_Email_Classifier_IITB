import app1
import app2
import app3
import streamlit as st
import base64


PAGES = {
    "HOME": app1,
    "CLASSIFY EMAIL(with trained model)": app2,
    "CLASSIFY EMAIL(train new model)":app3
     
}

st.markdown(
    f"""
    <style>
    .reportview-container {{
       background: linear-gradient(120deg , #e2c35d , #fda085);
    }}
   .sidebar .sidebar-content {{
    #    background-image: linear-gradient(120deg ,#89D4CF ,#734AE8);
        background: #f5f5f3;
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()