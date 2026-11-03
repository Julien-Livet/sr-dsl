from sr_types import *
from typing import Tuple
import numpy as np

def linear_coeffs(x: Array, y: Array) -> Tuple[Float, Float]:
    a = np.array([[np.sum(x), len(x)], \
                 [np.sum([xi ** 2 for xi in x]), np.sum(x)]])
    b = np.array([[np.sum(y)], [np.inner(x, y)]])

    coefficients = np.linalg.inv(a) @ b

    return (coefficients[0][0], coefficients[1][0])

def first(tup: Tuple[Float, Float]):
    return tup[0]

def last(tup: Tuple[Float, Float]):
    return tup[-1]

def invert(x: Numerical) -> Numerical:
    return -x

def add(x: Numerical, y: Numerical) -> Numerical:
    return x + y

def subtract(x: Numerical, y: Numerical) -> Numerical:
    return x - y

def multiply(x: Numerical, y: Numerical) -> Numerical:
    return x * y

def divide(x: Numerical, y: Numerical) -> Numerical:
    return x / y

def power(x: Numerical, y: Numerical) -> Numerical:
    return x ** y

def sin(x: Numerical) -> Numerical:
    return np.sin(x)

def cos(x: Numerical) -> Numerical:
    return np.cos(x)

def tan(x: Numerical) -> Numerical:
    return np.tan(x)

def asin(x: Numerical) -> Numerical:
    return np.asin(x)

def acos(x: Numerical) -> Numerical:
    return np.acos(x)

def atan(x: Numerical) -> Numerical:
    return np.atan(x)

def exp(x: Numerical) -> Numerical:
    return np.exp(x)

def log(x: Numerical) -> Numerical:
    return np.log(x)

def sinh(x: Numerical) -> Numerical:
    return np.sinh(x)

def cosh(x: Numerical) -> Numerical:
    return np.cosh(x)

def tanh(x: Numerical) -> Numerical:
    return np.tanh(x)

def asinh(x: Numerical) -> Numerical:
    return np.asinh(x)

def acosh(x: Numerical) -> Numerical:
    return np.acos(x)

def atanh(x: Numerical) -> Numerical:
    return np.atanh(x)
