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
    data1 = pd.read_csv(data_path)
    fig, axes = plt.subplots(nrows=2, ncols=4,figsize=(32, 17))
    toprow= ['Access to electricity (% of population)', 'CO2 emissions (kt)', 'Population, total', 'Renewable energy consumption (% of total final energy consumption)']
    bottomrow= ['Land area (sq. km)', 'Death rate, crude (per 1,000 people)', 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)', 'Adjusted net national income (constant 2015 US$)']
    c=-1
    for i in range(len(toprow)): 
        data1.plot.scatter(x=toprow[i], y='Renewable electricity output (% of total electricity output)', ax=axes[0,c+1])
        c=c+1
    c=-1
    for i in range(len(bottomrow)): 
        data1.plot.scatter(x=bottomrow[i], y='Renewable electricity output (% of total electricity output)', ax=axes[1,c+1])
        c=c+1
    plt.subplots_adjust(wspace=0.2, hspace=0.15)
    plt.savefig(output_path)
    return print('EDA figure saved')

if __name__ == '__main__':
    main()