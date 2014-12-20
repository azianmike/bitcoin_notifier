__author__ = 'michaelluo'

import smtplib
try:
    import UsernameAndPassword
except ImportError:
    raise ImportError('Make a UsernameAndPassword.py file with your username and password')



def sendEmailUsingGmailSMTP(loginUsername, loginPassword, recipient, message):
    """
    Takes in a loginUsername and loginPassword (used to login into Gmail SMTP
    Also takes in a recipient (to send notification to) and a message
    """

    sender = 'from@fromdomain.com'
    receivers = [recipient]

    message = 'Subject: Bitcoin notifier \n\nThis is a test e-mail message.'


    try:
       smtpObj = smtplib.SMTP('smtp.gmail.com:587')
       smtpObj.starttls()
       smtpObj.login(loginUsername, loginPassword)
       smtpObj.sendmail(sender, receivers, message)
       print "Successfully sent email"
    except smtplib.SMTPException:
       print "Error: unable to send email"

#sendEmailUsingGmailSMTP(UsernameAndPassword.gmailUsername, UsernameAndPassword.gmailPassword, "michaeluo@gmail.com", 'test')