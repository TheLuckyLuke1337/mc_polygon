from numpy import pi, cos, sin, round

from .circumcircle import circumcircle

from .config import RESOLUTION, SAMPLING


def gen_points(n, L):
    sample_res = RESOLUTION/SAMPLING
    half_res = RESOLUTION/2
    radius = circumcircle(n, L)
    points = []
    alpha = -pi/4+pi/(2*n)
    x = round(cos(alpha) * radius) * RESOLUTION
    y = round(sin(alpha) * radius) * RESOLUTION
    print(f"{x = }   {y = }")
    for i in range(n):
        angle = 2*pi*i / n
        for _ in range(L*SAMPLING):
            y += cos(angle) * sample_res
            x += -sin(angle) * sample_res
            points.append((x + half_res, y + half_res))
    return points
