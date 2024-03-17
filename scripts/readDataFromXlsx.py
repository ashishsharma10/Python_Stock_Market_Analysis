import pandas as pd

def getCompanySymbols():
    company_list = []
    # Load spreadsheet
    xl = pd.read_excel('./data/NSE_COMPANIES_LIST.xlsx')

    # convert xlsx data to object
    companies_dictionaries = xl.to_dict(orient='records')

    # get symbols of companies
    for company in companies_dictionaries:
        company_list.append(company['Symbol']) 

    return company_list

def getNameFromSymbol(symbol):
    if(not symbol):
        return False

    # Load spreadsheet
    xl = pd.read_excel('./data/NSE_COMPANIES_LIST.xlsx')
    selectedCompanyName = ''

    # convert xlsx data to object
    companies_dictionaries = xl.to_dict(orient='records')
    for company in companies_dictionaries:
        if(company['Symbol'] == symbol.upper()):
            selectedCompanyName = company['Company Name']
            break

    return selectedCompanyName

def getCompanyNames():
    company_list = []
    # Load spreadsheet
    xl = pd.read_excel('./data/NSE_COMPANIES_LIST.xlsx')

    # convert xlsx data to object
    companies_dictionaries = xl.to_dict(orient='records')

    # get symbols of companies
    for company in companies_dictionaries:
        company_list.append(company['Company Name']) 

    return company_list