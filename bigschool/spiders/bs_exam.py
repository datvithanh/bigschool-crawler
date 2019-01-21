import scrapy
from scrapy.selector import Selector
import json
from bs4 import BeautifulSoup as bs
import pymysql

class exam(scrapy.Spider):
    name = "bs-exam"

    def start_requests(self):
        data = json.load(open('data_exam.json'))
        data = data['data'][2]
        if data["status"] == "done":
            exit(0)
        print('----------------------------------------------------------------')
        print(data['name'])
        urls = data['urls']
        cookies = data['cookies']
        for url in urls:
            yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        config = json.load(open('config.json'))
        db = pymysql.connect(config['host'],config['user'],config['password'],config['database_name'])
        cursor = db.cursor()

        questions = response.selector.xpath(
            "//div[@class='questionContent']").extract()
        answers = response.selector.xpath(
            "//label[@class='col-sm-12'][contains(text(),'Lời giải chi tiết')]/..").extract()
        print(len(questions))
        print(len(answers))
        for i in range(len(questions)):
            de_bai = db.escape_string(bs(questions[i], 'html.parser').prettify())
            dap_an = db.escape_string(bs(answers[i], 'html.parser').prettify())
            sql = "insert into bs_posts(title, url, crawler, subject_html, content_html, data, count) \
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(response.url, response.url, 'big_school', de_bai, dap_an, '', i+1)
            cursor.execute(sql)
            db.commit()
        
        cursor.close()
        db.close()

# https://ask.bigschool.vn/ask.html?type=&txtSearch=&o=0&c=12&s=1&t=-1&p=128

# <label class="col-sm-12">Lời giải chi tiết</label>
