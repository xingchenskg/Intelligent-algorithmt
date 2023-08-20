![](..\\png\scrapy1.png)
### scrapy的组件 ###
### 数据处理流程 ###
#### 创建项目 ####
终端：进到要创建项目的地方

	scrapy startproject 项目名称
	cd 项目名称
	scrapy genspider 文件名称（尽量英文） 网站域名（movie.douban.com)范围
pycharm:

spider(name.py).py
![](..\\png\spider(name.py).png)
拿取的直接解析
response.xpath(),.css(),.json()

	extract()提取内容（文本）
	链接的拼接detail_url=resp.urljoin(href(残缺的url))
	yield scrapy.Request(url=detail_url,callback=self.parse_detail)
	同样在本函数内可以考虑继续爬取下一页的信息。
	#进入详情页的条件是：在redis里面没有存储过该url
	1.直接往redis里set集合怼
	判断是否存在该元素
	result=self.red.sismember("tianya:ty:detail:url",detail_url)
	if result:
		print(f"该url已经被抓取过{detail_url}")
	else:
		yield scrapy.Request(
				url=detail_url,
				callback=self.parse_detail,
				)
![](..\\png\next_page.png)
	如去除在不同时间爬取相同的数据

	1.使用python的set集合来去重（关了就没有了）
	2.推荐使用redis的set集合去除重复（塞进去，就不同，塞不进去就重复的）
		1.通过url,优点：简单，缺点：如果url内部进行更新，会忽略一些数据
		2.数据。优点：准确性高，缺点：数据集庞大，对redis不利。
		from redis import Redis
		在类中
		先启动Redis
		def __init__(self,name=None,**kwargs):
			self.red=Redis(host="127.0.0.1",port=7980,db=9,password="123456")
			让父类能初始化
			super(Typider,self).__init__()#要用父类里面的方法

	
	def parse_detail(self,resp,**kwargs):
		t=nameItem()
		解析
		t['attr']=解析的数据
		yield t #此时在piplines文件中可打印
	可以导入items文件的类
		result=self.red.sadd("tianya:ty:detail:url",detail_url)#也可放到pipelines中
	
items文件中

	class ...Item（scrapy.Item):
		title= scrapy.Field()
	提取一项，选择器列表可以用extract_first()有空不报错,选择器只能用extract()
	可以先封装成字典，yield将数据传入管道，将函数变成生成器函数，减少内存，管道中item是数据
pipelines文件
![](..\\png\pipelines.png)
	可以自定义管道，但是返回，参数一样
	管道默认是不生效的，需要settings里面开启管道
	ITEM_PIPLINES={这一行取消注释里面是管道路径
![](..\\png\settings_pipelines.png)

爬虫中间件，下载器中间件	

运行项目

	scrapy crawl spider中的name
	不想看日志：
	setting文件
		：NEWSPIDER_MODULE=的下面一行加上LOG_LEVEL="WARNING"
	日志级别：DEBUG,INFO,WARNING,ERROR,CRITICAL
虚拟环境清单

	pip freeze > requirement.txt
	装别人清单：pip install -r requirement.txt
写入excel：




分布式爬虫

分布式集群

调度器
分析scrapy源码
进入scrapy源码

![](..\\png\scrapy.png)
![](..\\png\schedulerinit.png)
![](..\\png\duiliequeue.png)

消息队列
![](..\\png\queue.png)

在enqueue_request函数中的request_seen函数
![](..\\png\fingerprints.png)

fingerprints是一个创建的set()集合

![](..\\png\2.png)

分布式
![](..\\png\fenbushipachong.png)

1.和普通爬虫一样创建项目
2.修改项目

	from scrapy_redis.spider import RedisSpider,RedisCrawlSpider
	class nameSpider(RedisSpider(修改))
		#去掉起始url
		redis_key="name_start_url"
		def parse(self,resp,**kwargs):#修改参数
3.修改配置文件

	1.打开settings
		ROBOTSTXT_OBEY=Fakse
		LOG_LEVEL="WARNING"
![](..\\png\fenbushipipe.png)

其中Piplie少个e
![](..\\png\fenbushipeizhi.png)

启动多个进程

![](..\\png\fenbushiredis.png)

过滤器
![](..\\png\guolvqi.png)

![](..\\png\bitmap.png)

安装之后，在settings中配置
![](..\\png\bloomfilter.png)