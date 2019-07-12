class ProblemSet:
    def __init__(self, n, m, best_sum, best_vertexes, instances, weights):
        self.n = int(n)
        self.m = int(m)
        self.best_sum = float(best_sum)
        self.best_vertexes = best_vertexes
        self.instances = instances
        self.weights = weights

    def __str__(self):
        return f"[n: {self.n}, m: {self.m}]\n\n[best sum: {self.best_sum}]\n\n[best vertexes: {self.best_vertexes}]"
