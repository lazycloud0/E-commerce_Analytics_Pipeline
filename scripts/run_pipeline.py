import os
from data_pipeline.extract import extract_data
from data_pipeline.transform import transform_data
from data_pipeline.load import load_data
from data_pipeline.config import RAW_DATA_PATH, PROCESSED_DATA_PATH, DB_URI

def run_pipeline():
    # Extract
    customers = extract_data(os.path.join(RAW_DATA_PATH, 'customers.csv'))
    products = extract_data(os.path.join(RAW_DATA_PATH, 'products.csv'))
    sales = extract_data(os.path.join(RAW_DATA_PATH, 'sales.csv'))

    # Transform
    customers = transform_data(customers)
    products = transform_data(products)
    sales = transform_data(sales)

    # Load
    load_data(customers, 'customers', DB_URI)
    load_data(products, 'products', DB_URI)
    load_data(sales, 'sales', DB_URI)

if __name__ == '__main__':
    run_pipeline()