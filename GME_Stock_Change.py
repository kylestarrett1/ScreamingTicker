import yfinance as yf
import time
from playsound import playsound

#define the ticker symbol
tickerSymbol = 'GME'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

def current_price(tickerSymbol):
    ticker = yf.Ticker(tickerSymbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2021-2-28', end='2021-3-8')

lastPrice = 0

startTime = time.time()

while True:

    if current_price(tickerSymbol) < lastPrice:
        playsound('No_God_No.wav')
        print(str(time.asctime())+' ****************** $'+str(current_price(tickerSymbol))+' ******************')
    elif current_price(tickerSymbol) > lastPrice:
        playsound('napalm_death.mp3')
        print(str(time.asctime())+' ****************** $'+str(current_price(tickerSymbol))+' ******************')

    lastPrice = current_price(tickerSymbol)    

    
    time.sleep(300.0 - ((time.time() - startTime) % 300.0))