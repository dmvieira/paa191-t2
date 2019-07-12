import pybnb
from paa191t2.branch_and_bound.binary import solve_formula, build_partition, get_bound
from paa191t2.branch_and_bound.loader import Loader

loader = Loader()

problem_set = loader.parse_from_file("nl01-51.txt")


class Experiment(pybnb.Problem):
    def __init__(self, problem_set):
        self.bounds = [0.0, 1000.0]
        self.instances = problem_set.instances
        self.weights = problem_set.weights
        self.partition = build_partition(list(range(1, problem_set.n + 1)))
        self.stash = [(1, False), (1, True)]
        self.node = 1
        self.last_node = problem_set.n + 1
        self.solution = 0

    def sense(self):
        return pybnb.maximize

    def objective(self):
        if self.node == self.last_node:
            self.solution = solve_formula(self.instances, self.partition, self.weights)
        return self.solution

    def bound(self):
        self._bound = get_bound(self.instances, self.partition, self.weights)
        return self._bound

    def save_state(self, node):
        node.state = self.partition

    def load_state(self, node):
        self.partition = node.state

    def branch(self):
        if (self._bound > self.solution) and (self.last_node > self.node + 1):
            self.stash.append([self.node + 1, False])
            self.stash.append([self.node + 1, True])
        self.node, self.value = self.stash.pop()
        self.partition[str(self.node)] = self.value
        node = pybnb.Node()
        node.state = self.partition
        yield node


problem = Experiment(problem_set)
results = pybnb.solve(problem,
                      relative_gap=1e-4)
print(results)
