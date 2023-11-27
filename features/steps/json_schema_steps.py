from behave import *
from jsonschema import validate
import json


@then(u'Verify JSON Schema of the Response returned')
def step_impl(context):
    scenario_name = context.scenario.name
    schema_file_path = None
    if scenario_name.startswith('TC01'):
        schema_file_path = 'features/resources/json_schemas/add_book_schema.json'

    elif scenario_name.startswith('TC02'):
        schema_file_path = 'features/resources/json_schemas/get_book_by_id_schema.json'

    elif scenario_name.startswith('TC03'):
        schema_file_path = 'features/resources/json_schemas/get_book_by_author_schema.json'

    elif scenario_name.startswith('TC04') or scenario_name.startswith('TC05'):
        schema_file_path = 'features/resources/json_schemas/delete_book_schema.json'

    with open(schema_file_path, 'r') as schema_file:
        schema = json.load(schema_file)

    data = context.response.json()

    try:
        # Validate the data against the schema
        validate(instance=data, schema=schema)
        print("JSON data is valid against the schema.")
    except Exception as e:
        print(f"Validation error: {e}")
