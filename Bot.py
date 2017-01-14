
from Bittrex import Bittrex
from Poloniex import Poloniex
import threading

#Generic api url
URL = 'https://bittrex.com/api/v1.1/'
URLpoloniex = 'https://poloniex.com/'

#Instance object for each exchange
bittrex = Bittrex(URL)
poloniex = Poloniex(URLpoloniex)

bittrex.getOpenOrders(bittrex.apiMarketURl+'/getopenorders','BTC-ETH')

#function to call every 20s the function to get the current prices
def prices(): 
    bittrex.getPrices(bittrex.apiPublicUrl+'/getticker','BTC-ETH')
    poloniex.getPrices(poloniex.apiPublicUrl,'returnTicker')
    t = threading.Timer(20.0,prices)
    t.start()

#prices()


