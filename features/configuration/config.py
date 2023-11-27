import configparser
from csv import *


def get_config():
    config = configparser.ConfigParser()
    config.read(r'features/configuration/properties.ini')
    return config


def create_json_value_file(*args):
    with open(r'features/resources/test_data/json_values.csv', 'w') as f:
        csv_writer = writer(f)
        csv_writer.writerow([*args])


def read_json_value_file():
    with open(r'features/resources/test_data/json_values.csv', 'r') as f:
        csv_reader = reader(f)
        csv_rows = []
        for row in csv_reader:
            csv_rows.append(row)
        return csv_rows[0]
