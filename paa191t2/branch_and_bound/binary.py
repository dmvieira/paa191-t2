import uuid
import math
import networkx as nx


def partition_bb(to_fix, partition):
    """Particiona por 0 e 1 e retorna grafo com todos os nós
    com valores para zero e um (seguindo ou não o ramo da árvore)
    """
    partition[to_fix] = False

    return partition

def get_bound(instances: dict, partition: dict, weights: dict):
    """Retorna valor de upper bound de relaxação"""
    bound = 0

    for instance in instances:
        if weights[instance] > 0:
            bound += weights[instance]
            for element in instances[instance]:
                if not partition[element]:
                    bound -= weights[instance]
                    break
    return bound

def solve_formula(instances: dict, partition: dict, weights: dict):
    """Retorna valor da solução final"""
    result = 0
    for instance in instances:
        result += weights[instance]
        for element in instances[instance]:
            if not partition[element]:
                result -= weights[instance]
                break
    return result

def build_partition(n):
    return {str(i):True for i in range(1, n+1)}

def binary_bb(
    start_nodes_list: list,
    instances: dict,
    weights: dict,
    node_index: int = 0,
    partition: dict = None,
    start_index: int = 0,
    last_bound = 0):
    
    if (node_index == len(start_nodes_list)) or (
        (start_index == len(start_nodes_list)) and (node_index == len(start_nodes_list))
        ):
        return solve_formula(instances, partition, weights)
    
    if not partition:
        partition = build_partition(len(start_nodes_list))

    partition[node_index] = False
    bound = get_bound(instances, partition, weights)
    print(start_index, sum(partition.values()), len(partition))
    if last_bound > bound:
        return last_bound

    for node in range(start_index, len(start_nodes_list)):
        bound = binary_bb(start_nodes_list, instances, weights, node_index+1, partition, start_index, bound)
    
    start_index += 1
    partition = build_partition(len(start_nodes_list))
    for n in range(start_index):
        partition[n] = False
    return binary_bb(start_nodes_list, instances, weights, 0, partition, start_index, bound)