import json
from pathlib import Path

from utilit.settings import OPERATION_PATH


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
        if operait["state"] == "EXECUTED":
            executed_operations.append(operait)
    return executed_operations



def loads_last_operations(operations: list[dict]):
    """
    возвращает список дат с операциями
    :param operations:
    :return:
    """
    date_operations = []
    for date_ in operations:
        date_operations.append(date_["date"])
    return date_operations


    # return [list_opera for i  in operations]


# print(loads_json(OPERATION_PATH))
a = loads_json(OPERATION_PATH)
print(loads_last_operations(a))






