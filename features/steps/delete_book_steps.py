from behave import *
import requests


@when(u'We execute the Delete Book Resource for Library API')
def step_impl(context):
    context.response = requests.post(
        url=context.delete_book_url,
        json=context.delete_book_payload,
        headers=context.header
    )


@then(u'Verify the message property')
def step_impl(context):
    response_json = context.response.json()
    assert response_json['msg'] == 'book is successfully deleted', 'Msg property is not as per the requirement'


@then(u'Verify Response Code is 404')
def step_impl(context):
    assert context.response.status_code == 404, 'Response Code is not 404'


@then(u'Verify the error message in message property')
def step_impl(context):
    response_json = context.response.json()
    assert response_json['msg'] == 'Delete Book operation failed, looks like the book doesnt exists', ('Msg property '
                                                                                                       'is not as per'
                                                                                                       ' the '
                                                                                                       'requirement')
