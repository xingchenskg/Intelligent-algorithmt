import time

from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By





path_driver=Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
bro=webdriver.Chrome(service=path_driver)
url1='https://www.jd.com'
bro.get(url1)
#窗口最大化
bro.maximize_window()
# time.sleep(5)
search=bro.find_element(By.XPATH,'//*[@id="key"]')
search.send_keys('平板ipad')
search.send_keys(Keys.ENTER)
time.sleep(5)
max_y=10000
y=0
while y<=max_y:
    bro.execute_script(f'window.scrollTo(0,{y})')
    y+=1000
    time.sleep(5)