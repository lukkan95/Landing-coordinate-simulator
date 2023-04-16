from geo2ecef import *
from numpy import *

def enu2ecef2(V_enu, R_geo):
    R_ecef = geo2ecef(R_geo)
    phi = radians(R_geo[0])
    lambda_ = radians(R_geo[1])

    M = array([
        [-sin(lambda_), -sin(phi)*cos(lambda_), cos(phi)*cos(lambda_)],
        [cos(lambda_), -sin(phi) * sin(lambda_), cos(phi)*sin(lambda_)],
        [0, cos(phi), sin(phi)]

    ])

    V_ecef = M.dot([V_enu[0], V_enu[1], V_enu[2]])