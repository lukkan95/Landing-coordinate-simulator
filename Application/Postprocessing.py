import os.path
# from os import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
simulation_batches_number = 4
start_number = 1
sim_number = 97

result = []

for j in range(1, simulation_batches_number+1):
    batch_folder_name = f'simulations_{j}'
    # if not os.path.exists(batch_folder_name):
    #     os.mkdir(batch_folder_name)
    # temp_path = f'{ROOT_DIR}\{batch_folder_name}'
    # os.chdir(temp_path)
    for sim in os.listdir(batch_folder_name):
        f = os.path.join(batch_folder_name, sim)
        # with open(temp_path, 'w') as output:
        #     output.write('hello')
        if os.path.isfile(f):
            print(f)
