from launchpad import launchpad


class Main(object):

    def __init__(self):

        self.launchpad_latitude = launchpad.latitude
        self.launchpad_longitude = launchpad.longitude
        self.launchpad_coordinates = launchpad.coordinates
        self.launchpad_azimuth = launchpad.azimuth
        self.launchpad_elevation = launchpad.elevation
        self.launchpad_launch_vector = launchpad.launch_vector
