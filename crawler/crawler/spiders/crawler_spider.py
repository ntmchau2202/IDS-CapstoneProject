from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import FormRequest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["worldweatheronline.com"]

    url_list = [
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-cau-giay/ha-noi-q408.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-ba-dinh/ha-noi-q407.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-dong-da/ha-noi-q409.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-ha-dong/ha-noi-q410.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-hai-ba-trung/ha-noi-q411.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/hoan-kiem/ha-noi-q412.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-hoang-mai/ha-noi-q413.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-long-bien/ha-noi-q414.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-tay-ho/ha-noi-q415.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-thanh-xuan/ha-noi-q416.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-nam-tu-liem/ha-noi-q434.htm",
        "http://i-batdongsan.com/cho-thue-shop-kiot-quan/quan-bac-tu-liem/ha-noi-q704.htm"
    ]

    def start_requests(self):
        for url in self.url_list:
            yield FormRequest(url,dont_filter=True)

    def parse(self, response):
        items_list = Selector(response).xpath('//div[@class="content-items"]')

        for item_data in items_list:
            item_data.xpath(".//div[2]text()").extract_first()
        weather_data.append(time1_data_text)

        df = pd.DataFrame(np.array(weather_data))
        df['date'] = np.full(
            shape=8,
            fill_value=request_date,
        )
        df.to_csv('output.csv', mode='a', header=False, index=False)

