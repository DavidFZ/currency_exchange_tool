import datetime
import json

from util.time_util import TimeUtil
import os


class JsonPersistence:
    def save_json(json_dict, file_path):
        """
        save json to file

        :param json_dict: json object

        :param file_path: file path
        """
        with open(file_path, 'w') as f:
            j = json.dumps(json_dict)
            f.write(j)

    @staticmethod
    def load_json(file_path):
        """
        load json from file

        :param file_path: json file path
        :return: json object
        """
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def request_rate_and_save(file_name=TimeUtil.get_current_date() + ".json"):
        """
        request exchange rate from online API and save to file

        :param file_name: save json file name
        """
        file_name = "./data/" + file_name
        from util.request_exchange_rate import RequestExchangeRate
        requested_json = RequestExchangeRate.batch_request_exchange_rate()
        JsonPersistence.save_json(requested_json, file_name)

    @staticmethod
    def load_latest_json():
        """
        load latest json file
        :return: json object
        """
        file_name = JsonPersistence.load_latest_file_name()
        file_path = "./data/" + file_name
        return JsonPersistence.load_json(file_path)

    @staticmethod
    def load_latest_file_name():
        """
        load latest file name
        :return: latest cached json file name
        """
        folder = "./data/"
        files = os.listdir(folder)
        files.sort(key=lambda x: os.path.getmtime(folder + x))
        return files[-1]


if __name__ == '__main__':
    cached = JsonPersistence.load_latest_json()
    print(cached['rate'])
