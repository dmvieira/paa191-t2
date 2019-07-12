from functools import reduce
from queue import PriorityQueue, LifoQueue
import operator


def product(iterable):
    return reduce(operator.mul, iterable, 1)


def create_a_function(*args, **kwargs):
    def function_template(*args, **kwargs):
        return product(kwargs.values())
    return function_template


class Variables:
    def __init__(self, products):
        min_variables = set()
        max_variables = set()
        all = set()
        target = 0
        priority = {}
        for product in products:
            all.update(product.variables)
            if product.coeficient > 0:
                max_variables.update(product.variables)
                target += product.coeficient
            else:
                min_variables.update(product.variables)
            for v in product.variables:
                if not v in priority:
                    priority[v] = 0
                priority[v] += product.coeficient
        self.priority = list(sorted(priority.items(), key=lambda t: t[0]))
        self.max = max_variables - min_variables
        self.min = min_variables - max_variables
        self.neutral = max_variables & min_variables
        self.all = all
        self.size = len(all)
        self.target = target

    def all_zero(self):
        return {k: 0 for k in self.all}

    def all_one(self):
        return {k: 1 for k in sorted(self.all, key=lambda v: int(v[1:]))}

    def __repr__(self):
        return f'Target:{self.target}\nMax: {self.max}\nMin: {self.min}\nNeutral: {self.neutral}\nAll: {self.all}\n\n'

    def __str__(self):
        return self.__repr__()


class Product:
    def __init__(self, index, coeficient, variables):
        self.index = index
        self.coeficient = coeficient
        self.variables = variables
        self.fn = create_a_function()

    def evaluate(self, assignment):
        values = {var: assignment[var] for var in self.variables}
        values[f'c{self.index}'] = self.coeficient
        return self.fn(**values)

    def __repr__(self):
        return f'c{self.index}({self.coeficient}) * {" * ".join(self.variables)}'

    def __str__(self):
        return self.__repr__()


class Expression:
    def __init__(self, products, variables):
        self.products = products
        self.variables = variables
        self.variables_index = 0

    def evaluate(self, assignment):
        return sum(map(lambda p: p.evaluate(assignment), self.products), 0)

    def bound(self, assignment):
        return sum(map(lambda p: p.evaluate(assignment), filter(lambda p: p.coeficient > 0, self.products)), 0)

    def next_variable(self):
        varr = self.variables.priority[self.variables_index]
        self.variables_index += 1
        if self.variables_index >= len(self.variables.priority):
            self.variables_index = 0
        return varr[0]

    def __repr__(self):
        return str(self.variables) + ' + '.join(map(str, self.products))

    def __str__(self):
        return self.__repr__()


class SubProblem:
    def __init__(self, expression, level, index, assignment, value, leaf):
        self.expression = expression
        self.level = level
        self.index = index
        self.value = value
        self.assignment = assignment.copy()
        self.assignment[index] = value
        self.leaf = leaf

    def bound(self):
        return self.expression.bound(self.assignment)

    def solution(self):
        return self.expression.evaluate(self.assignment)

    def __repr__(self):
        bound_value = self.expression.bound(self.assignment)
        solution_value = self.expression.evaluate(self.assignment)
        return f'[{self.index}] Level: {self.level}, Bound: {bound_value}, Solution: {solution_value}, Assignment: {"".join(map(str, self.assignment.values()))}'

    def __str__(self):
        return self.__repr__()


class Problem:

    def __init__(self, expression):
        initial_assignment = expression.variables.all_one()
        self.solution = 0
        self.solution_assignment = initial_assignment
        self.upper_bound = expression.bound(initial_assignment)
        self.subproblem_count = 0
        self.expression = expression
        self.lifo = LifoQueue()
        self.__expand_sub_problem(1, self.expression.next_variable(), assignment=initial_assignment.copy())

    def has_subproblem(self):
        return not self.lifo.empty()

    def next_subproblem(self):
        return self.lifo.get()

    def check_solution(self, sub_problem):
        partial = sub_problem.solution()
        if partial > self.solution:
            self.solution = partial
            self.solution_assignment = sub_problem.assignment
            return True
        return False

    def check_bound(self, sub_problem):
        return sub_problem.bound() >= self.upper_bound

    def branch(self, sub_problem):
        self.__expand_sub_problem(sub_problem.level + 1, self.expression.next_variable(), sub_problem.assignment.copy())

    def __expand_sub_problem(self, level, index, assignment):
        if level > self.expression.variables.size:
            return
        sub0 = SubProblem(expression=self.expression, level=level, index=index, assignment=assignment.copy(), value=0, leaf=level == self.expression.variables.size)
        if self.check_bound(sub0):
            self.subproblem_count += 1
            self.lifo.put(sub0)
        sub1 = SubProblem(expression=self.expression, level=level, index=index, assignment=assignment.copy(), value=1, leaf=level == self.expression.variables.size)
        if self.check_bound(sub1):
            self.subproblem_count += 1
            self.lifo.put(sub1)

    def __repr__(self):
        return f'Solution: {self.solution, "".join(map(lambda v: str(v[1]), self.solution_assignment.items()))}, UpperBound: {self.upper_bound}, SubProblems: {self.subproblem_count}, Lifo: {self.lifo._qsize()}'

    def __str__(self):
        return self.__repr__()


def build_smart_instance(problem_set):
    products = set()
    for product_index, product_variables in problem_set.instances.items():
        product = Product(product_index, problem_set.weights[product_index], set(map(lambda v: f'x{v}', product_variables)))
        products.add(product)
    return Expression(products, Variables(products))


def mock_smart_instance():
    products = []
    products.append(Product(1, 10, set(['x1'])))
    products.append(Product(2, 20, set(['x1', 'x2'])))
    products.append(Product(3, -40, set(['x2', 'x3'])))
    return Expression(products, Variables(products))
