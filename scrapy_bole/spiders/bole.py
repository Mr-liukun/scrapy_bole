
import scrapy

from scrapy_bole.items import ItemsBole

from scrapy.http import Request
from urllib import parse

class BoleSpider(scrapy.Spider):
    name = 'bole'  # 爬虫的识别名字，必须唯一
    allowed_domains = ['http://blog.jobbole.com/all-posts/']  # 域名范围，爬虫只会爬取这个域名下的网页
    start_urls = ['http://blog.jobbole.com/all-posts/']  # 爬虫的url列表
    def parse(self, response):

        # bole = ItemsBole()
        #
        # #标题
        # title = response.xpath('//*[@id="archive"]/div[1]/div[2]/p[1]/a[1]/text()')
        # title = title.extract_first()
        # bole["title"] = title
        #
        # # 时间
        # time = response.xpath('//*[@id="archive"]/div[1]/div[2]/p[1]/text()[2]')
        # ti = time.extract_first()
        # s = len(ti)
        # time = ti[s-13:s-2]
        # bole["time"] = time
        #
        # #分类
        # type = response.xpath('//*[@id="archive"]/div[1]/div[2]/p[1]/a[2]/text()')
        # type = type.extract_first()
        # bole["type"] = type
        #
        # #简介
        # content = response.xpath('//*[@id="archive"]/div[1]/div[2]/span/p/text()')
        # content = content.extract_first()
        # bole["content"] = content


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

        tag =""

        for i in range(len(typeList)):
            if i==0:
                type = typeList[i].extract
                continue

            if typeList[i].extract().find("评论") != -1:
                continue
            if i != len(typeList)-1:
                tag += typeList[i].extract()+","
            else:
                tag += typeList[i].extract()


        #content = response.css("div.entry p::text").extract()

        bole["url"] = url
        bole["title"] = title
        bole["type"] = type
        bole["tag"] = tag
        bole["content"] = ""
        bole["time"] = time

        return bole



