# Predicting the renewable electricity output of different countries
### DSCI 310 Group Project for Team 14
Contributors: Caden Chan, Neha Menon, Peter Chen & Tak Sripratak

Data Source Link (From World Bank): https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators

# About
As a complex issue, climate change doesn't have a singular cause, though the impacts of burning fossil fuels is a large source of greenhouse gases, and has caused detrimental effects. Our analysis here attempts to explore **if a subset of renewable energy related World Development Indicators** along with a simple **linear regression model** can be used to **predict renewable electricity outputs** of countries throughout the world. Our analysis created a model with an Root Mean Squared Error (RMSE) score of 23.74. Our model was able to predict most cases accurately though there are some predictions with low accuracy, not close to the actual values. Our model did predict some countries to have a negative renewable electricity output which demonstrates the need for a more complex analysis to be conducted, using advanced machine learning methods. By creating an advanced machine learning model, the capabilities of countries to produce more renewable electricity based on their other World Development Indicators can be calculated and used to influence country specific and global goals and targets.

# Report
The final report can be found at `reports/renewable_energy_report.html` after the following steps are completed to run analysis and generate the report. 

# Usage (Docker)

To set up the environment to reproduce the study results, build and run the container using either `Dockerfile` or the DockerHub image. All required packages and versions are specified in container image. 

First, ensure Docker has been installed and is running. This step must be done for the analysis to run, and the following commands to succesfully execute. 

Then, clone the repository by putting the following command into your terminal: 
```
git clone https://github.com/DSCI-310-2024/DSCI310-Group14.git

```

Navigate into the project directory using terminal commands. 

To run the analysis, first paste the following command into terminal:

```
docker-compose run --rm final-analysis-env make clean

```
Then the next command to run the analysis:

```
docker-compose run --rm final-analysis-env make all

```

This should automatically read and tidy the data, perform analysis, and generate two reports, `renewable_energy_report.html` and `renewable_energy_report.pdf`, both of which can be found within the `reports` folder of the main directory.

# Tests

To run the tests, go to the root of the project directory and enter 
```
pytest tests/

```
# Project Dependencies: 
This project requires certain packages to be installed in order for the analysis to execute and the correct visualizations to be generated, and for the final report to be built. All dependencies are solved when the container is used. 

- `matplotlib`
- `numpy`
- `pandas`
- `scikit-learn`
- `seaborn`
- `click`
- `quarto`
- `tabulate`
-  `altair`
- `renewenergy`
- Jupyter Lab


# License

The renewable electricity report is licensed under the Creative Commons [Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). The code contained in this repository is licensed under the [MIT license](https://opensource.org/licenses/MIT). For more information, please see the license file. 


# References

Copied from the report: 

Lotzof, K. Renewable energy and its importance for tackling climate change. (n.d.). National History Museum. Retrieved March 2, 2024, from https://www.nhm.ac.uk/discover/renewable-energy.html

Munk School Staff. Why some countries lead – and others lag – in the race to clean energy: Study | University of Toronto. (2022, October 7). Retrieved March 2, 2024, from https://www.utoronto.ca/news/why-some-countries-lead-and-others-lag-race-clean-energy-study

National Geographic Society. Climate Change. (2023, October 19). Retrieved March 2, 2024, from https://education.nationalgeographic.org/resource/climate-change

Renewable energy – powering a safer future. (n.d) United Nations; United Nations. Retrieved March 2, 2024, from https://www.un.org/en/climatechange/raising-ambition/renewable-energy

Shinn, L. Renewable Energy Definition—Sources, Clean Alternatives. (2022, June 1). NRDC.   Retrieved March 2, 2024, from https://www.nrdc.org/stories/renewable-energy-clean-facts

World Development Indicators, The World Bank | Data Catalog. (2023, December 18). Retrieved March 2, 2024, from https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators
