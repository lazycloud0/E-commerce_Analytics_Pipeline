import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from data_pipeline.config import DB_URI

def visualize_data():
    engine = create_engine(DB_URI)
    
    # Load data from the data warehouse
    sales = pd.read_sql('sales', engine)
    products = pd.read_sql('products', engine)
    customers = pd.read_sql('customers', engine)
    
    # Example visualization: Total sales over time
    sales['timestamp'] = pd.to_datetime(sales['timestamp'])
    sales.set_index('timestamp', inplace=True)
    sales['total_sales'].resample('M').sum().plot()
    plt.title('Total Sales Over Time')
    plt.xlabel('Time')
    plt.ylabel('Total Sales')
    plt.show()

if __name__ == '__main__':
    visualize_data()