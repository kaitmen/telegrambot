import json
import requests

import settings

def get_value(currency):
    try:
        value = settings.CURRENCIES[currency.lower()]
        return value
    except KeyError:
        raise APIException(f"Валюта {currency} не найдена!")


def get_price_from_api(base_curr, sym_curr, amount):
    api = settings.EXCHANGE_RATE_API.format(to_curr=sym_curr, from_curr=base_curr, amount=amount)

    headers = {'apikey': settings.EXCHANGE_RATE_KEY}
    response = requests.get(api, headers=headers)

    if response.status_code != 200:
        raise APIException(f'Ошибка подключения к сервису обмена валют!')
    content = json.loads(response.content)
    if not content['success']:
        raise APIException(f"Ошибка подключения к сервису обмена валют!\n{content['info']}")

    return content['result']


class APIException(Exception):
    pass


class Exchanger:
    @staticmethod
    def get_price(base=None, sym=None, amount=None):
        if not (base and sym and amount):
            raise APIException('Неверное количество параметров!')

        base_curr = get_value(base)
        sym_curr = get_value(sym)
        if base_curr == sym_curr:
            raise APIException(f'Вы ввели одинаковые валюты{base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Количество {amount} должно быть числовым значением!')

        new_price = get_price_from_api(base_curr, sym_curr, amount)

        result = f"Перевод {amount} {base} в {sym} : {new_price}"
        return result

