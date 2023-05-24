from launchpad import launchpad
from coordinates_from_csv import *
from geo2enu import *
from Postprocessing import Postprocessing
from GUI_Window import *


class Main(object):

    def __init__(self):
        self.launchpad_initialization()
        self.coordinates_initialization()
        self.range_limits_enu = self.coordinateArray2enu(range_limits, launchpad.coordinates)
        self.smaller_range_limits_enu = self.coordinateArray2enu(smaller_range_limits, launchpad.coordinates)
        self.range_shore_enu = self.coordinateArray2enu(range_shore, launchpad.coordinates)
        self.range_sea_limits_enu = self.coordinateArray2enu(range_sea_limits, launchpad.coordinates)


    def launchpad_initialization(self):
        self.launchpad_latitude = launchpad.latitude
        self.launchpad_longitude = launchpad.longitude
        self.launchpad_coordinates = launchpad.coordinates
        self.launchpad_azimuth = launchpad.azimuth
        self.launchpad_elevation = launchpad.elevation
        self.launchpad_launch_vector = launchpad.launch_vector

    def coordinates_initialization(self):
        self.range_limits = range_limits
        self.smaller_range_limits = smaller_range_limits
        self.range_shore = range_shore
        self.range_sea_limits = range_sea_limits

    def coordinateArray2enu(self, coordinateArray, referenceCordinates):
        enuArray_list = []
        for i in range(len(coordinateArray)):
            enuArray = geo2enu(coordinateArray[i], referenceCordinates)
            enuArray_list.append(enuArray)
        return enuArray_list


if __name__ == '__main__':

    main = Main()
    postprocessing = Postprocessing()
    window1 = Figure1()
    window1.column_graph(main, postprocessing)
    window2 = Figure2()
    window2.column_graph(postprocessing)
