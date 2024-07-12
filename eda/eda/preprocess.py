import pandas as pd

def fill_missing_values(df: pd.DataFrame, strategy: str = 'mean'):
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        if strategy == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif strategy == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif strategy == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)
    return df

def encode_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes categorical columns in the given DataFrame without using sklearn.
    
    Args:
    df (pd.DataFrame): Input DataFrame
    
    Returns:
    pd.DataFrame: DataFrame with categorical columns encoded
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df_encoded = df.copy()
    
    # Identify categorical columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    # Dictionary to store encoding mappings
    encoding_dict = {}
    
    # Encode each categorical column
    for col in categorical_columns:
        # Get unique values and create a mapping
        unique_values = df[col].unique()
        value_to_int = {value: i for i, value in enumerate(unique_values)}
        
        # Apply the mapping to the column
        df_encoded[col] = df[col].map(value_to_int)
        
        # Store the encoding for this column
        encoding_dict[col] = value_to_int
    
    return df_encoded, encoding_dict


__all__ = ['fill_missing_values', 'encode_categorical_columns']