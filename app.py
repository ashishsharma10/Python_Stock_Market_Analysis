from scripts import getCompanyNames, getUserRequiredData, getSymbolFromName 
from views import companyInfoSection, loadCss, selectedOptionHeading
import streamlit as st


st.set_page_config(page_title="Analysis with python", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

option = st.selectbox(
    'Select the company to analyze ?',
    getCompanyNames(),
    index=None)

if option: 
    selectedOptionHeading(option)
    companySymbol = getSymbolFromName(option)
    if not companySymbol:
        st.write('No company found with the required name')
    else:
        companyInfo = getUserRequiredData('info', companySymbol=companySymbol)
        loadCss()
        companyInfoSection(companyInfo)
