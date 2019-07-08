import uuid
import math
import networkx as nx


def partition_bb(graph: nx.DiGraph, node, parent_node):
    """Particiona por 0 e 1 e retorna grafo com todos os nós
    com valores para zero e um (seguindo ou não o ramo da árvore)
    """
    node_name_true = uuid.uuid4()
    node_name_false = uuid.uuid4()
    graph.add_node(node_name_true, name=node, value=None)
    graph.add_node(node_name_false, name=node, value=None)

    graph.add_edge(parent_node, node_name_false, status=0)
    graph.add_edge(parent_node, node_name_true, status=1)

    return graph, [node_name_true, node_name_false]


def next_node_value(graph: nx.DiGraph, node, weights):
    """Calcula valor do próximo nó percorrendo como DFS a árvore e retornando o valor
    """
    parent = next(graph.predecessors(node))
    edge = graph.get_edge_data(parent, node)
    if edge["status"] == 0:
        graph.node[node]["value"] = graph.node[parent]["value"]
    else:
        graph.node[node]["value"] = graph.node[parent]["value"] + weights[str(graph.node[node]["name"])]

    return graph


def get_start_bound(weights):
    """Retorna valor de uma solução viável inicial.
    Ela pode ser a soma de todos os números negativos
    """
    lower_sum = 0
    for weight in weights.values():
        if weight < 0:
            lower_sum += weight
    return lower_sum


def select_partition(graph: nx.DiGraph, parent):
    """Escolher melhor partição a se usar como novo bound
    """
    bound = math.inf * -1
    selected_node = None
    for node in graph.successors(parent):
        if graph.node[node]["value"] > bound:
            bound = graph.node[node]["value"]
            selected_node = node
    return bound, selected_node


def get_next_node(graph: nx.DiGraph, parent_node, visited, start_nodes_list):
    for node in graph.successors(parent_node):
        if node not in visited:
            visited.append(node)
            yield node, visited
    for node in start_nodes_list:
        if node not in visited:
            visited.append(node)
            yield node, visited
    raise StopIteration()


def remove_graph_lower_bound(graph: nx.DiGraph, parent, bound):
    for node in graph.successors(parent):
        if graph.node[node]["value"] is not None and graph.node[node]["value"] < bound:
            graph.remove_node(node)
    return graph


def binary_bb(start_nodes_list: list, graph: nx.DiGraph, weights: dict):
    bound = get_start_bound(weights)
    execution_graph = nx.DiGraph()
    parent_node = uuid.uuid4()
    start_node = start_nodes_list[0]
    execution_graph.add_node(parent_node, name=0, value=bound)
    graph.add_node(parent_node)
    graph.add_edge(parent_node, start_node)
    visited = [parent_node]
    selected_nodes = []
    for node, visited in get_next_node(graph, parent_node, visited, start_nodes_list):
        execution_graph, nodes = partition_bb(execution_graph, node, parent_node)
        execution_graph = next_node_value(execution_graph, nodes[0], weights)
        execution_graph = next_node_value(execution_graph, nodes[1], weights)
        bound, parent_node = select_partition(execution_graph, parent_node)
        selected_nodes.append(parent_node)
        execution_graph = remove_graph_lower_bound(execution_graph, parent_node, bound)
    return execution_graph, selected_nodes, bound
