import requests
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework import status

import json
from datetime import datetime, timedelta

from config.settings import CURRENCY_API_URL, CURRENCY_API_KEY


def convert_currency_to_usd(rub_price):
    usd_price = 0
    response = requests.get(
        f'{CURRENCY_API_URL}v3/latest?apikey={CURRENCY_API_KEY}&currencies=RUB'
    )

    if response.status_code == status.HTTP_200_OK:
        # print(response.json())
        usd_rate = response.json()['data']['RUB']['value']
        print(usd_rate)

        usd_price = round(rub_price * usd_rate)
    return usd_price


def set_schedule(*args, **kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        price=IntervalSchedule.SECONDS,

    )

    PeriodicTask.objects.create(
        interval=schedule,  # we created this above.
        name='Importing contacts',  # simply describes this periodic task.
        task='proj.tasks.import_contacts',  # name of task.
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
