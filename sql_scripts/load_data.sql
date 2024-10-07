-- Load Customers
INSERT INTO customers (name, email, location)
VALUES ('John Doe', 'john@example.com', 'New York');

-- Load Products
INSERT INTO products (name, category, price)
VALUES ('Laptop', 'Electronics', 999.99);

-- Load Sales
INSERT INTO sales (customer_id, product_id, total_sales, timestamp)
VALUES (1, 1, 999.99, '2023-10-01 12:00:00');
