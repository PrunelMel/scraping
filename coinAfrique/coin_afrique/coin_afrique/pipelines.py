# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

class CoinAfriquePipeline:

    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()
        self.create()
        self.db_id = self.getId()


    def create(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id VARCHAR(15),
        category VARCHAR(50),
        image VARCHAR(500),
        title VARCHAR(500),
        price VARCHAR(50),
        posted_since VARCHAR(50),
        location VARCHAR(500))
        """)

    def getId(self)-> list:
        prodId = self.cursor.execute("SELECT product_id FROM products").fetchall()
        return [i[0] for i in prodId]

    def process_item(self, item, spider):

        if item['prod_id'] in self.db_id:
            print("Exist")
        else:
            self.cursor.execute("INSERT INTO products(product_id, category, image, title, price, posted_since, location) VALUES (?,?,?,?,?,?,?)",(item['prod_id'], item['category'], item['img'], item['title'], item['price'], item['posted_since'], item['location']))
            self.connection.commit()
        return item
