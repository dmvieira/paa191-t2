from paa191t2.branch_and_bound.binary import binary_bb
from paa191t2.branch_and_bound.loader import Loader
from paa191t2.smart_branch_and_bound import mock_smart_instance, build_smart_instance
from paa191t2.smart_branch_and_bound.iterative import branch_and_bound


def recursive(problem_set):
    result = binary_bb(
        list(range(1, problem_set.n + 1)),
        problem_set.instances,
        problem_set.weights
    )
    print(result)


def smart(problem_set):
    expression = build_smart_instance(problem_set)
    problem = branch_and_bound(expression, problem_set.best_sum)
    print('<<<< Problem solved ', problem_set.best_sum == problem.solution,  ' >>>>')


def instrumented_smart(instance=None):
    expression = build_smart_instance(instance)
    branch_and_bound(expression)


if __name__ == "__main__":
    loader = Loader()
    problem_set = loader.parse_from_file("nl01-43.txt")
    smart(problem_set)
