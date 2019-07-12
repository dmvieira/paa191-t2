import almetro
from almetro.instance import generator
from almetro.complexity import Complexity
from paa191t2.branch_and_bound.loader import Loader

loader = Loader()

def load_instances():
    instances = [map(lambda i: f'nl01-{40+i}', range(12))]    
    for instance in instances:
        problem_set = loader.parse_from_file(f'{instance}.txt')
        yield {
            'name': f'{instance} (2^(n={problem_set.n}))',
            'size': {'n': problem_set.n, 'm': problem_set.m},
            'value': {
                'graph': Graph(G),
                'source_node': 1,
                'distance_struct': distance_struct
            }
        }

def generate_instances():
