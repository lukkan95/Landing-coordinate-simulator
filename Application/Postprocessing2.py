import os.path
import re
# from os import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
simulation_batches_number = 4
start_number = 1
sim_number = 97

result = []


# def sorting_key(arg):
#     z = re.split('sim|_', arg[0:5])
#     print(z)

def sorting_key(arg):
    return arg[0:5]

i = 0
for j in range(1, simulation_batches_number+1):
    batch_folder_name = f'{ROOT_DIR}\simulations_{j}'
    path = os.listdir(batch_folder_name)
    for filename in sorted(map(lambda x: re.split('sim|_', x)[1], path), key=int):
        with open(f'{ROOT_DIR}\simulations_{j}\sim{filename}_2_summary', 'r') as f:
            head = next(f.read() for _ in range(9))
            head_splitted = re.split('\n', head)
            print(head_splitted)
            i+=1

print(i)

