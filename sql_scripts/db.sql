-- Create Customers Dimension Table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    location VARCHAR(255)
);

-- Create Products Dimension Table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    price DECIMAL(10, 2)
);

-- Create Sales Fact Table
CREATE TABLE sales (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    product_id INTEGER REFERENCES products(product_id),
    total_sales DECIMAL(10, 2),
    timestamp TIMESTAMP
);
