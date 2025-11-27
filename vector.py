#Вектори 3D (Vector3) і базові операції
#Створити ADT для векторів у 3D (через добуток примітивних типів). Реалізувати операції норми, скалярний,
#векторний добуток, змішаний добуток.

from dataclasses import dataclass
from math import sqrt

@dataclass(frozen=True)
class Vector:
    x: float
    y: float
    z: float

def norm(v: Vector) -> float:
    match v:
        case Vector(x, y, z):
             #sqrt(x^2 + y^2 + z^2)
            return sqrt(x*x + y*y + z*z)


def dot(v1: Vector, v2: Vector) -> float:
    match v1, v2:
        case Vector(a1, b1, c1), Vector(a2, b2, c2):
            return a1*a2 + b1*b2 + c1*c2


def cross(v1: Vector, v2: Vector) -> Vector:
    match v1, v2:
        case Vector(a1, b1, c1), Vector(a2, b2, c2):
            return Vector(
                b1*c2 - c1*b2,
                c1*a2 - a1*c2,
                a1*b2 - b1*a2
            )


def triple_product(v1: Vector, v2: Vector, v3: Vector) -> float:
    """Змішаний добуток = dot(v1, cross(v2, v3))"""
    return dot(v1, cross(v2, v3))

def main_vector():
    print("=== Vector3d test ===")

    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(-1, 0, 2)

    print("v1 =", v1)
    print("v2 =", v2)
    print("v3 =", v3)

    print("Norm v1:", norm(v1))
    print("Dot(v1, v2):", dot(v1, v2))
    print("Cross(v1, v2):", cross(v1, v2))
    print("Triple product:", triple_product(v1, v2, v3))

if __name__ == "__main__":
    main_vector()
