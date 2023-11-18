import numpy
import requests

currencies = ['CNY', 'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'HKD', 'NZD']

sample_json = '''{
    "success": true,
    "timestamp": 1700272623,
    "base": "USD",
    "date": "2023-11-18",
    "rates": {
        "CNY": 7.211104,
        "EUR": 0.91605,
        "JPY": 149.53504,
        "GBP": 0.802762,
        "AUD": 1.535391,
        "CAD": 1.37215,
        "HKD": 7.79725,
        "NZD": 1.667779
    }
}'''


def get_query_parm(from_currency, to_currency):
    if from_currency == to_currency:
        return currencies


def sample_query():
    payload = {}
    headers = {
        "apikey": "vWcM1xUFJRJCxw0oMNAzcvtWCVs3XxMM"
    }

    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=CNY%2CEUR%2CJPY%2CGBP%2CAUD%2CCAD%2CHKD%2CNZD%2C&base=USD"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    status_code = response.status_code
    result = response.text
    print(status_code)


if __name__ == '__main__':
    sample_query()
