import datetime

import requests


class RequestExchangeRate:
    currencies = ['CNY', 'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'HKD', 'NZD']

    @staticmethod
    def get_url_parm(base):
        c = ""
        for currency in RequestExchangeRate.currencies:
            if currency != base:
                c += currency + "%2C"
        c += "&base=" + base
        return c

    @staticmethod
    def get_url(base):
        return "https://api.apilayer.com/exchangerates_data/latest?symbols=" + RequestExchangeRate.get_url_parm(
            base)

    @staticmethod
    def get_request_header():
        return {
            "apikey": "vWcM1xUFJRJCxw0oMNAzcvtWCVs3XxMM"
        }

    @staticmethod
    def get_response(url):
        return requests.request("GET", url, headers=RequestExchangeRate.get_request_header(), data={})

    @staticmethod
    def batch_request_exchange_rate():
        date = datetime.datetime.now()
        rates = []

        for currency in RequestExchangeRate.currencies:
            change_rate_json = RequestExchangeRate.get_response(RequestExchangeRate.get_url(currency)).json()
            r = change_rate_json['rates']
            r['base'] = currency
            rates.append(r)

        r = {"rate": rates, "date": str(date.date())}
        return r
