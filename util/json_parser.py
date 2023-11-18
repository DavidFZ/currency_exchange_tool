import json


class JsonParser:
    # convert json string to dict
    @staticmethod
    def parse_json(json_str):
        json_dict = json.loads(json_str)
        return json_dict


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
