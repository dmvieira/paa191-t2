from queue import LifoQueue
from . import Problem

def branch_and_bound(expression):
    problem = Problem(expression)
    print('INITIAL PROBLEM', problem)
    i = 0
    while problem.has_subproblem() and not problem.ran_enough():
        i += 1
        sub_problem = problem.next_subproblem()
        if sub_problem.leaf:   
            if problem.check_solution(sub_problem):
                print('BEST', sub_problem)
                
        
        if problem.check_bound(sub_problem):      
            problem.branch(sub_problem)
        
        if not problem.has_subproblem():
            print('>>>>>>>> NO SOLUTION FOUND')

    print('FINAL PROBLEM', problem, 'Iterations', i)