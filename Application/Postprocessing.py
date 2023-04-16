import os.path
import re
from launchpad import *
from enu2geo import *


class Postprocessing(object):

    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.simulation_batches_number = 4
        self.start_number = 1
        self.sim_number = 97



    def making_result(self):
        result = []
        i = 0
        for j in range(1, self.simulation_batches_number+1):
            batch_folder_name = f'{self.ROOT_DIR}\simulations_{j}'
            path = os.listdir(batch_folder_name)
            for filename in sorted(map(lambda x: re.split('sim|_', x)[1], path), key=int):
                with open(f'{self.ROOT_DIR}\simulations_{j}\sim{filename}_2_summary', 'r') as f:
                    head = next(f.read() for _ in range(9))
                    head_splitted = re.split('\n', head)
                    head_splitted.insert(0, f'simulations_{j}\sim{filename}_2_summary')
                    result.append(head_splitted)
                    i += 1
        return result



    def create_impact_points(self, result):
        impact_points = []
        for x in result:
            temp_list = [float(re.split(': ', x[2])[1]), float(re.split(': ', x[3])[1]), 0]
            impact_points.append(temp_list)
        return impact_points




    def create_impact_points_coordinates(self, arg):
        impact_points_coordinates = []
        for x in arg:
            temp = enu2geo(x, launchpad.coordinates)
            impact_points_coordinates.append(temp)
        for elem in impact_points_coordinates:
            elem[2] = 0
        return impact_points_coordinates

    def final_impact_points_coordinates(self):
        impact_points_coordinates = self.create_impact_points_coordinates(self.create_impact_points(
            self.making_result()))
        return impact_points_coordinates


# if __name__ == '__main__':
#   postprocessing = Postprocessing()
#   print(*postprocessing.final_impact_points(), sep='\n')
