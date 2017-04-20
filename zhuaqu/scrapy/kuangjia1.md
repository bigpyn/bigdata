Python爬虫框架Scrapy教程(1)—入门

最近实验室的项目中有一个需求是这样的，需要爬取若干个（数目不小）网站发布的文章元数据（标题、时间、正文等）。问题是这些网站都很老旧和小众，当然也不可能遵守 Microdata 这类标准。这时候所有网页共用一套默认规则无法保证正确抓取到信息，而每个网页写一份spider代码也不切实际。

这时候，我迫切地希望能有一个框架可以通过只写一份spider代码和维护多个网站的爬取规则，就能自动抓取这些网站的信息，很庆幸 Scrapy 可以做到这点。鉴于国内外关于这方面资料太少，所以我将这段时间来的经验和代码分享成了本文。

为了讲清楚这件事，我分成了三篇文章来叙述：

编程方式下运行 Scrapy spider
使用Scrapy定制可动态配置的爬虫
使用Redis和SQLAlchemy对Scrapy Item去重并存储
本篇文章主要介绍如何使用编程的方式运行Scrapy爬虫。

在开始本文之前，你需要对 Scrapy 有所熟悉，知道 Items、Spider、Pipline、Selector 的概念。如果你是 Scrapy 新手，想了解如何用Scrapy开始爬取一个网站，推荐你先看看官方的教程。

运行一个Scrapy爬虫可以通过命令行的方式（scrapy runspider myspider.py）启动，也可以使用核心API通过编程的方式启动。为了获得更高的定制性和灵活性，我们主要使用后者的方式。

我们使用官方教程中的 Dmoz 例子来帮助我们理解使用编程方式启动spider。我们的 spider 文件dmoz_spider.py 长这个样子：


import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
import scrapy
 
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
 
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
 
    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
 

接下来我们需要写一个脚本run.py，来运行DmozSpider：


from dmoz_spider import DmozSpider

# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings

def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Closing reactor", level=log.INFO)
    reactor.stop()

log.start(loglevel=log.DEBUG)
settings = Settings()

# crawl responsibly
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
crawler = Crawler(settings)

# stop reactor when spider closes
crawler.signals.connect(spider_closing, signal=signals.spider_closed)

crawler.configure()
crawler.crawl(DmozSpider())
crawler.start()
reactor.run()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
from dmoz_spider import DmozSpider
 
# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
 
def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Closing reactor", level=log.INFO)
    reactor.stop()
 
log.start(loglevel=log.DEBUG)
settings = Settings()
 
# crawl responsibly
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
crawler = Crawler(settings)
 
# stop reactor when spider closes
crawler.signals.connect(spider_closing, signal=signals.spider_closed)
 
crawler.configure()
crawler.crawl(DmozSpider())
crawler.start()
reactor.run()
然后运行python run.py就启动了我们的爬虫了，但是由于我们这里没有对爬下来的结果进行任何的存储操作，所以看不到结果。你可以写一个 item pipline 用来将数据存储到数据库，使用settings.set接口将这个 pipline 配置到ITEMS_PIPLINE，我们将在第三篇文章中具体讲解这部分内容。下一篇博客将会介绍如何通过维护多个网站的爬取规则来抓取各个网站的数据。

你可以在 GitHub 上看到本文的完整项目。

注：本文使用的 Scrapy 版本是 0.24，GitHub 上的master分支已支持 Scrapy 1.0

本系列的三篇文章

Python爬虫框架Scrapy教程(1)——入门
Python爬虫框架Scrapy教程(2)—动态可配置
Python爬虫框架Scrapy教程(3)—使用Redis和SQLAlchemy对Scrapy Item去重并存储
参考资料

Running scrapy spider programmatically
