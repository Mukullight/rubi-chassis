import pytest
import numpy as np
from plotly.io import to_json
from nullval import spline_interpolation


def test_compute_cubic_spline_multi_simple():
    """
    Test cubic spline interpolation with a simple dataset.
    """
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 1, 4, 1, 0, 1])
    x_new_sets = [np.linspace(0, 5, 100)]
    y_new_sets = spline_interpolation.compute_cubic_spline_multi(x, y, x_new_sets)
    assert len(y_new_sets) == 1
    assert len(y_new_sets[0]) == len(x_new_sets[0])
    assert np.isfinite(y_new_sets[0]).all()


def test_compute_cubic_spline_multi_mismatched_lengths():
    """
    Test that the function raises a ValueError when x and y lengths do not match.
    """
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 1, 4, 1, 0])
    x_new_sets = [np.linspace(0, 5, 100)]
    with pytest.raises(
        ValueError, match="The input arrays x and y must have the same length."
    ):
        spline_interpolation.compute_cubic_spline_multi(x, y, x_new_sets)


def test_compute_cubic_spline_multi_insufficient_points():
    """
    Test that the function raises a ValueError when there are less than 2 data points.
    """
    x = np.array([0])
    y = np.array([0])
    x_new_sets = [np.linspace(0, 5, 100)]
    with pytest.raises(
        ValueError,
        match="At least two data points are required for spline interpolation.",
    ):
        spline_interpolation.compute_cubic_spline_multi(x, y, x_new_sets)


'''
@pytest.mark.timeout(30)
def test_plot_cubic_spline_multi_runs():
    """
    Test that the plot_cubic_spline_multi function runs without errors within 30 seconds.
    """
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 1, 4, 1, 0, 1])
    x_new_sets = [np.linspace(0, 5, 100)]
    y_new_sets = spline_interpolation.compute_cubic_spline_multi(x, y, x_new_sets)
    # Instead of showing the plot, convert it to JSON to ensure the function runs without errors
    fig = spline_interpolation.plot_cubic_spline_multi(x, y, x_new_sets, y_new_sets)
    fig_json = to_json(fig)
    assert fig_json is not None


'''
