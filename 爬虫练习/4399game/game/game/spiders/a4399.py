import scrapy


class A4399Spider(scrapy.Spider):
    name = '4399'
    allowed_domains = ['4399.com']
    start_urls = ['http://4399.com/']

    def parse(self, response):
        pass
