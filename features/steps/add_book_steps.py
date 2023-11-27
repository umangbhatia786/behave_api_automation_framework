from behave import *
from features.configuration.api_resources import LibraryAPIResources
from features.configuration.config import *
from features.resources.api_payload import get_add_book_payload
import requests
from features.resources.test_data_generator import *


@when(u'We execute the Add Book Resource for Library API')
def step_impl(context):

    context.response = requests.post(
        url=context.add_book_url,
        json=context.add_book_payload,
        headers=context.header
    )


@then(u'Verify Response Code is 200')
def step_impl(context):
    assert context.response.status_code == 200, 'Response Code is not 200'


@then(u'Verify that success message is returned in Response JSON')
def step_impl(context):
    response_json = context.response.json()
    assert response_json['Msg'] == 'successfully added', 'Msg in Response JSON is not as per requirement'


@then(u'Verify that ID generated is concatenation of ISBN and Aisle')
def step_impl(context):
    context.book_id = context.response.json()['ID']
    expected_id = context.isbn + context.aisle
    actual_id = context.response.json()['ID']
    assert actual_id == expected_id, 'Generated ID is not as per requirements'
    create_json_value_file(context.book_name, context.isbn, context.aisle, context.full_name, context.book_id)
