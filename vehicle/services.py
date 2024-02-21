import requests
from rest_framework import status

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
