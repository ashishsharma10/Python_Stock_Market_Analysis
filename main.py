from scripts import getNameFromSymbol, getUserRequiredData
import pandas as pd
import sys

userName = input("Hi!, welcome to stock analysis with python, let's get started \n \nwhat is your name? : ")

companySymbol =  input(f'Hi {userName}, please tell me the company symbol you want to analyse : ')

companyName = getNameFromSymbol(companySymbol)

if(not companyName):
    print('not a valid company name')
    sys.exit()

isSelectedCompanyCorrect = input(f'so you want to analyze {companyName}, is that correct? Y/N : ').upper()

if(not isSelectedCompanyCorrect == 'Y'):
    print('sorry please try again')
    sys.exit()

print(f'now tell me the data you want to see')

companyDataList = ['info', 'actions', 'shares', 'incomeStatement', 'balanceSheet', 'cashFlow', 'recommendation']

df = pd.DataFrame(companyDataList, columns=['Data Available'])
print(df)

dataWanted = int(input('i want : '))

if(dataWanted < 0 or dataWanted > 6):
    print('not a valid selection')
    sys.exit()

isDataSelectionCorrect = input(f'so you wanna see {companyDataList[dataWanted]} of {companyName}? Y/N : ').upper()

if(not isDataSelectionCorrect == 'Y'):
    print('sorry please try again')
    sys.exit()

companyData = getUserRequiredData(requiredData=companyDataList[dataWanted], companySymbol=companySymbol)

print(companyData)
