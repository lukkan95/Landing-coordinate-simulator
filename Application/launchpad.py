from math import *


class Launchpad(object):

    latitude = 54.568481
    longitude = 16.758939
    coordinates = [latitude, longitude, 0.0]
    azimuth = 310  # degrees
    elevation = 85  # degrees
    launch_vector = [i * 5 for i in [0, 0, sin(radians(azimuth)), cos(radians(azimuth))]]


launchpad = Launchpad()