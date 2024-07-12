import pandas as pd

def summary_statistics(df: pd.DataFrame):
    return df.describe()

def missing_values_stats(df: pd.DataFrame):
    return df.isnull().sum()

def unique_values_stats(df: pd.DataFrame):
    return df.nunique()

__all__ = ['summary_statistics', 'missing_values_stats', 'unique_values_stats']