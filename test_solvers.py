from dsl import *
import numpy as np

def test_affine():
    x = np.random.random(10)
    a = np.random.rand()
    b = np.random.rand()
    y = a * x + b

    coeffs = linear_coeffs(x, y)
    a = first(coeffs)
    b = last(coeffs)
    O = add(multiply(a, x), b)

    assert(np.allclose(O, y))
