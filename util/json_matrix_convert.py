from util.request_exchange_rate import RequestExchangeRate
from util.json_persistence import JsonPersistence


class JsonMatrixConvert:
    @staticmethod
    def convert_to_array(json_dict):
        matrix = []
        for key in json_dict:
            if key != 'base':
                matrix.append(json_dict[key])
        return matrix

    @staticmethod
    def json_to_matrix(rates):
        index = 0
        matrix = []
        for rate in rates:
            change_rate_array = JsonMatrixConvert.convert_to_array(rate)
            change_rate_array.insert(index, 1)
            matrix.append(change_rate_array)
            index += 1
        return matrix

    @staticmethod
    def get_latest_cached_matrix():
        cached_json = JsonPersistence.load_latest_json()['rate']
        return JsonMatrixConvert.json_to_matrix(cached_json)


if __name__ == '__main__':
    print(JsonMatrixConvert.get_latest_cached_matrix())
