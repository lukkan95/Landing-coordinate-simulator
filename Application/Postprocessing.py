import os.path
import re
from launchpad import *
# from os import *
from enu2geo import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
simulation_batches_number = 4
start_number = 1
sim_number = 97



def making_result():
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
    # print(i)
    return result

# print(*result, sep='\n')


def create_impact_points(result):
    impact_points = []
    for x in result:
        temp_list = [float(re.split(': ', x[2])[1]), float(re.split(': ', x[3])[1]), 0]
        impact_points.append(temp_list)
    return impact_points


# print(*create_impact_points(making_result()), sep='\n')


impact_points = create_impact_points(making_result())


def create_impact_points_coordinates(arg):
    impact_points_coordinates = []
    for x in arg:
        temp = enu2geo(x, launchpad.coordinates)
        # temp_list = [re.split(': ', x[2])[1], re.split(': ', x[3])[1], 0]
        impact_points_coordinates.append(temp)
    for elem in impact_points_coordinates:
        elem[2] = 0
    return impact_points_coordinates

print(*create_impact_points_coordinates(impact_points), sep='\n')
