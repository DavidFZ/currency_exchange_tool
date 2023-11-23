from util.request_exchange_rate import RequestExchangeRate
from util.json_persistence import JsonPersistence


class JsonMatrixConvert:
    @staticmethod
    def convert_to_array(json_dict):
        """
        convert currency exchange rate json to rates

        :param json_dict: json object

        :return rates: rate list of exchange rate from specific base currency
        """
        rates = []
        for key in json_dict:
            if key != 'base':
                rates.append(json_dict[key])
        return rates

    @staticmethod
    def json_to_matrix(json_dict):
        """
        convert currency exchange rate json to matrix

        :param json_dict: json object

        :return matrix: rate matrix of exchange rate from json
        """
        index = 0
        matrix = []
        for rate in json_dict:
            change_rate_array = JsonMatrixConvert.convert_to_array(rate)
            change_rate_array.insert(index, 1)
            matrix.append(change_rate_array)
            index += 1
        return matrix

    @staticmethod
    def get_latest_cached_matrix():
        """
        get and read latest json file

        :return json: latest cached json file
        """
        cached_json = JsonPersistence.load_latest_json()['rate']
        return JsonMatrixConvert.json_to_matrix(cached_json)


if __name__ == '__main__':
    print(JsonMatrixConvert.get_latest_cached_matrix())
