The goal is to create a script able to get product's data from website coinafrique.com.
It must return if available: category, name, date, location and price.
This project only require python especially and scrapy framework.
To run the project, just run in terminal: 
1. Create a new folder and clone our repository
2. Then create a virtual environment and activate it by enter in your terminal 'python3 -m venv venv' and after '. venv/bin/activate'.
3. Finally install scrapy with 'pip install scrapy' and run 'scrapy crawl div -O data.json:json' to get scraped data.

