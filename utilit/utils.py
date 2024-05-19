import json
from pathlib import Path

from Account_transactions.utilit.clases import Operation


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
Создает список экземпляров и возращает их
    :param operations: list[dict]
    :return: list[Operation]
    """
    operations_classes = []
    for oper_ns in operations:
        oper_operationAmount = oper_ns["operationAmount"]
        oper_exemp = Operation(
            pk=oper_ns["id"],
            date=oper_ns["date"],
            amount=oper_operationAmount["amount"],
            state=oper_ns["state"],
            currency_name=oper_operationAmount["currency"]["name"],
            description=oper_ns["description"],
            from_=oper_ns.get("from"),
            to=oper_ns["to"],
        )
        operations_classes.append(oper_exemp)
    return operations_classes


def sort_operation_exec(operation: list[Operation]) -> list[Operation]:
    """
    Сортирует список экземпляров по дате
    :param operation:
    :return:
    """
    return sorted(operation, reverse=True)


