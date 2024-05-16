import json
from pathlib import Path

from Account_transactions.utilit.clases import Operation
from Account_transactions.utilit.settings import OPERATION_PATH


def loads_json(path: Path) -> list[dict]:
    """
    загружает json-файл и преобразует в список словарей
    :param path: Path
    :return: list[dict]
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    """
    Возвращает список положительно проведенных операций
    :param operations: list[dict]
    :return: list[dict]
    """
    executed_operations = []
    for operait in operations:
        if operait.get('state') == 'EXECUTED':
            executed_operations.append(operait)
    return executed_operations


def ret_list_class_is_operations(operations: list[dict]) -> list[Operation]:
    """

    :param operations:
    :return:
    """
    operations_classes = []
    for oper in operations:
        oper_operationAmount = oper['operationAmount']
        oper_exemp = Operation(
            date=operations['date'],
            pk=operations['id'],
            state=operations['id'],
        )
    pass


a = loads_json(OPERATION_PATH)
print(get_executed_operations(a))
