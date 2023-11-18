import requests


class Currency:
    currencies = ['CNY', 'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'HKD', 'NZD']

    @staticmethod
    def get_url_parm(base):
        c = ""

        for currency in Currency.currencies:
            if currency != base:
                c += currency + "%2C"

        c += "&base=" + base
        return c

    def get_url(base):
        return "https://api.apilayer.com/exchangerates_data/latest?symbols=" + Currency.get_url_parm(
            base)


if __name__ == '__main__':
    # str = "https://api.apilayer.com/exchangerates_data/latest?symbols=CNY%2CEUR%2CJPY%2CGBP%2CAUD%2CCAD%2CHKD%2CNZD%2C&base=USD"
    # print(str)
    # print(Currency.get_url('USD'))
    # print(str.__eq__(Currency.get_url_parm('USD')))

    url = Currency.get_url('USD')
    response = requests.request("GET", url)
    print(response.text)
