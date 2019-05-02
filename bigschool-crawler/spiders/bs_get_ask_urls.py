import scrapy
from scrapy.selector import Selector
import json
from bs4 import BeautifulSoup as bs
import pymysql

class exam(scrapy.Spider):
    name = "bs-get-ask-urls"

    def start_requests(self):
        url = "https://ask.bigschool.vn/ask.html?type=&txtSearch=&o=0&c=12&s=1&t=-1&p="
        for i in range(128):
            yield scrapy.Request(url=url+str(i+1), callback=self.parse)

    def parse(self, response):
        f = open('temp.txt', 'a')
        for url in response.selector.xpath("//span[@class='rep-btn']/a/@href").extract():
            f.write("{}\n".format(url))
