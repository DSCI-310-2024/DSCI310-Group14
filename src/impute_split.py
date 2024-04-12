import pandas as pd
from sklearn.model_selection import train_test_split
import numpy


def impute_split(data, impute_val, train_size, rand_seed=0):  
    """
    Takes a data frame and creates a a training and testing split, with imputation for NA values

    Parameters
    ----------
    data: DataFrame
        The initial dataset to be tidied
    impute_value: 
        The value to replace all NA values with within the dataset
    train_size: float
        A value from 0-1 that represents the % of data to be used in the training split (remainder will be used in testing split)
    rand_seed: int
        A seed value to be used for randomness, allowing for reproducible results; default value is 0

    Returns
    -------
    train: DataFrame
        Imputed, training dataset split
    test: DataFrame
        Imputed, testing dataset split

    Examples
    --------

    Create dummy dataframe
    >>> data = {
    >>>     'A': [1, 2, None, 4, 5],
    >>>     'B': [None, 6, 7, 8, 9],
    >>>     'C': [10, 11, 12, None, 14]
    >>>     'D': [15, 16, None, None, 19]
    >>> }
    >>> df = pd.DataFrame(data)

    Randomly split the dummy dataframe into two dataframes, with 2 rows each. All None values will be converted to a zero.
    >>> train, test = impute_split(data, 0, 0.5, 123)

    Randomly split the dummy dataframe into two dataframes, with train having 3 rows and test having 1. All None values will be converted to 999.
    >>> train, test = impute_split(data, 999, 0.75)

    """

    numpy.random.seed(rand_seed)
    data = data.fillna(impute_val)
    train, test = train_test_split(data, train_size = train_size)
    return train, test
