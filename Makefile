all: results/figures/final_analysis.png

#download data from the URL
data/raw/downloaded.csv: scripts/reading_data.py
	python scripts/reading_data.py \
	--url="https://databank.worldbank.org/data/download/WDI_CSV.zip" \
	--data_file="WDIData.csv" \
	--data_path=data/raw \
	--file_name=downloaded.csv \

#tidy the data and split into training and testing set
data/processed/energy_test.csv data/processed/energy_train.csv: data/raw/downloaded.csv scripts/cleaning_data.py
	python scripts/cleaning_data.py \
	--dataread=data/raw/downloaded.csv \
	--dataout=data/processed \
	--datafile1=energy_test.csv \
	--datafile2=energy_train.csv \
	--seed=123

#eda 
results/figures/EDA.png: data/processed/energy_train.csv scripts/eda.py
	python scripts/eda.py --data_path=data/processed/energy_train.csv \
	--output_path=results/figures/EDA.png

#linear regression analysis
results/figures/final_analysis.png : data/processed/energy_test.csv data/processed/energy_train.csv scripts/linear_regression.py
	python scripts/linear_regression.py --training_data_path=data/processed/energy_train.csv \
	--test_data_path=data/processed/energy_test.csv \
	--output_path=results/figures/final_analysis.png

clean:
	rm -f data/raw/downloaded.csv
	rm -f data/energy_test.csv
	rm -f data/energy_train.csv
	rm -f results/figures/EDA.png
	rm -f results/figures/final_analysis.png
