import pandas as pd
import sys
import pathlib
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_read import reading_datain
import pytest

# Dummy data for tests to work with
empty_zip="https://github.com/DSCI-310-2024/DSCI310-Group14/blob/testing1/tests/test_data/emptyfile.zip"

zip_with_files= "https://github.com/DSCI-310-2024/DSCI310-Group14/raw/testing1/tests/test_data/dummydata.zip"

invalid_url="https://github.com/DSCI-310-2024/DSCI310-Group14/blob/testing1/tests/test_data/emptyfil"

no_zip_url= "https://github.com/DSCI-310-2024/DSCI310-Group14/blob/testing1/tests/test_data/test1.csv"


def test_path_exists():
    # Check if the path to the datafile exists and is valid
    path = pathlib.Path("data/raw/downloaded.csv")
    assert os.path.exists(path)

def test_url_not_exist():
    # Check if the inputted URL exists, and is not an invalid URL
    # url= 'https://github.com/ttimbers/breast_cancer_predictor_py/blob/main/src/read_zip'
    with pytest.raises(ValueError, match='The inputed URL does not exist.'):
        reading_datain(invalid_url,"WDICSV.csv", "data/raw","downloaded.csv")

def test_nozip():
    # Check if the inputted URL is a .zip file, as otherwise the function will not be able to run
    # url= 'https://databank.worldbank.org'
    with pytest.raises(ValueError, match='The inputed URL is not a ZIP file, please input a ZIP file'):
        reading_datain(no_zip_url,"WDICSV.csv", "data/raw","downloaded.csv")

def test_specified_file_does_not_exist():
    # Check if the specified file exists within the zip file that the URL corresponds to 

    # url="https://databank.worldbank.org/data/download/WDI_CSV.zip"
    with pytest.raises(ValueError, match="The specified file is not present within the inputed ZIP file"):
        reading_datain(zip_with_files, "fakename.csv", "data/raw","downloaded.csv")

def test_clean_up():
    # Clean up the downloaded csv file
    os.remove("data/raw/downloaded.csv")
    path = pathlib.Path("data/raw/downloaded.csv")
    assert not os.path.exists(path)







 

