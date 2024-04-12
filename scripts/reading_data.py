import click
from io import BytesIO
# import urllib.request as urllib2
import pandas as pd
import os
from zipfile import ZipFile
from urllib.request import urlopen
import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from renewenergy.reading_data import reading_data


@click.command()
@click.option('--url',help='URL of file you want to read in', type=str)
@click.option('--data_file', help='Which file in the ZIP file the data you want is in', type=str)
@click.option('--data_path', help='Which directory would you like this file to be written to?', type=str)
@click.option('--file_name', help='Name of file to save data set to', type=str)

def reading_data(url, data_file, data_path, file_name):
    """Simple program that reads in the data from a URL, and selects a file from the .zip."""
    reading_datain(url, data_file, data_path, file_name)

if __name__ == '__main__':
    reading_data()