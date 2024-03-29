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
    data1=data1.fillna(0)
    energy_train, energy_test= train_test_split(data1, train_size=0.75)
    os.makedirs(dataout, exist_ok=True)  
    energy_test.to_csv(dataout+"/"+datafile1)  
    energy_train.to_csv(dataout+ "/"+datafile2)

if __name__ == '__main__':
    main()
