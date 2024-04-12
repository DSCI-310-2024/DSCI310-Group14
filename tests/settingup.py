
import os
import zipfile
import pandas as pd

data_for_df= {'Country':['Canada', 'US', 'Jamaica'],
        'Number':[20, 21, 19]}
data= pd.DataFrame(data_for_df)

# make a directory with file called test1.csv
file1= open("test_data/test1.csv", "w")
file1.write("this is a test file")


data.to_csv('test_data/targ.csv', index=False)


# make a empty zip file
with zipfile.ZipFile('test_data/emptyfile.zip', 'w', zipfile.ZIP_STORED) as zipf:
    pass

# make a dummy zip file
with zipfile.ZipFile('test_data/dummydata.zip', 'w', zipfile.ZIP_STORED) as zipf:
    zipf.write("test_data/targ.csv")
    zipf.write("test_data/test1.csv")



