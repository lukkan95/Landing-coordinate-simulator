from math import *


class Launchpad(object):

    latitude = 54.566681
    longitude = 16.742101
    coordinates = [latitude, longitude, 0.0]
    azimuth = 300  # degrees
    elevation = 85  # degrees
    launch_vector = [i * 5 for i in [0, 0, sin(radians(azimuth)), cos(radians(azimuth))]]


launchpad = Launchpad()