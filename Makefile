all: results/figures/EDA.png \
		results/figures/final_analysis.png \
		reports/renewable_energy_report.html \
		reports/renewable_energy_report.pdf \

#download data from the URL
data/raw/downloaded.csv: scripts/reading_data.py
	python scripts/reading_data.py \
	--url="https://databank.worldbank.org/data/download/WDI_CSV.zip" \
	--data_file="WDICSV.csv" \
	--data_path=data/raw \
	--file_name=downloaded.csv \

#tidy the data and split into training and testing set
data/processed/energy_test.csv data/processed/energy_train.csv: data/raw/downloaded.csv scripts/cleaning_data.py
	python scripts/cleaning_data.py \
	--dataread=data/raw/downloaded.csv \
	--dataout=data/processed \
	--datafile1=energy_test.csv \
	--datafile2=energy_train.csv \
	--seed=123 \

#eda 
results/figures/EDA.png: data/processed/energy_train.csv scripts/eda.py
	python scripts/eda.py \
	--data_path=data/processed/energy_train.csv \
	--output_path=results/figures/EDA.png \

#linear regression analysis
results/figures/final_analysis.png: data/processed/energy_test.csv data/processed/energy_train.csv scripts/linear_regression.py
	python scripts/linear_regression.py \
 	--training_data_path=data/processed/energy_train.csv \
	--test_data_path=data/processed/energy_test.csv \
	--output_path=results/figures/final_analysis.png \

#write the report
reports/renewable_energy_report.html : results reports/renewable_energy_report.qmd
	quarto render reports/renewable_energy_report.qmd --to html

reports/renewable_energy_report.pdf : results reports/renewable_energy_report.qmd
	quarto render reports/renewable_energy_report.qmd --to pdf

clean:
	rm -f data/raw/downloaded.csv
	rm -f data/processed/energy_test.csv
	rm -f data/processed/energy_train.csv
	rm -f results/figures/EDA.png
	rm -f results/figures/final_analysis.png
	rm -f reports/renewable_energy_report.html
	rm -f reports/renewable_energy_report.pdf
