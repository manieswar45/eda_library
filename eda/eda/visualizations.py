import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_missing_values(df: pd.DataFrame, columns: list = None, percentage: bool = False):
    if columns is not None:
        df = df[columns]
    
    # Calculate percentage of missing values
    if percentage:
        missing_percent = df.isnull().mean() * 100
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    
    # Add missing value percentages as text annotations if percentage is True
    if percentage:
        for idx, col in enumerate(df.columns):
            plt.text(idx + 0.5, -0.5, f'{missing_percent[col]:.1f}%', 
                     ha='center', va='center', color='black', fontsize=12)
    
    plt.show()
    #pass

def plot_distributions(df: pd.DataFrame, columns: list = None):
    if columns is not None:
        df = df[columns]
    
    df.hist(figsize=(20, 20), bins=30)
    plt.show()
    #pass

def plot_correlation_matrix(df: pd.DataFrame):
    numerical_columns = df.select_dtypes(include = ['float64', 'int64']).columns
    df = df[numerical_columns]
    plt.figure(figsize=(12, 10))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
    #pass

__all__ = ['plot_missing_values', 'plot_distributions', 'plot_correlation_matrix']