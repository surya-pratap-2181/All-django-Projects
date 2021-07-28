from django.contrib.auth.signals import user_logged_in
from django.dispatch import Signal, receiver
from django.contrib.auth.models import User
from django.core.cache import cache

from django.http import request


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('-------------------------')
    print("Logged in Signal.... Run Intro")
    ip = request.META.get('REMOTE_ADDR')
    print('Client Ip:', ip)
    request.session['ip'] = ip
    ct = cache.get('count', 0, version=user.pk)
    newct = ct + 1
    cache.set('count', newct, 60*60*24, version=user.pk)


# Creating custom signal
notification = Signal(providing_args=['request', 'user'])


@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")
