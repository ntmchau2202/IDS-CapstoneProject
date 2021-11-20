# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging


class CrawlerPipeline:
    def process_item(self, item, spider):
        logging.info("\n=========\n\n PROCESS \n\n=========\n")
        logging.info(item)
        # item.to_csv('output.csv', mode='a', header=False, index=False)
        return item
