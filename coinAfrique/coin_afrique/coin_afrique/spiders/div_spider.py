from typing import Any, Iterable
import scrapy
from scrapy.http import Response



class div_spider(scrapy.Spider):
    
    name = "div"

    start_urls:list = [ "https://bj.coinafrique.com/" ]    

    def parse(self, response):

        for div in response.css("div.card.ad__card.round"):

            data:dict = {
                "prod_id": div.css("a.card-image span.btn-floating::attr(data-post-id)").get(),
                "category": div.css("a.card-image span.btn-floating::attr(data-ad-category)").get(),
                "img": div.css("a.card-image img.ad__card-img::attr(src)").get(),
                "title": div.css("a.card-image span.btn-floating::attr(data-ad-title)").get(),
                "price": " ".join(div.css("div p.ad__card-price a *::text").getall()),
                "posted_since": " ".join(div.css("a.card-image div.ad__card-timesince *::text").getall()),
                "location":div.css("div.card-content div p.ad__card-location span::text").get()
            }

            yield data

        for a in response.css("div.pagination.custom ul.center.custom li.pagination-number a"):
            yield response.follow(a, callback = self.parse)
