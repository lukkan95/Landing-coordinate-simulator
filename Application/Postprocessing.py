import os.path
import re
# from os import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
simulation_batches_number = 4
start_number = 1
sim_number = 97

result = []


i = 0
for j in range(1, simulation_batches_number+1):
    batch_folder_name = f'{ROOT_DIR}\simulations_{j}'
    path = os.listdir(batch_folder_name)
    for filename in sorted(map(lambda x: re.split('sim|_', x)[1], path), key=int):
        with open(f'{ROOT_DIR}\simulations_{j}\sim{filename}_2_summary', 'r') as f:
            head = next(f.read() for _ in range(9))
            head_splitted = re.split('\n', head)
            head_splitted.insert(0, f'simulations_{j}\sim{filename}_2_summary')
            result.append(head_splitted)
            i+=1

# print(*result, sep='\n')
print(i)

def create_impact_points(result):
    impact_points = []
    for x in result:
        temp_list = [re.split(': ', x[2])[1], re.split(': ', x[3])[1], 0]
        impact_points.append(temp_list)
    return impact_points

print(*create_impact_points(result), sep='\n')

