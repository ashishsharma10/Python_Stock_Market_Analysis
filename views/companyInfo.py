import streamlit as st 
from .htmlTemplets.companyInfoHtml import getCompanyBasicInfo
from .htmlTemplets.css import css

# def selectedOptionHeading(selectedCompany):
    

def companyInfoSection(marketCap, currentPrice, lastDividendValue, sector, industry, dividendYield, volume, targetHighPrice, targetLowPrice, bookValue, returnOnEquity, recommendationKey):
    st.write(getCompanyBasicInfo(marketCap, currentPrice, lastDividendValue, sector, industry, dividendYield, volume, targetHighPrice, targetLowPrice, bookValue, returnOnEquity, recommendationKey), unsafe_allow_html=True)

def loadCss():
    st.write(css, unsafe_allow_html=True)