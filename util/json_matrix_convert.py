import request_exchange_rate
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
    def request_rate_to_matrix(rates):
        index = 0
        matrix = []
        for rate in rates:
            change_rate_array = JsonMatrixConvert.convert_to_array(rate['rates'])
            change_rate_array.insert(index, 1)
            matrix.append(change_rate_array)
            index += 1
        return matrix




if __name__ == '__main__':
    # # batch request exchange rate
    # json = JsonMatrixConvert.batch_request_exchange_rate()
    # # add timestamp and save to file
    # json_with_timestamp = {json}
    # json_with_timestamp = json_with_timestamp.append({'timestamp': datetime.datetime.timestamp()})
    # JsonPersistence.save_json(json_with_timestamp, './test.json')

    # load json from file
    file = open('./test.json', 'r')
    json = file.read()
    json = json
