from Config import keys
from Parser import exchange_rate



class APIException(Exception):
    pass

class ExchangeConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if quote == base:
            raise APIException('Нельзя переводить валюту саму в себя!')

        if base not in keys.keys():
            raise APIException(f'Не удалось обработать валюту "{base}"! Попробуйте снова!')

        if quote not in keys.keys():
            raise APIException(f'Не удалось обработать валюту "{quote}"! Попробуйте снова!')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        base1, quote1 = keys.get(base), keys.get(quote)
        result = float(exchange_rate.get(base1)[1]) / float(exchange_rate.get(quote1)[0]) * amount
        total_base = round(result, 2)
        return total_base