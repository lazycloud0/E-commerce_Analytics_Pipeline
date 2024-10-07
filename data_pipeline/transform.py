import pandas as pd

def transform_data(df):
    """Transform the data by cleaning and processing."""
    # Example transformation: drop rows with missing values
    df = df.dropna()
    return df