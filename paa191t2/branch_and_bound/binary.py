MEMO_BOUND = dict()
MEMO_SOLVE = dict()
SOL = 0


def serialize_key(key):
    return str(sorted(key.items()))


def get_bound(instances: dict, partition: dict, weights: dict):
    """Retorna valor de upper bound de relaxação"""
    global MEMO_BOUND

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
    global MEMO_SOLVE

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


def recursive_bb(start_nodes_list, partition, instances, weights, node_index, value):
    global SOL

    print(SOL)
    node = start_nodes_list[node_index]
    partition[str(node)] = value
    bound = get_bound(instances, partition, weights)
    if node == start_nodes_list[-1]:
        partial_solution = solve_formula(instances, partition, weights)
        SOL = max(SOL, partial_solution)

    elif bound > SOL:
        node_index = start_nodes_list.index(node)
        recursive_bb(start_nodes_list, partition, instances, weights, node_index + 1, True)
        recursive_bb(start_nodes_list, partition, instances, weights, node_index + 1, False)
    return SOL


def binary_bb(start_nodes_list: list, instances: dict, weights: dict):
    global SOL
    SOL = build_start_solution(weights)
    partition = build_partition(start_nodes_list)
    recursive_bb(start_nodes_list, partition, instances, weights, 0, True)
    recursive_bb(start_nodes_list, partition, instances, weights, 0, False)

    return SOL
