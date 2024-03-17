import yfinance as yf
from .formatData import formatInfo, formatActions, formatShares, formatIncomStatement, formatBalanceSheet, formatCashFlow, formatRecommendations

def getUserRequiredData(requiredData, companySymbol):
    baseClass = yf.Ticker(f"{companySymbol.upper()}.NS")
    if(requiredData == 'info'):
           return formatInfo(baseClass)
    elif(requiredData  == 'actions'):
          return formatActions(baseClass)
    elif(requiredData == 'shares'):
          return formatShares(baseClass)
    elif(requiredData == 'incomeStatement'):
          return formatIncomStatement(baseClass)
    elif(requiredData == 'balanceSheet'):
          return formatBalanceSheet(baseClass)
    elif(requiredData == 'cashFlow'):
          return formatCashFlow(baseClass)
    elif(requiredData == 'recommendation'):
          return formatRecommendations(baseClass)
        