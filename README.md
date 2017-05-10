# zhihuuser_scrapy-redis
使用scrapy-redis的分布式爬虫    
此项目是对上一个知乎爬虫项目的升级版，连接如：https://github.com/hiajianchan/zhihuSpider，此爬虫在最近运行发现会被反爬，轮询IP和Cookie也不好解决，看来知乎
的反爬能力还是很强的。所以只能降低爬取速率，但是为了不降低效率，就是用了分布式爬取。    
基本原理就是，重构scrapy队列函数和调度器，然而并不难，因为python提供的scrapy-redis模块已经帮我们解决，只需调用就好。也就是在settings.py下修改参数  如下：   
REDIS_URL = 'redis://root:密码@ip地址:端口号'            此处REDIS_URL为redis数据库所在机器的url，，，密码为登录redis数据库密码    
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"    
SCHEDULER = "scrapy_redis.scheduler.Scheduler"      
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'      
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'      
SCHEDULER_PERSIST = True         
还用重写middlewares中间件，，可以找来scrapy-redis的说明文刚看    
爬取的数据为json格式，，所以我们将数据存储到MOngoDB数据库中，，因为MongoDB不仅适合存储json数据，，而且可以很好的进行分布式存储。   

