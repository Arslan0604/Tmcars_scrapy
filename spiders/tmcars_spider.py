import scrapy


class TmcarsSpiderSpider(scrapy.Spider):
    name = "tmcars_spider"
    allowed_domains = ["tmcars.info"]
    start_urls = ["https://tmcars.info/cars/toyota"]

    def parse(self, response):
        pass
