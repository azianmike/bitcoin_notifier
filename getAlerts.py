import os, sys
from django.conf import settings
sys.path.append('/var/www/bitcoin_notifier')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitcoin_notifier_web.settings")
import time
import django
django.setup()
from submitAlertJSON.models import Alert


def getActiveEmailAlerts(price, exchangeName):
    alertsLessThanPrice = Alert.objects.filter(priceThreshold__gte=price, sign='lessThan', exchange=exchangeName, nextAlert__lte=int(time.time()))
    alertsGreaterThanPrice = Alert.objects.filter(priceThreshold__lte=price, sign='greaterThan', exchange=exchangeName, nextAlert__lte=int(time.time()))
    listOfAlerts = []
    for alert in alertsLessThanPrice:
        temp = {}
        temp['email'] = alert.email
        temp['phone'] = alert.phone
        temp['priceThreshold'] = alert.priceThreshold
        temp['sign'] = alert.sign
        temp['intervalInSeconds'] = alert.intervalInSeconds
        temp['emailAlert'] = alert.emailAlert
        temp['textAlert'] = alert.textAlert
        listOfAlerts.append(temp)
    
    for alert in alertsGreaterThanPrice:
        temp = {}
        temp['email'] = alert.email
        temp['phone'] = alert.phone
        temp['priceThreshold'] = alert.priceThreshold
        temp['sign'] = alert.sign
        temp['intervalInSeconds'] = alert.intervalInSeconds
        temp['emailAlert'] = alert.emailAlert
        temp['textAlert'] = alert.textAlert
        listOfAlerts.append(alert)

    return listOfAlerts

alerts = getActiveEmailAlerts(190, 'coinbase')
print alerts
print int(time.time())
