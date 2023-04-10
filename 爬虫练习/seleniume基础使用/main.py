from selenium import webdriver
from lxml import etree
#实例化一个浏览器对象
bro=webdriver.Chrome(executable_path='./chromedriver')
#让浏览器对指定url发起一个请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
#获取当前页面的源码数据
page_text=bro.page_source
tree=etree.HTML(page_text)
