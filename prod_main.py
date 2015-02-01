__author__ = 'michaelluo'

import sys
from getPrice import getExchangePrice
import time
from notifyViaEmail import sendEmailUsingGmailSMTP, sendEmailUsingMandrill
import math

def mainCheckLoop(compareOperator, email, exchange, interval, price):
    intervalInSeconds = float(interval) * 3600
    currInterval = 0
    startInterval = time.time()
    endInterval = time.time()
    while (1):
        currPrice = getExchangePrice(exchange)
        assert (currPrice != None)

            sendEmailUsingMandrill(email, message)
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
    price = float(sys.argv[2])
    compareOperator = sys.argv[1]
    email = sys.argv[3]
    interval = sys.argv[4]
    exchange = sys.argv[5].lower()

    mainCheckLoop(compareOperator, email, exchange, interval, price)


if __name__ == "__main__":
    main()



