from nullval import __version__
from nullval import linear_interpolation
import pytest
import numpy as np


def test_version():
    assert __version__ == "0.1.0"


def test_li_int_simple():
    """
    Test to check if the output produced is accurate
    """
    x_points = np.array([0, 1, 2, 3, 4])
    y_points = np.array([0, 1, 4, 9, 16])
    x_new = np.array([0.5, 1.5, 2.5])
    y_expected = np.array([0.5, 2.5, 6.5])
    y_new = linear_interpolation.li_int(x_points, y_points, x_new)
    np.testing.assert_almost_equal(y_new, y_expected, decimal=5)


def test_li_int_complex():
    """
    Test to see if it accepts mathematical functions and produce the values within the range domain(f(x))--> range(f(x))
    """
    x_points = np.linspace(0, 10, 10)
    y_points = np.sin(x_points)
    x_new = np.linspace(0, 10, 50)
    y_new = linear_interpolation.li_int(x_points, y_points, x_new)
    assert len(y_new) == len(x_new)
    assert np.all((y_new >= -1) & (y_new <= 1))


def test_li_int_non_monotonic():
    """
    Checking to see if the function is strictly increasing or decreasing
    """
    x_points = np.array([0, 3, 2, 1])
    y_points = np.array([0, 9, 4, 1])
    x_new = np.array([0.5, 1.5, 2.5])
    with pytest.raises(ValueError, match="x_points must be strictly monotonic"):
        linear_interpolation.li_int(x_points, y_points, x_new)


def test_li_int_mismatched_lengths():
    """
    Checking to see if the array lengths math
    """
    x_points = np.array([0, 1, 2])
    y_points = np.array([0, 1])
    x_new = np.array([0.5, 1.5])
    with pytest.raises(
        ValueError, match="x_points and y_points must have the same length"
    ):
        linear_interpolation.li_int(x_points, y_points, x_new)
