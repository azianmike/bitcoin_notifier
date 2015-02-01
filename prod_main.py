__author__ = 'michaelluo'

import sys
from getPrice import getExchangePrice
import time
from notifyViaEmail import sendEmailUsingGmailSMTP, sendEmailUsingMandrill
import math
from getAlerts import getActiveEmailAlerts

def mainCheckLoop(compareOperator, email, exchange, interval, price):
    while (1):
        currPrice = getExchangePrice(exchange)
        assert (currPrice != None)
        allEmailAlerts = getActiveEmailAlerts(currPrice, exchange)
        for email in allEmailAlerts:
            sendEmailUsingMandrill(email['email'], message)

        time.sleep(1)


def main():
    '''
    Params:
    [less than or greater (use or < or >=)] [price] [email] [interval in hours] [exchange]
    '''
    if checkValidArgs(sys.argv):
        printUsageAndExit()

    exchange = sys.argv[1].lower()

    mainCheckLoop(compareOperator, email, exchange, interval, price)


if __name__ == "__main__":
    main()



