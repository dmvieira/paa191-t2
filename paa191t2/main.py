import networkx as nx
from paa191t2.branch_and_bound.binary import binary_bb
from paa191t2.branch_and_bound.loader import Loader

loader = Loader()

problem_set = loader.parse_from_file("nl01-40.txt")
result = binary_bb(
    list(range(1, problem_set.n + 1)),
    problem_set.instances,
    problem_set.weights
)

print(result)
