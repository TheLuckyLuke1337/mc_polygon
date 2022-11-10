from numpy import sin, pi


def circumcircle(n: int, L: float) -> float:
    return L / (2*sin(pi/n))
