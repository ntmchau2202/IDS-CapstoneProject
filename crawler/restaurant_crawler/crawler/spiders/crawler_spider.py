from scrapy import Spider, Request
from scrapy.selector import Selector
from scrapy.http import FormRequest

from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["pasgo.vn"]

    def start_requests(self):
        url = "https://pasgo.vn/ha-noi/nha-hang"
        for page_number in range(1,50):
            yield FormRequest(f"{url}?page={page_number}",dont_filter=True)

    def parse(self, response):
        restaurant_list = Selector(response).xpath("//div[@class='wapcontent']/div[2]/div")

        for info in restaurant_list:
            res_url = info.xpath(".//a/@href").extract()[0]
            if res_url == "https://pasgo.vn/ha-noi/nha-hang":
                continue     
            yield Request(res_url, callback=self.parse_restaurant)
    
    def parse_restaurant(self, response):
        item = CrawlerItem()
        item["point"] = Selector(response).xpath("//span[@class='pasgo-star']/meta[@itemprop='ratingValue']/@content").extract_first()
        item["name"] = Selector(response).xpath("//span[@class='pasgo-title']/text()").extract_first()
        item["location"] = Selector(response).xpath('//span[@itemprop="streetAddress"]/text()').extract_first()
        item["open_time"] = Selector(response).xpath('//p[@class="hours-pickup"]/@content').extract_first()
        item["category"] = Selector(response).xpath('//article[1]/div[2]/div/div/div[1]/span/text()').extract_first()
        item["price"] = Selector(response).xpath('//span[@class="pasgo-giatrungbinh"]/text()').extract_first()

        yield item

