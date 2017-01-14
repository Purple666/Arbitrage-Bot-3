
# Class for Poloniex  echange that extend the tempalte class

import Template
import requests

class Poloniex(Template.Template):
    def __init__(self, apiUrl):
        self.apiPublicUrl =  apiUrl + 'public'
        self.apiPrivateUrl = apiUrl + 'tradingApi'
        self.bid = 0.0
        self.ask = 0.0

# Override template.getPrices 
    def getPrices(self, url,parameter):
        parameters = {'command': parameter}
        self.r = requests.get(url,parameters)
        data = self.r.json()
        if self.bid !=  data['BTC_ETH']['lowestAsk'] or self.ask !=  data['BTC_ETH']['highestBid']:
            print('\t \t |POLONIEX|')
            self.ask = data['BTC_ETH']['lowestAsk']
            self.bid = data['BTC_ETH']['highestBid']
            print('BTC_ETH \t BID: ', self.bid,'\t ASK: ',self.ask,'\t LAST: ',data['BTC_ETH']['last'])
            print('\n')
        else:
            print('ERROR')
        