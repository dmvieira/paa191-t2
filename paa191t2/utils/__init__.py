import os
import almetro
from almetro.instance import generator
from almetro.complexity import Complexity
from paa191t2.branch_and_bound.loader import Loader
from paa191t2.smart_branch_and_bound.iterative import smart_bb

loader = Loader(resource_folder='')


def load_instance(instance_name, instance_file, i=0):
    problem_set = loader.parse_from_file(instance_file)
    return {
        'name': f'{instance_name} (2^(n={problem_set.n}))',
        'size': {'n': problem_set.n, 'm': problem_set.m, 'c': i},
        'value': {
            'instance': problem_set
        }
    }


def generate_instances(instance_dir):
    i = 0
    for _file in sorted(filter(lambda p: 'nl01' in p, os.listdir(instance_dir))):
        i += 1
        yield load_instance(_file.replace('.txt', ''),f'{instance_dir}/{_file}', i)


def c2_exp_n(n=1, m=1, c=1):
    return 2**n + c


np_exponential = Complexity(
    theoretical=c2_exp_n,
    experimental=c2_exp_n,
    text='O(2^n)',
    latex=r'$\mathcal{O}(2^n)$'
)

def almetro_np_non_linear_binary(instance_dir, trials=5, instances=10, complexity=None):
    instance_generator = generate_instances(instance_dir)
    return almetro\
        .new()\
        .with_execution(trials=trials, runs=1)\
        .with_instances(instances=instances, provider=generator(instance_generator))\
        .metro(algorithm=smart_bb, complexity=complexity)