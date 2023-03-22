from launchpad import launchpad
from coordinates_from_csv import *


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

    def enuArray(self, coordinateArray, referenceCordinates):
        for i in range(len(coordinateArray)):





if __name__ == '__main__':
    main = Main()
    # print(main.range_limits)