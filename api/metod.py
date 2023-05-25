from serializers.auth import CreateBooking
from pydantic.main import ModelMetaclass as PydanticModel

def delete_fields(flag: str, data: dict, model: PydanticModel, paths: list | tuple) -> None:
    if isinstance(paths, tuple):
        paths = [paths]

    fields_to_delete = []
    if flag == 'required':
        fields_to_delete = model.schema()['required']
    elif flag == 'optional':
        fields_to_delete = _get_optional_fields(model)

    for item in paths:
        obj = _get_value_by_path(data, item)
        for field in fields_to_delete:
            obj.pop(field)

def _get_value_by_path(data: dict, path: tuple) -> dict:
    current_val = data
    for key in path:
        current_val = current_val[key]

    return current_val

def _get_optional_fields(model: PydanticModel) -> list:
    if '$ref' in model.schema():
        all_fields = set(model.schema()['definitions'][f'{model.__name__}']['properties'].keys())
    else:
        all_fields = set(model.schema()['properties'].keys())

    try:
        required_fields = set(_get_required_fields(model))
    except KeyError:
        required_fields = set()

    return list(all_fields.difference(required_fields))


def _get_required_fields(model: PydanticModel) -> list:
    if '$ref' in model.schema():
        required_fields = model.schema()['definitions'][f'{model.__name__}']['required']
    else:
        required_fields = model.schema()['required']

    return required_fields

print(delete_fields(flag='required', ))

@pytest.mark.parametrize('model, path', fields_to_test)
def test_required_fields(model, path):

    order = prepare_data('create_order')

    fields_to_delete = get_required_fields_paths(model, path)
    delete_fields('required', order, model, path)

    create_order = order_base_client.create_order(order)

    assert create_order.status_code == 422, f'{create_order.text}'
    missing_fields = get_missing_fields(fields_to_delete, create_order.json()['detail'])
    assert len(missing_fields) == 0, missing_fields