import sys
import pathlib
import os
from functions.functionread import reading_datain


url= 'https://databank.worldbank.org/data/download/WDI_CSV.zip'

def test_path_exists():
    url= 'https://databank.worldbank.org/data/download/WDI_CSV.zip'
    trial1=reading_datain(url,"WDICSV.csv", "data/raw","downloaded.csv")
    path = pathlib.Path("data/raw/downloaded.csv")
    #path= "data/raw/downloaded.csv"
    assert os.path.exists(path)


# def test_contents_same():
#     actual = pd.read_csv("data/raw/downloaded.csv")
#     expected = pd.read_csv("reading_data_example.txt")
#     assert actual == expected

 
#test case 1: empty file 
#test case 2: no file called WDIData.csv
#test case 3: works
#test case 4: only one file in zip 

