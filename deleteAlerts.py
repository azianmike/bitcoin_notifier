import os, sys
from django.conf import settings
sys.path.append('/var/www/bitcoin_notifier')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitcoin_notifier_web.settings")
import django
django.setup()
from submitAlertJSON.models import Alert

def deleteAllAlerts(email):
    alerts = Alert.objects.filter(person=email)
    for tempAlert in alerts:
        tempAlert.deleteAlert()

#deleteAllAlerts('michaeluo@gmail.com')
