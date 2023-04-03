import os.path
import re
# from os import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
simulation_batches_number = 4
start_number = 1
sim_number = 97

result = []


def sorting_key(arg):
    z = re.split('sim|_', arg[0:5])
    print(z)

for j in range(1, simulation_batches_number+1):
    batch_folder_name = f'{ROOT_DIR}\simulations_{j}'
    path = os.listdir(batch_folder_name)
    # for sim in path:
    #     # f = os.path.join(batch_folder_name, sim)
    # z = path.sort(key=sorting_key)
    # for x in path:
    #     print(re.split('sim|_', x))
    # z = path.sort(key=lambda x: int(re.split('sim|_', x)[1]))
    print(sorted(path, key=sorting_key))
