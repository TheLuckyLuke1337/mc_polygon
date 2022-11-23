from math import sqrt

from .circumcircle import circumcircle

# distance between mid point and a linesegment in a circle


def incircle(n: int, L: float) -> float:
    return sqrt(pow(circumcircle(n, L), 2) - pow((L/2), 2))
