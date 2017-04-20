Python爬虫框架Scrapy教程(2)—动态可配置
本文紧接上篇博客，在上一篇博客中我们讲解了如何使用编程的方式运行Scrapy spider。本文将讲解如何通过维护多个网站的爬取规则来抓取各个网站的数据。

具体要实现的目标是这样的，有一张Rule表用来存储各个网站的爬取规则，Scrapy获取Rule表中的记录后，针对每一条rule自动生成一个spider，每个spider去爬它们各自网站的数据。这样我们只需要维护Rule表中的规则（可以写个Web程序来维护），而不用针对上千个网站写上千个spider文件了。

我们使用 SQLAlchemy 来映射数据库，Rule表的结构如下：


from sqlalchemy import Column, String , DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    allow_domains = Column(String)
    start_urls = Column(String)
    next_page = Column(String)
    allow_url = Column(String)
    extract_from = Column(String)
    title_xpath = Column(String)
    body_xpath = Column(String)
    publish_time_xpath = Column(String)
    source_site_xpath = Column(String)
    enable = Column(Integer)
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
from sqlalchemy import Column, String , DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
class Rule(Base):
    __tablename__ = 'rules'
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    allow_domains = Column(String)
    start_urls = Column(String)
    next_page = Column(String)
    allow_url = Column(String)
    extract_from = Column(String)
    title_xpath = Column(String)
    body_xpath = Column(String)
    publish_time_xpath = Column(String)
    source_site_xpath = Column(String)
    enable = Column(Integer)
 

接下来我们要重新定制我们的spider，命名为DeepSpider，让他能够通过rule参数初始化。我们令DeepSpider继承自 CrawlSpider，一个提供了更多强大的规则(rule)来提供跟进link功能的类。deep_spider.py长这个样子：


# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Article(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    publish_time = scrapy.Field()
    source_site = scrapy.Field()

class DeepSpider(CrawlSpider):
    name = "Deep"

    def __init__(self,rule):
        self.rule = rule
        self.name = rule.name
        self.allowed_domains = rule.allow_domains.split(",")
        self.start_urls = rule.start_urls.split(",")
        rule_list = []
        #添加`下一页`的规则
        if rule.next_page:
            rule_list.append(Rule(LinkExtractor(restrict_xpaths = rule.next_page)))
        #添加抽取文章链接的规则
        rule_list.append(Rule(LinkExtractor(
            allow=[rule.allow_url],
            restrict_xpaths = [rule.extract_from]),
            callback='parse_item'))
        self.rules = tuple(rule_list)
        super(DeepSpider, self).__init__()


    def parse_item(self, response):
        self.log('Hi, this is an article page! %s' % response.url)

        article = Article()

        article["url"] = response.url

        title = response.xpath(self.rule.title_xpath).extract()
        article["title"] = title[0] if title else ""

        body = response.xpath(self.rule.body_xpath).extract()
        article["body"] =  '\n'.join(body) if body else ""

        publish_time = response.xpath(self.rule.publish_time_xpath).extract()
        article["publish_time"] = publish_time[0] if publish_time else ""

        source_site = response.xpath(self.rule.source_site_xpath).extract()
        article["source_site"] = source_site[0] if source_site else ""

        return article
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
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
 
