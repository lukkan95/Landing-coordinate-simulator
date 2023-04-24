import os.path
from launchpad import *
from enu2geo import *
from geo2enu import *
from flat_rotation import *
from get_summary import *

class Postprocessing(object):

    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.simulation_batches_number = 1
        self.start_number = 1
        self.sim_number = 50
        self.rocket_folder_name = "case18_rocket"
        self.parachutes_folder_name = "case19_parachute"
        self.results = []
        self.impact_points = []
        self.impact_points_coordinates = []
        self.parachute_case_letters = ['B', 'C']
        self.number_of_result_series = 1 + len(self.parachute_case_letters)


    def making_result_new(self):
        z = get_summary(self.rocket_folder_name, '', self.sim_number)
        self.results.append(z)
        for i in range(len(self.parachute_case_letters)):
            y = get_summary(self.parachutes_folder_name, self.parachute_case_letters[i], self.sim_number)
            self.results.append(y)
        return self.results

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

    def geo(self):
        impact_points_coordinates = self.create_impact_points_coordinates(self.create_impact_points(
            self.making_result_new()))
        return impact_points_coordinates

    def enu(self):
        temp_enu_list = []
        impact_points_geo = self.geo()
        for elem in impact_points_geo:
            temp_enu_list.append(geo2enu(elem, launchpad.coordinates))
        # print('im called')
        return temp_enu_list

    def mean(self):
        impact_points_enu = self.enu()
        temp_column_1 = []
        temp_column_2 = []
        for i in impact_points_enu:
            temp_column_1.append(i[0])
            temp_column_2.append(i[1])
        temp_mean = [mean(temp_column_1), mean(temp_column_2)]
        return temp_mean

    def downgrade_line_theta(self):
        temp_mean = self.mean()
        return rad2deg(atan2(temp_mean[0], temp_mean[1]))

    def range(self):
        temp_geo = self.geo()
        temp_enu = self.enu()
        temp_theta = self.downgrade_line_theta()
        temp_range = []
        for i in range(len(temp_geo)):
            temp_range.append(flat_rotation(temp_enu[i][0:1], 360 - temp_theta))
        return temp_range




