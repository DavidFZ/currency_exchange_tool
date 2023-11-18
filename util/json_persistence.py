import json

from util.date_util import DateUtil
from util.json_parser import JsonParser


class JsonPersistence:
    @staticmethod
    def save_json(json_dict, file_path):
        with open(file_path, 'w') as f:
            json.dump(json_dict, f)

    @staticmethod
    def append_json(json_dict, file_path):
        with open(file_path, 'a') as f:
            json.dump(json_dict, f)


if __name__ == '__main__':
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
    json_dict = JsonParser.parse_json(sample_json)
    sample_json = json.dumps(json_dict)
    print(json_dict['rates'])

    time_stamp = json_dict['timestamp']
    a = int(time_stamp)
    date = DateUtil.convert_timestamp_to_date(int(time_stamp))
    json_dict = [json_dict['base'], date, json_dict['rates']]
    print(json_dict)
    # JsonPersistence.save_json(json_dict, './test.json')
