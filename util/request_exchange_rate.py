import datetime

import requests


class RequestExchangeRate:
    # base currency
    currencies = ['CNY', 'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'HKD', 'NZD']

    @staticmethod
    def get_url_parm(base):
        """
        generate request parm

        :param base: base currency name

        :return url: request parm
        """
        c = ""
        for currency in RequestExchangeRate.currencies:
            if currency != base:
                c += currency + "%2C"
        c += "&base=" + base
        return c

    @staticmethod
    def get_url(base):
        """
        generate request url

        :param base: base currency

        :return: request url
        """
        return "https://api.apilayer.com/exchangerates_data/latest?symbols=" + RequestExchangeRate.get_url_parm(
            base)

    @staticmethod
    def get_request_header():
        """
        get private API key

        :return: API key
        """
        return {
            "apikey": "vWcM1xUFJRJCxw0oMNAzcvtWCVs3XxMM"
        }

    @staticmethod
    def get_response(url):
        """
        get response

        :param url: request url

        :return: response
        """
        return requests.request("GET", url, headers=RequestExchangeRate.get_request_header(), data={})

    @staticmethod
    def batch_request_exchange_rate():
        """
        batch request rate

        :return rate_matrix: exchange rate metrix
        """
        date = datetime.datetime.now()
        rates = []

        for currency in RequestExchangeRate.currencies:
            change_rate_json = RequestExchangeRate.get_response(RequestExchangeRate.get_url(currency)).json()
            r = change_rate_json['rates']
            r['base'] = currency
            rates.append(r)

        r = {"rate": rates, "date": str(date.date())}
        return r
