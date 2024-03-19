import streamlit as st 
from .htmlTemplets.companyInfoHtml import getCompanyBasicInfo
from .htmlTemplets.css import css

def selectedOptionHeading(selectedCompany):
    st.write(f"<h1>{selectedCompany}</h1>", unsafe_allow_html=True)
    

def companyInfoSection(companyInfo):
    availableOptions = []
    defaultOptions = ['dividendYield','marketCap','currentPrice','targetHighPrice','targetLowPrice','marketCap','lastDividendValue','returnOnEquity','bookValue','recommendationKey','dayLow','dayHigh']
    for key in companyInfo:
        if key not in defaultOptions:
            availableOptions.append(key)
    
    selectedOptions = st.multiselect(
    'Add ratio to table',
    availableOptions)
    st.write(getCompanyBasicInfo(companyInfo), unsafe_allow_html=True)

def loadCss():
    st.write(css, unsafe_allow_html=True)