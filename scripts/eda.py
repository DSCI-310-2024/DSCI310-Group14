import click
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Following after the cleaning_data.py, 
perform an exploritary Exploratory Data Analysis (EDA) on the training set exported from the cleaning_data.py
"""

@click.command()
@click.option('--data_path', help='path of training set data (csv) to read', type=str)
@click.option('--output_path', help='path to save the EDA figure, need to end with .png', type=str)

def main(data_path, output_path):

    #load data
    data = pd.read_csv(data_path)
    
    #define columns to plot
    toprow = ['Access to electricity (% of population)', 'CO2 emissions (kt)', 'Population, total', 'Renewable energy consumption (% of total final energy consumption)']
    bottomrow = ['Land area (sq. km)', 'Death rate, crude (per 1,000 people)', 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)', 'Adjusted net national income (constant 2015 US$)']
    
    #combine all columns for x-axis in a single list
    x_columns = toprow + bottomrow
    
    #specify the common y-axis column for all plots
    y_column = 'Renewable electricity output (% of total electricity output)'
    
    #scatter plots
    fig = create_scatter_plots(data, x_columns, y_column, nrows=2, ncols=4)
    
    #save the fig
    plt.savefig(output_path)
    print('EDA figure saved')

def create_scatter_plots(data, x_columns, y_column, nrows, ncols, figsize=(32, 17)):
    """
    Create scatter plots for given columns against a common y-column.

    Parameters:
    - data (DataFrame): The data to plot.
    - x_columns (list): A list of column names for the x-axis.
    - y_column (str): The column name for the y-axis.
    - nrows (int): Number of rows in the subplot grid.
    - ncols (int): Number of columns in the subplot grid.
    - figsize (tuple): Figure size.

    Returns:
    - matplotlib.figure.Figure: The created figure.
    """
    if data.empty or not set(x_columns + [y_column]).issubset(data.columns) or data[x_columns + [y_column]].dropna().empty:
        raise ValueError("DataFrame is empty or specified columns contain no data")
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    axes = axes.flatten()  # Flatten in case of single row/column to simplify indexing
    for i, x_col in enumerate(x_columns[:nrows*ncols]):  # Ensure we do not exceed subplot count
        if x_col in data and y_column in data:
            data.plot.scatter(x=x_col, y=y_column, ax=axes[i])
        else:
            raise ValueError(f"Column {x_col} or {y_column} does not exist in DataFrame")
    plt.subplots_adjust(wspace=0.2, hspace=0.15)
    return fig

if __name__ == '__main__':
    main()