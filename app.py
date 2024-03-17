import streamlit as st
from scripts import getCompanyNames

st.markdown("<h3>Hi!, welcome to stock analysis with python</h3>", unsafe_allow_html=True)

option = st.selectbox(
    'Select the company to analyze ?',
    getCompanyNames(),
    index=None)

st.write('You selected:', option)