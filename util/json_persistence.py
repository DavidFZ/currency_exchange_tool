import datetime
import json

from util.time_util import TimeUtil
import os


class JsonPersistence:
    @staticmethod
    def save_json(json_dict, file_path):
        with open(file_path, 'w') as f:
            j = json.dumps(json_dict)
            f.write(j)

    @staticmethod
    def load_json(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def request_rate_and_save(file_name=TimeUtil.get_current_date() + ".json"):
        file_name = "../data/" + file_name
        from util.request_exchange_rate import RequestExchangeRate
        requested_json = RequestExchangeRate.batch_request_exchange_rate()
        JsonPersistence.save_json(requested_json, file_name)

    @staticmethod
    def load_latest_json():
        file_name = JsonPersistence.load_latest_file_name()
        file_path = "./data/" + file_name
        return JsonPersistence.load_json(file_path)

    @staticmethod
    def load_latest_file_name():
        folder = "./data/"
        files = os.listdir(folder)
        files.sort(key=lambda x: os.path.getmtime(folder + x))
        return files[-1]


if __name__ == '__main__':
    cached = JsonPersistence.load_latest_json()
    print(cached['rate'])
