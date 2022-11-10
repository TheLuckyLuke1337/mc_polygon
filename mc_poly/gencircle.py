from numpy import pi, cos, sin

from .config import RESOLUTION


def gen_points(r):
    half_res = RESOLUTION/2
    points = []

    for i in range(200):
        angle = 2*pi*i / 200
        y = cos(angle) * RESOLUTION * (r - 0.5)
        x = sin(angle) * RESOLUTION * (r - 0.5)
        points.append((x, y))
    return points
