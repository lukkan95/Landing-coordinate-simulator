from math import *

def geo2ecef(R_geo):

    latitude = R_geo[0]
    longitude = R_geo[1]
    altitude = R_geo[2]

    a = 6378137
    b = 6356752

    e = sqrt(1-(b/a)**2)
    N = a / sqrt(1 - e**2 * (sin(radians(latitude)))**2)

    R_1 = (N+altitude) * cos(radians(latitude)) * cos(radians(longitude))  #X
    R_2 = (N+altitude) * cos(radians(latitude)) * sin(radians(longitude)) #Y
    R_3 = ((b/a)**2*N+altitude) * sin(radians(latitude)) #Z

    R = [R_1, R_2, R_3]
    return R


# print(geo2ecef([54.515, 16.648, 0.0]))
# print(geo2ecef([54.567, 16.742, 0]))