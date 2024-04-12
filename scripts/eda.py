import click
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.create_scatter_plots import create_scatter_plots
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

if __name__ == '__main__':
    main()
