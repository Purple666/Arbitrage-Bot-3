import requests


class Template():
    
    r = ""                                    

    #CONSTRUCTOR
    def __init__(self,apiUrl):
        self.apiUrl = apiUrl
        self.bid = 0.0
        self.ask = 0.0
        
    #PUBLIC API

     #Used to get the current tick values for a market
    def getPrices(self,url,parameter):
        pass
        
    # Used to get retrieve the orderbook for a given market
    def getOrderBook(self):
        print('ciao')
    
    #MARKET Api

    # Returns open orders for a given market
    def getOpenOrders(self,url,market):
        pass
        
    
    #Used to place an sell order in a specific market
    def sell(self):
        print('ciao')
    
    #Used to place a buy order in a specific market
    def buy (self):
        print('ciao')

    #Used to cancel a buy or sell order.
    def cancel(self):
        print('ciao')

