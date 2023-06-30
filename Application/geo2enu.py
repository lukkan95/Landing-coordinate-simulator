from numpy import *

from Application.geo2ecef import geo2ecef


def geo2enu(geo_coordinates_transformed, geo_coordinates_base):

    ecef_coordinates_transformed = array([
        geo2ecef(geo_coordinates_transformed)
        ])

    ecef_coordinates_base = array([
        geo2ecef(geo_coordinates_base)
        ])

    R_geo = geo_coordinates_base
    phi = radians(R_geo[0])
    lambda_ = radians(R_geo[1])

    M = array([
                    [-sin(lambda_), cos(lambda_), 0.0],
                    [-sin(phi) * cos(lambda_), -sin(phi) * sin(lambda_), cos(phi)],
                    [cos(phi) * cos(lambda_),  cos(phi) * sin(lambda_), sin(phi)]

    ])

    enu_coordinates = M.dot(transpose(ecef_coordinates_transformed) - transpose(ecef_coordinates_base))
    return enu_coordinates

# print(geo2enu([54.515, 16.648, 0.0], [54.567, 16.742, 0]))