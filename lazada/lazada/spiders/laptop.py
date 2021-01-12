import scrapy
from scrapy_splash import SplashRequest

class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    def start_requests(self):
        url ='https://www.lazada.com.my/shop-laptops-gaming/?spm=a2o4k.home.cate_1_2.2.75f82e7e1Mg1X9'
        yield SplashRequest(url)        

    def parse(self, response):
        products_selector = response.css('[data-tracking="product-card"]')
        for product in products_selector:
            yield {
                'name': product.css('a[title]::attr(title)').get(),
                'price': product.css('span:contains("RM")::text').get()
            }
