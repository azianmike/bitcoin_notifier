import os, sys
from django.conf import settings
sys.path.append('/var/www/bitcoin_notifier')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitcoin_notifier_web.settings")

import django
django.setup()
from submitAlertJSON.models import Alert


def getActiveEmailAlerts(price, exchangeName):
    alertsLessThanPrice = Alert.objects.filter(priceThreshold__gte=price, sign='lessThan', exchange=exchangeName)
    alertsGreaterThanPrice = Alert.objects.filter(priceThreshold__lte=price, sign='greaterThan', exchange=exchangeName)
    listOfAlerts = []
    for alert in alertsLessThanPrice:
        listOfAlerts.append(alert)
    
    for alert in alertsGreaterThanPrice:
        listOfAlerts.append(alert)

    return listOfAlerts

#alerts = getActiveEmailAlerts(220, 'coinbase')
#print alerts