class Article(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    publish_time = scrapy.Field()
    source_site = scrapy.Field()
 
class DeepSpider(CrawlSpider):
    name = "Deep"
 
    def __init__(self,rule):
        self.rule = rule
        self.name = rule.name
        self.allowed_domains = rule.allow_domains.split(",")
        self.start_urls = rule.start_urls.split(",")
        rule_list = []
        #添加`下一页`的规则
        if rule.next_page:
            rule_list.append(Rule(LinkExtractor(restrict_xpaths = rule.next_page)))
        #添加抽取文章链接的规则
        rule_list.append(Rule(LinkExtractor(
            allow=[rule.allow_url],
            restrict_xpaths = [rule.extract_from]),
            callback='parse_item'))
        self.rules = tuple(rule_list)
        super(DeepSpider, self).__init__()
 
 
    def parse_item(self, response):
        self.log('Hi, this is an article page! %s' % response.url)
 
        article = Article()
 
        article["url"] = response.url
 
        title = response.xpath(self.rule.title_xpath).extract()
        article["title"] = title[0] if title else ""
 
        body = response.xpath(self.rule.body_xpath).extract()
        article["body"] =  '\n'.join(body) if body else ""
 
        publish_time = response.xpath(self.rule.publish_time_xpath).extract()
        article["publish_time"] = publish_time[0] if publish_time else ""
 
        source_site = response.xpath(self.rule.source_site_xpath).extract()
        article["source_site"] = source_site[0] if source_site else ""
 
        return article
要注意的是start_urls，rules等都初始化成了对象的属性，都由传入的rule对象初始化，parse_item方法中的抽取规则也都有rule对象提供。

为了同时运行多个spider，我们需要稍稍修改上节中的运行脚本run.py，如下所示：


# -*- coding: utf-8 -*-
from spiders.deep_spider import DeepSpider
from model.config import DBSession
from model.rule import Rule

# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings


RUNNING_CRAWLERS = []

def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Spider closed: %s" % spider, level=log.INFO)
    RUNNING_CRAWLERS.remove(spider)
    if not RUNNING_CRAWLERS:
        reactor.stop()

log.start(loglevel=log.DEBUG)

settings = Settings()

# crawl settings
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")

db = DBSession()
rules = db.query(Rule).filter(Rule.enable == 1)
for rule in rules:
    crawler = Crawler(settings)
    spider = DeepSpider(rule)  # instantiate every spider using rule
    RUNNING_CRAWLERS.append(spider)

    # stop reactor when spider closes
    crawler.signals.connect(spider_closing, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()

# blocks process so always keep as the last statement
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
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
# -*- coding: utf-8 -*-
from spiders.deep_spider import DeepSpider
from model.config import DBSession
from model.rule import Rule
 
# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
 
 
RUNNING_CRAWLERS = []
 
def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Spider closed: %s" % spider, level=log.INFO)
    RUNNING_CRAWLERS.remove(spider)
    if not RUNNING_CRAWLERS:
        reactor.stop()
 
log.start(loglevel=log.DEBUG)
 
settings = Settings()
 
# crawl settings
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
 
db = DBSession()
rules = db.query(Rule).filter(Rule.enable == 1)
for rule in rules:
    crawler = Crawler(settings)
    spider = DeepSpider(rule)  # instantiate every spider using rule
    RUNNING_CRAWLERS.append(spider)
 
    # stop reactor when spider closes
    crawler.signals.connect(spider_closing, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
 
# blocks process so always keep as the last statement
reactor.run()
我们从数据库中查出启用的rules，并对于rules中每一个规则实例化一个DeepSpider对象。这儿的一个小技巧是建立了一个RUNNING_CRAWLERS列表，新建立的DeepSpider对象 spider 都会加入这个队列。在 spider 运行完毕时会调用spider_closing方法，并将该spider从RUNNING_CRAWLERS移除。最终，RUNNING_CRAWLERS中没有任何spider了，我们会停止脚本。

运行run.py后，就能对Rule表中网站进行爬取了，但是我们现在还没有对爬下来的结果进行存储，所以看不到结果。下一篇博客，我们将使用 Scrapy 提供的强大的 Pipline 对数据进行保存并去重。

现在我们可以往Rule表中加入成百上千个网站的规则，而不用添加一行代码，就可以对这成百上千个网站进行爬取。当然你完全可以做一个Web前端来完成维护Rule表的任务。当然Rule规则也可以放在除了数据库的任何地方，比如配置文件。

由于本人刚接触 Scrapy 不久，如有理解不当之处或是更好的解决方案，还请不吝赐教 :)

你可以在 GitHub 上看到本文的完整项目。

注：本文使用的 Scrapy 版本是 0.24，GitHub 上的master分支已支持 Scrapy 1.0

本系列的三篇文章

Python爬虫框架Scrapy教程(1)——入门
Python爬虫框架Scrapy教程(2)—动态可配置
Python爬虫框架Scrapy教程(3)—使用Redis和SQLAlchemy对Scrapy Item去重并存储
参考资料

Running scrapy spider programmatically
