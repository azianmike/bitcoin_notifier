__author__ = 'michaelluo'


def tryGettingPrice(timesToTry):
    '''
    Tries getting the price x times (to account for HTTP errors and slow networks)

    '''
    from urllib2 import urlopen, HTTPError, URLError
    from json import loads
    for x in range(0, timesToTry):
        try:
            coinbaseJSON = loads(urlopen("https://api.coinbase.com/v1/prices/buy?qty=1").read())
            return coinbaseJSON
        except HTTPError:
            print HTTPError
        except URLError:
            print URLError

    return coinbaseJSON


def getCoinbasePrice():
    '''
    Use HTTP GET to get the price of 1 bitcoin.

    Returns (double) price of 1 bitcoin WITHOUT any fees.
    '''


    coinbaseJSON = tryGettingPrice(10)


    price = float(coinbaseJSON['subtotal']['amount'])

    return price

def getExchangePrice(exchange):
    if exchange == 'coinbase':
        return getCoinbasePrice()