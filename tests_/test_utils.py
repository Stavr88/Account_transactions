from Account_transactions.utilit.utils import get_executed_operations


def test_get_executed_operations():
    operations = [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {}, {'state': '1111'}]
    execute = [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}]
    assert get_executed_operations(operations) == execute
