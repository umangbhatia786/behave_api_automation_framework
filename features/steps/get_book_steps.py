from behave import *
import requests


@when(u'We execute the Get Book Resource for Library API providing ID as query parameter')
def step_impl(context):
    context.response = requests.post(
        url=context.get_book_url,
        params=context.param,
        headers=context.header
    )


@then(u'Verify ISBN is same as provided')
def step_impl(context):
    response_json = context.response.json()
    assert response_json[0]['isbn'] == context.validation_values[1], 'ISBN is not same as the one provided in test data'


@then(u'Verify Aisle is same as provided')
def step_impl(context):
    response_json = context.response.json()
    assert response_json[0]['aisle'] == context.validation_values[2], ('Aisle is not same as the one provided in test '
                                                                       'data')


@then(u'Verify Book Name is same as provided')
def step_impl(context):
    response_json = context.response.json()
    assert response_json[0]['book_name'] == context.validation_values[0], ('Book Name is not same as the one provided '
                                                                           'in test data')


@then(u'Verify Author Name is same as provided')
def step_impl(context):
    response_json = context.response.json()
    assert response_json[0]['author'] == context.validation_values[3], ('Book Name is not same as the one provided in '
                                                                        'test data')


@when(u'We execute the Get Book Resource for Library API providing Author Name as query parameter')
def step_impl(context):
    context.response = requests.post(
        url=context.get_book_url,
        params=context.param,
        headers=context.header
    )
