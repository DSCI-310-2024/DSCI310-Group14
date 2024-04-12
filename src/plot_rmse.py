import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import set_config
from sklearn.metrics import mean_squared_error
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.split_xy_columns import split_xy_columns


def plot_rmse(training_data_path, test_data_path, output_path):
    """
    Perform linear regression and plot the results on a graph containing Expected vs Predicted observations 

    Parameters
    ----------
    training_data_path: str
        Path to training data .csv file
    
    test_data_path: str
        Path to test data .csv file
    
    output_path: str
        Directory to which the figure should be saved to. 
    
    
    Returns
    -------
    results.png:
        Figure containing the Predicted vs Expected Values of the linear regression.

    Examples
    --------
    >>> plot_rmse("data/energy_train.csv", "data/energy_test.csv", "results/" )
    
    """
    #read clean train and test dataset

    energy_train = pd.read_csv(training_data_path)
    energy_test = pd.read_csv(test_data_path)

    #splitting the x and y columns of the data

    energy_train_x, energy_train_y = split_xy_columns(energy_train)
    energy_test_x, energy_test_y = split_xy_columns(energy_test)
    
    #making the linear model
    lm=LinearRegression()
    lm.fit(energy_train_x, energy_train_y)
    
    y_true = energy_test_y['Renewable electricity output (% of total electricity output)']
    y_pred = lm.predict(energy_test_x)
    energy_RMSE = mean_squared_error(y_true=y_true,
                                     y_pred=y_pred)**(1/2)

    fig = plt.figure()
    plt.scatter(x=y_pred, y=energy_test_y['Renewable electricity output (% of total electricity output)'])
    plt.title(f"Predicted vs. Ground Truth Target Value (RMSE={energy_RMSE})")
    plt.xlabel("Predicted Values")
    plt.ylabel("True Values")
    plt.savefig(output_path)
    return energy_RMSE, fig

#if __name__ == '__main__':
#    plot_rmse()
