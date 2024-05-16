from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
OPERATION_PATH = Path.joinpath(ROOT_PATH, 'data', 'operations.json')
POINT_COUNT = 5


print(OPERATION_PATH)
