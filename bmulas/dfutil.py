"""
package df_util module - module containing specific ultilities for DF management
"""
import pandas as pd

def getNulls(X):
    try:
        assert isinstance(X, pd.DataFrame)
        nulls = X.isnull().sum()
        print(nulls)

    except AssertionError:
        raise AssertionError('{} not a valid class. Expecting pandas DataFrame.'.format(type(X)))

def description(X):
    try:
        assert isinstance(X, pd.DataFrame)
        for col in X:
            print(f'Now looking at column {col}.')
            print(' ')
            print(X[col].describe())
            print(' ')
    except AssertionError:
        raise AssertionError('{} not a valid class. Expecting pandas DataFrame.'.format(type(X)))

def add_col(df, name, new_list):
    try:
        assert len(new_list) == df.shape[0]
        df[name] = pd.Series(new_list)
        return df

    except Exception as e:
        print(e)