# Binance  Bot
# Made by: Blerton Asani
# Apply you own API Keys from binance


from binance.client import Client
from binance.enums import *
import math
import time


def float_to_string(number, precision=10):
    return '{0:.{prec}f}'.format(   
        number, prec=precision,
    ).rstrip('0').rstrip('.') or '0'
    
#Add Your own API
api_key =  ""
api_secret = ""


try:
    client = Client(api_key, api_secret)
    print("[+]Connected to Binance")
except:
    print("En error has occured while conneting to binance")
    

balance = 0.00021
pairfull = ''

def runBot(pair):
    fullPair = pair.strip()

    
    
    minQty = 1.0
    minPrice = 0.00000001;


    pairprice = client.get_avg_price(symbol= fullPair + 'BTC') # It trades against BTC feel free to change
    symbolPrice = float(pairprice['price']) 
    pairfull = fullPair + 'BTC'
    amountOfCoin = balance / symbolPrice  
    amountOfCoin = float_to_string(amountOfCoin, int(- math.log10(minQty)))
   
    buyorder = client.create_order(
    symbol=pairfull,
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=amountOfCoin)
    

    sellCoin  = float(amountOfCoin) - 1
    sellAmount = math.trunc(sellCoin)

   
    #get the price from the order 
    infoPrice =  buyorder['fills'][0]
    priceBought = infoPrice['price']

  
    percentSell = (float(priceBought) * 165) / 100
    roundedPriceToSell = float_to_string(percentSell, int(- math.log10(minPrice)))

    sellorder = client.create_order(
    symbol=pairfull,
    side=Client.SIDE_SELL,
    type=Client.ORDER_TYPE_LIMIT,
    price=roundedPriceToSell,
    timeInForce='GTC',
    quantity=sellAmount)

    print("--- %s seconds ---" % (time.time() - start_time))
   
   
   print("Waiting for limit sell order exeution")
   sleep(5)
  
    

symbol = input("Please enter the symbol:")
runBot(symbol.upper())

