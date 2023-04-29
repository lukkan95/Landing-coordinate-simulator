from math import *
from numpy import *


def flat_rotation(vector_in_rotated_frame, angle_of_rotation):
    theta = deg2rad(angle_of_rotation)
    R = array([
        [cos(theta), -sin(theta)],
        [sin(theta), cos(theta)]
    ])
    vector_in_original_frame = transpose(R).dot(transpose(vector_in_rotated_frame))
    return vector_in_original_frame
