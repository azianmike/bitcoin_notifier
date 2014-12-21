__author__ = 'michaelluo'

import sys
import getopt

def checkValidArgs(args):
    if len(args) != 5:
        return True
    try:
        float(args[1])
    except ValueError:
        return True

    listOfCompareOperators = ['>', '<', '>=', '<=']
    if args[2] not in listOfCompareOperators:
        return True

    return False


def printUsageAndExit():
    print 'Invalid arguments: python main.py [price] [less than or greater (use <= or > or < or >=)] [email] [interval in hours]'
    sys.exit(2)


if __name__ == "__main__":
    '''
    Params:
    [price] [less than or greater (use <= or > or < or >=)] [email] [interval in hours]
    '''
    print type(sys.argv[1])
    if checkValidArgs(sys.argv):
        printUsageAndExit()


