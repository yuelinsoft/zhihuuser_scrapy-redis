# -*- coding: utf-8 -*-
import time
# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Encoding': 'gzip, deflate, sdch, br',
    #'Accept-Language': 'zh-CN,zh;q=0.8',
    #'Cache-Control': 'max-age=0',
    #'Connection': 'keep-alive',
    # #'Host': 'www.zhihu.com',
    #'Referer': 'https://www.zhihu.com/',
    #'Upgrade-Insecure-Requests': '1',
    'Cookie':'q_c1=3b9dc427dc1f4d3682d263f13d2c4fa2|1491660959000|1491660959000; d_c0="AHBC6qeOkwuPTp6hmPx7OQbTB75FUrv5ksc=|1491660960"; _zap=c14ae6f9-eace-46d3-a2e6-4e2b4437f85c; aliyungf_tc=AQAAADItonk/NQEAuhsvfXf0z8IrEd5Y; acw_tc=AQAAAPCggGMOAwMAuhsvfbJL5iIpnhNG; _xsrf=cbc6c9e07dd789e4e61fb1dc72a9c2f3; r_cap_id="YzFhYWY2MmFlNmQ2NDRhNGFkOTNlMTIyYTNiNDMxMDk=|1494247567|9c3ae614f233072d9b898affecd60a1fda7b9395"; cap_id="NmFiNTZhODhjYjJlNGY4ZTliZDQ0YzJlMDQyZmQyYmE=|1494247567|d1a9308fd2a91350ce6a0f8ff0c8681972687c1b"; l_n_c=1; __utma=51854390.434227422.1494232144.1494244675.1494247571.3; __utmb=51854390.0.10.1494247571; __utmc=51854390; __utmz=51854390.1494232144.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20170328=1^3=entry_date=20170328=1; s-q=scrapy-redis%E9%A1%B9%E7%9B%AE; s-i=4; sid=2ojbqdat; z_c0=Mi4wQUJDQ2xBaGxoUXNBY0VMcXA0NlRDeGNBQUFCaEFsVk5pZlkzV1FEdGp2dTFKUWRNQ2ZnTDN4VzA0MXFLN093Ymh3|1494249928|60777aea2bd47ef8fe343f5606b4bf4efecfd3a0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'authorization': 'Bearer Mi4wQUJDQ2xBaGxoUXNBY0VMcXA0NlRDeGNBQUFCaEFsVk5pZlkzV1FEdGp2dTFKUWRNQ2ZnTDN4VzA0MXFLN093Ymh3|1494248859|d58be97160599f4b1311b42c2a7f1907a163aa6c',
    'Host': 'www.zhihu.com',
    'x-udid': 'AHBC6qeOkwuPTp6hmPx7OQbTB75FUrv5ksc='
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'zhihuuser.pipelines.ZhihuuserPipeline': 300,
     'zhihuuser.pipelines.ZhihuuserPipeline': 300,
     'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#FILE_URL = None
#FILE_HOST = 'localhost'
#FILE_PORT = 6379
#FILTER_DB = 0
# REDIS_QUEUE_NAME = 'OneName'   # 如果不设置或者设置为None，则使用默认的，每个spider使用不同的去重队列和种子队列。如果设置了，则不同spider共用去重队列和种子队列
#设置redis
USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
REDIS_URL = 'redis://root:chj@192.168.227.130:6379'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
SCHEDULER_PERSIST = True