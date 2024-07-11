from typing import Any, Iterable
import scrapy
from scrapy.http import Response



class owner (scrapy.Spider):
    
    name = "owner"

    start_urls:list = [ "https://infonet.fr/entreprises/55204300202902-air-france-klm/" ]    

    def parse(self, response):

        for div in response.css("div#company-contact-information > div.col-12"):

            data:dict = {
                "1":div.attrib["class"]
            }

            yield data

        """for a in response.css("div.pagination.custom ul.center.custom li.pagination-number a"):
            yield response.follow(a, callback = self.parse)"""
