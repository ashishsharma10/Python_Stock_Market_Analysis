from scripts import format_Mcap, format_recommendation

def getCompanyBasicInfo(companyInfo):
    dividendYield = companyInfo.get('dividendYield')
    marketCap = companyInfo.get('marketCap')
    currentPrice = companyInfo.get('currentPrice')
    returnOnEquity = companyInfo.get('returnOnEquity')
    bookValue = companyInfo.get('bookValue')
    recommendationKey = companyInfo.get('recommendationKey')
    dayLow = companyInfo.get('dayLow')
    dayHigh = companyInfo.get('dayHigh')
    trailingPE = companyInfo.get('trailingPE')
    forwardPE = companyInfo.get('forwardPE')
    
    dividend_yield_percentage = f'{"{:.2f}".format(dividendYield * 100)}%' if dividendYield is not None else None
    trailing_PE = "{:.2f}".format(trailingPE) if trailingPE is not None else None
    forward_PE = "{:.2f}".format(forwardPE) if forwardPE is not None else None
    return_on_equity = "{:.2f}".format(returnOnEquity * 100) if returnOnEquity is not None else None
    
    return f"""
    <div class="info-container">
      
      <div class="info-child">
      <p class='title'>Market Cap:</p>
      <p class='value'>{format_Mcap(marketCap)}</p>
      </div>
      
      <div class="info-child">
      <p class='title'>Current Price:</p> 
      <p class='value'>{currentPrice}</p>
      </div>
      
      <div class="info-child">
        <p class='title'>HIgh / Low:</p>
        <p class='value'>{dayHigh} / {dayLow}</p>
      </div>
      
      <div class="info-child">
      <p class='title'>Divident Yield:</p> 
      <p class='value'>{dividend_yield_percentage}</p>
      </div>
      
      <div class="info-child">
      <p class='title'>Book Value:</p> 
      <p class='value'>{bookValue}</p>
      </div>
      
       <div class="info-child">
      <p class='title'>ROE:</p> 
      <p class='value'>{return_on_equity}</p>
      </div>

      <div class="info-child">
      <p class='title'>Recommendation:</p>
      <p class='value'>{format_recommendation(recommendationKey)}</p>
      </div>
      
       <div class="info-child">
      <p class='title'>Trailing PE:</p> 
      <p class='value'>{trailing_PE}</p>
      </div>

      <div class="info-child">
      <p class='title'>Forward PE:</p>
      <p class='value'>{forward_PE}</p>
      </div>

    </div>
"""