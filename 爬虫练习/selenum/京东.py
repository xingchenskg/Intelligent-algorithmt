from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import xlwt
from selenium.webdriver.chrome.service import Service

url = 'https://www.jd.com/'
phone_list = []

# 创建浏览器对象
path_driver=Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
web=webdriver.Chrome(service=path_driver)
# 进行请求
web.get(url)

# 窗口最大化
web.maximize_window()

# search = web.find_element(By.XPATH, '//*[@id="key"]')
# search.send_keys('手机')
#
# # bd = web.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button')
# # bd.click()

search=web.find_element(By.XPATH,'//*[@id="key"]')
search.send_keys('平板ipad')
search.send_keys(Keys.ENTER)
time.sleep(3)
# 自动下拉
max_y = 10000
y = 0
while y <= max_y:
    web.execute_script(f'window.scrollTo(0, {y})')
    y += 1000
    time.sleep(3)

# print(web.page_source)
# title = web.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[4]/div/div[4]/a/em').text
# # print(title)
# pic = web.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[4]/div/div[1]/a/img').get_attribute('src')
# print(title, '\n', pic)

elements_list = web.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')

for element in elements_list:
    price = element.find_element(By.XPATH, './div/div[3]/strong/i').text
    name = element.find_element(By.XPATH, './div/div[4]/a/em').text
    evaluate = element.find_element(By.XPATH, './div/div[5]/strong').text
    phone_list.append([price, name, evaluate])

for i in phone_list:
    print(i)

# xls = xlwt.Workbook()
# sheet = xls.add_sheet('data')
#
# titles = ('价格', '手机信息', '评价条数')
# for index, data in enumerate(titles):
#     sheet.write(0, index, data)
#
# for i, item in enumerate(price):
#     sheet.write(i+1, 1, item)
#
# for i, item in enumerate(name):
#     sheet.write(i+1, 2, item)
#
# for i, item in enumerate(evaluate):
#     sheet.write(i+1, 3, item)
#
# xls.save('京东_手机.xls')
