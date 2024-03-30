import pandas as pd
import sys
import pathlib
import os
from functions.functionread import reading_datain
import pytest



#will test if function works as it is meant to

def test_path_exists():
    url= 'https://databank.worldbank.org/data/download/WDI_CSV.zip'
    trial1=reading_datain(url,"WDICSV.csv", "data/raw","downloaded.csv")
    path = pathlib.Path("data/raw/downloaded.csv")
    assert os.path.exists(path)

def test_url_not_exist():
    url= 'https://github.com/ttimbers/breast_cancer_predictor_py/blob/main/src/read_zip'
    with pytest.raises(ValueError, match='The inputed URL does not exist.'):
        reading_datain(url,"WDICSV.csv", "data/raw","downloaded.csv")

def test_nozip():
    url= 'https://databank.worldbank.org'
    with pytest.raises(ValueError, match='The inputed URL is not a ZIP file, please input a ZIP file'):
        reading_datain(url,"WDICSV.csv", "data/raw","downloaded.csv")

# def test_zip():
#     url="https://databank.worldbank.org/data/download/WDI_CSV.zip"
#     with pytest.raises(ValueError, match="The specified file is not present within the inputed ZIP file"):
#         reading_datain(url, "WDICSV.csv", "data/raw","downloaded.csv")

def test_specified_file_does_not_exist():
    url="https://databank.worldbank.org/data/download/WDI_CSV.zip"
    with pytest.raises(ValueError, match="The specified file is not present within the inputed ZIP file"):
        reading_datain(url, "fakename.csv", "data/raw","downloaded.csv")

def test_filename_exists():
    url="https://databank.worldbank.org/data/download/WDI_CSV.zip"
    with pytest.raises(ValueError, match="The filename already exists."):
        reading_datain(url,"WDICSV.csv", "data/raw","downloaded.csv")

# def test_path_preexisting():
#     url=""
#     with pytest.raises(ValueError, match="The filepath already exists."):
#         reading_datain(url, "", "", "")





 

