from queue import LifoQueue
from . import Problem

def branch_and_bound(expression):
    problem = Problem(expression)
    print('INITIAL PROBLEM', problem)
    i = 0
    while problem.has_subproblem():
        i += 1
        sub_problem = problem.next_subproblem()
        if sub_problem.leaf:   
            if problem.check_solution(sub_problem):
                print('BEST', sub_problem)
                break
        
        if problem.check_bound(sub_problem):      
            problem.branch(sub_problem)
            print('INTERMEDIATE PROBLEM', problem)
    print('FINAL PROBLEM', problem, 'Iterations', i)