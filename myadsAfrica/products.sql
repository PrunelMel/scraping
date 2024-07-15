-- SQLite
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(15),
    category VARCHAR(50),
    title VARCHAR(500),
    location VARCHAR(500),
    price VARCHAR(50),
    date VARCHAR(50)
);

DROP TABLE products;