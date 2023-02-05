TOKEN = "5651698346:AAFI037dszKxKvLquy-Hfy1tB0aQoDNi-qY"
CURRENCIES = {
    'dollar': 'USD',
    'euro': 'EUR',
    'ruble': 'RUB'
}

EXCHANGE_RATE_KEY = "SEfPukPw5am4yoZFvQZhf0VjFhskXE9n"
EXCHANGE_RATE_API = 'https://api.apilayer.com/exchangerates_data/convert?to={to_curr}&from={from_curr}&amount={amount}'

START_MSG = "Привет!\nЭто бот для быстрого обмена валют. Если хочешь узнать курс валюты - напиши команду '/values'."
VALUES_MSG = "Чтобы узнать курс, напиши валюту 'из', валюту 'в' и сумму через пробел.\n." \
             "Сейчас я могу работать с такими валютами, выбирай:\n" + ', '.join(CURRENCIES.keys())

