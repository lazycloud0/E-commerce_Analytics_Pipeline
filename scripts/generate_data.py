import pandas as pd
import random
from datetime import datetime, timedelta

# Generate sales data
def generate_sales_data(num_records):
    customers = [f'Customer_{i}' for i in range(1, 101)]
    products = [f'Product_{i}' for i in range(1, 21)]
    data = []

    for _ in range(num_records):
        transaction_id = len(data) + 1
        customer_id = random.choice(customers)
        product_id = random.choice(products)
        quantity = random.randint(1, 5)
        price = random.uniform(10.0, 100.0)
        timestamp = datetime.now() - timedelta(days=random.randint(0, 30))
        total_sales = quantity * price

        data.append([transaction_id, customer_id, product_id, quantity, price, timestamp, total_sales])

    df = pd.DataFrame(data, columns=['transaction_id', 'customer_id', 'product_id', 'quantity', 'price', 'timestamp', 'total_sales'])
    df.to_csv('data/sales_data.csv', index=False)

if __name__ == "__main__":
    generate_sales_data(1000)  # Generate 1000 records
