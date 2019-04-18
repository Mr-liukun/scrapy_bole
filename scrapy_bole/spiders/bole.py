
import scrapy

from scrapy_bole.items import ItemsBole

from scrapy.http import Request
from urllib import parse

class BoleSpider(scrapy.Spider):
    name = 'bole'  # 爬虫的识别名字，必须唯一
    allowed_domains = ['http://blog.jobbole.com/all-posts/']  # 域名范围，爬虫只会爬取这个域名下的网页
    start_urls = ['http://blog.jobbole.com/all-posts/']  # 爬虫的url列表
    def parse(self, response):

        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail,dont_filter=True)

        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
             yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse,dont_filter=True)


    def parse_detail(self, response):

        bole = ItemsBole()

        url = response.url

        time = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", "").strip()

        title = response.css(".entry-header h1::text").extract()[0]

        typeList = response.css("p.entry-meta-hide-on-mobile a::text")

        type=""

        for i in range(len(typeList)):
            if typeList[i].extract().find("评论") != -1:
                continue

            if i != len(typeList) - 1:
                type += typeList[i].extract() + ","
            else:
                type += typeList[i].extract()

        #content = response.css("div.entry p::text").extract()

        bole["url"] = url
        bole["title"] = title
        bole["type"] = type
        bole["content"] = ""
        bole["time"] = time
        return bole



