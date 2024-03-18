from scripts import format_Mcap, format_recommendation

def getCompanyBasicInfo(marketCap, currentPrice, lastDividendValue, sector, industry, dividendYield, volume, targetHighPrice, targetLowPrice, bookValue, returnOnEquity, recommendationKey):
    dividend_yield_percentage = f'{"{:.2f}".format(dividendYield * 100)}%' if dividendYield is not None else None
    target_high_price = f'₹ {targetHighPrice}' if targetHighPrice is not None else None
    target_low_price = f'₹ {targetLowPrice}' if targetLowPrice is not None else None
    last_dividend_value = f'₹ {lastDividendValue}' if lastDividendValue is not None else None
    return_on_equity = "{:.2f}".format(returnOnEquity * 100) if returnOnEquity is not None else None
    
    return f"""
    <div class="info-container">
      
      <div class="info-child">
      <p class='title'>Market Cap:</p>
      <p class='value'>{format_Mcap(marketCap)}</p>
      </div>
      
      <div class="info-child">
        <p class='title'>Last Dividend:</p>
        <p class='value'>{last_dividend_value}</p>
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
      <p class='title'>Current Price:</p> 
      <p class='value'>{currentPrice}</p>
      </div>
      
       <div class="info-child">
      <p class='title'>Target High Price:</p> 
      <p class='value'>{target_high_price}</p>
      </div>

      <div class="info-child">
      <p class='title'>Target Low Price:</p>
      <p class='value'>{target_low_price}</p>
      </div>
      
      <div class="info-child">
      <p class='title'>Sector: </p>
      <p class='value'>{sector}</p>
      </div>
      
      <div class="info-child">
      <p class='title'>Industry: </p>
      <p class='value'>{industry}</p>
      </div>
      
      <div class="info-child">
      <p class='title'>Volume: </p>
      <p class='value'>{volume}</p>
      </div>
    </div>
"""