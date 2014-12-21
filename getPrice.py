__author__ = 'michaelluo'



def getCoinbasePrice():
    '''
    Use HTTP GET to get the price of 1 bitcoin.

    Returns (double) price of 1 bitcoin WITHOUT any fees.
    '''
    from urllib2 import urlopen
    from json import loads
    coinbaseJSON = loads(urlopen("https://api.coinbase.com/v1/prices/buy?qty=1").read())

    price = coinbaseJSON['subtotal']['amount']

    return price
