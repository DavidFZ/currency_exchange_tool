import json


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


if __name__ == '__main__':
    json_dict = JsonPersistence.load_json('./test.json')
    print(json_dict)
