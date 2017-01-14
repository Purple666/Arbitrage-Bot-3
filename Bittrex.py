
# Class for Bittrex echange that extend the tempalte class

import Template
import requests
import time
import hmac
import hashlib
import urllib


class Bittrex(Template.Template):
    def __init__(self, apiUrl):
        self.apiPublicUrl =  apiUrl + 'public'
        self.apiPrivateUrl = apiUrl + 'account'
        self.apiMarketURl =  apiUrl + 'market'
        self.bid = 0.0
        self.ask = 0.0
        self.apiKey = ''
        self.Secret = ''             
        self.sign = ""
# Override template.getPrices 
    def getPrices(self,url,parameter):
        parameters = {'market': parameter}
        self.r = requests.get(url,parameters)
        data = self.r.json()
        if data['success']:
            if self.bid !=  data['result']['Bid'] or self.ask !=  data['result']['Ask']:
                self.ask = data['result']['Ask']
                self.bid = data['result']['Bid']
                print('\t \t |BITTREX|')
                print( parameter +' \t BID: ', self.bid,'\t ASK: ',self.ask,'\t LAST: ',data['result']['Last'])
        else:
            print('ERROR')



# Returns open orders for a given market

    def getOpenOrders(self,url, market):
        nonce = int(time.time())
        urlrequest = url + '?apikey=' + self.apiKey + '&nonce=' +str(nonce)
        
        signature = hmac.new(self.Secret.encode(), urlrequest.encode(), hashlib.sha512).hexdigest()

        parameter = {
            'market':market,        
        }
        headers = {
            'apisign': signature
        }
        self.r = requests.get(urlrequest,parameter, headers= headers)
        print(self.r.url)
        print(self.r.json())



        
