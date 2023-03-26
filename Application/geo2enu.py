from numpy import *
from geo2ecef import *

def geo2enu(geo_coordinates_transformed, geo_coordinates_base):

    ecef_coordinates_transformed = geo2ecef(geo_coordinates_transformed)
    ecef_coordinates_base = geo2ecef(geo_coordinates_base)

    substracted = []
    for item1, item2 in zip(ecef_coordinates_transformed, ecef_coordinates_base):
        substracted.append(item1-item2)

    R_geo = geo_coordinates_base
    phi = radians(R_geo[0])
    lambda_ = radians(R_geo[1])

    M = array([
                    [-sin(lambda_), cos(lambda_), 0.0],
                    [-sin(phi) * cos(lambda_), -sin(phi) * sin(lambda_), cos(phi)],
                    [cos(phi) * cos(lambda_),  cos(phi) * sin(lambda_), sin(phi)]

    ])

    substracted_matrix = array([
        [substracted[0], substracted[1], substracted[2]]

    ])
    # print(substracted_matrix.shape, M.shape)
    # print(substracted_matrix)
    enu_coordinates = dot(substracted_matrix, M)
    # print(f'GEO2ENU - enu_coordinates:{enu_coordinates}')
    return enu_coordinates

