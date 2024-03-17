import pandas as pd

def formatInfo(data):
    return (f'{data.info}').replace("'",'"')

def formatActions(data):
    df = data.actions 
    return addDateToData(df)


def formatIncomStatement(data):
    df = data.income_stmt
    return addDateToData(df)

def formatBalanceSheet(data):
    df = data.balance_sheet
    return addDateToData(df)

def formatCashFlow(data):
    df = data.cashflow
    return addDateToData(df)

def formatRecommendations(data):
    df = data.recommendations
    return df.to_json(orient='records',date_format='iso')

def formatShares(data):
    da = data.get_shares_full(start="2022-01-01", end=None)
    df = pd.DataFrame(list(da.items()), columns=['Date', 'Value'])
    df['Date'] = df['Date'].astype(str)
    return df.to_json(orient='records')

def addDateToData(tableData):
    tableData.reset_index(inplace=True)
    return tableData.to_json(orient='records',date_format='iso')