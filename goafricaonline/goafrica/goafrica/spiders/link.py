import scrapy
from scrapy.linkextractors import LinkExtractor


class LinkSpider(scrapy.Spider):
    name = "link"
    allowed_domains = ["goafricaonline.com"]
    start_urls = ["https://goafricaonline.com/bj"]

    def parse(self, response):
        link_extractor = LinkExtractor()
        for link in link_extractor.extract_links(response):
            yield {"url":link.url}
