知识库特邀编辑伊海波，滴滴出行工程师，曾任龙图龙图游戏数据分析部技术负责人。CSDN博客专家，资深Python/Golang后端工程师，熟悉网络编程，关注数据分析，Web开发和Web安全。

Python前景和相关资源
如何面试Python后端工程师
Python大牛小灶福利

Python 前景

Python 有以 Django 和 Flask 的形式组合的全栈/最小框架。Django 1.10 在去年 8 月发布，为 Postgres 引入了全文搜索和一个大修改的中间件层。

十项编程语言让你在2017年实现薪酬提升

1. Java——10万2千美元
2. JavaScript——9万5千美元
3. Python——10万美元
4. C++——10万美元
5. Ruby——10万美元
6. C——10万美元
7. Swift——9万5千美元
8. C#——9万4千美元
9. 汇编语言——9万美元
10. PHP——7万5千美元

Python 知识点

GUI 图形界面
Tkinter/wxPython/PyGTK/PyQt/PySide

Web框架
django/web2py/flask/bottle/tornadoweb/webpy

科学计算
numpy/SciPy/pandas/blaze

密码学
cryptography/hashids/Paramiko/Passlib/PyCrypto/PyNacl

爬虫相关
urllib/urllib2/requests/scrapy/pyspider/portia/html2text/BeautifulSoup/lxml/selenium/mechanize/pyquery/creepy

图像处理
bigmoyan/Python Imaging Library (PIL)/pillow/Python-qrcode

自然语言处理
nltk/snownlp/Pattern/TextBlob/Polyglot/jieba

数据库驱动
mysql-python/PyMySQL/PyMongo

如何面试Python后端工程师

重点不是Python而是后端工程师，因为Python只是系统的一部分，linux基础操作，Sql，消息队列，Git要熟悉。木桶理论，每一环都不能落下，但精通其中一两个就好。

关于语言
Q ：推荐一本看过最好的Python书籍？ 考察能力，便于拉开话题
Q：谈谈python的装饰器，迭代器，yield？
Q：标准库线程安全的队列是哪一个？不安全的是哪一个？logging是线程安全的吗？
Q：Python适合的场景有哪些？当遇到计算密集型任务怎么办？
Q：python高并发解决方案？
希望听到twisted->tornado->gevent，如果你能说到golang,erlang更好
面试者可以在这里说明：Golang，Rust是否了解？numpy，pandas是什么？


关于操作系统
可以直接认为是linux，毕竟搞后端的多数是和linux打交道
Q：tcp/udp的区别？tcp粘包是怎么回事，如何处理？udp有粘包吗？
Q：time_wait是什么情况？出现过多的close_wait可能是什么原因？
Q：epoll,select的区别？边缘触发，水平触发区别？

关于存储
存储可能包含rdbms，nosql以及缓存等，以mysql,redis举例
Mysql相关
Q：谈谈mysql字符集和排序规则？
Q：varchar与char的区别是什么？大小限制？utf8字符集下varchar最多能存多少个字符
Q：primary key和unique的区别？
Q：外键有什么用，是否该用外键？外键一定需要索引吗？
Q：myisam与innodb的区别？innodb的两阶段锁定协议是什么情况？
Q：索引有什么用，大致原理是什么？设计索引有什么注意点？
关于redis相关
Q：什么场景用redis，为什么mysql不适合？
Q：谈谈redis的事务？用事务模拟原子+1操作？原子操作还有其它解决方案吗？
Q：redis内存满了会怎么样？

安全
web安全相关
Q：sql注入是怎么产生的，如何防止？
Q：xss如何预防？htmlescape后能否避免xss?
Q：csrf是什么？django是如何防范的？
密码技术
Q：什么是分组加密？加密模式有哪些？ecb和cbc模式有什么区别？为什么需要iv向量？
Q：简单说说https的过程？
Q：对称加密与非对称加密区别？
Q：如何生成共享秘钥？ 如何防范中间人攻击？
