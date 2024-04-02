
import os
import pytest
import tempfile
import pandas as pd
import numpy as np
from click.testing import CliRunner
import matplotlib.pyplot as plt
from scripts.eda import main
from scripts.eda import create_scatter_plots

#test create_scatter_plots
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6],
    'D': [6, 5, 4, 3, 2]
})
x_columns = ['A', 'B', 'C']
y_column = 'D'

def test_return_type():
    """Test that the function returns a matplotlib fig"""
    fig = create_scatter_plots(data, x_columns, y_column, 1, 3)
    assert isinstance(fig, plt.Figure)

def test_subplot_count():
    """Test that the function creates the correct number of subplots"""
    nrows, ncols = 1, 3
    fig = create_scatter_plots(data, x_columns, y_column, nrows, ncols)
    assert len(fig.axes) == nrows * ncols

def test_subplot_count_mismatch():
    """Test handling when x_columns are more than subplots"""
    nrows, ncols = 1, 2  # Less than length of x_columns
    fig = create_scatter_plots(data, x_columns, y_column, nrows, ncols)
    # Function should only create 2 subplots, even though there are 3 x_columns
    assert len(fig.axes) == nrows * ncols

def test_empty_data():
    """Test function with empty DataFrame to see if it handles it gracefully."""
    empty_data = pd.DataFrame()
    with pytest.raises(ValueError):
        create_scatter_plots(empty_data, x_columns, y_column, 1, 3)
