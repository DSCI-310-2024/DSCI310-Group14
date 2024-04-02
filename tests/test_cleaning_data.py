import pandas as pd
import numpy as np
import os
import pathlib
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.cleaning_data import clean_data
import pytest
import click

# @click.command()
# @click.option('--dataread', help='path to directory where data is located')
# @click.option('--dataout', help='Which directory would you like this file to be written to?')
# @click.option('--datafile1', help='Name of file to save testing set to')
# @click.option('--datafile2', help='Name of file to save training set to')
# @click.option('--seed', default= 123, help='To ensure consistent values, what seed to set the analysis to')

# Create temporary directories and files

def test_output_files_exist():
   # Check if the output files exist
    clean_data("data/WDIData.csv", "temp", "test_energy_test.csv", "test_energy_train.csv", 310)
    assert os.path.exists(os.path.join(dataout, datafile1))
    assert os.path.exists(os.path.join(dataout, datafile2))

# @click.command()
# @click.option('--dataread', help='path to directory where data is located')
# @click.option('--dataout', help='Which directory would you like this file to be written to?')
# @click.option('--datafile1', help='Name of file to save testing set to')
# @click.option('--datafile2', help='Name of file to save training set to')
# @click.option('--seed', default= 123, help='To ensure consistent values, what seed to set the analysis to')

# def test_output_files_dataframes():
#     # Check if energy_train and energy)test are DataFrames
    
#     dataread = "/data/WDIData.csv"
#     dataout = "temp"
#     datafile1 = "test_energy_test.csv"
#     datafile2 = "test_energy_train.csv"
#     seed = 310
#     main(dataread, dataout, datafile1, datafile2, seed)
#     energy_test = pd.read_csv(os.path.join(dataout, datafile1))
#     energy_train = pd.read_csv(os.path.join(dataout, datafile2))
    
#     assert isinstance(energy_train, pd.DataFrame)
#     assert isinstance(energy_test, pd.DataFrame)

# @click.command()
# @click.option('--dataread', help='path to directory where data is located')
# @click.option('--dataout', help='Which directory would you like this file to be written to?')
# @click.option('--datafile1', help='Name of file to save testing set to')
# @click.option('--datafile2', help='Name of file to save training set to')
# @click.option('--seed', default= 123, help='To ensure consistent values, what seed to set the analysis to')

# def test_df_not_empty():
#     # Tests is the pivot tables operation resulted in empty DataFrame
#     dataread = "/data/WDIData.csv"
#     dataout = "temp"
#     datafile1 = "test_energy_test.csv"
#     datafile2 = "test_energy_train.csv"
#     seed = 310
#     main(dataread, dataout, datafile1, datafile2, seed)
#     energy_test = pd.read_csv(os.path.join(dataout, datafile1))
#     energy_train = pd.read_csv(os.path.join(dataout, datafile2))
    
#     assert len(energy_train) > 0
#     assert len(energy_test) > 0
#     assert len(energy_train) + len(energy_test) > 0
#     assert energy_train.shape[0] > 0 
#     assert energy_test.shape[0] > 0  

# @click.command()
# @click.option('--dataread', help='path to directory where data is located')
# @click.option('--dataout', help='Which directory would you like this file to be written to?')
# @click.option('--datafile1', help='Name of file to save testing set to')
# @click.option('--datafile2', help='Name of file to save training set to')
# @click.option('--seed', default= 123, help='To ensure consistent values, what seed to set the analysis to')

# def test_column_names():
#     # Tests is the correct columns were selected and exist
    
#     dataread = "/data/WDIData.csv"
#     dataout = "temp"
#     datafile1 = "test_energy_test.csv"
#     datafile2 = "test_energy_train.csv"
#     seed = 310
#     main(dataread, dataout, datafile1, datafile2, seed)
#     energy_test = pd.read_csv(os.path.join(dataout, datafile1))
#     energy_train = pd.read_csv(os.path.join(dataout, datafile2))
    
#     expected_columns = [
#         'Access to electricity (% of population)', 'Adjusted net national income (constant 2015 US$)',
#         'CO2 emissions (kt)', 'Death rate, crude (per 1,000 people)',
#         'Land area (sq. km)', 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)',
#         'Population, total', 'Renewable energy consumption (% of total final energy consumption)',
#         'Renewable electricity output (% of total electricity output)'
#     ]
#     assert all(col in energy_train.columns for col in expected_columns)
#     assert all(col in energy_test.columns for col in expected_columns)

# @click.command()
# @click.option('--dataread', help='path to directory where data is located')
# @click.option('--dataout', help='Which directory would you like this file to be written to?')
# @click.option('--datafile1', help='Name of file to save testing set to')
# @click.option('--datafile2', help='Name of file to save training set to')
# @click.option('--seed', default= 123, help='To ensure consistent values, what seed to set the analysis to')

# def test_na_imputed():
#     # Tests is NA values were imputed properly
#     dataread = "data/WDIData.csv"
#     dataout = "temp"
#     datafile1 = "test_energy_test.csv"
#     datafile2 = "test_energy_train.csv"
#     seed = 123
#     main(dataread, dataout, datafile1, datafile2, seed)
#     energy_test = pd.read_csv(os.path.join(dataout, datafile1))
#     energy_train = pd.read_csv(os.path.join(dataout, datafile2))
    
#     assert energy_train.isnull().sum().sum() == 0
#     assert energy_test.isnull().sum().sum() == 0
    
