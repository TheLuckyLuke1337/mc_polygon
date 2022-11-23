import pygame as p

from .config import RESOLUTION, SQUARES, SAMPLING
from . import gencircle, genpoly
from .quick_gen import generate_circle, generate_polygon


def map_gen(n, L) -> list[list[bool]]:
    if n in ('o',):
        return generate_circle(L)
    else:
        return generate_polygon(n, L+1)
