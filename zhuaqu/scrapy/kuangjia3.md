Python爬虫框架Scrapy教程(3)—使用Redis和SQLAlchemy
在上篇博客中，我们讲解了如何通过维护多个网站的爬取规则来抓取各个网站的数据。本文将简要地谈谈如何使用Scrapy的Item Pipline将爬取的数据去重并存储到数据库中。

Scrapy框架的高度灵活性得益于其数据管道的架构设计，开发者可以通过简单的配置就能轻松地添加新特性。我们可以通过如下的方式添加一个pipline。


settings.set("ITEM_PIPELINES", {'pipelines.DataBasePipeline': 300})
1
settings.set("ITEM_PIPELINES", {'pipelines.DataBasePipeline': 300})
这里ITEM_PIPELINES是一个Python字典，其中key保存的pipline类在项目中的位置，value为整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内。

存储到数据库
在上一篇博客中，我们已经介绍了使用SQLAlchemy 作为我们的ORM。同样的，为了将爬取的文章保存到数据库，我们先要有一个Article模型，包含了 URL，标题，正文等字段。


from sqlalchemy import Column, String , DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    body = Column(String)
    publish_time = Column(DateTime)
    source_site = Column(String)

from sqlalchemy import Column, String , DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
class Article(Base):
    __tablename__ = 'articles'
 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    body = Column(String)
    publish_time = Column(DateTime)
    source_site = Column(String)
之后在DataBasePipeline中，我们需要生成Aticle对象，并将item中对应的字段赋给Aticle对象，最后通过SQLAlchemy将文章插入到数据库中。


from model.config import DBSession
from model.article import Article
class DataBasePipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        a = Article(title=item["title"].encode("utf-8"),
                    url=item["url"],
                    body=item["body"].encode("utf-8"),
                    publish_time=item["publish_time"].encode("utf-8"),
                    source_site=item["source_site"].encode("utf-8"))
        self.session.add(a)
        self.session.commit()

    def close_spider(self,spider):
        self.session.close()

from model.config import DBSession
from model.article import Article
class DataBasePipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()
 
    def process_item(self, item, spider):
        a = Article(title=item["title"].encode("utf-8"),
                    url=item["url"],
                    body=item["body"].encode("utf-8"),
                    publish_time=item["publish_time"].encode("utf-8"),
                    source_site=item["source_site"].encode("utf-8"))
        self.session.add(a)
        self.session.commit()
 
    def close_spider(self,spider):
        self.session.close()
 

使用Redis去重
为了防止同一个网页爬取两遍，我们使用Redis来去重，因为 Redis 作为Key/Value数据库在这个场景是非常适合的。我们认为一个URL能唯一代表一个网页。所以使用URL作为键值存储。

我们希望在存储之前就进行去重操作，所以需要更改下ITEM_PIPELINES的配置。


settings.set("ITEM_PIPELINES" , {
    'pipelines.DuplicatesPipeline': 200,
    'pipelines.DataBasePipeline': 300,
})

settings.set("ITEM_PIPELINES" , {
    'pipelines.DuplicatesPipeline': 200,
    'pipelines.DataBasePipeline': 300,
})
DuplicatesPipeline长这个样子。


from scrapy.exceptions import DropItem
from model.config import Redis

class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        if Redis.exists('url:%s' % item['url']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            Redis.set('url:%s' % item['url'],1)
            return item
from scrapy.exceptions import DropItem
from model.config import Redis
 
class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        if Redis.exists('url:%s' % item['url']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            Redis.set('url:%s' % item['url'],1)
            return item
当检测到Item已经存在，会抛出DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。

最后，运行脚本，你能看到我们的程序欢快地跑起来了。


python run.py

python run.py
你可以在 GitHub 上看到本文的完整项目。

注：本文使用的 Scrapy 版本是 0.24，GitHub 上的master分支已支持 Scrapy 1.0

本系列的三篇文章

Python爬虫框架Scrapy教程(1)——入门
Python爬虫框架Scrapy教程(2)—动态可配置
Python爬虫框架Scrapy教程(3)—使用Redis和SQLAlchemy对Scrapy Item去重并存储
参考资料

Running scrapy spider programmatically
文/wuchong
