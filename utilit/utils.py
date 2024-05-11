import json
from pathlib import Path


def loads_json(path: Path) -> list[dict]:
    with open(path, encoding='utf-8') as file:
        return json.load(file)







