import click
from io import BytesIO
# import urllib.request as urllib2
import pandas as pd
import os
from zipfile import ZipFile
from urllib.request import urlopen



@click.command()
@click.option('--url',help='URL of file you want to read in')
@click.option('--data_file',default="WDIData.csv", help='Which file in the ZIP file the data you want is in')
@click.option('--data_path', help='Which directory would you like this file to be written to?')
@click.option('--save_file_to', help='Which file would you like this file to be saved to?')

def reading_data(url, data_file, data_path, save_file_to):
    """Simple program that reads in the data from a URL, and selects a file from the .zip."""
    data_url= urlopen(url)
    file = ZipFile(BytesIO(data_url.read()))
    data_csv = file.open(data_file)
    data = pd.read_csv(data_csv)
    os.makedirs(data_path, exist_ok=True)  
    data.to_csv(save_file_to)  

if __name__ == '__main__':
    reading_data()

