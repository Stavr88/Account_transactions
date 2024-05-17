from Account_transactions.utilit.settings import OPERATION_PATH, OPERATION_PATH_TEST
from Account_transactions.utilit.utils import get_executed_operations, loads_json, ret_list_class_is_operations


def test_get_executed_operations():
    operations = [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {}, {'state': '1111'}]
    execute = [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}]
    assert get_executed_operations(operations) == execute


def test_loads_json():
    path_1 = OPERATION_PATH_TEST
    assert loads_json(path_1) == [{"id": 441945886}]

