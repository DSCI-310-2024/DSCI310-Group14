import click
from io import BytesIO
import pandas as pd
import os
from zipfile import ZipFile
from urllib.request import urlopen
from sklearn.model_selection import train_test_split
import numpy as np
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.clean_data import clean_data
# from renewenergy.clean_data import clean_data

@click.command()
@click.option('--dataread', help='path to directory where data is located')
@click.option('--dataout', help='Which directory would you like this file to be written to?')
@click.option('--datafile1', help='Name of file to save testing set to')
@click.option('--datafile2', help='Name of file to save training set to')
@click.option('--seed', default= 123,help='To ensure consistent values, what seed to set the analysis to')

def cleaning_data(dataread,dataout,datafile1, datafile2, seed):
    clean_data(dataread,dataout,datafile1, datafile2, seed)

if __name__ == '__main__':
    cleaning_data()
