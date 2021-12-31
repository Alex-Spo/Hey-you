import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convetr(quote: str, base: str, amount:str):

        if quote == base:
            raise ConvertionExeption(f'Нельзя конвертировать одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise (f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise (f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Вводите правильно количество валюты, \nразделитель - точка')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        _base = json.loads(r.content)[keys[base]]
        total_base = round((_base * amount), 4)

        return total_base