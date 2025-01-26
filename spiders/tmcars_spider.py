import scrapy


class TmcarsSpiderSpider(scrapy.Spider):
    name = "tmcars_spider"
    allowed_domains = ["tmcars.info"]
    start_urls = ["https://tmcars.info/cars/toyota"]

    def parse(self, response):
        pass
        toyota = response.css('div.col-lg-6.col-md-6.col-xl-4.col-sm-6.col-xs-12')

        city = response.css('p.pb-0.pt-0.mb-2.mt-1.no-wrapped::text').get()
        title = response.css('h5.font-weight-semibold.mt-1.shorted-title::text').get()
        price = response.css('span.font-weight-bold::text').get()
        
