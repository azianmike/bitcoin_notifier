__author__ = 'michaelluo'

import smtplib
import os, sys
from django.conf import settings
sys.path.append('/var/www/bitcoin_notifier')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitcoin_notifier_web.settings")
import django
django.setup()
from submitAlertJSON.models import AlertsPerHour
from deleteAlerts import deleteAllAlerts
try:
    import UsernameAndPassword
except ImportError:
    raise ImportError('Make a UsernameAndPassword.py file with your username and password')


def checkAlertLimits(recipient):
    import time
    tempPerson = AlertsPerHour.objects.get(person=recipient)
    if tempPerson.alertsSentInLastHour >= 10:
        deleteAllAlerts(recipient)
        sendEmailUsingMandrill(recipient, "You are receiving too many alerts, please calm down")
        return False
    else:
        currTime = time.time()
        if tempPerson.lastHour<currTime and tempPerson.lastHour+3600>currTime:
            tempPerson.alertsSentInLastHour += 1
        else:
            tempPerson.lastHour = currTime
            tempPerson.alertsSentInLastHour = 1
        tempPerson.save() 
    return True
        
def sendEmailUsingMandrill(recipient, message):
    """
    Takes in a loginUsername and loginPassword (used to login into Gmail SMTP
    Also takes in a recipient (to send notification to) and a message
    """

    if recipient == None or recipient == '' or '@' not in recipient or '.' not in recipient:
        raise AssertionError("Recipient email address it not valid")

    sender = 'notify@coinsniff.com'
    receivers = [recipient]

    message = 'From:'+sender+'\r\nTo:'+recipient+'\r\nSubject: Bitcoin notifier \n\n' + message


    try:
       smtpObj = smtplib.SMTP('smtp.mandrillapp.com:587')
       smtpObj.starttls()
       smtpObj.login(UsernameAndPassword.mandrillUsername, UsernameAndPassword.mandrillPassword)
       smtpObj.sendmail(sender, receivers, message)
    except smtplib.SMTPException:
       raise smtplib.SMTPException("Cannot connected to smtp")


def checkAlertsAndSendEmail(recipient, message):
    if not checkAlertLimits(recipient):
        return
    else:
        sendEmailUsingMandrill(recipient, message)

def sendEmailUsingGmailSMTP(recipient, message):
    """
    Takes in a loginUsername and loginPassword (used to login into Gmail SMTP
    Also takes in a recipient (to send notification to) and a message
    """

    if recipient == None or recipient == '' or '@' not in recipient or '.' not in recipient:
        raise AssertionError("Recipient email address it not valid")

    sender = 'from@fromdomain.com'
    receivers = [recipient]

    message = 'From:'+sender+'\r\nTo:'+recipient+'\r\nSubject: Bitcoin notifier \n\n' + message


    try:
       smtpObj = smtplib.SMTP('smtp.gmail.com:587')
       smtpObj.starttls()
       smtpObj.login(UsernameAndPassword.gmailUsername, UsernameAndPassword.gmailPassword)
       smtpObj.sendmail(sender, receivers, message)
    except smtplib.SMTPException:
       raise smtplib.SMTPException("Cannot connected to smtp")



#sendEmailUsingGmailSMTP(UsernameAndPassword.gmailUsername, UsernameAndPassword.gmailPassword, "michaeluo@gmail.com", 'test')
