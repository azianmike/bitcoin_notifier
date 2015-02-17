__author__ = 'michaelluo'

import sys
from getPrice import getExchangePrice
import time
from notifyViaEmail import sendEmailUsingGmailSMTP, sendEmailUsingMandrill, checkAlertsAndSendEmail
import math
from getAlerts import getActiveEmailAlerts

def createMessage(alert, exchange, currPrice):
    compareOperator=''
    if alert['sign'] == 'lessThan':
        compareOperator='<'
    if alert['sign'] == 'greaterThan':
        compareOperator='>'
    message = 'Current price of 1btc on ' + exchange + ' is $' + str(currPrice)+' ('+compareOperator+str(alert['priceThreshold'])+') at '+str(time.strftime("%c"))
    message += '\n\nClick the link to cancel THIS specific alert http://coinsniff.com/cancelPage/'+alert['alertID']
    return message    

def mainCheckLoop(exchange):
    while (1):
        currPrice = getExchangePrice(exchange)
        assert (currPrice != None)
        allEmailAlerts = getActiveEmailAlerts(currPrice, exchange)
        for alert in allEmailAlerts:
            message = createMessage(alert,exchange, currPrice)
            #sendEmailUsingMandrill(alert['email'], message)
            checkAlertsAndSendEmail(alert['email'], message)
            print 'sent email to '+alert['email']
        time.sleep(1)


def main():
    '''
    Params:
    [less than or greater (use or < or >=)] [price] [email] [interval in hours] [exchange]
    '''
    exchange = sys.argv[1].lower()

    mainCheckLoop(exchange)


if __name__ == "__main__":
    main()



