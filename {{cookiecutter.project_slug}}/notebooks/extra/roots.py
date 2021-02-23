"""
Return the roots of the second degree polynom
"""
import numpy as np


def roots_second_degree(a, b, c):
    r"""
    Return the roots of a second degree polynom

    Returns the two roots of a second degree polynom given by

    .. math:

        p(x) = a x^2 + b x + c

    Parameters
    ----------
    a, b, c: floats
        Coefficients of the polynom

    Returns
    -------
    root_1, root_2: complex
        Roots of the polynom
    """
    discriminant = b ** 2 - 4 * a * c
    root_1 = 0.5 / a * (-b + np.sqrt(complex(discriminant)))
    root_2 = 0.5 / a * (-b - np.sqrt(complex(discriminant)))
    return root_1, root_2
