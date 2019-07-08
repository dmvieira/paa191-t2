import os
from paa191t2.branch_and_bound.problem_set import ProblemSet


class Loader:
    def __init__(self, resource_folder="paa191t2/resources/"):
        self.resource_folder = resource_folder

    def parse_from_file(self, filename):
        with open(os.path.join(self.resource_folder, filename)) as instances:
            n, m, best = instances.readline().strip().replace("/n", "").split()
            best_indexes = instances.readline().strip().replace("/n", "").split()[1:]

            edges = []
            weights = dict()

            for raw_line in instances.readlines():
                line = raw_line.strip().replace("/n", "").split()
                ident = line[0]
                c = line[1]
                ids = line[3:] + [ident]
                for i in range(0, len(ids) - 1):
                    edges.append(" ".join([ids[i], ids[i + 1]]))
                weights[ident] = float(c)

            return ProblemSet(n, m, best, best_indexes, edges, weights)
