import scrapy
i=0
class TorobSpider(scrapy.Spider):
    name = "torob"
    allowed_domains = ["www.torob.com"]
    start_urls = ["https://torob.com/search/?query=%D8%AA%D8%B3%D9%85%D9%87%20%D8%AA%D8%A7%DB%8C%D9%85"]

    def parse(self , response):
        information = response.css('div h2.ProductCard_desktop_product-name__JwqeK::text').extract()
        price = response.css('div div.ProductCard_desktop_product-price-text__y20OV::text').extract()
        yield {
            'info' : information,
            'price' : price
        }