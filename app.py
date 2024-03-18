from scripts import getCompanyNames, getUserRequiredData, getSymbolFromName 
from views import companyInfoSection, loadCss
import streamlit as st
import json


st.set_page_config(page_title="Analysis with python", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

st.markdown("<h3>Hi!, welcome to stock analysis with python</h3>", unsafe_allow_html=True)

option = st.selectbox(
    'Select the company to analyze ?',
    getCompanyNames(),
    index=None)

if option: 
    st.markdown(f"<h3>{option}</h3>", unsafe_allow_html=True)
    st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
    companySymbol = getSymbolFromName(option)
    if not companySymbol:
        st.write('No company found with the required name')
    else:
        companyInfo = getUserRequiredData('info', companySymbol=companySymbol)
        loadCss()
        companyInfoSection(marketCap=companyInfo.get('marketCap'), currentPrice=companyInfo.get('currentPrice'), lastDividendValue=companyInfo.get('lastDividendValue'), sector=companyInfo.get('sector'), industry=companyInfo.get('industry'), dividendYield=companyInfo.get('dividendYield'), volume=companyInfo.get('volume'), targetHighPrice=companyInfo.get('targetHighPrice'), targetLowPrice=companyInfo.get('targetLowPrice'), bookValue=companyInfo.get('bookValue'), returnOnEquity=companyInfo.get('returnOnEquity'), recommendationKey=companyInfo.get('recommendationKey'))
