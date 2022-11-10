import pygame as p

from .config import RESOLUTION, SQUARES, SAMPLING
from . import gencircle, genpoly


def map_gen(n, L) -> list[list[bool]]:
    if n == 'o':
        points = gencircle.gen_points(L)
    else:
        points = genpoly.gen_points(n, L)
    points = tuple(([point[0]*SAMPLING, point[1]*SAMPLING])
                   for point in points)
    map = [[None for _ in range(SQUARES)] for _ in range(SQUARES)]
    half_squares = SQUARES/2
    sample_res = SAMPLING*RESOLUTION
    for i in range(SQUARES):
        for j in range(SQUARES):
            square = p.Rect(
                (i-half_squares)*sample_res, (j-half_squares)*sample_res,
                sample_res, sample_res,
            )
            for point in points:
                map[i][j] = map[i][j] or square.collidepoint(point)
    return map
