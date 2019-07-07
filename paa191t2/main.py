import matplotlib.pyplot as plt
import networkx as nx
from paa191t2.branch_and_bound.binary import binary_bb

with open("paa191t2/resources/nl01-40.txt") as instances:
    n, m, best = instances.readline().strip().replace("/n", "").split()
    best_indexes = instances.readline().strip().replace("/n", "").split()[1:]

    edges = []
    weights = dict()

    for raw_line in instances.readlines():
        line = raw_line.strip().replace("/n", "").split()
        ident = line[0]
        c = line[1]
        ids = line[3:] + [ident]
        for i in range(0, len(ids)-1):
            edges.append(" ".join([ids[i], ids[i+1]]))
        weights[ident] = c
    
    graph = nx.parse_edgelist(edges, create_using=nx.DiGraph())
    graph.remove_edges_from(graph.selfloop_edges())

    binary_bb(graph, weights)
    # nx.draw(graph)
    # plt.savefig("test_full.png")