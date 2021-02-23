"""
Test function to get roots of second degree polynom
"""
import numpy.testing as npt
from .roots import roots_second_degree


def test_root():
    """
    Test roots_second_degree function against known solutions
    """
    # p(x) = x ** 2
    roots = roots_second_degree(1, 0, 0)
    npt.assert_allclose(roots, 0)
    # p(x) = x ** 2 - 1
    roots = roots_second_degree(1, 0, -1)
    npt.assert_allclose(roots[0], 1)
    npt.assert_allclose(roots[1], -1)
    # p(x) = 2 * x ** 2 - 8 * x - 24 = 2 * (x - 2) ** 2 - 32
    roots = roots_second_degree(2, -8, -24)
    npt.assert_allclose(roots[0], 6)
    npt.assert_allclose(roots[1], -2)
