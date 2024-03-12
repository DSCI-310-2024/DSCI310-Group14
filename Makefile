

#download data from the URL
data/downloaded.csv: scripts/reading_data.py
        python scripts/reading_data.py --url= "https://databank.worldbank.org/data/download/WDI_CSV.zip"\
        --data_file= "WDIData.csv"\
        --data_path=data/raw\
        --save_file_to= data/raw/downloaded.csv


#tidy the data and split into training and testing set
data/energy_test.csv data/energy_train.csv: data/raw/downloaded.csv scripts/cleaning.py
        python scripts/cleaning.py --dataread=data/raw/downloaded.csv\ 
        --dataout= data/processesed\
        --datafile1= data/processesed/energy_test.csv\
        --datafile2=data/processesed/energy_train.csv
