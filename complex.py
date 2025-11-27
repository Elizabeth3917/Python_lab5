#Комплексні числа (Complex)
#Числа виду (a + b*i) a - реальна частина (float) b - уявна частина (float)
#Створити ADT-тип (через добуток примітивних типів) для комплексних чисел і реалізувати базову арифметику
#(додавання, віднімання, добуток, обчислення спряженого числа, обчислення модуля комплексного числа).

from dataclasses import dataclass
from math import sqrt

@dataclass(frozen=True)
class Complex:
    real: float
    imag: float

def add_complex(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case Complex(a, b), Complex(c, d):
            return Complex(a + c, b + d)


def sub_complex(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case Complex(a, b), Complex(c, d):
            return Complex(a - c, b - d)


def mul_complex(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case Complex(a, b), Complex(c, d):
            # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
            return Complex(a*c - b*d, a*d + b*c)


def conjugate(c: Complex) -> Complex:
    match c:
        case Complex(a, b):
            return Complex(a, -b)


def modulus(c: Complex) -> float:
    match c:
        case Complex(a, b):
            return sqrt(a*a + b*b)

def main_complex():
    print("=== Complex numbers test ===")

    c1 = Complex(2, 3)
    c2 = Complex(1, -4)

    print("c1 =", c1)
    print("c2 =", c2)

    print("Addition:", add_complex(c1, c2))
    print("Subtraction:", sub_complex(c1, c2))
    print("Multiplication:", mul_complex(c1, c2))
    print("Conjugate c1:", conjugate(c1))
    print("Modulus c1:", modulus(c1))

if __name__ == "__main__":
    main_complex()
