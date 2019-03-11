# python资源汇总

- 作者：codehackfox@gmail.com
- 时间：2019-03-10 13:33:30

>## 0x00、图书链接

- [各种图书资源](https://github.com/xsoer/learn-files/tree/master/%E8%AF%AD%E8%A8%80%E7%9B%B8%E5%85%B3/python)

>## 0x01、常用库

### 01、通用库
- urllib
    * allows you access websites via your program
    * [文档](https://docs.python.org/3/library/urllib.html)
- requests -网络库
- grab – 网络库（基于pycurl）。
- pycurl – 网络库（绑定libcurl）。
- urllib3 – Python HTTP库，安全连接池、支持文件post、可用性高。
- httplib2 – 网络库。
- RoboBrowser – 一个简单的、极具Python风格的Python库，无需独立的浏览器即可浏览网页。
- MechanicalSoup -一个与网站自动交互Python库。
- mechanize -有状态、可编程的Web浏览库。
- socket – 底层网络接口(stdlib)。
- Unirest for Python – Unirest是一套可用于多种语言的轻量级的HTTP库。
- hyper – Python的HTTP/2客户端。
- PySocks – SocksiPy更新并积极维护的版本，包括错误修复和一些其他的特征。作为socket模块的直接替换。


### 02、爬虫库
- scrapy – 网络爬虫框架（基于twisted），不支持Python3。
- pyspider – 一个强大的爬虫系统。
- cola – 一个分布式爬虫框架
- portia – 基于Scrapy的可视化爬虫。
- restkit – Python的HTTP资源工具包。它可以让你轻松地访问HTTP资源，并围绕它建立的对象。
- demiurge – 基于PyQuery的爬虫微框架。


### 03、HTML/XML解析器
- lxml – C语言编写高效HTML/ XML处理库。支持XPath。
- cssselect – 解析DOM树和CSS选择器。
- pyquery – 解析DOM树和jQuery选择器。
- BeautifulSoup – 低效HTML/ XML处理库，纯Python实现。
- html5lib – 根据WHATWG规范生成HTML/ XML文档的DOM。该规范被用在现在所有的浏览器上。
- feedparser – 解析RSS/ATOM feeds。
- MarkupSafe – 为XML/HTML/XHTML提供了安全转义的字符串。
- xmltodict – 一个可以让你在处理XML时感觉像在处理JSON一样的Python模块。
- xhtml2pdf – 将HTML/CSS转换为PDF。
- untangle – 轻松实现将XML文件转换为Python对象。
- Bleach – 清理HTML（需要html5lib）。
- sanitize – 为混乱的数据世界带来清明。

### 04、文本处理
- difflib – （Python标准库）帮助进行差异化比较。
- Levenshtein – 快速计算Levenshtein距离和字符串相似度。
- fuzzywuzzy – 模糊字符串匹配。
- esmre – 正则表达式加速器。
- ftfy – 自动整理Unicode文本，减少碎片化。

### 05、自然语言处理
- NLTK -编写Python程序来处理人类语言数据的最好平台。
- Pattern – Python的网络挖掘模块。他有自然语言处理工具，机器学习以及其它。
- TextBlob – 为深入自然语言处理任务提供了一致的API。是基于NLTK以及Pattern的巨人之肩上发展的。
- jieba – 中文分词工具。
- SnowNLP – 中文文本处理库。
- loso – 另一个中文分词库。
- scikit-learn
- tensorflow
- kera


### 06、图像处理库
- matplotlib
    - [官网](https://matplotlib.org/)
    - [文档地址](https://matplotlib.org/contents.html)
    - [文档pdf版本](https://matplotlib.org/Matplotlib.pdf)
    - [中文文档](https://www.matplotlib.org.cn/index.html)
    - [总结说明](https://github.com/xsoer/interview/blob/master/%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80/python/libaray/matplotlib.md)


### 07、浏览器自动化与仿真
- selenium – 自动化真正的浏览器（Chrome浏览器，火狐浏览器，Opera浏览器，IE浏览器）。
- Ghost.py – 对PyQt的webkit的封装（需要PyQT）。
- Spynner – 对PyQt的webkit的封装（需要PyQT）。
- Splinter – 通用API浏览器模拟器（selenium web驱动，Django客户端，Zope）。

### 08、多重处理
- threading – Python标准库的线程运行。对于I/O密集型任务很有效。对于CPU绑定的任务没用，因为python GIL。
- multiprocessing – 标准的Python库运行多进程。
- celery – 基于分布式消息传递的异步任务队列/作业队列。
- concurrent-futures – concurrent-futures 模块为调用异步执行提供了一个高层次的接口。

### 09、异步
- asyncio – （在Python 3.4 +版本以上的 Python标准库）异步I/O，时间循环，协同程序和任务。
- Twisted – 基于事件驱动的网络引擎框架。
- Tornado – 一个网络框架和异步网络库。
- pulsar – Python事件驱动的并发框架。
- diesel – Python的基于绿色事件的I/O框架。
- gevent – 一个使用greenlet 的基于协程的Python网络库。
- eventlet – 有WSGI支持的异步框架。
- Tomorrow – 异步代码的奇妙的修饰语法。

### 10、队列
- celery – 基于分布式消息传递的异步任务队列/作业队列。
- huey – 小型多线程任务队列。
- mrq – Mr. Queue – 使用redis & Gevent 的Python分布式工作任务队列。
- RQ – 基于Redis的轻量级任务队列管理器。
- simpleq – 一个简单的，可无限扩展，基于Amazon SQS的队列。
- python-gearman – Gearman的Python API

### 11、云计算
- picloud – 云端执行Python代码。
- dominoup.com – 云端执行R，Python和matlab代码

### 12、网页内容提取
- newspaper – 用Python进行新闻提取、文章提取和内容策展。
- html2text – 将HTML转为Markdown格式文本。
- python-goose – HTML内容/文章提取器。
- lassie – 人性化的网页内容检索工具

### 13、WebSocket
- Crossbar – 开源的应用消息传递路由器（Python实现的用于Autobahn的WebSocket和WAMP）。
- AutobahnPython – 提供了WebSocket协议和WAMP协议的Python实现并且开源。
- WebSocket-for-Python – Python 2和3以及PyPy的WebSocket客户端和服务器库。

### 14、DNS解析
- dnsyo – 在全球超过1500个的DNS服务器上检查你的DNS。
- pycares – c-ares的接口。c-ares是进行DNS请求和异步名称决议的C语言库。

### 15、计算机视觉
- OpenCV – 开源计算机视觉库。
- SimpleCV – 用于照相机、图像处理、特征提取、格式转换的简介，可读性强的接口（基于OpenCV）。
- mahotas – 快速计算机图像处理算法（完全使用 C++ 实现），完全基于 numpy 的数组作为它的数据类型。

### 16、web框架
- Django
- Flask
- Web2py
- Tornado
- CherryPy
