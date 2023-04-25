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

    def create_impact_points(self):
        call_results = self.making_result_new()
        impact_points = []
        for x in call_results:
            temp_list = []
            for y in x:
                temp_list.append([y[1], y[2], 0])
            impact_points.append(temp_list)
        return impact_points


    def create_impact_points_coordinates(self):
        call_impact_points = self.create_impact_points()
        impact_points_coordinates = []
        for x in call_impact_points:
            temp_list = []
            for y in x:
                temp = enu2geo(y, launchpad.coordinates)
                temp_list.append(temp)
            impact_points_coordinates.append(temp_list)
        for i in impact_points_coordinates:
            for elem in i:
                elem[2] = 0
        return impact_points_coordinates

    def geo(self):
        impact_points_coordinates = self.create_impact_points_coordinates()
        return impact_points_coordinates

    def enu(self):
        temp_enu_list = []
        call_impact_points_geo = self.geo()
        for elem in call_impact_points_geo:
            temp_list = []
            for x in elem:
                temp_list.append(geo2enu(x, launchpad.coordinates))
            temp_enu_list.append(temp_list)
        return temp_enu_list

    def mean(self):
        call_impact_points_enu = self.enu()
        temp_mean_summ = []
        for i in call_impact_points_enu:
            temp_column_1 = []
            temp_column_2 = []
            for x in i:
                temp_column_1.append(x[0])
                temp_column_2.append(x[1])
            temp_mean = [mean(temp_column_1), mean(temp_column_2)]
            temp_mean_summ.append(temp_mean)
        return temp_mean_summ

    def downgrade_line_theta(self):
        temp_mean = self.mean()
        temp_theta = []
        for i in temp_mean:
            temp_theta.append(rad2deg(atan2(i[0], i[1])))
        return temp_theta

    def range(self):
        temp_geo = self.geo()
        temp_enu = self.enu()
        temp_theta = self.downgrade_line_theta()
        temp_range = []
        for i in range(len(temp_geo)):
            temp_range.append(flat_rotation(temp_enu[i][0:1], 360 - temp_theta))
        return temp_range




