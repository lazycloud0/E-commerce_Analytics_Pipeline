import pandas as pd
from sqlalchemy import create_engine

# Define ETL pipeline functions
# Extract data from a file
def extract_data(file_path):
    return pd.read_csv(file_path)

# Transform data
def transform_data(df):
    # Example transformation: Calculate total sales
    df['total_sales'] = df['quantity'] * df['price']
    return df

# Load data into a SQL database
def load_data(df, db_url):
    engine = create_engine(db_url)
    df.to_sql('sales', con=engine, if_exists='replace', index=False)

# Define main function
def main():
    # Define database URL (PostgreSQL example)
    db_url = 'postgresql://username:password@localhost:5432/ecommerce_db'

    # Extract
    df = extract_data('data/sales_data.csv')

    # Transform
    transformed_df = transform_data(df)

    # Load
    load_data(transformed_df, db_url)

if __name__ == "__main__":
    main()
