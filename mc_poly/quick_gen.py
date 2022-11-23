from math import pi, cos, sin

from .vector import Vector
from .config import SQUARES
from .incircle import incircle


def get_block_map(mode: int, squares: int):
    origo = Vector((0.5, 0.5))
    if mode == 0:
        origo = origo * 0
    offset_vector = Vector((squares/2, squares/2)) - origo
    block_map = [[Vector((i, j)) - offset_vector for i in range(squares)]
                 for j in range(squares)]

    return block_map


def get_reference_points(n: int, L: int or float):
    distance = 2 * incircle(n, L) + 0.05
    reference_points = []
    for i in range(n):
        angle = 2*pi * (i+n)/n
        angle += pi/2
        x = cos(angle) * distance
        y = sin(angle) * distance
        reference_points.append(Vector((x, y)))
    return reference_points


def generate_polygon(n, L):
    block_map = get_block_map(1-L % 2, SQUARES)
    reference_points = get_reference_points(n, L)
    for i, row in enumerate(block_map):
        for j, block in enumerate(row):
            covered = True
            for point in reference_points:
                if Vector.norm(block) > Vector.distance_between(block, point):
                    covered = False
            block_map[i][j] = covered
    return block_map


def generate_circle(d: int or float):
    block_map = get_block_map(d % 2, SQUARES)
    for i, row in enumerate(block_map):
        for j, block in enumerate(row):
            block_map[i][j] = Vector.norm(block) < 0.05+d/2
    return block_map


def map_gen(n, L) -> list[list[bool]]:
    if n in ('o',):
        return generate_circle(L)
    else:
        return generate_polygon(n, L+1)
