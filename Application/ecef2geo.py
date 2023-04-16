from numpy import *

def ecef2geo(R_ecef):

    if linalg.norm(R_ecef) == 0:
        R_geo = [0, 0, 0]

    else:
        # --- WGS84 constants
        a = 6378137.0
        f = 1.0 / 298.257223563
        # --- derived constants
        b = a - f * a
        e = sqrt(a**2 - b**2) / a
        clambda = arctan(R_ecef[1] / R_ecef[0])
        p = sqrt(R_ecef[0]**2 + R_ecef[1] ** 2)
        h_old = 0.0
        # first guess with h=0 meters
        theta = arctan(R_ecef[2] / p * (1.0 - e ** 2))
        cs = cos(theta)
        sn = sin(theta)
        N = a ** 2 / sqrt((a * cs) ** 2 + (b * sn) ** 2)
        h = p / cs - N

        while abs(h - h_old) > 1.0e-6:
            h_old = h
            theta = arctan(R_ecef[2] / (p * (1.0 - e ** 2 * N / (N + h))))
            cs = cos(theta)
            sn = sin(theta)
            N = a ** 2 / sqrt((a * cs) ** 2.0 + (b * sn) ** 2)
            h = p / cs - N

        R_geo = [rad2deg(theta), rad2deg(clambda), h]

    return R_geo
