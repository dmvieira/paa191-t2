from queue import LifoQueue
from . import Problem


def branch_and_bound(expression, solution=None):
    problem = Problem(expression)
    print('INITIAL PROBLEM', problem)
    i = 0
    # problem.has_subproblem() : Enquanto existem subproblemas viaveis na pilha de execucao
    # problem.ran_enough() : Termina a execucao do algoritmo em casos extremos (desrespeite o threshold)
    while problem.has_subproblem() and not problem.ran_enough():
        i += 1
        # Pega o ultimo subproblema incluido na pilha
        # O comportamento deste algoritmo e analogo a DFS
        sub_problem = problem.next_subproblem()

        # Caso um caminho completo entre v e u, sendo v raiz da arvore e u a ultima folha avaliada
        if sub_problem.leaf:
            # Verifica se o somotario dos produtos para o conjunto de variaveis satisfaz o criterio de melhor            
            if problem.check_solution(sub_problem):
                # Neste caso, melhor significa qualquer valor para f(x) maior que o ultimo valor valido registrado anteriormente
                print('BEST', sub_problem)
                
                # Esta linha e apenas para demonstracoes
                if solution is not None and problem.solution == solution:
                    break

                print('Intermediate problem', problem)

        # Caso o upper bound seja melhor que a ultima solucao registrada o ramo continuara a ser explorado
        # Internamente este metodo evita que novos subproblemas sejam criados caso o nivel da arvore seja o mais profundo, ou seja uma folha
        if problem.check_bound(sub_problem):
            # Neste caso dois novos subproblemas seram criados, para x=0 e x=1
            # Porem antes de serem colocados na pilha de execucao, o criterio de bound sera aplicado para cada um deles
            # Dessa maneira, evitamos que subproblemas nao solucionaveis sejam colocados na pilha
            problem.branch(sub_problem)

        # Caso todos os subproblemas viaveis tenham sido avaliados, significa que nao fomos capazes de encontrar uma solucao para o problema
        if not problem.has_subproblem():
            print('>>>>>>>> NO SOLUTION FOUND')

    print('FINAL PROBLEM', problem, 'Iterations', i)
    return problem
