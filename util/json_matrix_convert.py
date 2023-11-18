from request_exchange_rate import RequestExchangeRate
from util.json_persistence import JsonPersistence


class JsonMatrixConvert:
    @staticmethod
    def convert_to_array(json_dict):
        matrix = []
        for key in json_dict:
            matrix.append(json_dict[key])
        return matrix

    @staticmethod
    def request_rate_to_matrix():
        rates = RequestExchangeRate.batch_request_exchange_rate()
        index = 0
        matrix = []
        for rate in rates:
            change_rate_array = JsonMatrixConvert.convert_to_array(rate['rates'])
            change_rate_array.insert(index, 1)
            matrix.append(change_rate_array)
            index += 1
        return matrix


if __name__ == '__main__':
    # batch request exchange rate
    requested_json = RequestExchangeRate.batch_request_exchange_rate()
    print(requested_json)
    JsonPersistence.save_json(requested_json, './test.json')

    # load json from file
    # file = open('./test.json', 'r')
    # cached_json = file.read()
    # # string to json
    # cached_json = str(cached_json)
    # cached_json = json.loads(cached_json)
    # print(cached_json)
    #
    # cached_json = JsonMatrixConvert.convert_to_array(cached_json)
    #
    # print(cached_json)
