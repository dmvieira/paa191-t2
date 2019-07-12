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
    print(problem_set)
    print('---'*10)
    expression = build_smart_instance(problem_set)
    problem = branch_and_bound(expression)
    print('<<<< Problem solved ', problem_set.best_sum == problem.solution, ' >>>>')
    print('<<<< Solution Found ', list(filter(lambda v: v[1], problem.solution_assignment.items())),' >>>>>')


if __name__ == "__main__":
    loader = Loader()
    problem_set = loader.parse_from_file("nl01-40.txt")
    smart(problem_set)