from launchpad import launchpad
from coordinates_from_csv import *
from geo2enu import *


class Main(object):

    def __init__(self):
        self.launchpad_initialization()
        self.coordinates_initialization()


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
        for i in range(len(coordinateArray)):
            # print(i)
            enuArray = geo2enu(coordinateArray[i], referenceCordinates)
            print(enuArray)




if __name__ == '__main__':
    main = Main()
    z = main.range_limits
    # print(range_limits[0])
    main.coordinateArray2enu(range_limits, launchpad.coordinates)
