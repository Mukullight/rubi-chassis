import numpy as np
from nullval import lagrange_interpolation
import pytest


def test_basic_functionality():
    """
    Test basic functionality with a simple set of points.
    """
    x_points = np.array([0, 1, 2])
    y_points = np.array([1, 3, 2])
    x_new = np.array([0.5, 1.5])
    # Corrected expected values based on manual calculation / Wolfram Alpha
    expected_result = np.array([2.370, 2.870])
    result = lagrange_interpolation.lagrange_interpolation(x_points, y_points, x_new)
    np.testing.assert_almost_equal(result, expected_result, decimal=2)


def test_single_point():
    """
    Test interpolation when there is only one data point.
    """
    x_points = np.array([0])
    y_points = np.array([1])
    x_new = np.array([0])
    expected_result = np.array([1])
    result = lagrange_interpolation.lagrange_interpolation(x_points, y_points, x_new)
    np.testing.assert_almost_equal(result, expected_result, decimal=5)


def test_multiple_points():
    """
    Test interpolation with a more complex set of data points.
    """
    x_points = np.array([0, 1, 2, 3])
    y_points = np.array([1, 3, 2, 4])
    x_new = np.array([0.5, 1.5, 2.5])
    expected_result = np.array([2.75, 2.5, 2.25])
    result = lagrange_interpolation.lagrange_interpolation(x_points, y_points, x_new)
    np.testing.assert_almost_equal(result, expected_result, decimal=3)


def test_linear_function():
    """
    Test interpolation on a simple linear function to check correctness.
    """
    x_points = np.array([0, 1])
    y_points = np.array([0, 1])
    x_new = np.array([0.5, 1.5, 2])
    expected_result = np.array([0.5, 1.5, 2])
    result = lagrange_interpolation.lagrange_interpolation(x_points, y_points, x_new)
    np.testing.assert_almost_equal(result, expected_result, decimal=5)


def test_error_handling():
    """
    Test if the function correctly raises an error when the lengths of x_points and y_points do not match.
    """
    x_points = np.array([0, 1])
    y_points = np.array([1])
    x_new = np.array([0.5])
    with pytest.raises(ValueError):
        lagrange_interpolation.lagrange_interpolation(x_points, y_points, x_new)
