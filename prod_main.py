__author__ = 'michaelluo'

import sys
from getPrice import getExchangePrice
import time
from notifyViaEmail import sendEmailUsingGmailSMTP
import math

def checkValidArgs(args):
    if len(args) != 2:
        return True

    return False


def printUsageAndExit():
    print 'Invalid arguments: python main.py [less than or greater (use or < or >=)] [price] [email] [interval in hours] [exchange]'
    sys.exit(2)


def comparePrices(currPrice, price, compareOperator):
    if compareOperator == '<':
        if currPrice < price:
            return True
    elif compareOperator == '>':
        if currPrice > price:
            return True

    return False


def mainCheckLoop(compareOperator, email, exchange, interval, price):
    intervalInSeconds = float(interval) * 3600
    currInterval = 0
    startInterval = time.time()
    endInterval = time.time()
    while (1):
        currPrice = getExchangePrice(exchange)
        assert (currPrice != None)
        endInterval = time.time()
        currInterval = currInterval - abs(endInterval - startInterval)

        if comparePrices(currPrice, price, compareOperator) and currInterval <= 0:
            message = 'Current price of 1btc on ' + exchange + ' is $' + str(currPrice)+' ('+compareOperator+str(price)+') at '+str(time.strftime("%c"))
            sendEmailUsingGmailSMTP(email, message)
            print 'sent an email'
            startInterval = time.time()
            endInterval = time.time()
            currInterval = intervalInSeconds - abs(endInterval - startInterval)
            time.sleep(intervalInSeconds) #sleeps for the interval time so dont need to keep querying

        time.sleep(1)


def main():
    '''
    Params:
    [less than or greater (use or < or >=)] [price] [email] [interval in hours] [exchange]
    '''
    if checkValidArgs(sys.argv):
        printUsageAndExit()
    mysqlIP = sys.argv[2]

    mainCheckLoop(compareOperator, email, exchange, interval, price)


if __name__ == "__main__":
    main()




