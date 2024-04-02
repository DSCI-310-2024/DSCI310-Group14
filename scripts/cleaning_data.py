import click
from io import BytesIO
import pandas as pd
import os
from zipfile import ZipFile
from urllib.request import urlopen
from sklearn.model_selection import train_test_split
import numpy


@click.command()
@click.option('--dataread', help='path to directory where data is located')
@click.option('--dataout', help='Which directory would you like this file to be written to?')
@click.option('--datafile1', help='Name of file to save testing set to')
@click.option('--datafile2', help='Name of file to save training set to')
@click.option('--seed', default= 123,help='To ensure consistent values, what seed to set the analysis to')

def main(dataread,dataout,datafile1, datafile2, seed):
    numpy.random.seed(seed)
    data1 = pd.read_csv(dataread)
    data1=data1.pivot_table(index= 'Country Name', values="2015", columns='Indicator Name')
    data1= data1[['Access to electricity (% of population)', 'Adjusted net national income (constant 2015 US$)', 
             'CO2 emissions (kt)', 'Death rate, crude (per 1,000 people)',
              'Land area (sq. km)', 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)',
                'Population, total','Renewable energy consumption (% of total final energy consumption)',
             'Renewable electricity output (% of total electricity output)']]
    energy_train, energy_test = impute_split(data1, 0, 0.75, seed)
    os.makedirs(dataout, exist_ok=True)  
    energy_test.to_csv(dataout+"/"+datafile1)  
    energy_train.to_csv(dataout+ "/"+datafile2)

def impute_split(data, impute_val, train_size, rand_seed=0):  
    """
    Takes a data frame and creates a a training and testing split, with imputation for NA values

    Parameters:
    - data: The initial dataset (DataFrame) to be tidied
    - impute_value: The value to replace all NA values with within the dataset
    - train_size: A value from 0-1 that represents the % of data to be used in the training split (remainder will be used in testing split)
    - rand_seed: A seed value to be used for randomness, allowing for reproducible results; default value is 0

    Returns:
    train: Imputed, training dataset split
    test: Imputed, testing dataset split
    """

    numpy.random.seed(rand_seed)
    data = data.fillna(impute_val)
    train, test = train_test_split(data, train_size = train_size)
    return train, test

if __name__ == '__main__':
    main()
