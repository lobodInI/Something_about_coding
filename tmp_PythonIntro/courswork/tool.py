import json


def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data


def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)