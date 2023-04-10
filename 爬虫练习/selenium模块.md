selenium模块：
帮助我们便捷地获取的网站动态加载数据
便捷实现模拟登陆

	什么是selenium模块：
		基于浏览器自动化的一个模块。
	selenium使用流程：
		环境安装：pip install selenium
		下载一个浏览器的驱动程序(谷歌浏览器）
		https://chromedriver.storage.googleapis.com/index.html
	实例化一个浏览器对象
	编写基于浏览器自动化的操作代码
	from selenium import webdriver
	from time import sleep
	from lxml import etree
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service                                                 
	#实例化一个浏览器对象
	path_driver=Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
	bro=webdriver.Chrome(service=path_driver)
	#让浏览器对指定url发起一个请求
	bro.get('http://scxk.nmpa.gov.cn:81/xk/')
	#窗口最大化
	bro.maximize_window()
	#获取当前页面的源码数据
	page_text=bro.page_source
	tree=etree.HTML(page_text)
	......
	time.sleep(5)
	#关闭浏览器
	bro.quit()
	#标签定位(find_element_by_selector('.btn-search')
	searchinput=bro.find_element_by_定位标签('值'）
	#标签交互(人和浏览器交互）
	searchinput.send_key('搜索名称')
	#滚轮向下拖动
		执行一组js程序
		bro.execute_script('js代码'):此处是window.scrollTo(0,document.body.sc.ollHeight)')
	#浏览器回退
	bro.back()
	#前进
	bro.forward()
	#定位元素
	search=bro.find_element(By.XPATH,'//*[@id="kw"]')
	search.send_keys('成都大学')
	search.send_keys(Keys.ENTER)
	#执行点击操作
	bd=bro.find_element(By.XPATH,'//*[@id="kw"]')
	bd.click()

selenium处理iframe

	想要定位标签是存在iframe标签之中的则：
		bro.switch_to.fram('iframe属性值')#切换浏览器标签定位的作用域
		再来定位
		#动作链
		from selenium.webdriver import ActionChains
		action=ActionChains(bro)
		#点击长安指定的标签
		action.click_and_hold(div)
		for i in range（5）:
			#perform()立即执行动作链操作
			action.move_by_offset(17,0).perform()//x水平方向y竖直方向，	向右偏移17个像素
		sleep（0.3)
		#释放动作链
		action.release()
		#点击标签
		定位的标签.click()

cookie:用来记录客户状态
