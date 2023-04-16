# Импортирую нужные библиотеки и словарь из основного файла tgbot.py
import json
import requests

valuta = {
    'Bitcoin': 'BTC',
    'Ethereum': 'ETH',
    'Arbitrum': 'ARB',
    'Tether': 'USDT',
    'Cardano': 'ADA',
    'XRP': 'XRP',
    'Dogecoin': 'DOGE',
    'SOLANA': 'SOL',
    'Доллар': 'USD'
}


class APIException(Exception):  # Создаю класс исключений, наследование от встроенных Exception
    pass


class Convertor:  # Класс Конвертер,который будет обрабатывать исключения и выводить в чат конвертацию валют
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = valuta[base]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = valuta[quote]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена!")

        if base_key == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={sym_key}")
        resp = json.loads(r.content)
        new_price = resp[sym_key] * amount
        new_price = round(new_price, 2)
        message = f"Цена {amount} {base} в {quote} : {new_price}"
        return message
