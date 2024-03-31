
import os
import zipfile

#make a directory with file called WDIData.csv
file1= open("test1.csv", "w")
file1.write("this is a test file")

file1= open("WDIDATA.csv", "w")
file1.write("DUMMY DATA")


#make a empty zip file
with zipfile.ZipFile('emptyfile.zip', 'w', zipfile.ZIP_STORED) as zipf:
    pass

with zipfile.ZipFile('dummydata.zip', 'w', zipfile.ZIP_STORED) as zipf:
    zipf.write('test1.csv')
    zipf.write('WDIDATA.csv')



