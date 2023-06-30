# from geo2ecef import *
from numpy import *

from Application.geo2ecef import geo2ecef


def enu2ecef2(V_enu, R_geo):
    R_ecef = geo2ecef(R_geo)
    phi = radians(R_geo[0])
    lambda_ = radians(R_geo[1])

    M = array([
        [-sin(lambda_), -sin(phi)*cos(lambda_), cos(phi)*cos(lambda_)],
        [cos(lambda_), -sin(phi) * sin(lambda_), cos(phi)*sin(lambda_)],
        [0, cos(phi), sin(phi)]

    ])
    sum_arrays = [V_enu[0]+R_ecef[0], V_enu[1]+R_ecef[1], V_enu[2]+R_ecef[2]]

    # print(sum_arrays)
    V_ecef = M.dot([V_enu[0], V_enu[1], V_enu[2]]) + [R_ecef[0], R_ecef[1], R_ecef[2]]

    return V_ecef