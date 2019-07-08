import networkx as nx
from paa191t2.branch_and_bound.binary import binary_bb
from paa191t2.branch_and_bound.loader import Loader

loader = Loader()

problem_set = loader.parse_from_file("nl01-40.txt")
graph = nx.parse_edgelist(problem_set.edges, create_using=nx.DiGraph(), nodetype=int)
graph.remove_edges_from(graph.selfloop_edges())

execution_graph, selected_nodes, bound = binary_bb(list(range(1, problem_set.n + 1)), graph, problem_set.weights)

print([execution_graph.node[node]["name"] for node in selected_nodes], bound)
