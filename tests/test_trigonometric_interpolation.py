import pytest
import numpy as np
from plotly.io import to_json
import nullval
from nullval import trigonometric_interpolation

# from trigonometric_interpolation import trigonometric_interpolation, plot_trigonometric_interpolation
"""
def test_trigonometric_interpolation_simple():
    """
    Test trigonometric interpolation with simple known data points.
    """
    N = 1000
    x = np.linspace(0, 2 * np.pi, N)
    y = np.sin(x)
    x_new = np.linspace(0, 2 * np.pi, 1000)
    y_new = trigonometric_interpolation(x, y, x_new)
    mae = np.mean(np.abs(y_new - np.sin(x_new)))
    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert mae <= 0.01, f"Mean Absolute Error {mae} is greater than 0.01"


def test_trigonometric_interpolation_small_data():
    """
    Test trigonometric interpolation with a small number of data points.
    """
    x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    y = np.array([0, 1, 0, -1, 0])
    x_new = np.linspace(0, 2*np.pi, 100)
    y_new = trigonometric_interpolation(x, y, x_new)

    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert np.allclose(y_new, np.sin(x_new), atol=1e-8), "Interpolated values do not match expected values"

def test_trigonometric_interpolation_large_data():
    """
    Test trigonometric interpolation with a large number of data points.
    """
    N = 1000
    x = np.linspace(0, 2*np.pi, N)
    y = np.sin(x)
    x_new = np.linspace(0, 2*np.pi, 100)
    y_new = trigonometric_interpolation(x, y, x_new)

    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert np.allclose(y_new, np.sin(x_new), atol=1e-8), "Interpolated values do not match expected values"

def test_trigonometric_interpolation_missing_data():
    """
    Test trigonometric interpolation with missing data points.
    """
    x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    y = np.array([0, np.nan, 0, -1, 0])
    x_new = np.linspace(0, 2*np.pi, 100)

    with pytest.raises(ValueError):
        trigonometric_interpolation(x, y, x_new)

def test_trigonometric_interpolation_noisy_data():
    """
    Test trigonometric interpolation with noisy data.
    """
    N = 1000
    x = np.linspace(0, 2*np.pi, N)
    y = np.sin(x) + np.random.normal(0, 0.1, N)
    x_new = np.linspace(0, 2*np.pi, 100)
    y_new = trigonometric_interpolation(x, y, x_new)

    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert np.allclose(y_new, np.sin(x_new), atol=1e-2), "Interpolated values do not match expected values"



def test_trigonometric_interpolation_cosine():
    """
    Test trigonometric interpolation with cosine data points.
    """
    x = np.linspace(0, 2 * np.pi, 10)
    y = np.cos(x)
    x_new = np.linspace(0, 2 * np.pi, 100)
    y_new = trigonometric_interpolation(x, y, x_new)
    
    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert np.allclose(y_new, np.cos(x_new), atol=0.1), "Interpolated values do not match expected cosine values"

@pytest.mark.timeout(30)
def test_plot_trigonometric_interpolation_runs():
    """
    Test that the plot_trigonometric_interpolation function runs without errors.
    """
    x_points = np.linspace(0, 2 * np.pi, 10)
    y_points = np.sin(x_points)
    x_new = np.linspace(0, 2 * np.pi, 100)
    y_new = trigonometric_interpolation(x_points, y_points, x_new)
    
    fig = trigonometric_interpolation.plot_trigonometric_interpolation(x_points, y_points, x_new, y_new)
    fig_json = to_json(fig)
    assert fig_json is not None, "Plotly figure JSON is None"









"""
