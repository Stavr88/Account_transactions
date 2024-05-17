from Account_transactions.utilit.settings import OPERATION_PATH, POINT_COUNT
from Account_transactions.utilit.utils import loads_json, get_executed_operations, sort_operation_exec, \
    ret_list_class_is_operations

operations = loads_json(OPERATION_PATH)
operations_executed = get_executed_operations(operations)
get_class_is_operations = ret_list_class_is_operations(operations_executed)
sort_op = sort_operation_exec(get_class_is_operations)

for operations_executed in sort_op[:POINT_COUNT]:
    print()
    print(operations_executed)

