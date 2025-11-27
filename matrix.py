#Матриця 2×2 і лінійні перетворення
#Добуток типів Matrix2. Операції: детермінант, обернена, добуток.

from dataclasses import dataclass

@dataclass(frozen=True)
class Matrix:
    a11: float
    a12: float
    a21: float
    a22: float

def det(m: Matrix) -> float:
    match m:
        case Matrix(a, b, c, d):
            return a*d - b*c


def inverse(m: Matrix) -> Matrix:
    match m:
        case Matrix(a, b, c, d):
            determinant = a*d - b*c
            if determinant == 0:
                raise ValueError("Matrix is not invertible")
            inv_det = 1 / determinant
            return Matrix(
                d * inv_det,
                -b * inv_det,
                -c * inv_det,
                a * inv_det
            )


def mul_matrix(m1: Matrix, m2: Matrix) -> Matrix:
    match m1, m2:
        case Matrix(a11, a12, a21, a22), Matrix(b11, b12, b21, b22):
            return Matrix(
                a11*b11 + a12*b21,
                a11*b12 + a12*b22,
                a21*b11 + a22*b21,
                a21*b12 + a22*b22
            )

def main_matrix():
    print("=== Matrix test ===")

    m1 = Matrix(1, 2, 3, 4)
    m2 = Matrix(5, 6, 7, 8)

    print("m1 =", m1)
    print("m2 =", m2)

    print("det(m1):", det(m1))
    print("m1 * m2:", mul_matrix(m1, m2))

    try:
        print("Inverse m1:", inverse(m1))
    except ValueError as e:
        print("Inverse error:", e)

if __name__ == "__main__":
    main_matrix()
