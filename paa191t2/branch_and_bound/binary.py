import math

MEMO_BOUND = dict()
MEMO_SOLVE = dict()


def serialize_key(key):
    return str(sorted(key.items()))


def get_bound(instances: dict, partition: dict, weights: dict):
    """Retorna valor de upper bound de relaxação"""
    key = serialize_key(partition)
    if MEMO_BOUND.get(key):
        return MEMO_BOUND[key]
    bound = 0

    for instance in instances:
        if weights[instance] > 0:
            bound += weights[instance]
            for element in instances[instance]:
                if not partition[element]:
                    bound -= weights[instance]
                    break
    MEMO_BOUND[key] = bound
    return bound


def solve_formula(instances: dict, partition: dict, weights: dict):
    """Retorna valor da solução final"""
    key = serialize_key(partition)
    if MEMO_SOLVE.get(key):
        return MEMO_SOLVE[key]
    result = 0
    for instance in instances:
        result += weights[instance]
        for element in instances[instance]:
            if not partition[element]:
                result -= weights[instance]
                break
    MEMO_SOLVE[key] = result
    return result


def build_start_solution(weights: dict):
    start_solution = 0
    return start_solution


def build_partition(node_list):
    return {str(i): True for i in node_list}


def stack(default_stack, node, value):
    default_stack.append([node, value])
    return default_stack


def unstack(default_stack: list):
    node_value = default_stack.pop()
    return default_stack, node_value


def binary_bb(start_nodes_list: list, instances: dict, weights: dict):

    stack_path = list()
    stack_path = stack(stack_path, start_nodes_list[0], 0)
    stack_path = stack(stack_path, start_nodes_list[0], 1)

    solution = build_start_solution(weights)
    partition = build_partition(start_nodes_list)
    visited = []

    c = 0
    while len(stack_path) > 0:
        stack_path, node_value = unstack(stack_path)
        node, value = node_value
        node_value = f"{node}_{value}"
        partition[str(node)] = value
        bound = get_bound(instances, partition, weights)
        if bound > solution:

            if node == start_nodes_list[-1]:
                path_solution = solve_formula(instances, partition, weights)

                if path_solution > solution:
                    solution = path_solution
 
            elif node_value not in visited:
                node_index = start_nodes_list.index(node)
                stack_path = stack(stack_path, start_nodes_list[node_index + 1], 0)
                stack_path = stack(stack_path, start_nodes_list[node_index + 1], 1)

            if len(visited) > 0 and node > int(visited[-1].split("_")[0]):
                visited = [node_value]
            else:
                visited.append(node_value)

    return solution
