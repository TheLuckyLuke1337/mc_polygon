from dataclasses import dataclass

import math


@dataclass(frozen=True)
class Vector():
    components: tuple[int or float]

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError
        return Vector(tuple([e1+e2 for e1, e2 in zip(self.components, other.components)]))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError
        return Vector(tuple([e1-e2 for e1, e2 in zip(self.components, other.components)]))

    # dot multiplication
    def __mul__(self, other):
        if type(other) != Vector:
            return Vector(tuple([e1*other for e1 in self.components]))
        elif len(self.components) != len(other.components):
            raise ValueError
        return Vector(tuple([e1*e2 for e1, e2 in zip(self.components, other.components)]))

    # dot multiplication
    def __rmul__(self, other):
        if type(other) in (float, int):
            return Vector(tuple([e1*other for e1 in self.components]))
        elif len(self.components) != len(other.components):
            raise ValueError
        return Vector(tuple([e1*e2 for e1, e2 in zip(self.components, other.components)]))

    @staticmethod
    def distance_between(v1, v2) -> float:
        return Vector.norm(v1-v2)

    @staticmethod
    def norm(v) -> float:
        sum = 0
        for i in v.components:
            sum += pow(i, 2)
        return math.sqrt(sum)


def main():
    v1 = Vector((0, 1, 2))
    v2 = Vector((3, 4, 5))
    print(Vector.norm(v1))
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)
    print(Vector.distance_between(v1, v2))
    print(v1 * 1)
    print(1 * v2)
    print('2' * v2)


if __name__ == '__main__':
    main()
