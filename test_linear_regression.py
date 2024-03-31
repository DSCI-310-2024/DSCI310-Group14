import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import set_config
from sklearn.metrics import mean_squared_error

from scripts.linear_regression import split_xy_columns, plot_rmse

def test_split_xy_columns():
    # Create a sample dataset
    data = {
        'Feature1': [1, 2, 3],
        'Feature2': [4, 5, 6],
        'Country Name': ['a', 'b', 'c'],
        'Renewable electricity output (% of total electricity output)': [10, 20, 30]
    }
    dataset = pd.DataFrame(data)

    # Call the function to split the dataset
    dataset_x, dataset_y = split_xy_columns(dataset)

    # Check if dataset_x and dataset_y are pandas DataFrames
    assert isinstance(dataset_x, pd.DataFrame), "dataset_x is not a pandas DataFrame"
    assert isinstance(dataset_y, pd.DataFrame), "dataset_y is not a pandas DataFrame"

    # Check if dataset_x contains only features and dataset_y contains only the target column
    expected_columns_x = set(['Feature1', 'Feature2'])
    expected_columns_y = set(['Renewable electricity output (% of total electricity output)'])
    assert set(dataset_x.columns) == expected_columns_x, "dataset_x does not contain the expected features"
    assert 'Country Name' not in dataset_x.columns
    assert set(dataset_y.columns) == expected_columns_y, "dataset_y does not contain the expected target column"

    print("test_split_xy_columns passed successfully!")

def test_main():
    # Create dummy data
    training_data_path = "dummy_training_data.csv"
    test_data_path = "dummy_test_data.csv"
    output_path = "test_output_plot.png"

    # Call the main function
    energy_RMSE, plot = plot_rmse(training_data_path, test_data_path, output_path)

    # Check if RMSE is a number
    assert isinstance(energy_RMSE, (int, float)), "RMSE is not a number"

    # Check if the plot object is created
    assert isinstance(plot, plt.Figure), "Plot is not created successfully"

    # Check if the plot is saved successfully
    saved_plot = plt.imread(output_path)
    assert saved_plot is not None, "Plot is not saved successfully"

    print("test_main passed successfully!")