import pandas as pd

def extract_data(file_path):
    """Extract data from a CSV file."""
    return pd.read_csv(file_path)