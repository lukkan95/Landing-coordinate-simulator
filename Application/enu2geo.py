from Application.ecef2geo import ecef2geo
from Application.enu2ecef2 import enu2ecef2


def enu2geo(enu_position, enu_base_geo_coordinates):
    ecef_position = enu2ecef2(enu_position, enu_base_geo_coordinates)
    geo_coordinates = ecef2geo(ecef_position)
    return geo_coordinates