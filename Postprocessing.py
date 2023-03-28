import os.path
# from os import *


simulation_batches_number = 4
start_number = 1
sim_number = 97

result = []

for j in range(1, simulation_batches_number+1):
    batch_folder_name = f'simulations_{j}'
    if not os.path.exists(batch_folder_name):
        os.mkdir(batch_folder_name)

    for k in range(1, 2):
        result_file_name = f'sim{k+start_number}_2_summary'
        temp_path = f'..\simulations_{j}'
        with open('123', 'w') as output:
            output.write('hello')

