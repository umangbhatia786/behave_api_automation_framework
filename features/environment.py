from features.configuration.api_resources import LibraryAPIResources
from features.configuration.config import get_config, read_json_value_file
from features.resources.api_payload import *
from features.resources.test_data_generator import *


def before_scenario(context, scenario):
    context.my_config = get_config()
    context.header = {'Content-Type': 'application/json'}

    if scenario.name.startswith("TC01"):
        context.book_name = generate_random_book_name()
        context.isbn = generate_random_isbn()
        context.aisle = generate_random_aisle()
        context.full_name = generate_random_full_name()
        context.add_book_url = f'{context.my_config["QA"]["baseURL"]}{LibraryAPIResources.add_book}'
        context.add_book_payload = get_add_book_payload(context.book_name, context.isbn, context.aisle,
                                                        context.full_name)

    elif scenario.name.startswith("TC02"):
        context.get_book_url = f'{context.my_config["QA"]["baseURL"]}{LibraryAPIResources.get_book}'
        context.validation_values = read_json_value_file()
        context.param = get_book_by_id_params(context.validation_values[4])

    elif scenario.name.startswith("TC03"):
        context.get_book_url = f'{context.my_config["QA"]["baseURL"]}{LibraryAPIResources.get_book}'
        context.validation_values = read_json_value_file()
        context.param = get_book_by_author_params(context.validation_values[3])

    elif scenario.name.startswith("TC04") or scenario.name.startswith("TC05"):
        context.delete_book_url = f'{context.my_config["QA"]["baseURL"]}{LibraryAPIResources.delete_book}'
        context.validation_values = read_json_value_file()
        context.delete_book_payload = get_delete_book_payload(context.validation_values[4])
