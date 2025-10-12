import pytest
import numpy as np
from plotly.io import to_json
from nullval import (
    polynomial_interpolation,
)  # import polynomial_interpolation, plot_polynomial_interpolation
from nullval.polynomial_interpolation import plot_polynomial_interpolation


def test_polynomial_interpolation_simple():
    """
    Test polynomial interpolation with a simple dataset.
    """
    x = np.array([1.0, 2.0, 3.0, 4.0])
    y = np.array([1.0, 4.0, 9.0, 16.0])
    degree = 2
    x_new = np.linspace(min(x), max(x), 100)
    y_new = polynomial_interpolation(x, y, degree, x_new)

    # Verify the length of the output and ensure values are finite
    assert len(y_new) == pytest.approx(len(x_new))
    assert np.all(np.isfinite(y_new))


def test_polynomial_interpolation_high_degree():
    """
    Test polynomial interpolation with a high degree polynomial.
    """
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y = np.array([1.0, 8.0, 27.0, 64.0, 125.0])
    degree = 4
    x_new = np.linspace(min(x), max(x), 100)
    y_new = polynomial_interpolation(x, y, degree, x_new)

    # Verify the length of the output and ensure values are finite
    assert len(y_new) == len(x_new)
    assert np.isfinite(y_new).all()


def test_polynomial_interpolation_mismatched_lengths():
    """
    Test that the function raises a TypeError when x and y lengths do not match.
    """
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([1.0, 4.0])
    degree = 2
    x_new = np.linspace(min(x), max(x), 100)
    with pytest.raises(TypeError):
        polynomial_interpolation(x, y, degree, x_new)


"""
def test_plot_polynomial_interpolation_runs():
    
    Test that the plot_polynomial_interpolation function runs without errors.

    x = np.array([1.0, 2.0, 3.0, 4.0])
    y = np.array([1.0, 4.0, 9.0, 16.0])
    degree = 2
    x_new = np.linspace(min(x), max(x), 100)
    
    # Instead of showing the plot, convert it to JSON to ensure the function runs without errors
    fig = plot_polynomial_interpolation(x, y, degree, x_new)
    fig_json = to_json(fig)
    assert fig_json is not None


"""
