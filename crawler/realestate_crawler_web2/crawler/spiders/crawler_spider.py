from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import FormRequest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["alonhadat.com.vn"]

    url_list = [
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/407/quan-ba-dinh.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/408/quan-cau-giay.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/409/quan-dong-da.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/410/quan-ha-dong.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/411/quan-hai-ba-trung.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/412/hoan-kiem.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/413/quan-hoang-mai.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/414/quan-long-bien.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/415/quan-tay-ho.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/416/quan-thanh-xuan.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/434/quan-nam-tu-liem.html",
        "https://alonhadat.com.vn/nha-dat/cho-thue/shop-kiot-quan/ha-noi/704/quan-bac-tu-liem.html"
    ]

    def start_requests(self):
        for url in self.url_list:
            yield FormRequest(url,dont_filter=True)

    def parse(self, response):
        items_list = Selector(response).xpath('//div[@class="content-items"]/div')
        dataset = []

        for item_data in items_list:
            item = CrawlerItem()
            item["area"] = item_data.xpath("./div[@class='text']//div[@class='ct_dt']/text()").extract()[0]
            item["price"] = item_data.xpath("./div[@class='text']//div[@class='ct_price']/text()").extract()[0]
            item["location"] = item_data.xpath("./div[@class='text']//div[@class='ct_dis']/text()").extract()[-1][2:]
            
            yield item

